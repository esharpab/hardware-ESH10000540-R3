---
project: ESH10000633
revision: R1
document: Production Test Plan
status: Draft
created: 2026-05-04
---

# Production Test Plan — Sparrow Complete Product R1

## Purpose

Define the production test strategy, coverage, and pass/fail criteria for the assembled Sparrow R1 product.

This test covers **system-level integration** only. It does not repeat parametric characterization already performed in sub-assembly verification plans (ESH10000535 R3, ESH10000540 R3, ESH10000543 R2). See DECISIONS.md D.01.

> **Note:** ESH10000536 (Active Load R2) and ESH10000534 (PoE R4) are part of the Sparrow system. No sub-assembly verification plans exist for these modules; PT-AL and PT-POE coverage has been derived from the Sparrow system datasheet.

---

## Test Setup

| Item | Description | Status |
|------|-------------|--------|
| Accordion A2 (ESH10000182) | Test controller — hosts I2C, SPI, power | Available |
| Sparrow Test Adapter (ESH10000654 R0) | Physical interface Accordion ↔ Sparrow DUT | ✅ Assembled in-house — verification pending |
| DC Supply (20 V) | 20 V input to Fixture Link | TBD |
| DC Supply (56 V) | 56 V input to PoE module (PT-POE) | TBD |
| Test Software | Accordion automation scripts | TBD |

> **Note:** ESH10000654 R0 is assembled and in-house. Requirements defined (21 req). 4 open interface items remain (see ESH10000654 R0 SPECIFICATION.md open items). PT procedure can be written in parallel once PSU connector assignment and PoE routing are confirmed.

---

## Coverage Map

The table below maps each production test area to the sub-assembly verification it derives from, and states the rationale for inclusion or exclusion.

| PT Area | Derived From | Rationale |
|---------|-------------|-----------|
| PT-M — Mechanical assembly | ESH10000535 M.00–M.02, ESH10000540 M.00–M.03, ESH10000543 M.00–M.04 | Assembly integrity check — confirms correct build |
| PT-PWR — System power-on | ESH10000543 P.00–P.04, ESH10000535 P.00–P.06, ESH10000540 P.00–P.01 | Confirms eFuse path, key rails present — not full characterization |
| PT-PSU — Programmable rails (spot check) | ESH10000540 P.08–P.42 | One setpoint per rail to confirm assembly; full range tested at sub-assembly |
| PT-COMM — I2C bus scan | ESH10000543 C.00, ESH10000535 CIO.00/CIO.03, ESH10000543 C.03–C.04 | Confirms all devices accessible end-to-end through Fixture Link transceivers |
| PT-FW — Firmware | ESH10000535 CIO.02–CIO.03 | Confirms ATmega programmed and responding |
| PT-SIG — Signal paths (spot check) | ESH10000535 UIO.00–UIO.03, ESH10000540 UIO.19–UIO.34, UIO.35–UIO.83, UIO.00–UIO.18, UIO.84–UIO.91 | One representative channel per signal type — full range at sub-assembly |
| PT-COS — Cosmetics / LEDs | ESH10000543 C.01–C.02, ESH10000535 CIO.07 | Visual quality and LED function |
| PT-AL — Active Load (spot check) | ESH10000536 datasheet (IMEAS ±1%, VMEAS ±2%) | Both channels: sink 100 mA, verify IMEAS and VMEAS within spec |
| PT-POE — PoE subsystem (spot check) | ESH10000534 datasheet (VMEAS ±2.5%, IMEAS ±3%) | Power-on, PoE negotiation, VMEAS and IMEAS within spec |

---

### Explicitly Out of Scope (covered at sub-assembly level)

- Full parametric power rail sweep (all VADJ/VIO setpoints, slew rates, ILM, OVLO, ITIMER)
- Full AIN channel matrix (all gains, both polarities, all 8 channels)
- Full FE_MPIO matrix (all 12 channels × all setpoints)
- eFuse characterization (PG threshold, ITIMER, OVLO)
- N-Top ±18V, PWM/TACH VCCO full setpoint sweep
- AGND–GND isolation (ESH10000540 P.69)
- RS485 bias resistor verification
- Connector pin mapping verification (tested at sub-assembly level)

