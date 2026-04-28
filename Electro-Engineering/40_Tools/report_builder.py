"""report_builder.py — Generate structured Markdown reports from a YAML spec.

Reads a report spec (YAML) and assembles a Markdown report by reading
CSVs, embedding images, and formatting tables.  Generic: not tied to
any project's data schema.

Usage:
    python 40_Tools/report_builder.py \\
        --spec  20_Projects/Project-B12_Thermal/report_spec.yaml \\
        --data-dir c:/Git/b12_thermal/B12_test_runs/TC4-2_rising_amb \\
        --var run_name=TC4-2_rising_amb \\
        --out   20_Projects/Project-B12_Thermal/SLIDES/TC4-2_report.md \\
        --copy-assets

Dependencies: Python stdlib + pandas + pyyaml.
"""

from __future__ import annotations

import argparse
import datetime
import glob as globmod
import os
import shutil
import sys
from pathlib import Path

import pandas as pd
import yaml


# ---------------------------------------------------------------------------
# Markdown table helper
# ---------------------------------------------------------------------------

def df_to_markdown(df: pd.DataFrame, float_format: str = ".2f") -> str:
    """Convert a DataFrame to a GitHub-flavored Markdown table."""
    lines: list[str] = []

    # Header
    lines.append("| " + " | ".join(str(c) for c in df.columns) + " |")

    # Alignment row — right-align numeric columns
    aligns: list[str] = []
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            aligns.append("---:")
        else:
            aligns.append("---")
    lines.append("| " + " | ".join(aligns) + " |")

    # Data rows
    for _, row in df.iterrows():
        cells: list[str] = []
        for col in df.columns:
            val = row[col]
            if pd.isna(val):
                cells.append("")
            elif isinstance(val, float):
                if val == int(val):
                    cells.append(str(int(val)))
                else:
                    cells.append(f"{val:{float_format}}")
            else:
                cells.append(str(val))
        lines.append("| " + " | ".join(cells) + " |")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Block renderers
# ---------------------------------------------------------------------------

def _resolve_source(source: str, data_dir: Path) -> Path:
    """Resolve a source path relative to data_dir."""
    return data_dir / source


def _asset_path(src: Path, out_dir: Path, copy: bool) -> str:
    """Return the Markdown-relative path for an image.

    If *copy* is True, copies the file into {out_stem}_assets/ beside the
    output file and returns the relative path.  Otherwise returns the
    absolute path to the original.
    """
    if copy:
        assets_dir = out_dir
        assets_dir.mkdir(parents=True, exist_ok=True)
        dst = assets_dir / src.name
        if not dst.exists():
            shutil.copy2(src, dst)
        # Return path relative from the output .md's parent
        return dst.name
    return str(src)


def render_table(block: dict, data_dir: Path, variables: dict) -> str:
    """Read a CSV and render it as a GFM Markdown table."""
    src = _resolve_source(block["source"], data_dir)
    if not src.exists():
        if block.get("required", True):
            print(f"  [ERROR] Missing required file: {src}", file=sys.stderr)
            sys.exit(1)
        return ""

    df = pd.read_csv(src)

    # Column subset
    columns = block.get("columns")
    if columns:
        missing = [c for c in columns if c not in df.columns]
        if missing:
            print(f"  [WARN] Columns not found in {src.name}: {missing}",
                  file=sys.stderr)
        columns = [c for c in columns if c in df.columns]
        df = df[columns]

    # Sort
    sort_by = block.get("sort_by")
    if sort_by and sort_by in df.columns:
        df = df.sort_values(sort_by, ascending=block.get("ascending", True))

    # Group-by + group_head (e.g. worst sensor per group)
    group_by = block.get("group_by")
    group_head = block.get("group_head")
    if group_by and group_head and group_by in df.columns:
        df = df.groupby(group_by, sort=False).head(group_head).reset_index(drop=True)

    # Head limit
    head = block.get("head")
    if head:
        df = df.head(head)

    float_fmt = block.get("float_format", ".2f")
    table_md = df_to_markdown(df, float_format=float_fmt)

    parts: list[str] = []
    caption = block.get("caption")
    if caption:
        parts.append(f"**{_substitute(caption, variables)}**\n")
    parts.append(table_md)
    return "\n".join(parts)


def render_image(block: dict, data_dir: Path, assets_dir: Path | None,
                 copy: bool, variables: dict) -> str:
    """Render a single image embed."""
    src = _resolve_source(block["source"], data_dir)
    if not src.exists():
        if block.get("required", True):
            print(f"  [ERROR] Missing required file: {src}", file=sys.stderr)
            sys.exit(1)
        return ""

    caption = block.get("caption", src.stem)
    caption = _substitute(caption, variables)
    path = _asset_path(src, assets_dir, copy) if assets_dir else str(src)
    return f"![{caption}]({path})"


