#!/usr/bin/env python3
"""Phase 1: Build candidate sets of potentially redundant AutoPkg download recipes.

Scans all repos under REPOS_DIR, parses download recipes, groups them into
candidate sets by download source and fuzzy name matching, pre-computes
git history and dependent counts, and writes structured JSON to stdout.

Requirements: pyyaml (pip install pyyaml)
"""

import argparse
import concurrent.futures
import glob
import hashlib
import json
import os
import plistlib
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

import yaml

# Where the cloned autopkg repos live. Override with --repos-dir.
DEFAULT_REPOS_DIR = Path(__file__).resolve().parent.parent.parent / "autopkg"

SKIP_PROCESSORS = {
    "EndOfCheckPhase",
    "StopProcessingIf",
    "Copier",
    "FileFinder",
    "Unarchiver",
    "PkgCopier",
    "DmgCreator",
    "CodeSignatureVerifier",
    "Versioner",
    "FileMover",
    "PathDeleter",
    "PkgExtractor",
}

VAR_PATTERN = re.compile(r"%[A-Za-z_][A-Za-z0-9_]*%")

ARCH_VARS = {
    "ARCH",
    "ARCHITECTURE",
    "DOWNLOAD_ARCH",
    "ARCH_TYPE",
    "PLATFORM_ARCH",
    "ARM_ARCHITECTURE",
    "INTEL_ARCHITECTURE",
    "SUPPORTED_ARCH",
}

RELEASE_VARS = {"RELEASE", "MAJOR_VERSION", "CHANNEL", "RELEASE_TYPE"}


def short_name(processor):
    return processor.rsplit("/", 1)[-1]


def parse_recipe(filepath):
    fp = str(filepath)
    try:
        if fp.endswith(".yaml"):
            with open(fp, encoding="utf-8") as f:
                return yaml.safe_load(f)
        else:
            with open(fp, "rb") as f:
                return plistlib.load(f)
    except Exception:
        return None


def resolve_vars(text, input_vars):
    if not text:
        return text

    def replacer(match):
        var_name = match.group(0)[1:-1]
        return str(input_vars.get(var_name, match.group(0)))

    return VAR_PATTERN.sub(replacer, text)


def normalize_url(url, input_vars=None):
    if not url:
        return None
    if input_vars:
        url = resolve_vars(url, input_vars)
    normalized = re.sub(r"^https?://", "", url)
    normalized = normalized.rstrip("/")
    normalized = normalized.lower()
    normalized = VAR_PATTERN.sub("", normalized)
    normalized = re.sub(r"/{2,}", "/", normalized)
    normalized = re.sub(r"-{2,}", "-", normalized)
    return normalized


def is_windows_recipe(recipe, filepath):
    ident = recipe.get("Identifier", "").lower()
    fp = filepath.lower()
    for marker in (
        "-win64",
        "-win32",
        "-win.",
        "win64",
        "win32",
        "-msi",
        "windows",
        ".msi",
        ".exe",
    ):
        if marker in ident or marker in os.path.basename(fp):
            return True
    desc = recipe.get("Description", "").lower()
    if "windows" in desc and "mac" not in desc:
        return True
    return False


def analyze_processors(recipe):
    """Single pass over Process list to extract all needed info."""
    processors = []
    processor_set = set()
    source_type = None
    source_key = None
    input_vars = recipe.get("Input", {})

    for step in recipe.get("Process", []):
        name = short_name(step.get("Processor", ""))
        processors.append(name)
        processor_set.add(name)

        # Extract download source from first matching processor
        if source_type is not None:
            continue
        if name in SKIP_PROCESSORS or name == "DeprecationWarning":
            continue

        args = step.get("Arguments", {})
        if name == "GitHubReleasesInfoProvider":
            repo = resolve_vars(args.get("github_repo", ""), input_vars)
            if repo and not repo.startswith("%"):
                source_type, source_key = "github", repo.lower().strip("/")
        elif name in ("SparkleUpdateInfoProvider", "AppcastURLProvider"):
            url = resolve_vars(args.get("appcast_url", ""), input_vars)
            if url and not url.startswith("%"):
                source_type, source_key = "sparkle", normalize_url(url, input_vars)
        elif name in ("URLTextSearcher", "URLDownloader", "CURLDownloader"):
            url = resolve_vars(args.get("url", ""), input_vars)
            if url and not url.startswith("%"):
                source_type, source_key = "url", normalize_url(url, input_vars)
        elif name not in SKIP_PROCESSORS:
            source_type, source_key = "unknown", f"processor:{name}"

    return processors, processor_set, source_type, source_key


