"""
verification_parser.py — Parse verification plans and test measurement sessions.

Reads Markdown files with YAML front matter and structured tables.
Used by verification_export.py to generate Excel and summary exports.

Dependencies: pyyaml
"""

import re
from pathlib import Path
from typing import Any

import yaml


def _split_front_matter(text: str) -> tuple[dict[str, Any], str]:
    """Split a Markdown file into YAML front matter and body."""
    match = re.match(r"^---\s*\n(.*?\n)---\s*\n", text, re.DOTALL)
    if not match:
        return {}, text
    front_matter = yaml.safe_load(match.group(1)) or {}
    body = text[match.end():]
    return front_matter, body


def _parse_markdown_table(lines: list[str]) -> list[dict[str, str]]:
    """Parse a GFM Markdown table into a list of row dicts.

    Expects: header row, separator row (|---|...), then data rows.
    Returns rows as dicts keyed by header names (stripped, lowercased).
    """
    if len(lines) < 2:
        return []

    # Find header row
    header_line = lines[0]
    headers = [h.strip() for h in header_line.strip().strip("|").split("|")]

    # Skip separator row (lines[1])
    rows = []
    for line in lines[2:]:
        line = line.strip()
        if not line or not line.startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        # Pad or trim to match header count
        while len(cells) < len(headers):
            cells.append("")
        row = {}
        for i, header in enumerate(headers):
            row[header] = cells[i] if i < len(cells) else ""
        rows.append(row)
    return rows


def _find_category_tables(body: str, categories: list[dict]) -> dict[str, list[dict[str, str]]]:
    """Find and parse the test step table under each ### Category heading."""
    result = {}
    category_names = {cat["name"]: cat["id"] for cat in categories}

    # Split body into sections by ### headings
    sections = re.split(r"^### (.+)$", body, flags=re.MULTILINE)
    # sections = [pre, heading1, content1, heading2, content2, ...]

    for i in range(1, len(sections), 2):
        heading = sections[i].strip()
        content = sections[i + 1] if i + 1 < len(sections) else ""

        if heading not in category_names:
            continue

        cat_id = category_names[heading]

        # Find the table in this section
        table_lines = []
        in_table = False
        for line in content.split("\n"):
            stripped = line.strip()
            if stripped.startswith("|") and not in_table:
                in_table = True
                table_lines.append(stripped)
            elif in_table and stripped.startswith("|"):
                table_lines.append(stripped)
            elif in_table:
                break

        rows = _parse_markdown_table(table_lines)
        # Tag each row with category id
        for row in rows:
            row["_category"] = cat_id
        result[cat_id] = rows

    return result


def parse_verification_plan(path: str | Path) -> dict[str, Any]:
    """Parse a VERIFICATION.md file.

    Returns:
        {
            "metadata": { product, revision, phase, ... },
            "categories": [ { id, name, color, slots }, ... ],
            "test_steps": { "M": [{ID, Step, ...}, ...], "P": [...], ... },
            "dut_slots": int,
        }
    """
    text = Path(path).read_text(encoding="utf-8")
    front_matter, body = _split_front_matter(text)

    categories = front_matter.get("categories", [])
    dut_slots = front_matter.get("dut_slots", 4)

    metadata = {
        k: v for k, v in front_matter.items()
        if k not in ("categories", "dut_slots")
    }

    test_steps = _find_category_tables(body, categories)

    return {
        "metadata": metadata,
        "categories": categories,
        "test_steps": test_steps,
        "dut_slots": dut_slots,
    }


def parse_test_session(path: str | Path) -> dict[str, Any]:
    """Parse a test measurement session file.

    Returns:
        {
            "session_id": str,
            "date": str,
            "engineer": str,
            "dut_id": str,
            "dut_serial": str,
            "categories_tested": [str, ...],
            "measurements": [ { ID, Measured DMM, ... }, ... ],
        }
    """
    text = Path(path).read_text(encoding="utf-8")
    front_matter, body = _split_front_matter(text)

    # Find the Measurements table
    measurements = []
    lines = body.split("\n")
    in_measurements = False
    table_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.lower().startswith("## measurement"):
            in_measurements = True
            continue
        if in_measurements and stripped.startswith("##"):
            break
        if in_measurements and stripped.startswith("|"):
            table_lines.append(stripped)

    measurements = _parse_markdown_table(table_lines)

    return {
        "session_id": front_matter.get("session_id", ""),
        "date": front_matter.get("date", ""),
        "engineer": front_matter.get("engineer", ""),
        "dut_id": front_matter.get("dut_id", ""),
        "dut_serial": front_matter.get("dut_serial", ""),
        "categories_tested": front_matter.get("categories_tested", []),
        "measurements": measurements,
    }


def collect_test_results(results_dir: str | Path) -> dict[str, list[dict[str, str]]]:
    """Scan all .md files in results_dir, parse sessions, group measurements by DUT serial.

    Returns:
        {
            "SN-00042": [ { ID, Measured DMM, ... }, ... ],
            "SN-00043": [ ... ],
        }
    """
    results_dir = Path(results_dir)
    by_serial: dict[str, list[dict[str, str]]] = {}

    if not results_dir.is_dir():
        return by_serial

    for md_file in sorted(results_dir.glob("*.md")):
        # Skip placeholder files
        if md_file.name.startswith("."):
            continue
        try:
            session = parse_test_session(md_file)
        except Exception:
            continue

        serial = session.get("dut_serial", "")
        if not serial or not session["measurements"]:
            continue

        if serial not in by_serial:
            by_serial[serial] = []
        by_serial[serial].extend(session["measurements"])

    return by_serial
