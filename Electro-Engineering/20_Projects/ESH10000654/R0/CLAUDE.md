# ESH10000654 R0 Project Rules

**Project:** Sparrow Test Adapter  
**Revision:** R0 (Design)

---

## Authority & File Precedence

For this project, consult files in this order:

1. **SPECIFICATION.md** (root) — Authoritative requirements and design scope
2. **Design/DESIGN_PROGRESS.md** — Design milestones and open items
3. **STATUS.md** (root) — Current focus and blockers
4. **DECISIONS.md** (root) — Rationale for key choices
5. **DESIGN_LOG.md** (root) — Chronological design work record
6. **Daily logs** (`10_Daily/`) — Session-by-session work record

---

## Folder Structure & File Organization

```
ESH10000654/R0/
├── CLAUDE.md                 (this file)
├── SPECIFICATION.md          (requirements)
├── STATUS.md                 (current state)
├── DECISIONS.md              (design decisions)
├── DESIGN_LOG.md             (chronological design work)
│
├── Design/
│   ├── README.md             (index)
│   └── DESIGN_PROGRESS.md    (milestones & progress)
│
├── Review/
│   ├── README.md             (index & workflow)
│   ├── SCHEMATIC_REVIEW.md   (schematic ERC findings)
│   └── LAYOUT_REVIEW.md      (layout review findings)
│
├── Verification/
│   └── README.md             (placeholder — populated when DV starts)
│
├── ProductionTest/
│   └── README.md             (placeholder — populated when PT is defined)
│
├── Signoff/
│   └── README.md             (placeholder)
│
├── ASSETS/
├── DOCS/
└── ISSUES/
```

---

## Key Rules

- **Traceability is mandatory:** Every design decision must link to a requirement or rationale.
- **No assumptions:** If interface requirements or connector pinouts are unclear, ask before proceeding.
- **Decisions are documented:** Any change to design scope or approach → update DECISIONS.md.
- **Test results are immutable:** Once logged in Verification/DUT_LOG.md (when populated), never edit a result.

---

## Context

This adapter is used in Sparrow verification and production test together with Accordion.
When verification activities start, create `Verification/VERIFICATION.md` and `Verification/DUT_LOG.md`.

---

## Session Start

When resuming work:
1. Read **STATUS.md** (current focus and blockers).
2. Skim **Design/DESIGN_PROGRESS.md** (latest design state).
3. Check **DECISIONS.md** for any recent plan changes.

Do not read other files unless specifically referenced.

---

## Session End

- Append to **DESIGN_LOG.md** (if design work was done).
- Update **STATUS.md** (current focus, next actions, blockers).
- Optionally update **DECISIONS.md** if new decisions were made.
- Create or append to daily log: `10_Daily/<YYYY>/<YYYY-MM-DD>.md`.
- Git commit and push if changes were made.
