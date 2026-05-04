# ESH10000543 R2 Project Rules

**Project:** Fixture Link  
**Revision:** R2 (Schematic Review)

---

## Authority & File Precedence

For this project, consult files in this order:

1. **SPECIFICATION.md** (root) — Authoritative requirements and design scope
2. **Review/SCHEMATIC_REVIEW.md** — Schematic ERC findings and dispositions
3. **STATUS.md** (root) — Current focus and blockers
4. **DECISIONS.md** (root) — Rationale for key choices
5. **Daily logs** (`10_Daily/`) — Session-by-session work record

---

## Folder Structure & File Organization

```
ESH10000543/R2/
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
│   └── SCHEMATIC_REVIEW.md   (schematic ERC findings)
│
├── ASSETS/
├── DOCS/
└── ISSUES/
```

---

## Key Rules

- **Findings are not dispositions:** AI reports ERC findings — only the engineer dispositions them.
- **No assumptions:** If netlist or schematic content is unclear, ask before proceeding.
- **Decisions are documented:** Any design or review decision goes in DECISIONS.md with rationale.

---

## Session Start

When resuming work:
1. Read **STATUS.md** (current focus and blockers).
2. Skim **Review/SCHEMATIC_REVIEW.md** (open findings and dispositions).
3. Check **DECISIONS.md** for any recent plan changes.

Do not read other files unless specifically referenced.

---

## Session End

- Update **Review/SCHEMATIC_REVIEW.md** if findings were added or dispositioned.
- Update **STATUS.md** (current focus, next actions, blockers).
- Optionally update **DECISIONS.md** if new decisions were made.
- Create or append to daily log: `10_Daily/<YYYY>/<YYYY-MM-DD>.md`.
- Git commit and push if changes were made.
