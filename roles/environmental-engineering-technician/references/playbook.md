# Playbook

Filled reference tables and worked calculations for the four recurring technician tasks: holding-time/preservation lookup, field meter calibration, flow-proportional composite pacing, and isokinetic stack sampling. Numbers are illustrative of the cited source's structure — verify current edition and project-specific QAPP values before use in a real compliance submission.

## 1. Holding time and preservation quick table (40 CFR 136, Table II — common NPDES/drinking-water analytes)

| Analyte | Container | Preservative | Holding time |
|---|---|---|---|
| pH | Field-measured | None | Analyze immediately (no shippable hold) |
| Dissolved oxygen (probe) | Field-measured | None | Analyze immediately; Winkler-azide fixation extends to ~8 hr if fixed on site |
| Temperature | Field-measured | None | Analyze immediately |
| Residual chlorine | Field-measured | None | Analyze immediately (~15 min practical window) |
| BOD5 / CBOD5 | Plastic/glass | Cool ≤6°C | 48 hours |
| Hexavalent chromium (Cr6+) | Plastic/glass | Cool ≤6°C | 24 hours |
| Fecal coliform / E. coli | Sterile plastic | Cool ≤6°C | 6-8 hours (verify state primacy agency) |
| TSS | Plastic/glass | Cool ≤6°C | 7 days |
| COD | Plastic/glass | Cool ≤6°C, H2SO4 to pH<2 | 28 days |
| Oil & grease / TPH | Glass | Cool ≤6°C, HCl or H2SO4 to pH<2 | 28 days |
| Total phosphorus | Plastic/glass | Cool ≤6°C, H2SO4 to pH<2 | 28 days |
| Nitrate | Plastic/glass | Cool ≤6°C | 48 hours (unpreserved) |
| Nitrate-nitrite | Plastic/glass | Cool ≤6°C, H2SO4 to pH<2 | 28 days |
| TOC | Glass | Cool ≤6°C, HCl or H2SO4 to pH<2 | 28 days |
| VOCs (water) | Glass, zero headspace | HCl to pH<2, cool ≤6°C | 14 days (7 days if unpreserved) |
| SVOCs (extractables) | Amber glass | Cool ≤6°C | 7 days to extraction, 40 days extraction-to-analysis |
| Metals, total recoverable (except Hg, Cr6+) | Plastic | HNO3 to pH<2 | 6 months (180 days) |
| Mercury, total | Plastic | HNO3 to pH<2 | 28 days |

**Rule for reading this table:** the clock starts at collection time, not lab receipt. For a two-stage analyte (SVOCs), both clocks apply independently — a sample extracted on day 6 still has the full 40-day analysis window from the extraction date, not the collection date.

## 2. pH meter calibration log (filled example, 3-point)

| Step | Buffer | Nominal pH | Reading (mV) | Notes |
|---|---|---|---|---|
| Cal point 1 | pH 4.01 | 4.01 | +176.4 mV | Fresh buffer, lot #, exp. date checked |
| Cal point 2 | pH 7.00 | 7.00 | +3.2 mV | Near-zero expected at true 7.00 |
| Cal point 3 | pH 10.01 | 10.01 | −170.5 mV | |
| Slope calc | — | — | (176.4−(−170.5))/(10.01−4.01) = 57.82 mV/pH unit | |
| Theoretical (Nernst) | — | — | 0.1984 × T(K) mV/pH unit | At 21°C (294.15 K): 58.36 mV/pH unit |
| % of theoretical | — | — | 57.82 / 58.36 = 99.1% | PASS if within QAPP's stated band (commonly 95-105%) |
| Post-use check | pH 7.00 | 7.00 | Reads 6.89 SU | Drift = 0.11 SU vs. ±0.10 SU tolerance → **FAIL, data invalidated since last pass** |

## 3. Dissolved oxygen meter — saturated-air calibration

Membrane/optical DO meters are commonly calibrated against water-saturated air (100% saturation), corrected for local barometric pressure and temperature, per Standard Methods 4500-O G:

