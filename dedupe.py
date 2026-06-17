#!/usr/bin/env python3
"""Run the dedupe CLI from the repo root."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from recipe_dedupe.cli import main  # noqa: E402

if __name__ == "__main__":
    main()
