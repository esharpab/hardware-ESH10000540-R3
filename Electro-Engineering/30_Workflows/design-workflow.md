# Design Workflow

## Purpose
Guide the lifecycle from requirements through schematic/layout to release and verification handoff.
Schematic and layout work is done in PADS or KiCad — this workflow tracks progress in the workbook.

## When to use this workflow
- Starting a new hardware design project
- Adding requirements tracking to an existing project
- When schematic/layout work is in progress and milestones need tracking

---

## Step 1 — Define requirements

Create `SPECIFICATION.md` from `60_Templates/specification.md`.

Gather inputs:
- Customer specification or product brief
- Applicable standards and regulatory requirements
- Internal constraints (mounting, interfaces, power budget, environment)

Draft requirements with clear acceptance criteria. Each requirement needs:
- Unique ID (REQ-001, REQ-002...)
- Type, source, and priority
- A measurable acceptance criterion

Review and approve requirements:
- Update each requirement's status from Draft to Approved
- Record the approval decision in DECISIONS.md

## Step 2 — Schematic capture

Work is done in PADS or KiCad (external to workbook).

In the workbook:
- Update milestone DS.01 in `DESIGN_PROGRESS.md`
- Record the schematic file path in the EDA file references table
- Log key design decisions in `DECISIONS.md` as they arise
- Open questions go to `QUESTIONS.md`, assumptions to `ASSUMPTIONS.md`

## Step 3 — Schematic review

- **AI-assisted ERC:** Use `30_Workflows/schematic-review.md` to run an electrical rule check on the schematic or netlist before the formal review gate.
- Update milestone DS.02 and the schematic review gate in `DESIGN_PROGRESS.md`
- Log review findings as issues in `ISSUES/` (same ISS-NNN format as verification issues)
- Use `DESIGN_LOG.md` for changes that will carry forward or need tracking across revisions

## Step 4 — BOM and procurement

- Update milestone DS.03 when BOM is released
- Record the BOM file path in EDA file references

## Step 5 — Layout

Work is done in PADS or KiCad.

In the workbook:
- Update milestone DS.04 at layout start
- Update milestone DS.05 and the layout review gate when review occurs
- Log review findings in `ISSUES/`

## Step 6 — Release

- Update milestones DS.06 (Gerber), DS.07 (Assembly drawing) when released
- Record all release artifacts in EDA file references
- Update DS.08 (Fabrication order), DS.09 (Assembly order) when placed
- Record the release decision in `DECISIONS.md`

## Step 7 — Handoff to verification

- Link requirements to `VERIFICATION.md` test steps by populating the Trace column in `SPECIFICATION.md`
- Use the verification-planning workflow (`30_Workflows/verification-planning.md`) to build the verification plan
- Ensure every "Must" requirement has at least one test case
- For Design + Verification projects, this is where the verification scope begins

---

## AI usage in this workflow
- AI can help draft requirements from pasted datasheets, specifications, or standards
- AI can help maintain milestone status from session notes
- AI can generate a design status summary on request
- AI can help trace requirements to test steps during handoff
- AI must not mark design milestones as complete, reviews as passed, or requirements as approved — only the engineer can do that
- AI must not invent Req IDs, milestone dates, or review outcomes
