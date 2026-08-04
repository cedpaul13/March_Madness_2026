#!/usr/bin/env bash
# Deploys docs/index.html to the gh-pages branch so the website ships
# without its HTML source living on main. Run it after any site edit:
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

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

cp "$ROOT/docs/index.html" "$TMP/index.html"
touch "$TMP/.nojekyll"
cd "$TMP"
git init -q -b gh-pages
git config user.name "$NAME"
git config user.email "$EMAIL"
git add index.html .nojekyll
git commit -q -m "Deploy site $(date +%Y-%m-%d)"
git push -f "$REMOTE" gh-pages

echo "Deployed: https://cedpaul13.github.io/March_Madness_2026/"
