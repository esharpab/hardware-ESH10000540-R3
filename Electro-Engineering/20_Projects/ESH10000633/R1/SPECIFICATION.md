---
project: ESH10000633
product: Sparrow Complete Product
revision: R1
type: Specification
created: 2026-05-04
last_updated: 2026-05-04
---

# Specification: Sparrow Complete Product R1

## Scope

This document defines the product-level requirements and acceptance criteria for the Sparrow Complete Product R1.
Requirements are derived from the **Sparrow Hardware Datasheet v3 (2026-04-16)**, stored at:
`DOCS/Sparrow Hardware Datasheet-v3-20260504_150735.pdf`

The Sparrow is a multi-channel test instrument. The MES top-level BOM (ESH10000633 R1) contains two major sub-assemblies; their contents are listed below.

**ESH10000631 — Sparrow Accordion A2**

| Sub-assembly | ESH | Rev | Notes |
|-------------|-----|-----|-------|
| Accordion A2 Bare | ESH10000182 | — | Accordion base chassis |
| Sparrow N-Top | ESH10000535 | R3 | N-Top PCBA |
| Fixture Link | ESH10000543 | R2 | Interface PCBA between Accordion and Fixture Electronics |
| PoE | ESH10000534 | R4 | M.2 PoE module |

**ESH10000636 — Sparrow ASSY Fixture Electronics with Active Load**

| Sub-assembly | ESH | Rev | Notes |
|-------------|-----|-----|-------|
| Sparrow Fixture Electronics PCBA | ESH10000540 | R3 | Main fixture electronics |
| Sparrow IDC N-Top | ESH10000634 | R3 | IDC connector board for N-Top interface |
| Active Load | ESH10000536 | R2 | M.2 active load module |

Test tooling:

| Tool | ESH | Rev |
|------|-----|-----|
| Sparrow Test Adapter | ESH10000654 | R0 |

---

## Category Definitions

| Category | Description |
|----------|-------------|
| System | Assembly integrity, power input, and system-level integration |
| Power | Power rails — common, external, PoE, Active Load, PSU (optional) |
| Communication | I2C and RS485 bus integrity across sub-assemblies |
| Firmware | MCU responsiveness and IDPROM |
| Signal | End-to-end signal path integrity (AIN, MPIO, PWM, Tach, Relay, Fixed Load, Audio, Tampering) |
| Cosmetic | LED indication and visual quality |

---

## Requirements

> **Source:** All acceptance criteria are taken from Sparrow Hardware Datasheet v3, Section 5.2 (Electrical Characteristics) and Section 3 (Key Features), unless otherwise noted.

