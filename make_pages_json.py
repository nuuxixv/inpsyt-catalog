#!/usr/bin/env python3
"""Generate pages.json from the extracted page text file."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

HEADER_PATTERN = re.compile(r"--- Page (\d+) ---\s*")

def parse_pages(text: str) -> list[dict]:
    parts = HEADER_PATTERN.split(text)
    if parts and not parts[0].strip():
        parts = parts[1:]
    pages = []
    for page_str, body in zip(parts[0::2], parts[1::2]):
        page_num = int(page_str)
        body = body.strip()
        lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
        title = lines[0] if lines else f"Page {page_num}"
        note = " ".join(lines[1:4]) if len(lines) > 1 else ""
        pages.append(
            {
                "page": page_num,
                "title": title[:80],
                "note": note[:160],
                "file": f"[inpsyt]2026Catalog_{page_num:03d}.webp",
                "text": body,
            }
        )
    return pages


def main() -> None:
    parser = argparse.ArgumentParser(description="Create pages.json from text dump")
    parser.add_argument(
        "text",
        type=Path,
        nargs="?",
        default=Path("2026_catalog_text.txt"),
        help="입력 텍스트 파일 경로",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("pages.json"),
        help="생성할 JSON 파일 경로",
    )
    args = parser.parse_args()

    content = args.text.read_text(encoding="utf-8")
    pages = parse_pages(content)
    args.output.write_text(json.dumps(pages, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved {args.output} ({len(pages)} pages)")


if __name__ == "__main__":
    main()