def render_images(block: dict, data_dir: Path, assets_dir: Path | None,
                  copy: bool, variables: dict) -> str:
    """Glob-expand and render multiple image embeds."""
    pattern = block.get("glob", "")
    matches = sorted(globmod.glob(str(data_dir / pattern)))
    if not matches:
        if block.get("required", True):
            print(f"  [WARN] No files matched glob: {pattern}", file=sys.stderr)
        return ""

    parts: list[str] = []
    for m in matches:
        src = Path(m)
        caption = src.stem
        path = _asset_path(src, assets_dir, copy) if assets_dir else str(src)
        parts.append(f"![{caption}]({path})")
    return "\n\n".join(parts)


def render_text(block: dict, variables: dict) -> str:
    """Render literal text with {var} substitution."""
    content = block.get("content", "")
    return _substitute(content, variables)


# ---------------------------------------------------------------------------
# Variable substitution
# ---------------------------------------------------------------------------

def _substitute(text: str, variables: dict) -> str:
    """Replace {key} placeholders with variable values."""
    for key, val in variables.items():
        text = text.replace(f"{{{key}}}", val)
    return text


# ---------------------------------------------------------------------------
# Main assembly
# ---------------------------------------------------------------------------

RENDERERS = {
    "table": render_table,
    "image": render_image,
    "images": render_images,
    "text": render_text,
}


def build_report(spec: dict, data_dir: Path, variables: dict,
                 out_path: Path, copy_assets: bool) -> str:
    """Assemble the full Markdown report from a parsed spec."""
    parts: list[str] = []

    # Title
    title = spec.get("title", "Report")
    parts.append(f"# {_substitute(title, variables)}")

    # Date
    date_val = spec.get("date")
    if date_val == "auto":
        date_val = datetime.date.today().isoformat()
    if date_val:
        parts.append(f"\n*Generated: {date_val}*")

    # Subtitle
    subtitle = spec.get("subtitle")
    if subtitle:
        parts.append(f"\n*{_substitute(subtitle, variables)}*")

    # Assets directory (beside output file)
    assets_dir = None
    if copy_assets:
        assets_dir = out_path.parent / f"{out_path.stem}_assets"

    # Sections
    for section in spec.get("sections", []):
        heading = section.get("heading", "")
        section_parts: list[str] = []

        for block in section.get("blocks", []):
            block_type = block.get("type", "")
            if block_type == "table":
                result = render_table(block, data_dir, variables)
            elif block_type == "image":
                result = render_image(block, data_dir, assets_dir,
                                      copy_assets, variables)
            elif block_type == "images":
                result = render_images(block, data_dir, assets_dir,
                                       copy_assets, variables)
            elif block_type == "text":
                result = render_text(block, variables)
            else:
                print(f"  [WARN] Unknown block type: {block_type}",
                      file=sys.stderr)
                continue

            if result:
                section_parts.append(result)

        # Only emit section if at least one block produced output
        if section_parts:
            parts.append(f"\n---\n\n## {_substitute(heading, variables)}")
            parts.extend(section_parts)

    parts.append("\n---\n\n*Report generated by report_builder.py*\n")
    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a Markdown report from a YAML spec + data files.")
    parser.add_argument("--spec", required=True,
                        help="Path to the YAML report spec.")
    parser.add_argument("--data-dir", required=True,
                        help="Root directory for resolving source paths in the spec.")
    parser.add_argument("--var", action="append", default=[],
                        help="KEY=VALUE variable for {key} substitution (repeatable).")
    parser.add_argument("--out", required=True,
                        help="Output path for the generated .md file.")
    parser.add_argument("--copy-assets", action="store_true",
                        help="Copy images to {stem}_assets/ beside the output file.")
    args = parser.parse_args()

    # Parse variables
    variables: dict[str, str] = {}
    for var in args.var:
        if "=" not in var:
            print(f"ERROR: --var must be KEY=VALUE, got: {var}", file=sys.stderr)
            return 1
        key, val = var.split("=", 1)
        variables[key] = val

    # Load spec
    spec_path = Path(args.spec)
    if not spec_path.exists():
        print(f"ERROR: Spec file not found: {spec_path}", file=sys.stderr)
        return 1
    with open(spec_path, encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    # Validate data dir
    data_dir = Path(args.data_dir)
    if not data_dir.is_dir():
        print(f"ERROR: Data directory not found: {data_dir}", file=sys.stderr)
        return 1

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Build report
    report = build_report(spec, data_dir, variables, out_path, args.copy_assets)

    out_path.write_text(report, encoding="utf-8")
    print(f"Report written to: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
