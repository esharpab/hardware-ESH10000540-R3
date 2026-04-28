# Workflow: Verification Export

Export a Markdown-based verification plan (with optional test results) to Excel or a Markdown summary.

---

## Prerequisites

- Python 3.10+
- Packages: `openpyxl`, `pyyaml` (install via `pip install openpyxl pyyaml`)

---

## Export to Excel

Generates an `.xlsx` file matching the standard DUT verification sheet layout (categories, measurement columns per serial, conditional formatting).

```
cd 40_Tools/
python verification_export.py excel \
    --plan ../20_Projects/Project-ESH10000597/R0/VERIFICATION.md \
    --results ../20_Projects/Project-ESH10000597/R0/TEST_RESULTS/ \
    --out ../20_Projects/Project-ESH10000597/R0/DOCS/ESH10000597_VER_export.xlsx
```

- `--plan` — path to the VERIFICATION.md (v2 format with YAML front matter)
- `--results` — path to TEST_RESULTS/ directory containing measurement session files (optional)
- `--out` — output .xlsx path

If `--results` is omitted, the Excel contains only the test step definitions (no measurement data).

---

## Export Markdown summary

Generates a summary report with pass/fail counts per category, failure details, and DUT summary.

```
cd 40_Tools/
python verification_export.py summary \
    --plan ../20_Projects/Project-ESH10000597/R0/VERIFICATION.md \
    --results ../20_Projects/Project-ESH10000597/R0/TEST_RESULTS/ \
    --out ../20_Projects/Project-ESH10000597/R0/DOCS/ESH10000597_summary.md
```

### Converting to PDF

The summary Markdown can be converted to PDF using any of these methods:

1. **Pandoc** (if installed): `pandoc summary.md -o summary.pdf`
2. **VS Code**: Open the .md file → Ctrl+Shift+P → "Markdown PDF: Export (pdf)"
3. **Browser**: Open in any Markdown viewer and print to PDF

---

## Workflow: Prototype → Batch

1. **Prototype phase**: Fill in VERIFICATION.md with test steps. Run tests on a single DUT, recording results as measurement session files in TEST_RESULTS/.
2. **Batch phase**: Test additional DUTs using the same plan. Each session file links to a different `dut_serial`. The export tool merges all serials into the Excel (up to `dut_slots` columns).
3. **Export**: Run the Excel export to get a single sheet with all DUT results side by side.

---

## File format reference

### VERIFICATION.md (v2)

- YAML front matter: `product`, `revision`, `phase`, `engineer`, `dut_slots`, `categories` (list of `{id, name, color, slots}`)
- Body: One `### CategoryName` section per category, each containing a GFM table with columns: `ID | Step | Function | Test | Signals | Nominal | Unit | Tolerance`

### Test measurement session (.md)

- YAML front matter: `session_id`, `date`, `engineer`, `dut_id`, `dut_serial`, `categories_tested`
- Body: `## Measurements` section with a GFM table: `ID | Measured DMM | Measured ADC Min | Measured ADC Max | Pass/Fail | Comment`

Templates for both are in `60_Templates/`.
