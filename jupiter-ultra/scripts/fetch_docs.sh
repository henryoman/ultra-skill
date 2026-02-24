#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="$ROOT_DIR/references/raw"
URLS_FILE="$ROOT_DIR/references/source-urls.txt"

mkdir -p "$RAW_DIR/api" "$RAW_DIR/developer" "$RAW_DIR/portal"

if [[ ! -f "$URLS_FILE" ]]; then
  echo "Missing URL list: $URLS_FILE" >&2
  exit 1
fi

while IFS= read -r url; do
  [[ -z "$url" ]] && continue

  section="developer"
  if [[ "$url" == *"/api-reference/ultra"* ]]; then
    section="api"
  elif [[ "$url" == *"/portal/"* ]]; then
    section="portal"
  fi

  slug="${url#https://dev.jup.ag/}"
  slug="${slug//\//__}"
  file="$RAW_DIR/$section/${slug}.md"

  md_url="${url}.md"
  echo "Fetching: $md_url"
  curl -fsSL "$md_url" -o "$file"
done < "$URLS_FILE"

echo "Done. Files written under $RAW_DIR"
