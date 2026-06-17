import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def resolve_path(path, base=ROOT):
    p = Path(path).expanduser()
    if p.is_absolute():
        return p
    return (base / p).resolve()


def load_json(path, default):
    path = Path(path)
    if not path.exists():
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")


def load_repo_overrides(path):
    raw = load_json(path, {})
    return {repo: entry for repo, entry in raw.items() if not repo.startswith("_")}


def load_set_overrides(path):
    raw = load_json(path, {})
    return {name.lower(): entry for name, entry in raw.items() if not name.startswith("_")}
