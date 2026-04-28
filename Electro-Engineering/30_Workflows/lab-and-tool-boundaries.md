# Lab and Tool Boundaries

## Purpose
Maintain a clear separation between this Engineering Workbook (documentation) and the tools, instruments, and data used in the lab.

---

## The Engineering Workbook (OneDrive)
- Document-only workspace: Markdown files, templates, logs, plans
- No executable scripts should be run from here (except `40_Tools/report_builder.py` as a standalone utility)
- Never use this workbook as a data store for raw measurement files — those go in the project's `TEST_RESULTS/assets/` folder or a dedicated data archive

---

## Lab tools and instruments
When working with lab equipment (oscilloscopes, power supplies, analyzers, climatic chambers, etc.):
- Never operate equipment remotely or programmatically from an AI session without explicit intent confirmation
- Before any automated or scripted measurement run: confirm setup, DUT state, and safety conditions
- Any operating limits (voltage, current, temperature, humidity) must be defined and checked before starting a test — not inferred

---

## Safety boundary
If a requested action could damage a DUT, affect lab equipment, or generate misleading results:
- Add an explicit risk note before proceeding
- Ask for confirmation of intent before making the change

Examples requiring explicit confirmation:
- Running a stress test beyond specified limits
- Connecting an uncharacterized DUT to powered test fixtures
- Modifying a test procedure in a way that changes pass/fail criteria

---

## Data files and evidence
- Raw data (CSVs, waveform exports, photos) lives in `TEST_RESULTS/assets/` or `70_Assets/`
- Session logs in `TEST_RESULTS/` reference these files by relative path
- Do not embed raw data in Markdown logs — reference paths only

---

## AI usage
- AI may help analyze data after it has been collected and manually pasted or referenced
- AI may not initiate instrument control, start measurements, or modify hardware configuration
