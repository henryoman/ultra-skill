#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SITEMAP_TMP="/tmp/jup_sitemap.xml"
URLS_FILE="$ROOT_DIR/references/source-urls.txt"

curl -fsSL "https://dev.jup.ag/sitemap.xml" -o "$SITEMAP_TMP"

rg -o '<loc>[^<]+' "$SITEMAP_TMP" \
  | sed 's#<loc>##' \
  | sort -u \
  | awk '/\/api-reference\/ultra(\/|$)/ || /\/docs\/ultra(\/|$)/ || /\/portal\//' \
  > "$URLS_FILE"

echo "Updated $URLS_FILE"
wc -l "$URLS_FILE"
