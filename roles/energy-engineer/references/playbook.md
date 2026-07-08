# Playbook

Filled tables, formulas, and worked mini-calculations an energy engineer runs against during a commercial or industrial energy audit. Verify current utility rates, degree-day normals, and AHRI-certified performance data before citing in a stamped calculation — these are commonly applied methods and named standards, not a substitute for project-specific source data.

## 1. ASHRAE audit level comparison

| Level | Scope | Typical deliverable | Accuracy | When required |
|---|---|---|---|---|
| I — Walk-through | Utility bill analysis, visual survey, no-cost/low-cost measures only | Benchmarking report, prioritized list of buildings/systems for deeper study | +/-30-50% | Portfolio screening before committing audit budget to a specific site |
| II — Detailed/General | Instrumented spot measurements, end-use breakdown, full ECM list with cost/savings/payback per measure | ECM-by-ECM engineering analysis with SIR ranking | +/-15-25% | Standard basis for a capital commitment decision |
| III — Investment-grade | Calibrated simulation (ASHRAE Guideline 14 tolerance) or detailed sub-metered analysis, contract-ready savings numbers | Investment-grade audit report suitable for ESPC guarantee terms | +/-10% | ESPC-guaranteed-savings contracts, large capital projects, or where financing requires bankable numbers |

**Rule:** don't quote a Level 2 report's payback numbers into an ESPC guarantee clause — the accuracy band doesn't support a contractual guarantee; re-run as Level 3 first.

## 2. Envelope degree-day calculation — worked example (warehouse wall, distinct from SKILL.md's roof case)

**Building:** unconditioned metal-building warehouse, Chicago, IL, gas unit heaters only (no cooling — heating-only calc). Existing wall: insulated metal panel, R-13 nominal, 8,000 ft2 wall area. Retrofit: continuous insulation overlay to R-25.

