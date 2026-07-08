# Process Playbook

Filled run templates for the four process families a nanofab technician executes most: RCA wet clean, ALD deposition, AFM metrology, and cleanroom/exposure verification. Populate the tables in place; don't paraphrase them into prose in a log.

## 1. RCA wet-clean run log (SC1 / SC2 / piranha)

Fill this table before touching chemistry. Ratios and temperature bands are the process — deviations get logged, not eyeballed.

| Field | SC1 (APM) | SC2 (HPM) | Piranha (SPM) |
|---|---|---|---|
| Ratio (NH4OH : H2O2 : H2O) | 1 : 4 : 20 | HCl:H2O2:H2O = 1:1:6 | H2SO4:H2O2 = 4:1 |
| Nominal temp | 80°C | 80°C | 120°C |
| Controlled-etch tight band (exposures >60 min) | 55–75°C | n/a | n/a |
| Nominal exposure | 10 min | 10 min | 10–15 min |
| Purpose | Organic/particle removal, light oxide etch | Metallic-ion removal | Heavy organic strip |
| Bath temp at start | ___ °C (log) | ___ °C | ___ °C |
| Bath temp at exposure midpoint | ___ °C | ___ °C | ___ °C |
| Bath temp at end | ___ °C | ___ °C | ___ °C |
| Pass/fail vs. band | Pass if within band above for full exposure | | |

**Escalation rule:** any single reading outside the logged band by >2°C → hold exposure timer, re-check thermocouple calibration, do not extend run time to compensate. Two consecutive out-of-band readings on the same bath → abort run, tag bath for engineer review before next use.

## 2. ALD run-health checkpoint template

Run at every scheduled ellipsometry/witness-wafer checkpoint (typically every 100 cycles or per recipe spec, whichever is tighter).

| Checkpoint | Cycles run | Cumulative thickness (Å) | Observed GPC (Å/cycle) | Qualified GPC (Å/cycle) | Δ from qualified | Action |
|---|---|---|---|---|---|---|
| 0 (baseline) | 0 | 0.0 | — | 0.650 | — | Proceed |
| 1 | 100 | 55.0 | 0.550 | 0.650 | −15.4% | >10% → verification sub-run required |
| Verification sub-run | +20 | +10.4 | 0.520 | 0.650 | −20.0% | Confirms decline → pause, flag delivery system |
| 2 (post-service) | +20 | ___ | ___ | 0.650 | ___ | Resume only if GPC within ±5% of qualified |

**Drift-response thresholds:**
- GPC within ±5% of qualified value → continue on original cycle program.
- GPC 5–10% off qualified value → flag for next checkpoint, no run pause.
- GPC >10% off qualified value → run 20-cycle verification sub-run before any decision.
- Two consecutive checkpoints (scheduled or verification) trending the same direction → pause run, escalate to process engineer for precursor/valve inspection before resuming.
- After service, do not resume the original cycle count — re-qualify GPC via a fresh 20-cycle check and recompute remaining cycles from the re-qualified rate.

**Remaining-cycles formula (use latest confirmed rate, never nominal, once drift is confirmed):**
`remaining_cycles = ceil((target_thickness_Å − thickness_deposited_so_far_Å) / latest_confirmed_GPC)`

## 3. Lithography step sequence (optical, generic node)

1. **Substrate prep** — dehydration bake 120°C / 5 min, HMDS prime (vapor or spin, per recipe). Log bake oven temp at start and end; >±3°C from setpoint → re-bake.
2. **Resist spin** — target thickness per recipe (e.g., 1.2 µm at 3000 rpm / 45 s). Measure thickness on a monitor wafer; >5% off target → re-spin, do not proceed to expose.
3. **Soft bake** — per resist spec (e.g., 90°C / 60 s). Log actual hot-plate temp, not setpoint.
4. **Alignment & exposure** — verify alignment marks within tool spec (typically ≤0.25 µm overlay) before committing exposure dose. Log dose (mJ/cm²) actually delivered, read off tool log, not assumed from recipe.
5. **Post-exposure bake (chemically amplified resists only)** — per spec; skipping or under-time this step is a common silent failure — log explicitly even when "n/a."
6. **Develop** — fixed time per recipe (e.g., 60 s single-puddle); log actual develop time, not nominal.
7. **CD/profile check** — measure critical dimension against target ± tolerance (e.g., 90 nm ± 9 nm, 10%). Out of tolerance → hold lot, do not proceed to etch, escalate per Decision framework step 6.

## 4. AFM probe-wear tracking log

| Probe model | Spec tip radius (new) | Spec max (end-of-life) | Hours in use | Last measured resolution feature (nm) | Trend vs. prior 3 sessions | Action |
|---|---|---|---|---|---|---|
| Bruker ScanAsyst-Air | 2 nm nominal | 8 nm max | ___ | ___ | flat / degrading | Swap if degrading + hours > mfr guidance |
| Bruker RTESP-300 | 8 nm nominal | 12 nm max | ___ | ___ | flat / degrading | Swap if degrading + hours > mfr guidance |

**Rule:** resolution loss that tracks with cumulative probe hours (not with sample change) is a consumable swap, logged as such — not written up as a process or sample anomaly.

## 5. ISO 14644-1 cleanroom classification verification

| Class | Max particles/m³ at ≥0.5 µm | Max particles/m³ at ≥0.3 µm |
|---|---|---|
| ISO 5 | 3,520 | 10,200 |
| ISO 6 | 35,200 | 102,000 |
| ISO 7 | 352,000 | n/a (not specified) |

**Sequence:**
1. Confirm particle counter calibration is current (annual, per manufacturer) before use.
2. Sample at the number of locations required by the bay's rated area (per ISO 14644-1 Annex A sampling-location formula), not a single spot check.
3. Compare each location's reading against the class threshold table above — one location over threshold fails the whole zone's current classification, even if the average is under.
4. Log date, counter serial/cal-due date, per-location readings, and pass/fail. Do not carry forward a prior classification without a current reading on file.
5. Fail → notify facilities/EHS before resuming particle-sensitive work in that bay; do not self-waive.

## 6. NIOSH air-sampling documentation template

> **Material sampled:** [e.g., MWCNT, ultrafine TiO2]
> **Method:** [NIOSH method number]
> **Duration:** [8-hr TWA / task-length, specify]
> **Result:** ___ µg/m³ (or mg/m³)
> **Limit referenced:** [e.g., NIOSH REL 1 µg/m³ respirable elemental carbon — CNT/CNF; note explicitly: no OSHA PEL exists for this material]
> **Limit type:** REL (recommended, not enforceable) / vendor SDS limit / OSHA PEL (if one exists)
> **Disposition:** [under REL — treat as "not detected at measurement floor," not proof of safety, per First-principles core #1] / [over REL — stop work in area, escalate to EHS]

Every sampling result gets filed with the limit type spelled out — a safety reviewer reading only the number, without the REL/PEL distinction, will assume regulatory force that doesn't exist.
