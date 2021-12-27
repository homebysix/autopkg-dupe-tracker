#!/usr/bin/env python3
# coding: utf-8

"""Given the path to a directory containing clones of all the AutoPkg org recipe
repositories, this script will evaluate recipes for potential redundancies and
produce a basic HTML site with the results."""

import base64
import hashlib
import json
import os
import plistlib
import subprocess
from datetime import datetime
from glob import glob

import yaml

__author__ = "Elliot Jordan"
__version__ = "3.0.0"

# The directory that contains clones of all AutoPkg repos. Recommend using a
# bulk clone tool like Repo Lasso (https://github.com/homebysix/repo-lasso) to
# create this base directory.
REPOS_BASE = "./autopkg"

# GitHub project name, for generating GitHub Pages URLs
PROJECT = "autopkg-dupe-tracker"


def get_recipes():
    """Gets the contents to all AutoPkg recipes within a base directory."""

    # Get relative paths to recipes up to 2 levels deep
    recipe_paths = (
        glob(f"{REPOS_BASE}/*/*.recipe")
        + glob(f"{REPOS_BASE}/*/*/*.recipe")
        + glob(f"{REPOS_BASE}/*/*.recipe.yaml")
        + glob(f"{REPOS_BASE}/*/*/*.recipe.yaml")
    )

    # Read contents and metadata of recipes
    recipes = {}
    for full_path in recipe_paths:
        path = os.path.relpath(full_path, REPOS_BASE)
        print(f"Analyzing {path}")
        parents, filename = os.path.split(path)
        if path.endswith(".yaml"):
            with open(os.path.join(REPOS_BASE, path), "rb") as f:
                recipe = yaml.load(f, Loader=yaml.FullLoader)
        else:
            with open(os.path.join(REPOS_BASE, path), "rb") as f:
                recipe = plistlib.load(f)
        mod_dates_proc = subprocess.run(
            [
                "git",
                "-C",
                os.path.dirname(os.path.join(REPOS_BASE, path)),
                "log",
                "--follow",
                "--reverse",
                "--date=iso",
                "--pretty=format:%ad",
                filename,
            ],
            capture_output=True,
            text=True,
        )
        recipes[path] = {
            "parent_repo": parents.split("/")[0],
            "parent_recipes": [],
            "filename": filename,
            "score": 0,
            "warnings": {},
            # TODO:
            "first_commit": mod_dates_proc.stdout.split("\n")[0],
            "latest_commit": mod_dates_proc.stdout.split("\n")[-1],
            # "tests": None,
            "contents": recipe,
        }

    return recipes


def append_result(results, hash, item):
    """Append to results, creating an index if needed."""

    if hash not in results:
        results[hash] = [item]
    else:
        results[hash].append(item)

    return results


def compare_contents(recipes):
    """Detect recipes that are literal duplicates of each other."""

    results = {}
    for relpath, recipe in recipes.items():
        content_json = json.dumps(recipe["contents"], default=str)
        content_lower = content_json.lower().encode("ascii")
        content_base64 = base64.b64encode(content_lower)
        content_sha256 = hashlib.sha256(content_base64).hexdigest()
        results = append_result(results, content_sha256, relpath)

    return results


def compare_filenames(recipes, ignore_numbers=False):
    """Detect duplicate filenames, ignoring case and spaces."""

    results = {}
    for relpath, recipe in recipes.items():
        filename = recipe["filename"].lower().replace(" ", "")
        if filename.startswith("sharedprocessors"):
            continue
        if ignore_numbers:
            filename = "".join(x for x in filename if not x.isdigit())
        results = append_result(results, filename, relpath)

    return results


def compare_ids(recipes):
    """Detect recipes with duplicate identifiers."""

    results = {}
    for relpath, recipe in recipes.items():
        identifier = recipe["contents"].get("Identifier").lower()
        if identifier:
            results = append_result(results, identifier, relpath)

    return results


