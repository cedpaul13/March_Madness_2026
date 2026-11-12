#!/usr/bin/env bash
# Deploys the versioned HTML, stylesheet and NCAA logo to gh-pages.
# Run it after validating any site edit:
#
#   ./scripts/deploy_site.sh
#
# One-time setup on GitHub: Settings > Pages > Deploy from a branch >
# branch "gh-pages", folder "/ (root)".
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
REMOTE="$(git -C "$ROOT" remote get-url origin)"
NAME="$(git -C "$ROOT" config user.name)"
EMAIL="$(git -C "$ROOT" config user.email)"
EXPECTED="$(git ls-remote --heads "$REMOTE" refs/heads/gh-pages | cut -f1)"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

cp "$ROOT/docs/index.html" "$TMP/index.html"
cp "$ROOT/docs/design.css" "$TMP/design.css"
cp "$ROOT/docs/ncaa-logo.svg" "$TMP/ncaa-logo.svg"
touch "$TMP/.nojekyll"
cd "$TMP"
git init -q -b gh-pages
git config user.name "$NAME"
git config user.email "$EMAIL"
git add index.html design.css ncaa-logo.svg .nojekyll
git commit -q -m "Deploy site $(date +%Y-%m-%d)"
git push --force-with-lease="refs/heads/gh-pages:$EXPECTED" "$REMOTE" gh-pages

echo "Deployed: https://cedpaul13.github.io/March_Madness_2026/"
