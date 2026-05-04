# ESH10000633 R1 Project Rules

**Project:** Sparrow Complete Product
**Revision:** R1 (Production Test)

---

## Sub-assemblies

| ESH | Product | Rev |
|-----|---------|-----|
| ESH10000182 | Accordion A2 Base | — |
| ESH10000535 | Sparrow N-Top | R3 |
| ESH10000540 | Sparrow Fixture Electronics PCBA | R3 |
| ESH10000543 | Fixture Link | R2 |
| ESH10000536 | Active Load | R2 |
| ESH10000534 | PoE | R4 |
| ESH10000654 | Sparrow Test Adapter (test tooling) | R0 |

---

## Authority & File Precedence

For this project, consult files in this order:

1. **SPECIFICATION.md** (root) — Product-level requirements and acceptance criteria
2. **ProductionTest/PRODUCTION_TEST_PLAN.md** — Test strategy, coverage, and pass/fail criteria
3. **ProductionTest/PRODUCTION_TEST_PROCEDURE.md** — Step-by-step technician procedure
4. **STATUS.md** (root) — Current focus and blockers
5. **DECISIONS.md** (root) — Rationale for key choices
6. **Daily logs** (`10_Daily/`) — Session-by-session work record

---

## Folder Structure & File Organization

```
ESH10000633/R1/
├── CLAUDE.md                 (this file)
├── SPECIFICATION.md          (product requirements)
├── STATUS.md                 (current state)
├── DECISIONS.md              (decisions log)
├── DESIGN_LOG.md             (chronological work record)
│
├── ProductionTest/
│   ├── README.md
│   ├── PRODUCTION_TEST_PLAN.md     (strategy, coverage, pass/fail criteria)
│   └── PRODUCTION_TEST_PROCEDURE.md  (technician step-by-step)
│
├── Verification/
│   └── README.md             (placeholder for system-level DVT if needed)
│
├── ASSETS/
├── DOCS/
└── ISSUES/
```

---

## Key Rules

- **Sub-assembly verification is separate:** Component-level characterization lives in each sub-project. This project only tracks system-level production test.
- **Test results are immutable:** Once recorded in a DUT log, never edit. Add a correction note instead.
- **No assumptions:** If a test result or acceptance criterion is unclear, ask before proceeding.
- **Traceability is mandatory:** Every production test step must link to a system requirement or a sub-assembly functional area.

---

## Session Start

When resuming work:
1. Read **STATUS.md** (current focus and blockers).
2. Read **ProductionTest/PRODUCTION_TEST_PLAN.md** (open items and coverage gaps).
3. Check **DECISIONS.md** for any recent plan changes.

Do not read other files unless specifically referenced.

---

## Session End

- Update **ProductionTest/PRODUCTION_TEST_PLAN.md** if strategy or coverage changed.
- Update **STATUS.md** (current focus, next actions, blockers).
- Update **DECISIONS.md** if new decisions were made.
- Create or append to daily log: `10_Daily/<YYYY>/<YYYY-MM-DD>.md`.
- Git commit and push if changes were made.
