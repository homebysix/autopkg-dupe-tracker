# AutoPkg Download Recipe Deduplication — Evaluation Prompt

You are evaluating AutoPkg download recipe candidate sets for deduplication.
Your job is to analyze each set and recommend which recipe(s) to KEEP and which
to DEPRECATE.

## Setup

Before starting, create a Python virtual environment and install dependencies:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Use `.venv/bin/python` for any Python commands (e.g., running `build_candidates.py`).

## Input

Read `data/candidates.json`. It contains candidate sets as JSON. Each set has
an `id`, `display_name`, and `members` array. Each member includes pre-computed
metadata:

- `has_codesig`, `has_endofcheck`, `has_arch_var`, `has_release_var`
- `first_commit` (ISO date of the recipe's first git commit)
- `dependent_count` and `dependent_repos`
- `processors` (ordered list of processor names in the recipe)
- `source_type` and `source_key`

If there are many sets, process them in batches (e.g., 50 at a time).

## Overrides

Before evaluating, read the override files:

- **`data/override_repos.json`** — repos flagged `never_keep` must not be
  recommended as the keeper. If a `never_keep` repo has the only functionally
  superior recipe, note that in the rationale but still pick the alternative
  repo as keeper.
- **`data/override_sets.json`** — per-set exceptions. If a set has a
  `wont_fix` or `exception` decision, skip it (verdict `skip`, skip_reason
  referencing the override). If it has an `override_keep`, use that as the
  keeper.

## What to do for each set

1. **Read each recipe file** at `repos/autopkg/<repo>/<rel_path>` to understand
   what it actually does — the metadata gives you signals but reading the recipe
   reveals nuances (asset_regex patterns, hardcoded URLs, custom processors).

2. **Compare recipes** using these criteria (in priority order):

   **Functional:**
   - CodeSignatureVerifier presence (absence is a negative signal)
   - EndOfCheckPhase presence (absence is a negative signal)
   - Multi-arch support via input variable (has_arch_var)
   - Multi-channel/release support via input variable (has_release_var)
   - Download source resilience: GitHub Releases > Sparkle > structured API > HTML scraping
   - Pseudo-universal recipes (download both Intel and Apple Silicon, then
     synthesize a combined installer) should be deprecated in favor of a recipe
     that downloads a true universal binary, if one exists in the set. If no
     true universal source exists, ignore the pseudo-universal recipe when
     comparing.

   **Metadata quality:**
   - Useful Description? Clear Input variable names?

   **History (tiebreaker):**
   - Earlier first_commit wins (use pre-computed first_commit field)
   - If within ~30 days, also consider update recency

   **Format (minor tiebreaker):**
   - Plist slightly preferred over YAML

   **Do NOT consider:**
   - Repo popularity, reputation, or community size — small and large repos have equal footing
   - Total recipe count in the repo
   - StopProcessingIf usage
   - Download format differences (DMG vs PKG vs ZIP) — NOT redundant

3. **Run `autopkg run -vvq <full_path>`** only when sources differ and it's
   unclear from reading alone whether the download works. Same-source recipes
   usually both work or both fail.

4. **Check for existing PRs**: Run
   `gh pr list --repo autopkg/<repo> --state all --search "deprecat OR <app-name>"`

   When mentioning PRs in rationale, reason, or dependency_impact text, always
   use GitHub-style references: `autopkg/repo-name#123`. Never use bare `#123`
   or `#123 on repo-name`.

## Output format

Write a JSON array to `data/evaluations/YYYY-MM-DD.json` (using today's date).
Each element:

```json
{
  "set_id": "<id from input>",
  "recipe_type": "download",
  "app_name": "<display_name from input>",
  "verdict": "recommend" | "skip",
  "skip_reason": "<if verdict is skip, why — e.g., 'different formats', 'different products'>",
  "confidence": "HIGH" | "MEDIUM" | "LOW",
  "keep": [
    {
      "repo": "<repo-name>",
      "rel_path": "<path within repo>",
      "reason": "<1-line reason for keeping>"
    }
  ],
  "deprecate": [
    {
      "repo": "<repo-name>",
      "rel_path": "<path within repo>",
      "reason": "<1-line reason for deprecating>"
    }
  ],
  "rationale": [
    {
      "category": "shared",
      "text": "<what the recipes have in common — e.g., both use GitHubReleasesInfoProvider with CodeSignatureVerifier>"
    },
    {
      "category": "favors_keep",
      "text": "<advantage of the kept recipe — e.g., has ARCHITECTURE input variable for arm64/x64 selection>"
    },
    {
      "category": "favors_deprecate",
      "text": "<weakness of the deprecated recipe — e.g., no architecture variable, Intel-only by default>"
    },
    {
      "category": "tiebreaker",
      "text": "<minor factor — e.g., first committed 2016 vs 2018>"
    }
  ],
  "criteria": [
    {
      "key": "codesig|endofcheck|arch|release|source_resilience|metadata|history|format",
      "label": "<human-readable label>",
      "favors": "keep" | "deprecate" | null
    }
  ],
  "deprecation_message": "Consider switching to <app> recipes in the <repo> repo. This recipe is deprecated and will be removed in the future.",
  "dependency_impact": "<N child recipes across M repos> | none",
  "existing_prs": [
    {
      "repo": "<repo-name>",
      "number": 123,
      "url": "https://github.com/autopkg/<repo>/pull/123",
      "title": "<PR title>",
      "state": "open" | "merged" | "closed"
    }
  ]
}
```

For SKIP verdicts, only `set_id`, `app_name`, `verdict`, and `skip_reason` are required.

## Confidence levels

- **HIGH**: Clear winner on functional criteria (one has CodeSignatureVerifier, the
  other doesn't; one is parameterized, the other hardcoded; one works, the other doesn't)
- **MEDIUM**: Both work and are similar, but one has meaningful advantages
- **LOW**: Recipes are nearly identical; decision rests on tiebreakers
