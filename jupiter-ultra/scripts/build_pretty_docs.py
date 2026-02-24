#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "references" / "raw"
URLS_FILE = ROOT / "references" / "source-urls.txt"
OUT = ROOT / "references" / "docs"

WEB3_PATTERNS = [
    r"@solana/web3\.js",
    r"\bweb3\.js\b",
    r"\bVersionedTransaction\b",
    r"\bTransactionMessage\b",
    r"\bConnection\s*\(",
    r"\bKeypair\.fromSecretKey\b",
    r"\bsendRawTransaction\b",
    r"\bsendAndConfirmRawTransaction\b",
]
WEB3_RE = re.compile("|".join(WEB3_PATTERNS), re.IGNORECASE)
FENCE_RE = re.compile(r"```(?P<lang>[a-zA-Z0-9_-]*)\n(?P<body>.*?)\n```", re.DOTALL)


def section_for_url(url: str) -> str:
    if "/api-reference/ultra" in url:
        return "api"
    if "/portal/" in url:
        return "portal"
    return "developer"


def raw_file_for_url(url: str) -> Path:
    slug = url.replace("https://dev.jup.ag/", "").replace("/", "__") + ".md"
    return RAW / section_for_url(url) / slug


def clean_leading_index_notice(text: str) -> str:
    lines = text.splitlines()
    if len(lines) >= 4 and lines[0].startswith("> ## Documentation Index"):
        i = 0
        while i < len(lines) and lines[i].startswith(">"):
            i += 1
        while i < len(lines) and lines[i].strip() == "":
            i += 1
        return "\n".join(lines[i:]).strip() + "\n"
    return text


