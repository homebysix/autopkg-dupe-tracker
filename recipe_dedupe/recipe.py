import glob
import os
import plistlib
import re
import subprocess
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse

import yaml

from .models import RecipeRecord

VAR_PATTERN = re.compile(r"%[A-Za-z_][A-Za-z0-9_]*%")
FORMAT_PATTERN = re.compile(r"\.(dmg|pkg|mpkg|zip|tar|tgz|tbz2?|bz2|gz)\b", re.I)
BARE_EXT_PATTERN = re.compile(r"^(dmg|pkg|zip|tar|tgz|tbz2?|bz2|gz)$", re.I)

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

SKIP_SOURCE_PROCESSORS = {
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
    "DeprecationWarning",
}


def short_name(processor):
    return (processor or "").rsplit("/", 1)[-1]


def parse_recipe_file(path):
    try:
        if str(path).endswith(".yaml"):
            with open(path, encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
        with open(path, "rb") as f:
            return plistlib.load(f) or {}
    except Exception:
        return {}


def resolve_vars(text, input_vars):
    if not text:
        return text

    def replace(match):
        name = match.group(0)[1:-1]
        return str(input_vars.get(name, match.group(0)))

    return VAR_PATTERN.sub(replace, str(text))


def normalize_name(text):
    text = (text or "").lower().strip()
    text = re.sub(r"\b(download|pkg|install|munki|recipe)\b", "", text)
    return re.sub(r"[^a-z0-9]+", "", text)


def display_name(recipe):
    name = recipe.get("Input", {}).get("NAME")
    if name and not str(name).startswith("%"):
        return str(name)
    ident = recipe.get("Identifier", "")
    return ident.split(".")[-1] if ident else ""


def normalize_url(url, input_vars):
    url = resolve_vars(url, input_vars)
    if not url or str(url).startswith("%"):
        return None, None
    parsed = urlparse(str(url))
    if not parsed.netloc:
        return None, None
    domain = parsed.netloc.lower()
    path = re.sub(r"/{2,}", "/", parsed.path.rstrip("/"))
    key = f"{domain}{path}".lower()
    key = VAR_PATTERN.sub("{var}", key)
    return key, domain


def extract_source(recipe, processors):
    input_vars = recipe.get("Input", {})
    for step in recipe.get("Process", []) or []:
        name = short_name(step.get("Processor"))
        if name in SKIP_SOURCE_PROCESSORS:
            continue
        args = step.get("Arguments", {}) or {}
        if name == "GitHubReleasesInfoProvider":
            repo = resolve_vars(args.get("github_repo", ""), input_vars)
            if repo and not str(repo).startswith("%"):
                repo = str(repo).lower().strip("/")
                return "github", repo, "github.com"
        if name in ("SparkleUpdateInfoProvider", "AppcastURLProvider"):
            key, domain = normalize_url(args.get("appcast_url", ""), input_vars)
            if key:
                return "sparkle", key, domain
        if name in ("URLTextSearcher", "URLDownloader", "CURLDownloader"):
            key, domain = normalize_url(args.get("url", ""), input_vars)
            if key:
                return "url", key, domain
        return "unknown", f"processor:{name}", None
    return None, None, None


def extract_codesig_authorities(recipe):
    authorities = []
    for step in recipe.get("Process", []) or []:
        if short_name(step.get("Processor")) != "CodeSignatureVerifier":
            continue
        args = step.get("Arguments", {}) or {}
        raw = args.get("requirement") or args.get("expected_authority_names") or ""
        if isinstance(raw, list):
            authorities.extend(str(item) for item in raw)
        else:
            authorities.extend(re.findall(r'certificate\s+\d+\[[^\]]+\]\s*=\s*"([^"]+)"', str(raw)))
            if not authorities and raw:
                authorities.append(str(raw))
    return sorted({a.strip() for a in authorities if a and a.strip()})


_ARG_KEYS = (
    "url",
    "appcast_url",
    "asset_regex",
    "filename",
    "download_path",
    "re_pattern",
    "pattern",
)
_FORMAT_ALIASES = {"mpkg": "pkg", "tbz": "tbz2"}


def extract_formats(recipe):
    found = set()

    for val in (recipe.get("Input") or {}).values():
        text = str(val)
        stripped = text.strip()
        for m in FORMAT_PATTERN.finditer(text):
            found.add(m.group(1).lower())
        if BARE_EXT_PATTERN.match(stripped):
            found.add(stripped.lower())

    for step in recipe.get("Process", []) or []:
        name = short_name(step.get("Processor"))
        args = step.get("Arguments") or {}

        for key in _ARG_KEYS:
            if key in args:
                for m in FORMAT_PATTERN.finditer(str(args[key])):
                    found.add(m.group(1).lower())

        if name == "Unarchiver":
            archive = str(args.get("archive_path") or args.get("source_path") or "")
            m = FORMAT_PATTERN.search(archive)
            found.add(m.group(1).lower() if m else "zip")

        if name == "AppDmgVersioner":
            found.add("dmg")

        if name == "CodeSignatureVerifier":
            input_path = str(args.get("input_path") or "")
            if ".dmg/" in input_path.lower() or input_path.lower().endswith(".dmg"):
                found.add("dmg")
            elif "%pathname%" in input_path and input_path.endswith(".app"):
                found.add("dmg")
            else:
                for m in FORMAT_PATTERN.finditer(input_path):
                    found.add(m.group(1).lower())
            if args.get("expected_authority_names"):
                found.add("pkg")

    found = {_FORMAT_ALIASES.get(f, f) for f in found}
    return sorted(found)


# "win" as a delimited token (Foo-Win, x.win.y, win32/64, windows) or an
# .msi/.exe artifact. Delimiters avoid matching darwin, wineskin, winzip, etc.
WINDOWS_PATTERN = re.compile(r"(?:^|[-_. ])win(?:dows|32|64)?(?:$|[-_. ])|\.msi|\.exe")


def is_windows_recipe(recipe, rel_path):
    hay = " ".join(
        [
            recipe.get("Identifier", ""),
            recipe.get("Description", ""),
            os.path.basename(rel_path),
        ]
    ).lower()
    return bool(WINDOWS_PATTERN.search(hay))


def skip_reason(recipe, processor_set, rel_path):
    if "DeprecationWarning" in processor_set:
        return "deprecated"
    if "PackageRequired" in processor_set:
        return "package_required"
    parent = recipe.get("ParentRecipe", "")
    if parent and ".download." in parent:
        return "child_of_download"
    if is_windows_recipe(recipe, rel_path):
        return "windows"
    return None


def repo_name_for(path, repos_dir):
    rel = Path(path).relative_to(repos_dir)
    return rel.parts[0]


def rel_path_for(path, repos_dir):
    rel = Path(path).relative_to(repos_dir)
    return "/".join(rel.parts[1:])


def first_commit(path, repos_dir):
    repo = repo_name_for(path, repos_dir)
    repo_dir = Path(repos_dir) / repo
    rel_path = rel_path_for(path, repos_dir)
    try:
        # No --follow: rename detection needs blob content, which blobless
        # clones (clone_repos.sh) fetch lazily over the network, one per file.
        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%aI", "--", rel_path],
            cwd=repo_dir,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except Exception:
        return None
    if result.returncode != 0:
        return None
    lines = [line for line in result.stdout.splitlines() if line]
    return lines[-1] if lines else None


def recipe_files(repos_dir):
    patterns = ["**/*.recipe", "**/*.recipe.yaml", "**/*.recipe.plist"]
    files = []
    for pattern in patterns:
        files.extend(glob.glob(str(Path(repos_dir) / pattern), recursive=True))
    return sorted(Path(f) for f in files)


def build_parent_index(files, repos_dir):
    index = defaultdict(lambda: {"count": 0, "repos": set()})
    for path in files:
        recipe = parse_recipe_file(path)
        parent = recipe.get("ParentRecipe")
        if not parent:
            continue
        repo = repo_name_for(path, repos_dir)
        index[parent]["count"] += 1
        index[parent]["repos"].add(repo)
    return index


def read_download_recipes(repos_dir, skip_git=False):
    repos_dir = Path(repos_dir).expanduser().resolve()
    files = recipe_files(repos_dir)
    parent_index = build_parent_index(files, repos_dir)
    records = []
    history_jobs = []
    skipped = defaultdict(int)

    for path in files:
        if ".download." not in path.name:
            continue
        recipe = parse_recipe_file(path)
        processors = [short_name(step.get("Processor")) for step in recipe.get("Process", []) or []]
        processor_set = set(processors)
        repo = repo_name_for(path, repos_dir)
        rel_path = rel_path_for(path, repos_dir)
        reason = skip_reason(recipe, processor_set, rel_path)
        if reason:
            skipped[reason] += 1
            continue

        name = display_name(recipe)
        source_type, source_key, source_domain = extract_source(recipe, processors)
        input_vars = recipe.get("Input", {}) or {}
        dependents = parent_index.get(recipe.get("Identifier", ""), {"count": 0, "repos": set()})
        record = RecipeRecord(
            repo=repo,
            rel_path=rel_path,
            identifier=recipe.get("Identifier", ""),
            display_name=name,
            name_key=normalize_name(name or recipe.get("Identifier", "")),
            description=recipe.get("Description", ""),
            parent_recipe=recipe.get("ParentRecipe", ""),
            source_type=source_type,
            source_key=source_key,
            source_domain=source_domain,
            processors=processors,
            input_vars=sorted(input_vars),
            has_codesig="CodeSignatureVerifier" in processor_set,
            has_endofcheck="EndOfCheckPhase" in processor_set,
            has_arch_var=bool(ARCH_VARS & set(input_vars)),
            has_release_var=bool(RELEASE_VARS & set(input_vars)),
            codesig_authorities=extract_codesig_authorities(recipe),
            artifact_formats=extract_formats(recipe),
            first_commit=None,
            dependent_count=dependents["count"],
            dependent_repos=sorted(dependents["repos"]),
        )
        records.append(record)
        if not skip_git:
            history_jobs.append((path, record))

    if history_jobs:
        with ThreadPoolExecutor(max_workers=8) as pool:
            futures = {
                pool.submit(first_commit, path, repos_dir): record for path, record in history_jobs
            }
            for future in as_completed(futures):
                futures[future].first_commit = future.result()

    return records, {
        "total_recipe_files": len(files),
        "download_recipes": len(records),
        "skipped": dict(skipped),
    }
