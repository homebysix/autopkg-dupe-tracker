import plistlib
import tempfile
import unittest
from pathlib import Path

from recipe_dedupe.candidates import build_candidates
from recipe_dedupe.recipe import read_download_recipes
from recipe_dedupe.scoring import evaluate_candidate


def write_recipe(path, identifier, name, process, description="Downloads app."):
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "Identifier": identifier,
        "Input": {"NAME": name},
        "Description": description,
        "Process": process,
    }
    with open(path, "wb") as f:
        plistlib.dump(data, f)


def github_process(repo, with_codesig=True, fmt="dmg", arch=False):
    process = [
        {
            "Processor": "GitHubReleasesInfoProvider",
            "Arguments": {
                "github_repo": repo,
                "asset_regex": f".*\\.{fmt}",
            },
        },
        {"Processor": "URLDownloader", "Arguments": {"filename": f"App.{fmt}"}},
        {"Processor": "EndOfCheckPhase", "Arguments": {}},
    ]
    if with_codesig:
        process.append(
            {
                "Processor": "CodeSignatureVerifier",
                "Arguments": {
                    "requirement": 'certificate 1[field.1.2.840.113635.100.6.2.6] = "Developer ID Certification Authority"'  # noqa: E501
                },
            }
        )
    if arch:
        process[0]["Arguments"]["asset_regex"] = "%ARCH%.*\\.dmg"
    return process


class PipelineTests(unittest.TestCase):
    def test_source_match_builds_high_confidence_keeper_recommendation(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            write_recipe(
                base / "repo-a" / "Foo" / "Foo.download.recipe",
                "com.example.a.download.Foo",
                "Foo",
                github_process("vendor/foo", with_codesig=True),
            )
            write_recipe(
                base / "repo-b" / "Foo" / "Foo.download.recipe",
                "com.example.b.download.Foo",
                "Foo",
                github_process("vendor/foo", with_codesig=False),
            )

            records, _ = read_download_recipes(base, skip_git=True)
            candidates = build_candidates(records)
            evaluation = evaluate_candidate(candidates[0])

            self.assertEqual(len(candidates), 1)
            self.assertEqual(candidates[0].match_strength, "HIGH")
            self.assertEqual(evaluation["verdict"], "recommend")
            self.assertEqual(evaluation["duplicate_confidence"], "HIGH")
            self.assertEqual(evaluation["keep"][0]["repo"], "repo-a")

    def test_different_artifacts_are_review_not_deprecation(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            write_recipe(
                base / "repo-a" / "Foo" / "Foo.download.recipe",
                "com.example.a.download.Foo",
                "Foo",
                github_process("vendor/foo", fmt="dmg"),
            )
            write_recipe(
                base / "repo-b" / "Foo" / "Foo.download.recipe",
                "com.example.b.download.Foo",
                "Foo",
                github_process("vendor/foo", fmt="pkg"),
            )

            records, _ = read_download_recipes(base, skip_git=True)
            candidate = build_candidates(records)[0]
            evaluation = evaluate_candidate(candidate)

            self.assertEqual(evaluation["verdict"], "review")
            self.assertFalse(evaluation["substitutability"]["compatible_artifact"])

    def test_never_keep_repo_is_penalized(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            write_recipe(
                base / "repo-a" / "Foo" / "Foo.download.recipe",
                "com.example.a.download.Foo",
                "Foo",
                github_process("vendor/foo", with_codesig=True),
            )
            write_recipe(
                base / "repo-b" / "Foo" / "Foo.download.recipe",
                "com.example.b.download.Foo",
                "Foo",
                github_process("vendor/foo", with_codesig=True),
            )

            records, _ = read_download_recipes(base, skip_git=True)
            candidate = build_candidates(records)[0]
            evaluation = evaluate_candidate(
                candidate,
                repo_overrides={"repo-a": {"flag": "never_keep"}},
            )

            self.assertEqual(evaluation["keep"][0]["repo"], "repo-b")

    def test_first_commit_breaks_equal_keeper_scores(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            write_recipe(
                base / "repo-a" / "Foo" / "Foo.download.recipe",
                "com.example.a.download.Foo",
                "Foo",
                github_process("vendor/foo", with_codesig=True),
            )
            write_recipe(
                base / "repo-z" / "Foo" / "Foo.download.recipe",
                "com.example.z.download.Foo",
                "Foo",
                github_process("vendor/foo", with_codesig=True),
            )

            records, _ = read_download_recipes(base, skip_git=True)
            for record in records:
                record.first_commit = (
                    "2020-01-01T00:00:00+00:00"
                    if record.repo == "repo-z"
                    else "2022-01-01T00:00:00+00:00"
                )
            candidate = build_candidates(records)[0]
            evaluation = evaluate_candidate(candidate)

            self.assertEqual(evaluation["keep"][0]["repo"], "repo-z")

    def test_name_only_match_requires_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            write_recipe(
                base / "repo-a" / "Foo" / "Foo.download.recipe",
                "com.example.a.download.Foo",
                "Foo",
                [
                    {
                        "Processor": "URLDownloader",
                        "Arguments": {"url": "https://a.example/Foo.dmg"},
                    },
                    {"Processor": "EndOfCheckPhase", "Arguments": {}},
                ],
            )
            write_recipe(
                base / "repo-b" / "Foo" / "Foo.download.recipe",
                "com.example.b.download.Foo",
                "Foo",
                [
                    {
                        "Processor": "URLDownloader",
                        "Arguments": {"url": "https://b.example/Foo.dmg"},
                    },
                    {"Processor": "EndOfCheckPhase", "Arguments": {}},
                ],
            )

            records, _ = read_download_recipes(base, skip_git=True)
            candidate = build_candidates(records)[0]
            evaluation = evaluate_candidate(candidate)

            self.assertEqual(candidate.match_strength, "LOW")
            self.assertEqual(evaluation["verdict"], "review")


if __name__ == "__main__":
    unittest.main()