- U1 = 1/13 = 0.0769 Btu/hr-ft2-F; U2 = 1/25 = 0.0400; delta-U = 0.0369.
- NOAA climate-normal HDD65 for Chicago (O'Hare station, verify current normal) approx. 6,300.
- Q saved = 24 x HDD x A x delta-U = 24 x 6,300 x 8,000 x 0.0369 = 44,634,240 Btu/yr = 446.34 therms of delivered heat.
- Unit heater efficiency 80% AFUE: gas input saved = 446.34 / 0.80 = 557.93 therms/yr.
- At an industrial gas rate of $0.95/therm: cost savings = 557.93 x 0.95 = **$530/yr**.
- Installed cost (full wall retrofit, panel + labor): 8,000 x $4.25/ft2 = $34,000. Simple payback = 34,000 / 530 = **64.2 years**.

**Rule:** a standalone envelope measure at full installed cost frequently doesn't pencil (as here) — check whether the component is being replaced or re-skinned on its own schedule regardless of the energy decision, and re-cost at the incremental delta only, the way SKILL.md's roof case does. A measure rejected on full-cost basis can still be worth doing on incremental-cost basis.

## 3. HVAC/refrigeration efficiency metric reference

| Metric | Definition | Test standard | Applies to | Formula |
|---|---|---|---|---|
| SEER | Seasonal cooling output / seasonal energy input, part-load weighted across standard temperature bins | AHRI 210/240 | Unitary DX equipment <65,000 Btu/hr (about 5.5 tons) | SEER = sum(cooling output, Btu) / sum(energy input, Wh) |
| EER | Full-load Btu/hr output per Watt input at one design condition (95F outdoor / 80F indoor, 67F wb) | AHRI 210/240, 340/360 | Any DX cooling equipment — single full-load rating point | EER = (Btu/hr) / W |
| IEER | Integrated Energy Efficiency Ratio — weighted average of EER at 100/75/50/25% load points, replaces IPLV for commercial unitary equipment | AHRI 340/360 | Unitary/packaged equipment >=65,000 Btu/hr | IEER = 0.020A + 0.617B + 0.238C + 0.125D (A/B/C/D = EER at 100/75/50/25% load) |
| COP | Coefficient of Performance — output/input in matching units | AHRI 550/590 (chillers), AHRI 210/240 (heat pump heating mode) | Chillers, heat pumps | COP = Q_out(kW) / P_in(kW) = EER / 3.412 |
| kW/ton | Chiller-plant benchmarking metric, inverse of COP scaled to tons | Derived | Chiller plants | kW/ton = 3.517 / COP |

**Worked conversion:** a chiller rated 0.62 kW/ton → COP = 3.517 / 0.62 = 5.673 → EER = 5.673 x 3.412 = **19.36**. Comparing that 19.36 EER against a competing unit's quoted SEER number would repeat the exact metric-mismatch error the RTU naive read makes in SKILL.md — convert both sides to the same metric before ranking.

## 4. IPMVP M&V option selection matrix

| Option | Measurement boundary | Method | Best for | Typical uncertainty driver |
|---|---|---|---|---|
| A — Retrofit isolation, key parameter | Single ECM/system | Measure 1+ key parameters short-term or continuously; stipulate the rest | Lighting retrofits, fixed-load equipment swaps with stable, well-documented operating hours | Accuracy of the stipulated (unmeasured) parameter |
| B — Retrofit isolation, all parameters | Single ECM/system | Measure all relevant parameters, short-term or continuous | Variable-load equipment (RTUs, VFDs) where stipulation would be inaccurate | Metering duration and coverage of the full load range |
| C — Whole facility | Entire utility meter | Utility billing regression against a driving variable, pre- vs. post-retrofit | Multiple interacting ECMs installed together that can't be isolated | Non-ECM-related usage changes (occupancy, added load, production rate) |
| D — Calibrated simulation | Entire facility or major subsystem | Energy model calibrated to actual billing per ASHRAE Guideline 14 (CV(RMSE) <=15% monthly / 5% annual NMBE within +/-5% annual) | New construction, or when no valid pre-retrofit baseline period exists | Model calibration quality |

**Rule:** the option is chosen by whether the ECM's key parameter can be isolated with dedicated metering, not by which option the audit template defaults to — Option C on a single easily-isolated measure buries a small real signal in whole-facility noise; Option D on a simple, well-metered single measure spends model-calibration effort a lighter option would cover.

## 5. ECM bundle ranking — simple payback vs. SIR (7% discount rate)

SIR = PV(annual savings over measure life) / installed cost, where PV factor = [1 - (1+r)^-n] / r.

| ECM | Installed cost | Annual $ savings | Measure life (yr) | Simple payback (yr) | PV factor (7%) | SIR |
|---|---|---|---|---|---|---|
| BAS/controls optimization | $22,000 | $6,400 | 8 | 3.44 | 5.971 | **1.74** |
| LED lighting retrofit | $45,000 | $9,800 | 12 | 4.59 | 7.943 | **1.73** |
| VFDs on supply fans | $28,000 | $5,100 | 12 | 5.49 | 7.943 | **1.45** |
| Roof insulation (incremental basis) | $15,000 | $1,815 | 20 | 8.26 | 10.594 | **1.28** |
| RTU replacement | $180,000 | $10,997 | 15 | 16.37 | 9.108 | **0.56** |

**Rule:** the RTU replacement has the largest absolute dollar savings and a payback (16.37 yr) close to but under its 15-year measure life, yet its SIR is below 1.0 — it destroys value on a discounted basis over its own service life. Ranked by payback alone it looks mid-pack; ranked by SIR it's last. When the two rankings disagree this sharply, present both to the capital decision-maker explicitly rather than defaulting to whichever ranking favors the largest project.

## 6. ESPC guarantee true-up calculation

**Formula:** True-up owed by ESCO to owner = max(0, Guaranteed savings - Measured savings) x applicable rate. Savings measured above the guarantee typically accrue to the owner under standard ESPC risk allocation, not as an additional payment to the ESCO, unless the contract states a shared-savings clause.

**Worked example (lighting-only ESPC, distinct from SKILL.md's RTU/roof case):** Guaranteed annual savings 220,000 kWh (IPMVP Option A, stipulated fixture wattage x metered annual operating hours). Year-3 measured: metered operating hours applied to as-built fixture wattage give 198,500 kWh. Shortfall = 220,000 - 198,500 = 21,500 kWh. Year-3 blended utility rate (escalated 2%/yr per the contract's stated escalation clause from a $0.105/kWh baseline) = $0.115/kWh. True-up owed = 21,500 x $0.115 = **$2,472.50**, invoiced to the ESCO per the contract's annual reconciliation clause.
