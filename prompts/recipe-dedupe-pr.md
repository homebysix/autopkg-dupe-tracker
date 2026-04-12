# AutoPkg Recipe Deduplication — Pull Request Prompt

You are opening pull requests to deprecate or reparent AutoPkg recipes based on
evaluated candidate sets. Each PR should be clear, friendly, and provide enough
context for maintainers to merge confidently.

## Background

Read `data/evaluations/<latest>.json` for the evaluated candidate sets. Each set
with verdict `recommend` identifies recipes to keep and recipes to deprecate.

Before starting, read the override files:

- **`data/override_repos.json`** — repos flagged `never_keep`
- **`data/override_sets.json`** — per-set exceptions and manual PR links

The AutoPkg org has OAuth restrictions that block `gh pr create`. Instead, push
branches to the `homebysix` fork and use `open` to launch the PR creation page
in the browser.

## PR types

There are two kinds of PRs:

### 1. Deprecation PR

Add a `DeprecationWarning` processor to the recipe being deprecated. This is
the most common PR type.

**Recipe changes:**

1. Add a `DeprecationWarning` processor as the **first** entry in the Process
   array, with a `warning_message` pointing to the keeper repo.
2. Bump `MinimumVersion` to `1.1` if it is currently lower (DeprecationWarning
   requires AutoPkg 1.1+).

**Deprecation message format:**

```
Consider switching to <AppName> recipes in the <keeper-repo> repo. This recipe is deprecated and will be removed in the future.
```

### 2. Reparent PR

Change the `ParentRecipe` identifier in a child recipe to point to the keeper's
download recipe instead of the deprecated one. This is needed when a child
recipe in a third-party repo depends on the recipe being deprecated, and an
equivalent parent exists in the keeper repo.

**Before opening a reparent PR:**

1. Confirm the keeper repo has an equivalent download recipe.
2. Verify the download format is compatible with the child recipe's processors
   (e.g., if the child uses `Unarchiver`, the download must produce a format
   Unarchiver supports: zip, tar, tar.gz, tar.bz2 — NOT dmg).
3. Run the reparented recipe (only if it's a pkg or munki type, NOT install):
   `autopkg run -vvq <recipe> 2>&1 > /tmp/recipe_output.log`
4. Sanitize the captured output to remove references to local users, tokens/secrets,
   or other proprietary information. Check whether this script exists for this
   purpose: ~/Dropbox/Scripts/anonymizer.py
5. Include the sanitized verbose output in the PR body (see template below).

If the download formats are incompatible (e.g., dmg vs zip), do NOT open a
reparent PR. Note the incompatibility in the deprecation PR instead.

## Cross-referencing

When opening both a deprecation PR and a reparent PR for the same candidate set,
cross-reference them:

- In the deprecation PR, mention the reparent PR with a GitHub-style reference:
  `autopkg/other-repo#123`
- In the reparent PR, mention the deprecation PR the same way

Since the autopkg org blocks `gh pr create`, you may not know the PR number
until after it's created. Add cross-references as comments after both PRs exist. Prompt the user to provide links to the PRs after they're opened.

## Commit messages and PR titles

Use the same text for both. One line, imperative mood, under 50 characters, no
attribution lines.

- Deprecation: `Deprecate <AppName> recipes`
- Reparent: `Adjust <AppName> <type> recipe parent`

Deprecating a download recipe implicitly deprecates its child recipes (munki,
pkg, etc.), so use "Deprecate Foo recipes" (plural) even if only the download
recipe file is changed.

## PR body structure

### Deprecation PR

```
Per the AutoPkg [repo maintenance expectations](https://github.com/autopkg/autopkg/wiki/Sharing-Recipes#repo-maintenance-expectations), duplicate recipes can appear in search results and cause confusion, especially for people getting started with AutoPkg. Consolidating in favor of recipes with the broadest utility helps reduce that noise.

The <AppName> download recipe in <keeper-repo> is a more broadly useful alternative to this repo's recipe:
- **<Advantage 1>** — brief explanation
- **<Advantage 2>** — brief explanation

<Optional: note about child recipes in other repos being reparented, with cross-reference>

This consolidation will help simplify search results and lower maintenance effort. Thank you for considering!
```

List only **differentiating** advantages of the keeper (at least one). Omit
features both recipes share. If the deprecated recipe's download source is
broken, note that. Child recipes in the same repo are auto-deprecated — mention
only if relevant, phrased as informational.

### Reparent PR

```
The <AppName> download recipe in <old-parent-repo> is under consideration for deprecation (<cross-ref>). This PR updates the <type> recipe in this repo to use <keeper-repo>'s download as a parent.

The download format is compatible — verified by running the recipe after the change:

<details>
<summary>Verbose output</summary>

\```
<sanitized autopkg run -vvq output>
\```

</details>

Thank you for considering!
```

## Tone

Friendly and appreciative — these are volunteer maintainers. Be factual, not
prescriptive; brief, not verbose.

## Checking for existing PRs

Before opening a PR, check for existing deduplication/deprecation PRs:

```bash
gh pr list --repo autopkg/<repo> --state all --search "deprecate OR deprecation OR deprecated OR duplicate OR <AppName>"
```

Skip any set that already has an open deduplication/deprecation PR for the same recipe.

## Workflow

For each evaluated set with verdict `recommend`:

1. Check for existing PRs (skip if found).
2. Read the actual recipe files to verify the evaluation.
3. Open the deprecation PR on the repo containing the recipe to deprecate.
4. Identify child recipes in other repos that reference the deprecated recipe's
   identifier (grep for the identifier across all repos).
5. For each affected child recipe:
   - If the keeper repo has an equivalent recipe of the same type (munki, pkg,
     etc.), the child will be auto-deprecated — no PR needed.
   - If the keeper repo does NOT have an equivalent, and the download format is
     compatible, open a reparent PR.
   - If the format is incompatible, note this in the deprecation PR body.
6. Cross-reference related PRs.
