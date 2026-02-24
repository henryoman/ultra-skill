---
name: jupiter-ultra
description: Jupiter Ultra Swap specialist for API integration and troubleshooting. Use when building, debugging, or reviewing Jupiter Ultra flows (order, execute, balances, holdings, routers, search, shield), rate limits, portal setup, API keys, migration from Lite API, and integrator fee/payer configuration.
---

# Jupiter Ultra Skill

Use the local reference snapshots first, and refresh them when the user asks for the latest docs.

## Workflow

1. Identify request type:
- Endpoint behavior or payloads: use `references/api-docs.md` and `references/raw/api/`.
- Integration guides and concepts: use `references/developer-docs.md` and `references/raw/developer/`.
- API key, quota, payment, migration, and portal settings: use `references/portal-docs.md` and `references/raw/portal/`.

2. Pull evidence from raw docs:
- Search raw snapshots with `rg` for endpoint paths, field names, or phrases.
- Prefer exact API paths (for example `/ultra/v1/order`, `/ultra/v1/execute`) when extracting details.

3. Keep answers implementation-focused:
- Return concrete request/response guidance, required fields, and gotchas.
- Call out uncertainty if a field or behavior is not explicit in the snapshot.

4. Refresh docs when needed:
- Run `scripts/refresh_sources.sh` to rebuild `references/source-urls.txt` from sitemap filters.
- Run `scripts/fetch_docs.sh` to re-download all tracked pages into `references/raw/`.

## Local Resources

- URL list: `references/source-urls.txt`
- API index: `references/api-docs.md`
- Developer index: `references/developer-docs.md`
- Portal index: `references/portal-docs.md`
- Raw API pages: `references/raw/api/`
- Raw developer pages: `references/raw/developer/`
- Raw portal pages: `references/raw/portal/`
