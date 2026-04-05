#!/usr/bin/env python3
"""Check GitHub PRs for deduplication-related activity.

For each repo that has tracked recipes, searches for deprecation PRs and
matches them to tracked recipe files. Merges with manually-specified PRs
from override_sets.json. Writes pr_status.json.

Requires: gh CLI (authenticated)
"""

import json
import re
import subprocess
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def normalize_pr_state(raw_state):
    """Map GitHub PR state strings to our canonical states."""
    state = raw_state.lower()
    if state == "merged":
        return "merged"
    if state == "closed":
        return "closed"
    return "open"


def gh_fetch_prs(repo):
    """Fetch all PRs from a repo and filter locally for deprecation PRs.

    GitHub's search indexing is unreliable on small/inactive repos, so we
    fetch all PRs and match the title ourselves.
    """
    try:
        result = subprocess.run(
            [
                "gh",
                "pr",
                "list",
                "--repo",
                f"autopkg/{repo}",
                "--state",
                "all",
                "--json",
                "number,title,state,url,files",
                "--limit",
                "100",
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0 or not result.stdout.strip():
            return repo, []
        prs = json.loads(result.stdout)
        filtered = [pr for pr in prs if "deprecat" in pr.get("title", "").lower()]
        return repo, filtered
    except Exception as e:
        print(f"  gh error for {repo}: {e}", file=sys.stderr)
        return repo, []


def gh_view_pr(pr_repo, pr_num):
    """Fetch a single PR's current state."""
    try:
        result = subprocess.run(
            [
                "gh",
                "pr",
                "view",
                str(pr_num),
                "--repo",
                f"autopkg/{pr_repo}",
                "--json",
                "title,state,url",
            ],
            capture_output=True,
            text=True,
            timeout=15,
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except Exception:
        pass
    return None


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Check PR status for dedup sets")
    parser.add_argument("--candidates", type=Path, default=ROOT / "data" / "candidates.json")
    parser.add_argument("--overrides", type=Path, default=ROOT / "data" / "override_sets.json")
    parser.add_argument("--output", "-o", type=Path, default=ROOT / "data" / "pr_status.json")
    parser.add_argument("--workers", type=int, default=8, help="Number of parallel gh requests")
    args = parser.parse_args()

    # Load candidates to know which repos and files to check
    with open(args.candidates) as f:
        candidates = json.load(f)

    # Build map: repo -> set of tracked recipe paths
    repo_paths = defaultdict(set)
    # And: (repo, rel_path) -> list of set_ids
    path_to_sets = defaultdict(list)
    for s in candidates["sets"]:
        for m in s["members"]:
            repo_paths[m["repo"]].add(m["rel_path"])
            path_to_sets[(m["repo"], m["rel_path"])].append(s["id"])

    # Load manual PR overrides
    override_prs = {}  # set_display_name -> list of PR URLs
    if args.overrides.exists():
        with open(args.overrides) as f:
            overrides = json.load(f)
        for name, entry in overrides.items():
            if "prs" in entry:
                override_prs[name.lower()] = entry["prs"]

    # Search repos for deprecation PRs in parallel
    repos = sorted(repo_paths.keys())
    print(
        f"Checking {len(repos)} repos for deprecation PRs ({args.workers} workers)...",
        file=sys.stderr,
    )
    found_prs = {}  # set_id -> list of PR info dicts

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(gh_fetch_prs, repo): repo for repo in repos}
        for future in as_completed(futures):
            repo, prs = future.result()
            if not prs:
                continue
            print(f"  {repo}: {len(prs)} deprecation PR(s)", file=sys.stderr)

            for pr in prs:
                pr_number = pr["number"]
                state = normalize_pr_state(pr["state"])

                # Check which tracked files this PR touches
                pr_files = [f["path"] for f in pr.get("files", [])] if pr.get("files") else []
                matched_sets = set()
                for pf in pr_files:
                    for set_id in path_to_sets.get((repo, pf), []):
                        matched_sets.add(set_id)

                for set_id in matched_sets:
                    if set_id not in found_prs:
                        found_prs[set_id] = []
                    found_prs[set_id].append(
                        {
                            "repo": repo,
                            "number": pr_number,
                            "title": pr["title"],
                            "url": pr["url"],
                            "state": state,
                        }
                    )

    # Merge manual override PRs (fetch state in parallel)
    name_to_set_id = {}
    for s in candidates["sets"]:
        name_to_set_id[s["display_name"].lower()] = s["id"]
        name_to_set_id[s["app_name"].lower()] = s["id"]

    override_tasks = []  # (set_id, url, pr_repo, pr_num)
    for name, pr_urls in override_prs.items():
        set_id = name_to_set_id.get(name)
        if not set_id:
            print(
                f"  Warning: override PR for '{name}' doesn't match any set",
                file=sys.stderr,
            )
            continue
        if set_id not in found_prs:
            found_prs[set_id] = []
        for url in pr_urls:
            if any(p["url"] == url for p in found_prs[set_id]):
                continue
            match = re.match(r"https://github\.com/autopkg/([^/]+)/pull/(\d+)", url)
            if match:
                override_tasks.append((set_id, url, match.group(1), int(match.group(2))))
            else:
                found_prs[set_id].append({"url": url, "state": "unknown", "source": "override"})

    if override_tasks:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {
                pool.submit(gh_view_pr, pr_repo, pr_num): (set_id, url, pr_repo, pr_num)
                for set_id, url, pr_repo, pr_num in override_tasks
            }
            for future in as_completed(futures):
                set_id, url, pr_repo, pr_num = futures[future]
                pr_data = future.result()
                if pr_data:
                    found_prs[set_id].append(
                        {
                            "repo": pr_repo,
                            "number": pr_num,
                            "title": pr_data.get("title", ""),
                            "url": pr_data.get("url", url),
                            "state": normalize_pr_state(pr_data["state"]),
                            "source": "override",
                        }
                    )
                else:
                    found_prs[set_id].append({"url": url, "state": "unknown", "source": "override"})

    # Write output
    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "prs_by_set": found_prs,
        "total_prs_found": sum(len(v) for v in found_prs.values()),
        "sets_with_prs": len(found_prs),
    }

    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)

    print(
        f"Found {output['total_prs_found']} PRs across {output['sets_with_prs']} sets",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
