# Layout Review Workflow

## Purpose
Structured process for AI-assisted layout review of PCB designs using text-format output files.
The engineer provides layout exports; the AI performs deterministic checks and reports findings.
This workflow is the layout counterpart to `schematic-review.md`.

## Scope (v1)
- **Review type:** Structural, completeness, and DFM checks extractable from text-format layout files
- **Not in scope:** Trace width / clearance DRC, thermal relief, power plane pour quality, courtyard/silkscreen overlap, return path analysis, high-speed routing quality — all require EDA tool DRC with copper rendering

---

## Supported formats

| Format | Extension | What it provides |
|--------|-----------|-----------------|
| GenCAD 1.4 | `.cad` | Board outline, layer stackup, pad definitions, component placements, signal list, full trace routing geometry |
| IPC-D-356A | `.ipc` | Net-to-pad assignments, pad XY positions and sizes, drill diameters, via inventory |
| PADS AIS placement | `.txt` | Component placements: ref-des, footprint, rotation, X/Y, side (TOP/BOTTOM), flags |
| PADS QCV netlist | `.qcv` | Schematic net list (source of truth for net count, net names) |
| BOM CSV | `.csv` | Mounted vs No-Mount status, quantities, part numbers |
| Gerber RS-274X | `.gtl/.gbl/.gb2–7/.gts/.gbs/.gtp/.gbp/.gto/.gbo/.gko` | Copper, mask, paste, silk, outline layers; aperture tables encode minimum feature sizes |
| Excellon NCDrill | `.ncd` | Drill sizes per tool, plated / non-plated / milled classification |

---

## Format-specific parsing guidance

### GenCAD 1.4 (.cad)

Top-level sections delimited by `$SECTION` / `$ENDSECTION` markers:

| Section | Content |
|---------|---------|
| `$BOARD` | Board outline as LINE / ARC commands in mm |
| `$PADS` | Pad shape definitions (ROUND, RECTANGULAR, FINGER, POLYGON) |
| `$PADSTACKS` | Via and through-hole pad stack definitions |
| `$SHAPES` | Component footprint geometry (silkscreen, copper, courtyard) |
| `$DEVICES` | Device type declarations |
| `$COMPONENTS` | Component placements: `COMPONENT refdes`, `PLACE x y layer rotation` |
| `$SIGNALS` | Net declarations: `SIGNAL netname`, followed by `PIN refdes-pin` lines |
| `$TRACKS` | Track width style definitions |
| `$LAYERS` | Layer names in stack order (one `LAYER name` per line) |
| `$ROUTES` | Trace routing: `ROUTE netname` followed by `TRACK width`, `LAYER name`, `LINE x1 y1 x2 y2` / `ARC ...` / `VIA x y` |
| `$MECH` | Mechanical outlines |
| `$TESTPINS` | Test point list (may be empty) |
| `$POWERPINS` | Power pin list (may be empty) |

**Parser notes:**
- Board dimensions: read `$BOARD` LINE commands, compute bounding box (min/max X and Y).
- Layer count and names: read `$LAYERS` section — one layer per line.
- Net list: `$SIGNALS` section uses `SIGNAL name` followed by `PIN ref-pin` lines.
- Routing completeness: count `ROUTE` entries in `$ROUTES` and compare to `SIGNAL` count in `$SIGNALS`. All signals should have a corresponding route entry.
- Power plane nets (GND, AGND, etc.) appear in `$ROUTES` as copper plane outlines — they will have a `ROUTE` entry with a `PLANE` directive, unlike signal traces. Both are counted as routed.
- Route net names for named nets use the signal name directly (e.g. `ROUTE GND`, `ROUTE 3V3`). Internal copper pour segments use parenthesised IDs (e.g. `ROUTE (Net0)`) — these are layout-tool-internal identifiers, not separate electrical nets.

