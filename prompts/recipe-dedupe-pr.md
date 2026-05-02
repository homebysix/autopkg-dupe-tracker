# AutoPkg Recipe Deduplication — Pull Request Prompt

You are opening pull requests to deprecate or reparent AutoPkg recipes.

## Input

If a set is provided below, process only that set. Otherwise, read
`data/evaluations/<latest>.json`, also read the override files, and process
each set with verdict `recommend` and `action_status` of `needs_pr`.

```json
{{SET_JSON}}
```

**Override files** (always read before processing):

- **`data/override_repos.json`** — repos flagged `never_keep`
- **`data/override_sets.json`** — per-set exceptions and manual PR links

## Environment

- **Local recipe cache**: `/Users/elliotj/Developer/_personal/repo-lasso/repos/autopkg/<repo>/<rel_path>`
- **Fork remotes**: each repo clone has `origin` pointing to `https://github.com/homebysix/<repo>` and `upstream` pointing to `https://github.com/autopkg/<repo>`. Push branches to `origin`; PRs target `upstream`.
- **PR creation**: The autopkg org blocks `gh pr create`. After pushing a branch, get the upstream default branch with `git symbolic-ref refs/remotes/upstream/HEAD | sed 's|refs/remotes/upstream/||'` (most repos use `master`, not `main`), then pre-fill the PR form by URL-encoding the title and body and appending them as query parameters:
  ```bash
  DEFAULT_BRANCH=$(git symbolic-ref refs/remotes/upstream/HEAD | sed 's|refs/remotes/upstream/||')
  TITLE="Deprecate <AppName> recipes"
  BODY="Per the AutoPkg..."
  ENCODED_TITLE=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.stdin.read().strip()))" <<< "$TITLE")
  ENCODED_BODY=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.stdin.read().strip()))" <<< "$BODY")
  open "https://github.com/autopkg/<repo>/compare/${DEFAULT_BRANCH}...homebysix:<branch>?expand=1&title=${ENCODED_TITLE}&body=${ENCODED_BODY}"
  ```
- **Anonymizer script**: `~/Library/CloudStorage/Dropbox-Personal/Scripts/anonymizer.py` — pipe autopkg run output through this before including it in PR bodies.

## Workflow

For each set:

1. **Check for existing PRs** — stop and report if one is already open:
   ```bash
   gh pr list --repo autopkg/<deprecate-repo> --state all --search "deprecate OR deprecation OR deprecated OR duplicate OR <AppName>"
   ```

2. **Read the recipe files** at their local cache paths to verify the evaluation matches reality.

3. **Open the deprecation PR**:
   - Branch name: `deprecate-<appname-lowercase-kebab>`
   - In the deprecate recipe: add a `DeprecationWarning` processor as the **first** entry in the Process array, with `warning_message` set to the `deprecation_message` from the set data.
   - Bump `MinimumVersion` to `1.1` if currently lower (DeprecationWarning requires AutoPkg 1.1+).
   - Commit and PR title: `Deprecate <AppName> recipes`
   - Push branch to `origin`, open PR URL in browser.

4. **Find child recipes** that reference the deprecated recipe's identifier:
   ```bash
   grep -r "<deprecated-identifier>" /Users/elliotj/Developer/_personal/repo-lasso/repos/autopkg \
     --include="*.recipe" --include="*.recipe.yaml" -l
   ```

5. **For each affected child recipe in a different repo** than the deprecate repo:
   - Keeper repo has an equivalent of the same type → child will be auto-deprecated, no PR needed.
   - No equivalent in keeper AND download formats are compatible → open a reparent PR (see below).
   - Formats incompatible (e.g., dmg vs zip) → note in the deprecation PR body instead.

6. **Cross-reference PRs** once both exist. Prompt the user to share PR URLs so cross-references can be added as comments.

## PR types

### Deprecation PR

**Recipe changes:**

1. Add a `DeprecationWarning` processor as the **first** entry in the Process array, with `warning_message` pointing to the keeper repo.
2. Bump `MinimumVersion` to `1.1` if currently lower.

**Deprecation message format:**

```
Consider switching to <AppName> recipes in the <keeper-repo> repo. This recipe is deprecated and will be removed in the future.
```

### Reparent PR

Change the `ParentRecipe` identifier in a child recipe to point to the keeper's
download recipe instead of the deprecated one.

**Before opening a reparent PR:**

1. Confirm the keeper repo has an equivalent download recipe.
2. Verify the download format is compatible with the child recipe's processors
   (if the child uses `Unarchiver`, the download must be zip/tar/tar.gz/tar.bz2 — not dmg).
3. Run and sanitize (only for pkg or munki recipes — not install):
   ```bash
   autopkg run -vvq <recipe> 2>&1 | python3 ~/Library/CloudStorage/Dropbox-Personal/Scripts/anonymizer.py > /tmp/recipe_output.log
   ```
4. Include the sanitized output in the PR body.

If download formats are incompatible, do NOT open a reparent PR — note the incompatibility in the deprecation PR body instead.

## PR body templates

### Deprecation PR

```
Per the AutoPkg [repo maintenance expectations](https://github.com/autopkg/autopkg/wiki/Sharing-Recipes#repo-maintenance-expectations), duplicate recipes can appear in search results and cause confusion, especially for people getting started with AutoPkg. Consolidating in favor of recipes with the broadest utility helps reduce that noise.

The [<AppName> download recipe in <keeper-repo>](<link to keeper recipe file on GitHub>) is a more broadly useful alternative to this repo's recipe:
- **<Advantage 1>** — brief explanation
- **<Advantage 2>** — brief explanation

<Optional: note about child recipes in other repos being reparented, with cross-reference>

This consolidation will help simplify search results and lower maintenance effort. Thank you for considering!
```

Use the `rationale` entries from the set data with category `favors_keep` and `favors_deprecate` to populate the advantages list. List only **differentiating** features of the keeper; omit anything both recipes share. If the deprecated recipe's download source is broken, note that. Do **not** list dependent counts as a standalone bullet — maintainers don't control other repos and it reads as a weak justification.

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

## Commit and PR title format

Same text for both. One line, imperative mood, under 50 characters:
- Deprecation: `Deprecate <AppName> recipes`
- Reparent: `Adjust <AppName> <type> recipe parent`

Deprecating a download recipe implicitly deprecates its child recipes, so use "Deprecate Foo recipes" (plural) even if only the download recipe file is changed.

## Cross-referencing

When opening both a deprecation PR and a reparent PR for the same set, cross-reference them using GitHub-style references (`autopkg/repo-name#123`). Since the PR number isn't known until after creation, add cross-references as comments after both PRs exist. Prompt the user to provide links after they're opened.

## Tone

Friendly and appreciative — these are volunteer maintainers. Factual, not prescriptive; brief, not verbose.
