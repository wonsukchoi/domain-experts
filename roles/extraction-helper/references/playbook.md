# Playbook

Filled templates for the three recurring extraction-helper tasks: pipe tally on a trip, H2S/gas-alarm response, and blast exclusion-zone calculation. Populate with the day's real numbers — these are executable formats, not descriptions.

## 1. Rig floor tally book (per trip)

Columns, filled for a bit trip at 8,215 ft TD (95 ft BHA):

| Item | Length (ft) | Cumulative (ft) | Notes |
|---|---|---|---|
| BHA (bit + motor + 2 stabilizers + collar) | 95.0 | 95.0 | per BHA report |
| Stand 1 | 92.8 | 187.8 | tallied at pickup |
| Stand 2 | 93.4 | 281.2 | tallied at pickup |
| … | … | … | continue per stand, not per estimate |
| Stand 88 | 92.1 | 8,120.0 | last stand, drill pipe total |
| **Drill pipe total** | | **8,120.0** | must equal TD − BHA |
| **TD (tally book)** | | **8,215.0** | cross-check against driller's counter |

**Trip checkpoint rule:** after every 10 stands pulled and racked, read the fingerboard count aloud to the derrickhand and compare to (stands pulled so far). Any gap gets called immediately — do not wait for end of trip.

**Sign-off line (only after count matches):**
> "[N] of [N] stands racked, BHA at rotary, floor clear. Tally confirmed against depth counter — no discrepancy." / or the discrepancy note format shown in the SKILL.md worked example if one exists.

## 2. Gas-alarm response ladder (H2S / multi-gas)

| Reading | Response | Who acts |
|---|---|---|
| 0–9 ppm H2S | Normal — continue task, log reading at shift start/mid/end | Helper |
| 10 ppm (OSHA action level, low alarm) | Stop task, don SCBA if trained and directed, move upwind, notify driller/company man | Helper + supervisor |
| 20 ppm (OSHA ceiling) | Evacuate to designated muster point, do not re-enter without supervisor clearance and re-test | All personnel in zone |
| 100 ppm (IDLH) | Full evacuation, only SCBA-trained rescue personnel re-enter, well-control/emergency procedure initiated | Emergency response only |

**Rule:** the response tier is set by the monitor reading at the moment of alarm, not by how the air smells or how long you've been on location without a prior alarm. Olfactory fatigue means the nose stops being a reliable indicator well before IDLH.

## 3. Blast exclusion-zone calculation (scaled distance)

Formula: minimum safe distance (ft) = K × √(W), where W = maximum charge weight per delay (lb) and K = scaled-distance factor (state/company-set, commonly 50–60 ft/√lb for structures per USBM RI 8507-derived rules; use the site's permitted K, never assume).

**Worked example, filled:**
- Maximum charge weight per delay this shot: 180 lb
- Site's permitted K for structures: 55
- Minimum safe distance = 55 × √180 = 55 × 13.42 = **738 ft**
- Yesterday's shot used 150 lb/delay → distance was 55 × √150 = 55 × 12.25 = 674 ft
- Today's charge weight increased (180 lb vs. 150 lb) → **yesterday's flag line at 674 ft is short by 64 ft and must be moved out to 738 ft before loading continues.**

**Rule:** recompute per shot, using that shot's actual maximum charge weight per delay from the blast log — never reuse yesterday's flag line on the assumption the pattern is "about the same."
