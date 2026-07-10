# Playbook

Filled worksheets and thresholds for field decisions — populate the numbers, don't redesign the process.

## 1. Mid-section discharge computation worksheet

Formula per vertical: `q = w × d × v` where `w` is the width assigned to that vertical (midpoint between the two adjacent stations), `d` is the measured depth, and `v` is the mean velocity at that vertical (0.6-depth for d < 2.5 ft; average of 0.2- and 0.8-depth for d ≥ 2.5 ft).

| Station | Distance from initial point (ft) | Width, w (ft) | Depth, d (ft) | Velocity method | Mean velocity, v (ft/s) | q = w·d·v (ft³/s) | % of total Q |
|---|---|---|---|---|---|---|---|
| 1 | 4 | 3 | 0.8 | 0.6-depth | 0.9 | 2.16 | 0.6% |
| 2 | 8 | 4 | 1.5 | 0.6-depth | 1.6 | 9.60 | 2.7% |
| 3 | 13 | 5 | 2.4 | 0.6-depth | 2.3 | 27.60 | 7.9% |
| 4 | 18 | 5 | 3.1 | 0.2/0.8-depth | 2.9 | 44.95 | 12.8% |
| 5 | 24 | 6 | 3.6 | 0.2/0.8-depth | 3.3 | 71.28 | 20.3% |
| 6 | 30 | 6 | 3.8 | 0.2/0.8-depth | 3.4 | 77.52 | 22.1% |
| 7 | 36 | 6 | 3.5 | 0.2/0.8-depth | 3.1 | 65.10 | 18.6% |
| 8 | 41 | 5 | 2.9 | 0.6-depth | 2.6 | 37.70 | 10.7% |
| 9 | 45 | 4 | 1.8 | 0.6-depth | 1.7 | 12.24 | 3.5% |
| 10 | 48 | 3 | 0.9 | 0.6-depth | 1.0 | 2.70 | 0.8% |
| **Total** | | **47** | | | | **350.85** | 100% |

Siting rule applied after the fact: any vertical over ~10% of total Q (here, verticals 5–7) flags that the cross-section is under-subdivided for that panel — add a vertical there on the next visit if the site geometry allows it. On a channel this narrow (47 ft), that's noted as an accepted exception rather than re-measured on the spot.

## 2. Measurement quality rating (Sauer & Meyer, 1992)

| Rating | Uncertainty band | Typical conditions |
|---|---|---|
| Excellent | ±2% | Stable stage, ideal cross-section, calibrated ADCP or ≥25-vertical wading measurement |
| Good | ±5% | Stable-to-slowly-changing stage, reasonable cross-section, standard method followed |
| Fair | ±8% | Unstable stage during measurement, imperfect cross-section, or reduced vertical count |
| Poor | >8% | Rapidly changing stage, ice effect, debris, equipment problems during the measurement |

**Decision rule:** compare the measurement-vs-rating deviation to the assigned band. Deviation inside the band → log as agreement, no action. Deviation outside the band on a single visit → flag, schedule a follow-up before touching the rating. Deviation outside the band on 2+ consecutive visits, same direction → apply a shift.

## 3. Rating shift decision table

| Consecutive measurements outside quality band | Direction | Action |
|---|---|---|
| 1 | Either | Flag; schedule follow-up measurement within 2–4 weeks; do not shift yet |
| 2, same direction | Same | Apply a temporary shift equal to the average deviation, effective from the first flagged date; note as provisional |
| 2, opposite directions | — | Treat as measurement noise or a genuinely unstable control (ice, debris, vegetation); investigate site physically before any shift |
| 3+, same direction, growing magnitude | Same | Apply shift; escalate to hydrologist-in-charge for a control-section survey and permanent rating revision |

## 4. Sensor/meter calibration tolerance table

| Instrument | Check method | Acceptable tolerance | Action if exceeded |
|---|---|---|---|
| Price AA / pygmy current meter | Spin test (pre- and post-measurement) | ≤2% deviation from rated spin time | Discard measurement if post-test also fails; re-run with a verified meter |
| pH sensor | Two-point buffer check (e.g., 7.00 / 10.00 SU) | ±0.1 SU | Full two-point recalibration before continuing |
| Specific conductance | Certified standard solution check | ±5% of standard value | Full two-point recalibration; note drift direction for trend tracking |
| Dissolved oxygen | Water-saturated air check against local barometric pressure | ±0.2–0.3 mg/L | Recalibrate against saturation table; verify membrane/cap condition |
| Turbidity | Formazin (or equivalent) standard check | ±5% of standard value | Clean optics, recalibrate; if still failing, flag sensor for lab service |

## 5. Water-quality sample holding times (selected, per 40 CFR 136)

| Analyte | Preservation | Holding time |
|---|---|---|
| Nitrate/nitrite | Cool to ≤6°C | 48 hours |
| BOD (biochemical oxygen demand) | Cool to ≤6°C | 48 hours |
| Total suspended solids | Cool to ≤6°C | 7 days |
| Total phosphorus | Cool to ≤6°C, H2SO4 to pH<2 | 28 days |
| Dissolved metals | Filter in field, HNO3 to pH<2 | 6 months |
| Fecal coliform / E. coli | Cool to ≤6°C | 8 hours to first subculture (24 hr max to analysis start) |

**Field rule:** if delivery to the lab won't beat the holding time, ice/preserve per the table and log the actual elapsed time on the chain-of-custody — a documented exceedance gets the result qualified; an undocumented one gets it silently discredited.

## 6. Storm/event sampling trigger logic

| Trigger type | Setpoint | Sampling interval during rise |
|---|---|---|
| Stage-triggered | Program at baseflow stage + 0.3–0.5 ft rise | Every 15–30 min for first 2 hours of rise, then hourly |
| Time-triggered (no reliable stage threshold) | Program at forecast storm onset − 1 hr | Same as above once triggered |
| Manual backup | Field crew deploys ahead of forecast peak | First bottle at first visible turbidity/stage change, then per interval |

Default to stage-triggered whenever the site has a reliable rating and telemetry; time-triggered is the fallback for ungaged or newly installed sites where the stage threshold hasn't been established yet.