**Board outline extraction (PowerShell):**
```powershell
$cad = Get-Content "Gencad_file.cad"
$inBoard = $false
$xs = @(); $ys = @()
foreach ($line in $cad) {
    if ($line -eq '$BOARD') { $inBoard = $true; continue }
    if ($line -eq '$ENDBOARD') { $inBoard = $false; continue }
    if ($inBoard -and $line -match 'LINE\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)') {
        $xs += [double]$matches[1]; $xs += [double]$matches[3]
        $ys += [double]$matches[2]; $ys += [double]$matches[4]
    }
}
"Board: $(($xs | Measure-Object -Minimum).Minimum),$(($ys | Measure-Object -Minimum).Minimum) to $(($xs | Measure-Object -Maximum).Maximum),$(($ys | Measure-Object -Maximum).Maximum)"
```

**Net/route completeness (PowerShell):**
```powershell
$inSig = $false; $inRoute = $false; $signals = @(); $routes = @()
foreach ($line in $cad) {
    if ($line -eq '$SIGNALS') { $inSig = $true; continue }
    if ($line -eq '$ENDSIGNALS') { $inSig = $false; continue }
    if ($line -eq '$ROUTES') { $inRoute = $true; continue }
    if ($line -eq '$ENDROUTES') { $inRoute = $false; continue }
    if ($inSig -and $line -match '^SIGNAL\s+(.+)') { $signals += $matches[1].Trim() }
    if ($inRoute -and $line -match '^ROUTE\s+(.+)') { $routes += $matches[1].Trim() }
}
$unrouted = $signals | Where-Object { $net = $_; -not ($routes | Where-Object { $_ -like "*$net*" }) }
"Signals: $($signals.Count)  Routes: $($routes.Count)  Unrouted: $($unrouted.Count)"
```

---

### IPC-D-356A (.ipc)

**Record structure:**

| Record type | Meaning |
|-------------|---------|
| `P NNAME<n> <name>` | Long net name alias: maps net reference number `n` to a full name |
| `317<netname>` | Type-317 test point record (component pad): net name follows record type at column 4 |
| `327<netname>` | Type-327 test point record (via): net name follows record type at column 4 |
| `999` | End-of-file record |

**Critical parsing note:** The first 3 characters of a data record are the **record type** (317 or 327), not the net reference number. The net name starts at column 4. For long net names, the IPC-356 tool assigns a short numeric ID and declares it in a `P NNAME<n>` header line; the short ID appears in column 4 in place of the full name.

**Net name extraction:**
```powershell
$ipc = Get-Content "IPC356_file.ipc"
$dataLines = $ipc | Where-Object { $_ -match '^\d{3}' }
# Net name: chars 4 onwards to first whitespace
$netNames = $dataLines | ForEach-Object {
    if ($_.Length -ge 4) { ($_.Substring(3) -split '\s+')[0].Trim() }
} | Where-Object { $_ -ne '' }
$uniqueNets = $netNames | Sort-Object -Unique
"Unique net names/IDs: $($uniqueNets.Count)"
```

**Via inventory (PowerShell):**
```powershell
$vias = $dataLines | Where-Object { $_ -match 'VIA' }
# Drill size: field matching D<digits> pattern
$drills = $vias | ForEach-Object {
    if ($_ -match 'D\s*(\d+)P') { [int]$matches[1] / 10000 }  # units: 0.0001 mm
} | Sort-Object -Unique
"Via drill sizes (mm): $($drills -join ', ')"
# Pad size from X<w>Y<h> after the drill field
```

**Net count vs QCV:** GenCAD/IPC-356 net count will exceed the QCV schematic net count when copper planes are present. PADS assigns internal fragment IDs (`(Net0)-1`, `(Net0)-2`, ...) to each independent copper segment of a pour. These are **not** separate electrical nets. The difference equals the number of pour fragments. This is expected and not a finding.

**Single-node / orphan pad detection:**
```powershell
$netCounts = $netNames | Group-Object
$singleRecord = $netCounts | Where-Object { $_.Count -eq 1 }
$nonPour = $singleRecord | Where-Object { $_.Name -notmatch '^\(Net' }
"Orphan pads (non-pour single records): $($nonPour.Count)"
$nonPour | ForEach-Object { "  ORPHAN: $($_.Name)" }
```
Copper pour fragments matching `^\(Net` with a single record are normal (pour segment). Only flag entries that are **named schematic nets** with a single pad connection.

---

### PADS AIS placement (.txt)

Column order: `RefDes  Footprint  Rotation  X  Y  Side  Flag`