### Explicitly Deferred (no PT test case — rationale recorded)

| Req | Description | Reason deferred |
|-----|-------------|-----------------|
| PWR-09 | External rail OCP circuit breaker activation | Requires deliberate overcurrent fault injection; risk of damaging DUT; covered by design review and sub-assembly characterization |
| PWR-11 | External rail IMEAS accuracy | Requires calibrated current load per rail; spot-check VMEAS (PT-PSU) is sufficient at production level |
| PWR-15 | PoE maximum output power ≤ 90 W | Requires high-power Ethernet load (>90 W capable); impractical at production test; covered by subsystem design |
| PWR-20 | Active Load Phoenix connector 3/5 A | Phoenix connector is an alternative interface; IDC header (0.4/1 A) tested via PT-AL; Phoenix characterization is sub-assembly scope |
| PWR-21 | Active Load EMAX 250 Ws shutdown | Requires sustained load run to energy limit; destructive/time-consuming; covered by firmware design |
| PWR-24 | PSU optional output (0–18 V) | PSU is an optional module not fitted in standard Sparrow R1 configuration |
| SIG-06 | Relay driver (4 ch) low-side drive | Relay driver functional check requires external coil load; not fitted in standard system test configuration |
| SIG-09 | Tampering latch-and-hold edge detection | Requires specific signal edge injection and software reset sequence; deferred to system-level DVT |

---

## Test Areas

### PT-M — Mechanical / Assembly

> Visual inspection before power-on.

| Step ID | Description | Pass Criteria | TA Requirement |
|---------|-------------|---------------|----------------|
| PT-M.00 | Verify all sub-assemblies installed: Accordion A2 (ESH10000631), Fixture Electronics with Active Load (ESH10000636) including Fixture Electronics PCBA (R3), IDC N-Top (ESH10000634 R3), and Active Load (R2); Sparrow N-Top (R3), Fixture Link (R2), PoE (R4) present inside Accordion | All sub-assemblies present and correctly seated | — |
| PT-M.01 | Inspect board-to-board connectors for correct seating; no bent pins visible | All connectors seated; no visible damage | — |
| PT-M.02 | Confirm revision markings: Fixture Link silkscreen reads R2 | Silkscreen correct | — |

---

### PT-PWR — System Power-On

> Apply 20 V. Verify eFuse path through Fixture Link and key rails across the system.

| Step ID | Description | Signal | Nominal | Tol | Pass Criteria | Source (sub-assy test) | TA Requirement |
|---------|-------------|--------|---------|-----|---------------|------------------------|----------------|
| PT-PWR.00 | Apply 20 V; verify VDD present at Fixture Link | VDD | 20.0 V | ±5% | 19.0–21.0 V | ESH10000543 P.00 | 20 V supply via TA |
| PT-PWR.01 | Assert PWR_EN; verify VOUT (eFuse output) | VOUT | 20.0 V | ±5% | 19.0–21.0 V | ESH10000543 P.04 | PWR_EN via Accordion GPIO |
| PT-PWR.02 | Measure 12 V DC/DC rail (Fixture Electronics) | 12V | 12.0 V | ±5% | 11.4–12.6 V | ESH10000540 P.01 | TA probe point |
| PT-PWR.03 | Measure 12 V rail at N-Top | 12V | 12.0 V | ±5% | 11.4–12.6 V | ESH10000535 P.00 | TA probe point |
| PT-PWR.04 | Measure 5 V rail | 5V | 5.0 V | ±5% | 4.75–5.25 V | ESH10000540 P.20 | TA probe point |
| PT-PWR.05 | Measure 3V3 rail | 3V3 | 3.3 V | ±2.5% | 3.218–3.383 V | ESH10000540 P.31 | TA probe point |
| PT-PWR.06 | Measure VREF rail (N-Top) | VREF_BUF | 2.5 V | ±0.14% | 2.497–2.504 V | ESH10000535 P.05 | TA probe point |
| PT-PWR.07 | Measure +18 V rail (N-Top) | +18V | 18.0 V | ±1% | 17.82–18.18 V | ESH10000535 P.21 | TA probe point |
| PT-PWR.08 | Measure −18 V rail (N-Top) | -18V | −18.0 V | ±1% | −17.82– −18.18 V | ESH10000535 P.22 | TA probe point |

