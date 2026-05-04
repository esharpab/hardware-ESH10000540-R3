# Schematic Review: Fixture Link R2

**Status:** Review complete — awaiting engineer disposition  
**File:** NetList_Fixture_Link_R2.qcv + PartsList_Fixture_Link_R2.csv  
**Format:** PADS QCV netlist + BOM CSV  
**Date:** 2026-05-04  
**Components:** ~150 (11 ICs, ~99 R, 14 C, 16 D, 2 J, 7 PCB refs)  
**Nets:** 125  
**Reviewer:** AI (Claude)

---

## ERC Review — Fixture Link R2

### Findings

| # | Check | Severity | Detail |
|---|-------|----------|--------|
| F-01 | ERC-D02 | ❌ Error | **R66 (1K, mounted): pin 1 is NC (by TERM), leaving D8 red LED channel undriven.** Net `D8_RED` has only R66-2 and D8-2 — no drive signal reaches D8 pin 2. R67-1 and R68-1 (D8 channels 1 and 3) are correctly connected to RTS and UART_ENn respectively. R66-1 is missing a connection to a driver net. Contrast with D4–D7 where red-channel resistors are NM (intentionally unused). |
| F-02 | ERC-D01 | ⚠️ Warning | **U7 (SN74LVC07APW): 6 open-drain outputs have no pull-up resistors on this board.** Affected nets: `SRQn` (U7-2), `INTERRUPTn` (U7-4), `SRQ4n_BUF` (U7-6), `SRQ3n_BUF` (U7-8), `SRQ2n_BUF` (U7-10), `SRQ1n_BUF` (U7-12). Each net connects only U7 output and a J1 pin. SN74LVC07A datasheet requires external pull-ups on all open-drain outputs. Pull-ups may be provided on the Accordion side of J1 — confirm intentional. |
| F-03 | ERC-D03 | ⚠️ Warning | **U16 (TRSF3232E): charge pump flying capacitors C8 and C9 are 1 µF.** TRSF3232E datasheet recommends 47–100 nF for C1± and C2± (charge pump flying caps). 1 µF is 10× above the typical maximum — may slow the charge pump oscillation and reduce the ±5 V rail headroom. RS-232 output voltage levels (±5 V min) should be verified. V+ and V− storage capacitors (C11, C12, 1 µF) are acceptable. |
| F-04 | ERC-C02 | ⚠️ Warning | **PCB reference components PCB1, PCB2, PCB4, PCB5, PCB6, PCB7, PCB8 are unconnected with no explicit NC flag.** Single-pin components in the un-connected section without `(by TERM)`. Likely mounting holes or fiducials — confirm no net assignment is missing. |
| F-05 | ERC-S01 | ⚠️ Warning | **C3 BOM row has no Value field.** Part number EGP10001454 (GRM21BR61H106KE43) appears on a second row for C4/C10/C16 with value 10 µF. C3 is almost certainly 10 µF — BOM data entry gap. Populate the Value field. |

---

### Info (no action required — for awareness)

| # | Detail |
|---|--------|
| I-01 | **U1/U2 complementary OE from UART_ENn.** U1 (SN74LVC126APW, active-HIGH OE) and U2 (SN74LVC125APW, active-LOW OE) are both driven by `UART_ENn`. When HIGH: U1 enabled (J1→UART direction), U2 disabled. When LOW: U2 enabled (UART→J1 direction), U1 disabled. Intentional bidirectional UART direction control. |
| I-02 | **U16 RIN2 (CTS input, pin 8) tied to GND via R96 (0R).** ROUT2 therefore permanently asserts CTS to U2-12 (UART CTS input). R97 (NM, 10K to 5V) provides a provision to reconnect CTS from J2 if needed. Intentional for no-hardware-CTS operation — confirm. |

---

### Summary

| Metric | Count |
|--------|-------|
| ❌ Errors | 0 (F-01 rejected — intentional) |
| ⚠️ Warnings | 1 open (F-02); 3 accepted/rejected |
| ℹ️ Info | 2 |
| ✅ Checks passed | 28 |

---

### Checks passed (✅)

