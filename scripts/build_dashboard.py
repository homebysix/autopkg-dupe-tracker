#!/usr/bin/env python3
"""Assemble dashboard data from candidates, evaluations, overrides, PR status, and repo flags.

Merges five data sources into a single docs/dashboard.json for the dashboard:
  1. data/candidates.json     — what sets exist (auto-generated)
  2. data/evaluations/*.json  — LLM recommendations (committed manually)
  3. data/override_sets.json      — human exceptions and manual PR links
  4. data/pr_status.json      — live PR states (auto-generated)
  5. data/override_repos.json     — repo-level flags (e.g., never_keep)
"""

import glob
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_json(path, default=None):
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return default


def load_evaluations(eval_dir):
    """Load all evaluation files, latest per set_id wins."""
    evals = {}  # set_id -> evaluation dict
    files = sorted(glob.glob(str(eval_dir / "*.json")))
    for fp in files:
        try:
            with open(fp) as f:
                data = json.load(f)
            # Handle both array and dict formats
            entries = (
                data if isinstance(data, list) else data.get("sets", data.get("evaluations", []))
            )
            for entry in entries:
                set_id = entry.get("set_id")
                if set_id:
                    evals[set_id] = entry
        except Exception as e:
            print(f"Warning: could not load {fp}: {e}", file=sys.stderr)
    return evals


