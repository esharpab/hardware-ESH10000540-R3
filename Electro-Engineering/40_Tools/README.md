# report_builder.py

Generic, config-driven report generator. Reads a YAML spec + data files (CSVs, PNGs) and produces a structured Markdown report.

## Usage

```bash
python 40_Tools/report_builder.py \
    --spec  report_spec.yaml \
    --data-dir /path/to/run/data \
    --var run_name=TC4-2_rising_amb \
    --out  SLIDES/TC4-2_report.md \
    --copy-assets
```

### Arguments

| Arg | Required | Description |
|-----|----------|-------------|
| `--spec` | yes | Path to the YAML report spec |
| `--data-dir` | yes | Root directory for resolving `source` paths in spec |
| `--var KEY=VALUE` | no | Repeatable. Substitutes `{key}` in titles/captions/text |
| `--out` | yes | Output path for the generated .md file |
| `--copy-assets` | no | Copy referenced images to `{stem}_assets/` beside output |

## Spec format

```yaml
title: "Report title — {run_name}"
date: auto            # "auto" = today, or a fixed string
subtitle: "Optional"  # optional

sections:
  - heading: "Section Name"
    blocks:
      - type: table
        source: path/to/data.csv     # relative to --data-dir
        columns: [col1, col2, col3]  # optional: subset of columns
        sort_by: col2                # optional: sort column
        ascending: false             # optional: sort direction (default true)
        head: 25                     # optional: limit rows
        group_by: category           # optional: group + take top N per group
        group_head: 1                # optional: rows per group
        float_format: ".1f"          # optional: numeric format (default ".2f")
        caption: "Table caption"     # optional
        required: false              # optional: skip if file missing (default true)

      - type: image
        source: plots/chart.png      # relative to --data-dir
        caption: "Chart description"
        required: false

      - type: images
        glob: "plots/02_*.png"       # glob relative to --data-dir
        required: false

      - type: text
        content: |
          Free-form Markdown text.
          Supports {variable} substitution.
```

## Block types

| Type | Purpose |
|------|---------|
| `table` | Read CSV, optionally filter/sort/group, render as GFM Markdown table |
| `image` | Embed a single image |
| `images` | Glob-expand multiple images |
| `text` | Literal Markdown text with `{var}` substitution |

All blocks support `required: false` — skipped silently if source file is missing.

## Dependencies

Python stdlib + `pandas` + `pyyaml`.