---

### PT-PSU — Programmable Power Supplies (spot check)

> Spot-check one setpoint per programmable rail via Accordion ADC (VMON).

| Step ID | Description | Signal | Nominal | Tol | Pass Criteria | Source (sub-assy test) | TA Requirement |
|---------|-------------|--------|---------|-----|---------------|------------------------|----------------|
| PT-PSU.00 | Enable 12V_EXT; read VMON_12V_EXT ADC | 12V_EXT | 12.0 V | ±5% | 11.4–12.6 V | ESH10000540 P.04 | — |
| PT-PSU.01 | Set VADJ_EXT to 3.3 V; read VMON_VADJ_EXT ADC | VADJ_EXT | 3.3 V | ±2.5% | 3.218–3.383 V | ESH10000540 P.13 | — |
| PT-PSU.02 | Set VIO_EXT to 3.3 V; read VMON_VIO_EXT ADC | VIO_EXT | 3.3 V | ±2.5% | 3.218–3.383 V | ESH10000540 P.26 | — |
| PT-PSU.03 | Enable 3V3_EXT; read VMON_3V3_EXT ADC | 3V3_EXT | 3.3 V | ±2.5% | 3.218–3.383 V | ESH10000540 P.33 | — |
| PT-PSU.04 | Enable 1V8_EXT; read VMON_1V8_EXT ADC | 1V8_EXT | 1.8 V | ±2.5% | 1.755–1.845 V | ESH10000540 P.39 | — |

---

### PT-COMM — Communication Bus

> Confirm all I2C/SPI devices accessible end-to-end from Accordion through Fixture Link.

| Step ID | Description | Pass Criteria | Source (sub-assy test) | TA Requirement |
|---------|-------------|---------------|------------------------|----------------|
| PT-COMM.00 | I2C scan: Fixture Link expander | Device ACKs at 0x20 | ESH10000543 C.00 | — |
| PT-COMM.01 | I2C scan: Fixture Link EEPROM; write and read back | Device ACKs at 0x50; write/read-back passes | ESH10000543 C.00 | — |
| PT-COMM.02 | Assert I2C_EN via Fixture Link expander; scan I2C bus downstream | All expected N-Top I2C devices ACK (ATmega @ 0x30, LED driver @ 0x14 or 0x0C, expander @ 0x20, IDPROM @ 0x50) | ESH10000543 C.04, ESH10000535 CIO.00 | — |
| PT-COMM.03 | SPI: access both AD5592R devices on Fixture Electronics | Read/write both AD5592R without error | ESH10000535 CIO.05 | — |

---

### PT-FW — Firmware

| Step ID | Description | Pass Criteria | Source (sub-assy test) | TA Requirement |
|---------|-------------|---------------|------------------------|----------------|
| PT-FW.00 | Confirm ATmega responds on I2C at 0x30 | ATmega ACKs | ESH10000535 CIO.03 | — |
| PT-FW.01 | Write and read back IDPROM | IDPROM write succeeds | ESH10000535 CIO.00 | — |

---

### PT-SIG — Signal Paths (spot check)

> One channel per signal type. Full matrix is covered at sub-assembly level.