def determine_action_status(evaluation, prs, override):
    """Determine the action status for a set."""
    # Override decisions take precedence
    if override:
        decision = override.get("decision", "")
        if decision in ("wont_fix", "exception", "deferred"):
            return decision

    # Check PR states
    if prs:
        has_merged = any(pr.get("state") == "merged" for pr in prs)
        has_open = any(pr.get("state") == "open" for pr in prs)
        if has_merged:
            return "resolved"
        if has_open:
            return "pr_open"

    # Fall back to evaluation confidence
    if evaluation:
        return "needs_pr"

    # No evaluation yet
    return "needs_evaluation"


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Build dashboard JSON")
    parser.add_argument("--output", "-o", type=Path, default=ROOT / "docs" / "dashboard.json")
    args = parser.parse_args()

    candidates = load_json(ROOT / "data" / "candidates.json")
    if not candidates:
        print("Error: data/candidates.json not found", file=sys.stderr)
        sys.exit(1)

    evaluations = load_evaluations(ROOT / "data" / "evaluations")
    overrides = load_json(ROOT / "data" / "override_sets.json", {})
    pr_status = load_json(ROOT / "data" / "pr_status.json", {})
    repo_flags = load_json(ROOT / "data" / "override_repos.json", {})

    # Strip example entries from repo_flags
    repo_flags = {k: v for k, v in repo_flags.items() if not k.startswith("_")}

    prs_by_set = pr_status.get("prs_by_set", {})

    # Build name->override lookup (case-insensitive)
    override_lookup = {k.lower(): v for k, v in overrides.items()}

    # Assemble dashboard data
    sets = []
    repos_involved = set()
    stats = {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "SKIP": 0, "RESOLVED": 0}

    for candidate in candidates["sets"]:
        set_id = candidate["id"]
        display_name = candidate["display_name"]
        evaluation = evaluations.get(set_id)
        override = override_lookup.get(display_name.lower())
        prs = prs_by_set.get(set_id, [])

        # Also check overrides for manual PR links
        if override and "prs" in override:
            for url in override["prs"]:
                if not any(p.get("url") == url for p in prs):
                    prs.append({"url": url, "state": "unknown", "source": "override"})

        action_status = determine_action_status(evaluation, prs, override)

        # Build the dashboard entry
        entry = {
            "id": set_id,
            "app_name": display_name,
            "action_status": action_status,
            "existing_prs": prs,
            "member_count": len(candidate["members"]),
            "members_summary": [
                {
                    "repo": m["repo"],
                    "rel_path": m["rel_path"],
                    "has_codesig": m["has_codesig"],
                    "has_endofcheck": m["has_endofcheck"],
                    "has_arch_var": m["has_arch_var"],
                    "dependent_count": m["dependent_count"],
                }
                for m in candidate["members"]
            ],
        }

        if evaluation and evaluation.get("verdict") == "skip":
            entry["confidence"] = "SKIP"
            entry["skip_reason"] = evaluation.get("skip_reason", "")
            entry["keep"] = []
            entry["deprecate"] = []
            entry["rationale"] = ""
            entry["criteria"] = []
            entry["deprecation_message"] = ""
            entry["dependency_impact"] = ""
            stats["SKIP"] += 1
        elif evaluation and evaluation.get("verdict") == "recommend":
            conf = evaluation.get("confidence", "MEDIUM")
            entry["confidence"] = conf
            entry["keep"] = evaluation.get("keep", [])
            entry["deprecate"] = evaluation.get("deprecate", [])
            entry["rationale"] = evaluation.get("rationale", "")
            entry["criteria"] = evaluation.get("criteria", [])
            entry["deprecation_message"] = evaluation.get("deprecation_message", "")
            entry["dependency_impact"] = evaluation.get("dependency_impact", "")
            stats[conf] = stats.get(conf, 0) + 1
            if action_status == "resolved":
                stats["RESOLVED"] += 1
        else:
            # No evaluation yet — show as unevaluated candidate
            entry["confidence"] = "UNEVALUATED"
            entry["keep"] = []
            entry["deprecate"] = []
            entry["rationale"] = ""
            entry["criteria"] = []
            entry["deprecation_message"] = ""
            entry["dependency_impact"] = ""
            # Include candidate metadata so the dashboard can show what's known
            entry["candidate_members"] = [
                {
                    "repo": m["repo"],
                    "rel_path": m["rel_path"],
                    "identifier": m["identifier"],
                    "has_codesig": m["has_codesig"],
                    "has_endofcheck": m["has_endofcheck"],
                    "has_arch_var": m["has_arch_var"],
                    "source_type": m["source_type"],
                }
                for m in candidate["members"]
            ]

        # Apply override annotations
        if override:
            entry["override"] = {
                "decision": override.get("decision", ""),
                "reason": override.get("reason", ""),
                "date": override.get("date", ""),
            }
            if override.get("override_keep"):
                entry["override"]["override_keep"] = override["override_keep"]

        # Check repo flags against this set's members
        flagged_repos = []
        for m in candidate["members"]:
            repo = m["repo"]
            if repo in repo_flags:
                flag_info = repo_flags[repo]
                flagged_repos.append(
                    {
                        "repo": repo,
                        "flag": flag_info.get("flag", ""),
                        "reason": flag_info.get("reason", ""),
                        "action": flag_info.get("action", ""),
                        "date": flag_info.get("date", ""),
                    }
                )
        if flagged_repos:
            entry["repo_flags"] = flagged_repos
            # Check if the recommended "keep" is in a flagged repo
            keep_repos = {m.get("repo") for m in entry.get("keep", [])}
            flagged_keep = [
                f for f in flagged_repos if f["repo"] in keep_repos and f["flag"] == "never_keep"
            ]
            if flagged_keep:
                entry["needs_reassessment"] = True
                entry["reassessment_reason"] = (
                    f"Recommended keeper is in {flagged_keep[0]['repo']} "
                    f"({flagged_keep[0]['reason']})"
                )

        for m in entry.get("keep", []) + entry.get("deprecate", []):
            repos_involved.add(m.get("repo", ""))
        for m in candidate["members"]:
            repos_involved.add(m["repo"])

        sets.append(entry)

    repos_involved.discard("")

    needs_reassessment = sum(1 for s in sets if s.get("needs_reassessment"))
    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stats": stats,
        "total_sets": len(sets),
        "needs_reassessment": needs_reassessment,
        "repos_involved": sorted(repos_involved),
        "repo_flags": {
            k: {
                "flag": v.get("flag", ""),
                "reason": v.get("reason", ""),
                "action": v.get("action", ""),
                "date": v.get("date", ""),
            }
            for k, v in repo_flags.items()
        },
        "sets": sets,
    }

    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)

    print(
        f"Built {args.output}: {len(sets)} sets "
        f"({stats['HIGH']} HIGH, {stats['MEDIUM']} MEDIUM, {stats['LOW']} LOW, "
        f"{stats['SKIP']} SKIP, {stats['RESOLVED']} resolved)",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
