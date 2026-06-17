#!/usr/bin/env python3
"""Check whether PRs recorded in override_sets.json have merged.

For each set that has a `prs` array but no `merged: true`, fetches the
current state of every listed PR via `gh pr view`. If all PRs are merged,
sets `merged: true` on that entry and writes the file back.

Requires: gh CLI (authenticated).
"""

import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from recipe_dedupe.io import ROOT, load_json, write_json

OVERRIDES_PATH = ROOT / "data" / "override_sets.json"


def pr_state(url):
    result = subprocess.run(
        ["gh", "pr", "view", url, "--json", "state"],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if result.returncode != 0:
        return url, "unknown"
    return url, json.loads(result.stdout).get("state", "unknown").upper()


def main():
    data = load_json(OVERRIDES_PATH, {})
    pending = {
        name: entry for name, entry in data.items() if entry.get("prs") and not entry.get("merged")
    }

    all_tasks = [(name, url) for name, entry in pending.items() for url in entry["prs"]]
    states = {}  # url -> state
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(pr_state, url): (name, url) for name, url in all_tasks}
        for future in as_completed(futures):
            name, url = futures[future]
            _, state = future.result()
            print(f"  {name}: {url} → {state}", file=sys.stderr)
            states[url] = state

    changed = []
    for name, entry in pending.items():
        if all(states.get(url) == "MERGED" for url in entry["prs"]):
            data[name]["merged"] = True
            changed.append(name)

    if changed:
        write_json(OVERRIDES_PATH, data)
        print(f"Marked merged: {', '.join(changed)}")
    else:
        print("No new merges detected.")


if __name__ == "__main__":
    main()