def compare_names(recipes):
    """Detect recipes with duplicate names and "types"."""

    results = {}
    for relpath, recipe in recipes.items():
        type = (
            recipe["filename"]
            .replace(".recipe", "")
            .replace(".yaml", "")
            .split(".")[-1]
        )
        name = (
            recipe["contents"].get("Input", {}).get("NAME", "").replace(" ", "").lower()
        )
        if name:
            results = append_result(results, ".".join((name, type)), relpath)

    return results


def compare_urls(recipes, input_key, proc_name, arg_name):
    """Detect recipes with duplicate identifiers."""

    results = {}
    for relpath, recipe in recipes.items():
        url = recipe["contents"].get("Input", {}).get(input_key)
        if not url:
            url = [
                x.get("Arguments", {}).get(arg_name)
                for x in recipe["contents"].get("Process", [{}])
                if x.get("Processor") == proc_name
            ]
            if url:
                url = url[0]
            else:
                continue
        if url and not url.startswith("%") and not url.endswith("%"):
            results = append_result(results, url, relpath)

    return results


def compile_test_results(recipes):
    """Function that returns a dictionary with results of recipe comparisons."""

    # fmt: off
    # Run duplicate detection tests and generate dictionary with results
    dupe_info = {
        "duplicate contents": {
            "score": 1.0,
            "results": compare_contents(recipes),
        },
        "duplicate filenames": {
            "score": 0.5,
            "results": compare_filenames(recipes),
        },
        "duplicate URLDownloader URLs": {
            "score": 0.2,
            "results": compare_urls(recipes, "DOWNLOAD_URL", "URLDownloader", "url"),
        },
        "duplicate Sparkle feeds": {
            "score": 0.2,
            "results": compare_urls(recipes, "SPARKLE_FEED_URL", "SparkleUpdateInfoProvider", "appcast_url"),
        },
        "duplicate filenames, ignoring numbers": {
            "score": 0.1,
            "results": compare_filenames(recipes, ignore_numbers=True),
        },
        "duplicate NAMEs": {
            "score": 0.1,
            "results": compare_names(recipes),
        },
        "duplicate identifiers": {
            "score": 0.1,
            "results": compare_ids(recipes),
        },
    }
    # fmt: on

    # Add test results into recipes dict
    for issue, test_info in dupe_info.items():
        for result in test_info["results"]:
            if len(test_info["results"][result]) > 1:
                for match in test_info["results"][result]:
                    recipes[match]["score"] += test_info["score"]
                    recipes[match]["warnings"][f"{issue} (<code>{result}</code>)"] = [
                        x for x in test_info["results"][result] if x != match
                    ]

    return recipes


