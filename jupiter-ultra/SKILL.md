---
name: jupiter-ultra
description: Jupiter Ultra Swap specialist for API integration and troubleshooting. Use when building, debugging, or reviewing Jupiter Ultra flows (order, execute, balances, holdings, routers, search, shield), rate limits, portal setup, API keys, migration from Lite API, and integrator fee/payer configuration.
---

# Jupiter Ultra Skill

Use the local reference snapshots first, and refresh them when the user asks for the latest docs.

## Workflow

1. Identify request type:
- Endpoint behavior or payloads: use `references/docs/api/`.
- Integration guides and concepts: use `references/docs/developer/`.
- API key, quota, payment, migration, and portal settings: use `references/docs/portal/`.

2. Pull evidence from raw docs:
- Search formatted snapshots with `rg` for endpoint paths, field names, or phrases.
- Prefer exact API paths (for example `/ultra/v1/order`, `/ultra/v1/execute`) when extracting details.

3. Keep answers implementation-focused:
- Return concrete request/response guidance, required fields, and gotchas.
- Call out uncertainty if a field or behavior is not explicit in the snapshot.

4. Refresh docs when needed:
- Run `scripts/refresh_sources.sh` to rebuild `references/source-urls.txt` from sitemap filters.
- Run `scripts/fetch_docs.sh` to re-download all tracked pages into `references/raw/`.
- Run `scripts/build_pretty_docs.py` to regenerate formatted docs under `references/docs/`.

## Local Resources

- URL list: `references/source-urls.txt`
- Formatted root index: `references/docs/README.md`
- Formatted API index: `references/docs/api/README.md`
- Formatted developer index: `references/docs/developer/README.md`
- Formatted portal index: `references/docs/portal/README.md`
- Raw API pages: `references/raw/api/`
- Raw developer pages: `references/raw/developer/`
- Raw portal pages: `references/raw/portal/`