| Req ID | Category | Requirement | Acceptance Criteria | Test Case(s) | Status |
|--------|----------|-------------|---------------------|--------------|--------|
| SYS-01 | System | All sub-assemblies (Accordion A2, Fixture Link R2, N-Top R3, Fixture Electronics R3) installed and correctly seated; no connector damage | All present; no bent pins; connectors fully engaged | PT-M.00, PT-M.01 | Draft |
| SYS-02 | System | Revision marking on Fixture Link silkscreen is correct | Silkscreen reads R2 | PT-M.02 | Draft |
| SYS-03 | System | System powers on from 20 V DC input via Fixture Link eFuse | eFuse output present; key rails within spec after PWR_EN | PT-PWR.00, PT-PWR.01 | Draft |
| SYS-04 | System | PoE subsystem accepts isolated 44–57 V input | No fault; PoE ON/OFF functional | PT-POE.00 | Draft |
| PWR-01 | Power | Common 12V rail output voltage (all IDC connectors, pin 2) | 11.4 V ≤ V ≤ 12.6 V | PT-PWR.02, PT-PWR.03 | Draft |
| PWR-02 | Power | Common 5V rail output voltage (all IDC connectors, pin 1) | 4.75 V ≤ V ≤ 5.25 V | PT-PWR.04 | Draft |
| PWR-03 | Power | 12V_EXT external rail output voltage | 11.6 V ≤ V ≤ 12.4 V | PT-PSU.00 | Draft |
| PWR-04 | Power | 3V3_EXT external rail output voltage | 3.23 V ≤ V ≤ 3.37 V | PT-PSU.03 | Draft |
| PWR-05 | Power | 1V8_EXT external rail output voltage | 1.76 V ≤ V ≤ 1.82 V | PT-PSU.04 | Draft |
| PWR-06 | Power | VADJ programmable rail range and accuracy | 0–6 V user-adjustable; accuracy ±1.6% | PT-PSU.01 | Draft |
| PWR-07 | Power | EXT_VIO programmable rail range and accuracy | 0–3.3 V user-adjustable; accuracy ±1.6% | PT-PSU.02 | Draft |
| PWR-08 | Power | VREF precision reference voltage | 2.499 V ≤ V ≤ 2.501 V; Iout ≤ ±10 mA; must not drive loads | PT-PWR.06 | Draft |
| PWR-09 | Power | External rails (12V_EXT, 3V3_EXT, 1V8_EXT, VADJ, EXT_VIO) overcurrent protection | Circuit breaker activates at Ilim = 0.5 A; fault flag raised; rail stays off until re-enabled | — | Draft |
| PWR-10 | Power | External rails voltage monitoring accuracy (VMEAS) | ±2% of nominal for all external rails | PT-PSU.00–.04 | Draft |
| PWR-11 | Power | External rails current monitoring accuracy (IMEAS) | ±10% of set current for all external rails | — | Draft |
| PWR-12 | Power | N-Top +18V rail output voltage | 17.82 V ≤ V ≤ 18.18 V (±1%) | PT-PWR.07 | Draft |
| PWR-13 | Power | N-Top −18V rail output voltage | −18.18 V ≤ V ≤ −17.82 V (±1%) | PT-PWR.08 | Draft |
| PWR-14 | Power | PoE input voltage range | Vin: 44–57 V; nominal 54 V | PT-POE.00 | Draft |
| PWR-15 | Power | PoE maximum output power | Pout ≤ 90 W | — | Draft |
| PWR-16 | Power | PoE voltage measurement accuracy (VMEAS) | ±2.5% of supply voltage | PT-POE.02 | Draft |
| PWR-17 | Power | PoE current measurement accuracy (IMEAS) | ±3% of measured current | PT-POE.03 | Draft |
| PWR-18 | Power | Active Load source voltage range | 0–24 V | PT-AL.00, PT-AL.02 | Draft |
| PWR-19 | Power | Active Load sink current — IDC header | 0–0.4 A continuous; 0–1 A peak | PT-AL.00, PT-AL.02 | Draft |
| PWR-20 | Power | Active Load sink current — Phoenix connector | 0–3 A continuous; 0–5 A peak | — | Draft |
| PWR-21 | Power | Active Load energy limit per run | EMAX ≤ 250 Ws; load shuts off at threshold | — | Draft |
| PWR-22 | Power | Active Load voltage measurement accuracy (VMEAS) | ±2% of load voltage | PT-AL.01, PT-AL.03 | Draft |
| PWR-23 | Power | Active Load current measurement accuracy (IMEAS) | ±1% of sink current | PT-AL.00, PT-AL.02 | Draft |
| PWR-24 | Power | PSU (optional) output voltage range and accuracy | 0–18 V; accuracy ±0.5%; VMEAS ±0.5%; IMEAS ±1.5% | — | Draft |
| COM-01 | Communication | I2C Controller accessible end-to-end; all expected devices ACK | Fixture Link expander @0x20; EEPROM @0x50; N-Top ATmega @0x30; LED driver @0x14 or 0x0C; N-Top expander @0x20; IDPROM @0x50 | PT-COMM.00–.02 | Draft |
| COM-02 | Communication | I2C Controller fast-mode operation | 400 kHz operation; EXT_VIO selectable 1.5–3.3 V | PT-COMM.02 | Draft |
| COM-03 | Communication | I2C Device (EEPROM 24AA02UID) writable and readable | Write/read-back succeeds; device ACKs 0x50–0x57 | PT-COMM.01, PT-FW.01 | Draft |
| COM-04 | Communication | SPI: both AD5592R devices on Fixture Electronics accessible | Read/write both devices without error | PT-COMM.03 | Draft |
| COM-05 | Communication | RS485 full-duplex interface operational | Data rate ≥ 1 Mbps; VMEAS range 0–5 V; TX differential signal present | PT-SIG.08 | Draft |
| FW-01 | Firmware | ATmega MCU programmed and responding on I2C | ATmega ACKs at address 0x30 | PT-FW.00, PT-COMM.02 | Draft |
| FW-02 | Firmware | IDPROM writable and readable | Write/read-back of IDPROM succeeds | PT-FW.01 | Draft |
| SIG-01 | Signal | MPIO (4 channels): analog/digital I/O 0–5 V | Vin/Vout 0–5 V; gain error ±0.3%; offset ±8 mV; throughput 96 kSPS; IOUT ±5 mA | PT-SIG.00 | Draft |
| SIG-02 | Signal | FE_MPIO (12 channels): analog/digital I/O 0–5 V, OV protected | Vin/Vout 0–5 V; OV tolerance 15 V; gain error ±0.3%; offset ±8 mV; throughput 2 kSPS; IOUT ±5 mA | PT-SIG.01 | Draft |
| SIG-03 | Signal | Differential AIN (8 channels): high-range precision measurement | Range ±48 V; calibrated gain error ±0.15%; calibrated offset ±2 mV; resolution 12-bit; throughput 96 kSPS | PT-SIG.02 | Draft |
| SIG-04 | Signal | PWM (2 channels): programmable frequency and duty cycle | Frequency 1 Hz–1 MHz; duty 0–100%; VCCO 0–3.3 V; VOH ≥ 2.9 V @3.3V/10mA; VOL ≤ 0.33 V @3.3V/10mA | PT-SIG.05 | Draft |
| SIG-05 | Signal | Tach (2 channels): frequency measurement input | Frequency counted correctly | PT-SIG.06 | Draft |
| SIG-06 | Signal | Relay driver (4 channels): low-side drive within spec | VCOIL 5–12 V; ICOIL ≤ 60 mA; integrated flyback protection | — | Draft |
| SIG-07 | Signal | Fixed Load (4 channels): switchable 2.2 kΩ to GND with voltage monitoring | RLOAD 2156–2244 Ω; VMEAS range 0–5 V; VMEAS gain error ±1.6%; offset ±6 mV | PT-SIG.03 | Draft |
| SIG-08 | Signal | Audio Load: switchable phantom/bias loads with voltage monitoring | RLOAD_PHANTOM 666–716 Ω; RLOAD_BIAS 2156–2264 Ω; VMEAS_RANGE 0–15 V; gain error ±1.6%; offset ±6 mV | PT-SIG.04 | Draft |
| SIG-09 | Signal | Tampering (2 channels): latch-and-hold edge detection | VIH 2.3–5.5 V; VIL −0.5–0.6 V; latch preserved until software reset | — | Draft |
| SIG-10 | Signal | USR_GPIO functional | GPIO driven HIGH reads back HIGH | PT-SIG.07 | Draft |
| COS-01 | Cosmetic | Power LED illuminates when asserted via Fixture Link expander | Power LED blue | PT-COS.00 | Draft |
| COS-02 | Cosmetic | RS-232 LED illuminates when asserted via Fixture Link expander | RS-232 LED blue | PT-COS.01 | Draft |
| COS-03 | Cosmetic | User LEDs (LP5012) respond to register write | At least one LED channel responds | PT-COS.02 | Draft |

---

## Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| R1 | 2026-05-04 | Martin Johansson | Initial document created; requirements table populated from Sparrow Hardware Datasheet v3 |
| R1 | 2026-05-04 | Martin Johansson | Sub-assembly table restructured to reflect two-level MES BOM hierarchy; ESH10000634 (Sparrow IDC N-Top) added |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Design Engineer | | | |
| Quality | | | |
