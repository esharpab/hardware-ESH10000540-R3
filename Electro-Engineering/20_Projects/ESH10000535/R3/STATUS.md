---
project: ESH10000535
revision: R3
updated: 2026-04-30 (session 2)
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
- [ ] Complete ERC-C08 / ERC-P06 / ERC-D per-device checks (17 types ready; 2 blocked on missing datasheets)
- [ ] Obtain engineer confirmation on OI-03 and OI-04
- [ ] Obtain design review sign-off

---

## Latest Confirmed State

- **Project created:** 2026-04-30
- **Design:** Complete (schematic, netlist, layout produced)
- **Schematic ERC review:** In progress
  - Structural ERC: Complete — all C/P/S/B checks passed or accepted
  - ERC findings: 3 accepted (ERC-P01 PADS limitation, ERC-S01 diode BOM values, power rail note)
  - Component data coverage: 19/19 types in COMPONENT_DATA.md (15 entries added 2026-04-30)
  - U23 (SN74LVC1G125DBVR) = SN74CBTLV1G125DBVR — bidirectional FET bus switch (not a buffer)
  - Q1 (G20N06D52) = dual N-ch MOSFET, DFN5×6-8L, 60V/20A/30mΩ
  - OI-01 and OI-02 closed; OI-03 and OI-04 pending engineer confirmation
  - OI-01 closed. OI-02 open (missing datasheets). OI-03 and OI-04 pending engineer confirmation.
  - ERC-C08/P06/D: ready to begin for 17 types; blocked on 2 missing datasheets

---

## Open Issues / Blockers

1. **ERC-C08/P06/D** — per-device checks not yet started; all 19 types now have COMPONENT_DATA.md entries
2. **OI-03** — VOUT+/VOUT− caps C2 and C3 are No-Mount; need engineer confirmation this is intentional
3. **OI-04** — ATmega4809 (U18): 26/48 pins present in netlist; need confirmation unconnected I/O pins are intentional NCs

---

## Next 3 Actions

1. **Complete ERC-C08/P06/D per-device checks** — all 19 types ready; start with most complex (ATmega4809, PGA849, LTC3265, G20N06D52)
2. **Obtain engineer confirmation** for OI-03 (C2/C3 NM) and OI-04 (ATmega4809 NCs)
3. **Close OI-03 and OI-04** pending engineer confirmation (C2/C3 NM; ATmega4809 NCs)

---

## Risks

- *Component data gap* — 15/19 types unverified; ERC-C08/P06/D checks blocked until resolved
- *Missing datasheets* — SN74LVC1G125DBVR and G20N06D52 cannot be ERC-checked until sourced