| Step ID | Description | Signal | Nominal | Tol | Pass Criteria | Source (sub-assy test) | TA Requirement |
|---------|-------------|--------|---------|-----|---------------|------------------------|----------------|
| PT-SIG.00 | MPIO_0: output 2.5 V via DAC; read back via ADC | MPIO_0 | 2.5 V | ±1% | 2.475–2.525 V | ESH10000535 UIO.03 / ESH10000540 UIO.31+UIO.23 | — |
| PT-SIG.01 | FE_MPIO_0: output 2.5 V via DAC; read back via ADC | FE_MPIO_0 | 2.5 V | ±1% | 2.475–2.525 V | ESH10000540 UIO.71+UIO.47 | — |
| PT-SIG.02 | AIN_P_CH1: apply 1 V stimulus; read ADC (G2) | AIN_P_CH1 | 1.0 V | ±0.34% | 0.997–1.003 V | ESH10000540 UIO.141 | TA must provide AIN stimulus |
| PT-SIG.03 | GND_SW0: activate and read ADC | GND_SW0_OUT | 5.0 V | — | ADC reads present | ESH10000540 UIO.11 | — |
| PT-SIG.04 | Activate MIC_BIAS_LOAD_L; read ADC | MIC_IN_L | 2.273 mA | ±2.3% | 2.221–2.325 mA | ESH10000540 P.61 | — |
| PT-SIG.05 | PWM output: set 50% duty at 1 kHz, VCCO 3.3 V; confirm output present | PWM | 50% / 1 kHz | — | PWM signal present on scope; no fault | ESH10000535 UIO.00 | TA probe or loopback |
| PT-SIG.06 | Tach input: inject 1 kHz signal at VCCO 3.3 V; confirm readback | TACH | 1 kHz | — | Tach count correct | ESH10000535 UIO.01 | TA signal injection |
| PT-SIG.07 | USR_GPIO_1: drive HIGH; read back | USR_GPIO_1 | HIGH | — | GPIO reads HIGH | ESH10000540 UIO.88 | — |
| PT-SIG.08 | RS485 ADC: drive logic '1' on RS485_TX; read ADC | RS485_TX | >0.2 V | — | ADC reads >0.2 V | ESH10000540 UIO.08 | TA loopback or driver |

---

### PT-COS — Cosmetic / LEDs

| Step ID | Description | Pass Criteria | Source (sub-assy test) | TA Requirement |
|---------|-------------|---------------|------------------------|----------------|
| PT-COS.00 | Assert LED_BLUEn via Fixture Link expander; confirm Power LED illuminates | Power LED blue | ESH10000543 C.01 | — |
| PT-COS.01 | Assert UART_ENn via Fixture Link expander; confirm RS-232 LED illuminates | RS-232 LED blue | ESH10000543 C.02 | — |
| PT-COS.02 | Write LED registers via LP5012; confirm user LEDs respond | At least one LED channel responds to register write | ESH10000535 CIO.07 | — |

---

### PT-AL — Active Load (spot check)

> Spot-check both Active Load channels: set a mid-range sink current, verify IMEAS and VMEAS are within spec. Full characterization is not required at production test.

| Step ID | Description | Signal | Nominal | Tol | Pass Criteria | Source | TA Requirement |
|---------|-------------|--------|---------|-----|---------------|--------|----------------|
| PT-AL.00 | Set Active Load CH0 to sink 100 mA; verify IMEAS within ±1%; confirm no fault flag | IMEAS_CH0 | 100 mA | ±1% | 99–101 mA | ESH10000536 datasheet (IMEAS ±1%) | 24 V supply on VLOAD_POS_0 via TA |
| PT-AL.01 | With 12 V applied to VLOAD_POS_0; read VMEAS_CH0; verify within ±2% | VMEAS_CH0 | 12.0 V | ±2% | 11.76–12.24 V | ESH10000536 datasheet (VMEAS ±2%) | 12 V on VLOAD_POS_0 via TA |
| PT-AL.02 | Set Active Load CH1 to sink 100 mA; verify IMEAS within ±1%; confirm no fault flag | IMEAS_CH1 | 100 mA | ±1% | 99–101 mA | ESH10000536 datasheet (IMEAS ±1%) | 24 V supply on VLOAD_POS_1 via TA |
| PT-AL.03 | With 12 V applied to VLOAD_POS_1; read VMEAS_CH1; verify within ±2% | VMEAS_CH1 | 12.0 V | ±2% | 11.76–12.24 V | ESH10000536 datasheet (VMEAS ±2%) | 12 V on VLOAD_POS_1 via TA |

---

### PT-POE — Power over Ethernet (spot check)

> Apply 56 V to the PoE module and connect an Ethernet PD load to verify subsystem power-up, VMEAS, and IMEAS within spec.
> **Safety: do not switch PoE output polarity while a DUT is active on ETH OUT.**