def remove_web3_code_blocks(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        lang = (m.group("lang") or "").lower()
        body = m.group("body")
        if WEB3_RE.search(body):
            return "\n> Removed incompatible SDK example; use API fetch or Solana Kit flow instead.\n"
        return m.group(0)

    out = FENCE_RE.sub(repl, text)
    # Remove Accordion blocks that contain incompatible SDK snippets.
    out = re.sub(
        r"<Accordion[^>]*>.*?</Accordion>",
        lambda m: (
            "\n> Removed incompatible SDK example; use API fetch or Solana Kit flow instead.\n"
            if WEB3_RE.search(m.group(0))
            else m.group(0)
        ),
        out,
        flags=re.DOTALL | re.IGNORECASE,
    )
    out = re.sub(r"^.*web3\.js.*$\n?", "", out, flags=re.IGNORECASE | re.MULTILINE)
    out = re.sub(rf"^.*(?:{WEB3_RE.pattern}).*$\n?", "", out, flags=re.IGNORECASE | re.MULTILINE)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.strip() + "\n"


def get_title(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    if m:
        return m.group(1).strip()
    return fallback


def nice_name(url: str) -> str:
    path = url.replace("https://dev.jup.ag", "").strip("/")
    parts = path.split("/")
    leaf = parts[-1]
    if leaf in {"ultra", "api-reference", "docs", "portal"}:
        return "index"
    return leaf


def fallback_title(url: str) -> str:
    path = url.replace("https://dev.jup.ag", "").strip("/")
    return path.replace("/", " - ").replace("-", " ").title()


def js_fetch_example(url: str, section: str) -> str:
    api_path = ""
    method = "GET"
    if section == "api":
        p = url.split("/api-reference/ultra", 1)[1]
        if p in ("", "/"):
            api_path = "/ultra/v1/order"
        else:
            tail = p.strip("/")
            api_path = f"/ultra/v1/{tail}"
        if api_path.endswith("/execute"):
            method = "POST"
    elif section == "developer":
        api_path = "/ultra/v1/order"
        method = "GET"
    else:
        api_path = "/ultra/v1/order"
        method = "GET"

    if method == "GET":
        return (
            "## JavaScript Example (API)\n\n"
            "```js\n"
            "const url = new URL('https://api.jup.ag" + api_path + "');\n"
            "// Add required params as needed for this endpoint\n"
            "// url.searchParams.set('inputMint', '<MINT>');\n"
            "// url.searchParams.set('outputMint', '<MINT>');\n"
            "// url.searchParams.set('amount', '<AMOUNT_IN_BASE_UNITS>');\n"
            "\n"
            "const res = await fetch(url, {\n"
            "  headers: { 'x-api-key': process.env.JUP_API_KEY }\n"
            "});\n"
            "const data = await res.json();\n"
            "console.log(data);\n"
            "```\n"
        )

    return (
        "## JavaScript Example (API)\n\n"
        "```js\n"
        "const res = await fetch('https://api.jup.ag" + api_path + "', {\n"
        "  method: 'POST',\n"
        "  headers: {\n"
        "    'Content-Type': 'application/json',\n"
        "    'x-api-key': process.env.JUP_API_KEY\n"
        "  },\n"
        "  body: JSON.stringify({\n"
        "    // order response + signedTransaction inputs\n"
        "  })\n"
        "});\n"
        "const data = await res.json();\n"
        "console.log(data);\n"
        "```\n"
    )


def ensure_js_example(text: str, url: str, section: str) -> str:
    if re.search(r"```(?:js|javascript)\b", text, flags=re.IGNORECASE):
        return text
    return text.rstrip() + "\n\n" + js_fetch_example(url, section)


def make_doc(url: str) -> tuple[str, str, str]:
    section = section_for_url(url)
    src = raw_file_for_url(url)
    if not src.exists():
        raise FileNotFoundError(f"Missing raw doc for URL: {url} -> {src}")

    text = src.read_text(encoding="utf-8")
    text = clean_leading_index_notice(text)
    text = remove_web3_code_blocks(text)
    text = ensure_js_example(text, url, section)

    title = get_title(text, fallback_title(url))
    name = nice_name(url)

    out_dir = OUT / section
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{name}.md"

    header = (
        f"---\n"
        f"title: {title}\n"
        f"source_url: {url}\n"
        f"section: {section}\n"
        f"---\n\n"
    )
    out_path.write_text(header + text, encoding="utf-8")
    return section, title, str(out_path.relative_to(ROOT))


def write_index(section: str, rows: list[tuple[str, str]]) -> None:
    folder = OUT / section
    index_path = folder / "README.md"
    title = {
        "api": "Jupiter Ultra API Docs",
        "developer": "Jupiter Ultra Developer Docs",
        "portal": "Jupiter Ultra Portal Docs",
    }[section]

    lines = [
        f"# {title}",
        "",
        f"High-signal, cleaned markdown pages for `{section}`.",
        "",
        "## Pages",
        "",
        "| Page | File |",
        "| :--- | :--- |",
    ]
    for page_title, filename in sorted(rows, key=lambda x: x[0].lower()):
        lines.append(f"| {page_title} | [{filename}](./{filename}) |")
    lines.append("")
    index_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    urls = [u.strip() for u in URLS_FILE.read_text(encoding="utf-8").splitlines() if u.strip()]
    produced: dict[str, list[tuple[str, str]]] = {"api": [], "developer": [], "portal": []}

    for url in urls:
        section, title, rel_path = make_doc(url)
        filename = Path(rel_path).name
        produced[section].append((title, filename))

    for section, rows in produced.items():
        write_index(section, rows)

    root_readme = OUT / "README.md"
    root_readme.write_text(
        "# Jupiter Ultra Docs\n\n"
        "Structured markdown docs with clean titles, section folders, and JavaScript API examples.\n\n"
        "## Sections\n\n"
        "| Section | Pages | Index |\n"
        "| :--- | ---: | :--- |\n"
        f"| API | {len(produced['api'])} | [Open](./api/README.md) |\n"
        f"| Developer | {len(produced['developer'])} | [Open](./developer/README.md) |\n"
        f"| Portal | {len(produced['portal'])} | [Open](./portal/README.md) |\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
