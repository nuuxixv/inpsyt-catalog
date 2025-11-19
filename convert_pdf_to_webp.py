#!/usr/bin/env python3
"""
PDF 페이지를 WebP(최소 압축)로 변환합니다.
사용법:
    python convert_pdf_to_webp.py "경로/2026Catalog.pdf" --output-dir "경로/webp"
출력 파일명:
    [inpsyt]2026Catalog_001.webp ~ [inpsyt]2026Catalog_nnn.webp
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

import pypdfium2 as pdfium
from PIL import Image


def convert(
    pdf_path: Path,
    output_dir: Path,
    *,
    width: int,
    start_page: int,
    end_page: Optional[int],
    quality: int,
    lossless: bool,
    overwrite: bool,
) -> None:
    pdf = pdfium.PdfDocument(str(pdf_path))
    output_dir.mkdir(parents=True, exist_ok=True)

    total_pages = len(pdf)
    start = max(1, start_page)
    stop = total_pages if end_page in (None, 0) else min(total_pages, end_page)
    if start > stop:
        raise SystemExit("시작 페이지가 끝 페이지보다 큽니다.")

    for page_number in range(start, stop + 1):
        page = pdf[page_number - 1]
        width_pts = page.get_width() or 1
        scale = width / width_pts
        pil_image = page.render(scale=scale).to_pil()

        if pil_image.width != width:
            new_height = int(pil_image.height * (width / pil_image.width))
            pil_image = pil_image.resize((width, new_height), Image.LANCZOS)

        filename = output_dir / f"[inpsyt]2026Catalog_{page_number:03d}.webp"
        if not overwrite and filename.exists():
            print(f"Skip {filename} (already exists)")
            continue

        pil_image.save(
            filename,
            format="WEBP",
            lossless=lossless,
            quality=quality,
            method=6,
        )
        print(f"Saved {filename}")


def main() -> None:
    parser = argparse.ArgumentParser(description="PDF를 WebP로 변환")
    parser.add_argument(
        "pdf",
        type=Path,
        help=r"변환할 PDF 경로 (예: C:\Users\김건우\Desktop\VS\catalog\2026 인싸이트 카달로그.pdf)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=r"결과 저장 폴더 경로 (예: C:\Users\김건우\Desktop\VS\catalog\webp)",
    )
    parser.add_argument("--width", type=int, default=1440, help="최종 WebP 가로폭")
    parser.add_argument("--start", type=int, default=1, help="시작 페이지 (1-based)")
    parser.add_argument("--end", type=int, default=0, help="끝 페이지 (0은 전체)")
    parser.add_argument("--quality", type=int, default=75, help="WebP 품질 (0-100)")
    parser.add_argument(
        "--lossless",
        action="store_true",
        help="무손실 WebP로 저장 (용량이 커집니다)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="이미 생성된 WebP가 있어도 덮어씁니다.",
    )
    args = parser.parse_args()

    pdf_path = args.pdf.expanduser().resolve()
    if not pdf_path.exists():
        raise SystemExit(f"PDF를 찾을 수 없습니다: {pdf_path}")

    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir
        else pdf_path.with_suffix("")
    )
    convert(
        pdf_path,
        output_dir,
        width=args.width,
        start_page=args.start,
        end_page=args.end if args.end > 0 else None,
        quality=args.quality,
        lossless=args.lossless,
        overwrite=args.overwrite,
    )


if __name__ == "__main__":
    main()