- `Side` field is `TOP` or `BOTTOM` (full word — do **not** match with `\bBOT\b`).
- `Flag` field is `YES` or `NO` — interpretation is tool-dependent (may indicate mechanical, no-mount, or glue flag). Do not use this field as a mount/NM indicator without verification.
- Header lines (`$HEADER$`, `$END HEADER$`, `$PART_SECTION_BEGIN$`, `$PART_SECTION_END$`, `BOARD_TYPE`, `UNITS`) do not start with `$` after stripping and can match component regex — filter them explicitly.
- `BOARD` lines (panel reference marks) appear with `BOTTOM` side — exclude from component counts.
- Fiducials and tooling holes (e.g. `pn-pcb_fiducial1`) appear in AIS but typically not in the BOM — expect AIS count > BOM count by the number of such mechanical items.

**Component side count (PowerShell):**
```powershell
$ais = Get-Content "AIS_file.txt"
$parts = $ais | Where-Object { $_ -notmatch '^\$' -and $_ -notmatch '^BOARD_TYPE' -and $_ -notmatch '^UNITS' -and $_ -notmatch '^BOARD\s' -and $_.Trim() -ne '' }
$top    = ($parts | Where-Object { $_ -match '\bTOP\b' }).Count
$bottom = ($parts | Where-Object { $_ -match '\bBOTTOM\b' }).Count
"TOP: $top  BOTTOM: $bottom  Total: $($top + $bottom)"
```

---

### PADS QCV netlist (.qcv)

Net lines: `NET : 'NetName' RefDes-Pin ...`

```powershell
$nets = (Get-Content "QCV_file.qcv") | Where-Object { $_ -match "^NET\s*:" }
"QCV net count: $($nets.Count)"
```

This is the schematic net count and is the reference for net consistency checks.

---

### BOM CSV

Typical columns: `PartNumber;Rev;RefDes;QtyOnBoard;NoMount;Value;Voltage;Part Name`

```powershell
$bom = Get-Content "BOM.csv" | Select-Object -Skip 1 | Where-Object { $_.Trim() -ne '' }
$mounted = $bom | Where-Object { $_ -notmatch ';NM;' }
$nm      = $bom | Where-Object { $_ -match ';NM;' }
$mountedQty = ($mounted | ForEach-Object { [int]($_ -split ';')[3] } | Measure-Object -Sum).Sum
$nmQty      = ($nm      | ForEach-Object { [int]($_ -split ';')[3] } | Measure-Object -Sum).Sum
"Mounted: $mountedQty  NM: $nmQty  Total: $($mountedQty + $nmQty)"
```

---

### Gerber RS-274X

All Gerber files from a single CAM export share:
- `%MOMM*%` — metric units
- `%FSLAX24Y24*%` — coordinate format (2 integer digits, 4 fractional digits, leading zeros suppressed). 1 unit = 0.0001 mm; coordinates like `X1400000` = 140.0000 mm.
- `%OFA0.0000B0.0000*%` — no offset
- `G04` lines — comments (job name, layer name, user, date)

**Aperture table (minimum feature size):**
```powershell
$circleDiams = (Get-Content "layer.gtl") | Where-Object { $_ -match '^%ADD\d+C,' } |
    ForEach-Object { [double]($_ -replace '.*C,(\d+\.\d+)\*.*','$1') } | Sort-Object
"Min aperture (mm): $($circleDiams[0])"
```

**Board outline from panel.gko:**
Extract coordinate extents from `LINE X1Y1 X2Y2` commands. Convert with ÷ 10000 (FSLAX24Y24).

**Paste file check:** Non-empty paste files (apertures + draw/flash commands) indicate SMD paste is defined. An empty paste bottom file with no bottom-side SMD components is expected. Non-empty paste bottom with no bottom-side components in AIS is a discrepancy to flag.

---

### Excellon NCDrill (.ncd)

Tool declarations: `T<n>C<diameter>` (diameter in mm, 3.3 format if leading-zero suppressed, or stated units).

```powershell
$ncd = Get-Content "ThruHolePlated.ncd"
$tools = $ncd | Where-Object { $_ -match '^T\d+C[\d.]+$' } |
    ForEach-Object { [double]($_ -replace 'T\d+C','') } | Sort-Object -Unique
"Drill sizes (mm): $($tools -join ', ')"
```

