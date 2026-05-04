---
project: ESH10000536
product: Active Load
revision: R2
type: TBD
created: 2026-05-04
last_updated: 2026-05-04
---

# Specification: Active Load (R2)

## Scope

This document defines the functional requirements and acceptance criteria for the Active Load R2 PCBA (internal name: `m2top_2xload`).
The Active Load is a dual-channel programmable electronic load that plugs into the Sparrow/Accordion platform via M.2 connector (J1). It is assembled together with Fixture Electronics (ESH10000540) in the Sparrow test fixture.

Each load channel is controlled via DAC (AD5593R) and measured via current sense amplifier (INA2181). The board also includes temperature monitoring (TMP116), fan control (MAX6650), an ID EEPROM (24AA02UID), and a digital isolator (ISOW7741).

Requirements are to be defined when the phase (design or verification / production test) is established.

---

## Requirements

### Category definitions

| Category | Description |
|----------|-------------|
| Mechanical | PCB form factor, mounting, and connector mechanical fit |
| Electrical | Signal routing, power distribution, and protection |
| Interface | Connector pinout, signal mapping, and compatibility |
| Function | Board-level functional behaviour |

---

### Requirements table

| Req ID | Category | Requirement | Acceptance Criteria | Test Case(s) | Status |
|--------|----------|-------------|---------------------|--------------|--------|
| *(no requirements yet)* | | | | | |

---

## Revision History

| Rev | Date | Author | Change |
|-----|------|--------|--------|
| R2 | 2026-05-04 | Martin Johansson | Initial document created |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Design Engineer | | | |
| Quality | | | |
