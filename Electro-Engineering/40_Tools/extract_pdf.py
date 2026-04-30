"""
extract_pdf.py — Extract text from a datasheet PDF for AI-assisted COMPONENT_DATA entry.

Outputs a plain-text file alongside the PDF (or to a specified path) with:
  - A summary header (filename, pages, file size, extraction timestamp)
  - Page-delimited text blocks for easy section navigation
  - A table-of-contents estimate (lines that look like section headings)

Usage:
    python extract_pdf.py <pdf_path> [options]

Options:
    --out <path>        Output .txt file path (default: same dir as PDF, .txt extension)
    --pages <a>-<b>     Extract only pages a to b (1-indexed, inclusive), e.g. --pages 5-12
    --toc               Print estimated table of contents to stdout and exit (no file written)
    --stdout            Print extracted text to stdout instead of writing a file
    --summary           Print one-line file summary and exit

Examples:
    python extract_pdf.py 70_Assets/LT3942.pdf
    python extract_pdf.py 70_Assets/SX1276.pdf --pages 1-20
    python extract_pdf.py 70_Assets/WM8962B.pdf --toc
    python extract_pdf.py 70_Assets/LT3942.pdf --stdout | head -100

Dependencies: PyMuPDF (pip install pymupdf)
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _require_fitz():
    try:
        import fitz  # noqa: F401
    except ImportError:
        print("ERROR: PyMuPDF is not installed. Run: pip install pymupdf", file=sys.stderr)
        sys.exit(1)
    return __import__("fitz")


def _format_size(n_bytes: int) -> str:
    if n_bytes >= 1_048_576:
        return f"{n_bytes / 1_048_576:.1f} MB"
    return f"{n_bytes / 1024:.0f} KB"


def _looks_like_heading(line: str) -> bool:
    """Heuristic: short lines that are ALL-CAPS, Title Case, or end with a digit (table/section numbers)."""
    s = line.strip()
    if not s or len(s) > 80:
        return False
    if len(s) < 3:
        return False
    # All uppercase words (common in datasheets: "PIN DESCRIPTION", "ELECTRICAL CHARACTERISTICS")
    words = s.split()
    if all(w.isupper() or not w.isalpha() for w in words) and any(w.isalpha() for w in words):
        return True
    # Title case line with no sentence punctuation
    if s[0].isupper() and not s.endswith((",", ";", "–", "—")) and sum(1 for c in s if c == " ") <= 6:
        return True
    return False


# ---------------------------------------------------------------------------
# Core extraction
# ---------------------------------------------------------------------------

def open_pdf(path: str):
    fitz = _require_fitz()
    try:
        doc = fitz.open(path)
    except Exception as e:
        print(f"ERROR: Could not open PDF: {e}", file=sys.stderr)
        sys.exit(1)
    return doc


def extract_pages(doc, first: int, last: int) -> list[tuple[int, str]]:
    """Return list of (page_number_1indexed, text) for pages first..last (1-indexed, inclusive)."""
    results = []
    total = len(doc)
    first = max(1, first)
    last = min(total, last)
    for i in range(first - 1, last):
        text = doc[i].get_text()
        results.append((i + 1, text))
    return results


def build_toc(doc, first: int, last: int) -> list[str]:
    """Return candidate heading lines with page numbers."""
    toc_lines = []
    seen = set()
    for page_num, text in extract_pages(doc, first, last):
        for line in text.splitlines():
            s = line.strip()
            if s and _looks_like_heading(s) and s not in seen:
                seen.add(s)
                toc_lines.append(f"  p{page_num:>4}  {s}")
    return toc_lines


def format_output(pdf_path: str, doc, pages: list[tuple[int, str]]) -> str:
    """Build the full extracted text string."""
    total_pages = len(doc)
    file_size = _format_size(os.path.getsize(pdf_path))
    extracted_now = datetime.now().strftime("%Y-%m-%d %H:%M")
    first_page = pages[0][0] if pages else 1
    last_page = pages[-1][0] if pages else total_pages

    header_lines = [
        "=" * 72,
        f"  FILE:      {os.path.basename(pdf_path)}",
        f"  PATH:      {pdf_path}",
        f"  PAGES:     {total_pages} total  |  extracted: {first_page}–{last_page}",
        f"  SIZE:      {file_size}",
        f"  EXTRACTED: {extracted_now}",
        "=" * 72,
        "",
        "USAGE NOTE: Feed to AI using the extraction prompt in",
        "  30_Workflows/component-data-workflow.md",
        "",
    ]

    body_parts = ["\n".join(header_lines)]
    for page_num, text in pages:
        separator = f"\n{'─' * 72}\n  PAGE {page_num} / {total_pages}\n{'─' * 72}\n"
        body_parts.append(separator + text)

    return "\n".join(body_parts)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_page_range(spec: str, total: int) -> tuple[int, int]:
    """Parse '5-12' or '5' into (first, last) (1-indexed)."""
    spec = spec.strip()
    if "-" in spec:
        parts = spec.split("-", 1)
        try:
            first, last = int(parts[0]), int(parts[1])
        except ValueError:
            print(f"ERROR: Invalid page range '{spec}'. Use format: 5-12", file=sys.stderr)
            sys.exit(1)
    else:
        try:
            first = last = int(spec)
        except ValueError:
            print(f"ERROR: Invalid page number '{spec}'.", file=sys.stderr)
            sys.exit(1)
    if first < 1 or last < first or last > total:
        print(
            f"ERROR: Page range {first}–{last} is out of bounds (document has {total} pages).",
            file=sys.stderr,
        )
        sys.exit(1)
    return first, last


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from a datasheet PDF for AI-assisted COMPONENT_DATA entry.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("pdf", help="Path to the PDF file")
    parser.add_argument("--out", metavar="PATH", help="Output .txt file path")
    parser.add_argument(
        "--pages",
        metavar="A-B",
        help="Extract only pages A to B (1-indexed, inclusive)",
    )
    parser.add_argument(
        "--toc",
        action="store_true",
        help="Print estimated table of contents to stdout and exit",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print extracted text to stdout instead of writing a file",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print one-line file summary and exit",
    )
    args = parser.parse_args()

    pdf_path = args.pdf
    if not os.path.isfile(pdf_path):
        print(f"ERROR: File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    doc = open_pdf(pdf_path)
    total_pages = len(doc)
    file_size = _format_size(os.path.getsize(pdf_path))

    # --summary: one-liner and exit
    if args.summary:
        print(f"{os.path.basename(pdf_path):<40} {total_pages:>4} pages  {file_size:>8}")
        return

    first, last = (1, total_pages)
    if args.pages:
        first, last = parse_page_range(args.pages, total_pages)

    # --toc: print candidate headings and exit
    if args.toc:
        print(f"Estimated TOC for: {os.path.basename(pdf_path)} ({total_pages} pages)")
        print(f"Pages {first}–{last}\n")
        toc = build_toc(doc, first, last)
        if toc:
            print("\n".join(toc))
        else:
            print("  (no headings detected)")
        return

    # Extract text
    pages = extract_pages(doc, first, last)
    output_text = format_output(pdf_path, doc, pages)

    # --stdout: print and exit
    if args.stdout:
        print(output_text)
        return

    # Write file
    if args.out:
        out_path = Path(args.out)
    else:
        out_path = Path(pdf_path).with_suffix(".txt")

    out_path.write_text(output_text, encoding="utf-8")

    page_info = f"pages {first}–{last}" if (first, last) != (1, total_pages) else "all pages"
    print(f"Extracted {last - first + 1} pages ({page_info}) → {out_path}")
    print(f"File size: {_format_size(out_path.stat().st_size)}")


if __name__ == "__main__":
    main()
