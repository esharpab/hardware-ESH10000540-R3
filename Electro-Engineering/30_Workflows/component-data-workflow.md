# Workflow: Component Data Management

**Purpose:** Maintain a single, authoritative global reference for component datasheet data across all E-Sharp engineering projects.  
**File:** [`COMPONENT_DATA.md`](../COMPONENT_DATA.md) — root of `Electro-Engineering/`  
**Authority:** The global file supersedes any per-project `COMPONENT_DATA.md` files.

---

## What belongs in COMPONENT_DATA.md

**Include (datasheet-sourced):**
- Pin descriptions and pin functions
- Key electrical parameters (min/typ/max tables)
- Design formulas (voltage dividers, current programming, frequency setting, etc.)
- Operating modes and state machines
- Register maps and power-on reset defaults
- SPI/I2C protocol details
- Recommended layout guidelines from the datasheet
- Crystal load capacitance requirements
- RF matching network topologies (generic — not project values)
- Device variant tables

**Do not include (keep in project files):**
- Net names and schematic signal assignments ("IO4 → LORA_NSS")
- Specific GPIO assignments tied to a board
- Project-specific BOM reference designators (R1, C5, U3)
- Requirement IDs (REQ-xxx, DEC-xxx, ISS-xxx)
- Circuit subsystem descriptions (e.g. "Current Sense Circuit")
- Connector pinout tables specific to one board

**Project-specific notes (optional — tagged):**
Concise project-specific context may be included at the bottom of a component entry, clearly tagged:

```
> **[ESHxxxxxxxx Rx]:** <note — keep to one or two sentences>
```

These are informational only and are not authoritative design data.

---

## Component Entry Template

Copy-paste this skeleton when adding a new component:

```markdown
## <Part Number / Common Name>

**Manufacturer:** <Name>  
**Mfr Part Number:** <Exact MPN — include variant suffix>  
**Package:** <Package type, dimensions if relevant>  
**Category:** <IC — Power | IC — Digital | IC — Analog | IC — MCU | IC — RF | Passive — Capacitor | Passive — Inductor | Passive — Ferrite Bead | Crystal | Module | Connector>  
**Datasheet:** <Document title, revision, date — enough to locate the source>  
**Added:** YYYY-MM-DD  
**Used in:** ESHxxxxxxxx Rx  <!-- update when adding to additional projects -->

<One sentence describing what this component does.>

### Pin Description

| Pin | Name | Type | Description |
|-----|------|------|-------------|

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|

### Formulas

### Operating Modes / State Machine

### Register Map  *(if applicable)*

### Application Notes  *(from datasheet — not project-specific)*

### Layout Notes

### Project Usage Notes  *(optional)*

> **[ESHxxxxxxxx Rx]:** <brief project-specific note>

---
```

Only include subsections that have content. Remove unused subsections entirely.

---

## Tools

### extract_pdf.py

**Location:** `40_Tools/extract_pdf.py`  
**Requirement:** Python 3.x + PyMuPDF (`pip install pymupdf`)

Extracts readable text from a datasheet PDF so AI can process it. Use this before handing a datasheet to AI — especially for large files where you only need specific pages.

| Mode | Command | Use case |
|------|---------|----------|
| Full extract | `python 40_Tools/extract_pdf.py <pdf>` | Writes `<pdf>.txt` alongside the source |
| Partial extract | `python 40_Tools/extract_pdf.py <pdf> --pages A-B` | Electrical specs are rarely on page 1 |
| To stdout | `python 40_Tools/extract_pdf.py <pdf> --stdout` | Pipe directly to AI or another tool |
| Table of contents | `python 40_Tools/extract_pdf.py <pdf> --toc` | Find relevant page ranges fast |
| Summary | `python 40_Tools/extract_pdf.py <pdf> --summary` | Confirm page count and file size |

**Typical workflow:**
```
python 40_Tools/extract_pdf.py 70_Assets/MyPart.pdf --toc        # find relevant pages
python 40_Tools/extract_pdf.py 70_Assets/MyPart.pdf --pages 1-30 # extract those pages
# hand the .txt output to AI with the extraction prompt below
```

---

## Adding a New Component

1. Obtain the component's datasheet PDF and place it in `70_Assets/`.
2. Run `extract_pdf.py` to extract text (see Tools section above).
3. Hand the extracted text to AI with the extraction prompt below, or manually fill in the template.
3. Append the new component section to `COMPONENT_DATA.md` after the last `---` divider.
4. Add the component to the **Table of Contents** in `COMPONENT_DATA.md`.
5. Update the **Used in** field for any existing entries if the new project also uses those components.

### AI Extraction Prompt

Use this prompt when handing a PDF to AI:

> "Extract datasheet reference data for `<part number>` from this PDF and format it as a `COMPONENT_DATA.md` entry following the template in `30_Workflows/component-data-workflow.md`. Include: pin descriptions, key electrical parameters, design formulas, operating modes, register maps if applicable, and layout notes. Use generic datasheet labels (R1, R2, C1, etc.) for formula variables — not project schematic reference designators. Do not include project-specific net names, GPIO assignments, or requirement IDs. Tag any project-specific application details with `> **[ESHxxxxxxxx Rx]:**`."

---

## Editing and Correction Rules

- **Append only.** Never modify or delete extracted datasheet content.
- **Errors:** Add a dated correction note immediately after the affected line:
  ```
  > **Correction (YYYY-MM-DD):** <corrected statement>. Original entry retained for traceability.
  ```
- **New datasheet revision:** Add a note citing the new revision number and changed values. Do not overwrite the old values.
- **Adding a project note:** Append to the existing "Project Usage Notes" subsection. Never replace an existing project note.

---

## Deprecation of Per-Project Files

Per-project `COMPONENT_DATA.md` files (e.g. in `20_Projects/ESH10000662/R1/`) are **superseded** by this global file. They are retained as read-only references. When updating or extending component data, always use the global file only.

Each per-project file carries a deprecation notice at the top.

---

## File Location

```
Electro-Engineering/
├── COMPONENT_DATA.md                       ← global authority
├── 30_Workflows/
│   └── component-data-workflow.md          ← this file
└── 20_Projects/
    └── ESHxxxxxxxx/
        └── Rx/
            └── COMPONENT_DATA.md           ← DEPRECATED — read-only reference
```
