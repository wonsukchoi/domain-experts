# Playbook

## F:M / SRT / HRT worksheet (activated sludge)

Fill with current shift data; recompute whenever influent flow or MLSS moves more than 10% from the prior sample.

| Field | Formula | Baseline example | Storm example |
|---|---|---|---|
| Flow (MGD) | measured | 3.0 | 6.0 |
| Influent BOD5 (mg/L) | lab/online | 200 | 140 |
| Aeration volume (MG) | fixed | 0.75 | 0.75 |
| MLSS (mg/L) | lab | 3,000 | 2,000 |
| F:M (lb/lb/day) | (Flow × BOD) / (Vol × MLSS) | 0.27 | 0.56 |
| HRT (hr) | Vol / Flow × 24 | 6.0 | 3.0 |
| SRT target (days) | operator-set via wasting rate | 8 | 10 (raised — cut wasting) |
| Functional band | 0.2–0.5 lb/lb/day (conventional) | in-band | over-band, flag |

**Action thresholds:**
- F:M 0.40-0.50: increase sampling frequency, hold wasting rate steady.
- F:M >0.50: cut WAS wasting by 30-50% for 24-48 hr, recheck MLSS and F:M every 12 hr until back in-band.
- F:M <0.15 for more than 2 days: increase wasting — excess biomass with low food is a bulking risk (filamentous growth favors low F:M).

## Chlorine CT compliance table (Surface Water Treatment Rule, Giardia 3-log)

Required CT (mg/L·min) at pH 7.0-7.5 for free chlorine, by water temperature — use the peak-hour instantaneous flow to compute actual contact time (T), never the daily average.

| Temp (°C) | Required CT (mg/L·min), 3-log Giardia |
|---|---|
| 0.5 | 137 |
| 5 | 121 |
| 10 | 100 |
| 15 | 84 |
| 20 | 67 |
| 25 | 55 |

**Worked check:** clearwell baffled volume 0.5 MG, peak hour flow 4.0 MGD → theoretical HRT = 0.5/4.0 × 24 × 60 = 180 min. Baffling factor (unbaffled/poor baffling) T10/T ≈ 0.3 → actual contact time (T10) ≈ 54 min. Residual held at 1.2 mg/L. CT achieved = 1.2 × 54 = 64.8 mg/L·min. At 15°C, required CT is 84 — **this plant is under-crediting** and needs either a higher residual, a longer contact time (raise clearwell level, improve baffling), or a tracer study to confirm the assumed baffling factor is actually that conservative.

## Storm-response wasting-rate schedule (activated sludge, hydraulic surge)

1. **Flow >150% of design average, MLSS trending down >10%/day:** cut WAS wasting 30%, hold RAS (return activated sludge) rate at maximum to keep solids in the aeration train rather than lost to the clarifier overflow.
2. **Flow >200% of design average:** cut WAS wasting 50%, engage flow equalization or step-feed if available to protect clarifier surface overflow rate; increase DO setpoint only if oxygen transfer (not biomass inventory) is confirmed as the limiting factor via a DO profile across the basin.
3. **Post-storm, flow returning to <120% of design average:** hold reduced wasting for one full SRT cycle (typically 24-72 hr depending on baseline SRT) before restoring baseline wasting rate — restoring too early re-triggers the MLSS deficit the reduced wasting was rebuilding.
4. **Recheck cadence during response:** MLSS and F:M every 12 hr; effluent BOD5/TSS grab sample every 24 hr until F:M is back inside the 0.2-0.5 band for two consecutive readings.

## NPDES Discharge Monitoring Report (DMR) — exceedance triage

| Situation | Report as violation? | Deadline |
|---|---|---|
| Single grab sample above a permit value defined as a daily maximum | Yes | Per permit's noncompliance reporting clause; many require 24-hr verbal + 5-day written for events with potential endangerment (40 CFR 122.41(l)(6)) |
| Single grab sample above a permit value defined only as a 7-day or 30-day average, average not yet breached | No — log as internal process upset, note in DMR comments if the state form requires narrative context | End of reporting period (routine DMR submission) |
| Averaging-period calculation (7-day or 30-day) exceeds the permit limit | Yes | Routine DMR submission; escalate to verbal notice if the exceedance also triggers a water-quality standards concern |
| Bypass or upset with no permit exceedance but potential for one | Situational — many permits require notice of bypass/upset regardless of measured outcome | Per permit's bypass/upset notification clause, typically 24 hr |

## Biosolids batch release checklist (40 CFR Part 503)

1. Confirm stabilization process met spec for the batch: digester temperature and retention time (mesophilic anaerobic: typically ≥15 days at ≥35°C for Class B via PSRP) — pull the process log for the specific batch, not a plant-wide average.
2. Pull fecal coliform result: <1,000 MPN/g dry weight (or Salmonella <3 MPN/4g) for Class A; <2,000,000 MPN/g dry weight for Class B.
3. Confirm vector attraction reduction (VAR) method used and documented (e.g., ≥38% volatile solids reduction, or alkaline addition to pH ≥12 for 2 hours holding ≥pH 11.5 for 22 more hours).
4. Match land-application site restrictions to the classification achieved — Class B carries site-access and crop-harvest waiting periods; Class A does not.
5. File the batch's testing and process records before land application, not after — a regulator audit checks the paper trail against the application date.