| Step ID | Description | Signal | Nominal | Tol | Pass Criteria | Source | TA Requirement |
|---------|-------------|--------|---------|-----|---------------|--------|----------------|
| PT-POE.00 | Apply 56 V to PoE module; assert ON/OFF control; verify subsystem powers on (no fault, LED active) | PoE VIN | 56 V | ±5% | 53.2–58.8 V; no fault indication | ESH10000534 datasheet (44–57 V input range) | 56 V supply via TA; PoE ON/OFF GPIO from Accordion |
| PT-POE.01 | Connect Ethernet PD load to ETH OUT; verify PoE negotiation completes (Cyan LED, normal polarity) | PoE link | — | — | Cyan LED active; PD load powered | ESH10000534 datasheet (TPS23881) | Ethernet PD load on ETH OUT |
| PT-POE.02 | Read VMEAS; verify within ±2.5% of applied voltage | VMEAS | 56.0 V | ±2.5% | 54.6–57.4 V | ESH10000534 datasheet (VMEAS ±2.5%) | — |
| PT-POE.03 | Draw ~100 mA from ETH OUT; read IMEAS; verify within ±3% | IMEAS | 100 mA | ±3% | 97–103 mA | ESH10000534 datasheet (IMEAS ±3%) | Calibrated Ethernet PD load on ETH OUT |

---

## Test Adapter Requirements Summary

The following is a preliminary list of what ESH10000654 must provide to support this test plan. This should be used as input to ESH10000654 R0 SPECIFICATION.md.

| Function | Requirement | Used By |
|----------|-------------|---------|
| 20 V power input | Route DC supply to Fixture Link VDD | PT-PWR.00 |
| PWR_EN control | GPIO from Accordion to Fixture Link PWR_EN | PT-PWR.01 |
| Power rail probe points | Test points for 12V, 5V, 3V3, VREF, ±18V | PT-PWR.02–.08 |
| AIN stimulus | Provide calibrated voltage stimulus to AIN_P/N channels | PT-SIG.02 |
| PWM probe/loopback | Access to PWM output for scope or loopback | PT-SIG.05 |
| Tach signal injection | Inject frequency signal to TACH input | PT-SIG.06 |
| RS485 driver/loopback | Drive or loopback RS485_TX for ADC test | PT-SIG.08 |
| Active Load supply (24 V, 2ch) | Route DC supply to VLOAD_POS_0 and VLOAD_POS_1 | PT-AL.00–.03 |
| PoE supply (56 V) | Route DC supply to PoE module VIN | PT-POE.00–.03 |
| PoE ON/OFF GPIO | GPIO from Accordion to PoE ON/OFF control | PT-POE.00 |
| Ethernet PD load | Passive PD load on ETH OUT for PoE negotiation and IMEAS test | PT-POE.01, PT-POE.03 |

---

## Open Items

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Define all system-level requirements in SPECIFICATION.md | Martin Johansson | Closed — requirements populated from Sparrow Hardware Datasheet v3 (44 requirements, SYS/PWR/COM/FW/SIG/COS) |
| 2 | Complete test adapter requirements (ESH10000654) driven by TA Requirements column above | Martin Johansson | In progress — SPECIFICATION.md drafted (21 req); 4 open interface items remain (PoE routing, PSU connector assignment, PWR_EN, PD load) |
| 3 | Confirm Accordion software API for I2C scan, SPI, GPIO, ADC readback | Martin Johansson | Open |
| 4 | Define DUT serial number format and IDPROM content | Martin Johansson | Open |
| 5 | Define firmware version to be loaded for production (ATmega) | Martin Johansson | Open |
| 6 | Decide if PT-SIG.02 (AIN stimulus) requires an isolated source or if TA provides a fixed reference | Martin Johansson | Open |
| 7 | Review ESH10000536 Active Load R2 verification plan; derive production test steps | Martin Johansson | Closed — no verification plan exists; PT-AL derived from system datasheet (IMEAS ±1%, VMEAS ±2%) |
| 8 | Review ESH10000534 PoE R4 verification plan; derive production test steps | Martin Johansson | Closed — no verification plan exists; PT-POE derived from system datasheet (TPS23881, VMEAS ±2.5%, IMEAS ±3%) |
