# Electronics Engineering Workbook — Operating Rules

This folder is my Engineering Workbook.
It is the persistent memory, control surface, and execution log for my electronics design and verification work.

This README defines how the workbook functions.

---

## Authority Order (Non‑Negotiable)

1. CANONICAL_PROMPT.md
   Defines how the AI must behave, reason, and respond.

2. Project VERIFICATION.md and/or SPECIFICATION.md (if present)
   Defines test scope, requirements coverage, and acceptance criteria; or
   defines design requirements and their traceability.

3. Project STATUS.md (if present)
   Authoritative current state, open issues, and decisions for that project.

4. README.md (this file)
   Defines how the Engineering Workbook is structured and used.

5. PROJECT_INDEX.md
   Defines which projects exist and their high-level status.

6. Daily logs (10_Daily/)
   Historical record only. Never rewritten, never "fixed".

---

## What This Workbook Is (and Is Not)

- This is NOT a code repository
- This is NOT a code-execution environment
- This IS a working system for:
  - Requirements definition and traceability
  - Design milestone tracking and review gates
  - Verification planning and requirements traceability
  - Test case definition and tracking
  - DUT state and history
  - Daily execution and AI collaboration
  - Long‑term context preservation across sessions

---

## Folder Responsibilities (Short)

- 00_Rituals — How work starts and ends (copy-paste AI session openers)
- 10_Daily — What actually happened (append-only, immutable)
- 20_Projects — Long‑lived project context and artifacts
- 30_Workflows — Reusable execution patterns (design and verification)
- 40_Tools — Utility scripts for report generation and analysis
- 60_Templates — Copy‑only scaffolding, never edited in place
- 70_Assets — Datasheets, schematics, figures, exported reports