1. Read local barometric pressure (e.g., 745 mmHg) and air temperature at the meter (e.g., 21°C).
2. Look up the table DO saturation value at 21°C, sea-level/760 mmHg (Standard Methods Table 4500-O:I): approximately 8.90 mg/L.
3. Correct for actual barometric pressure: DO_sat(corrected) = DO_sat(table) × (P_local / 760) = 8.90 × (745/760) = **8.71 mg/L**.
4. Set the meter's calibration value to 8.71 mg/L in saturated air; acceptance is typically the meter reading within ±0.2 mg/L (or ±3%) of the corrected value before proceeding.
5. Log the barometric pressure and correction used — a DO calibration with no barometric correction recorded is not independently checkable later.

## 4. Flow-proportional composite pacing — worked calc

Permit-specified pacing: 200 mL aliquot per 15,000 gallons of metered flow, 15 L compositing container, 24-hour event.

| Interval | Δ flow (gal) | Aliquots (Δflow ÷ 15,000) | Volume (mL) |
|---|---|---|---|
| 00:00–04:00 | 135,000 | 9 | 1,800 |
| 04:00–08:00 | 75,000 | 5 | 1,000 |
| 08:00–12:00 | 225,000 | 15 | 3,000 |
| 12:00–16:00 | 180,000 | 12 | 2,400 |
| 16:00–20:00 | 180,000 | 12 | 2,400 |
| 20:00–24:00 | 105,000 | 7 | 1,400 |
| **Total** | **900,000** | **60** | **12,000 (12.0 L)** |

Container margin: 15 L − 12.0 L = 3.0 L (20%). If a flow-meter fault interrupts pacing for part of an interval, switch to time-proportional pacing for the affected window only, log the switch (start/stop time, reason, meter fault code if available) on the field log, and note the deviation on the chain of custody — do not back-calculate a "corrected" flow-proportional volume for the gap.

## 5. Isokinetic sampling ratio — stack testing (EPA Method 5 framework)

Isokinetic sampling means the velocity of gas entering the sample nozzle matches the velocity of the surrounding stack gas, so the sample isn't biased toward or away from entrained particulate. The isokinetic ratio (%I) is checked *after* the run, not assumed during it:

**%I = 100 × (Vm,std × K × Ts,avg) / (Vs × θ × Ps × An)**

Where Vm,std = sample gas volume at standard conditions, Ts,avg = average stack temperature, Vs = average stack gas velocity, θ = sampling time, Ps = stack static pressure, An = nozzle cross-sectional area, K = a units-conversion constant per EPA Method 5. In practice, technicians use the field data sheet's pre-calculated worksheet rather than deriving the formula on site — the value that matters operationally is the result:

- **Acceptance: 90% ≤ %I ≤ 110%** (EPA Method 5 run-validity criterion). A run outside this range is invalid and must be repeated, regardless of how clean the particulate catch looks.
- A %I well above 110% (super-isokinetic) under-samples large particulate — the gas is drawn in slower than stack velocity, so larger particles miss the nozzle by inertia and the reported concentration is biased low.
- A %I well below 90% (sub-isokinetic) over-samples large particulate — the reported concentration is biased high.
- If a run's %I falls outside 90-110%, check first for a nozzle sized wrong for the expected stack velocity range or a leak-check failure before repeating the run with the same setup.

## 6. QC blank and duplicate acceptance — quick reference

| QC type | Purpose | Common acceptance criterion |
|---|---|---|
| Field (equipment/rinsate) blank | Detects contamination from sampling equipment | Result < method reporting limit (RL) |
| Trip blank (VOCs only) | Detects contamination during transport/storage | Result < RL; required in every VOC cooler |
| Field duplicate | Measures total (sampling + analytical) precision | RPD ≤ ~20% (water), ≤ ~35% (soil/sediment) — project QAPP governs exact number |
| Matrix spike / matrix spike duplicate | Measures analytical accuracy/precision in the sample matrix | Recovery within lab-established control limits (often 75-125%, method-specific) |

A field blank result above the RL means the sampling process itself (not the source water) may be the contaminant source — check equipment decontamination and container lot before trusting any positive detect in the associated sample batch.