Files to expect: `ThruHolePlated.ncd`, `ThruHoleNonPlated.ncd`, `ContourPlated.ncd` (milled slots).

---

## Layout checks

Perform each applicable check. Mark as ✅ Pass, ⚠️ Info, or ❌ Fail.

### Gerber checks

| ID | Check | Severity | Description |
|----|-------|----------|-------------|
| GBR-F01 | Gerber file inventory | ❌ Fail if missing | Confirm all copper layers, soldermask top/bottom, solderpaste top/bottom, silkscreen top/bottom, and board outline files are present. Confirm NCDrill files (plated, non-plated, contour) are present. |
| GBR-F02 | Format consistency | ❌ Fail if mismatch | All files from same CAM export: same coordinate format (FSLAX), same units (MOMM), same export date in G04 header. Mismatch indicates files from different revisions were mixed. |
| GBR-F03 | Minimum copper aperture | ⚠️ Info | Extract minimum circle aperture size from each copper Gerber's `%ADD...C,...` table. Apertures ≤ 0.10 mm are at the limit of standard fab rules and should be verified against the fab spec. Note: aperture tables define all apertures including via pads — the minimum may not be a trace width. If the min aperture is only 0.25 mm or larger, skip. |
| GBR-F04 | Paste file consistency | ⚠️ Info | Paste top should be non-empty if there are TOP-side SMD components. Paste bottom should be non-empty only if there are BOTTOM-side SMD components. An unexpected non-empty paste file is a finding. An expected paste file being empty is also a finding. |
| GBR-F05 | Board outline dimensions | ⚠️ Info | Extract board outline from `panel.gko` or the outline Gerber. Confirm dimensions match the assembly drawing and GenCAD `$BOARD`. Panel dimensions (with rails) should be consistent with the board + rail widths. |

### Layer and structural checks

| ID | Check | Severity | Description |
|----|-------|----------|-------------|
| LR-L01 | Layer stackup | ❌ Fail if wrong | Read GenCAD `$LAYERS`. Confirm layer count and names match the PCB specification. Flag if inner layer count differs from expected. Note: GenCAD does not encode signal vs. plane function per layer — only names are available. |
| LR-L02 | Board outline (GenCAD) | ⚠️ Info | Read GenCAD `$BOARD` outline. Confirm dimensions match GBR-F05 and assembly drawing. Cross-check with IPC-356 pad coordinates — all pad XY positions should fall within the board boundary. |

### Placement checks

| ID | Check | Severity | Description |
|----|-------|----------|-------------|
| LR-P01 | Placement completeness | ⚠️ Info | Compare AIS component count to BOM total (mounted + NM). AIS count should equal or slightly exceed BOM total — the surplus consists of fiducials, tooling holes, and mechanical items not in the BOM. A deficit (AIS < BOM) is an error. Report the difference and identify surplus items by footprint name. |
| LR-P02 | Bottom-side components | ⚠️ Info | List all BOTTOM-side components from AIS. For each type (IC, passive, connector, diode, mechanical), confirm bottom-side placement is intentional. Verify paste bottom is non-empty if any bottom-side SMD components are present. Flag unexpected bottom-side ICs as ❌ Fail — these are common when a footprint is inadvertently mirrored. |

### Net checks

| ID | Check | Severity | Description |
|----|-------|----------|-------------|
| LR-N01 | Net count consistency | ⚠️ Info | Compare QCV schematic net count to GenCAD `$SIGNALS` count. A surplus in GenCAD/IPC-356 is expected when copper pours are present (pour fragment IDs). A deficit (GenCAD < QCV) is an error — nets missing from layout. The difference should equal the number of pour fragments (typically 50–300 for a board with full GND/AGND pours). |
| LR-N02 | Single-node / orphan pads | ❌ Fail if real orphan | From IPC-356: count nets with exactly one pad record. Filter out copper pour fragments (names matching `^\(Net`). Any remaining single-record net is a potential orphan pad (unconnected SMD land or via). Report and ask engineer to confirm. |

### Via and drill checks

