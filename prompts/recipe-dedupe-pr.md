# AutoPkg Recipe Deduplication — Pull Request Prompt

You are opening pull requests to deprecate or reparent AutoPkg recipes, working from the deduplication dashboard. The analysis is advisory: read the actual recipes, apply judgment, and favor a soft, appreciative touch over mechanical processing. These are volunteer maintainers.

## How this fits the larger loop

The dashboard is rebuilt by a scheduled GitHub Pages job from `docs/dashboard.json`. You run *this* workflow locally. When you open a PR you record it in `data/override_sets.json`, then commit that change to the remote — so the ledger you update here becomes intake for later dashboard runs and for your own future runs. The build reads the ledger: a set with a non-empty `prs` array is dropped from `recommend` to `skip` ("PR(s) already opened"), so recording a PR and committing it removes the set from the queue on the next build. The record only takes effect once committed.

## Input

Default to a **single set per run**. Process all of `recommend` only if explicitly asked.

Resolve the target set from `docs/dashboard.json`:

- If a set is injected below, process exactly that set.
- Otherwise, if given a set `id` (the 12-char hash) or an app name, find the matching entry in `docs/dashboard.json` with `verdict == "recommend"`. If an id isn't found (set membership can shift between refreshes, changing the hash), fall back to the closest app-name match and confirm with the user.

```json
{{SET_JSON}}
```

**Always read these first:**

- `docs/dashboard.json` — the source of truth for sets, keepers, confidence, and rationale.
- `data/override_sets.json` — the PR ledger (keyed by app name) plus per-set exceptions.
- `data/override_repos.json` — repos flagged `never_keep` and why.

## Gating: decide whether the set still needs a PR

Skip the set (and report why) if any of these hold:

1. **Ledger hit** — `data/override_sets.json[<app>]` has a non-empty `prs` array. It's already been acted on.
2. **Already deprecated** — the deprecate recipe file already contains a `DeprecationWarning` processor. A prior deprecation merged; backfill the ledger if it's missing, then skip.
3. **Existing PR found** — see the repo check below.

Only proceed past gating for sets that genuinely still need work.

## Step 1 — Check relevant repos for existing PRs

Check the repos that this set would touch:

- The **deprecate repo**, for the exact `rel_path` in the set's `deprecate` entries.
- Any **child-recipe repos** surfaced later by the identifier grep (for reparents).

A found PR is **aligned with the deduplication goal** only if it touches the relevant recipe file **and** the change is a deprecation, reparent, or removal (adds `DeprecationWarning`, edits `ParentRecipe`, or deletes the recipe), **or** its title/body clearly references deprecation or consolidation toward the keeper. A PR that merely mentions the app for unrelated reasons does not count. When it's ambiguous, stop and ask the user rather than recording it.

Find PRs that touch the file, across all states. Use `gh pr list` (the list API), not `gh search prs` — the PR search index lags and misses recent PRs. The exact file-path touch is the authoritative signal; PR titles are only a hint for context:

```bash
# Authoritative: any PR (any state) that touches the exact recipe file.
gh pr list --repo autopkg/<deprecate-repo> --state all --limit 200 \
  --json number,title,state,url,files \
  --jq '.[] | select(any(.files[]; .path == "<rel_path>")) | {number,state,title,url}'
```

Note the `--limit`: repos with a long PR history (some have 100+) can truncate. Raise the limit if a repo is busy, since a closed-but-relevant PR could sit far back.

Handle by state:

- **Open** — stop and report the URL. Don't open a second PR.
- **Merged** — already done. Record it in the ledger and skip.
- **Closed, unmerged** — previously rejected. Alert the user and do **not** silently re-open; wait for direction.

If an aligned PR exists, update the ledger (Step 4) and skip the rest.

## Step 2 — Verify against the actual recipes

Read the recipe files at their local cache paths to confirm the dashboard's call matches reality:

- **Local recipe cache**: `../repo-lasso/repos/autopkg/<repo>/<rel_path>`

Confirm the keeper (`keep[0]`) really is the better long-term parent and the `deprecate` entries really are substitutable duplicates — not forks, enterprise builds, portable variants, rebrands, or architecture-specific distributions. If reading the recipes contradicts the dashboard, stop and report rather than opening a PR.

## Step 3 — Open the PR(s)

### Environment

- **Fork remotes**: each clone has `origin` → `https://github.com/homebysix/<repo>` and `upstream` → `https://github.com/autopkg/<repo>`. Push branches to `origin`; PRs target `upstream`.
- **PR creation**: the autopkg org blocks `gh pr create`. After pushing a branch, find the upstream default branch (most repos use `master`, not `main`) and open a pre-filled compare URL:
  ```bash
  DEFAULT_BRANCH=$(git symbolic-ref refs/remotes/upstream/HEAD | sed 's|refs/remotes/upstream/||')
  TITLE="Deprecate <AppName> recipes"
  BODY="Per the AutoPkg..."
  ENCODED_TITLE=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.stdin.read().strip()))" <<< "$TITLE")
  ENCODED_BODY=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.stdin.read().strip()))" <<< "$BODY")
  open "https://github.com/autopkg/<repo>/compare/${DEFAULT_BRANCH}...homebysix:<branch>?expand=1&title=${ENCODED_TITLE}&body=${ENCODED_BODY}"
  ```