| Check | Result |
|-------|--------|
| ERC-C01 — Floating nets | ✅ No single-node nets |
| ERC-C02 — Unconnected pins (ICs) | ✅ All IC pins accounted for |
| ERC-C03 — NC marker on connected pin | ✅ None found |
| ERC-C04 — Net label orphans | ✅ None |
| ERC-C05 — Duplicate net names | ✅ None |
| ERC-C06 — All-GND connector | ✅ J2 not all-GND |
| ERC-C08 — PCA9616 DINTP/DINTM (U8–U11 pins 10/11) | ✅ Correctly NC — INT channel unused per datasheet |
| ERC-C08 — 24AA025 A0/A1 (U15 pins 4/5) | ✅ Tied to GND — valid per datasheet |
| ERC-P01 — Power net sources | ✅ VDD, 3V3, 5V, VID from J1; VOUT from U3; VS+/VS− from U16 |
| ERC-P02 — Shorted power rails | ✅ None |
| ERC-P03 — Missing GND connections | ✅ All IC GND pins connected |
| ERC-P04 — Multiple GND domains | ✅ Single GND domain |
| ERC-P05 — Power pin conflict | ✅ None |
| ERC-P06 — U1, U2, U7 VCC | ✅ 3V3 (1.65–3.6 V range) |
| ERC-P06 — U3 IN | ✅ VDD (2.7–23 V range) |
| ERC-P06 — U8–U11 VDD(A), VDD(B) | ✅ 3V3; VDDA_SEL pulled HIGH on all 4 instances → VDD(A) in 2.2–5.5 V range |
| ERC-P06 — U14 VCC / VCC(I2C) | ✅ VCC=3V3; VCC(I2C)=VID (from J1) |
| ERC-P06 — U15 VCC | ✅ VID (1.7–5.5 V range) |
| ERC-P06 — U16 VCC | ✅ 5V (3.0–5.5 V range) |
| ERC-B01 — PCA9616 I2C differential pairs (U8–U11) | ✅ DSCLP/DSCLM/DSDAP/DSDAM correct on all 4 instances |
| ERC-B01 — U14/U15 I2C bus | ✅ U14 and U15 share SCL/SDA — correct |
| ERC-B03 — UART path through U1, U2, U16 | ✅ TX/RX/RTS/CTS routing correct |
| ERC-D01 — U3 EN/UVLO | ✅ R92 (10K pull-down); U14-2 GPIO driver |
| ERC-D01 — U3 OVLO | ✅ R42 (1M) / R43 (56K) divider from VDD |
| ERC-D01 — U3 ILM | ✅ R40 (1K to GND) |
| ERC-D01 — U8–U11 EN pull-down | ✅ 10K pull-down on all I2Cx_EN nets |
| ERC-D01 — U14 INT pull-up | ✅ R47 (10K to 3V3) |
| ERC-D01 — U14 RESET pull-up | ✅ R46 (1K to VID) |
| ERC-D02 — U3 ITIMER cap | ✅ C6 (22 nF to GND) |
| ERC-D02 — U3 dVdt cap | ✅ C7 (22 nF) via R95 (100R) to GND |
| ERC-D02 — U3 PG pull-up | ✅ R41 (10K to 3V3) |
| ERC-D02 — U15 SDA/SCL pull-ups | ✅ R44, R45 (to VID) on SDA/SCL |

---

### Recommended actions

- [ ] **F-01 (❌):** Identify the intended driver signal for R66-1 (D8 red LED channel) and connect in schematic. If the red channel of D8 is intentionally unused, mark R66 as NM (consistent with D4–D7 pattern).
- [ ] **F-02 (⚠️):** Confirm pull-ups for U7 open-drain outputs are provided on the Accordion side of J1. If not, add pull-up resistors on this board.
- [ ] **F-03 (⚠️):** Review TRSF3232E charge pump cap values. If C8/C9 must remain 1 µF, verify ±5 V rails at worst case with a bench measurement or simulation. Consider changing to 100 nF per datasheet recommendation.
- [ ] **F-04 (⚠️):** Confirm PCB1/2/4/5/6/7/8 are mechanical references with no missing signal connections.
- [ ] **F-05 (⚠️):** Add Value = "10u" to C3 BOM row.

---

## Finding Dispositions

| Finding | Disposition | Engineer | Date | Notes |
|---------|-------------|----------|------|-------|
| F-01 | Rejected | MJ | 2026-05-04 | R66 pin 1 NC is intentional — D8 red LED channel is unused by design |
| F-02 | Open | — | — | |
| F-03 | Accepted | MJ | 2026-05-04 | 1 µF charge pump caps intentional; RS-232 levels to be verified on bench |
| F-04 | Rejected | MJ | 2026-05-04 | PCB1/2/4/5/6/7/8 confirmed fiducials — no signal missing |
| F-05 | Accepted | MJ | 2026-05-04 | C3 is 10 µF; BOM value field blank — note for R3 to correct |

---

## Disposition Key

| Value | Meaning |
|-------|---------|
| Open | Not yet reviewed by engineer |
| Accepted | Finding confirmed; action required |
| Rejected | Finding dismissed; reason noted |
| Fixed | Corrected in schematic |
