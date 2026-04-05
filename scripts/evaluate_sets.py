#!/usr/bin/env python3
"""Evaluate candidate sets for deduplication recommendations."""

import json
import os
import plistlib
import re
import sys
from datetime import datetime

import yaml

REPOS_DIR = "/Users/elliotj/Developer/_personal/repo-lasso/repos/autopkg"


def read_recipe(repo, rel_path):
    """Read and return recipe content as string."""
    path = os.path.join(REPOS_DIR, repo, rel_path)
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return f.read()


def parse_recipe(repo, rel_path):
    """Parse recipe file and return dict."""
    path = os.path.join(REPOS_DIR, repo, rel_path)
    if not os.path.exists(path):
        return None
    try:
        if rel_path.endswith(".yaml"):
            with open(path) as f:
                return yaml.safe_load(f)
        else:
            with open(path, "rb") as f:
                return plistlib.load(f)
    except Exception:
        return None


def get_description(recipe_dict):
    """Extract description from parsed recipe."""
    if not recipe_dict:
        return ""
    return recipe_dict.get("Description", "")


def get_input_vars(recipe_dict):
    """Extract input variables from parsed recipe."""
    if not recipe_dict:
        return {}
    return recipe_dict.get("Input", {})


def is_plist(rel_path):
    return rel_path.endswith(".recipe")


def is_yaml(rel_path):
    return rel_path.endswith(".yaml")


def source_resilience_score(source_type):
    """Score source type for resilience. Higher is better."""
    scores = {
        "github": 4,
        "sparkle": 3,
        "url": 2,
        "unknown": 1,
    }
    return scores.get(source_type, 1)


def parse_date(date_str):
    """Parse ISO date string to datetime."""
    if not date_str:
        return None
    try:
        # Handle various ISO formats
        date_str = date_str.replace("Z", "+00:00")
        return datetime.fromisoformat(date_str)
    except (ValueError, TypeError):
        return None


