# New Project Setup

## Purpose
Create a consistent project folder in the workbook whenever a new project begins.

## Inputs — ask for these before starting
1. **Project name** — short, used in folder and index (e.g. `ESH10000597_R0_Functional`)
2. **Product / document** — product name, part number, or requirements document reference
3. **Hardware revision** — the revision under test or design (e.g. `R0`, `Rev B`)
4. **Phase** — e.g. Requirements, Schematic, Layout, Release, Prototype, DVT, Compliance, Sign-off
5. **Project type** — Design / Review / Verification / Production Test

## Naming convention
- Project folder: `20_Projects/Project-<ProjectName>/`
- Use underscores, no spaces. Match the naming from PROJECT_INDEX.md.

## Workflow

### Step 1 — Confirm inputs
Repeat back the five inputs. Ask for confirmation before creating anything.

### Step 2 — Create project folder structure
Create `20_Projects/Project-<ProjectName>/` with:

**Always present:**
```
Project-<ProjectName>/
├── _<ProductName>      — empty file; product name only, underscore prefix sorts it to the top for quick identification
├── README.md           — TL;DR: scope, product, revision, key contacts
├── STATUS.md           — current focus, next 3 actions, risks (use template)
├── DECISIONS.md        — decisions that change how work is conducted
├── QUESTIONS.md        — open questions to resolve (owner + date opened)
├── ASSUMPTIONS.md      — what is assumed true and impact if wrong
├── DESIGN_LOG.md       — design changes and suggestions for next revision
├── ISSUES/             — non-conformances and deviations
├── ASSETS/             — datasheets, schematics, photos, measurement exports
└── DOCS/               — generated reports, review packages
```

**If project type includes Design, also add:**
```
├── SPECIFICATION.md     — requirements, acceptance criteria, traceability
└── DESIGN_PROGRESS.md   — schematic/layout milestones and review gates
```

**If project type includes Verification, also add:**
```
├── VERIFICATION.md      — test scope, requirements coverage, acceptance criteria
├── DUT_LOG.md           — all DUTs for this project, their state and history
├── TEST_CASES/          — one file per test group or test area
└── TEST_RESULTS/        — test session logs and evidence
```

### Step 3 — Populate from templates

**Always:**
- STATUS.md → copy from `60_Templates/status_template.md`
- DESIGN_LOG.md → copy from `60_Templates/design_log.md`

**If project type includes Design:**
- SPECIFICATION.md → copy from `60_Templates/specification.md`
- DESIGN_PROGRESS.md → copy from `60_Templates/design_progress.md`

**If project type includes Verification:**
- VERIFICATION.md → copy from `60_Templates/verification.md`
- DUT_LOG.md → copy from `60_Templates/dut_log.md`

### Step 4 — Update PROJECT_INDEX.md
Add a row with: Project, Product/Document, Revision, Phase, Status (🔵 Planned), Notes.

## DECISIONS.md — entry rule
Add an entry when a choice:
- Constrains future test scope, design direction, or acceptance criteria
- Would cause rework or safety risk if silently changed
- Must be respected by AI in future sessions

Do NOT add: test results, daily observations, open questions.
AI must not add entries unless explicitly told "promote this to a decision".

## DESIGN_LOG.md — entry rule
Add an entry for any change observed or proposed for the next revision:
- Forward design changes during the current revision's design phase
- Design errors (component values, orientation, footprint, schematic)
- Mechanical / layout changes required by test findings
- Cosmetic improvements (silkscreen, labels)
- Open questions about the design that must be resolved before R1
- Suggestions for improvement that may or may not be adopted

Each entry needs: category (DES/COS/QST/SUG), severity (1–5), description, proposed action.
AI must not add entries unless explicitly told to log a design change.
