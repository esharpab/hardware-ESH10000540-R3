---
project: ESH10000540
revision: R3
updated: 2026-04-30
---

# Status: Sparrow Fixture Electronics PCBA R3

## Current Phase

**Review — Schematic ERC** (R3) — Near-complete

---

## Current Focus

- [x] Performed schematic ERC check (335 nets, 445 components)
- [x] Disposition ERC findings (43 total: all 24 errors and 19 warnings dispositioned)
- [x] Bus signal integrity checks (ERC-B01/B03) — I2C, UART/RS-485 verified
- [x] Component data coverage — 15/17 IC types now in COMPONENT_DATA.md
- [x] ERC-C08 (unconnected pins) — complete for 15/17 types; 2 types pending (no datasheet)
- [x] ERC-P06 (power pins) — complete for 15/17 types; 4 conditional items require engineer confirmation
- [x] ERC-D01/D02/D03 (device constraints) — complete for 15/17 types; 4 open items
- [ ] Engineer confirmation of 4 open ERC-D03 items (see SCHEMATIC_REVIEW.md)
- [ ] Obtain datasheets for 74HCS32PWR (U28) and KAQY214STLD (U30–U37)
- [ ] Obtain design review sign-off
- [ ] Plan and execute layout review (if applicable)

---

## Latest Confirmed State

- **Project created:** 2026-04-28
- **Design:** Complete (schematic and layout produced)
- **Schematic ERC review:** Near-complete
  - Errors: 24 — all dispositioned (ERC-P01 power-symbol limitation, accepted)
  - Warnings: 19 — all dispositioned (ground domains + BOM diode values, accepted)
  - Clean checks: 12/20 checks passed
  - Component data coverage: 15/17 — added 12 new entries to COMPONENT_DATA.md
  - Component data coverage: 17/17 — all device types covered
  - ERC-C08/P06/D: Complete for all 17 device types; all findings closed 2026-04-30
- **Schematic ERC sign-off:** ✅ Signed — Martin Johansson, 2026-04-30 (see Signoff/DESIGN_SIGNOFF.md)
- **Quality sign-off:** ⏳ Pending
- **Layout review:** Not yet started

---

## Open Issues / Blockers

1. ~~**U39 pin 11 (ADS7828) mode**~~ — ✅ Resolved: pin 11 = COM, tied to AGND via R180 (0Ω, mounted). Single-ended mode with analog ground reference. Closed 2026-04-30.
2. ~~**VIO_EXT voltage range (PCA9616 U4)**~~ — ✅ Resolved: VDDA_SEL=1 mode; VDD(A) = 2.2–5.5 V. Accepted 2026-04-30.
   ~~**VIO_EXT voltage range (24AA02UID U29)**~~ — ✅ Resolved: VIO_EXT = 1.8–3.3 V; min 1.8 V ≥ 1.7 V requirement. Closed 2026-04-30.
3. ~~**TPS54302 VDD minimum**~~ — ✅ Resolved: VDD = 20 V; within 4.5–28 V range. Closed 2026-04-30.
4. ~~**U6 pin 9 (AD5593R VLOGIC)**~~ — ✅ Resolved: confirmed 3V3 by engineer. Closed 2026-04-30.
5. ~~**74HCS32PWR (U28), KAQY214STLD (U30–U37)**~~ — ✅ Resolved: datasheets found (SN74HCS32, KAQY214); entries added to COMPONENT_DATA.md; ERC checks completed. Closed 2026-04-30.
6. **Power routing** — Verify all power nets have proper sources and routing in layout.

---

## Next 3 Actions

1. **Obtain Quality sign-off** on schematic ERC review — [Signoff/DESIGN_SIGNOFF.md](Signoff/DESIGN_SIGNOFF.md)
2. **Plan and execute layout review** — DFM, clearance, signal return paths (required before PCB release)
2. **Locate datasheets for 74HCS32PWR and KAQY214STLD** — Needed to close remaining ERC-C08/P06/D checks
3. **Proceed to design review sign-off** ([Signoff/DESIGN_SIGNOFF.md](Signoff/DESIGN_SIGNOFF.md)) once open items resolved

---

## Risks

- *ERC open items* — None; all 17 device types fully verified and closed 2026-04-30
- *Power routing* — Layout-level verification (DFM, clearance, return paths) not yet performed
