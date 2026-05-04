---
project: ESH10000540
product: Sparrow Fixture Electronics PCBA
revision: R3
type: Verification and Production Test
created: 2026-04-28
last_updated: 2026-05-04
---

# Specification: Sparrow Fixture Electronics PCBA (R3)

## Scope

This document defines the functional requirements, test scope, and acceptance criteria for
Sparrow Fixture Electronics PCBA revision R3 verification and production test.
Requirements are derived from the R2 verification plan (Verification_Sparrow_FE.xlsx, DUT sheet).

---

## Requirements

### Category definitions

| Category | Description |
|----------|-------------|
| Mechanical | Physical assembly checks |
| Power | Power rail generation, switching, monitoring, and protection |
| User IO | User-facing I/O channels (analog, digital, communication) |
| Controller IO | Internal controller buses and peripherals |
| Connectors | Connector signal mapping |

---

### Requirements table

| Req ID | Category | Requirement | Acceptance Criteria | Test Case(s) | Status |
|--------|----------|-------------|---------------------|--------------|--------|
| SR-M01 | Mechanical | All no-mount (NM) components must not be populated | Visual inspection: all NM components absent | M.00 | Pending |
| SR-M02 | Mechanical | Spacers for N-Top (M1, M2), M.2 Active Load (M3, M4), and M.2 PSU (M5, M6) must fit mechanically | All spacer groups fit without mechanical interference | M.01–M.03 | Pending |
| SR-P01 | Power | VDD (20 V) input supply must be within tolerance | 20.000 V ±5.0% (DMM) | P.00 | Pending |
| SR-P02 | Power | 12 V DC/DC, 12V_EXT switched output, IDC availability, voltage monitoring, current limit, and current sensing must all be within spec | 12 V ±5%; 12V_EXT ±5%; VMON_12V_EXT ±2.4%; PG trips at 500 mA ±5%; IMON_12V_EXT_R ±10% | P.01–P.07 | Pending |
| SR-P03 | Power | 6V5 DC/DC, 6V5_LIM switched output, VADJ_EXT adjustable output (1.5–6 V), voltage monitoring, current limit, and current sensing must all be within spec | 6V5 ±2.5%; VADJ_EXT ±2.5%; VMON_VADJ_EXT ±2.0%; PG trips at 500 mA ±5%; IMON_VADJ_EXT ±10% | P.08–P.19 | Pending |
| SR-P04 | Power | 5 V DC/DC, 5V_LIM switched output, IDC availability, VIO_EXT adjustable output (1.5–3.3 V), voltage monitoring, current limit, and current sensing must all be within spec | 5 V ±2.5%; VIO_EXT ±2.5%; VMON_VIO_EXT ±1.1%; PG trips at 500 mA ±5%; IMON_VIO_EXT ±10% | P.20–P.30 | Pending |
| SR-P05 | Power | 3V3 LDO, 3V3_EXT switched output, voltage monitoring, current limit, and current sensing must all be within spec | 3V3 ±2.5%; 3V3_EXT ±2.5%; VMON_3V3_EXT ±1.8%; PG trips at 500 mA ±5%; IMON_3V3_EXT_R ±10% | P.31–P.36 | Pending |
| SR-P06 | Power | 3V3_LIM switch, 1V8 LDO (1V8_EXT), voltage monitoring, current limit, and current sensing must all be within spec | 3V3_LIM ±2.5%; 1V8_EXT ±2.5%; VMON_1V8_EXT ±1.0%; PG trips at 500 mA ±5%; IMON_1V8_EXT ±10% | P.37–P.42 | Pending |
| SR-P07 | Power | VREF 2.500 V reference supply must be within tight tolerance | 2.500 V ±0.14% (DMM) | P.43 | Pending |
| SR-P08 | Power | UART-RS485 charge pump supply nodes (C1+/-, C2+/-, VS+, VS-) must all be present with non-zero voltages | Non-zero voltage measured by DMM on all four nodes | P.44–P.47 | Pending |
| SR-P09 | Power | Power LED must indicate active Fixture Link connection | LED_GREEN illuminates when Fixture Link is active | P.48 | Pending |
| SR-P10 | Power | Audio bias loads (MIC_BIAS_LOAD_L/Ln/R/Rn) and phantom loads (PHANTOM_LOAD_L/Ln/R/Rn) must produce correct load currents | Bias: 2.273 mA ±2.3%; Phantom: 7.353 mA ±5.4% | P.49–P.56 | Pending |
| SR-P11 | Power | Fixed loads (GND_SW0–GND_SW3) must produce correct load current when activated | 2.273 mA ±2.0% at 5 V | P.57–P.60 | Pending |
| SR-U01 | User IO | Audio ADC must correctly measure bias voltages at MIC_IN_L, MIC_IN_Ln, MIC_IN_R, and MIC_IN_Rn at both 15 V and 0.1 V stimulus | 15 V ±2.4%; 0.1 V ±7.1% | UIO.00–UIO.07 | Pending |
| SR-U02 | User IO | RS485 ADC must correctly measure RS485_TX* and RS485_RX* voltages | RS485_TX* logic-1: >0.2 V ±2.5%; RS485_RX* at 2.5 V ±1.9%; RS485_RX* at 0.1 V ±7.1% | UIO.08–UIO.10 | Pending |
| SR-U03 | User IO | Fixed load ADC must correctly measure GND_SW0–GND_SW3 output voltages at 5 V and 0.1 V stimulus | 5 V (informational); 0.1 V ±6.4% | UIO.11–UIO.18 | Pending |
| SR-U04 | User IO | MPIO_0–3 ADC must read applied input voltages within tolerance; DAC must output set voltages within tolerance | ADC: 0.1 V ±9.0%, 4 V ±0.7%; DAC: 0.1 V ±6.9%, 4 V ±0.55% | UIO.19–UIO.34 | Pending |
| SR-U05 | User IO | FE_MPIO_0–11 ADC must read applied input voltages; DAC must output set voltages; pseudo-digital input mode must function with 4.5 V / 0.5 V thresholds | ADC: 0.1 V ±9.0%, 4 V ±0.7%; DAC: 0.1 V ±6.9%, 4 V ±0.55%; pseudo-digital: correct HIGH at 5 V, LOW at 0 V | UIO.35–UIO.83 | Pending |
| SR-U06 | User IO | USR_GPIO_1–4 must function as digital input (VIL <0.8 V → LOW, VIH >2.0 V → HIGH) and digital output (VOL <0.5 V, VOH >2.3 V) | Input and output levels within stated thresholds | UIO.84–UIO.91 | Pending |
| SR-U07 | User IO | Analog high-range channels (AIN_P/N, CH1–8) must measure correctly at all gain settings (16, 8, 4, 2, 1, 0.5, 0.25, 0.125). Calibration required before measurement. | G16: ±4.9% @0.05 V; G8: ±2.5% @0.1 V; G4: ±0.58% @0.5 V; G2: ±0.34% @1 V; G1: ±0.22% @2 V; G0.5: ±0.13% @8 V; G0.25: ±0.115% @16 V; G0.125: ±0.11% @24 V. Note: R2 AIN_N at G0.25 failed on one board; R2 ±30 V test failed — reduced to ±24 V. | UIO.92–UIO.220 | Pending |
| SR-U08 | User IO | Latch function must operate correctly for both polarity settings | LATCH*_VALUE reflects correct state after reset and drive; both POL=0 and POL=1 modes pass | UIO.221–UIO.222 | Pending |
| SR-U09 | User IO | I2C_4 (I2C26) transceiver must meet I2C spec UM10204 for VIL, t_high, and t_rise at 1.5 V, 1.8 V, 2.5 V, and 3.3 V | VIL_max ≤0.3×VCC; t_high ≥0.6 μs; t_rise ≤0.3 μs. Note: R2 t_low (UIO.232–235) failed at all voltages — root cause must be identified for R3. | UIO.223–UIO.243 | Pending |
| SR-U10 | User IO | UART-RS485 loopback must successfully transfer frames at up to 1 Mbps | All sent frames received correctly; no frame errors | UIO.244 | Pending |
| SR-U11 | User IO | PWM output must produce correct frequency and duty cycle across supported voltage ranges | Frequency and duty cycle match programmed values (oscilloscope verification) | UIO.245 | Pending |
| SR-U12 | User IO | Active load channels 0 and 1 must control current (0.5 A, 1 A, 2 A) and correctly measure local and remote voltage via ADC | Current matches set point (DMM reference); local and remote voltage reads within tolerance | UIO.246–UIO.263 | Pending |
| SR-C01 | Controller IO | Controller I2C buses (I2C_1/I2C23, I2C_2/I2C24, I2C_3/I2C25) must enumerate all expected devices | I2C_1: ADC/DAC @0x10/11/48/49/4A, GPIO expander @0x20, IDPROM @0x50–57, LED driver @0x28/3C; I2C_2: M.2 Active Load @0x0C/10/14/48/49/50–57; I2C_3: M.2 PSU @0x48/4D/50–57 | CIO.00–CIO.02 | Pending |
| SR-C02 | Controller IO | IO Expander RESET_N pin must function correctly at power-up | RESET_N behavior matches expected sequence at power-up | CIO.03 | Pending |
| SR-C03 | Controller IO | ADC/DAC RESETn pin must function correctly | RESETn behavior matches expected sequence | CIO.04 | Pending |
| SR-C04 | Controller IO | LSHM PRESENCEn pin must correctly detect LSHM presence | PRESENCEn pin state is correct for connected and disconnected conditions | CIO.05 | Pending |
| SR-CN01 | Connectors | Signal mapping must be correct for all connectors: LSHM, N-Top, M.2 Active Load, M.2 PSU, Fixture Link, and Audio Load | All signals route to correct connector pins per schematic | C.00–C.05 | Pending |

---

## Test Scope

**In Scope:**
- Mechanical assembly inspection
- Power rail generation, switching, protection, and monitoring
- All user-facing I/O: analog channels, MPIO, FE_MPIO, GPIO, AIN high-range, audio, RS485, UART, PWM, active load
- Controller I2C device enumeration and peripheral control
- Connector signal mapping

**Out of Scope:**
- EMC/EMI testing
- Environmental testing (temperature, humidity)
- Production burn-in
- Software/firmware validation beyond I/O functional tests

---

## Acceptance Criteria

- All requirements status = Pass.
- No open Fail findings without documented disposition.
- DUT_LOG.md complete and traceable.

---

## Revision History

| Revision | Date | Changes |
|----------|------|---------|
| R3 | 2026-05-04 | Requirements derived from R2 verification plan (Verification_Sparrow_FE.xlsx); R2 failure notes captured in SR-U07 and SR-U09 |

---

## Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Design Lead | | | |
| Test Lead | | | |
| Quality | | | |

*Not signed off until verification is complete.*