- **Anonymizer**: `~/Library/CloudStorage/Dropbox-Personal/Scripts/anonymizer.py` — pipe `autopkg run` output through this before quoting it in a PR body.

### Deprecation PR

Recipe edits to the deprecate recipe:

1. Add a `DeprecationWarning` processor as the **first** entry in the `Process` array, with `warning_message` set to the set's `deprecation_message`.
2. Bump `MinimumVersion` to `1.1` if it's currently lower (DeprecationWarning requires AutoPkg 1.1+).

Recipes are either plist (`.recipe`) or YAML (`.recipe.yaml`); edit in the file's own format and preserve its existing structure and key ordering.

- Branch: `deprecate-<appname-lowercase-kebab>`
- Commit and PR title: `Deprecate <AppName> recipes` (plural — deprecating a download recipe implicitly deprecates its children, even if only the download file changes)
- Push to `origin`, then open the compare URL.

### Find child recipes (for reparenting)

```bash
grep -r "<deprecated-identifier>" ../repo-lasso/repos/autopkg \
  --include="*.recipe" --include="*.recipe.yaml" -l
```

For each affected child recipe in a **different** repo than the deprecate repo:

- Keeper repo already has an equivalent of the same type → child auto-deprecates, no PR needed.
- No equivalent in keeper **and** download formats are compatible → open a reparent PR.
- Formats incompatible (e.g. dmg vs zip) → note it in the deprecation PR body instead of reparenting.

### Reparent PR

Change the child's `ParentRecipe` identifier to point at the keeper's download recipe.

Before opening:

1. Confirm the keeper repo has an equivalent download recipe.
2. Verify format compatibility with the child's processors (a child using `Unarchiver` needs zip/tar/tar.gz/tar.bz2, not dmg).
3. For pkg or munki recipes (not install), run and sanitize:
   ```bash
   autopkg run -vvq <recipe> 2>&1 | python3 ~/Library/CloudStorage/Dropbox-Personal/Scripts/anonymizer.py > /tmp/recipe_output.log
   ```
4. Include the sanitized output in the PR body.

- Branch: descriptive, e.g. `reparent-<appname>-<type>`
- Commit and PR title: `Adjust <AppName> <type> recipe parent`

## Step 4 — Update and commit the ledger

After opening (or discovering) a PR, record it in `data/override_sets.json` under the app-name key, appending to the existing `prs` array rather than overwriting. Add the set `id` for traceability against future refreshes:

```json
"<AppName>": {
  "id": "<12-char set id>",
  "prs": ["https://github.com/autopkg/<repo>/pull/<n>"]
}
```

Then commit the ledger change (single-line message, imperative, under 50 chars, e.g. `Record <AppName> dedupe PR`) and push, so it serves as intake for the next dashboard build and your next run. Do not commit recipe-cache edits — those live in the forks and travel via the PRs.

Do not set `merged: true` manually. `scripts/check_pr_status.py` detects merged PRs and writes that field automatically — run it before building the dashboard to graduate resolved sets to the Done tab.

## PR body templates

### Deprecation PR

```
Per the AutoPkg [repo maintenance expectations](https://github.com/autopkg/autopkg/wiki/Sharing-Recipes#repo-maintenance-expectations), duplicate recipes can appear in search results and cause confusion, especially for people getting started with AutoPkg. Consolidating in favor of recipes with the broadest utility helps reduce that noise.

The [<AppName> download recipe in <keeper-repo>](<link to keeper recipe on GitHub>) is a more broadly useful alternative to this repo's recipe:
- **<Advantage 1>** — brief explanation
- **<Advantage 2>** — brief explanation

<Optional: note about child recipes in other repos being reparented, with cross-reference>

This consolidation will help simplify search results and lower maintenance effort. Thank you for considering!
```

Build the advantage bullets by comparing the keeper against the deprecate recipe — use the set's `keeper` rationale and the members' feature fields (`has_codesig`, `has_endofcheck`, `source_type`, `has_arch_var`, `has_release_var`, useful description). List only **differentiating** features the keeper has and the loser lacks; omit anything both share. If the deprecated recipe's download source is broken, note that.

Never surface internal scoring or override policy in a PR body. In particular, `deprecate`-category rationale like `"repo flagged never_keep"` is an internal signal, not a maintainer-facing argument — frame the body around the keeper's concrete merits instead. Do not cite dependent counts as a standalone bullet; maintainers don't control other repos and it reads as a weak justification.

### Reparent PR

```
The <AppName> download recipe in <deprecated-repo> is under consideration for deprecation (<cross-ref>). This PR updates the <type> recipe in this repo to use <keeper-repo>'s download as a parent.

The download format is compatible — verified by running the recipe after the change:

<details>
<summary>Verbose output</summary>

\```
<sanitized autopkg run -vvq output>
\```

</details>

Thank you for considering!
```

## Cross-referencing

When a set produces both a deprecation PR and a reparent PR, cross-reference them with GitHub-style references (`autopkg/repo-name#123`). Since the number isn't known until the PR exists, add cross-references as comments after both are open. Prompt the user to share the URLs.

## Tone

Friendly and appreciative — these are volunteer maintainers. Factual, not prescriptive; brief, not verbose. Imperative, single-line commit and PR titles under 50 characters.