def evaluate_set(s):
    """Evaluate a candidate set and return evaluation dict."""
    set_id = s["id"]
    display_name = s["display_name"]
    members = s["members"]

    # Special case: different download formats (DMG vs PKG vs ZIP) are NOT redundant
    # Check if recipes download different formats from same source

    # Parse all recipes
    parsed = []
    for m in members:
        recipe = parse_recipe(m["repo"], m["rel_path"])
        desc = get_description(recipe) if recipe else ""
        input_vars = get_input_vars(recipe) if recipe else {}
        parsed.append(
            {
                **m,
                "recipe": recipe,
                "description": desc,
                "input_vars": input_vars,
                "is_plist": is_plist(m["rel_path"]),
            }
        )

    # Check for different products (skip case)
    # If recipes have very different names or descriptions, they might be different products
    # Check for different download formats from same source
    if len(members) == 2:
        m0, m1 = members[0], members[1]
        # Check if one downloads PKG and other downloads DMG from same source
        if m0.get("source_key") == m1.get("source_key") and m0["source_key"]:
            r0 = read_recipe(m0["repo"], m0["rel_path"]) or ""
            r1 = read_recipe(m1["repo"], m1["rel_path"]) or ""
            # Check for different format indicators in asset_regex
            pkg_pattern = re.compile(r"\.pkg|\.mpkg|_pkg", re.I)
            dmg_pattern = re.compile(r"\.dmg", re.I)
            zip_pattern = re.compile(r"\.zip", re.I)

            def detect_format(content):
                formats = set()
                # Look in asset_regex patterns
                for regex_match in re.finditer(r"asset_regex.*?([^\n<]+)", content):
                    regex_val = regex_match.group(1)
                    if pkg_pattern.search(regex_val):
                        formats.add("pkg")
                    if dmg_pattern.search(regex_val):
                        formats.add("dmg")
                    if zip_pattern.search(regex_val):
                        formats.add("zip")
                return formats

            f0 = detect_format(r0)
            f1 = detect_format(r1)
            if f0 and f1 and f0 != f1:
                return {
                    "set_id": set_id,
                    "recipe_type": "download",
                    "app_name": display_name,
                    "verdict": "skip",
                    "skip_reason": f"different formats ({', '.join(f0)} vs {', '.join(f1)})",
                }

    # Score each member
    scores = []
    for p in parsed:
        score = 0
        reasons = []

        # CodeSignatureVerifier: +3
        if p["has_codesig"]:
            score += 3
        else:
            reasons.append("no CodeSignatureVerifier")

        # EndOfCheckPhase: +2
        if p["has_endofcheck"]:
            score += 2
        else:
            reasons.append("no EndOfCheckPhase")

        # Architecture variable: +2
        if p["has_arch_var"]:
            score += 2
            reasons.append("has architecture variable")

        # Release variable: +1
        if p["has_release_var"]:
            score += 1
            reasons.append("has release variable")

        # Source resilience
        src_score = source_resilience_score(p["source_type"])
        score += src_score

        # Description quality
        if p["description"] and len(p["description"]) > 20:
            score += 0.5

        # Dependent count (higher = more established)
        score += min(p["dependent_count"] * 0.3, 1.5)

        # Plist preference (minor)
        if p["is_plist"]:
            score += 0.1

        scores.append(
            {
                "member": p,
                "score": score,
                "reasons": reasons,
            }
        )

    # Sort by score descending
    scores.sort(key=lambda x: x["score"], reverse=True)

    # For tiebreakers, use first_commit
    best = scores[0]
    rest = scores[1:]

    # Check if top scores are very close (within 0.5)
    if rest and abs(best["score"] - rest[0]["score"]) < 0.5:
        # Use first_commit as tiebreaker
        best_date = parse_date(best["member"]["first_commit"])
        rest_date = parse_date(rest[0]["member"]["first_commit"])
        if best_date and rest_date:
            if rest_date < best_date:
                # The rest[0] is older, swap
                best, rest[0] = rest[0], best

    # Determine confidence
    if not rest:
        confidence = "HIGH"
    else:
        score_diff = best["score"] - rest[0]["score"]
        if score_diff >= 3:
            confidence = "HIGH"
        elif score_diff >= 1:
            confidence = "MEDIUM"
        else:
            confidence = "LOW"

    # Build rationale
    rationale = []
    criteria = []

    # Shared characteristics
    shared_items = []
    all_codesig = all(m["has_codesig"] for m in members)
    all_endofcheck = all(m["has_endofcheck"] for m in members)
    same_source = len(set(m.get("source_key", "") for m in members)) == 1

    if all_codesig:
        shared_items.append("CodeSignatureVerifier")
    if all_endofcheck:
        shared_items.append("EndOfCheckPhase")
    if same_source and members[0].get("source_type"):
        src = members[0]["source_type"]
        key = members[0].get("source_key", "")
        shared_items.append(f"{src} source ({key})" if key else f"{src} source")

    if shared_items:
        rationale.append({"category": "shared", "text": "Both use " + ", ".join(shared_items)})

    # Favors keep
    keep_member = best["member"]
    keep_advantages = []
    if keep_member["has_arch_var"] and not all(m["has_arch_var"] for m in members):
        keep_advantages.append("has architecture input variable for arm64/x64 selection")
    if keep_member["has_release_var"] and not all(m["has_release_var"] for m in members):
        keep_advantages.append("has release channel input variable")
    if keep_member["has_codesig"] and not all_codesig:
        keep_advantages.append("has CodeSignatureVerifier")
    if keep_member["has_endofcheck"] and not all_endofcheck:
        keep_advantages.append("has EndOfCheckPhase")
    src_keep = source_resilience_score(keep_member["source_type"])
    for r in rest:
        src_dep = source_resilience_score(r["member"]["source_type"])
        if src_keep > src_dep:
            keep_advantages.append(
                f"more resilient source ({keep_member['source_type']}"
                f" vs {r['member']['source_type']})"
            )
            break
    if keep_member["dependent_count"] > max(
        (r["member"]["dependent_count"] for r in rest), default=0
    ):
        keep_advantages.append(f"{keep_member['dependent_count']} dependent recipes")

    if keep_advantages:
        rationale.append({"category": "favors_keep", "text": "; ".join(keep_advantages)})

    # Favors deprecate
    for r in rest:
        dep_member = r["member"]
        dep_weaknesses = []
        if not dep_member["has_codesig"] and keep_member["has_codesig"]:
            dep_weaknesses.append("no CodeSignatureVerifier")
        if not dep_member["has_endofcheck"] and keep_member["has_endofcheck"]:
            dep_weaknesses.append("no EndOfCheckPhase")
        if not dep_member["has_arch_var"] and keep_member["has_arch_var"]:
            dep_weaknesses.append("no architecture variable")
        if not dep_member["has_release_var"] and keep_member["has_release_var"]:
            dep_weaknesses.append("no release variable")
        src_dep = source_resilience_score(dep_member["source_type"])
        if src_dep < src_keep:
            dep_weaknesses.append(f"less resilient source ({dep_member['source_type']})")

        if dep_weaknesses:
            rationale.append({"category": "favors_deprecate", "text": "; ".join(dep_weaknesses)})

    # Tiebreaker
    keep_date = parse_date(keep_member["first_commit"])
    for r in rest:
        dep_date = parse_date(r["member"]["first_commit"])
        if keep_date and dep_date:
            keep_yr = keep_date.strftime("%Y-%m")
            dep_yr = dep_date.strftime("%Y-%m")
            if keep_yr != dep_yr:
                rationale.append(
                    {
                        "category": "tiebreaker",
                        "text": f"first committed {keep_yr} vs {dep_yr}",
                    }
                )

    # Criteria
    codesig_favors = None
    if not all_codesig:
        codesig_favors = "keep" if keep_member["has_codesig"] else "deprecate"
    criteria.append({"key": "codesig", "label": "CodeSignatureVerifier", "favors": codesig_favors})

    endofcheck_favors = None
    if not all_endofcheck:
        endofcheck_favors = "keep" if keep_member["has_endofcheck"] else "deprecate"
    criteria.append({"key": "endofcheck", "label": "EndOfCheckPhase", "favors": endofcheck_favors})

    arch_favors = None
    if keep_member["has_arch_var"] and not all(m["has_arch_var"] for m in members):
        arch_favors = "keep"
    elif not keep_member["has_arch_var"] and any(m["has_arch_var"] for m in members):
        arch_favors = "deprecate"
    criteria.append({"key": "arch", "label": "Multi-architecture support", "favors": arch_favors})

    release_favors = None
    if keep_member["has_release_var"] and not all(m["has_release_var"] for m in members):
        release_favors = "keep"
    elif not keep_member["has_release_var"] and any(m["has_release_var"] for m in members):
        release_favors = "deprecate"
    criteria.append(
        {
            "key": "release",
            "label": "Release channel variable",
            "favors": release_favors,
        }
    )

    src_favors = None
    if not same_source:
        if src_keep > max(source_resilience_score(r["member"]["source_type"]) for r in rest):
            src_favors = "keep"
    criteria.append(
        {"key": "source_resilience", "label": "Source resilience", "favors": src_favors}
    )

    criteria.append({"key": "metadata", "label": "Metadata quality", "favors": None})

    history_favors = None
    if keep_date:
        for r in rest:
            dep_date = parse_date(r["member"]["first_commit"])
            if dep_date and keep_date < dep_date:
                history_favors = "keep"
            elif dep_date and keep_date > dep_date:
                history_favors = "deprecate"
    criteria.append({"key": "history", "label": "Commit history", "favors": history_favors})

    format_favors = None
    if keep_member["is_plist"] and any(is_yaml(r["member"]["rel_path"]) for r in rest):
        format_favors = "keep"
    elif is_yaml(keep_member["rel_path"]) and any(r["member"]["is_plist"] for r in rest):
        format_favors = "deprecate"
    criteria.append({"key": "format", "label": "Recipe format", "favors": format_favors})

    keep_reason = []
    if keep_member["has_arch_var"]:
        keep_reason.append("multi-arch support")
    if keep_member["has_release_var"]:
        keep_reason.append("release channel variable")
    if keep_member["has_codesig"] and not all_codesig:
        keep_reason.append("has CodeSignatureVerifier")
    if keep_member["dependent_count"] > 2:
        keep_reason.append(f"{keep_member['dependent_count']} dependents")
    if not keep_reason:
        keep_date_str = parse_date(keep_member["first_commit"])
        if keep_date_str:
            keep_reason.append(f"established since {keep_date_str.strftime('%Y')}")
        else:
            keep_reason.append("better overall quality")

    dep_reasons = []
    for r in rest:
        dm = r["member"]
        dr = []
        if not dm["has_codesig"] and keep_member["has_codesig"]:
            dr.append("missing CodeSignatureVerifier")
        if not dm["has_arch_var"] and keep_member["has_arch_var"]:
            dr.append("no architecture variable")
        if not dm["has_release_var"] and keep_member["has_release_var"]:
            dr.append("no release variable")
        if not dr:
            dep_date = parse_date(dm["first_commit"])
            keep_dt = parse_date(keep_member["first_commit"])
            if dep_date and keep_dt and dep_date > keep_dt:
                dr.append(f"newer duplicate (since {dep_date.strftime('%Y')})")
            else:
                dr.append("functionally equivalent duplicate")
        dep_reasons.append(
            {"repo": dm["repo"], "rel_path": dm["rel_path"], "reason": "; ".join(dr)}
        )

    # Build deprecation message
    dep_msg = (
        f"Consider switching to {display_name} recipes in the {keep_member['repo']} repo."
        " This recipe is deprecated and will be removed in the future."
    )

    # Dependency impact
    total_deps = sum(r["member"]["dependent_count"] for r in rest)
    total_dep_repos = set()
    for r in rest:
        total_dep_repos.update(r["member"]["dependent_repos"])
    if total_deps > 0:
        dep_impact = f"{total_deps} child recipe(s) across {len(total_dep_repos)} repo(s)"
    else:
        dep_impact = "none"

    return {
        "set_id": set_id,
        "recipe_type": "download",
        "app_name": display_name,
        "verdict": "recommend",
        "confidence": confidence,
        "keep": [
            {
                "repo": keep_member["repo"],
                "rel_path": keep_member["rel_path"],
                "reason": "; ".join(keep_reason),
            }
        ],
        "deprecate": dep_reasons,
        "rationale": rationale,
        "criteria": criteria,
        "deprecation_message": dep_msg,
        "dependency_impact": dep_impact,
        "existing_prs": [],
    }


def main():
    d = json.load(open("data/candidates.json"))
    sets = d["sets"]

    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else len(sets)

    results = []
    for i in range(start, min(end, len(sets))):
        s = sets[i]
        result = evaluate_set(s)
        results.append(result)
        print(
            f"Evaluated set {i}: {s['display_name']}"
            f" -> {result['verdict']} ({result.get('confidence', 'N/A')})",
            file=sys.stderr,
        )

    json.dump(results, sys.stdout, indent=2)


if __name__ == "__main__":
    main()
