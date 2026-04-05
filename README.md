# AutoPkg Dupe Tracker

Tracks and resolves redundant recipes across the [AutoPkg](https://github.com/autopkg) GitHub organization.

**[View the dashboard](https://homebysix.github.io/autopkg-dupe-tracker/)**

[![Dashboard Refresh Badge](https://github.com/homebysix/autopkg-dupe-tracker/actions/workflows/refresh.yml/badge.svg)](https://github.com/homebysix/autopkg-dupe-tracker/actions/workflows/refresh.yml)

## What this does

Multiple AutoPkg recipe repos often contain recipes for the same application. This project identifies those duplicates and recommends which to keep and which to deprecate, based on functional criteria specific to each recipe type.

## How recipe maintainers can help

If you maintain a recipe repo in the AutoPkg org, check the [dashboard](https://homebysix.github.io/autopkg-dupe-tracker/) and filter by your repo name. You can help by:

- **Merging open deprecation PRs** submitted to your repo
- **Adding `DeprecationWarning`** to recipes flagged for deprecation
- **Updating `ParentRecipe`** references in downstream recipes to point to the recommended keeper

## Workflow

### Local evaluation

These steps should be run periodically, manually:

1. **Clone the AutoPkg repos** locally by running `scripts/clone_repos.sh`. This fetches all repos in the AutoPkg org into an `autopkg/` sibling directory. Re-run periodically to pull updates. (Alternatively, [repo-lasso](https://github.com/homebysix/repo-lasso) can maintain the local clones.)

2. **Build candidates** from your local clones (`--repos-dir` points to wherever the AutoPkg repos live):

   ```bash
   python3 scripts/build_candidates.py --repos-dir ./autopkg -o data/candidates.json
   ```

3. **Run LLM evaluation** using the prompt at [`prompts/evaluate_candidates.md`](prompts/evaluate_candidates.md). The prompt reads `data/candidates.json` directly and writes results to `data/evaluations/YYYY-MM-DD.json`. For large candidate lists, tell the LLM to process ~50 sets at a time. Commit the results. Works with any LLM that can read files and run shell commands.

4. **Record exceptions** in `data/override_sets.json` when a recommendation should be overridden (won't-fix decisions, manual PR links for historical PRs, or cases where the normal criteria don't apply).

5. **Flag repos** in `data/override_repos.json` when a repo should never be the recommended keeper (unmaintained, maintainer handing off recipes, etc.).

6. **Create deprecation PRs** in the appropriate AutoPkg recipe repos. The dashboard detects these automatically via GitHub API.

### Dashboard refresh

The [dashboard](https://homebysix.github.io/autopkg-dupe-tracker/) renders `docs/dashboard.json` and displays each candidate set with its recommendation, rationale, PR status, dependency impact, and any overrides or repo flags. Recipe maintainers can filter by repo to see what affects them.

The [refresh workflow](.github/workflows/refresh.yml) runs the full pipeline weekly: cloning repos, building candidates, checking PR status, and assembling the dashboard. It uses the same scripts you run locally (steps 1-2 above), plus:

- **`scripts/check_pr_status.py`** — searches for deprecation PRs that touch tracked recipes, merges with manual PR links from `data/override_sets.json` &rarr; `data/pr_status.json`
- **`scripts/build_dashboard.py`** — assembles candidates + evaluations + overrides + PR status &rarr; `docs/dashboard.json`

## Disclaimer

The deduplication recommendations on this dashboard are generated with the assistance of generative AI and are meant as a starting point for human review. They may contain errors or miss important context. Always read the actual recipes and consider the broader impact before acting on any recommendation.

## Repository structure

```
scripts/                 Automation scripts (run by GH Actions and locally)
prompts/                 LLM prompt templates for evaluation (one per recipe type)
data/
  candidates.json        Auto-generated candidate sets
  evaluations/           LLM evaluation results (committed manually)
  override_sets.json     Per-set exceptions and manual PR links
  override_repos.json    Per-repo flags (e.g., never_keep)
  pr_status.json         Auto-generated PR status
docs/
  index.html             The dashboard
  dashboard.json             Dashboard data (auto-generated)
```

## License

Apache 2.0 — see [LICENSE](LICENSE).
