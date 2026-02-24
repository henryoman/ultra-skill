#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="$ROOT_DIR/references/raw"
OUT_DIR="$ROOT_DIR/references/organized"
URLS_FILE="$ROOT_DIR/references/source-urls.txt"

mkdir -p "$OUT_DIR/api" "$OUT_DIR/developer" "$OUT_DIR/portal"

if [[ ! -f "$URLS_FILE" ]]; then
  echo "Missing URL list: $URLS_FILE" >&2
  exit 1
fi

to_title() {
  echo "$1" | tr '-' ' ' | awk '{
    for (i = 1; i <= NF; i++) {
      $i = toupper(substr($i, 1, 1)) substr($i, 2)
    }
    print
  }'
}

section_from_url() {
  local url="$1"
  if [[ "$url" == *"/api-reference/ultra"* ]]; then
    echo "api"
  elif [[ "$url" == *"/portal/"* ]]; then
    echo "portal"
  else
    echo "developer"
  fi
}

slug_from_url() {
  local url="$1"
  if [[ "$url" =~ /api-reference/ultra$ ]] || [[ "$url" =~ /docs/ultra$ ]]; then
    echo "ultra"
  else
    echo "${url##*/}"
  fi
}

clean_filename() {
  local section="$1"
  local slug="$2"
  case "$section:$slug" in
    api:ultra) echo "overview" ;;
    api:order) echo "get-order" ;;
    api:execute) echo "execute-order" ;;
    api:holdings) echo "get-holdings" ;;
    api:shield) echo "get-shield" ;;
    api:search) echo "search-tokens" ;;
    api:routers) echo "list-routers" ;;
    api:balances) echo "get-balances-deprecated" ;;
    developer:ultra) echo "overview" ;;
    *) echo "$slug" ;;
  esac
}

title_for() {
  local section="$1"
  local slug="$2"
  case "$section:$slug" in
    api:ultra) echo "Ultra Swap API Overview" ;;
    api:order) echo "Ultra API: Get Order" ;;
    api:execute) echo "Ultra API: Execute Order" ;;
    api:holdings) echo "Ultra API: Get Holdings" ;;
    api:shield) echo "Ultra API: Get Shield" ;;
    api:search) echo "Ultra API: Search Tokens" ;;
    api:routers) echo "Ultra API: List Routers" ;;
    api:balances) echo "Ultra API: Get Balances (Deprecated)" ;;
    developer:ultra) echo "Ultra Developer Guide Overview" ;;
    developer:rate-limit) echo "Ultra Developer Guide: Rate Limit" ;;
    developer:response) echo "Ultra Developer Guide: Response" ;;
    portal:faq) echo "Portal: FAQ" ;;
    portal:setup) echo "Portal: API Key Setup" ;;
    portal:rate-limit) echo "Portal: Rate Limit" ;;
    portal:responses) echo "Portal: Responses" ;;
    portal:payment) echo "Portal: Payment Methods" ;;
    portal:latency) echo "Portal: Latency" ;;
    portal:migrate-from-lite-api) echo "Portal: Migrate From Lite API" ;;
    developer:*) echo "Ultra Developer Guide: $(to_title "$slug")" ;;
    portal:*) echo "Portal: $(to_title "$slug")" ;;
    *) echo "$(to_title "$slug")" ;;
  esac
}

clear_dir() {
  local dir="$1"
  find "$dir" -type f -name '*.md' -delete
}

clear_dir "$OUT_DIR/api"
clear_dir "$OUT_DIR/developer"
clear_dir "$OUT_DIR/portal"

while IFS= read -r url; do
  [[ -z "$url" ]] && continue

  section="$(section_from_url "$url")"
  slug="$(slug_from_url "$url")"
  base="${url#https://dev.jup.ag/}"
  raw_file="$RAW_DIR/$section/${base//\//__}.md"

  if [[ ! -f "$raw_file" ]]; then
    echo "Skipping missing raw file: $raw_file" >&2
    continue
  fi

  out_name="$(clean_filename "$section" "$slug")"
  out_file="$OUT_DIR/$section/${out_name}.md"
  title="$(title_for "$section" "$slug")"

  {
    echo "# $title"
    echo
    echo "- Source: $url"
    echo "- Snapshot: ../../raw/$section/${base//\//__}.md"
    echo
    echo "---"
    echo
    sed '/^> ## Documentation Index$/,/^$/d' "$raw_file" \
      | awk '
        BEGIN { replaced = 0 }
        {
          if (!replaced && $0 ~ /^# /) {
            print "## Source Content"
            print ""
            print "### " substr($0, 3)
            replaced = 1
            next
          }
          print
        }
      ' \
      | sed 's/^## OpenAPI$/## OpenAPI Specification/'
  } > "$out_file"
done < "$URLS_FILE"

make_index() {
  local section="$1"
  local heading="$2"
  local index_file="$OUT_DIR/$section/README.md"

  {
    echo "# $heading"
    echo
    echo "| File | Title |"
    echo "| --- | --- |"
    for file in "$OUT_DIR/$section"/*.md; do
      [[ "$(basename "$file")" == "README.md" ]] && continue
      title_line="$(sed -n '1s/^# //p' "$file")"
      rel_name="$(basename "$file")"
      echo "| [$rel_name](./$rel_name) | $title_line |"
    done | sort
  } > "$index_file"
}

make_index "api" "Ultra API Docs (Organized)"
make_index "developer" "Ultra Developer Docs (Organized)"
make_index "portal" "Ultra Portal Docs (Organized)"

cat > "$OUT_DIR/README.md" <<'INDEX'
# Jupiter Ultra Docs (Organized)

This directory contains cleaned, consistently titled snapshots generated from `references/raw/`.

## Sections

- [API](./api/README.md)
- [Developer](./developer/README.md)
- [Portal](./portal/README.md)

## Refresh Workflow

1. `bash jupiter-ultra/scripts/refresh_sources.sh`
2. `bash jupiter-ultra/scripts/fetch_docs.sh`
3. `bash jupiter-ultra/scripts/organize_docs.sh`
INDEX

echo "Organized docs written to $OUT_DIR"
