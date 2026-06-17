import argparse

from .candidates import build_candidates
from .dashboard import write_dashboard
from .io import load_repo_overrides, load_set_overrides, resolve_path
from .recipe import read_download_recipes
from .scoring import evaluate_candidate, rank_key


def build_parser():
    parser = argparse.ArgumentParser(description="Build the AutoPkg duplicate recipe dashboard")
    parser.add_argument(
        "--repos-dir",
        required=True,
        help="Directory containing local AutoPkg recipe repos.",
    )
    parser.add_argument("--output-dir", default="docs")
    parser.add_argument("--override-repos", default="data/override_repos.json")
    parser.add_argument("--override-sets", default="data/override_sets.json")
    parser.add_argument("--skip-git", action="store_true", help="Skip first_commit lookups")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    repos_dir = resolve_path(args.repos_dir)
    output_dir = resolve_path(args.output_dir)
    repo_overrides = load_repo_overrides(resolve_path(args.override_repos))
    set_overrides = load_set_overrides(resolve_path(args.override_sets))

    records, scan_stats = read_download_recipes(repos_dir, skip_git=args.skip_git)
    candidates = build_candidates(records)
    evaluations = [
        evaluate_candidate(candidate, repo_overrides, set_overrides) for candidate in candidates
    ]
    evaluations.sort(key=rank_key)
    data = write_dashboard(output_dir, evaluations, scan_stats)
    print(f"Wrote {output_dir}: {data['summary']['total_sets']} sets {data['summary']['verdicts']}")
