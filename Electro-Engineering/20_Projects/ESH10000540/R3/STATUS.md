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
  - ERC-C08/P06/D: Verified for all 15 covered device types; 4 items flagged for engineer confirmation
- **Review sign-off:** Pending — requires engineer disposition of 4 open items
- **Layout review:** Not yet started

---

## Open Issues / Blockers

1. **U39 pin 11 (ADS7828) mode** — Pin 11 on U39_COM net via 2K2 resistors; confirm whether differential mode (intentional) or GND error. See ERC-D03.
2. **VIO_EXT voltage range** — U4 (PCA9616) VDDA and U29 (24AA02UID) VDD on VIO_EXT; confirm 2.7V–5.5V and 1.7V–5.5V minimum respectively. See ERC-P06.
3. **TPS54302 VDD minimum** — VDD from J9 must be ≥ 4.5V; confirm min supply voltage under all conditions. See ERC-D03.
4. **U6 pin 9 (AD5593R VLOGIC)** — Net not confirmed; assumed 3V3 by symmetry with U5-9. Engineer to verify.
5. **74HCS32PWR (U28), KAQY214STLD (U30–U37)** — No datasheets available; ERC-C08/P06/D cannot be completed for these two types.
6. **Power routing** — Verify all power nets have proper sources and routing in layout.

---

## Next 3 Actions

1. **Engineer confirms / resolves the 4 ERC-D03 open items** — Required before sign-off
2. **Locate datasheets for 74HCS32PWR and KAQY214STLD** — Needed to close remaining ERC-C08/P06/D checks
3. **Proceed to design review sign-off** ([Signoff/DESIGN_SIGNOFF.md](Signoff/DESIGN_SIGNOFF.md)) once open items resolved

---

## Risks

- *ERC open items* — 4 conditional items in ERC-D03 require engineer judgement; none appear to be design errors based on netlist evidence
- *Missing datasheets* — 74HCS32PWR and KAQY214STLD unverified; risk low if standard logic and relay parts
- *Power routing* — Layout-level verification (DFM, clearance, return paths) not yet performed