def generate_site(recipes):
    """Given a recipe dict, produce HTML files for a static site."""

    # Generate repo and recipe data
    parent_repos = list({x["parent_repo"] for x in recipes.values()})
    repo_rows = []
    recipe_rows = {}
    for repo in sorted(parent_repos, key=str.lower):
        # Repo data
        recipe_count = len([x for x in recipes if recipes[x]["parent_repo"] == repo])
        warning_recipes = []
        for recipe in recipes.values():
            if recipe["parent_repo"] == repo:
                for matches in recipe["warnings"].values():
                    for match in matches:
                        if match not in warning_recipes:
                            warning_recipes.append(match)
        warnings_count = len(warning_recipes)
        repo_rows.extend(
            (
                "\n\t\t\t<tr>",
                f'<td><a href="{repo}">{repo}</a></td>',
                f"<td>{min([x['first_commit'] for x in recipes.values() if x['parent_repo'] == repo if x['first_commit']])}</td>",
                f"<td>{max([x['latest_commit'] for x in recipes.values() if x['parent_repo'] == repo if x['latest_commit']])}</td>",
                f"<td>{recipe_count}</td>",
                "<td>unknown</td>",
                f"<td>{warnings_count}</td>",
                "</tr>",
            )
        )
        recipe_rows[repo] = []
        for relpath, recipe in recipes.items():
            # Recipe data
            if recipe["parent_repo"] != repo:
                continue
            warning_recipes = []
            for matches in recipe["warnings"].values():
                for match in matches:
                    if match not in warning_recipes:
                        warning_recipes.append(match)
            warnings_count = len(warning_recipes)
            recipe_rows[repo].extend(
                (
                    "\n\t\t\t<tr>",
                    f'<td><a href="{"/".join(relpath.split("/")[1:])}.html">{relpath.replace(repo + "/", "")}</a></td>',
                    f"<td>{recipe['first_commit']}</td>",
                    f"<td>{recipe['latest_commit']}</td>",
                    f"<td>{warnings_count}</td>",
                    "</tr>",
                )
            )
            # Write recipe html
            with open("templates/recipe.html", "r") as f:
                recipe_html = f.read()

            warnings_html = "" if recipe["warnings"] else "<p>None</p>"
            for issue, matches in recipe["warnings"].items():
                warnings_html += f"\n<p>The following recipes have {issue}:</p>"
                warnings_html += "\n<ul>"
                for match in matches:
                    warnings_html += (
                        f'\n<li><a href="/{PROJECT}/{match}.html">{match}</a></li>'
                    )
                warnings_html += "\n</ul>"
            repl = {
                "%TITLE%": recipe["filename"],
                "%PARENT_REPO%": recipe["parent_repo"],
                "%LAST_REFRESH%": datetime.strftime(
                    datetime.utcnow(), "%Y-%m-%d %H:%M:%S"
                ),
                "%DESCRIPTION%": recipe["contents"].get("Description", "None"),
                "%IDENTIFIER%": recipe["contents"]["Identifier"],
                "%PARENT_RECIPES%": recipe["contents"].get("ParentRecipe", "None"),
                "%FIRST_COMMIT%": recipe["first_commit"],
                "%LATEST_COMMIT%": recipe["latest_commit"],
                "%WARNINGS%": warnings_html,
            }
            for r in repl:
                recipe_html = recipe_html.replace(r, repl[r])
            if not os.path.isdir(os.path.dirname(f"docs/{relpath}")):
                os.makedirs(os.path.dirname(f"docs/{relpath}"))
            with open(f"docs/{relpath}.html", "w") as f:
                f.write(recipe_html)

        # Write repo html
        with open("templates/repo.html", "r") as f:
            repo_html = f.read()
        repl = {
            "%TITLE%": repo,
            "%LAST_REFRESH%": datetime.strftime(datetime.utcnow(), "%Y-%m-%d %H:%M:%S"),
            "%RECIPE_ROWS%": "".join(recipe_rows[repo]),
        }
        for r in repl:
            repo_html = repo_html.replace(r, repl[r])
        if not os.path.isdir(f"docs/{repo}"):
            os.makedirs(f"docs/{repo}")
        with open(f"docs/{repo}/index.html", "w") as f:
            f.write(repo_html)

    # Write homepage index.html
    with open("templates/home.html", "r") as f:
        home_html = f.read()
    repl = {
        "%TITLE%": "AutoPkg Dupe Tracker",
        "%LAST_REFRESH%": datetime.strftime(datetime.utcnow(), "%Y-%m-%d %H:%M:%S"),
        "%REPO_ROWS%": "".join(repo_rows),
    }
    for r in repl:
        home_html = home_html.replace(r, repl[r])
    if not os.path.isdir("docs"):
        os.makedirs("docs")
    with open("docs/index.html", "w") as f:
        f.write(home_html)


def main():
    """Main process."""

    print("Analyzing all AutoPkg recipes from %s" % REPOS_BASE)
    if os.path.isfile("cache.json"):
        with open("cache.json", "rb") as f:
            recipes = json.load(f)
    else:
        recipes = get_recipes()
        with open("cache.json", "w") as f:
            json.dump(recipes, f, indent=2)
    recipes = compile_test_results(recipes)

    print("Generating site data...")
    generate_site(recipes)


if __name__ == "__main__":
    main()
