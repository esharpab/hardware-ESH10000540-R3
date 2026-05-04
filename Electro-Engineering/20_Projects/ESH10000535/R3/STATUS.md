---
project: ESH10000535
revision: R3
updated: 2026-05-04 (session 3)
---

# Status: Sparrow N-Top R3

## Current Phase

**Review — Schematic ERC** (R3) — In progress

---

## Current Focus

- [x] Import design artifacts (netlist, BOM, schematic PDF) into DOCS/
- [x] Run structural ERC (C01–C07, P01–P06, S01–S04, B01–B03)
- [x] Complete component data coverage — 19/19 types in COMPONENT_DATA.md (15 entries added 2026-04-30)
- [x] Obtain missing datasheets — all resolved (U23: sn74cbtlv1g125.pdf; Q1: G20N06D52.pdf)
- [x] Complete ERC-C08 / ERC-P06 / ERC-D per-device checks — all 19 types done (2026-05-04)
- [ ] Obtain engineer confirmation on OI-03 through OI-08 (6 open items)
- [ ] Obtain design review sign-off

---

## Latest Confirmed State

- **Project created:** 2026-04-30
- **Design:** Complete (schematic, netlist, layout produced)
- **Schematic ERC review:** In progress
  - Structural ERC: Complete — all C/P/S/B checks passed or accepted
  - Component data coverage: 19/19 types in COMPONENT_DATA.md
  - ERC-C08: Complete — 2 flags (OI-05 U1 pin count; OI-06 U9 pin 22; OI-07 Q1 pin mapping)
  - ERC-P06: Complete — 1 flag (OI-08 U19/U20 VCCB DAC range + Q1 gate drive)
  - ERC-D: Complete — 30 checks performed; 13 flagged items logged; key flags: U5 OE polarity (D04), U7 URXD_R contention (D06), U8 MODE pin (D08), U17 EN permanent (D18), SPI_ENn pull-up (D26), U24 footprint pin mapping (D27), U26 open-drain pull-ups (D28)
  - OI-03 and OI-04 pending engineer confirmation (carried from previous session)
  - OI-05 through OI-08 raised in ERC-C08/P06/D session (2026-05-04)

---

## Open Issues / Blockers

1. **OI-03** — VOUT+/VOUT− caps C2/C3 are NM; engineer to confirm intentional
2. **OI-04** — ATmega4809 U18: 26/48 pins; engineer to confirm I/O NCs intentional
3. **OI-05** — U1 (24AA025UIDT-I/OT): 6 pins in netlist vs 5-pin 24AA02UID in COMPONENT_DATA.md; verify pinout + VID rail
4. **OI-06** — U9 PADS pin 22 absent; determine if INT (OK floating) or ADDR (must be tied)
5. **OI-07** — Q1 G20N06D52: G/S/D mapping cannot be verified from text; verify against datasheet figure or footprint
6. **OI-08** — U19/U20 VCCB (DAC-set) must stay ≤ 3.6V; Q1 gate drive VGS < 4.5V (verify RDS(ON) acceptable)

---

## Next 3 Actions

1. **Engineer confirms/resolves OI-03 through OI-08** — 6 open items from ERC
2. **Dispositon ERC-D flags** — U5 OE polarity (D04), U7 mutual exclusion (D06), U8 MODE pin (D08), U26 pull-ups (D28), U24 footprint (D27)
3. **Proceed to design review sign-off** once all open items resolved

---

## Risks

- *6 open items* (OI-03–OI-08) require engineer input before sign-off can proceed
- *OI-08* (VCCB > 3.6V) is a device damage risk if DAC range not verified
- *OI-07* (Q1 pin mapping) must be verified against PCB footprint