def should_skip(processor_set, recipe, filepath):
    if "DeprecationWarning" in processor_set:
        return "deprecated"
    if "PackageRequired" in processor_set:
        return "package_required"
    parent = recipe.get("ParentRecipe", "")
    if parent and ".download." in parent:
        return "child_of_download"
    if is_windows_recipe(recipe, filepath):
        return "windows"
    return None


def get_app_name(recipe, filepath):
    name = recipe.get("Input", {}).get("NAME", "")
    if not name or name.startswith("%"):
        ident = recipe.get("Identifier", "")
        parts = ident.split(".")
        if parts:
            name = parts[-1]
    name = name.lower().strip()
    name = re.sub(r"[^a-z0-9]", "", name)
    return name


def get_display_name(recipe):
    name = recipe.get("Input", {}).get("NAME", "")
    if name and not name.startswith("%"):
        return name
    ident = recipe.get("Identifier", "")
    parts = ident.split(".")
    return parts[-1] if parts else ""


def get_repo_name(filepath, base):
    rel = os.path.relpath(filepath, base)
    return rel.split(os.sep)[0]


def get_rel_path(filepath, base):
    rel = os.path.relpath(filepath, base)
    parts = rel.split(os.sep)
    return "/".join(parts[1:])


def git_first_commit(filepath, base):
    repo_name = get_repo_name(filepath, base)
    repo_dir = os.path.join(base, repo_name)
    rel = get_rel_path(filepath, base)
    try:
        result = subprocess.run(
            ["git", "log", "--follow", "--diff-filter=A", "--format=%aI", "--", rel],
            cwd=repo_dir,
            capture_output=True,
            text=True,
            timeout=10,
        )
        lines = result.stdout.strip().split("\n")
        return lines[-1] if lines and lines[-1] else None
    except Exception:
        return None


def find_worktree_dirs(base):
    """Find directories under base whose .git is a file (i.e. git worktrees).

    Stops descending at any repo boundary (.git file or directory) to avoid
    walking through repo internals.
    """
    worktree_dirs = set()

    def walk(d):
        try:
            entries = list(os.scandir(d))
        except OSError:
            return
        for entry in entries:
            if entry.name == ".git":
                if entry.is_file(follow_symlinks=False):
                    worktree_dirs.add(d)
                return
        for entry in entries:
            if entry.is_dir(follow_symlinks=False):
                walk(entry.path)

    walk(str(base))
    return worktree_dirs


def is_under_any(filepath, dirs):
    fp = os.path.abspath(filepath)
    for d in dirs:
        prefix = d if d.endswith(os.sep) else d + os.sep
        if fp.startswith(prefix):
            return True
    return False


def build_parent_index(all_recipe_files, base):
    """Build a one-pass index of ParentRecipe -> list of (repo,) for dependent counting."""
    index = defaultdict(lambda: {"count": 0, "repos": set()})
    for fp in all_recipe_files:
        try:
            data = parse_recipe(fp)
            if data is None:
                continue
            parent = data.get("ParentRecipe", "")
            if parent:
                repo = get_repo_name(fp, base)
                index[parent]["count"] += 1
                index[parent]["repos"].add(repo)
        except Exception:
            pass
    return index


def make_set_id(members):
    idents = sorted(set(m["identifier"] for m in members))
    raw = "|".join(idents)
    return hashlib.sha256(raw.encode()).hexdigest()[:12]