| ID | Check | Severity | Description |
|----|-------|----------|-------------|
| LR-V01 | Via drill / annular ring | ⚠️ Info | From IPC-356 (drill size) and Gerber (via pad size): calculate annular ring = (pad dia − drill dia) / 2. Flag if < 0.10 mm for standard fab, or < 0.075 mm for advanced fab. List all drill sizes from NCDrill and flag any drill < 0.20 mm that is plated (aspect ratio concern if board is > 1.6 mm thick). |

### Routing checks

| ID | Check | Severity | Description |
|----|-------|----------|-------------|
| LR-R01 | Routing completeness | ❌ Fail if unrouted | From GenCAD `$SIGNALS` vs `$ROUTES`: every signal should have a corresponding route entry. Unrouted signals = missing copper. Use substring matching (`-like "*$net*"`) since route names and signal names may have minor formatting differences. Report all unrouted signal names. |
| LR-R02 | Power net routing presence | ❌ Fail if missing | Spot-check key power nets (GND, AGND, VDD, 3V3, 5V, 12V and design-specific rails from the ERC review) in GenCAD `$ROUTES`. A power net absent from routes means it was never placed or was accidentally deleted. All power nets identified in the schematic ERC must appear in routes. |

---

## Review procedure

### 1. Confirm files available

Ask the engineer which layout output files are available. The minimum set for a useful review:

| Files | Enables |
|-------|---------|
| GenCAD `.cad` | All LR checks |
| IPC-356 `.ipc` | LR-N01/N02, LR-V01 (annular ring) |
| AIS `.txt` | LR-P01/P02 |
| QCV `.qcv` + BOM `.csv` | LR-N01 net count, LR-P01 BOM comparison |
| Gerber `.gtl/.gbl` etc. | GBR-F01/F02/F03/F04/F05 |
| NCDrill `.ncd` | LR-V01 (drill sizes) |

If only Gerbers are available, run GBR checks only.
If only GenCAD and IPC-356 are available, run LR checks (skip GBR).

### 2. Read board and format metadata

Extract from GenCAD header and Gerber G04 comments:
- Board dimensions (GenCAD `$BOARD`)
- Layer count (GenCAD `$LAYERS`)
- CAM export date (Gerber G04)
- CAD tool name (GenCAD `$HEADER` USER field)

Check that Gerber files all share the same export date (GBR-F02).

### 3. Run all applicable checks

Work through the check tables in order: GBR → LR-L → LR-P → LR-N → LR-V → LR-R.

For each finding:
- Record the check ID
- State the specific component(s), net(s), or layer(s) involved
- Classify as ✅ Pass, ⚠️ Info, or ❌ Fail
- For Info items: describe what needs engineer confirmation

### 4. Report findings

Write findings to the project's `Review/LAYOUT_REVIEW.md` using this structure:

```markdown
---
project: <ESH number>
revision: <Rn>
date: <YYYY-MM-DD>
phase: Review
---

# Layout Review — <Product name> <Revision>

## File Information
| Field | Value |
|-------|-------|
| Files reviewed | ... |
| CAD tool | ... |
| CAM export date | ... |
| Components | <total> (mounted, NM) |
| Nets (schematic) | <QCV count> |
| Nets (layout) | <GenCAD count> |
| Board dimensions | ... |
| Layer count | ... |
| Review type | Structural / completeness / DFM (text-parseable checks only) |
| Reviewer | AI — findings require engineer disposition |

## Scope and Limitations
<State what was and was not checked>

## Findings Summary
| Check | ID | Result | Notes |
|-------|----|--------|-------|
...

## Detailed Findings
<One section per check, pass and info both included>

## Checks Not Performed
<List DRC and visual checks that require EDA tool>

## Disposition Summary
| ID | Finding | Disposition | By | Date |
...

## Sign-off
...
```

### 5. Engineer disposition

For each ⚠️ Info finding, the engineer must either:
- **Confirm** — intentional, no change needed (record reason)
- **Action** — design change required (create issue or update design)

For each ❌ Fail finding, a design action is mandatory before sign-off.

**Sign-off condition:** All Fail findings resolved (fixed or accepted with documented rationale), all Info findings dispositioned.

---

## Checks not performable from text files

The following require EDA tool DRC with copper rendering and are **out of scope** for this workflow:

