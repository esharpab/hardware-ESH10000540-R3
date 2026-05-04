# ESH10000534 R4 Project Rules

**Project:** PoE  
**Revision:** R4 (Design)

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
ESH10000534/R4/
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

## Context

This board is part of the **Sparrow project**, assembled inside the **Accordion A2** module.
It interfaces to the Accordion via M.2 connector (J1: pn-accordion_m2_module_2).

**Key design elements relevant to production test:**

| Ref | Part | Function |
|-----|------|----------|
| U1 | TPS2491 | PoE PD controller — board receives PoE power |
| U4 | TPS23881 | PoE PSE controller — board sources PoE to downstream ports |
| U8 | LTC2992 | I²C power/current monitor |
| U9 | ISOW7842 | Isolated digital bus (I²C/SPI) |
| U10 | LP5012 | 12-ch LED driver |
| U12/U13 | DRV8220 | H-bridge drivers for relay coils |
| U14 | PI4IOE5V6416EP | 16-bit I²C I/O expander |
| U7 | EEPROM 2K I2C | Board ID / configuration storage |
| Re1/Re2 | HFD4 | Relays switched by DRV8220 |
| J2 | Terminal block 5×2 | PoE power port connections |
| J3 | RJ45 RA TH | Standard Ethernet port |
| J4 | RJ45 PoE+ 4-pair | PoE+ port |
| TP1/TP2/TP3 | Test points | In-circuit test access |

Source files in DOCS/:
- `m2top_PoE_R4.pdf` — schematic
- `M2top_PoE_R4_BOM.xlsx` — BOM
- `vb_ais.txt` — PCB assembly placement (AIS format)

When production test activities start, create `ProductionTest/PRODUCTION_TEST.md`.

---

## Key Rules

- **Traceability is mandatory:** Every design decision must link to a requirement or rationale.
- **No assumptions:** If interface requirements or pinouts are unclear, ask before proceeding.
- **Decisions are documented:** Any change to design scope or approach → update DECISIONS.md.
- **Test results are immutable:** Once logged, never edit a result — add a correction note instead.

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
