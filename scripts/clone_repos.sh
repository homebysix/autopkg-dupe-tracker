#!/bin/bash
# Clone or update all repositories in the autopkg GitHub org.
# Usage: ./clone_repos.sh [target_dir]
#   target_dir defaults to ../autopkg (sibling of this repo)

set -euo pipefail

TARGET="${1:-$(dirname "$(dirname "$(realpath "$0")")")/../autopkg}"
mkdir -p "$TARGET"
cd "$TARGET"

echo "Cloning/updating autopkg org repos into $TARGET"

# Fetch all repo names from the autopkg org (requires gh CLI)
REPOS=$(gh repo list autopkg --limit 500 --json name --jq '.[].name' | sort)
TOTAL=$(echo "$REPOS" | wc -l | tr -d ' ')
echo "Found $TOTAL repos in the autopkg org"

COUNT=0
for REPO in $REPOS; do
    COUNT=$((COUNT + 1))
    if [ -d "$REPO" ]; then
        echo "[$COUNT/$TOTAL] Updating $REPO..."
        # Backfill history for clones made before the blobless switch, else
        # first_commit stays blind to anything past the shallow boundary.
        if [ -f "$REPO/.git/shallow" ]; then
            git -C "$REPO" fetch --unshallow --filter=blob:none --quiet 2>/dev/null || true
        fi
        git -C "$REPO" pull --ff-only --quiet 2>/dev/null || true
    else
        echo "[$COUNT/$TOTAL] Cloning $REPO..."
        git clone --filter=blob:none "https://github.com/autopkg/$REPO.git" "$REPO" 2>/dev/null || {
            echo "  Warning: failed to clone $REPO, retrying..."
            git clone --filter=blob:none "https://github.com/autopkg/$REPO.git" "$REPO" 2>/dev/null || {
                echo "  Warning: failed to clone $REPO after 2 tries, skipping."
            }
        }
    fi
done

echo "Done. $COUNT repos in $TARGET"