| Check | Why not possible from text |
|-------|--------------------------|
| Trace width / clearance DRC | Requires rendering copper geometry and computing polygon distances |
| Thermal relief | Visual / geometric inspection of pad-to-plane connections |
| Power plane pour quality | Requires polygon rendering to check pour coverage and isolation |
| Courtyard / silkscreen overlap | Courtyard data not present in GenCAD or IPC-356 |
| High-speed routing quality | Parallel runs, length matching, differential pair skew — partial text analysis insufficient |
| Return path analysis | Requires layer-by-layer copper visibility to trace signal return paths |
| Solder joint inspection | Assembly quality — not in layout files |

**Recommendation:** Always follow this review with a full EDA DRC pass in the CAD tool before PCB release.

---

## AI usage rules

- AI performs checks and reports findings — **it does not approve or reject a layout.**
- AI must not claim a design is "correct" or "clean" — only that no failures were detected in the checks performed.
- Findings are always presented to the engineer for disposition.
- If a file is incomplete, truncated, or a section is missing, the AI stops and reports which checks could not be run.

---

## Limitations

- **AI cannot render copper.** All geometric DRC (clearance, width, annular ring from copper, plane integrity) requires an EDA tool.
- **No layer function encoding.** GenCAD `$LAYERS` provides layer names only, not signal/plane/power assignments. Layer function must be inferred from name conventions or confirmed by the engineer.
- **IPC-356 drill sizes are nominal.** Actual manufactured drill sizes may differ by the fab's drill tolerance. Annular ring calculations from IPC-356 are advisory, not DRC-equivalent.
- **AIS flag field** (`YES`/`NO` last column) — interpretation is CAD-tool-specific (may be glue dot, mechanical flag, or no-mount flag). Do not use as mount status without tool documentation. Use the BOM CSV `NoMount` column for mount status.
- **Pour fragment IDs** — PADS/Xpedition assigns internal IDs to copper pour segments (`(Net0)-1` etc.). These inflate the layout net count above the schematic net count. This is normal and must not be misclassified as extra nets.
- **GenCAD route names vs signal names** — named nets use the schematic name directly; copper plane boundaries use parenthesised IDs. Cross-reference using substring matching, not exact equality.

---

## Validation log

| Design | Format | Components | Nets | Checks run | Notes |
|--------|--------|------------|------|------------|-------|
| ESH10000540 R3 (Sparrow FE PCBA) | GenCAD 1.4, IPC-356A, AIS, QCV, BOM CSV, Gerber RS-274X, Excellon | 445 (394 + 51 NM) | 335 (QCV) / 485 (GenCAD) | All 14 checks | 9 Pass, 5 Info, 0 Fail. Key findings: 0.10 mm min aperture; 24 bottom-side components (TVS diodes + standoffs); via annular ring 0.10 mm; all 485 signals routed. See ESH10000540/R3/Review/LAYOUT_REVIEW.md. 2026-05-04. |

**Parser issues found and resolved (2026-05-04):**

1. **IPC-356 record type vs net ID** — initial parsing treated the first 3 characters as a net reference number. Corrected: the first 3 characters are the record type (317 = component pad, 327 = via). Net name starts at column 4.
2. **AIS BOTTOM regex** — initial regex `\bBOT\b` missed BOTTOM-side components because the AIS file uses the full word `BOTTOM`. Corrected: use `\bBOTTOM\b`. Failure to match BOTTOM would cause LR-P02 to report 0 bottom-side components incorrectly.
3. **GenCAD route matching** — initial check used exact equality between signal names and route identifiers, causing all power nets to appear unrouted. Corrected: use substring matching (`-like "*$net*"`) because route identifiers for copper planes include surrounding whitespace or parentheses.
4. **QCV net count regex** — initial regex `^\*NET\*` (PADS ASCII format) produced 0 matches on QCV files. Corrected: QCV format uses `NET :` prefix. Always check the first few lines of the file to confirm the format before applying a count regex.
5. **IPC-356 single-node nets** — copper pour fragments generate one IPC-356 record each (one test point per fragment), making them appear as single-node nets. Filter by name pattern `^\(Net` before reporting orphan pads. After filtering, all remaining single-record entries are real orphan pads.
