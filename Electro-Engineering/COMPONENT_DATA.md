# Component Data — Global Reference

> **Authority:** Single source of truth for component datasheet reference data across all E-Sharp engineering projects.  
> **Rule:** Datasheet content is **append-only**. Do not modify or delete existing entries. If a correction is needed, add a dated note immediately after the affected content.  
> **Rule:** Generic datasheet data only. Project-specific connections, net names, and workarounds must be tagged `> **[ESHxxxxxxxx Rx]:**` in a "Project Usage Notes" subsection.  
> **Contributing:** See [`30_Workflows/component-data-workflow.md`](30_Workflows/component-data-workflow.md) for the full process, entry template, and AI extraction prompt.

---

## Table of Contents

- [LT3942](#lt3942) — Buck-Boost LED Driver / Voltage Regulator (Analog Devices)
- [PI4IOE5V6416](#pi4ioe5v6416) — 16-bit I2C GPIO Expander (Diodes Inc.)
- [ESP32-C6-MINI-1](#esp32-c6-mini-1) — Wi-Fi 6 / BLE 5 / 802.15.4 MCU Module (Espressif)
- [BQ24075T](#bq24075t) — Li-Ion Battery Charger with Power Path (Texas Instruments)
- [ADS7828](#ads7828) — 12-bit 8-channel I2C ADC (Texas Instruments)
- [MCP1700](#mcp1700) — 250 mA Ultra-Low Iq LDO Regulator (Microchip Technology)
- [SX1276](#sx1276) — LoRa / FSK Transceiver 137–1020 MHz (Semtech)
- [MPZ2012S102AT000](#mpz2012s102at000) — 1 kΩ @ 100 MHz Ferrite Bead, 0805 (TDK)
- [CS06465-32M (NDK NX2016SA)](#cs06465-32m-ndk-nx2016sa) — 32 MHz SMD Crystal (NDK)
- [A782MS227M1VLAS020](#a782ms227m1vlas020) — 220 µF / 35 V Aluminium Electrolytic Capacitor (Vishay)
- [SRP7028AA Series](#srp7028aa-series) — Shielded Power Inductor 0.15–22 µH (Bourns)
- [XRCGB32M000F3M00R0](#xrcgb32m000f3m00r0) — 32 MHz SMD Crystal 2016 (Murata)
- [INA333](#ina333) — Zero-Drift Instrumentation Amplifier (Texas Instruments)
- [ESP32-S3](#esp32-s3) — Dual-Core LX7 SoC, Wi-Fi 4 + BT5, QFN56 (Espressif)
- [WM8962B](#wm8962b) — Ultra-Low Power Stereo CODEC with Class D Speaker Amp (Cirrus Logic)
- [TRSF3232E](#trsf3232e) — 3 V–5.5 V Dual RS-232 Transceiver with Charge Pump (Texas Instruments)
- [24AA025UID](#24aa025uid) — 2 Kbit I2C EEPROM with Preprogrammed 32-bit Unique ID, Cascadable (Microchip)
- [MAX491E / MAX491ESD](#max491e--max491esd) — ±15 kV ESD-Protected Full-Duplex RS-485/RS-422 Transceiver (Maxim)
- [AMS1117](#ams1117) — 1 A Adjustable/Fixed Low Dropout Linear Regulator (Advanced Monolithic Systems)
- [SN74LVC2G06](#sn74lvc2g06) — Dual Inverter Buffer with Open-Drain Outputs (Texas Instruments)
- [SN74HCS86](#sn74hcs86) — Quad 2-Input Exclusive-OR Gate (Texas Instruments)
- [SN74HCS74](#sn74hcs74) — Dual D-Type Flip-Flop with Clear and Preset (Texas Instruments)
- [REF3425-EP](#ref3425-ep) — 2.5 V Enhanced Product Precision Voltage Reference (Texas Instruments)
- [TPS54302](#tps54302) — 4.5V–28V, 3A, EMI-Friendly Synchronous Buck Converter (Texas Instruments)
- [PCA9616](#pca9616) — 3-Channel Fm+ Differential I2C-Bus Buffer with Hot-Swap Logic (NXP)
- [PCA9506](#pca9506) — 40-Bit I2C-Bus I/O Port with RESET, OE and INT (NXP)
- [24AA02UID](#24aa02uid) — 2 Kbit I2C EEPROM with Unique 32-Bit Serial Number (Microchip)
- [ALM2402-Q1](#alm2402-q1) — AEC-Q100 Dual High-Current Op-Amp, 400 mA (Texas Instruments)
- [TPS259474](#tps259474) — 2.7V–23V 5.5A eFuse, Adjustable OVLO, Circuit Breaker (Texas Instruments)
- [AD5593R](#ad5593r) — 8-Channel 12-bit Configurable ADC/DAC with I2C Interface (Analog Devices)
- [SN74HCS32](#sn74hcs32) — Quadruple 2-Input OR Gate with Schmitt-Trigger Inputs (Texas Instruments)
- [KAQY214](#kaqy214) — 400 V / 130 mA N.O. PhotoMOS Solid State Relay (COSMO Electronics)
- [G20N06D52](#g20n06d52) — 60V / 20A N-Channel Enhancement Mode Power MOSFET, Dual DFN5×6-8L (Goford Semiconductor)
- [PS509LEX](#ps509lex) — Differential 4:1 / Dual 4:1 Precision Analog Multiplexer (Diodes Inc.)
- [SN74LVC126APW](#sn74lvc126apw) — Quad Bus Buffer with 3-State Outputs, Active-HIGH OE (Texas Instruments)
- [SN74LVC125APW](#sn74lvc125apw) — Quad Bus Buffer with 3-State Outputs, Active-LOW OE (Texas Instruments)
- [SN74LVC07APW](#sn74lvc07apw) — Hex Buffer and Driver with Open-Drain Outputs (Texas Instruments)
- [LTC3265EDHC](#ltc3265edhc) — Dual Charge Pump + Dual LDO Bipolar Supply (Analog Devices / Linear Technology)
- [AD5592R](#ad5592r) — 8-Channel 12-bit Configurable ADC/DAC/GPIO with SPI Interface (Analog Devices)
- [PGA849](#pga849) — Low-Noise Wide-Bandwidth Precision Programmable Gain InAmp (Texas Instruments)
- [74LVC1G19DBV](#74lvc1g19dbv) — Single 1-of-2 Decoder / Demultiplexer (Nexperia)
- [OPA192](#opa192) — Precision Rail-to-Rail I/O Op-Amp (Texas Instruments)
- [LP5012RUKR](#lp5012rukr) — 12-Channel I2C RGB LED Driver (Texas Instruments)
- [ATmega4809](#atmega4809) — 48-Pin megaAVR 0-Series Microcontroller (Microchip Technology)
- [SN74AVC4T774RGYR](#sn74avc4t774rgyr) — 4-Bit Dual-Supply Bus Transceiver with Independent Direction Control (Texas Instruments)
- [TLV9102IDR](#tlv9102idr) — Dual Low-Voltage Rail-to-Rail Op-Amp (Texas Instruments)
- [SN74LVC1G125DBVR](#sn74lvc1g125dbvr) — Single Low-Voltage FET Bus Switch, Active-LOW OE (Texas Instruments)
- [SN74LVC1G126DBVR](#sn74lvc1g126dbvr) — Single Bus Buffer with 3-State Output, Active-HIGH OE (Texas Instruments)

---

## LT3942

**Manufacturer:** Analog Devices (formerly Linear Technology)  
**Mfr Part Number:** LT3942  
**Package:** 28-pin TSSOP  
**Category:** IC — Power / LED Driver  
**Datasheet:** LT3942 datasheet (Analog Devices / Linear Technology)  
**Added:** 2026-04 (migrated from ESH10000662 R0)  
**Used in:** ESH10000662 R0, ESH10000662 R1

4-switch buck-boost LED driver and voltage regulator with PWM dimming, UVLO, OVLO, soft-start, and current monitoring.

### Formulas

#### Current Sense (CTRL / IOUT)

| Condition | Formula |
|-----------|---------|
| VCTRL < 1.15 V | `I_IS(MAX) = (VCTRL − 0.25 V) / (10 × RIS)` — linear |
| 1.15 V ≤ VCTRL ≤ 1.35 V | Nonlinear transition — see table below |
| VCTRL > 1.35 V | `I_IS(MAX) = 100 mV / RIS` — constant full scale |

**V(ISP−ISN) threshold vs VCTRL (datasheet Table 2):**

| VCTRL (V) | V(ISP−ISN) (mV) |
|-----------|----------------|
| 1.15 | 90 |
| 1.20 | 94.5 |
| 1.25 | 98 |
| 1.30 | 99.5 |
| 1.35 | 100 |

- **RIS** — current sense resistor (Ω); datasheet label, not project ref des
- **VCTRL** — voltage at CTRL pin

#### UVLO (EN/UVLO pin resistor divider)

Rising threshold: `UVLO(+) = 1.235 V × (R1 + R2) / R2 + 2.5 µA × R1`  
Falling threshold: `UVLO(−) = 1.220 V × (R1 + R2) / R2`

#### OVLO (OVLO pin resistor divider)

Rising threshold: `OVLO(+) = 1.220 V × (R3 + R4) / R4`  
Falling threshold: `OVLO(−) = 1.185 V × (R3 + R4) / R4`

> R1–R4 are generic datasheet labels — not project schematic reference designators.

#### Current Monitor (ISMON)

`VISMON = 10 × (VISP − VISN) + 250 mV`

VISMON = 1.25 V at full scale (V(ISP−ISN) = 100 mV).

#### Output Voltage (FB resistor divider — voltage regulator mode)

`VOUT = 1.00 V × (R5 + R6) / R6`  
`VOUT(OVP) = 1.05 V × (R5 + R6) / R6`

- R5 — top resistor (PVOUT to FB); datasheet label
- R6 — bottom resistor (FB to GND); datasheet label
- FB regulation target: 1.00 V (±1.5%)

#### Soft-Start Time (voltage regulator mode)

`tSS = 1 V × CSS / 12.5 µA`

CSS — external capacitor from SS pin to GND. Recommended starting value: 22 nF → tSS ≈ 1.76 ms.

#### Switching Frequency vs RT Resistor

| fOSC (kHz) | RT (kΩ, 1%) |
|------------|-------------|
| 300 | 178 |
| 400 | 124 |
| 600 | 78.7 |
| 800 | 56.2 |
| 1000 | 43.2 |
| 1200 | 33.2 |
| 1400 | 26.7 |
| 1600 | 21.5 |
| 1800 | 17.8 |
| 2000 | 14.3 |

#### Maximum Output Current

`IOUT ≤ 0.1 × VOUT`

Accounts for RDS(ON) of power switches and DCR of inductor at elevated junction temperature.

#### Inductor Selection

Minimum inductance — buck region (highest ripple at PVIN(MAX)):
```
L_BUCK > PVOUT × (1 − PVOUT/PVIN(MAX)) / (fSW × IOUT(MAX) × ΔIL%)
```

Minimum inductance — boost region (lowest ripple at PVIN(MIN)):
```
L_BOOST > PVIN(MIN)² × (PVOUT − PVIN(MIN)) / (fSW × IOUT(MAX) × ΔIL% × PVOUT²)
```

Minimum for stability (prevents subharmonic oscillation):
```
L > VOUT / (2 × fSW × ISW(MAX))
```

- ΔIL% — allowable inductor current ripple (fraction, e.g. 0.3 for 30%)
- ISW(MAX) — maximum switch current limit = 2 A (min)
- Use shielded, low-DCR ferrite inductor

#### Loop Compensation (voltage regulator mode)

VC pin: **680 pF** compensation capacitor + **75 kΩ** series resistor. CSS must be ≥ 5–10× VC compensation capacitor.

#### Input RMS Current (worst case, buck region)

`IRMS ≈ IOUT(MAX) × √(PVOUT/PVIN × (1 − PVOUT/PVIN))`

Worst case at PVIN = 2 × PVOUT → `IRMS ≈ IOUT(MAX) / 2`

### Operating Modes

| PVIN / PVOUT ratio | Mode | Control scheme |
|--------------------|------|----------------|
| >> 1 (PVIN much higher) | Buck | Peak-buck current mode; C always off, D always on |
| ~> 1 (PVIN slightly higher) | Buck-boost | Peak-buck; C on for first 20% of cycle |
| <~ 1 (PVIN slightly lower) | Buck-boost | Peak-boost; A on for first 80% of cycle |
| << 1 (PVIN much lower) | Boost | Peak-boost current mode; A always on, B always off |

Switchover thresholds (ISP/ISN common mode): low-to-high at 1.7 V, high-to-low at 1.6 V.

### Startup / Enable Threshold Sequence

| EN/UVLO voltage | State |
|-----------------|-------|
| < 0.3 V | Shutdown — VIN quiescent < 2 µA |
| 0.3–0.9 V | Shutdown exit / wake-up begins |
| 0.9–1.220 V | UVLO mode — 2.5 µA pull-down active; INTVCC charges |
| > 1.235 V (rising) | Enable mode — switching permitted once OVLO cleared |

OVLO: switching blocked when OVLO pin > 1.220 V (rising); resumes at 1.185 V (falling, 35 mV hysteresis).

**SS pin startup thresholds:**

| SS voltage | Transition |
|------------|-----------|
| SS pulled to GND | POR / UVLO / OVLO / thermal shutdown |
| SS < 0.2 V + PWMON high | Enter UP/PRE (soft-start charging begins) |
| SS > 0.25 V | Enter UP/TRY → UP/RUN; switching enabled |
| SS < 1 V | FB regulated to SS voltage (soft-start ramp) |
| SS > 1.75 V | Enter OK/RUN; fault detection active |
| SS discharged below 1.7 V (fault) | Enter DOWN/STOP; switching disabled |
| SS discharged below 0.2 V (fault) | Re-enter UP/RUN (hiccup) |

PWM pin must be above threshold (> 1.5 V in external mode, or VREF/INTVCC in voltage regulator) for PWMON to go high and allow switching to start.

### Voltage Regulator Configuration Reference

Settings that differ from LED driver defaults (datasheet Table 4):

| Pin | Voltage Regulator setting |
|-----|--------------------------|
| RP | Tie to GND |
| PWM | Tie to VREF or INTVCC (load switch control); forced low disables all switches |
| V(ISP−ISN) | Acts as current limit (not current regulation) |
| SS | 100 kΩ to VREF (keep-running fault mode — mandatory for voltage regulator) |
| FB | Programs output voltage and OVP threshold |

### Pin Functions

| Pin | Name | Description |
|-----|------|-------------|
| PVIN | Power Input | Connects to converter power input. Bypass to GND with ceramic capacitor placed as close as possible to chip, with vias to ground plane. |
| VIN | Bias Supply | Supplies internal circuitry and INTVCC regulator. Connect to PVIN or another supply. Bypass to GND with ceramic capacitor. |
| INTVCC | Internal 3.6 V LDO Output | Powered from VIN; supplies internal control circuitry and gate drivers. Bypass to GND with minimum 1 µF ceramic capacitor. |
| EN/UVLO | Enable / Undervoltage Lockout | Force below 0.3 V to shut down (VIN quiescent < 2 µA). Force above 1.235 V for normal operation. Falling threshold 1.220 V; 2.5 µA pull-down enables UVLO hysteresis programming. Tie to VIN if unused. |
| OVLO | Overvoltage Lockout | Resistor divider from PVIN programs OVLO threshold. Force above 1.220 V to pull SS to GND and stop switching. Tie to GND if unused. |
| RP | PWM Dimming Frequency Set | Resistor to GND sets internal PWM dimming frequency. Max 1 MΩ; do not leave open. Tie to GND for external PWM dimming or voltage regulator mode. |
| PWM | Load Switch Enable / PWM Dim Input | Voltage regulator: controls ON/OFF of high-side PMOS load switch; tie to VREF or INTVCC if unused. LED driver: external PWM (0 V to >1.5 V digital) or internal PWM (1–2 V analog). Forcing low turns off all power switches, disconnects VC, and turns off PWMTG. |
| VREF | 2 V Reference Output | Accurate 2 V reference; up to 1 mA output current. Bypass to GND with minimum 0.22 µF ceramic capacitor. |
| CTRL | Current Sense Threshold Control | Programs ISP/ISN regulation current: `I_IS(MAX) = MIN(VCTRL − 0.25 V, 1 V) / (10 × RIS)`. Linear range 0.25–1.15 V; constant 100 mV threshold for VCTRL ≥ 1.35 V; smooth transition 1.15–1.35 V. Tie to VREF for 100 mV full scale. Force below 0.2 V to stop switching. |
| ISP | Current Sense Positive | Positive terminal of RIS sense resistor. Use Kelvin connection for accuracy. |
| ISN | Current Sense Negative | Negative terminal of RIS sense resistor. Use Kelvin connection for accuracy. |
| ISMON | Current Monitor Output | Buffered output = 10 × V(ISP−ISN) + 0.25 V. Equals 1.25 V at 100 mV full-scale V(ISP−ISN). |
| FAULT | Fault Open-Drain Output | Pulled low on open LED (VFB > 0.95 V and V(ISP−ISN) < 10 mV) or short LED (VFB < 0.25 V). Requires external pull-up. Updated during PWM high state; latched during PWM low. |
| SS | Soft-Start / Fault Mode | Capacitor to GND sets soft-start ramp (12.5 µA internal pull-up). UVLO, OVLO, or thermal shutdown pulls SS to GND immediately. Single resistor to VREF sets fault mode: no resistor = hiccup, 499 kΩ = latch-off, 100 kΩ = keep-running. In voltage regulator: always connect SS to VREF via 100 kΩ. |
| FB | Voltage Loop Feedback | Error amplifier regulates VFB to 1.00 V. Open LED (VFB > 0.95 V and V(ISP−ISN) < 10 mV) or short LED (VFB < 0.25 V) pulls FAULT low. Overvoltage (VFB > 1.05 V) turns off all power switches and PWMTG. |
| VC | Error Amplifier Output | Compensate control loop with external RC network. Disconnected from internal loads during PWM low state to preserve voltage for dimming performance. |
| RT | Switching Frequency Set | Resistor to GND sets oscillator frequency 300 kHz to 2 MHz. |
| SYNC/SPRD | Sync / Spread Spectrum | GND: internal oscillator. Clock signal: external sync. INTVCC: 25% triangle spread spectrum above internal oscillator. |
| PWMTG | Top Gate Drive | Buffered, inverted PWM drives external high-side PMOS switch. Voltage swing from MAX(PVOUT − 5 V, 1.2 V) to PVOUT. Leave open if unused. |
| PVOUT | Power Output | Connects to converter power output and serves as positive rail for PWMTG drive. Bypass to GND with ceramic capacitor close to chip, vias to ground plane. |
| SW2 | Boost Switch Node | Connects to internal power switches; swings GND to ~PVOUT + Vdiode. Minimise PCB area and trace length. |
| BST2 | Boost Bootstrap Supply | Integrated bootstrap diode from INTVCC. External bootstrap capacitor to SW2 required. |
| BST1 | Buck Bootstrap Supply | Integrated bootstrap diode from INTVCC. External bootstrap capacitor to SW1 required. |
| SW1 | Buck Switch Node | Connects to internal power switches; swings ~−Vdiode to PVIN. Minimise PCB area and trace length. |
| GND (EP) | Ground / Exposed Pad | Solder exposed pad directly to ground plane. |

### Project Usage Notes

> **[ESH10000662 R0]:** PWM pin found floating in R0 (ISS-002, closed). Must be strapped to 3.3 V via IO for all analog tests. Consistent with datasheet: forcing PWM low disables all power switches.

---

## PI4IOE5V6416

**Manufacturer:** Diodes Incorporated  
**Mfr Part Number:** PI4IOE5V6416 (2 ADDR pins, A1+A0); PI4IOE5V6416ZDEX (1 ADDR pin, TSSOP-24)  
**Package:** TSSOP-24  
**Category:** IC — Digital / GPIO Expander  
**Datasheet:** DS40821 Rev 4-2 (Diodes Inc., November 2024)  
**Added:** 2026-04 (migrated from ESH10000662 R0, ESH10000671 R0)  
**Used in:** ESH10000662 R0, ESH10000662 R1, ESH10000671 R0

Low-voltage translating 16-bit I2C GPIO expander. 16 I/Os in two 8-bit ports (P0 and P1). VDD(I2C) and VDD(P) independent (1.65–5.5 V each). PCA9555 / TCA9555 compatible.

### I2C Address

**Standard variant (2 address pins A1, A0):**

| A1 | A0 | 7-bit address |
|----|----|---------------|
| 0 | 0 | 0x20 |
| 0 | 1 | 0x21 |
| 1 | 0 | 0x22 |
| 1 | 1 | 0x23 |

**ZDEX variant (1 address pin ADDR):**

| ADDR | 7-bit address |
|------|---------------|
| GND | 0x20 |
| VCC | 0x21 |

### Power-on Reset Defaults

> **"All I/Os are set to inputs at reset."** — datasheet block diagram note.

| Register | Address | Default | Effect |
|---|---|---|---|
| Input port 0/1 | 00h/01h | `xxxx xxxx` | Read-only; reflects pin state |
| Output port 0/1 | 02h/03h | `0xFF` | Output latch = **all HIGH** |
| Polarity inversion 0/1 | 04h/05h | `0x00` | No inversion |
| Configuration 0/1 | 06h/07h | `0xFF` | All pins = **input** (1 = input, 0 = output) |
| Output drive strength 0/1 | 40h–43h | `0xFF` | Full drive strength |
| Input latch 0/1 | 44h/45h | `0x00` | Latching disabled |
| Pull-up/pull-down enable 0/1 | 46h/47h | `0x00` | **Pull resistors DISABLED** |
| Pull-up/pull-down selection 0/1 | 48h/49h | `0xFF` | Pull-up selected (irrelevant — disabled) |
| Interrupt mask 0/1 | 4Ah/4Bh | `0xFF` | All interrupts masked |
| Output port configuration | 4Fh | `0x00` | Push-pull output mode |

**Critical:** Pull resistors are **disabled by default**. All I/Os are true high-impedance on boot — pin voltage is determined entirely by external PCB circuitry. No active internal pull-ups until register 46h/47h is written.

### Output Mode Glitch Risk

When a pin transitions from input to output (bit in 06h/07h cleared from 1→0), the output latch (02h/03h) determines the driven level. Default output latch = `0xFF` (HIGH). If the driver clears the configuration bit **before** writing the desired output value, the pin briefly glitches HIGH regardless of intent.

**Safe driver init sequence: write output value first (02h/03h), then configure direction (06h/07h).**

### Pull Resistor Electrical Parameters

| Parameter | Min | Typ | Max | Unit |
|---|---|---|---|---|
| Internal pull-up resistance (Rpu) | 50 | 100 | 150 | kΩ |
| Internal pull-down resistance (Rpd) | 50 | 100 | 150 | kΩ |

Pull resistors apply to I/O pins only. Enable via 46h/47h; select direction via 48h/49h (1 = pull-up, 0 = pull-down).

### Functional Signals (ZDEX variant)

| Signal | Type | Description |
|--------|------|-------------|
| VCC | P | Supply. Bypass with 100 nF to GND. |
| GND | P | Ground |
| SDA | I/O | I2C data, open-drain |
| SCL | I | I2C clock |
| ADDR | I | Address select. GND → 0x20; VCC → 0x21 |
| INT | O | Interrupt output, active-low, open-drain. Pull up to VCC via 10 kΩ. Asserts on any input port state change. |
| RESET | I | Active-low reset. Pull to VCC via 10 kΩ; optional 100 nF to GND for POR glitch filter. |
| P00–P07 | I/O | Port 0 — 8-bit bidirectional GPIO |
| P10–P17 | I/O | Port 1 — 8-bit bidirectional GPIO |

### Key Register Summary for Driver Implementation

| Task | Registers | Notes |
|---|---|---|
| Set pin directions | 06h (P0), 07h (P1) | 1=input, 0=output. Write AFTER output values. |
| Set output values | 02h (P0), 03h (P1) | Write BEFORE setting direction to prevent glitch |
| Enable pull resistors | 46h (P0), 47h (P1) | 1=enable; disabled by default |
| Select pull direction | 48h (P0), 49h (P1) | 1=pull-up, 0=pull-down |

### Project Usage Notes

> **[ESH10000662 R0]:** Standard variant (2 address pins). A1=A0=0 → address 0x20.

> **[ESH10000671 R0]:** ZDEX variant (1 ADDR pin). ADDR tied to GND → address 0x20. INT connected to MCU GPIO via 10 kΩ pull-up. RESET passively held high via 10 kΩ (no MCU soft-reset; all GPIOs allocated).

---

## ESP32-C6-MINI-1

**Manufacturer:** Espressif Systems  
**Mfr Part Number:** ESP32-C6-MINI-1 (built-in PCB antenna); ESP32-C6-MINI-1U (external antenna connector)  
**Package:** 13.2 × 16.6 × 2.4 mm, 53-pad SMD module  
**Category:** Module / IC — MCU  
**Datasheet:** ESP32-C6-MINI-1/1U Datasheet (Espressif Systems)  
**Added:** 2026-04 (migrated from ESH10000671 R0)  
**Used in:** ESH10000671 R0

Wi-Fi 6 (802.11ax), BLE 5, and IEEE 802.15.4 (Zigbee/Thread) module. Single-core RISC-V at up to 160 MHz. Built-in PCB antenna (MINI-1) or U.FL external antenna connector (MINI-1U).

### Pin Description

| Name | No. | Type | Function |
|------|-----|------|----------|
| GND | 1, 2, 11, 14, 36–53 | P | Ground |
| 3V3 | 3 | P | Power supply |
| NC | 4 | — | NC |
| IO2 | 5 | I/O/T | GPIO2, LP_GPIO2, LP_UART_RTSN, ADC1_CH2, FSPIQ |
| IO3 | 6 | I/O/T | GPIO3, LP_GPIO3, LP_UART_CTSN, ADC1_CH3 |
| NC | 7 | — | NC |
| EN | 8 | I | High: chip on. Low: chip off (powers down). Do not leave EN floating. |
| IO4 | 9 | I/O/T | MTMS, GPIO4, LP_GPIO4, LP_UART_RXD, ADC1_CH4, FSPIHD |
| IO5 | 10 | I/O/T | MTDI, GPIO5, LP_GPIO5, LP_UART_TXD, ADC1_CH5, FSPIWP |
| IO0 | 12 | I/O/T | GPIO0, XTAL_32K_P, LP_GPIO0, LP_UART_DTRN, ADC1_CH0 |
| IO1 | 13 | I/O/T | GPIO1, XTAL_32K_N, LP_GPIO1, LP_UART_DSRN, ADC1_CH1 |
| IO6 | 15 | I/O/T | MTCK, GPIO6, LP_GPIO6, LP_I2C_SDA, ADC1_CH6, FSPICLK |
| IO7 | 16 | I/O/T | MTDO, GPIO7, LP_GPIO7, LP_I2C_SCL, FSPID |
| IO12 | 17 | I/O/T | GPIO12, USB_D- |
| IO13 | 18 | I/O/T | GPIO13, USB_D+ |
| IO14 | 19 | I/O/T | GPIO14 |
| IO15 | 20 | I/O/T | GPIO15 |
| NC | 21 | — | NC |
| IO8 | 22 | I/O/T | GPIO8 |
| IO9 | 23 | I/O/T | GPIO9 |
| IO18 | 24 | I/O/T | GPIO18, SDIO_CMD, FSPICS2 |
| IO19 | 25 | I/O/T | GPIO19, SDIO_CLK, FSPICS3 |
| IO20 | 26 | I/O/T | GPIO20, SDIO_DATA0, FSPICS4 |
| IO21 | 27 | I/O/T | GPIO21, SDIO_DATA1, FSPICS5 |
| IO22 | 28 | I/O/T | GPIO22, SDIO_DATA2 |
| IO23 | 29 | I/O/T | GPIO23, SDIO_DATA3 |
| RXD0 | 30 | I/O/T | U0RXD, GPIO17, FSPICS1 |
| TXD0 | 31 | I/O/T | U0TXD, GPIO16, FSPICS0 |
| NC | 32–35 | — | NC |

**Type key:** P = Power, I = Input, O = Output, T = High-impedance (tristate)

### Boot / Reset Circuit

| Function | Pin | Recommended implementation |
|----------|-----|---------------------------|
| Reset | EN (pin 8) | 10 kΩ pull-up to 3V3; 100 nF to GND for POR glitch filter |
| Boot mode | IO9 (pin 23) | 10 kΩ pull-up to 3V3. Ground IO9 before asserting then releasing reset to enter download mode. |

**Download mode entry (manual):**
1. Ground IO9 (pulls IO9 low)
2. Assert reset briefly (EN low → EN high)
3. Release IO9 after reset releases

> IO9 is safe high during normal I2C operation if shared with I2C SCL — pull-up holds it HIGH at boot unless IO9-side pad is grounded.

### Project Usage Notes

> **[ESH10000671 R0]:** EN net = MCU_EN; test point TP_RESET on EN node. IO9 shares LP_I2C_SCL (I2C0 SCL). No dedicated test point on IO9; enter download mode by grounding the IO9-side pad of the pull-up resistor.

---

## BQ24075T

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** BQ24075T  
**Package:** WSON-16 (3 mm × 3 mm)  
**Category:** IC — Power / Battery Charger  
**Datasheet:** BQ24072T/BQ24075T/BQ24079T datasheet (Texas Instruments)  
**Added:** 2026-04 (migrated from ESH10000671 R0)  
**Used in:** ESH10000671 R0

Li-Ion battery charger with integrated power path management. System load (OUT) is powered directly from input or battery. OUT regulated to 5.5 V (BQ24075T/79T); SYSOFF pin controls battery-to-OUT FET.

### Pin Description

> Pin numbers below are for BQ24075T. TD (pin 15 on BQ24072T) is not present on BQ24075T; SYSOFF occupies pin 15 instead.

| Name | No. | Type | Description |
|------|-----|------|-------------|
| TS | 1 | I/O | External NTC thermistor input. Connect to center tap of resistor divider from VIN to GND with NTC in parallel with bottom resistor. For applications without TS, set divider to 20% ratio. |
| BAT | 2, 3 | I/O | Charger power stage output and battery voltage sense input. Connect to positive terminal of battery. Bypass to VSS with 4.7–47 µF ceramic capacitor. |
| CE | 4 | I | Charge enable, active-low. High = standby (OUT active, supplement mode available). Low = charging enabled. Internally pulled down ~285 kΩ. Do not leave unconnected. |
| EN2 | 5 | I | Input current limit configuration input. Use with EN1 to control maximum input current. Internally pulled down ~285 kΩ. Do not leave unconnected. |
| EN1 | 6 | I | Input current limit configuration input. See EN2. Internally pulled down ~285 kΩ. Do not leave unconnected. |
| PGOOD | 7 | O | Open-drain power good status output. Pulls to VSS when valid input source detected; high-Z when input out of limits. Connect via 1–100 kΩ pull-up resistor or LED. |
| VSS | 8 | — | Ground. Connect to thermal pad and ground rail of circuit. |
| CHG | 9 | O | Open-drain charging status output. Pulls to VSS when charging; high-Z when complete or disabled; flashes to indicate timer fault. Connect via 1–100 kΩ pull-up resistor or LED. |
| OUT | 10, 11 | O | System supply output. Regulated when input is within operating range. When input is out of range, OUT is connected to VBAT (unless SYSOFF is high). Bypass to VSS with 4.7–47 µF ceramic capacitor. |
| ILIM | 12 | I | Adjustable input current limit programming. Connect 1.07–7.5 kΩ resistor from ILIM to VSS to program maximum input current (EN2=1, EN1=0). Leaving unconnected disables all charging. |
| IN | 13 | I | Input power connection. Operating range 4.35–6.6 V. Accepts up to 26 V without damage but operation suspended above 6.6 V. Bypass to VSS with 1–10 µF ceramic capacitor. |
| TMR | 14 | I | Timer programming input. Connect to VSS to disable all safety timers. Connect 18–72 kΩ resistor to VSS to program timer length. Leave unconnected for default timer values. |
| SYSOFF | 15 | I | System enable input (BQ24075T only). High = FET connecting battery to OUT is off; charging also disabled when adapter present. Low = normal operation. Internally pulled up to VBAT via ~5 MΩ. Do not leave unconnected. |
| ISET | 16 | I/O | Fast charge current programming. Connect 590 Ω–3 kΩ resistor from ISET to VSS. Charging disabled if left unconnected. During charging, voltage on ISET reflects actual charge current (monitoring). |
| Thermal Pad | — | — | Internally connected to VSS. Must be connected to same potential as VSS on PCB. Do not use as primary ground input. |

**Type key:** I = Input, O = Output, I/O = Bidirectional, — = Power/Ground

### Device Variants

| Part | VOVP | VBAT(REG) | VOUT(REG) | VDPPM | Pin 15 |
|------|------|-----------|-----------|-------|--------|
| BQ24072T | 6.6 V | 4.2 V | VBAT + 225 mV | VOREG − 100 mV | TD (termination disable) |
| **BQ24075T** | **6.6 V** | **4.2 V** | **5.5 V** | **4.3 V** | **SYSOFF** |
| BQ24079T | 6.6 V | 4.1 V | 5.5 V | 4.3 V | SYSOFF |

### EN1 / EN2 Input Current Modes

| EN2 | EN1 | Maximum input current into IN |
|-----|-----|-------------------------------|
| 0 | 0 | 100 mA — USB100 mode |
| 0 | 1 | 500 mA — USB500 mode |
| 1 | 0 | Set by external RILIM resistor |
| 1 | 1 | Standby (USB suspend mode) |

### Key Electrical Parameters (BQ24075T)

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| IN operating voltage | 4.35 | — | 6.4 | V | Withstands up to 26 V without damage |
| Input OVP threshold (VOVP) | 6.4 | 6.6 | 6.8 | V | — |
| UVLO threshold | 3.2 | 3.3 | 3.4 | V | — |
| OUT regulation voltage | 5.4 | 5.5 | 5.6 | V | Fixed; BQ24075T/79T only |
| Battery charge voltage VBAT(REG) | 4.16 | 4.20 | 4.24 | V | — |
| DPPM threshold VDPPM | 4.2 | 4.3 | 4.4 | V | OUT voltage where charge current reduces |
| Pre-charge → fast-charge threshold | 2.9 | 3.0 | 3.1 | V | — |
| Max charge current ICHG | 300 | — | 1500 | mA | Set by RISET |
| Charge current factor KISET | 797 | 890 | 975 | AΩ | ICHG = KISET / RISET |
| Max input current factor KILIM | 1330 | 1600 | 1700 | AΩ | IIN-MAX = KILIM / RILIM |
| USB100 input current limit | 90 | 95 | 100 | mA | EN2=0, EN1=0 |
| USB500 input current limit | 450 | 475 | 500 | mA | EN2=0, EN1=1 |
| Sleep current into BAT (IBAT(PDWN)) | — | 6.5 | — | µA | No input, no load on OUT |
| Standby current into IN (EN1=EN2=1) | — | 50 | — | µA | VIN ≤ 6 V |
| Thermal regulation temperature TJ(REG) | — | 125 | — | °C | Charge current auto-reduces |
| Thermal shutdown TJ(OFF) | — | 155 | — | °C | — |

### Programming Formulas

| Parameter | Formula | Factor | Valid range |
|-----------|---------|--------|-------------|
| Fast charge current | ICHG = KISET / RISET | KISET = 890 AΩ (typ) | 590 Ω – 3 kΩ |
| Input current limit | IIN-MAX = KILIM / RILIM | KILIM = 1600 AΩ (typ) | 1.07 kΩ – 7.5 kΩ |
| Charge timer (fast) | tMAXCHG = 10 × KTMR × RTMR | KTMR = 45 s/kΩ (typ) | 18 kΩ – 72 kΩ |
| Charge current monitor | VISET = ICHARGE / 400 × RISET | — | Read voltage on ISET pin during charge |

### Status Indicator Behaviour

**PGOOD (open-drain, active-low):**

| Input condition | PGOOD |
|----------------|-------|
| VIN < UVLO | Hi-Z |
| UVLO < VIN < VIN(DT) | Hi-Z |
| VIN(DT) < VIN < VOVP | Low (valid input) |
| VIN > VOVP | Hi-Z |

**CHG (open-drain, active-low):**

| Charge state | CHG |
|-------------|-----|
| Charging (first cycle after power-on or CE toggle) | Low |
| Charging suspended by thermal or DPPM loop | Low |
| Safety timer expired — fault | Flashing ~2 Hz |
| Charging done | Hi-Z |
| Recharging after termination | Low |
| Charger disabled or no valid input | Hi-Z |
| Battery absent | Hi-Z |

> Connect CHG and PGOOD to logic rail via 1–100 kΩ pull-up, or directly to LED in series with 1.5 kΩ resistor.

### Layout Notes

- Place decoupling capacitors on IN and OUT as close as possible to the IC with short traces to GND (thermal pad)
- Keep low-current GND paths separate from high-current charge/discharge paths; single-point ground technique
- IN and OUT traces must be sized for max charge current (up to 1.5 A)
- Thermal pad is the primary ground connection — solder to PCB ground; add thermal vias under pad
- IN bypass: 1–10 µF ceramic; BAT bypass: 4.7–47 µF ceramic; OUT bypass: 4.7–47 µF ceramic
- If TS function not used: set resistor divider to hold TS at valid level (R6 = 200 kΩ, R7 = 49.9 kΩ)

### Project Usage Notes

> **[ESH10000671 R0]:** ICHG ≈ 593 mA → RISET = 1.5 kΩ (BOM consolidation with RILIM; within valid range 590 Ω–3 kΩ).

---

## ADS7828

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** ADS7828 (SOIC-16 or QSOP-16)  
**Package:** SOIC-16 / QSOP-16  
**Category:** IC — Analog / ADC  
**Datasheet:** ADS7828 datasheet (Texas Instruments)  
**Added:** 2026-04 (migrated from ESH10000671 R0)  
**Used in:** ESH10000671 R0

12-bit, 8-channel ADC with I2C interface. Supports single-ended and differential input modes. External or internal 2.5 V reference. No ALERT/BUSY output pin (confirmed 2026-04-10).

### Key Features

- 12-bit resolution, 8 channels
- 2 address pins (A0, A1) → addresses 0x48–0x4B
- Single-ended or differential input modes
- External or internal 2.5 V reference (VREF pin)
- VDD supply range: 2.7 V to 5.5 V

### Functional Signals

| Signal | Type | Description |
|--------|------|-------------|
| VDD | P | Supply. Bypass with 100 nF to GND. |
| GND | P | Ground |
| VREF | I | Reference voltage. Tie to VDD for full-scale = VDD. |
| SDA | I/O | I2C data, open-drain |
| SCL | I | I2C clock |
| A0 | I | I2C address bit 0. GND = 0; VCC = 1 |
| A1 | I | I2C address bit 1. GND = 0; VCC = 1 |
| COM | I | Differential input common. Tie to GND for single-ended operation. |
| CH0–CH7 | I | Analog input channels |

### I2C Address Table

| A1 | A0 | Address |
|----|----|---------|
| 0 | 0 | 0x48 |
| 0 | 1 | 0x49 |
| 1 | 0 | 0x4A |
| 1 | 1 | 0x4B |

### Project Usage Notes

> **[ESH10000671 R0]:** A0=A1=GND → address 0x48. VREF connected to REF3425 output (2.5 V precision reference) → full-scale = 2.5 V, 1 LSB = 0.610 mV. CH0: VBAT resistor divider midpoint (2×1 MΩ; VCH0_max = 2.1 V at VBAT=4.2 V). CH1: INA333 output centred at 1.25 V = 0 A. CH2–CH7: NC (spare).

---

## MCP1700

**Manufacturer:** Microchip Technology  
**Mfr Part Number:** MCP1700T-3302E/TT (SOT-23, 3.3 V); other voltages and packages available — see variant table  
**Package:** SOT-23, SOT-89, TO-92, 2×2 DFN-6  
**Category:** IC — Power / LDO  
**Datasheet:** DS20001826E — MCP1700 Low Quiescent Current LDO (Microchip Technology, 2018)  
**Added:** 2026-04 (migrated from ESH10000671 R0)  
**Used in:** ESH10000671 R0

Ultra-low quiescent current (1.6 µA typ) LDO voltage regulator. 250 mA max output current. Output voltage set by part number suffix.

### Pin Description

| Name | SOT-23 No. | SOT-89 No. | TO-92 No. | DFN-6 No. | Function |
|------|-----------|-----------|----------|----------|----------|
| GND | 1 | 1 | 1 | 3 | Ground. Bias current only (typ 1.6 µA). No high-current path. Minimise voltage drop between GND pin and negative side of load. |
| VOUT | 2 | 3 | 3 | 6 | Regulated voltage output. Place COUT as close as possible to this pin. |
| VIN | 3 | 2 | 2 | 1 | Unregulated supply input. Bypass with 1 µF ceramic. Source impedance must be low (< 10 Ω) for stability. |
| NC | — | — | — | 2, 4, 5 | No internal connection. True no-connect. |
| EP | — | — | — | 7 | Exposed Thermal Pad. Internally connected to GND. Must be connected to GND on PCB. |

### Device Variants (3.3 V)

| Part Number | Package | VOUT | Notes |
|-------------|---------|------|-------|
| MCP1700T-3302E/TT | SOT-23 | 3.3 V | Standard SMD; θJA = 212°C/W |
| MCP1700T-3302E/MB | SOT-89 | 3.3 V | Better thermal margin; θJA = 104°C/W |
| MCP1700T-3302E/MAY | 2×2 DFN-6 | 3.3 V | Best thermal; θJA = 91°C/W; EP to GND required |
| MCP1700-3302E/TO | TO-92 | 3.3 V | Through-hole; θJA = 92°C/W |

> Other output voltages available: 1.2V, 1.8V, 2.5V, 2.8V, 2.9V, 3.0V, 5.0V (voltage code in part number varies).

### Key Electrical Parameters

Conditions unless stated: VIN = VR + 1V, ILOAD = 100 µA, COUT = 1 µF X7R, CIN = 1 µF X7R, TA = +25°C.

| Parameter | Sym. | Min | Typ | Max | Unit | Conditions |
|-----------|------|-----|-----|-----|------|------------|
| Input operating voltage | VIN | 2.3 | — | 6.0 | V | VIN ≥ 2.3V and VIN ≥ VR + VDROPOUT + VR×3% |
| Quiescent current | Iq | — | 1.6 | 4.0 | µA | IL = 0 mA |
| Max output current (VR ≥ 2.5V) | IOUT | — | — | 250 | mA | — |
| Max output current (VR < 2.5V) | IOUT | — | — | 200 | mA | — |
| Output voltage accuracy (25°C) | VOUT | −2% | ±0.4% | +2% | — | — |
| Output voltage accuracy (over temp) | VOUT | −3% | — | +3% | — | TJ = −40°C to +125°C |
| Output voltage temp coefficient | TCVOUT | — | 50 | — | ppm/°C | — |
| Line regulation | — | −1.0 | ±0.75 | +1.0 | %/V | VIN from (VR+1)V to 6V |
| Load regulation | — | −1.5 | ±1.0 | +1.5 | % | IL = 0.1 mA to 250 mA (VR ≥ 2.5V) |
| Dropout voltage (VR ≥ 2.5V) | VDO | — | 178 | 350 | mV | IL = 250 mA |
| Dropout voltage (VR < 2.5V) | VDO | — | 150 | 350 | mV | IL = 200 mA |
| Output noise | eN | — | 3 | — | µV/√Hz | IL = 100 mA, f = 1 kHz, COUT = 1 µF |
| PSRR | PSRR | — | 44 | — | dB | f = 100 Hz, COUT = 1 µF, IL = 50 mA |
| Thermal shutdown threshold | TSD | — | 140 | — | °C | — |
| Output rise time | TR | — | 500 | — | µs | 10% to 90% of VR |
| Operating junction temperature | TJ | −40 | — | +125 | °C | — |
| Absolute max junction temperature | — | — | — | 150 | °C | — |

### Thermal Data

| Package | θJA (°C/W) | PD(MAX) at TA = 25°C | PD(MAX) at TA = 85°C |
|---------|-----------|----------------------|----------------------|
| 2×2 DFN-6 | 91 | 1099 mW | 440 mW |
| SOT-23 | 212 | 472 mW | 189 mW |
| SOT-89 | 104 | 962 mW | 385 mW |
| TO-92 | 92 | 1087 mW | 435 mW |

> PD(MAX) = (125°C − TA) / θJA

### Power Dissipation Formulas

| Parameter | Formula |
|-----------|---------|
| Internal power dissipation | PLDO = (VIN(MAX) − VOUT(MIN)) × IOUT(MAX) |
| Junction temperature | TJ = PLDO × θJA + TA |
| Max allowable package dissipation | PD(MAX) = (125°C − TA(MAX)) / θJA |

### Layout Notes

- CIN = 1 µF ceramic (X7R); COUT = 1 µF ceramic (X7R) minimum — both required for stability
- COUT must be placed as close as possible to VOUT pin; minimise trace inductance
- CIN and COUT ESR range: 0–2 Ω (ceramic, tantalum, or aluminium electrolytic all acceptable)
- GND pin is low-current only — no high-current ground return; minimise resistance between GND pin and load return
- For DFN: EP internally connected to GND — tie EP to PCB ground; add thermal vias if IOUT > 100 mA
- VIN source impedance must be low (< 10 Ω) for stability — CIN directly at VIN pin

### Project Usage Notes

> **[ESH10000671 R0]:** VIN from BQ24075 OUT: 3.7 V (battery, low) → 5.5 V (VBUS). VOUT = 3.3 V; VDO(max) = 350 mV → minimum VIN for regulation at full load = 3.65 V. Risk: at low battery (< 3.65 V), VOUT droops — system should monitor VBAT and shut down before dropout. Worst-case dissipation (VBUS input, IOUT = 200 mA): (5.5 − 3.3) × 0.2 = 440 mW → SOT-23 at thermal limit for TA > 83°C; prefer SOT-89 or DFN for thermal margin.

---

## SX1276

**Manufacturer:** Semtech Corporation  
**Mfr Part Number:** SX1276 (137–1020 MHz; SX1277/78/79 are restricted frequency variants)  
**Package:** QFN-28 (thermal/ground pad on underside)  
**Category:** IC — RF / LoRa Transceiver  
**Datasheet:** SX1276/77/78/79 Datasheet Rev. 6, January 2019 (Semtech)  
**Added:** 2026-04 (migrated from ESH10000671 R0)  
**Used in:** ESH10000671 R0

LoRa spread spectrum transceiver. SF 6–12, BW 7.8–500 kHz, up to −148 dBm sensitivity. Full frequency range (SX1276): 137–1020 MHz. PA_BOOST up to +20 dBm (duty cycle limited). RFO_HF up to +14 dBm. Sleep current 0.2 µA typ.

### Pin Description

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 0 (EP) | GND | — | Exposed ground pad (underside); must be soldered to PCB GND |
| 1 | RFI_LF | I | RF receive input, Band 2 & 3 (≤525 MHz). Tie to GND when using Band 1 only |
| 2 | VR_ANA | — | Regulated supply for analogue blocks (internal LDO output). Bypass with 100 nF to GND only — no DC load |
| 3 | VBAT_ANA | — | Supply input for analogue blocks. Connect to 3V3; bypass 100 nF + 10 µF to GND |
| 4 | VR_DIG | — | Regulated supply for digital blocks (internal LDO output). Bypass with 100 nF to GND only |
| 5 | XTA | I/O | Crystal oscillator pin A. Connect 32 MHz crystal + load capacitor to GND |
| 6 | XTB | I/O | Crystal oscillator pin B. Connect 32 MHz crystal + load capacitor to GND. NC if TCXO used |
| 7 | NRESET | I/O | Active-low reset. Assert LOW ≥100 µs, then release; wait 5 ms before SPI. Leave floating during POR |
| 8 | DIO0 | I/O | Digital I/O, software configured (see DIO mapping table) |
| 9 | DIO1/DCLK | I/O | Digital I/O, software configured |
| 10 | DIO2/DATA | I/O | Digital I/O, software configured |
| 11 | DIO3 | I/O | Digital I/O, software configured |
| 12 | DIO4 | I/O | Digital I/O, software configured |
| 13 | DIO5 | I/O | Digital I/O, software configured (CLKOUT output by default at power-on) |
| 14 | VBAT_DIG | — | Supply input for digital blocks. Connect to 3V3; bypass 100 nF + 10 µF to GND |
| 15 | GND | — | Ground |
| 16 | SCK | I | SPI clock input |
| 17 | MISO | O | SPI data output (high-Z when NSS = HIGH) |
| 18 | MOSI | I | SPI data input |
| 19 | NSS | I | SPI chip select, active-low |
| 20 | RXTX/RF_MOD | O | Antenna switch control: HIGH during TX, LOW during RX. Drive external RF switch CTRL directly — no firmware overhead needed |
| 21 | RFI_HF | I | RF receive input, Band 1 (≥862 MHz). LNA input for 868 MHz |
| 22 | RFO_HF | O | RF transmit output, Band 1, up to +14 dBm. Leave floating when PA_BOOST path selected |
| 23 | GND | — | Ground |
| 24 | VBAT_RF | — | Supply input for RF blocks. Connect to 3V3; bypass 100 nF + 4.7 µF to GND; recommend ferrite bead on 3V3 feed to this pin |
| 25 | VR_PA | — | Regulated supply for PA (internal LDO output). Bypass with 10 µF low-ESR to GND only |
| 26 | GND | — | Ground |
| 27 | PA_BOOST | O | High-power PA output, all frequency bands. Up to +20 dBm via external matching network. Leave floating if unused |
| 28 | RFO_LF | O | RF transmit output, Band 2 & 3 (≤525 MHz). Tie to GND when using Band 1 only |

### Power Amplifier Mode Selection

| PaSelect (RegPaConfig[7]) | PA Output | Power Range | Formula |
|---------------------------|-----------|-------------|---------|
| 0 | RFO_HF or RFO_LF | −4 to +14 dBm | Pout = Pmax − (15 − OutputPower); Pmax = 10.8 + 0.6×MaxPower |
| 1 | PA_BOOST | +2 to +17 dBm (+20 dBm high power mode) | Pout = 17 − (15 − OutputPower) |

> **+20 dBm operation:** Set RegPaDac[2:0] = 0x07 (register 0x4D, value 0x87). Duty cycle limited to 1% max. VSWR limit 3:1. VDD min 2.4 V. OcpTrim must be increased to allow adequate supply current.

### DIO Mapping — LoRa Mode (Table 18)

| DIOx Mapping | DIO0 | DIO1 | DIO2 | DIO3 | DIO4 | DIO5 |
|-------------|------|------|------|------|------|------|
| 00 | **RxDone** | RxTimeout | FhssChangeChannel | CadDone | CadDetected | ModeReady |
| 01 | **TxDone** | FhssChangeChannel | FhssChangeChannel | ValidHeader | PllLock | ClkOut |
| 10 | CadDone | CadDetected | FhssChangeChannel | PayloadCrcError | PllLock | ClkOut |
| 11 | — | — | — | — | — | — |

> Firmware typically sets DIO0 mapping to 00 (RxDone) before RX and 01 (TxDone) before TX. Always read RegIrqFlags on interrupt to confirm event and clear flags.

### Crystal Specification (Section 7.1)

| Symbol | Description | Min | Typ | Max | Unit |
|--------|-------------|-----|-----|-----|------|
| FXOSC | Crystal frequency | — | 32 | — | MHz |
| RS | Crystal serial resistance | — | 15 | 100 | Ω |
| C0 | Crystal shunt capacitance | — | 1 | 3 | pF |
| CFOOT | External load capacitor on each XTA, XTB pin | 10 | 15 | 22 | pF |
| CLOAD | Crystal load capacitance | 6 | — | 12 | pF |

> Use crystal with CL = 6–12 pF. Place load caps (10–22 pF, verify against crystal datasheet) on XTA and XTB to GND. For bandwidths < 62.5 kHz a TCXO is recommended for frequency stability.

### Power Consumption Summary

| Mode | Condition | Current |
|------|-----------|---------|
| Sleep | — | 0.2 µA typ, 1 µA max |
| Standby | Crystal oscillator enabled | 1.6 mA typ |
| RX (Band 1, BW 7.8–62.5 kHz) | LnaBoost off | 9.9 mA typ |
| RX (Band 1, BW 125 kHz) | LnaBoost off | 10.3 mA typ |
| TX +20 dBm | PA_BOOST, high power mode | 120 mA typ |
| TX +17 dBm | PA_BOOST | 87 mA typ |
| TX +13 dBm | RFO_HF | 29 mA typ |
| TX +7 dBm | RFO_HF | 20 mA typ |

### SPI Interface

- Protocol: CPOL=0, CPHA=0 (Motorola Mode 0), slave-only
- Max SCK: 10 MHz; NSS min setup to first SCK: 30 ns; NSS hold after last SCK: 100 ns
- Address byte: bit 7 = write (1) / read (0), bits[6:0] = register address
- Modes: single-byte, burst (auto-increment address), and FIFO access
- MISO is high-impedance when NSS = HIGH

### Reset Timing

- Manual reset: assert NRESET LOW for ≥ 100 µs, then release
- After release: wait **5 ms** before issuing any SPI commands
- During reset: VDD current may spike up to 1 mA
- NRESET must be left floating (not driven) during power-on POR sequence

### RF Front-End Topology (Band 1 / 868 MHz)

PA_BOOST path for +17/+20 dBm requires external π-network matching into SPDT antenna switch:

```
PA_BOOST (pin 27) → C_shunt → L_series → C_shunt → RF_switch RF1
RFI_HF (pin 21) ← RF_switch RF2 ← Antenna connector ← RF_switch RFC
RXTX/RF_MOD (pin 20) → RF_switch CTRL  (HIGH = TX, LOW = RX)
```

Topology: PA_BOOST → C1 (shunt to GND) → L1 (series, high-Q, SRF > 2 GHz) → C2 (shunt to GND) → antenna switch RF1.

### Layout Notes

- Place all decoupling capacitors as close as possible to the respective VBAT/VR pins
- 3V3_RF supply island: use ferrite bead from main 3V3 rail; no other loads on this island
- Crystal: place close to XTA/XTB; keep load cap traces short; guard with GND pour
- PA_BOOST trace: 50 Ω controlled impedance from pin 27 to matching network to RF switch
- RFI_HF trace: 50 Ω controlled impedance from RF switch to pin 21; keep short
- RF switch RFC to antenna: 50 Ω controlled impedance
- GND stitching vias under SX1276 and along RF traces
- EP (pin 0) soldered to PCB ground plane; thermal/GND stitching vias under EP

### Project Usage Notes

> **[ESH10000671 R0]:** π-network values: C1 = 10 pF C0G/0402, L1 = 15 nH high-Q/0402 (SRF > 2 GHz), C2 = 10 pF C0G/0402. Antenna switch: PE4259 SPDT (VDD=3V3, CTRL directly from RXTX pin 20). Antenna connector: Würth 60312002114503 edge-mount SMA. 3V3_RF isolated via TDK MPZ2012S102AT000 ferrite bead. Crystal: NDK CS06465-32M. NRESET driven by PI4IOE5V6416ZDEX P10.

---

## MPZ2012S102AT000

**Manufacturer:** TDK Corporation  
**Mfr Part Number:** MPZ2012S102AT000  
**Package:** 0805 (2.0 × 1.25 × 0.85 mm)  
**Series:** MPZ — Power line ferrite bead  
**Category:** Passive — Ferrite Bead  
**Datasheet:** TDK MPZ series datasheet  
**Added:** 2026-04 (migrated from ESH10000671 R0)  
**Used in:** ESH10000671 R0

Power-line ferrite bead for RF supply decoupling. 1 kΩ @ 100 MHz, 1.5 A rated current.

### Electrical Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Impedance @ 100 MHz | 1 kΩ ±25% | Datasheet |
| Rated current | 1.5 A | — |
| DC resistance (max) | 150 mΩ | V-drop ≈ 18 mV at 120 mA |
| Operating temperature | −55 to +125 °C | — |

### Selection Rationale

Compared against Murata BLM18AG331SN1D (0402, 330 Ω @ 100 MHz, 200 mA max, ~1.5 Ω DCR):

- MPZ2012S102AT000: 1 kΩ @ 100 MHz (3× higher filtering), 1.5 A (7.5× more current headroom), 150 mΩ DCR (10× lower)
- BLM18AG331: marginal headroom at 120 mA TX peak; high DCR causes excessive voltage drop
- 0805 footprint is acceptable where routing density is not a constraint

### Project Usage Notes

> **[ESH10000671 R0]:** Used as FB_RF — isolation between main 3V3 rail and SX1276 VBAT_RF (pin 24). No other loads on the 3V3_RF island.

---

## CS06465-32M (NDK NX2016SA)

**Manufacturer:** NDK (Nihon Dempa Kogyo)  
**NDK Spec. No.:** EXS00A-CS06465  
**Mfr Part Number:** CS06465-32M  
**Package:** SMD 2016 — 2.0 × 1.6 × 0.45 mm (4-pad)  
**Category:** Crystal — SMD  
**Datasheet:** EXS11B-10519 A (NDK)  
**Added:** 2026-04 (migrated from ESH10000671 R0)  
**Used in:** ESH10000671 R0

32 MHz fundamental mode SMD crystal. Used as oscillator clock source (e.g. SX1276 XTA/XTB).

### Electrical Specifications

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| Nominal frequency | — | 32.000 | — | MHz | Fundamental mode |
| Frequency tolerance | −10 | — | +10 | ppm | at +25°C |
| Frequency stability | −10 | — | +10 | ppm | −20 to +70°C |
| Frequency stability | −30 | — | +30 | ppm | −40 to +85°C |
| Equivalent series resistance (ESR) | — | 20 | 50 | Ω | — |
| Load capacitance (CL) | — | 10 | — | pF | IEC π-network |
| Shunt capacitance (C0) | — | 0.60 | — | pF | — |
| Motional capacitance (C1) | — | 1.89 | — | fF | — |
| Motional inductance (L1) | — | 13.14 | — | mH | — |
| Drive level | — | — | 100 | µW | — |
| Aging | −3 | — | +3 | ppm | 1 year |
| Operating temperature | −40 | — | +85 | °C | — |
| Recommended oscillation margin | 600 | — | — | Ω | — |

### Pin Configuration

| Pad | Function |
|-----|----------|
| #1 | XTAL terminal A |
| #2 | GND (connected to metal cover) |
| #3 | XTAL terminal B |
| #4 | GND (connected to metal cover) |

### Recommended Land Pattern

| Dimension | Value |
|-----------|-------|
| Pad width | 0.65 mm |
| Pad height | 0.55 mm |
| Overall footprint width | 1.35 mm |
| Overall footprint height | 2.10 mm |

### Layout Notes

- Place as close as possible to oscillator IC XTA/XTB pins
- Keep load cap traces short; route directly to GND
- Guard ring with GND pour recommended
- Do not place ground or signal patterns on PCB top layer underneath the crystal (NDK caution 12-6)
- Conformal coating not permitted — crystal is not hermetically sealed
- Reflow peak: 260 ± 5°C, ≤ 10 s; max 2 reflow passes

### Project Usage Notes

> **[ESH10000671 R0]:** Connected to SX1276 XTA (pin 5) and XTB (pin 6). Load caps: 15 pF C0G on each terminal to GND (C_eff ≈ 9.5 pF, accounting for CL=10 pF and ~2 pF stray capacitance).

---

## A782MS227M1VLAS020

**Manufacturer:** Vishay  
**Mfr Part Number:** A782MS227M1VLAS020  
**Package:** Radial can — 10.30 × 10.30 mm  
**Category:** Passive — Capacitor / Aluminium Electrolytic  
**Datasheet:** Vishay A782MS series datasheet  
**Added:** 2026-04 (migrated from ESH10000671 R0)  
**Used in:** ESH10000671 R0

220 µF / 35 V aluminium electrolytic capacitor for bulk rail decoupling.

### Electrical Specifications

| Parameter | Value |
|-----------|-------|
| Capacitance | 220 µF |
| Tolerance | ±20% |
| Voltage rating | 35 V |

### Project Usage Notes

> **[ESH10000671 R0]:** Used as 3V3 rail bulk decoupling capacitor. Place close to the MCU module rather than near LDO output. Orient polarity per silkscreen; verify footprint polarity before layout sign-off.

---

## SRP7028AA Series

**Manufacturer:** Bourns  
**Mfr Part Number:** SRP7028AA-[value code] (e.g., SRP7028AA-1R0M for 1.0 µH)  
**Package:** SMD — 7.1×6.4 mm body, 2.8 mm max height  
**Category:** Passive — Inductor / Power Inductor  
**Datasheet:** Bourns SRP7028AA Series  
**Added:** 2026-04  
**Used in:** —

Shielded SMD power inductor series with metal alloy powder core. Intended for DC–DC converter applications. AEC-Q200 qualified. Inductance range 0.15–22 µH.

### Key Specifications

| Parameter | Value |
|-----------|-------|
| Inductance range | 0.15–22 µH |
| Tolerance | ±20% (Y = ±30% for R15) |
| Core material | Metal alloy powder |
| Max operating temp | −55 to +155°C (incl. temp rise) |
| Irms definition | ΔT = 40°C temperature rise |
| Isat definition | 30% inductance drop |
| Measurement frequency | 100 kHz / 1 V |
| Compliance | AEC-Q200, RoHS, Halogen-Free |
| MSL | 1 |
| Reel quantity | 1,000 pcs / 13-inch reel |

### Electrical Specifications

| Part Number | L (µH) | Tol | DCR Typ (mΩ) | DCR Max (mΩ) | Irms (A) | Isat (A) | SRF (MHz) |
|-------------|--------|-----|--------------|--------------|----------|----------|-----------|
| SRP7028AA-R15Y | 0.15 | ±30% | 1.7 | 2.1 | 30 | 40 | 8 |
| SRP7028AA-R22M | 0.22 | ±20% | 2.0 | 2.5 | 23 | 34 | 8 |
| SRP7028AA-R33M | 0.33 | ±20% | 2.8 | 3.4 | 21 | 25 | 8 |
| SRP7028AA-R36M | 0.36 | ±20% | 3.3 | 3.9 | 20 | 24 | 8 |
| SRP7028AA-R47M | 0.47 | ±20% | 3.4 | 4.0 | 18 | 20 | 8 |
| SRP7028AA-R56M | 0.56 | ±20% | 3.9 | 4.5 | 16.5 | 18 | 10 |
| SRP7028AA-R68M | 0.68 | ±20% | 4.7 | 5.3 | 16 | 17 | 10 |
| SRP7028AA-R82M | 0.82 | ±20% | 5.4 | 6.0 | 14 | 16 | 10 |
| SRP7028AA-1R0M | 1.0 | ±20% | 6.7 | 7.4 | 12 | 15 | 10 |
| SRP7028AA-1R2M | 1.2 | ±20% | 7.7 | 9.5 | 10 | 14 | 10 |
| SRP7028AA-1R5M | 1.5 | ±20% | 10.2 | 12.1 | 10 | 14 | 10 |
| SRP7028AA-2R2M | 2.2 | ±20% | 13.5 | 15.0 | 8 | 10 | 10 |
| SRP7028AA-2R7M | 2.7 | ±20% | 17.3 | 20.0 | 7.2 | 9.8 | 10 |
| SRP7028AA-3R3M | 3.3 | ±20% | 19.0 | 22.0 | 6.5 | 9.5 | 10 |
| SRP7028AA-4R7M | 4.7 | ±20% | 28.0 | 33.0 | 5.5 | 6.5 | 10 |
| SRP7028AA-5R6M | 5.6 | ±20% | 39.0 | 42.0 | 5.5 | 6.0 | 10 |
| SRP7028AA-6R8M | 6.8 | ±20% | 43.0 | 50.0 | 4.5 | 6.0 | 10 |
| SRP7028AA-8R2M | 8.2 | ±20% | 54.0 | 60.0 | 4.5 | 6.0 | 10 |
| SRP7028AA-100M | 10.0 | ±20% | 62.0 | 68.0 | 4.0 | 5.5 | 10 |
| SRP7028AA-150M | 15.0 | ±20% | 110.0 | 140.0 | 3.0 | 4.5 | 10 |
| SRP7028AA-220M | 22.0 | ±20% | 150.0 | 190.0 | 2.5 | 3.0 | 10 |

### Physical / Mechanical

| Dimension | Value (mm) |
|-----------|------------|
| Body length (L) | 7.1 ± 0.3 |
| Body width (W) | 6.4 ± 0.3 |
| Height (H) | 2.8 ± 0.2 |
| Terminal width | 3.0 ± 0.2 |
| Terminal standoff | 0 to 0.15 |
| Termination | Sn |

**Reflow profile:**

| Stage | Condition |
|-------|-----------|
| Pre-heating | 60–150 s |
| Soldering | 60–180 s |
| Peak temperature (TP) | 260°C / max 10 s |
| Alternate peak (tp) | 245°C / 20–40 s |
| Max reflows | 3 |
| Natural cooling | 480 s max |

### Project Usage Notes

No project-specific notes yet.

---

## XRCGB32M000F3M00R0

**Manufacturer:** Murata Manufacturing Co., Ltd.  
**Mfr Part Number:** XRCGB32M000F3M00R0  
**Package:** 3-pad SMD — 2.0×1.6×0.65 mm (alumina substrate, metal cap cover)  
**Category:** Passive — Crystal / Timing  
**Datasheet:** Murata spec JGC49-2767B (Oct 2018)  
**Added:** 2026-04  
**Used in:** —

32.000 MHz SMD crystal in 2016 package. Metal cap construction on alumina substrate. Pin 1 and Pin 3 are crystal terminals; Pin 2 is NC / cover GND. Load capacitance CL = 6.0 pF.

### Electrical Specifications

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Nominal frequency | — | 32.0000 | MHz |
| Frequency tolerance (initial, 25°C) | — | ±30 | ppm max |
| Frequency vs temperature (−30 to +85°C) | — | ±40 | ppm max |
| Aging | — | ±5 | ppm/year max |
| Equivalent series resistance | ESR | ≤100 | Ω |
| Load capacitance | CL | 6.0 ± 0.1 | pF |
| Insulation resistance (DC 10 V) | — | ≥500 | MΩ |
| Drive level (typical) | — | 150 | µW |
| Drive level (maximum) | — | 300 | µW |
| Max DC voltage | — | ≤6 | V |
| Max AC voltage | — | ≤15 | Vp-p |
| Withstanding voltage | — | 100 V DC / ≤5 s | — |
| Operating temperature | — | −30 to +85 | °C |
| Storage temperature | — | −55 to +85 | °C |

### Pin Description

| Pin | Function |
|-----|----------|
| 1 | Crystal terminal (input/output) |
| 2 | No connect (NC) / Cover GND |
| 3 | Crystal terminal (input/output) |

### Physical / Mechanical

| Dimension | Value (mm) |
|-----------|------------|
| Length | 2.0 ± 0.1 |
| Width | 1.6 ± 0.1 |
| Height | 0.65 ± 0.05 |
| Construction | Alumina substrate, metal cap cover |

### Project Usage Notes

No project-specific notes yet.

---

## INA333

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** INA333  
**Package:** 8-pin VSSOP (DGK) / 8-pin WSON (DRG)  
**Category:** IC — Analog / Instrumentation Amplifier  
**Datasheet:** TI SBOS445C (July 2008, Rev. December 2015)  
**Added:** 2026-04  
**Used in:** —

Zero-drift, single-supply instrumentation amplifier. Gain set by a single external resistor (G = 1–1000). Ultra-low quiescent current (50 µA typ) for battery-powered sensor conditioning. Rail-to-rail output.

### Formulas

**Gain setting:**
```
G = 1 + (100 kΩ / RG)
```

| G | RG |
|---|----|
| 1 | Open |
| 10 | 11.1 kΩ |
| 100 | 1.01 kΩ |
| 1000 | 100.1 Ω |

**Total input offset voltage (RTI):**
```
VOSI_total = VOSI + VOSO / G
```

### Electrical Specifications

(VS = 1.8–5.5 V, TA = 25°C, RL = 10 kΩ, VREF = VS/2, G = 1 unless noted)

#### Input Offset and Drift

| Parameter | Min | Typ | Max | Unit |
|-----------|-----|-----|-----|------|
| Offset voltage RTI (G = 1) | — | ±10 | ±25 | µV |
| Offset voltage (G ≥ 10) | — | ±10 ± 25/G | ±25 ± 75/G | µV |
| Offset drift vs temperature | — | ±0.1 ± 0.5/G | — | µV/°C |
| Offset drift vs supply | — | ±1 ± 5/G | ±5 ± 15/G | µV/V |

#### Input Bias and Noise

| Parameter | Typ | Max | Unit |
|-----------|-----|-----|------|
| Input bias current (IB) | ±70 | ±200 | pA |
| Input offset current (IOS) | ±50 | ±200 | pA |
| Voltage noise (G = 100, 10 Hz–1 kHz) | 50 | — | nV/√Hz |
| Voltage noise (0.1–10 Hz) | 1 | — | µVpp |
| Current noise (10 Hz) | 100 | — | fA/√Hz |

#### CMRR

| Gain | Min | Typ | Unit |
|------|-----|-----|------|
| G = 1 (DC to 60 Hz) | 80 | 90 | dB |
| G ≥ 10 (DC to 60 Hz) | 100 | 110–115 | dB |

#### Gain Error

| Gain | Typ | Max | Unit |
|------|-----|-----|------|
| G = 1 | ±0.01% | ±0.1% | — |
| G = 10 | ±0.05% | ±0.25% | — |
| G = 100 | ±0.07% | ±0.25% | — |
| G = 1000 | ±0.25% | ±0.5% | — |

Gain TC (G = 1): ±1 typ / ±5 max ppm/°C; (G > 1): ±15 typ / ±50 max ppm/°C.

#### Frequency Response

| G | Bandwidth −3 dB | Slew Rate |
|---|-----------------|-----------|
| 1 | 150 kHz | 0.16 V/µs |
| 10 | 35 kHz | — |
| 100 | 3.5 kHz | 0.05 V/µs |
| 1000 | 350 Hz | — |

#### Power Supply

| Parameter | Min | Typ | Max | Unit |
|-----------|-----|-----|-----|------|
| Supply voltage (single) | +1.8 | — | +5.5 | V |
| Supply voltage (dual) | ±0.9 | — | ±2.75 | V |
| Quiescent current (IQ) | — | 50 | 75 | µA |
| IQ vs temperature | — | — | 80 | µA |
| Operating temp range | −40 | — | +125 | °C |

#### Thermal Resistance

| Metric | DGK (VSSOP) | DRG (WSON) | Unit |
|--------|-------------|------------|------|
| RθJA | 169.5 | 60 | °C/W |
| RθJC (top) | 62.7 | 60 | °C/W |
| RθJB | 90.3 | 50 | °C/W |
| RθJC (bottom) | — | 6 | °C/W |

### Pin Description

(DGK 8-pin VSSOP — DRG WSON is pin-compatible)

| Pin | Name | Function |
|-----|------|----------|
| 1 | RG | Gain resistor terminal (−) |
| 2 | IN− | Inverting input |
| 3 | IN+ | Non-inverting input |
| 4 | V− | Negative supply |
| 5 | REF | Reference input (output offset) |
| 6 | OUT | Amplifier output |
| 7 | V+ | Positive supply |
| 8 | RG | Gain resistor terminal (+) |

### Project Usage Notes

No project-specific notes yet.

---

## ESP32-S3

**Manufacturer:** Espressif Systems  
**Mfr Part Number:** ESP32-S3 (series — see variant table)  
**Package:** QFN56 7×7 mm (56 castellated pads + 1 GND exposed pad)  
**Category:** IC — MCU / SoC / Wireless  
**Datasheet:** ESP32-S3 Series Datasheet v2.2 (Espressif)  
**Added:** 2026-04  
**Used in:** —

> **Note:** This entry covers the bare chip (QFN56). Contrast with [ESP32-C6-MINI-1](#esp32-c6-mini-1) which is a module. In-package flash/PSRAM variants available — see variant table.

Dual-core Xtensa® LX7 @ up to 240 MHz with 2.4 GHz Wi-Fi 4 (802.11b/g/n) and Bluetooth 5 LE. Adds AI/DSP extended instruction set (PIE), USB OTG FS, 45 GPIOs. 512 KB SRAM + 384 KB ROM on-chip.

### Variant Comparison

| Part Number | Flash | PSRAM | Max TA | VDD_SPI |
|-------------|-------|-------|--------|---------|
| ESP32-S3 | — | — | 105°C | 3.3 V / 1.8 V |
| ESP32-S3FN8 | 8 MB Quad | — | 85°C | 3.3 V |
| ESP32-S3RH2 | — | 2 MB Quad | 105°C | 3.3 V |
| ESP32-S3R8 | — | 8 MB Octal | 65°C | 3.3 V |
| ESP32-S3R16V | — | 16 MB Octal | 65°C | 1.8 V |
| ESP32-S3FH4R2 | 4 MB Quad | 2 MB Quad | 85°C | 3.3 V |

### Key Specifications

| Feature | Value |
|---------|-------|
| CPU | Dual-core Xtensa® LX7 |
| Clock frequency | Up to 240 MHz |
| SRAM (on-chip) | 512 KB |
| ROM | 384 KB |
| RTC fast SRAM | 8 KB |
| Wi-Fi | 802.11b/g/n 2.4 GHz, WPA3 |
| Bluetooth | BT5 LE (1/2 Mbps, 125/500 Kbps) |
| GPIOs | 45 |
| ADC | 2× SAR 12-bit, up to 20 ch, 100 kSPS |
| USB | USB 2.0 OTG FS + USB Serial/JTAG |
| UART / SPI / I2C / I2S | 3× / 4× / 2× / 2× |
| Touch sensor | 14 channels |
| ULP coprocessors | ULP-RISC-V + ULP-FSM |
| Security | AES, SHA, RSA, Secure Boot, Flash Enc. |
| Deep-sleep current | ~7 µA (typ) |
| Package | QFN56 7×7 mm |

### Electrical Specifications

#### Absolute Maximum Ratings

| Parameter | Min | Max | Unit |
|-----------|-----|-----|------|
| VDDA, VDD3P3, VDD3P3_RTC, VDD3P3_CPU | −0.3 | 3.6 | V |
| Cumulative IO output current | — | 1500 | mA |
| Storage temperature | −40 | 150 | °C |

#### Recommended Operating Conditions

| Parameter | Min | Typ | Max | Unit |
|-----------|-----|-----|-----|------|
| VDDA, VDD3P3 | 3.0 | 3.3 | 3.6 | V |
| VDD3P3_RTC | 3.0 | 3.3 | 3.6 | V |
| VDD3P3_CPU | 3.0 | 3.3 | 3.6 | V |
| VDD_SPI (as input) | 1.8 | — | 3.6 | V |

#### DC Characteristics (3.3 V, 25°C)

| Parameter | Min | Typ | Max | Unit |
|-----------|-----|-----|-----|------|
| VIH | 0.75 × VDD | — | VDD + 0.3 | V |
| VIL | −0.3 | — | 0.25 × VDD | V |
| IOH (PAD_DRIVER = 3) | — | 40 | — | mA |
| IOL (PAD_DRIVER = 3) | — | 28 | — | mA |
| Weak pull-up / pull-down | — | 45 | — | kΩ |

#### ADC Characteristics

| Parameter | Min | Max | Unit |
|-----------|-----|-----|------|
| Resolution | — | 12 | bit |
| DNL | −4 | +4 | LSB |
| INL | −8 | +8 | LSB |
| Sampling rate | — | 100 | kSPS |
| Input range (ATTEN0) | 0 | 850 | mV |
| Input range (ATTEN3) | 0 | 2900 | mV |

#### Current Consumption (3.3 V, 25°C)

| Mode | Condition | Current |
|------|-----------|---------|
| Wi-Fi TX | 802.11b 1 Mbps @ 21 dBm, peak | 340 mA |
| Deep sleep | — | ~7 µA |

### Boot Configuration (Strapping Pins)

| GPIO | Default | Function |
|------|---------|----------|
| GPIO0 | Weak pull-up | 1 = SPI Boot; 0 = Download Boot |
| GPIO46 | Weak pull-down | 0 = enable ROM serial print |
| GPIO45 | Weak pull-down | VDD_SPI voltage sel (0 = 3.3 V) |
| GPIO3 | Floating | JTAG source selection |

> **Boot mode:** GPIO0=1 → SPI Boot (normal). GPIO0=0 + GPIO46=0 → Download Boot (UART/USB).

### Pin Overview

The ESP32-S3 has 56 pins (QFN56):
- **IO (GPIO0–GPIO46):** 45 GPIOs; most support IO MUX, RTC IO MUX, and analog functions
- **Power:** VDDA, VDD3P3 ×2, VDD3P3_RTC, VDD3P3_CPU, VDD_SPI, GND
- **RF:** LNA_IN (antenna input)
- **Crystal:** XTAL_P / XTAL_N (40 MHz ext.); XTAL_32K_P / _N (opt. 32 kHz)
- **Reset:** CHIP_PU (active high)
- **SPI flash/PSRAM:** SPICS0(32), SPICLK(33), SPIQ(34), SPID(35), SPIWP(31), SPIHD(30), SPICS1(28), VDD_SPI(29)

### Project Usage Notes

No project-specific notes yet.

---

## WM8962B

**Manufacturer:** Cirrus Logic (formerly Wolfson Microelectronics)  
**Mfr Part Number:** WM8962B / WM8962BECSN/R  
**Package:** 49-ball W-CSP — 3.6×3.9 mm (7×7 array, 0.5 mm pitch)  
**Category:** IC — Audio / CODEC  
**Datasheet:** WM8962B Product Datasheet Rev 4.3 (Cirrus Logic)  
**Added:** 2026-04  
**Used in:** —

Ultra-low power stereo audio CODEC with Class D speaker amplifier and Class-W headphone driver. Features ALC, DRC, 5-band EQ, 3D surround processing. I2C or SPI control interface. Intended for battery-powered portable audio applications.

### Key Specifications

| Feature | Value |
|---------|-------|
| ADC SNR | 91–94 dB (A-weighted, high-performance mode) |
| DAC SNR | 87–98 dB (A-weighted, high-performance mode) |
| HP output power | 26 mW @ 32 Ω (LP mode); 31 mW @ 16 Ω |
| Speaker (stereo, 8 Ω) | 1.26 W @ 1% THD+N (SPKVDD = 5.5 V) |
| Speaker (stereo, 4 Ω) | 1.75 W @ 1% THD+N (SPKVDD = 5 V) |
| Speaker (mono, 4 Ω) | 2.45 W @ 1% THD+N (SPKVDD = 5.5 V) |
| Control interface | I2C (2-wire) or SPI (3/4-wire), selected via CIFMODE |
| Audio interface | I2S (master/slave), TDM — BCLK, LRCLK, DACDAT, ADCDAT |
| Sample rates | 8–48 kHz |
| Temperature range | −40 to +85°C |
| Package | 49-ball W-CSP 3.6×3.9 mm |
| MSL | 1 |
| Peak solder temp | 260°C |

### Electrical Specifications

#### Absolute Maximum Ratings

| Rail | Max |
|------|-----|
| DCVDD, AVDD, PLLVDD | +2.5 V |
| MICVDD, DBVDD | +4.5 V |
| SPKVDD1, SPKVDD2 | +7.0 V |
| CPVDD | +2.2 V |
| HP outputs (HPOUTL/R) | ±(CPVDD + 0.3) V |
| TJ | +150°C |

#### Recommended Operating Conditions

| Symbol | Min | Typ | Max | Unit |
|--------|-----|-----|-----|------|
| DCVDD | 1.62 | 1.8 | 2.0 | V |
| DBVDD | 1.62 | 1.8 | 3.6 | V |
| AVDD | 1.7 | 1.8 | 2.0 | V |
| PLLVDD | 1.7 | 1.8 | 2.0 | V |
| CPVDD | 1.7 | 1.8 | 2.0 | V |
| MICVDD | 1.7 | 2.5 | 3.6 | V |
| SPKVDD1, SPKVDD2 | 1.7 | 5.0 | 5.5 | V |
| TA | −40 | — | +85 | °C |

### Pin Description (49-ball W-CSP)

| Ball | Name | Type | Description |
|------|------|------|-------------|
| G7 | MCLK/XTI | Digital In | Master clock input / crystal input |
| F7 | XTO | Analogue Out | Crystal output |
| G6 | CLKOUT5 | Analogue Out | FLL / oscillator clock output |
| E4 | CLKOUT2/GPIO2 | Digital Out | PLL2 clock output / GPIO |
| F4 | CLKOUT3/GPIO3 | Digital Out | PLL3/FLL clock output / GPIO |
| G2 | DCVDD | Supply | Digital core supply |
| G3 | DBVDD | Supply | Digital buffer supply |
| G4 | PLLVDD | Supply | PLL supply |
| G5 | PLLGND | Ground | PLL ground |
| F3 | DGND | Ground | Digital ground |
| D6 | AVDD | Supply | Analogue supply |
| D7 | AGND | Ground | Analogue ground |
| C6 | CPVDD | Supply | Charge pump supply |
| C7 | CPGND | Ground | Charge pump ground |
| B6 | CPCA | Analogue In | Charge pump fly-back cap pin A |
| B7 | CPCB | Analogue In | Charge pump fly-back cap pin B |
| A6 | CPVOUTP | Supply Out | Charge pump positive rail (HP supply) |
| A7 | CPVOUTN | Supply Out | Charge pump negative rail (HP supply) |
| A2 | SPKVDD1 | Supply | Left speaker supply |
| C2 | SPKVDD2 | Supply | Right speaker supply |
| B1 | SPKGND1 | Ground | Left speaker ground |
| C1 | SPKGND2 | Ground | Right speaker ground |
| A3 | MICVDD | Supply | Microphone bias amp supply |
| A1 | SPKOUTLP | Output | Left speaker + output |
| B3 | SPKOUTLN | Output | Left speaker − output |
| B2 | SPKOUTRP | Output | Right speaker + output |
| C3 | SPKOUTRN | Output | Right speaker − output |
| A5 | HPOUTR | Output | Right headphone / line output |
| B5 | HPOUTL | Output | Left headphone / line output |
| B4 | HPOUTFB | Analogue In | HP ground loop noise rejection feedback |
| C5 | VMIDC | Reference | Mid-rail reference (AVDD/2); decouple externally |
| A4 | MICBIAS | Reference | Microphone bias output |
| C4 | IN1L | Analogue In | Left SE input 1 |
| D4 | IN1R | Analogue In | Right SE input 1 |
| D5 | IN2L | Analogue In | Left SE input 2 |
| E5 | IN2R | Analogue In | Right SE input 2 |
| F5 | IN3L | Analogue In | Left SE input 3 |
| F6 | IN3R | Analogue In | Right SE input 3 |
| E6 | IN4L | Analogue In | Left SE input 4 |
| E7 | IN4R | Analogue In | Right SE input 4 |
| D1 | DACDAT | Digital In | DAC audio data |
| D2 | ADCDAT | Digital Out | ADC audio data |
| D3 | LRCLK | Digital I/O | Left/right word clock |
| E1 | BCLK | Digital I/O | Bit clock |
| F1 | SCLK | Digital In | Control interface clock |
| E2 | SDA | Digital I/O | Control interface data (I2C SDA) |
| E3 | CS/GPIO6 | Digital I/O | SPI chip select / GPIO |
| F2 | CIFMODE | Digital In | Interface select: 0 = SPI, 1 = I2C |
| G1 | GPIO5 | Digital I/O | Digital mic input / GPIO |

### Project Usage Notes

No project-specific notes yet.

---

## 24AA025UID

**Manufacturer:** Microchip Technology  
**Mfr Part Number:** 24AA025UIDT-I/OT (6-lead SOT-23, industrial, tape and reel)  
**Package:** SOT-23, 6-lead  
**Category:** IC — Memory / I2C EEPROM with Unique ID  
**Datasheet:** DS20005202A, Microchip Technology, 2013  
**Added:** 2026-05-04  
**Used in:** ESH10000543 R2

2 Kbit I2C EEPROM organised as 2 × 128 × 8 bit, with a preprogrammed 32-bit unique serial number. Cascadable — up to 8 devices on one bus via A0/A1 address pins. VCC 1.7 V–5.5 V. SDA and SCL are open-drain; external pull-up resistors required on both lines.

### Pin Description (6-lead SOT-23)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | SCL | I | Serial clock input |
| 2 | VSS | — | Ground |
| 3 | SDA | I/O (OD) | Serial address/data, open-drain |
| 4 | A1 | I | Chip address bit 1 — **must be tied to VSS or VCC** |
| 5 | A0 | I | Chip address bit 0 — **must be tied to VSS or VCC** |
| 6 | VCC | — | Supply voltage, 1.7 V–5.5 V |

> Note: A2 is not bonded in the 6-lead SOT-23 package; the corresponding slave address bit must always be '0'.

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC | 1.7 | — | 5.5 | V | Operating |
| VIH | 0.7×VCC | — | — | V | |
| VIL | — | — | 0.3×VCC | V | |
| VOL | — | — | 0.4 | V | IOL = 3.0 mA, VCC ≥ 2.5 V |
| ICCS (standby) | — | 0.01 | 1 | µA | |
| ICC (read) | — | 0.05 | 1 | mA | |
| FCLK | — | — | 400 / 100 | kHz | VCC ≥ 2.5 V / VCC < 2.5 V |
| TWC (write cycle) | — | — | 5 | ms | |
| Operating temp | −40 | — | +85 | °C | Industrial |

### Application Notes

- **SDA requires pull-up to VCC** — open-drain output. Typical: 10 kΩ for 100 kHz, 2 kΩ for 400 kHz.
- **SCL requires pull-up to VCC** — I2C bus requirement.
- **A0 and A1 must be connected to VSS or VCC** — must not be left floating. Determines I2C slave address bits.
- VCC bypass capacitor recommended.
- Up to 8 devices cascadable on one bus (4 for SOT-23 package variant).

### Project Usage Notes

> **[ESH10000543 R2]:** U15 (24AA025UIDT-I/OT). I2C EEPROM for device identification. VCC on VID net; A0 and A1 tied to GND (address = 0b000).

---

## TRSF3232E

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** TRSF3232EIPWR (TSSOP-16, industrial −40 °C to +85 °C); TRSF3232EIDR (SOIC-16)  
**Package:** TSSOP-16 (PW suffix); SOIC-16 (D suffix); also SOT-23-THN (DYY) and VQFN  
**Category:** IC — Digital / Interface  
**Datasheet:** TRSF3232E datasheet, SLLS825C, Texas Instruments, August 2007 – revised December 2024  
**Added:** 2026-04-30  
**Used in:** ESH10000540 R3

Dual RS-232 driver/receiver with integrated charge pump. Operates from a single 3.0 V to 5.5 V supply; generates ±5 V RS-232 levels internally using two external charge-pump capacitors. Two independent TX channels (DINx → DOUTx) and two independent RX channels (RINx → ROUTx).

### Pin Description (D / PW — SOIC-16 / TSSOP-16)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | C1+ | — | Positive terminal of charge-pump capacitor C1 |
| 2 | V+ | O | Positive charge-pump output (~+5.5 V); connect storage capacitor to GND |
| 3 | C1− | — | Negative terminal of charge-pump capacitor C1 |
| 4 | C2+ | — | Positive terminal of charge-pump capacitor C2 |
| 5 | C2− | — | Negative terminal of charge-pump capacitor C2 |
| 6 | V− | O | Negative charge-pump output (~−5.5 V); connect storage capacitor to GND |
| 7 | DOUT2 | O | RS-232 line data output, channel 2 (to remote RS-232 system) |
| 8 | RIN2 | I | RS-232 line data input, channel 2 (from remote RS-232 system) |
| 9 | ROUT2 | O | Logic-level data output, channel 2 (to UART) |
| 10 | DIN2 | I | Logic-level data input, channel 2 (from UART) |
| 11 | DIN1 | I | Logic-level data input, channel 1 (from UART) |
| 12 | ROUT1 | O | Logic-level data output, channel 1 (to UART) |
| 13 | RIN1 | I | RS-232 line data input, channel 1 (from remote RS-232 system) |
| 14 | DOUT1 | O | RS-232 line data output, channel 1 (to remote RS-232 system) |
| 15 | GND | — | Ground |
| 16 | VCC | — | Supply voltage; connect 0.1 µF bypass capacitor to GND |
| Pad | — | — | Exposed thermal pad; may be connected to GND or left floating |

> VQFN (RGT) package has a different pin numbering — see Table 4-1 in the datasheet.

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC | 3.0 | — | 5.5 | V | — |
| Driver output voltage (RS-232) | ±5.0 | — | — | V | Into 3 kΩ load |
| Receiver input threshold high | — | 1.7 | — | V | RIN → ROUT goes low |
| Receiver input threshold low | — | 0.8 | — | V | RIN → ROUT goes high |
| Data rate | — | — | 250 | kbps | — |
| Charge pump capacitors (C1, C2) | 47 | 100 | — | nF | Ceramic |
| Storage capacitors (V+, V−) | 47 | 100 | — | nF | Ceramic |
| ESD protection (RS-232 pins) | ±15 | — | — | kV | Human Body Model |

### Application Notes

- Each channel is fully independent; unused driver outputs (DOUTx) may be left unconnected.
- If DINx is left unconnected, DOUTx output is in a defined state due to internal pull-up on DIN.
- Connect 100 nF ceramic capacitors: C1+ to C1−, C2+ to C2−, V+ to GND, V− to GND.
- Thermal pad may be connected to GND plane or left floating.

### Project Usage Notes

> **[ESH10000540 R3]:** U18; RS-232 ↔ RS-485 bridge. Channel 2 RX (RIN2/ROUT2) receives data from D-SUB connector; channel 1 TX (DIN1/DOUT1) transmits to D-SUB connector. DOUT2 (pin 7) left unconnected — channel 2 driver not used. Powered from 5V rail.

---

## MAX491E / MAX491ESD

**Manufacturer:** Maxim Integrated (now Analog Devices)  
**Mfr Part Number:** MAX491ESD+T (SOIC-14, −40 °C to +85 °C); MAX491CSD (0 °C to +70 °C)  
**Package:** SOIC-14 (ESD suffix = wide-body SO-14); also DIP-14  
**Category:** IC — Digital / Interface  
**Datasheet:** MAX481E/MAX483E/MAX485E/MAX487E–MAX491E/MAX1487E, Maxim Integrated  
**Added:** 2026-04-30  
**Used in:** ESH10000540 R3

Full-duplex RS-485/RS-422 transceiver with ±15 kV ESD protection on bus pins. Separate differential TX (Y/Z) and RX (A/B) pairs allow simultaneous transmit and receive on a 4-wire RS-485 bus. Independent Driver Enable (DE) and Receiver Enable (/RE) controls.

### Pin Description (MAX491E, 14-pin SOIC/DIP)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | N.C. | — | No Connect — not internally connected |
| 2 | RO | O | Receiver Output. High when A > B by 200 mV; low when A < B by 200 mV. Hi-Z when /RE = high |
| 3 | /RE | I | Receiver Enable, active low. RO enabled when /RE = low |
| 4 | DE | I | Driver Output Enable, active high. Y and Z active when DE = high |
| 5 | DI | I | Driver Input. DI = low → Y low, Z high. DI = high → Y high, Z low |
| 6 | GND | — | Ground |
| 7 | GND | — | Ground |
| 8 | N.C. | — | No Connect — not internally connected |
| 9 | Y | O | Non-inverting Driver Output (RS-485 TX+) |
| 10 | Z | O | Inverting Driver Output (RS-485 TX−) |
| 11 | B | I | Inverting Receiver Input (RS-485 RX−) |
| 12 | A | I | Non-inverting Receiver Input (RS-485 RX+) |
| 13 | N.C. | — | No Connect — not internally connected |
| 14 | VCC | — | Positive Supply. Bypass with 0.1 µF ceramic to GND |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC | 4.75 | 5.0 | 5.25 | V | — |
| Driver differential output (no load) | 5.0 | — | — | V | — |
| Driver differential output (with load) | 1.5 | — | — | V | R = 27 Ω or 50 Ω |
| Receiver differential threshold | −0.2 | — | +0.2 | V | — |
| Receiver input hysteresis | 70 | — | — | mV | — |
| Receiver output high | 3.5 | — | — | V | IO = −4 mA |
| Receiver output low | — | — | 0.4 | V | IO = +4 mA |
| Maximum data rate | — | 2.5 | — | Mbps | MAX491E |
| ESD protection (A, B, Y, Z) | ±15 | — | — | kV | Human Body Model |

### Function Tables

**Driver (DE = 1):**

| DI | Y | Z |
|----|---|---|
| 1 | H | L |
| 0 | L | H |

**Receiver (/RE = 0):**

| A − B | RO |
|-------|----|
| > +0.2 V | H |
| < −0.2 V | L |
| Open inputs | H |

### Application Notes

- Y/Z = driver outputs (TX); A/B = receiver inputs (RX). Full-duplex 4-wire RS-485: Y→A-line, Z→B-line.
- DE and /RE may be driven complementarily for simple TX/RX toggle.
- Place 0.1 µF bypass capacitor between VCC (pin 14) and GND close to the IC.
- Bus termination resistor (typically 120 Ω) at each end of the RS-485 cable.

### Project Usage Notes

> **[ESH10000540 R3]:** U24; full-duplex RS-485 interface. DE (pin 4) = RS485_EN; /RE (pin 3) = RS485_ENn (complementary via U42 open-drain inverter). TX: DI ← UART_TXD_BUF (from U18 ROUT2). RX: RO → UART_RXD_BUF (to U18 DIN1). Bus: Y=RS485_TX+, Z=RS485_TX−, A=RS485_RX+, B=RS485_RX−. Powered from 5V rail.

---

## AMS1117

**Manufacturer:** Advanced Monolithic Systems (AMS)  
**Mfr Part Number:** AMS1117-ADJ / AMS1117-1.2 / -1.5 / -1.8 / -2.5 / -2.85 / -3.3 / -5  
**Package:** SOT-223 (4-lead), TO-252 (3-lead)  
**Category:** IC — Power / LDO Regulator  
**Datasheet:** AMS1117_20120314 (Advanced Monolithic Systems, Rev 2012-03-14)  
**Added:** 2026-04-30  
**Used in:** ESH10000540 R3

1 A, low dropout three-terminal regulator available in fixed output voltages (1.2 V–5 V) and an adjustable variant; quiescent current flows into the load rather than to ground.

### Pin Description

**SOT-223 (4-lead) — Fixed variants (AMS1117-1.2 … AMS1117-5):**

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | GND | — | Ground |
| 2 | OUTPUT | O | Regulated output (also connected to tab) |
| 3 | INPUT | I | Unregulated input voltage |
| Tab | OUTPUT | — | Exposed metal tab — internally connected to pin 2 (OUTPUT); must be soldered |

**SOT-223 (4-lead) — Adjustable variant (AMS1117-ADJ):**

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | ADJ | I | Adjust pin — sets output voltage via external resistor divider |
| 2 | OUTPUT | O | Regulated output (also connected to tab) |
| 3 | INPUT | I | Unregulated input voltage |
| Tab | OUTPUT | — | Exposed metal tab — internally connected to pin 2 (OUTPUT); must be soldered |

**TO-252 (3-lead) — Fixed variants:**

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | GND / ADJ | — | Ground (fixed) or Adjust (ADJ variant) |
| 2 | INPUT | I | Unregulated input |
| 3 | OUTPUT | O | Regulated output (tab also = OUTPUT) |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VIN (abs max) | — | — | 18 | V | All variants |
| Dropout voltage | — | 1.10 | 1.25 | V | IOUT = 1 A |
| IOUT (max) | — | — | 1 | A | — |
| VREF (ADJ variant) | 1.225 | 1.250 | 1.275 | V | 1.5 V ≤ VIN−VOUT ≤ 7 V, 10 mA ≤ IOUT ≤ 1 A |
| IADJ (ADJ pin current) | — | 50 | 120 | µA | — |
| IADJ change | — | — | 5 | µA | Over line/load range |
| Min load current (ADJ) | 10 | — | — | mA | Required to maintain regulation |
| Current limit | 1.1 | 1.5 | — | A | VIN−VOUT = 2 V, TJ = 25 °C |
| Quiescent current | — | 5 | 13 | mA | VIN = VOUT + 1.25 V |
| Line regulation | — | 0.035 | 0.2 | % | IOUT = 10 mA, (VOUT+1.5 V) ≤ VIN ≤ 12 V |
| Load regulation | — | 0.2 | 0.7 | % | VIN−VOUT = 2 V, 10 mA ≤ IOUT ≤ 1 A |
| Ripple rejection | 60 | 72 | — | dB | f = 120 Hz, VIN−VOUT = 3 V, 1 VPP ripple |
| Thermal shutdown | — | 155 | — | °C | Junction temperature |
| θJC (SOT-223) | — | 15 | — | °C/W | Junction-to-case |
| θJC (TO-252) | — | 3 | — | °C/W | Junction-to-case |
| Operating temp | −20 | — | 125 | °C | Junction |

**Fixed variant output voltages:**

| Part Number | VOUT (nom) | VIN (min for regulation) |
|-------------|-----------|--------------------------|
| AMS1117-1.2 | 1.200 V | 2.7 V |
| AMS1117-1.5 | 1.500 V | 3.0 V |
| AMS1117-1.8 | 1.800 V | 3.3 V |
| AMS1117-2.5 | 2.500 V | 4.0 V |
| AMS1117-2.85 | 2.850 V | 4.35 V |
| AMS1117-3.3 | 3.300 V | 4.8 V |
| AMS1117-5.0 | 5.000 V | 6.5 V |

### Formulas

#### Output Voltage (ADJ variant)

```
VOUT = VREF × (1 + R2/R1) + IADJ × R2
```

- VREF = 1.250 V (typ); use 1.225 V / 1.275 V for worst-case min/max
- IADJ = 50–120 µA — adds a small error term; typically negligible if R2 ≤ 1 kΩ
- R1 = resistor from OUTPUT to ADJ pin (datasheet label)
- R2 = resistor from ADJ pin to GND (datasheet label)
- Simplified (IADJ term negligible): `VOUT ≈ 1.250 × (1 + R2/R1)`

### Application Notes

- Place a 10 µF (or larger) electrolytic capacitor on the output, within 4 cm of the VOUT pin, for stability.
- Input bypass capacitor (1 µF ceramic) recommended close to the input pin.
- ADJ variant requires a minimum 10 mA load current to maintain regulation; use a dummy load resistor if the load current may drop below this.
- The quiescent current (up to 13 mA) flows into the OUTPUT pin, not to ground — include this in total load current budgeting.
- Tab (SOT-223 pin 2 / TO-252 tab) is OUTPUT — connect to copper pour for thermal dissipation.

### Project Usage Notes

> ⚠️ **ERC check — ADJ minimum load (recurring issue):** Every use of the AMS1117-ADJ must be checked for minimum load at all operating conditions. The ADJ variant requires ≥ 10 mA into the output to maintain regulation. The resistor divider on the ADJ pin contributes quiescent current — verify this plus downstream loads always sum to ≥ 10 mA. If the load may drop below 10 mA under any condition, add a dummy load resistor. This has caused regulation issues in previous projects (flagged ESH10000535 R3, 2026-05-04).

---

## SN74LVC2G06

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** SN74LVC2G06DBVR (SOT-23-6) and variants  
**Package:** SOT-23-6 (DBV), SC70-6 (DCK), SON-6 (DRY / DSF), DSBGA-6 (YZP)  
**Category:** IC — Logic / Buffer (open-drain)  
**Datasheet:** SN74LVC2G06, SCES307J, Texas Instruments, Revised July 2015  
**Added:** 2026-04-30  
**Used in:** ESH10000540 R3

Dual CMOS inverter buffer with open-drain outputs; 1.65 V–5.5 V supply, 5.5 V-tolerant inputs and outputs, 32 mA sink current.

### Pin Description

**SOT-23-6 (DBV) — top view:**

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | 1A | I | Input 1 |
| 2 | GND | — | Ground |
| 3 | 2A | I | Input 2 |
| 4 | 2Y | O | Open-drain output 2 |
| 5 | VCC | — | Supply voltage |
| 6 | 1Y | O | Open-drain output 1 |

Pin assignments are identical for SC70-6 (DCK) and SON-6 (DRY/DSF).

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC | 1.65 | — | 5.5 | V | Operating |
| VI, VO (max) | — | — | 5.5 | V | Inputs and open-drain outputs |
| IOL (VCC = 1.65 V) | — | — | 4 | mA | Low-level output current |
| IOL (VCC = 2.3 V) | — | — | 8 | mA | — |
| IOL (VCC = 3.0 V) | — | — | 16 | mA | — |
| IOL (VCC = 4.5 V) | — | — | 32 | mA | — |
| ICC (static) | — | — | 10 | µA | VI = VCC or GND, IO = 0 |
| tpd (3.3 V, −40 to 85 °C) | 1 | — | 3.4 | ns | A → Y |
| tpd (3.3 V, −40 to 125 °C) | 1 | — | 3.9 | ns | A → Y |
| ESD (HBM) | — | — | 2000 | V | ANSI/ESDA/JEDEC JS-001 |
| ESD (CDM) | — | — | 1000 | V | JEDEC JESD22-C101 |
| θJA (SOT-23-6 DBV) | — | 165 | — | °C/W | Junction-to-ambient |
| Operating temp | −40 | — | 125 | °C | — |

### Function Table

| A (input) | Y (open-drain output) |
|-----------|-----------------------|
| L | Hi-Z (output floats — must be pulled high externally) |
| H | L (output pulls to GND) |

### Application Notes

- Open-drain outputs **require an external pull-up resistor** to the desired high-side voltage (up to 5.5 V). Without a pull-up, the output cannot assert a high level.
- Suitable for open-drain bus wiring (wired-AND / wired-OR) and level translation (e.g. 3.3 V input → 5 V pulled-high output).
- Maximum sink current is 32 mA at VCC = 4.5 V; derate for lower supply voltages.
- The IOFF feature disables outputs when VCC = 0 V, preventing back-drive through the device.
- This device is an inverting buffer: a high input drives the output low; a low input lets the output float.

### Layout Notes

- All unused inputs must be tied to VCC or GND — never left floating. An undefined input creates an undefined output state and excessive ICC.
- Place a 0.1 µF bypass capacitor between VCC (pin 5) and GND close to the device.
- For multiple VCC pins (multi-gate packages), use 0.01–0.022 µF per pin; paralleling with 1 µF is acceptable.
- Route pull-up resistor close to the output pin to minimize stub length.

### Project Usage Notes

---

## SN74HCS86

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** SN74HCS86PW (TSSOP-14) and variants  
**Package:** TSSOP-14 (PW), SOIC-14 (D), WQFN-14 (BQA)  
**Category:** IC — Logic / Gate (XOR)  
**Datasheet:** SN74HCS86, SCLS783B, Texas Instruments, Revised January 2021  
**Added:** 2026-04-30  
**Used in:** ESH10000540 R3

Quadruple 2-input XOR gate with Schmitt-trigger inputs; 2 V–6 V supply, no input transition rate requirement, AEC Q100 qualified.

### Pin Description

**D or PW Package — 14-pin SOIC or TSSOP (top view):**

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | 1B | I | Channel 1, Input B |
| 2 | 1A | I | Channel 1, Input A |
| 3 | 1Y | O | Channel 1, Output |
| 4 | 2A | I | Channel 2, Input A |
| 5 | 2B | I | Channel 2, Input B |
| 6 | 2Y | O | Channel 2, Output |
| 7 | GND | — | Ground |
| 8 | 3Y | O | Channel 3, Output |
| 9 | 3A | I | Channel 3, Input A |
| 10 | 3B | I | Channel 3, Input B |
| 11 | 4Y | O | Channel 4, Output |
| 12 | 4A | I | Channel 4, Input A |
| 13 | 4B | I | Channel 4, Input B |
| 14 | VCC | — | Positive supply |
| — | Thermal Pad | — | BQA package only — connect to GND or leave floating; do not connect to any signal or supply |

### Key Electrical Parameters

| Parameter | VCC | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|-----|------|-------|
| VCC | — | 2 | 5 | 6 | V | Operating |
| VT+ (pos. threshold) | 4.5 V | 1.7 | — | 3.15 | V | Schmitt-trigger threshold |
| VT− (neg. threshold) | 4.5 V | 0.9 | — | 2.2 | V | Schmitt-trigger threshold |
| ΔVT (hysteresis) | 4.5 V | 0.4 | — | 1.4 | V | VT+ − VT− |
| VOH | 4.5 V (IOH=−6 mA) | 4.0 | 4.3 | — | V | — |
| VOH | 6 V (IOH=−7.8 mA) | 5.4 | 5.75 | — | V | — |
| VOL | 4.5 V (IOL=6 mA) | — | 0.18 | 0.30 | V | — |
| VOL | 6 V (IOL=7.8 mA) | — | 0.22 | 0.33 | V | — |
| IOH / IOL | 4.5 V | — | — | ±6 | mA | — |
| IOH / IOL | 6 V | — | — | ±7.8 | mA | — |
| ICC (static) | 6 V | — | 0.1 | 2 | µA | VI = VCC or GND, IO = 0 |
| II (input leakage) | 6 V | — | — | ±1000 | nA | — |
| tpd (A or B → Y) | 4.5 V | 7 | — | 13 | ns | CL = 50 pF |
| tpd (A or B → Y) | 6 V | 6 | — | 12 | ns | CL = 50 pF |
| ESD (HBM) | — | — | — | ±4000 | V | AEC Q100-002 Level 2 |
| ESD (CDM) | — | — | — | ±1500 | V | AEC Q100-011 Level C6 |
| Operating temp | — | −40 | — | +125 | °C | — |

### Function Table

| A | B | Y |
|---|---|---|
| L | L | L |
| L | H | H |
| H | L | H |
| H | H | L |

Y = A ⊕ B (exclusive-OR in positive logic)

### Application Notes

- Unused inputs must be tied to VCC or GND — never leave floating.
- Unused push-pull outputs may be left unconnected.
- Maximum recommended CL: 50 pF to meet datasheet switching specs.
- Schmitt-trigger inputs have no transition rate requirement — suitable for slow or noisy signals.
- Each gate channel is fully independent; unused channels should have inputs grounded.

### Layout Notes

- Place 0.1 µF ceramic bypass capacitor between VCC (pin 14) and GND close to the device.
- Use solid ground plane to reduce noise and EMI.

### Project Usage Notes

---

## SN74HCS74

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** SN74HCS74PW (TSSOP-14) and variants  
**Package:** TSSOP-14 (PW), SOIC-14 (D), WQFN-14 (BQA), SOT-23-thin-14 (DYY)  
**Category:** IC — Logic / Flip-Flop (D-type)  
**Datasheet:** SN74HCS74, SCLS782D, Texas Instruments, Revised December 2021  
**Added:** 2026-04-30  
**Used in:** ESH10000540 R3

Dual D-type positive-edge-triggered flip-flop with Schmitt-trigger inputs, asynchronous active-low clear and preset; 2 V–6 V supply, AEC Q100 qualified.

### Pin Description

**D, PW, or DYY Package — 14-pin (top view):**

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | 1CLR | I | Clear for channel 1, active low |
| 2 | 1D | I | Data for channel 1 |
| 3 | 1CLK | I | Clock for channel 1, rising-edge triggered |
| 4 | 1PRE | I | Preset for channel 1, active low |
| 5 | 1Q | O | Output for channel 1 |
| 6 | 1Qbar | O | Inverted output for channel 1 |
| 7 | GND | — | Ground |
| 8 | 2Qbar | O | Inverted output for channel 2 |
| 9 | 2Q | O | Output for channel 2 |
| 10 | 2PRE | I | Preset for channel 2, active low |
| 11 | 2CLK | I | Clock for channel 2, rising-edge triggered |
| 12 | 2D | I | Data for channel 2 |
| 13 | 2CLR | I | Clear for channel 2, active low |
| 14 | VCC | — | Positive supply |
| — | Thermal Pad | — | BQA package only — connect to GND or leave floating |

### Key Electrical Parameters

| Parameter | VCC | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|-----|------|-------|
| VCC | — | 2 | 5 | 6 | V | Operating |
| VOH | 4.5 V (IOH=−6 mA) | 4.0 | 4.3 | — | V | — |
| VOL | 4.5 V (IOL=6 mA) | — | 0.18 | 0.30 | V | — |
| IOH / IOL | 4.5 V | — | — | ±6 | mA | — |
| IOH / IOL | 6 V | — | — | ±7.8 | mA | — |
| ICC (static) | 6 V | — | 0.1 | 2 | µA | — |
| fmax | 4.5 V | — | 45 | 95 | MHz | Clock frequency |
| fmax | 6 V | — | 65 | 105 | MHz | Clock frequency |
| tpd (CLK → Q) | 4.5 V | 8 | — | 19 | ns | CL = 50 pF |
| tpd (PRE/CLR → Q) | 4.5 V | 8 | — | 19 | ns | CL = 50 pF |
| tSU (Data before CLK↑) | 4.5 V | 9 | — | — | ns | — |
| tH (Data after CLK↑) | 4.5 V | 0 | — | — | ns | — |
| tw (CLK high or low) | 4.5 V | 12 | — | — | ns | — |
| tw (PRE or CLR low) | any | 11 | — | — | ns | — |
| VT+ (Schmitt) | 4.5 V | 1.7 | — | 3.15 | V | — |
| VT− (Schmitt) | 4.5 V | 0.9 | — | 2.2 | V | — |
| ΔVT (hysteresis) | 4.5 V | 0.4 | — | 1.4 | V | — |
| ESD (HBM) | — | — | — | ±4000 | V | AEC Q100-002 Level 2 |
| ESD (CDM) | — | — | — | ±1500 | V | AEC Q100-011 Level C6 |
| Operating temp | — | −40 | — | +125 | °C | — |

### Function Table

| PRE | CLR | CLK | D | Q | Qbar | Note |
|-----|-----|-----|---|---|------|------|
| L | H | X | X | H | L | Asynchronous preset |
| H | L | X | X | L | H | Asynchronous clear |
| L | L | X | X | H* | H* | Both active — unstable; avoid this state |
| H | H | ↑ | H | H | L | Data captured on rising clock edge |
| H | H | ↑ | L | L | H | Data captured on rising clock edge |
| H | H | L or H | X | Q₀ | Qbar₀ | Hold — no change |

(X = don't care; ↑ = rising edge; * = nonstable configuration)

### Application Notes

- All asynchronous inputs (PRE, CLR) are active-low; tie inactive inputs to VCC.
- To make D=Qbar (divide-by-2 / toggle): connect Qbar to D — each rising CLK edge toggles Q.
- Schmitt-trigger inputs have no transition rate requirement — suitable for slow or noisy clock signals.
- Unused inputs must be tied to VCC or GND.
- Unused outputs may be left unconnected (push-pull CMOS).

### Layout Notes

- Place 0.1 µF ceramic bypass capacitor between VCC (pin 14) and GND close to the device.
- Keep clock routing short to minimize noise pickup.

### Project Usage Notes

---

## REF3425-EP

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** REF3425-EP (2.5 V) / REF3430-EP (3 V) / REF3433-EP (3.3 V) / REF3440-EP (4.096 V)  
**Package:** SOT-23-6 (DBV)  
**Category:** IC — Analog / Voltage Reference  
**Datasheet:** REF3425-EP/REF3430-EP/REF3433-EP/REF3440-EP, SBAS942B, Texas Instruments, Revised April 2019  
**Added:** 2026-04-30  
**Used in:** ESH10000540 R3

Low-drift (10 ppm/°C max), low-power (95 µA max) precision CMOS voltage reference with enable/shutdown pin and Kelvin force/sense connections; 6-pin SOT-23.

### Pin Description

**SOT-23-6 (DBV) — top view:**

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | GND_F | — | Ground force — main GND connection |
| 2 | GND_S | — | Ground sense — Kelvin sense for ground; tie to GND_F if Kelvin not used |
| 3 | ENABLE | I | Enable: ≥ 1.6 V = active mode, ≤ 0.5 V = shutdown; tie to IN if shutdown not used |
| 4 | IN | — | Input supply voltage |
| 5 | OUT_S | O | Output sense — Kelvin sense for VOUT; tie to OUT_F if Kelvin not used |
| 6 | OUT_F | O | Output force — main reference output |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VOUT (REF3425-EP) | — | 2.500 | — | V | ±0.05% initial accuracy |
| VOUT (REF3430-EP) | — | 3.000 | — | V | ±0.05% initial accuracy |
| VOUT (REF3433-EP) | — | 3.300 | — | V | ±0.05% initial accuracy |
| VOUT (REF3440-EP) | — | 4.096 | — | V | ±0.05% initial accuracy |
| Initial accuracy | — | — | ±0.05 | % | TA = 25°C |
| Temp coefficient | — | 2.5 | 10 | ppm/°C | −55°C to +125°C, box method |
| VIN (max) | — | — | 12 | V | — |
| VDO (dropout, IL=0, 25°C) | — | — | 50 | mV | Min input headroom above VOUT |
| VDO (dropout, IL=0, over temp) | — | — | 100 | mV | — |
| VDO (dropout, IL=10 mA, over temp) | — | — | 500 | mV | — |
| IL (output current) | −10 | — | +10 | mA | Sink and source |
| IQ (active mode, over temp) | — | 72 | 95 | µA | — |
| IQ (shutdown mode, over temp) | — | — | 3 | µA | EN ≤ 0.5 V |
| Line regulation | — | — | 15 | ppm/V | Over temp |
| Load regulation (sourcing) | — | — | 30 | ppm/mA | Over temp |
| Output voltage noise (0.1–10 Hz) | — | — | 5 | µVpp/V | — |
| Long-term stability | — | 25 | — | ppm | 0–1000 hours at 35°C |
| ESD (HBM) | — | — | ±2500 | V | ANSI/ESDA/JEDEC JS-001 |
| ESD (CDM) | — | — | ±1500 | V | JESD22-C101 |
| θJA (SOT-23-6) | — | 185 | — | °C/W | — |
| Operating temp | −55 | — | +125 | °C | Tj max = 150°C abs |

### Application Notes

- **ENABLE pin:** If shutdown not used, tie EN to IN pin. Never allow EN to sit between 0.5 V and 1.6 V — causes high quiescent current and may prevent startup.
- **Kelvin connections:** For simple 3-terminal use, short GND_S to GND_F and OUT_S to OUT_F. For maximum accuracy, route separate high-impedance sense traces to the load to eliminate IR drop error in supply traces.
- **VIN slew rate:** Rising and falling slew rate of VIN should be close to 6 V/ms to avoid output overshoot or anomalies.
- **Short-circuit protection:** Output is protected; short-circuit current is limited to ~18–22 mA.
- **Solder heat shift:** Output may shift slightly after reflow (typically < 0.01%). If PCB is soldered on both sides, solder this device in the second reflow pass.

### Layout Notes

- Place 0.1 µF ceramic + 1 µF electrolytic (or ceramic) bypass capacitor at VIN (pin 4), close to the device.
- Place at least 0.1 µF ceramic at OUT_F (pin 6); add 1–10 µF for better transient performance. Prefer X5R or X7R ceramic; if using electrolytic, parallel with 0.1 µF ceramic to reduce ESR.
- Stable output capacitor value: 0.1 µF to 10 µF (over full temperature range).
- Use solid ground plane to reduce EMI noise pickup and distribute heat.
- Do not route sensitive analog output traces parallel to digital lines; cross only perpendicularly.
- Mount device as close to the load as practical to minimize trace IR drop.

### Project Usage Notes

> **[ESH10000540 R3]:** U27 (REF3425IDBVR) — EN tied to IN per application note. Output (OUT_F) routed to VREF net shared by U12, U39, U40 (ADS7828) and U5, U6 (AD5593R).

---

## TPS54302

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** TPS54302DDC (SOT-23-6)  
**Package:** SOT-23-THIN (DDC), 6-pin, 2.9 × 2.8 mm  
**Description:** 4.5 V–28 V Input, 3 A, EMI-Friendly Synchronous Step-Down Buck Converter  
**Datasheet:** SLVSDG6C, May 2016 – Revised March 2026 (Texas Instruments)

### Pin Functions — SOT-23-6 DDC (Top View)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | GND | — | Ground (source of LS NFET; controller GND; Kelvin connect for FB) |
| 2 | SW | O | Switch node between HS and LS FETs |
| 3 | VIN | — | Input voltage supply (drain of HS NFET) |
| 4 | FB | I | Feedback input; connect resistor divider from output |
| 5 | EN | I | Enable; float = enabled; active HIGH >1.23 V; internal 0.7 µA pullup |
| 6 | BOOT | O | Bootstrap supply for HS gate drive; 0.1 µF X7R/X5R cap to SW |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VIN range | 4.5 | — | 28 | V | — |
| IOUT (continuous) | — | — | 3 | A | Integrated 85/40 mΩ FETs |
| fSW | 290 | 400 | 510 | kHz | Fixed; ±6% spread spectrum |
| VFB (reference) | 0.581 | 0.596 | 0.611 | V | ±2.5% accuracy |
| HS RDS(on) | — | 85 | — | mΩ | TA = 25°C |
| LS RDS(on) | — | 40 | — | mΩ | TA = 25°C |
| IQ (non-switching) | — | 45 | — | µA | EN = 5 V |
| IOFF (shutdown) | — | 2 | — | µA | EN = GND |
| VEN threshold (rising) | 1.23 | 1.28 | — | V | — |
| VEN threshold (falling) | 1.10 | 1.16 | — | V | — |
| Soft-start | — | 5 | — | ms | Internal |
| TJ operating | −40 | — | 125 | °C | — |
| Thermal shutdown | — | 160 | — | °C | Hiccup restart after 32 768 cycles |
| θJA (SOT-23-6) | — | 118.9 | — | °C/W | — |
| θJB | — | 35.0 | — | °C/W | — |
| ESD HBM | — | — | ±2500 | V | ANSI/ESDA/JEDEC JS-001 |
| MSL | — | 1-260C-UNLIM | — | — | — |

### Application Notes

- **Output voltage:** VOUT = VREF × (1 + R2/R3); VREF = 0.596 V typ; start with R2 = 100 kΩ, 1% tolerance or better.
- **BOOT capacitor:** 0.1 µF X7R/X5R ceramic between BOOT (pin 6) and SW (pin 2); mandatory for operation.
- **EN pin:** Float to enable (internal pullup). Use open-drain/open-collector logic to control. For adjustable UVLO: R4 from VIN to EN, R5 from EN to GND.
- **Input capacitor:** ≥10 µF ceramic; optional additional 0.1 µF HF bypass at VIN to GND.
- **Overcurrent:** Cycle-by-cycle current limit on both FETs; hiccup mode after 512 overcurrent cycles (restarts after 16 384 cycles).
- **Spread spectrum:** ±6% of fSW at 1/512 swing frequency for EMI reduction.

### Layout Notes

- SW trace: short and wide to minimize radiated EMI; do not allow switching current to flow under device.
- Input and output capacitors: as close to device as possible.
- Kelvin connection to GND pin for FB voltage sense; FB trace small and away from SW node.

### Project Usage Notes

> **[ESH10000540 R3]:** U15 (5 V output, sourced from 12 V or higher VIN, output on 5V net via L1-2); U16 (12 V output); U17 (6.5 V output). Output voltage set by resistor divider on FB net for each instance. EN pins controlled by system enable signals. BOOT cap per instance on BOOT–SW net.

---

## PCA9616

**Manufacturer:** NXP Semiconductors  
**Mfr Part Number:** PCA9616PW (TSSOP-16)  
**Package:** TSSOP-16 (SOT403-1), 4.4 mm body width  
**Description:** 3-Channel Fast-Mode Plus Differential I2C-Bus Buffer with Hot-Swap Logic  
**Datasheet:** PCA9616 Rev. 2, 10 March 2014 (NXP Semiconductors)

### Pin Functions — TSSOP-16 (Top View)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | VDD(A) | PWR | Card-side power supply (0.8–5.5 V; reference only) |
| 2 | SDA | I/O | Card-side open-drain serial data |
| 3 | EN | I | Enable (active HIGH); internal pullup to VDD(A); never change during I2C transaction |
| 4 | SCL | I/O | Card-side open-drain serial clock |
| 5 | PIDET | O | Plug-in detect (open-drain LOW when diff bus reliably connected); pullup 10 kΩ to VDD(A) |
| 6 | READY | O | Connection ready (open-drain; HIGH=disconnected, LOW=connected); pullup 10 kΩ to VDD(A) |
| 7 | INT | I/O | Card-side open-drain interrupt/sideband; **must tie to VSS if unused** |
| 8 | VSS | GND | Ground (0 V) |
| 9 | VDDA_SEL | I | VDD(A) range select: VDDA_SEL=0 (LOW) → VDD(A) = 0.8–2.4 V; VDDA_SEL=1 (HIGH) → VDD(A) = 2.2–5.5 V |
| 10 | DINTP | I/O | Differential INT+ (leave NC if INT unused) |
| 11 | DINTM | I/O | Differential INT− (leave NC if INT unused) |
| 12 | DSCLM | I/O | Differential SCL− |
| 13 | DSCLP | I/O | Differential SCL+ |
| 14 | DSDAP | I/O | Differential SDA+ |
| 15 | DSDAM | I/O | Differential SDA− |
| 16 | VDD(B) | PWR | Differential-side power supply (3.0–5.5 V; best at 5 V) |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VDD(A) range (VDDA_SEL=0) | 0.8 | — | 2.4 | V | Card-side supply; VDDA_SEL tied LOW |
| VDD(A) range (VDDA_SEL=1) | 2.2 | — | 5.5 | V | Card-side supply; VDDA_SEL tied HIGH |
| VDD(B) range | 3.0 | — | 5.5 | V | Diff-side supply; best at 5 V |
| Bus speed | — | — | 1 | MHz | Fm+ capable |
| Diff. output voltage | — | 1.5 | — | V | Nominal differential |
| Diff. input sensitivity | — | — | 200 | mV | Minimum receive threshold |
| Input hysteresis | — | 30 | — | mV | — |
| Max cable length | — | — | 3 | m | At full speed |
| READY time from power-on | — | — | 11 | ms | 1 ms power + 10 ms debounce |
| Temperature | −40 | — | +85 | °C | — |
| ESD HBM | — | — | ±2000 | V | JESD22-A114 |
| ESD CDM | — | — | ±1000 | V | JESD22-C101 |

### Application Notes

- **INT pin (pin 7):** If unused, **must** be tied to VSS — do not leave floating (may generate false bus signals due to noise on high-impedance input).
- **PIDET (pin 5) and READY (pin 6):** Connect pull-up resistors (typically 10 kΩ) to VDD(A); leave open or tie to VSS if status monitoring not required.
- **VDDA_SEL (pin 9):** Selects VDD(A) operating range. Recommend explicit tie — do not float. VDDA_SEL=0 (tie to VSS): VDD(A) = 0.8–2.4 V. VDDA_SEL=1 (tie to VDD(B) via resistor): VDD(A) = 2.2–5.5 V.
- **EN pin (pin 3):** HIGH connects device to bus; must only change state during bus idle — never during an active I2C transaction.
- **Differential termination:** Each end of cable terminated with R1-R2-R1 network; R1 = 600 Ω, R2 = 120 Ω (CAT5, VDD(B) = 5 V) giving 100 Ω differential impedance.
- **Single-ended pull-ups:** Required on SDA and SCL lines; size based on bus capacitance and desired speed.

### Project Usage Notes

> **[ESH10000540 R3]:** U1–U4 — VDD(B) = 3V3 (diff-side; within 3.0–5.5 V ✅). VDDA_SEL (pin 9) pulled HIGH via R1/R4/R13/R16 (to 3V3) → VDDA_SEL=1 mode; VDD(A) must be 2.2–5.5 V. U1–U3: VDD(A) = 3V3 ✅. U4: VDD(A) = VIO_EXT — accepted; VIO_EXT must remain within 2.2–5.5 V (ERC-P06, ESH10000540 R3, 2026-04-30). INT pin (pin 7) tied to GND per datasheet requirement. Unconnected pins 10, 11 (DINTP/DINTM) — confirmed correct when INT channel unused. Diff pairs routed to cable connectors.

---

## PCA9506

**Manufacturer:** NXP Semiconductors  
**Mfr Part Number:** PCA9506BS (HVQFN-56); also PCA9506DGG (TSSOP-56)  
**Package:** HVQFN-56 (SOT684-1), 8×8×0.85 mm, 0.5 mm pitch  
**Description:** 40-Bit I2C-Bus I/O Port Expander with RESET, Output Enable and Interrupt (PCA9506: no internal I/O pull-ups)  
**Datasheet:** PCA9505_9506 Rev. 5, 30 September 2021 (NXP Semiconductors)

### Pin Functions — HVQFN-56 (key pins; full mapping: datasheet Table 3)

| Pin (HVQFN) | Pin (TSSOP) | Name | Type | Description |
|-------------|-------------|------|------|-------------|
| 50 | 1 | SDA | I/O | Serial data line |
| 51 | 2 | SCL | I | Serial clock line |
| 1–5, 52–56 | 3–12 | IO0_0–IO0_7 | I/O | I/O bank 0 (8 pins) |
| 6–14 | 13–21 | IO1_0–IO1_7 | I/O | I/O bank 1 (8 pins) |
| 15–19, 24–28 | 22–33 | IO2_0–IO2_7 | I/O | I/O bank 2 (8 pins) |
| 29–37 | 36–44 | IO3_0–IO3_7 | I/O | I/O bank 3 (8 pins) |
| 38–47 | 45–54 | IO4_0–IO4_7 | I/O | I/O bank 4 (8 pins) |
| 4, 16, 27, 32, 44, 55 | 6, 11, 23, 34, 39, 51 | VSS | GND | Ground (also exposed center pad — must connect) |
| 11, 39 | 18, 46 | VDD | PWR | Supply voltage |
| 20 | 27 | A0 | I | Address bit 0 |
| 21 | 28 | A1 | I | Address bit 1 |
| 22 | 29 | A2 | I | Address bit 2 |
| 23 | 30 | OE | I | Active LOW output enable (3-states all outputs) |
| 48 | 55 | INT | O | Active LOW interrupt (open-drain) |
| 49 | 56 | RESET | I | Active LOW hardware reset |

### I2C Address

Base address: 0b0100_A2A1A0. A2/A1/A0 must be hardwired to VDD or VSS; no internal pull-ups.

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VDD range | 2.3 | — | 5.5 | V | — |
| I2C clock | — | — | 400 | kHz | Fast mode |
| Output current (source per I/O) | — | — | 10 | mA | At 5 V |
| Output current (sink per I/O) | — | — | 15 | mA | At 5 V |
| Package total load | — | — | 600 | mA | All 40 outputs combined |
| Temperature | −40 | — | +85 | °C | — |
| ESD HBM | — | — | ±2000 | V | JESD22-A114 |
| ESD CDM | — | — | ±1000 | V | JESD22-C101 |

### Application Notes

- **Default state:** All I/Os default to inputs at power-up and after RESET.
- **RESET pin:** Active LOW; tie HIGH (via pull-up to VDD) for normal operation.
- **A0, A1, A2:** No internal pull-ups — must be connected to VDD or VSS.
- **OE pin:** Active LOW; 3-states all output-configured I/Os. Can be used for LED PWM (>80 Hz).
- **INT pin:** Open-drain; requires external pull-up to VDD; asserts LOW on any monitored input-change unless masked.
- **Exposed center pad (HVQFN):** Must be connected to VSS/GND; use thermal vias for heat conduction.

### Project Usage Notes

> **[ESH10000540 R3]:** U7 (PCA9506BS, HVQFN-56). Unconnected pins 43, 45, 46, 47 (HVQFN numbering) in netlist — pending engineer verification of HVQFN↔TSSOP pin mapping to confirm whether these are I/O, VSS, or VDD pins.

---

## 24AA02UID

**Manufacturer:** Microchip Technology  
**Mfr Part Number:** 24AA02UID (SOT-23-5)  
**Package:** SOT-23-5 (5-lead)  
**Description:** 2 Kbit I2C EEPROM with Preprogrammed Unique 32-Bit Serial Number  
**Datasheet:** DS20005202A, 2013 (Microchip Technology Inc.)

### Pin Functions — SOT-23-5

| Pin | Name | Description |
|-----|------|-------------|
| 1 | SCL | Serial clock line (open-drain input; requires external pull-up) |
| 2 | VCC | Supply voltage (1.7–5.5 V) |
| 3 | SDA | Serial data line (open-drain bidirectional; requires external pull-up) |
| 4 | VSS | Ground |
| 5 | NC | No connect |

**Address note:** The 5-lead SOT-23 (24AA02UID) has no address pins. I2C address is **fixed at 0x50** (0b1010_000). Address pins A0/A1/A2 are only on PDIP/SOIC-8 packages.

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC range | 1.7 | — | 5.5 | V | — |
| I2C clock | — | — | 400 | kHz | VCC ≥ 2.5 V |
| I2C clock (low VCC) | — | — | 100 | kHz | VCC < 2.5 V |
| ICC read | — | 0.05 | 1 | mA | — |
| ICC write | — | 0.1 | 3 | mA | VCC = 5.5 V, 400 kHz |
| ICCS standby | — | 0.01 | 1 | µA | SDA = SCL = VCC |
| Page write time | — | 3 | 5 | ms | Self-timed; self-erasing |
| Page size | — | 8 | — | bytes | 24AA02UID |
| Unique ID length | — | 32 | — | bits | Factory pre-programmed; upper block 0x80–0x83 |
| Data retention | — | — | >200 | years | — |
| Write endurance | — | — | >1 M | cycles | — |
| Temperature | −40 | — | +85 | °C | Industrial |
| ESD | — | — | >4000 | V | All pins |

### Application Notes

- **I2C address:** Fixed 0x50; not configurable in SOT-23-5 package.
- **SDA and SCL:** Both open-drain; require external pull-up resistors to VCC.
- **Unique ID:** 32-bit serial number pre-programmed at factory; read from addresses 0x80–0x83.
- **Page write:** Up to 8 bytes per write cycle; use acknowledge polling to detect completion after ~3 ms.
- **Write protection:** No WP pin in 5-lead SOT-23 variant.

### Project Usage Notes

> **[ESH10000540 R3]:** U29 — fixture identification EEPROM. VCC tied to 3V3. SDA on SDA bus, SCL on SCL bus. Pin 5 (NC) unconnected in netlist per package definition.

---

## ALM2402-Q1

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** ALM2402QPWPRQ1 (HTSSOP-14); also ALM2402QDRRQ1 (WSON/SON-12)  
**Package:** HTSSOP-14 (PWP), 5.0×4.4 mm, exposed thermal pad  
**Description:** AEC-Q100 Dual High-Current Op-Amp with Over-Temperature Shutdown, 400 mA Continuous Output  
**Datasheet:** SLOS912D, February 2015 – Revised July 2015 (Texas Instruments)

### Pin Functions — HTSSOP-14 (PWP)

| Pin | Name | I/O | Description |
|-----|------|-----|-------------|
| 1 | IN1− | I | Ch1 inverting input |
| 2 | IN1+ | I | Ch1 non-inverting input |
| 3 | OTF/SH_DN | I/O | Over-temperature flag and shutdown (see truth table) |
| 4 | IN2+ | I | Ch2 non-inverting input |
| 5 | IN2− | I | Ch2 inverting input |
| 7 | NC | — | No internal connection — **do not connect** |
| 8 | NC | — | No internal connection — **do not connect** |
| 9 | OUT2 | O | Ch2 op-amp output |
| 10 | VCC_O2 | I | Ch2 output stage supply |
| 11 | VCC | I | Gain stage supply (both channels) |
| 12 | VCC_O1 | I | Ch1 output stage supply |
| 13 | OUT1 | O | Ch1 op-amp output |
| 14 | GND | — | Ground (must connect) |
| EP | Exposed pad | — | Connect to GND for best thermal; must not connect to any other potential |

**OTF/SH_DN truth table:**

| State | Description |
|-------|-------------|
| Float or HIGH (≥1.0 V) | Normal operation (opamp ON) |
| LOW (≤0.35 V) | Shutdown (low IQ ≈ 0.5 mA total) |
| Output — pulls LOW | When TJ > 165°C (typ); requires external pull-up (e.g. 2.5 kΩ) to observe flag |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC range | 4.5 | — | 16 | V | Gain stage supply |
| VCC_O(x) range | 3 | — | 16 | V | Output stage supply |
| IOUT (continuous per channel) | — | — | 400 | mA | Sourcing and sinking |
| VIO (input offset) | — | 1 | 15 | mV | VICM = VCC/2 |
| ICC (both channels, IO=0) | — | 5 | 15 | mA | Normal operation |
| ICC (shutdown) | — | 0.5 | — | mA | OTF = 0 V |
| VICM (VCC = 5 V) | 0.2 | — | VCC−1.2 | V | — |
| OTF threshold | 157 | 165 | 175 | °C | Junction temperature; shutdown |
| TJ operating | −40 | — | 150 | °C | — |
| TA operating | −40 | — | 125 | °C | — |
| θJA (PWP/HTSSOP-14) | — | 46.5 | — | °C/W | — |
| ESD HBM (DRR) | — | — | ±2000 | V | — |
| ESD CDM (DRR) | — | — | ±750 | V | — |

### Application Notes

- **VCC_O(x):** Can be set lower than VCC to reduce output swing and on-chip power dissipation.
- **OTF/SH_DN (pin 3):** Requires external pull-up resistor to observe temperature flag; typical 2.5 kΩ to 5 V. Can also be used as a shutdown input (drive LOW to disable).
- **NC pins (HTSSOP pins 7, 8):** Do NOT connect — no internal connection.
- **GND (pin 14):** Must be connected.
- **Exposed pad:** Connect to GND; must not be connected to any other potential.

### Layout Notes

- Exposed pad: solder to board GND with thermal vias for heat spreading.
- VCC and VCC_O(x): place 100 nF bypass ceramic close to each supply pin.

### Project Usage Notes

> **[ESH10000540 R3]:** U14 (ALM2402QPWPRQ1, HTSSOP-14). NC pins 7 and 8 appear in netlist unconnected list — confirmed acceptable per datasheet.

---

## TPS259474

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** TPS259474LRPW (QFN-10); TPS259474ARPW (auto-retry variant)  
**Package:** QFN-10 (RPW HotRod), 2×2 mm, 0.45 mm pitch  
**Description:** 2.7V–23V, 5.5A, 28 mΩ True Reverse-Current Blocking eFuse — Adjustable OVLO, Circuit Breaker  
**Datasheet:** SLVSFC9B, October 2020 – Revised March 2022 (Texas Instruments)

**Device variant in use:** TPS259474LRPW — Adjustable OVLO | Circuit Breaker | **Latch-Off** fault response

### Device Comparison (TPS25947xx family)

| Part | OV Response | OC Response | Pin 3 | Pin 4 | Fault |
|------|-------------|-------------|-------|-------|-------|
| TPS259470ARPW | Adj. OVLO | Active Current Limit | AUXOFF | FLT | Auto-Retry |
| TPS259470LRPW | Adj. OVLO | Active Current Limit | AUXOFF | FLT | Latch-Off |
| TPS259472ARPW | Pin-sel. OVC | Active Current Limit | PG | PGTH | Auto-Retry |
| TPS259472LRPW | Pin-sel. OVC | Active Current Limit | PG | PGTH | Latch-Off |
| **TPS259474ARPW** | **Adj. OVLO** | **Circuit Breaker** | **PG** | **PGTH** | **Auto-Retry** |
| **TPS259474LRPW** | **Adj. OVLO** | **Circuit Breaker** | **PG** | **PGTH** | **Latch-Off** |

### Pin Functions — QFN-10 RPW (Top View)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | EN/UVLO | AI | Active HIGH enable; resistor divider sets UVLO; **do not leave floating** |
| 2 | OVLO | AI | Adjustable overvoltage lockout; resistor divider from IN to GND; **do not leave floating** |
| 3 | PG | DO | Power Good (open-drain HIGH when powerpath fully ON and PGTH threshold met) |
| 4 | PGTH | AI | Power Good threshold input |
| 5 | IN | PWR | Power input |
| 6 | OUT | PWR | Power output |
| 7 | dVdt | AO | Capacitor to GND sets output slew rate; float for fastest slew |
| 8 | GND | GND | Ground reference for all internal circuits |
| 9 | ILM | AO | Dual: RILM to GND sets current limit threshold; pin voltage monitors load current; **do not float** |
| 10 | ITIMER | AO | Capacitor to GND sets overcurrent blanking interval; leave open for fastest OCP response |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VIN range | 2.7 | — | 23 | V | Operating; abs max 28 V |
| IOUT (max continuous, TJ ≤ 125°C) | — | — | 5.5 | A | — |
| RON (back-to-back FETs) | — | 28.3 | — | mΩ | Typ. at 25°C |
| ILIM range | 0.5 | — | 6 | A | ±10% for ILIM > 1 A |
| RILM range | 549 | — | 6650 | Ω | — |
| IQ (ON state) | — | 428–610 | — | µA | — |
| IQ (disabled) | — | 73 | 130 | µA | — |
| TJ operating | −40 | — | 125 | °C | — |
| θJA (JEDEC 4-layer) | — | 74.5 | — | °C/W | — |
| ESD HBM | — | — | ±2000 | V | ANSI/ESDA/JEDEC JS-001 |
| ESD CDM | — | — | ±500 | V | ANSI/ESDA/JEDEC JS-002 |

### Application Notes

- **EN/UVLO (pin 1):** Do NOT leave floating. Tie to VIN via ≥350 kΩ for simple enable at VIN ≤ 5 V; use resistor divider for adjustable UVLO.
- **OVLO (pin 2):** Do NOT leave floating. Use resistor divider from IN to GND to set OV lockout threshold.
- **ILM (pin 9):** Do NOT leave floating. External RILM to GND sets current limit; pin also serves as analog current monitor output.
- **ITIMER (pin 10):** Capacitor to GND extends blanking window before OCP action. Leave open for fastest response.
- **dVdt (pin 7):** Capacitor to GND controls slew rate. Float for fastest turn-on.
- **PG (pin 3):** Open-drain; requires external pull-up. HIGH = powerpath fully ON.
- **Latch-Off (LRPW):** Fault latches device off; must cycle EN pin to restart.
- **UL 2367:** RILM must be ≥ 750 Ω.

### Project Usage Notes

> **[ESH10000540 R3]:** U8 (eFuse on 3V3_EXT rail), U9 (12V_EXT), U10 (5V_LIM), U11 (3V3_LIM), U13 (6V5_LIM). Each instance has dedicated EN (_EN net), PG (_PG net), and ILM nets. TPS259474LRPW — latch-off on fault. DIV nets (_DIV) are the OVLO resistor divider sense nodes.

---

## AD5593R

**Manufacturer:** Analog Devices  
**Mfr Part Number:** AD5593RBRUZ (TSSOP-16); also AD5593RBCPZ (LFCSP-16)  
**Package:** TSSOP-16 (RU-16), 4.4 mm body width  
**Description:** 8-Channel 12-Bit Configurable ADC/DAC with On-Chip 2.5 V Reference, GPIO, and I2C Interface  
**Datasheet:** AD5593R Rev. H (Analog Devices)

### Pin Functions — TSSOP-16 (RU-16)

| Pin | Name | Description |
|-----|------|-------------|
| 1 | RESET | Asynchronous reset; tie HIGH for normal operation; falling edge resets all registers and I/O config to defaults (250 µs recovery) |
| 2 | A0 | Address bit 0; sets LSB of 7-bit slave address |
| 3 | VDD | Power supply (2.7–5.5 V); decouple with 0.1 µF ceramic to GND |
| 4–7 | I/O0–I/O3 | Configurable I/O (ADC input / DAC output / GPIO input or output) |
| 8 | VREF | Reference I/O; internal 2.5 V when enabled; or external ref 1 V–VDD; decouple with 100 nF to GND |
| 9 | VLOGIC | Interface supply for SDA/SCL logic levels (1.8 V to VDD) |
| 10–13 | I/O4–I/O7 | Configurable I/O (ADC input / DAC output / GPIO input or output) |
| 14 | GND | Ground |
| 15 | SDA | I2C serial data (open-drain; pull-up to VLOGIC) |
| 16 | SCL | I2C serial clock (open-drain; pull-up to VLOGIC) |

### I2C Address

Fixed prefix 0b0010_0x0, where x = A0 pin:
- A0 = GND → 7-bit address **0x10**
- A0 = VDD → 7-bit address **0x11**

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VDD range | 2.7 | — | 5.5 | V | — |
| VLOGIC range | 1.8 | — | VDD | V | Sets I2C logic levels |
| ADC resolution | — | 12 | — | bits | — |
| DAC resolution | — | 12 | — | bits | — |
| ADC INL | −2 | — | +2 | LSB | — |
| DAC INL | −1 | — | +1 | LSB | — |
| ADC conversion time | — | 2 | — | µs | — |
| ADC SNR (VDD=2.7V, 0–VREF) | — | 69 | — | dB | — |
| VREF (internal) | 2.495 | 2.500 | 2.505 | V | 20 ppm/°C temp coeff |
| VREF output current | — | — | ±5 | mA | VDD ≥ 3 V |
| DAC output range | 0 | — | VREF or 2×VREF | V | Shared range bit |
| GPIO I/O current | — | — | 1.6 | mA | Source and sink |
| IDD (normal, all DAC, VDD=5V) | — | 1.6 | — | mA | Internal ref, gain=2 |
| IDD (power-down) | — | 3.5 | — | µA | — |
| Temperature | −40 | — | +105 | °C | — |
| ESD HBM | — | — | 500 | V | TSSOP |
| ESD CDM | — | — | 1250 | V | TSSOP (FICDM) |
| θJA (TSSOP-16) | — | 127 | — | °C/W | — |

### Application Notes

- **I/O pins default state:** GPIO with internal 85 kΩ pull-down to GND at power-up and after RESET.
- **RESET pin:** Tie HIGH for normal operation. Falling edge resets all configuration registers and I/O to defaults; takes up to 250 µs — do not write data during this period.
- **Internal reference:** Powered down by default; enable via power-down/reference control register (Bit 9 = 1). Voltage appears on VREF pin; buffer before use elsewhere in system.
- **VREF decoupling:** 100 nF ceramic to GND when using internal reference for specified performance.
- **External reference:** Connect to VREF pin; range 1 V to VDD.
- **I/O pin function:** Each pin independently configured via ADC/DAC/GPIO configuration registers. DAC and ADC range bits are shared across all channels (cannot mix 0–VREF and 0–2×VREF on the same device).
- **Temperature indicator:** Built-in die temperature sensor readable via ADC sequence; accuracy ±3°C; not production tested.

### Layout Notes

- Place 0.1 µF bypass at VDD (pin 3) and 100 nF at VREF (pin 8) close to device.
- Keep I/Ox analog traces short and away from switching noise sources.
- Use ground plane under device.

### Project Usage Notes

> **[ESH10000540 R3]:** U5, U6 (AD5593R, TSSOP-16). SDA (pin 15) on SDA bus; SCL (pin 16) on SCL bus. A0 determines I2C address per instance. VREF connected to VREF net (REF3425 2.5 V output). VLOGIC = 3V3 (confirmed). RESET tied HIGH for normal operation.

---

## SN74HCS32

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** SN74HCS32PWR (TSSOP-14)  
**Description:** Quadruple 2-Input OR Gate with Schmitt-Trigger Inputs  
**Datasheet:** SN74HCS32 datasheet, Texas Instruments (ti.com/lit/ds/symlink/sn74hcs32.pdf)

### Pin Functions (TSSOP-14)

| Pin | Name | Type | Function |
|-----|------|------|----------|
| 1 | 1A | I | Gate 1 input A |
| 2 | 1B | I | Gate 1 input B |
| 3 | 1Y | O | Gate 1 output (1A OR 1B) |
| 4 | 2A | I | Gate 2 input A |
| 5 | 2B | I | Gate 2 input B |
| 6 | 2Y | O | Gate 2 output (2A OR 2B) |
| 7 | GND | PWR | Ground |
| 8 | 3Y | O | Gate 3 output (3A OR 3B) |
| 9 | 3A | I | Gate 3 input A |
| 10 | 3B | I | Gate 3 input B |
| 11 | 4Y | O | Gate 4 output (4A OR 4B) |
| 12 | 4A | I | Gate 4 input A |
| 13 | 4B | I | Gate 4 input B |
| 14 | VCC | PWR | Positive supply (2–6 V) |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC | 2 | — | 6 | V | — |
| VI | 0 | — | VCC | V | Input voltage range |
| IOH | — | — | −6 | mA | At VCC = 4.5 V |
| IOL | — | — | 6 | mA | At VCC = 4.5 V |
| VOH (IOH = −20 µA) | VCC − 0.1 | — | — | V | Min high-level output |
| VOL (IOL = 20 µA) | — | 0.002 | — | V | Typ low-level output |
| tpd (VCC = 3.3 V, CL = 50 pF) | — | — | 18 | ns | Propagation delay |
| tpd (VCC = 4.5 V, CL = 50 pF) | — | 13 | — | ns | Typical |
| IQ | — | — | 2 | µA | Quiescent current |
| Temperature | −40 | — | +125 | °C | — |

### Application Notes

- **Unused inputs:** All unused inputs must be tied to VCC or GND — must not float. A 10 kΩ pull-up or pull-down resistor is acceptable if the input may be driven later.
- **Schmitt-trigger inputs:** Input hysteresis (~0.9 V at 3.3 V) provides noise immunity; safe for slowly-transitioning signals.
- **Output loading:** CMOS outputs; do not exceed IOH/IOL limits to maintain valid output levels.

### Layout Notes

- Bypass 100 nF ceramic at VCC (pin 14) to GND (pin 7).
- Keep output traces short to minimise capacitive loading and maintain tpd specification.

### Project Usage Notes

> **[ESH10000540 R3]:** U28 (SN74HCS32PWR, TSSOP-14). VCC = 3V3. Implements combinational OR logic for SR-latch set/reset generation: gate outputs drive Set and CLR inputs of 74HCS74 D flip-flops (U25, U26) used as latches for audio load switching (phantom/bias load control). All four gate inputs are driven by logic signals from U7 (PCA9506) and U25/U38 (74HCS86).

---

## KAQY214

**Manufacturer:** COSMO Electronics Corporation  
**Mfr Part Number:** KAQY214STLD (SOP-4)  
**Description:** 400 V / 130 mA Normally-Open PhotoMOS Solid State Relay  
**Datasheet:** KAQY214 datasheet, COSMO Electronics (cosmo-ic.com/upload/product/KAQY214.PDF)

### Pin Functions (SOP-4)

| Pin | Name | Side | Function |
|-----|------|------|---------|
| 1 | A+ | Input | LED anode — control current input |
| 2 | A− | Input | LED cathode — control current return |
| 3 | L1 | Output | MOSFET switch terminal 1 |
| 4 | L2 | Output | MOSFET switch terminal 2 |

Device is a 1-Form-A (normally open) switch: pins 3–4 are open when IF = 0; close when IF ≥ IFT.

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| LED forward voltage (VF) | — | 1.2 | 1.5 | V | At IF = 5 mA |
| LED forward current (IF) max | — | — | 50 | mA | Continuous |
| LED peak forward current (IFP) | — | — | 1 | A | Pulsed |
| LED reverse voltage max | — | — | 5 | V | — |
| Output blocking voltage (VOFF) | 400 | — | — | V | AC or DC |
| Output on-current (ION) max | — | — | 130 | mA | Continuous |
| Output on-resistance (RON) | — | 30 | — | Ω | IF=10 mA, IL=100 mA, VL=20 V |
| Output leakage (ILEAK) | — | 0.1 | — | mA | VL=400 V, IF=0 |
| Turn-on time (TON) | — | 1.0 | — | ms | IF=10 mA, VL=20 V, IL=100 mA |
| Turn-off time (TOFF) | — | 1.0 | — | ms | Same conditions |
| Isolation voltage (KAQY214) | 5000 | — | — | Vrms | Input–output |
| Isolation resistance (Riso) | 10¹⁰ | — | — | Ω | Vio = 500 V |
| Operating temperature | −40 | — | +85 | °C | — |

### Application Notes

- **Control current:** LED must be forward biased (pin 1 = anode, pin 2 = cathode). Typical control current 5–10 mA; limit with series resistor from drive signal to pin 1.
- **Output polarity:** Pins 3 and 4 are bidirectional — relay switches both AC and DC loads.
- **RON:** 30 Ω on-resistance is significant for low-voltage signal switching; include in signal path budget.
- **No snubber required:** Internal MOSFET handles inductive switching; no external clamp needed for resistive/capacitive loads within ratings.
- **Isolation:** KAQY214 variant has 5000 Vrms isolation; KAQY214S variant has 1500 Vrms — verify suffix when ordering.

### Layout Notes

- Keep input (LED) loop compact to minimise radiated emission from switching transient.
- Output pins 3–4 must be rated for load current on PCB copper; 130 mA requires ≥ 0.2 mm trace at 1 oz Cu.
- Maintain creepage/clearance between input and output pads per isolation rating.

### Project Usage Notes

> **[ESH10000540 R3]:** U30–U37 (KAQY214STLD, SOP-4). Eight relay instances used as analog switches on the AGND domain. Pin 2 (LED cathode) → GND; pin 1 (LED anode) driven by control signals (e.g. PHANTOM_LOAD_L_RES, MIC_BIAS_LOAD_L_RES) from logic circuitry. Pin 3 (L1) → AGND; pin 4 (L2) → individual load nets (U30_LOAD, U31_LOAD, U32_LOAD etc.) via series resistors. Used to switch audio phantom power and microphone bias loads.

---

## G20N06D52

**Manufacturer:** Goford Semiconductor (gofordsemi.com)  
**Mfr Part Number:** G20N06D52  
**Package:** DFN5×6-8L Dual (8-lead, 5 mm × 6 mm); contains two independent N-ch MOSFETs  
**Category:** IC — Power / MOSFET (N-channel, dual)  
**Datasheet:** G20N06D52, Goford Semiconductor, Rev. A1505  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

N-channel enhancement mode power MOSFET using trench technology. Two independent MOSFETs in one DFN5×6-8L package. 60 V VDS, 20 A continuous drain current, 30 mΩ RDS(ON) typical. Suitable for power switching and DC/DC converter applications.

### Pin Description (DFN5×6-8L Dual)

> **Note:** The pin assignment diagram in the datasheet is a graphical image and could not be extracted as text. Verify exact pin-to-gate/source/drain mapping against the datasheet figure or the PCB footprint. Typical dual-MOSFET DFN8 assigns pins 1–4 to one MOSFET and pins 5–8 to the second, with separate G/S/D per device and a shared exposed pad (drain or thermal) on the back.

| Pin Group | Typical Assignment | Notes |
|-----------|--------------------|-------|
| Pins 1–4 | MOSFET 1: G1, S1, S1, S1 (or variant) | Verify from datasheet figure |
| Pins 5–8 | MOSFET 2: D2, D2, G2, S2 (or variant) | Verify from datasheet figure |
| Exposed pad | Drain (common) or thermal only | Verify — may be shared drain |

### Key Electrical Parameters

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|-----------|--------|-----|-----|-----|------|------------|
| Drain-source voltage | VDS | — | — | 60 | V | — |
| Continuous drain current | ID | — | — | 20 | A | TC=25°C |
| Pulsed drain current | IDM | — | — | 80 | A | Pulse-limited by TJ |
| Gate-source voltage | VGS | — | — | ±20 | V | |
| Power dissipation | PD | — | — | 48 | W | TC=25°C |
| Single-pulse avalanche energy | EAS | — | — | 36 | mJ | Tj=25°C, VDD=50V, L=0.5mH |
| Drain-source breakdown voltage | V(BR)DSS | 60 | — | — | V | VGS=0V, ID=250µA |
| Zero-gate drain current | IDSS | — | — | 1 | µA | VDS=60V, VGS=0V |
| Gate-source leakage | IGSS | — | — | ±100 | nA | VGS=±20V |
| Gate threshold voltage | VGS(th) | 1.0 | 1.5 | 2.5 | V | VDS=VGS, ID=250µA |
| On-resistance | RDS(ON) | — | 26 | 30 | mΩ | VGS=10V, ID=10A |
| On-resistance | RDS(ON) | — | 30 | 40 | mΩ | VGS=4.5V, ID=10A |
| Transconductance | gFS | — | 11 | — | S | VGS=5V, ID=10A |
| Input capacitance | Ciss | — | 1326 | — | pF | VGS=0V, VDS=30V, f=1MHz |
| Output capacitance | Coss | — | 55 | — | pF | Same conditions |
| Reverse transfer capacitance | Crss | — | 51 | — | pF | Same conditions |
| Total gate charge | Qg | — | 25 | — | nC | VDD=30V, ID=10A, VGS=10V |
| Gate-source charge | Qgs | — | 4.5 | — | nC | |
| Gate-drain charge | Qgd | — | 6.5 | — | nC | |
| Turn-on delay | td(on) | — | 5 | — | ns | VDD=30V, ID=10A, RG=3Ω |
| Turn-on rise time | tr | — | 2.6 | — | ns | |
| Turn-off delay | td(off) | — | 16 | — | ns | |
| Turn-off fall time | tf | — | 2.3 | — | ns | |
| Body diode current | IS | — | — | 20 | A | TC=25°C |
| Body diode forward voltage | VSD | — | — | 1.2 | V | ISD=10A, VGS=0V |
| Reverse recovery charge | Qrr | — | 49 | — | nC | IF=10A, di/dt=100A/µs |
| Reverse recovery time | Trr | — | 29 | — | ns | |
| Thermal res. junction-ambient | RthJA | — | — | 50 | °C/W | |
| Thermal res. junction-case | RthJC | — | — | 2.6 | °C/W | |
| Operating junction temperature | TJ | −55 | — | 150 | °C | |

### Application Notes

- **Dual package:** Two independent MOSFETs share one DFN5×6-8L package. Each MOSFET has its own G/S/D. Confirm which MOSFET instance is used for Q1 in the schematic.
- **Gate drive:** Full enhancement at VGS=10V (26 mΩ typ). Logic-level operation possible at VGS=4.5V (30 mΩ typ) — confirm drive voltage in design.
- **VGS(th)=1–2.5V:** Ensure gate drive is above 2.5V max threshold plus margin for reliable turn-on.
- **Body diode** is present and has significant Qrr (49 nC) — relevant if used in synchronous rectification or H-bridge configurations.
- **Avalanche rated:** 36 mJ single-pulse avalanche energy (EAS).
- Exposed pad thermal connection is critical for rated PD; solder to PCB copper.

### Project Usage Notes

> **[ESH10000535 R3]:** Q1 (G20N06D52). Power switch or DC/DC element. Gate drive voltage, rail connection, and which of the two FET instances is used must be confirmed in schematic review (ERC-C08/P06/D).

---

## PS509LEX

**Manufacturer:** Diodes Incorporated  
**Mfr Part Number:** PS509LEX (TSSOP-16)  
**Package:** TSSOP-16 (L suffix)  
**Category:** IC — Analog Switch / Multiplexer  
**Datasheet:** PS508/PS509, DS41784 Rev 2-2, Diodes Incorporated, June 2020  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

Differential 4:1 (or dual single-ended 4:1) precision CMOS analog multiplexer. Operates with dual supplies ±5 V to ±18 V or single supply 10 V–36 V. Rail-to-rail switching, break-before-make action.

### Pin Description (PS509, TSSOP-16 — top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | A0 | I | Address bit 0 |
| 2 | EN | I | Enable, active HIGH. LOW = all channels off. |
| 3 | VSS | Pwr | Negative supply (most negative potential) |
| 4 | S1A | I/O | Source 1A (channel 1, differential half A) |
| 5 | S2A | I/O | Source 2A |
| 6 | S3A | I/O | Source 3A |
| 7 | S4A | I/O | Source 4A |
| 8 | DA | I/O | Drain A (common output, differential half A) |
| 9 | DB | I/O | Drain B (common output, differential half B) |
| 10 | S4B | I/O | Source 4B |
| 11 | S3B | I/O | Source 3B |
| 12 | S2B | I/O | Source 2B |
| 13 | S1B | I/O | Source 1B |
| 14 | VDD | Pwr | Positive supply (most positive potential) |
| 15 | GND | Pwr | Ground (0 V reference) |
| 16 | A1 | I | Address bit 1 |

**Truth table (PS509):**

| EN | A1 | A0 | Channels closed |
|----|----|----|-----------------|
| 0 | X | X | All off |
| 1 | 0 | 0 | S1A–DA and S1B–DB |
| 1 | 0 | 1 | S2A–DA and S2B–DB |
| 1 | 1 | 0 | S3A–DA and S3B–DB |
| 1 | 1 | 1 | S4A–DA and S4B–DB |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VDD (dual) | ±5 | — | ±18 | V | Dual supply |
| VDD (single) | 10 | — | 36 | V | Single supply |
| RON | — | 125 | — | Ω | Typical on-resistance |
| CON | — | 20 | — | pF | On-capacitance |
| Charge injection | — | 0.9 | — | pC | |
| Input leakage | — | 30 | — | pA | |
| Transition time | — | 171 | — | ns | Break-before-make |
| IDD (supply current) | — | 135 | — | µA | |
| Logic threshold VIH | 2 | — | VDD | V | TTL-compatible |
| Analog signal range | VSS−2 | — | VDD+2 | V | Signal pins |
| ESD (HBM) | — | — | 2000 | V | ANSI/ESDA/JEDEC JS-001 |
| Operating temp | −40 | — | +125 | °C | |

### Application Notes

- Decouple VDD and VSS each with 0.1 µF–10 µF ceramic to GND near the device.
- EN pin can be tied to VDD to permanently enable the device.
- Logic inputs (A0, A1, EN) are TTL-compatible when within the valid supply range; no special level shift needed when driven from 3.3 V with VDD ≥ 5 V.
- Break-before-make ensures no two channels overlap during address transitions.
- Unused SxA/SxB pins may be left floating; unused DA/DB must not be left floating — connect to a defined potential or through a pull resistor.

### Project Usage Notes

> **[ESH10000535 R3]:** U2, U3, U12, U25 (PS509LEX). Configured as 4:1 differential multiplexers. VDD=+18V, VSS=−18V. Used to switch analog measurement channels. A0, A1 address inputs driven from MCU/IO expander.

---

## SN74LVC126APW

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** SN74LVC126APW (TSSOP-14)  
**Package:** TSSOP-14 (PW)  
**Category:** IC — Logic / Buffer (3-state, active-HIGH OE)  
**Datasheet:** SN74LVC126A, SCAS339U, Texas Instruments, Revised July 2024  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

Quadruple bus buffer gate with 3-state outputs. Each channel has an independent active-HIGH output-enable (OE) — output is enabled when OE is HIGH; output is high-Z when OE is LOW. VCC 1.65 V–3.6 V, inputs accept up to 5.5 V.

### Pin Description (TSSOP-14, top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | 1OE | I | Channel 1 output enable, active HIGH |
| 2 | 1A | I | Channel 1 input |
| 3 | 1Y | O/Z | Channel 1 output (3-state) |
| 4 | 2OE | I | Channel 2 output enable, active HIGH |
| 5 | 2A | I | Channel 2 input |
| 6 | 2Y | O/Z | Channel 2 output (3-state) |
| 7 | GND | — | Ground |
| 8 | 3Y | O/Z | Channel 3 output (3-state) |
| 9 | 3A | I | Channel 3 input |
| 10 | 3OE | I | Channel 3 output enable, active HIGH |
| 11 | 4Y | O/Z | Channel 4 output (3-state) |
| 12 | 4A | I | Channel 4 input |
| 13 | 4OE | I | Channel 4 output enable, active HIGH |
| 14 | VCC | — | Supply voltage |

**Function:** OE=H → Y=A (non-inverting). OE=L → Y=Hi-Z.

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC | 1.65 | — | 3.6 | V | Operating |
| VI (input) | — | — | 5.5 | V | 5.5 V tolerant inputs |
| IOH | — | — | −12 | mA | At VCC=3.3 V |
| IOL | — | — | 12 | mA | At VCC=3.3 V |
| tpd (3.3 V) | — | — | 4.7 | ns | A→Y propagation |
| ICC (static) | — | — | 10 | µA | VI=VCC or GND |
| Operating temp | −40 | — | +125 | °C | |

### Application Notes

- To ensure the output is high-Z at power-up, tie OE to GND through a pull-down resistor (the input must not float).
- Do not allow input pins to float; undefined logic levels cause excessive ICC.
- **OE active-HIGH distinguishes 126A from 125A (active-LOW).** Verify the part number before using in mixed OE-polarity designs.

### Project Usage Notes

> **[ESH10000535 R3]:** U4, U5 (SN74LVC126APW). Used as bus buffers on D-SPI and U-SPI external interfaces. OE signals driven by MCU or IO expander to enable/disable SPI bus segments.

---

## SN74LVC125APW

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** SN74LVC125APW (TSSOP-14)  
**Package:** TSSOP-14 (PW)  
**Category:** IC — Logic / Buffer (3-state, active-LOW OE)  
**Datasheet:** SN74LVC125A, Texas Instruments  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

Quadruple bus buffer gate with 3-state outputs. Each channel has an independent active-LOW output-enable (OE\) — output is enabled when OE\ is LOW; output is high-Z when OE\ is HIGH. VCC 1.65 V–3.6 V, inputs accept up to 5.5 V.

### Pin Description (TSSOP-14, top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | 1OE\ | I | Channel 1 output enable, active LOW |
| 2 | 1A | I | Channel 1 input |
| 3 | 1Y | O/Z | Channel 1 output (3-state) |
| 4 | 2OE\ | I | Channel 2 output enable, active LOW |
| 5 | 2A | I | Channel 2 input |
| 6 | 2Y | O/Z | Channel 2 output (3-state) |
| 7 | GND | — | Ground |
| 8 | 3Y | O/Z | Channel 3 output (3-state) |
| 9 | 3A | I | Channel 3 input |
| 10 | 3OE\ | I | Channel 3 output enable, active LOW |
| 11 | 4Y | O/Z | Channel 4 output (3-state) |
| 12 | 4A | I | Channel 4 input |
| 13 | 4OE\ | I | Channel 4 output enable, active LOW |
| 14 | VCC | — | Supply voltage |

**Function:** OE\=L → Y=A (non-inverting). OE\=H → Y=Hi-Z.

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC | 1.65 | — | 3.6 | V | Operating |
| VI (input) | — | — | 5.5 | V | 5.5 V tolerant |
| IOH | — | — | −12 | mA | At VCC=3.3 V |
| IOL | — | — | 12 | mA | At VCC=3.3 V |
| tpd (3.3 V) | — | — | 4.8 | ns | A→Y propagation |
| ICC (static) | — | — | 10 | µA | |
| Operating temp | −40 | — | +125 | °C | |

### Application Notes

- To ensure output is high-Z at power-up, OE\ must be tied HIGH through a pull-up resistor.
- **OE active-LOW distinguishes 125A from 126A (active-HIGH).**
- Inputs must not float.

### Project Usage Notes

> **[ESH10000535 R3]:** U6, U7 (SN74LVC125APW). Used as bus buffers on U-SPI and UART external interfaces. OE\ driven LOW by MCU or IO expander to enable the buffer; HIGH disables (high-Z).

---

## SN74LVC07APW

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** SN74LVC07APW (TSSOP-14)  
**Package:** TSSOP-14 (PW)  
**Category:** IC — Logic / Buffer (open-drain outputs)  
**Datasheet:** SN74LVC07A, SCAS595W, Texas Instruments, October 1997 – Revised October 2016  
**Added:** 2026-05-04  
**Used in:** ESH10000543 R2

Hex buffer and driver with open-drain outputs. No output-enable pin — outputs are always active. VCC 1.65 V–5.5 V; inputs and outputs accept up to 5.5 V. Requires external pull-up resistors on all output nets.

### Pin Description (TSSOP-14, top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | 1A | I | Input 1 |
| 2 | 1Y | O (OD) | Open-drain output 1 |
| 3 | 2A | I | Input 2 |
| 4 | 2Y | O (OD) | Open-drain output 2 |
| 5 | 3A | I | Input 3 |
| 6 | 3Y | O (OD) | Open-drain output 3 |
| 7 | GND | — | Ground |
| 8 | 4Y | O (OD) | Open-drain output 4 |
| 9 | 4A | I | Input 4 |
| 10 | 5Y | O (OD) | Open-drain output 5 |
| 11 | 5A | I | Input 5 |
| 12 | 6Y | O (OD) | Open-drain output 6 |
| 13 | 6A | I | Input 6 |
| 14 | VCC | — | Supply voltage |

**Function:** Non-inverting buffer. A=H → Y pulls to GND (LOW). A=L → Y is high-Z (open drain — output must be pulled up externally).

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC | 1.65 | — | 5.5 | V | Operating |
| VI (input) | — | — | 5.5 | V | 5.5 V tolerant |
| IOL | — | 24 | — | mA | At VCC=3.3 V |
| tpd (3.3 V) | — | — | 5.5 | ns | A→Y propagation |
| Operating temp | −40 | — | +125 | °C | |

### Application Notes

- **Open-drain outputs require external pull-up resistors** on every output net that must be pulled HIGH. Omitting a pull-up leaves the net floating when the output is high-Z.
- **Unused inputs must be tied to VCC or GND** — datasheet states: "All unused inputs of the device must be held at VCC or GND to ensure proper device operation." Do not leave any input pin floating.
- VCC bypass capacitor required: 0.1 µF recommended.
- Outputs are 5.5 V tolerant — pull-up rail may be higher than VCC, enabling level translation up to 5.5 V.

### Project Usage Notes

> **[ESH10000543 R2]:** U7 (SN74LVC07APW). Used as open-drain buffer/driver.

---

## LTC3265EDHC

**Manufacturer:** Analog Devices (formerly Linear Technology)  
**Mfr Part Number:** LTC3265EDHC (18-lead DFN, 5 mm × 3 mm)  
**Package:** DFN-18 (DHC), 5 mm × 3 mm × 0.75 mm, exposed pad = GND  
**Category:** IC — Power / Charge Pump + LDO  
**Datasheet:** LTC3265, 3265fa, Linear Technology / Analog Devices  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

Low-noise dual bipolar supply: boost charge pump (×2 positive) + inverting charge pump (×−1 negative), each followed by an LDO post-regulator. Generates adjustable ±outputs from a single positive input. Up to 50 mA per LDO. Supports Burst Mode (low quiescent) or constant-frequency (low noise) operation.

### Pin Description (DFN-18 — pin numbers for DFN package)

| Pin | Name | Description |
|-----|------|-------------|
| 1 | CBST− | Boost charge pump flying capacitor, negative connection |
| 2 | CBST+ | Boost charge pump flying capacitor, positive connection |
| 3 | VIN\_P | Input supply for boost charge pump (4.5 V–16 V). Bypass with ceramic cap. |
| 4 | EN− | Active-HIGH enable for inverting charge pump and LDO−. Do not float. |
| 5 | BYP− | LDO− reference bypass. Connect 100 nF to GND to reduce output noise; leave floating if unused. |
| 6 | ADJ− | Feedback for LDO−. Servos to −1.2 V when loop is closed. |
| 7 | LDO− | Negative LDO output. Requires ≥2 µF low-ESR output cap to GND. |
| 8 | VOUT− | Inverting charge pump output (= −VIN\_N in constant-frequency mode). |
| 9 | CINV− | Inverting charge pump flying capacitor, positive connection |
| 10 | CINV+ | Inverting charge pump flying capacitor, negative connection |
| 11 | VIN\_N | Input for inverting charge pump (4.5 V–32 V). Tie to VIN\_P or VOUT+ per application. Bypass with ceramic cap. |
| 12 | RT | Frequency programming input (servos to 1.2 V when enabled). Resistor to GND sets fSW; tie to GND for 500 kHz fixed. |
| 13 | EN+ | Active-HIGH enable for boost charge pump and LDO+. Do not float. |
| 14 | MODE | Charge pump mode: HIGH = Burst Mode (low Iq, higher ripple); LOW = constant frequency (low noise). Do not float. |
| 15 | BYP+ | LDO+ reference bypass. Connect 100 nF to GND; leave floating if unused. |
| 16 | ADJ+ | Feedback for LDO+. Servos to +1.2 V when loop is closed. |
| 17 | LDO+ | Positive LDO output. Requires ≥2 µF low-ESR output cap to GND. |
| 18 | VOUT+ | Boost charge pump output (= 2×VIN\_P in constant-frequency mode). |
| 19 (EP) | GND | Exposed pad. Must be soldered to PCB ground plane. |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VIN\_P | 4.5 | — | 16 | V | Boost charge pump input |
| VIN\_N | 4.5 | — | 32 | V | Inverting charge pump input |
| VOUT+ (const. freq) | — | 2×VIN\_P | — | V | Boost output |
| VOUT+ (Burst Mode) | — | 0.94×2×VIN\_P | — | V | Regulated in Burst Mode |
| VOUT− (const. freq) | — | −VIN\_N | — | V | Inverting output |
| VOUT− (Burst Mode) | — | −0.94×VIN\_N | — | V | Regulated in Burst Mode |
| ILDO+ max | — | — | 50 | mA | LDO+ output current |
| ILDO− max | — | — | 50 | mA | LDO− output current |
| ADJ+ reference | — | 1.200 | — | V | LDO+ feedback voltage |
| ADJ− reference | — | −1.200 | — | V | LDO− feedback voltage |
| LDO− dropout | — | — | 500 | mV | At ILDO− = −50 mA |
| Quiescent current (Burst Mode) | — | 135 | — | µA | Both LDOs on |
| Shutdown current | — | 3 | — | µA | EN+ and EN− both LOW |
| fSW (programmable) | 50 | — | 500 | kHz | Via RT resistor |
| fSW (RT = GND) | — | 500 | — | kHz | Fixed 500 kHz |
| EN threshold HIGH | 1.1 | — | — | V | Rising threshold |
| EN threshold LOW | — | — | 1.0 | V | Falling threshold |
| Operating temp (E grade) | −40 | — | +125 | °C | Junction |

### Output Voltage Setting

For LDO+: VLDO+ = 1.2 V × (1 + R1/R2), where R1 from LDO+ to ADJ+ and R2 from ADJ+ to GND.  
For LDO−: VLDO− = −1.2 V × (1 + R3/R4), where R3 from LDO− to ADJ− and R4 from ADJ− to GND.

VIN\_N configuration:
- Tie VIN\_N = VOUT+: VOUT− = −2×VIN\_P → symmetric ±outputs.
- Tie VIN\_N = VIN\_P: VOUT− = −VIN\_P → asymmetric outputs.

### Application Notes

- **VOUT+ and VOUT−** are intermediate charge-pump output nodes, not external supply rails. LDO+ and LDO− are the regulated outputs.
- C2/C3 on VOUT+/VOUT− are optional filter capacitors and may be NM if ripple is acceptable.
- The exposed pad (GND) must be soldered down for thermal and electrical integrity.
- Place flying capacitors (CBST, CINV) and input bypass caps as close as possible to the device.
- Do not float EN+, EN−, or MODE pins.

### Project Usage Notes

> **[ESH10000535 R3]:** U8 (LTC3265EDHC). Generates ±18 V from 12 V input. VIN\_P=12 V, VIN\_N=VOUT+ (→VOUT−=−24 V? No — VIN\_N tied to VOUT+ → VOUT−=−2×VIN\_P=−24 V pre-LDO, LDO− regulated to −18 V). LDO+→+18V, LDO−→−18V. VOUT+ and VOUT− are internal nodes; C2 and C3 (NM) are optional filter caps on these nodes — NM is accepted per OI-03.

---

## AD5592R

**Manufacturer:** Analog Devices  
**Mfr Part Number:** AD5592R (16-lead TSSOP)  
**Package:** TSSOP-16; also available WLCSP-16, LFCSP-16  
**Category:** IC — Mixed-Signal / ADC/DAC/GPIO  
**Datasheet:** AD5592R, Rev. H, Analog Devices, July 2023  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

> **Note:** AD5592R uses SPI interface. The related AD5593R uses I2C — these are different parts. See separate AD5593R entry if needed.

8-channel, 12-bit configurable ADC/DAC with GPIO and integrated 2.5 V reference. Each I/O pin (I/O0–I/O7) is independently configurable as a 12-bit DAC output, 12-bit ADC input, digital output, or digital input. SPI interface up to 50 MHz (20 MHz for ADC operations). On-chip temperature sensor.

### Pin Description (TSSOP-16 — top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | RESET | I | Asynchronous reset, active LOW. Tie HIGH for normal operation. |
| 2 | SYNC | I | Frame sync / chip select, active LOW. |
| 3 | VDD | Pwr | Supply, 2.7 V–5.5 V |
| 4 | I/O0 | I/O | Configurable ADC/DAC/GPIO pin 0 |
| 5 | I/O1 | I/O | Configurable ADC/DAC/GPIO pin 1 |
| 6 | I/O2 | I/O | Configurable ADC/DAC/GPIO pin 2 |
| 7 | I/O3 | I/O | Configurable ADC/DAC/GPIO pin 3 |
| 8 | VREF | I/O | Reference I/O. Internal 2.5 V ref available here; or apply external ref (1 V–VDD). Bypass with 100 nF to GND. |
| 9 | SDO | O | Serial data output. Bits clocked out on rising SCLK edge. |
| 10 | I/O4 | I/O | Configurable ADC/DAC/GPIO pin 4 |
| 11 | I/O5 | I/O | Configurable ADC/DAC/GPIO pin 5 |
| 12 | I/O6 | I/O | Configurable ADC/DAC/GPIO pin 6 |
| 13 | I/O7 | I/O | Configurable ADC/DAC/GPIO pin 7. Also configurable as BUSY output. |
| 14 | GND | Pwr | Ground |
| 15 | SDI | I | Serial data input. Data clocked in on falling SCLK edge. |
| 16 | SCLK | I | Serial clock. Up to 50 MHz for DAC writes; max 20 MHz for ADC conversions. |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VDD | 2.7 | — | 5.5 | V | Operating |
| VREF (internal) | — | 2.5 | — | V | 20 ppm/°C drift |
| ADC resolution | — | 12 | — | bit | |
| ADC throughput | — | — | 400 | kSPS | |
| DAC output range | 0 | — | VREF or 2×VREF | V | Configurable |
| SCLK (DAC write) | — | — | 50 | MHz | |
| SCLK (ADC/readback) | — | — | 20 | MHz | |
| Operating temp | −40 | — | +125 | °C | Junction |

### Application Notes

- RESET must be tied HIGH; a low pulse resets all registers to default.
- VREF: bypass with ≥100 nF to GND for specified noise performance. Internal reference is off by default — enable via control register.
- I/O pins not configured as analog inputs should be driven to a valid logic level; floating I/O pins will pick up noise.
- I/O7 can be configured as a BUSY output to signal ongoing ADC conversions.
- SPI protocol is 16-bit frames: SYNC low → 16 SCLK falling edges for data in, rising edges for data out.

### Project Usage Notes

> **[ESH10000535 R3]:** U10, U22 (AD5592R). SPI interface on internal SPI bus (SCK/SCK\_R net). Used for analog measurement and/or control channels. VDD = 3V3 or 5VA (verify in schematic).

---

## PGA849

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** PGA849RGT (VQFN-16, 3 mm × 3 mm)  
**Package:** VQFN-16 (RGT), 3 mm × 3 mm, exposed thermal pad  
**Category:** IC — Analog / Instrumentation Amplifier  
**Datasheet:** PGA849, SBOSAG3A, Texas Instruments, March 2024 – December 2024  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

Low-noise, wide-bandwidth precision programmable gain instrumentation amplifier (InAmp). Differential to single-ended conversion. Eight pin-programmable binary gains: 1/8, 1/4, 1/2, 1, 2, 4, 8, 16 V/V (set by A2:A0 pins). Separate input-stage and output-stage supplies for isolation from downstream devices. Input overvoltage protection to ±40 V beyond supplies.

### Pin Description (VQFN-16 — top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | A2 | I | Gain select bit 2 (MSB) |
| 2 | IN+ | I | Non-inverting differential input |
| 3 | IN− | I | Inverting differential input |
| 4 | A0 | I | Gain select bit 0 (LSB) |
| 5 | A1 | I | Gain select bit 1 |
| 6 | VS+ | Pwr | Input-stage positive supply |
| 7 | LVDD | Pwr | Output-stage positive supply |
| 8 | NC | — | No connect |
| 9 | DA\_IN+ | I | Output difference amplifier summing node (+) |
| 10 | REF | I | Reference input (must be driven by low-impedance source) |
| 11 | OUT | O | Signal output |
| 12 | DA\_IN− | I | Output difference amplifier summing node (−) |
| 13 | NC | — | No connect |
| 14 | LVSS | Pwr | Output-stage negative supply |
| 15 | VS− | Pwr | Input-stage negative supply |
| 16 | DGND | Pwr | Ground reference for digital logic and gain-setting pins |
| EP | Thermal pad | Pwr | Must be soldered to PCB. Connect to VS− or float (not GND unless VS−=GND). |

**Gain table (A2, A1, A0):**

| A2 | A1 | A0 | Gain (V/V) |
|----|----|----|------------|
| 0 | 0 | 0 | 1/8 |
| 0 | 0 | 1 | 1/4 |
| 0 | 1 | 0 | 1/2 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 2 |
| 1 | 0 | 1 | 4 |
| 1 | 1 | 0 | 8 |
| 1 | 1 | 1 | 16 |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VS (input stage) | ±4 | — | ±18 | V | VS+ − VS− range |
| VSOUT (output stage) | ±2.25 | — | ±18 | V | LVDD − LVSS range |
| VIN (signal) | VS− − 40 | — | VS+ + 40 | V | Overvoltage protected |
| Bandwidth (all gains) | — | 10 | — | MHz | |
| Slew rate (G ≥ 1/2) | — | 35 | — | V/µs | |
| Gain error drift | — | — | ±2 | ppm/°C | |
| Input noise (G=16) | — | 8.6 | — | nV/√Hz | |
| Input current noise | — | 0.3 | — | pA/√Hz | |
| Settling (0.01%) | — | 700 | — | ns | |
| Output current | −100 | — | 100 | mA | Short-circuit continuous |
| Operating temp | −50 | — | +150 | °C | TA |

### Application Notes

- **REF pin** must be driven from a low-impedance source. Tie to mid-supply or 0 V for single-ended output referenced to GND.
- **DA\_IN+ / DA\_IN−** are the summing nodes of the internal output difference amplifier. These pins allow inserting a filter network in the signal path between the input G-stage and the output diff amp.
- **Thermal pad:** connect to VS− (or a copper plane tied to VS−) for thermal relief. Do not leave floating; do not connect to GND unless VS− = GND.
- **DGND** is the ground reference for the A2:A0 pins and internal logic. Connect to VS− in most cases, or to circuit GND.
- LVDD/LVSS supply the output stage independently — protects downstream ADC from overdrive if input is overdriven.
- Gain-select pins A2:A1:A0 are static; change only when device is not processing a signal.

### Project Usage Notes

> **[ESH10000535 R3]:** U11, U16 (PGA849). VS+=+18V, VS−=−18V (from LTC3265). LVDD/LVSS=5VA\_supply (verify in schematic). Used as precision front-end InAmps for differential analog measurement channels. Gain set by A2:A1:A0 from MCU or IO expander.

---

## 74LVC1G19DBV

**Manufacturer:** Nexperia  
**Mfr Part Number:** 74LVC1G19DBV (SOT363 / TSSOP6)  
**Package:** SOT363 (6-pin, also called TSSOP6)  
**Category:** IC — Logic / Decoder/Demultiplexer  
**Datasheet:** 74LVC1G19, Nexperia  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

Single 1-of-2 decoder / demultiplexer. Active-LOW enable (E\). When enabled, input A selects which output (Y0 or Y1) the input drives. When disabled (E\=HIGH), both outputs are HIGH. VCC 1.65 V–5.5 V, inputs 5.5 V tolerant.

### Pin Description (SOT363 / TSSOP6 — top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | A | I | Select / data input |
| 2 | E\ | I | Enable, active LOW. HIGH = both outputs HIGH (disabled). |
| 3 | GND | Pwr | Ground |
| 4 | Y1 | O | Output 1 |
| 5 | Y2 | O | Output 2 |
| 6 | VCC | Pwr | Supply voltage |

**Function table:**

| E\ | A | Y1 | Y2 |
|----|---|----|----|
| H | X | H | H |
| L | L | L | H |
| L | H | H | L |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC | 1.65 | — | 5.5 | V | Operating |
| VI | — | — | 5.5 | V | Input voltage (5.5 V tolerant) |
| IOH/IOL | — | — | ±32 | mA | At VCC=3.3 V |
| tpd (3.3 V) | — | — | ~6 | ns | Typical propagation |
| Operating temp | −40 | — | +125 | °C | |

### Application Notes

- Tie E\ LOW for permanent enable; use E\ as a chip-select-like gating signal.
- Unused outputs may be left unconnected, but input A must not float when E\=LOW.

### Project Usage Notes

> **[ESH10000535 R3]:** U13 (74LVC1G19DBV). Used as a 1-of-2 mux/demux on the UPDI programming interface. A = select input; E\ driven LOW to enable. Y0 and Y1 route UPDI signal to different destinations (ATmega4809 or external programming header).

---

## OPA192

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** OPA192IDBVT (SOT-23-5)  
**Package:** SOT-23-5 (DBV)  
**Category:** IC — Analog / Op-Amp  
**Datasheet:** OPA192, Texas Instruments  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

Precision rail-to-rail input/output (RRIO) op-amp. Key specs: ±2.25 V–±18 V supply, ±5 µV Vos (typ), 10 MHz GBW, 20 V/µs slew rate, RRIO, low noise. Suitable for precision single-supply or dual-supply applications.

### Pin Description (SOT-23-5 — top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | OUT | O | Output |
| 2 | V− | Pwr | Negative supply / ground |
| 3 | +IN | I | Non-inverting input |
| 4 | −IN | I | Inverting input |
| 5 | V+ | Pwr | Positive supply |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VS (supply range) | ±2.25 | — | ±18 | V | Single: 4.5 V–36 V |
| Vos (offset voltage) | — | ±5 | — | µV | |
| GBW | — | 10 | — | MHz | |
| Slew rate | — | 20 | — | V/µs | |
| Input voltage range | V− − 0.1 | — | V+ + 0.1 | V | Rail-to-rail |
| Output swing | V− + 20 mV | — | V+ − 20 mV | V | Rail-to-rail |
| Quiescent current | — | 1.2 | — | mA | Per amplifier |
| Operating temp | −40 | — | +125 | °C | |

### Application Notes

- Unity-gain stable.
- RRIO: output can swing within ~20 mV of either rail.
- When used as a voltage follower (unity gain buffer): connect OUT (pin 1) to −IN (pin 4).

### Project Usage Notes

> **[ESH10000535 R3]:** U15 (OPA192, SOT-23-5). Unity-gain voltage buffer: OUT(1)=VREF\_BUF, −IN(4)=VREF\_BUF (feedback), +IN(3)=VREF, V+(5)=5VA, V−(2)=GND. Buffers a reference voltage (VREF) to a low-impedance output (VREF\_BUF).

---

## LP5012RUKR

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** LP5012RUKR (WQFN-20, 3 mm × 3 mm)  
**Package:** WQFN-20 (RUK), 3 mm × 3 mm, exposed thermal pad  
**Category:** IC — LED Driver  
**Datasheet:** LP5009/LP5012, SLVSEH2B, Texas Instruments, May 2019 – August 2020  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

12-channel constant-current I2C RGB LED driver. 12-bit PWM per channel (29 kHz), integrated 3-phase PWM-shifting. Up to 25.5 mA per channel (VCC full range) or 35 mA (VCC ≥ 3.3 V). Supports independent colour-mixing and brightness control per RGB group. Up to 4 devices on one I2C bus (ADDR0/ADDR1). Fast-mode I2C up to 400 kHz.

### Pin Description (WQFN-20 — top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | VCAP | Pwr | Internal LDO bypass cap. Connect 1 µF ceramic to GND. |
| 2 | OUT0 | O | LED current sink 0 |
| 3 | OUT1 | O | LED current sink 1 |
| 4 | OUT2 | O | LED current sink 2 |
| 5 | OUT3 | O | LED current sink 3 |
| 6 | OUT4 | O | LED current sink 4 |
| 7 | OUT5 | O | LED current sink 5 |
| 8 | OUT6 | O | LED current sink 6 |
| 9 | OUT7 | O | LED current sink 7 |
| 10 | OUT8 | O | LED current sink 8 |
| 11 | OUT9 | O | LED current sink 9 |
| 12 | OUT10 | O | LED current sink 10 |
| 13 | OUT11 | O | LED current sink 11 |
| 14 | ADDR0 | I | I2C address bit 0. Must not be left floating. |
| 15 | ADDR1 | I | I2C address bit 1. Must not be left floating. |
| 16 | VCC | Pwr | Supply voltage (2.7 V–5.5 V) |
| 17 | SDA | I/O | I2C data |
| 18 | SCL | I | I2C clock (up to 400 kHz) |
| 19 | EN | I | Chip enable. LOW = shutdown (1 µA max IDD). |
| 20 | IREF | — | Current reference. Connect resistor to GND to set full-scale current. |
| EP | Thermal pad | Pwr | GND (combines AGND/PGND/DGND). Must be soldered to PCB ground plane. |

**I2C base address:** 0x14 (ADDR1=0, ADDR0=0); up to 4 addresses selectable with ADDR0/ADDR1.

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC | 2.7 | — | 5.5 | V | |
| VLED (LED anode supply) | — | — | 6 | V | Max LED forward voltage |
| IOUT per channel (VCC full range) | — | — | 25.5 | mA | |
| IOUT per channel (VCC ≥ 3.3 V) | — | — | 35 | mA | |
| Device-to-device accuracy | — | — | ±5 | % | |
| Channel-to-channel accuracy | — | — | ±5 | % | |
| IDD (shutdown, EN=LOW) | — | — | 1 | µA | |
| IDD (power-saving, all off >30 ms) | — | 10 | — | µA | |
| PWM frequency | — | 29 | — | kHz | 12-bit |
| I2C speed | — | — | 400 | kHz | Fast mode |
| Operating temp | −40 | — | +85 | °C | |

### Application Notes

- **VCAP:** Bypass with 1 µF ceramic cap to GND close to the pin.
- **IREF:** A resistor from IREF to GND sets the full-scale output current for all channels.
- **EN:** Pull LOW to enter shutdown (<1 µA). Pull HIGH to enable.
- **ADDR0/ADDR1** must be driven (HIGH or LOW); do not leave floating.
- Unused OUT pins may be left floating.

### Project Usage Notes

> **[ESH10000535 R3]:** U17 (LP5012RUKR). VCC=5V (from 5V rail via J3). Drives D2–D8 (QBLP600-RGB LEDs, 7 × RGB = 21 channels? Verify in schematic). ADDR0/ADDR1 set the I2C address. Controlled by ATmega4809 (U18) over I2C bus.

---

## ATmega4809

**Manufacturer:** Microchip Technology  
**Mfr Part Number:** ATmega4809 (48-pin TQFP or UQFN)  
**Package:** TQFP-48 or UQFN-48; center pad (QFN) to GND or floating  
**Category:** IC — Microcontroller (megaAVR 0-series)  
**Datasheet:** ATmega4808/4809 Data Sheet, DS40002173A, Microchip Technology, 2020  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

8-bit megaAVR 0-series MCU. 48 KB Flash, 6 KB SRAM, 256 B EEPROM, 48 pins. Peripherals: 4×USART, 1×SPI (master/slave), 1×TWI (I2C), 3×TCB timers, 1×TCA timer, 1×ADC (12-bit), 1×AC, 5×CCL LUT, event system, UPDI programming interface. Configurable custom logic (CCL) and flexible event system.

### Pin Description (48-Pin TQFP — sorted by pin number)

| Pin | Name | Domain | Alternate Functions |
|-----|------|--------|---------------------|
| 1 | GND | Pwr | — |
| 2 | VDD | Pwr | — |
| 3 | PA5 | VDD | USART0-XCK, SPI0-MISO, TCA0-WO5, EVOUT-A |
| 4 | PA6 | VDD | USART0-TXD (alt), SPI0-MOSI, TCA0-WO0 (alt) |
| 5 | PD6 | VDD | DAC0-OUT |
| 6 | PD7 | VDD | AIN7 |
| 7 | PB0 | VDD | USART3-TXD, SPI0-SCK (alt), TWI0-SDA (alt) |
| 8 | PD0 | VDD | AIN0, USART0-TXD (alt) |
| 9 | PD1 | VDD | AIN1, USART0-RXD (alt) |
| 10 | PC3 | VDD | USART1-XDIR, SPI0-SS (alt), TCA0-WO3 |
| 11 | PA2 | VDD | TWI0-SDA, USART0-XCK, SPI0-MOSI (alt), TCA0-WO2, EVOUTA |
| 12 | PF4 | VDD | USART2-TXD (alt) |
| 13 | PD5 | VDD | AIN5 |
| 14 | PC6 | VDD | USART1-TXD (alt), SPI0-MISO (alt) |
| 15 | PC7 | VDD | USART1-RXD (alt) |
| 16 | UPDI | VDD | Programming and debug interface |
| 17 | PF5 | VDD | USART2-RXD (alt) |
| 18 | PF6 | VDD | RESET (when RSTPIN fuse = 1) |
| 19 | PA1 | VDD | USART0-RXD, SPI0-MOSI (alt), TCA0-WO1, EVOUTA |
| 20 | PA4 | VDD | USART0-XDIR, SPI0-SS, TCA0-WO4, EVOUTA |
| 21 | PD4 | VDD | AIN4, USART0-RXD (alt) |
| 22 | PB4 | VDD | USART3-XDIR, SPI0-SS (alt) |
| 23 | VDD | Pwr | — |
| 24 | GND | Pwr | — |
| 25 | PC2 | VDD | USART1-TXD, SPI0-MISO (alt), TCA0-WO2 (alt) |
| 26 | PE3 | VDD | USART2-XDIR (alt) |
| 27 | PE0 | VDD | USART2-TXD, TWI0-SDA (alt) |
| 28 | PE2 | VDD | USART2-XCK (alt) |
| 29 | PE1 | VDD | USART2-RXD, TWI0-SCL (alt) |
| 30 | PB3 | VDD | USART3-XDIR (alt), SPI0-SS (alt), TWI0-SCL (alt) |
| 31 | PB2 | VDD | USART3-TXD (alt), SPI0-MOSI (alt), TWI0-SDA (alt) |
| 32 | PB1 | VDD | USART3-RXD (alt), SPI0-MISO (alt), TWI0-SCL (alt) |
| 33 | PA3 | VDD | TWI0-SCL, USART0-TXD, SPI0-SS (alt), TCA0-WO3, EVOUTA |
| 34 | PF1 (TOSC2) | VDD | Crystal oscillator, USART2-RXD (alt) |
| 35 | PF0 (TOSC1) | VDD | Crystal oscillator, USART2-TXD (alt) |
| 36 | PF3 | VDD | USART2-XDIR |
| 37 | PF2 | VDD | USART2-XCK, USART2-TXD (alt) |
| 38 | PD3 | VDD | AIN3 |
| 39 | PD2 | VDD | AIN2 |
| 40 | PC5 | VDD | USART1-RXD (alt), TCA0-WO5 (alt) |
| 41 | PC4 | VDD | USART1-XCK (alt), TCA0-WO4 (alt) |
| 42 | PC1 | VDD | USART1-RXD, SPI0-SS (alt), TCA0-WO1 (alt) |
| 43 | PC0 | VDD | USART1-TXD (alt), TCA0-WO0 (alt) |
| 44 | PA7 | VDD | USART0-RXD (alt), SPI0-SCK (alt) |
| 45 | PB5 | VDD | USART3-RXD (alt) |
| 46 | GND | Pwr | — |
| 47 | AVDD | AVDD | Analog supply for ADC/AC/DAC. Bypass separately. |
| 48 | PA0 (EXTCLK) | VDD | External clock input |

**Power supply pins:**
- VDD: pins 2, 23 — digital supply
- GND: pins 1, 24, 46 — digital ground
- AVDD: pin 47 — analog supply (must be separately bypassed; connect to VDD if no separate analog supply)

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VDD | 1.8 | — | 5.5 | V | Full operating range |
| AVDD | VDD − 0.1 | — | VDD + 0.1 | V | Keep within 0.1 V of VDD |
| FCLK (max) | — | — | 20 | MHz | At VDD ≥ 4.5 V |
| FCLK (max, 1.8–2.7 V) | — | — | 8 | MHz | |
| Flash | — | 48 | — | KB | |
| SRAM | — | 6 | — | KB | |
| EEPROM | — | 256 | — | B | |
| I/O pins | — | 40 | — | — | (48-pin package) |
| ADC resolution | — | 12 | — | bit | |
| Operating temp | −40 | — | +85 | °C | Industrial |

### Application Notes

- **UPDI** (pin 16): unified programming and debugging interface. Requires a single-wire half-duplex serial connection.
- **AVDD** (pin 47): must be decoupled with at least 100 nF ceramic cap close to pin. Connect to VDD if no separate analog supply.
- **TOSC1/TOSC2** (pins 35/34): external 32.768 kHz crystal or clock for RTC.
- **Unconnected GPIO pins** are valid: configure as inputs with pull-ups enabled in firmware to avoid floating. In netlist/schematic, pins not connected are expected behaviour for an MCU — not an ERC error.
- **PF6** can be configured as RESET pin via fuse; by default it is a GPIO.
- Center pad (UQFN only): connect to GND or leave floating. Solder for mechanical stability.

### Project Usage Notes

> **[ESH10000535 R3]:** U18 (ATmega4809, TQFP-48). VDD=3V3. AVDD=3V3. 26/48 pins present in netlist — unconnected I/O pins are intentional NCs (OI-04, pending engineer confirmation). Runs I2C bus (TWI0: PA2/PA3), SPI (SPI0), UART (USART), and UPDI programming via U13 mux. Controls bus buffers via SPI\_ENn, UART\_ENn.

---

## SN74AVC4T774RGYR

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** SN74AVC4T774RGYR (VQFN-16, 4 mm × 3.5 mm)  
**Package:** VQFN-16 (RGY), 4 mm × 3.5 mm, exposed thermal pad  
**Category:** IC — Logic / Bus Transceiver (level shifting, bidirectional)  
**Datasheet:** SN74AVC4T774, SCES693I, Texas Instruments, February 2008 – February 2025  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

4-bit dual-supply bidirectional bus transceiver with configurable voltage-level shifting and 3-state outputs. VCCA and VCCB each independently accept 1.1 V–3.6 V. Each of the 4 channels has an independent DIR control input. One shared OE\ input (active LOW). Control inputs (DIR, OE) are referenced to VCCA.

### Pin Description (VQFN-16 / RGY — top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | DIR1 | I | Direction control, channel 1. HIGH = A→B; LOW = B→A. Referenced to VCCA. |
| 2 | DIR2 | I | Direction control, channel 2 |
| 3 | A1 | I/O | Port A, channel 1 (VCCA domain) |
| 4 | A2 | I/O | Port A, channel 2 |
| 5 | A3 | I/O | Port A, channel 3 |
| 6 | A4 | I/O | Port A, channel 4 |
| 7 | DIR3 | I | Direction control, channel 3 |
| 8 | DIR4 | I | Direction control, channel 4 |
| 9 | OE | I | Output enable, active LOW (shared). HIGH = all outputs high-Z. Referenced to VCCA. |
| 10 | GND | Pwr | Ground |
| 11 | B4 | I/O | Port B, channel 4 (VCCB domain) |
| 12 | B3 | I/O | Port B, channel 3 |
| 13 | B2 | I/O | Port B, channel 2 |
| 14 | B1 | I/O | Port B, channel 1 |
| 15 | VCCB | Pwr | Port B supply (1.1 V–3.6 V) |
| 16 | VCCA | Pwr | Port A supply (1.1 V–3.6 V) |
| EP | Thermal pad | Pwr | GND. Connect to PCB GND. |

**Logic (one channel, OE=LOW):**
- DIR=HIGH: A→B (A is input, B is output)
- DIR=LOW: B→A (B is input, A is output)
- OE=HIGH: both A and B outputs high-Z

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCCA | 1.1 | — | 3.6 | V | Port A and control supply |
| VCCB | 1.1 | — | 3.6 | V | Port B supply |
| VI, VO tolerance | — | — | 4.6 | V | I/O pin max voltage |
| Data rate (1.8V↔3.3V) | — | 380 | — | Mbps | |
| Data rate (<1.8V↔3.3V) | — | 200 | — | Mbps | |
| ESD (HBM) | — | — | ±8000 | V | |
| ESD (CDM) | — | — | ±1500 | V | |
| Operating temp | −40 | — | +125 | °C | |

### Application Notes

- **OE should be tied HIGH (to VCCA) through a pull-up during power-up** to keep outputs high-Z until the supplies are stable. Minimum pull-up resistance is set by the OE driver's current capability.
- **Inputs must not float.** A floating A or B pin can cause excess ICC.
- If either VCC rail is at GND (VCC isolation feature), both ports go high-Z automatically.
- When translating from a lower VCCA to higher VCCB, or vice versa, DIR control is latency-critical — ensure DIR settles before the first data edge.

### Project Usage Notes

> **[ESH10000535 R3]:** U19, U20 (SN74AVC4T774RGYR). VCCA=3V3 (MCU side), VCCB=3V3 or different voltage (verify in schematic). Used as 4-bit bidirectional level-shifting buffers on SPI or other bus interfaces. DIR1–DIR4 driven individually from MCU or IO expander.

---

## TLV9102IDR

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** TLV9102IDR (SOIC-8)  
**Package:** SOIC-8 (D)  
**Category:** IC — Analog / Op-Amp (dual)  
**Datasheet:** TLV9102, Texas Instruments  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

Dual rail-to-rail input/output (RRIO) op-amp in SOIC-8. 2.7 V–16 V supply (or ±1.35 V–±8 V), 1.1 MHz GBW, 0.5 V/µs slew rate. General-purpose low-voltage dual op-amp for signal conditioning.

### Pin Description (SOIC-8 — top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | OUT1 | O | Output, amplifier 1 |
| 2 | −IN1 | I | Inverting input, amplifier 1 |
| 3 | +IN1 | I | Non-inverting input, amplifier 1 |
| 4 | V− | Pwr | Negative supply |
| 5 | +IN2 | I | Non-inverting input, amplifier 2 |
| 6 | −IN2 | I | Inverting input, amplifier 2 |
| 7 | OUT2 | O | Output, amplifier 2 |
| 8 | V+ | Pwr | Positive supply |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VS (supply) | 2.7 | — | 16 | V | Single supply |
| VS (dual) | ±1.35 | — | ±8 | V | |
| GBW | — | 1.1 | — | MHz | |
| Slew rate | — | 0.5 | — | V/µs | |
| Input range | V− | — | V+ | V | Rail-to-rail |
| Output swing | V− + 30 mV | — | V+ − 30 mV | V | Rail-to-rail |
| Quiescent current | — | 60 | — | µA | Per amplifier |
| Operating temp | −40 | — | +125 | °C | |

### Application Notes

- Unity-gain stable.
- Very low quiescent current (60 µA/amp) makes it suitable for battery or low-power applications.
- Input common-mode range includes both supply rails (true RRIO).

### Project Usage Notes

> **[ESH10000535 R3]:** U21 (TLV9102IDR). Supply rails and signal nets to be confirmed in schematic review (ERC-C08/P06). Used as dual op-amp for signal conditioning.

---

## SN74LVC1G125DBVR

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** SN74CBTLV1G125DBVR (SOT-23-5); BOM/schematic reference: SN74LVC1G125DBVR  
**Package:** SOT-23-5 (DBV)  
**Category:** IC — Logic / Bus Switch (single FET, bidirectional)  
**Datasheet:** SN74CBTLV1G125, SCDS057H, Texas Instruments, Revised June 2006 (file: sn74cbtlv1g125.pdf)  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

> **Note:** The BOM lists this device as SN74LVC1G125DBVR; the TI orderable part number in the datasheet is SN74CBTLV1G125DBVR. These refer to the same device. This is a **bidirectional FET bus switch**, not a unidirectional 3-state buffer — see function table below.

Single high-speed FET bus switch. When OE is LOW, port A is connected to port B through a low-resistance (~5 Ω) FET switch. When OE is HIGH, the switch is open (ports isolated). Rail-to-rail signal switching. Supports partial power-down via Ioff.

### Pin Description (SOT-23-5 / DBV — top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | OE | I | Output enable, active LOW. LOW = A↔B connected; HIGH = disconnected. |
| 2 | B | I/O | Port B — bidirectional switch terminal |
| 3 | GND | Pwr | Ground |
| 4 | A | I/O | Port A — bidirectional switch terminal |
| 5 | VCC | Pwr | Supply voltage |

**Function table:**

| OE | Function |
|----|----------|
| L | A port = B port (5 Ω switch closed) |
| H | Disconnect (both ports isolated) |

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC | 2.3 | — | 3.6 | V | Operating |
| VI (signal, rail-to-rail) | 0 | — | VCC | V | A and B ports |
| VI (absolute max) | −0.5 | — | 4.6 | V | |
| RON | — | 5 | — | Ω | Switch on-resistance |
| VIH (OE, VCC=2.7–3.6V) | 2.0 | — | — | V | |
| VIL (OE, VCC=2.7–3.6V) | — | — | 0.8 | V | |
| Ioff | — | — | 10 | µA | VCC=0, VI/VO=0–3.6V (partial power-down) |
| ICC (static) | — | — | 10 | µA | |
| Operating temp | −40 | — | +85 | °C | |

### Application Notes

- **Bidirectional:** Unlike a buffer, signal flow is not fixed — either A or B may be the driver depending on the circuit context.
- OE should be tied to VCC through a pull-up resistor to ensure the switch is open during power-up/power-down.
- The OE input must not be left floating.
- RON of 5 Ω is negligible for most digital signals but matters in analog or high-speed paths (voltage drop = I × 5 Ω).
- Ioff ensures no backflow current when VCC = 0, enabling safe use in partial-power-down systems.

### Project Usage Notes

> **[ESH10000535 R3]:** U23 (SN74LVC1G125DBVR / SN74CBTLV1G125DBVR). OE control net and A/B signal nets TBD from schematic. Bidirectional switch — verify direction intent in ERC-D.

---

## SN74LVC1G126DBVR

**Manufacturer:** Texas Instruments  
**Mfr Part Number:** SN74LVC1G126DBVR (SOT-23-5)  
**Package:** SOT-23-5 (DBV)  
**Category:** IC — Logic / Buffer (single, 3-state, active-HIGH OE)  
**Datasheet:** SN74LVC1G126, Texas Instruments  
**Added:** 2026-04-30  
**Used in:** ESH10000535 R3

Single bus buffer gate with 3-state output. Active-HIGH output enable (OE): output is enabled when OE is HIGH; output is high-Z when OE is LOW. VCC 1.65 V–5.5 V, inputs accept up to 5.5 V.

### Pin Description (SOT-23-5 — top view)

| Pin | Name | Type | Description |
|-----|------|------|-------------|
| 1 | OE | I | Output enable, active HIGH |
| 2 | GND | Pwr | Ground |
| 3 | A | I | Input |
| 4 | Y | O/Z | Output (3-state) |
| 5 | VCC | Pwr | Supply voltage |

**Function:** OE=H → Y=A. OE=L → Y=Hi-Z.

### Key Electrical Parameters

| Parameter | Min | Typ | Max | Unit | Notes |
|-----------|-----|-----|-----|------|-------|
| VCC | 1.65 | — | 5.5 | V | Operating |
| VI (input) | — | — | 5.5 | V | 5.5 V tolerant |
| IOH/IOL | — | — | ±32 | mA | At VCC=3.3 V |
| Operating temp | −40 | — | +125 | °C | |

### Application Notes

- OE must not be left floating; tie to GND to keep output permanently high-Z, or to VCC (or a driver) to enable.
- Single-channel version of SN74LVC126A (which has 4 channels in TSSOP-14).
- **Active-HIGH OE**: same polarity as SN74LVC126A. Contrast with SN74LVC1G125 (active-LOW OE).

### Project Usage Notes

> **[ESH10000535 R3]:** U24 (SN74LVC1G126DBVR). Single buffer used to gate a signal (net TBD). OE driven from MCU or IO expander.