def main():
    parser = argparse.ArgumentParser(description="Build candidate sets for deduplication")
    parser.add_argument(
        "--repos-dir",
        type=Path,
        default=DEFAULT_REPOS_DIR,
        help="Directory containing cloned autopkg repos",
    )
    parser.add_argument(
        "--output", "-o", type=str, default="-", help="Output file (default: stdout)"
    )
    parser.add_argument(
        "--skip-git",
        action="store_true",
        help="Skip git history lookups (faster for testing)",
    )
    parser.add_argument(
        "--skip-dependents",
        action="store_true",
        help="Skip dependent counting (faster for testing)",
    )
    args = parser.parse_args()

    base = args.repos_dir

    # Identify git worktrees so we can exclude them — they duplicate recipes
    # already counted in the primary clone.
    worktree_dirs = find_worktree_dirs(base)
    if worktree_dirs:
        print(f"Excluding {len(worktree_dirs)} git worktree(s)", file=sys.stderr)

    # Find all recipe files (not just download) for dependent counting
    all_recipe_files = []
    for pattern in ["**/*.recipe", "**/*.recipe.yaml", "**/*.recipe.plist"]:
        all_recipe_files.extend(glob.glob(str(base / pattern), recursive=True))
    if worktree_dirs:
        all_recipe_files = [fp for fp in all_recipe_files if not is_under_any(fp, worktree_dirs)]
    print(f"Found {len(all_recipe_files)} total recipe files", file=sys.stderr)

    # Find download recipes
    dl_patterns = [
        str(base / "**" / "*.download.recipe"),
        str(base / "**" / "*.download.recipe.yaml"),
        str(base / "**" / "*.download.recipe.plist"),
    ]
    all_files = []
    for pat in dl_patterns:
        all_files.extend(glob.glob(pat, recursive=True))
    if worktree_dirs:
        all_files = [fp for fp in all_files if not is_under_any(fp, worktree_dirs)]
    print(f"Found {len(all_files)} download recipe files", file=sys.stderr)

    # Parse and categorize (single pass over Process list per recipe)
    recipes = []
    skipped = defaultdict(int)
    parse_errors = 0

    for fp in sorted(all_files):
        data = parse_recipe(fp)
        if data is None:
            parse_errors += 1
            continue

        processors, processor_set, source_type, source_key = analyze_processors(data)

        skip_reason = should_skip(processor_set, data, fp)
        if skip_reason:
            skipped[skip_reason] += 1
            continue

        app_name = get_app_name(data, fp)
        repo = get_repo_name(fp, base)
        input_vars = data.get("Input", {})

        recipes.append(
            {
                "path": fp,
                "repo": repo,
                "rel_path": get_rel_path(fp, base),
                "identifier": data.get("Identifier", ""),
                "description": data.get("Description", ""),
                "app_name": app_name,
                "display_name": get_display_name(data),
                "source_type": source_type,
                "source_key": source_key,
                "has_codesig": "CodeSignatureVerifier" in processor_set,
                "has_endofcheck": "EndOfCheckPhase" in processor_set,
                "format": "yaml" if fp.endswith(".yaml") else "plist",
                "input_vars": list(input_vars.keys()),
                "has_arch_var": bool(ARCH_VARS & set(input_vars.keys())),
                "has_release_var": bool(RELEASE_VARS & set(input_vars.keys())),
                "processors": processors,
            }
        )

    print(
        f"Parsed {len(recipes)} recipes (skipped: {dict(skipped)}, errors: {parse_errors})",
        file=sys.stderr,
    )

    # Group by download source
    source_groups = defaultdict(list)
    ungrouped = []
    for r in recipes:
        if r["source_type"] and r["source_key"] and r["source_type"] != "unknown":
            key = f"{r['source_type']}:{r['source_key']}"
            source_groups[key].append(r)
        else:
            ungrouped.append(r)

    # Sub-group by app name to avoid collapsing different products
    candidate_sets = {}
    for key, members in source_groups.items():
        name_subgroups = defaultdict(list)
        for m in members:
            name_subgroups[m["app_name"]].append(m)
        for name, subgroup in name_subgroups.items():
            repos = set(m["repo"] for m in subgroup)
            if len(repos) >= 2:
                subkey = f"{key}|{name}" if name else key
                candidate_sets[subkey] = subgroup

    print(f"Source-matched candidate sets: {len(candidate_sets)}", file=sys.stderr)

    # Fuzzy name matching
    all_by_name = defaultdict(list)
    for r in recipes:
        if r["app_name"]:
            all_by_name[r["app_name"]].append(r)

    fuzzy_sets = {}
    for name, members in all_by_name.items():
        repos = set(m["repo"] for m in members)
        if len(repos) >= 2:
            already_covered = False
            for key, existing in candidate_sets.items():
                existing_paths = set(m["path"] for m in existing)
                member_paths = set(m["path"] for m in members)
                if member_paths.issubset(existing_paths):
                    already_covered = True
                    break
            if not already_covered:
                fuzzy_sets[f"name:{name}"] = members

    print(f"Fuzzy name-matched additional sets: {len(fuzzy_sets)}", file=sys.stderr)

    # Pairwise similarity for ungrouped
    similarity_sets = defaultdict(list)
    ungrouped_names = [(r, r["app_name"]) for r in ungrouped if r["app_name"]]
    matched_indices = set()
    for i, (r1, n1) in enumerate(ungrouped_names):
        if i in matched_indices:
            continue
        group = [r1]
        for j, (r2, n2) in enumerate(ungrouped_names):
            if j <= i or j in matched_indices or r1["repo"] == r2["repo"]:
                continue
            if SequenceMatcher(None, n1, n2).ratio() >= 0.85:
                group.append(r2)
                matched_indices.add(j)
        if len(group) >= 2:
            matched_indices.add(i)
            similarity_sets[f"similar:{n1}"] = group

    print(f"Similarity-matched additional sets: {len(similarity_sets)}", file=sys.stderr)

    # Union-find merge
    all_sets = {}
    all_sets.update(candidate_sets)
    all_sets.update(fuzzy_sets)
    all_sets.update(similarity_sets)

    path_to_set_keys = defaultdict(set)
    for key, members in all_sets.items():
        for m in members:
            path_to_set_keys[m["path"]].add(key)

    uf_parent = {k: k for k in all_sets}

    def find(x):
        while uf_parent[x] != x:
            uf_parent[x] = uf_parent[uf_parent[x]]
            x = uf_parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            uf_parent[ra] = rb

    for path, keys in path_to_set_keys.items():
        keys = list(keys)
        for i in range(1, len(keys)):
            union(keys[0], keys[i])

    components = defaultdict(set)
    for key in all_sets:
        components[find(key)].add(key)

    merged_sets = {}
    for root, keys in components.items():
        best_key = sorted(keys, key=lambda k: (k.startswith("name:"), k.startswith("similar:"), k))[
            0
        ]
        seen_paths = set()
        merged_members = []
        for key in keys:
            for m in all_sets[key]:
                if m["path"] not in seen_paths:
                    seen_paths.add(m["path"])
                    merged_members.append(m)
        repos = set(m["repo"] for m in merged_members)
        if len(repos) >= 2:
            merged_sets[best_key] = merged_members

    all_sets = merged_sets
    print(f"After merging overlapping sets: {len(all_sets)}", file=sys.stderr)

    # Enrich with git history (parallelized)
    if not args.skip_git:
        print("Computing git first-commit dates...", file=sys.stderr)
        all_members = [
            (key, i, m) for key, members in all_sets.items() for i, m in enumerate(members)
        ]
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            futures = {
                pool.submit(git_first_commit, m["path"], base): (key, i)
                for key, i, m in all_members
            }
            for future in concurrent.futures.as_completed(futures):
                key, i = futures[future]
                all_sets[key][i]["first_commit"] = future.result()
    else:
        for members in all_sets.values():
            for m in members:
                m["first_commit"] = None

    # Enrich with dependent counts (single-pass index)
    if not args.skip_dependents:
        print("Building ParentRecipe index...", file=sys.stderr)
        parent_index = build_parent_index(all_recipe_files, base)
        for members in all_sets.values():
            for m in members:
                entry = parent_index.get(m["identifier"], {"count": 0, "repos": set()})
                m["dependent_count"] = entry["count"]
                m["dependent_repos"] = sorted(entry["repos"])
    else:
        for members in all_sets.values():
            for m in members:
                m["dependent_count"] = 0
                m["dependent_repos"] = []

    # Build output
    output_sets = []
    for key, members in sorted(all_sets.items()):
        set_id = make_set_id(members)
        display_names = [m["display_name"] for m in members if m["display_name"]]
        display_name = (
            max(set(display_names), key=display_names.count)
            if display_names
            else members[0]["app_name"]
        )

        output_sets.append(
            {
                "id": set_id,
                "source_key": key,
                "display_name": display_name,
                "app_name": members[0]["app_name"],
                "members": [
                    {
                        "repo": m["repo"],
                        "rel_path": m["rel_path"],
                        "identifier": m["identifier"],
                        "description": m["description"],
                        "source_type": m["source_type"],
                        "source_key": m["source_key"],
                        "has_codesig": m["has_codesig"],
                        "has_endofcheck": m["has_endofcheck"],
                        "has_arch_var": m["has_arch_var"],
                        "has_release_var": m["has_release_var"],
                        "format": m["format"],
                        "input_vars": m["input_vars"],
                        "processors": m["processors"],
                        "first_commit": m["first_commit"],
                        "dependent_count": m["dependent_count"],
                        "dependent_repos": m["dependent_repos"],
                    }
                    for m in members
                ],
            }
        )

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repos_dir": str(base),
        "stats": {
            "total_download_files": len(all_files),
            "parsed": len(recipes),
            "skipped": dict(skipped),
            "parse_errors": parse_errors,
            "candidate_sets": len(output_sets),
        },
        "sets": output_sets,
    }

    out_text = json.dumps(output, indent=2)
    if args.output == "-":
        print(out_text)
    else:
        with open(args.output, "w") as f:
            f.write(out_text)
        print(f"Wrote {args.output}: {len(output_sets)} candidate sets", file=sys.stderr)


if __name__ == "__main__":
    main()
