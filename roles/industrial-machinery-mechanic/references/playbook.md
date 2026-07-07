# Playbook

Filled worksheets and tables a mechanic actually runs, not descriptions of them — adapt the numbers to the asset in front of you.

## 1. Vibration-trend triage table

Run this against the last 6 months of route data before deciding urgency. Class II example (15–75 kW, rigid foundation) — substitute the machine-class zone boundaries from ISO 10816-3/20816-3 for other classes.

| Class II zone boundary | Overall velocity (mm/s RMS) | Meaning |
|---|---|---|
| Zone A | ≤ 0.71 | New-machine condition |
| Zone B | ≤ 1.8 | Acceptable for unrestricted long-term operation |
| Zone C | ≤ 4.5 | Unsatisfactory for long-term operation — plan repair |
| Zone D | > 4.5 | Damage-risk — restrict operation, expedite |

**Trend-slope decision, given current zone:**

| Current zone | Flat ≥90 days | Rising, crossed a zone in <60 days |
|---|---|---|
| B | Monitor at current cadence | Increase reading frequency, investigate spectrum |
| C | Schedule at next planned window | Schedule this week, size cost tradeoff (below) |
| D | Investigate before next production run | Stop and investigate now regardless of schedule |

## 2. Frequency-domain triage (spectrum read)

| Dominant peak location | Likely mode | Confirming check |
|---|---|---|
| 1X running speed, radial | Imbalance | Phase readings 90° apart on same bearing should be in phase for pure imbalance |
| 2X running speed, radial + axial component | Angular misalignment | Laser alignment check at coupling |
| 1X running speed, high axial only | Parallel misalignment or bent shaft | Laser check + shaft runout with dial indicator |
| 3X, 4X, 5X harmonics with broadband noise floor | Looseness (bolted joint, baseplate, bearing fit) | Visual/tap test on mounting bolts, bearing fit check |
| BPFO/BPFI with 1X sidebands, low amplitude | Bearing defect, stage 1–2 (early) | Trend amplitude monthly; not yet urgent |
| BPFO/BPFI with sidebands, amplitude >2x baseline noise floor, harmonics of BPFO present | Bearing defect, stage 3 (advancing) | Schedule replacement within weeks, not months |
| Broadband high-frequency "haystack" with no discrete peaks | Bearing defect, stage 4 (imminent) or lubrication starvation | Stop and inspect before next run if criticality is high |

Bearing defect frequencies (BPFO, BPFI, BSF, FTF) are geometry-specific — pull them from the bearing manufacturer's data sheet or calculate from bore/pitch/ball diameter and contact angle; don't reuse another bearing's frequencies even if the model number looks similar.

## 3. Laser alignment tolerance table (flexible coupling, by RPM)

Offset tolerance tightens as RPM increases — the same 8 mils that's marginal at 900 rpm is grossly out of tolerance at 3600 rpm.

| RPM | Offset tolerance (mils) | Angularity tolerance (mils/inch of coupling spacing) |
|---|---|---|
| 900 | 0.006–0.009 | 0.7 |
| 1800 | 0.004–0.006 | 0.5 |
| 3600 | 0.002–0.003 | 0.3 |
| 7200+ | 0.0015 | 0.2 |

(Values per Piotrowski's *Shaft Alignment Handbook* general tolerance tables — verify against the specific coupling manufacturer's tolerance chart for rigid or disc couplings, which run tighter than the flexible-elastomeric figures above.) Always check soft foot (indicator movement >0.002 in when a mounting bolt is loosened one at a time) before trusting an alignment reading — correcting alignment over an uncorrected soft foot won't hold.

## 4. RCM failure-mode worksheet (filled example — 100 hp fan motor/gearbox)

| Failure mode | Effect if it happens | Detection method | Consequence category | PM strategy |
|---|---|---|---|---|
| DE bearing wear (misalignment-driven) | Bearing seizure, line down | Vibration route (monthly) + laser alignment (quarterly) | Production-critical, high cost | Condition-based (vibration + scheduled alignment check) |
| Gearbox oil contamination | Accelerated gear wear, eventual tooth failure | Oil sample (quarterly): ISO 4406, PQ index | Production-critical, high cost | Condition-based (oil analysis) |
| Coupling elastomer wear | Increased vibration, eventual coupling failure | Visual at PM + vibration trend | Moderate cost, some warning | Fixed-interval replacement (24 months) |
| Motor winding insulation degradation | Motor trip, rewind or replace | Thermography (quarterly) + insulation resistance test (annual) | High cost, some warning | Condition-based |
| Non-critical spare pump seal wear | Redundant pump down, no production impact | Visual leak check at rounds | Low cost, redundant asset | Run-to-failure |

**Criticality score used to sort the queue:** downtime cost/hour × annual failure probability. This asset: $8,200/hr × 0.15 (estimated annual failure probability at current trend) = $1,230 expected annual loss exposure before mitigation — high enough to justify the condition-based strategy above rather than run-to-failure.

## 5. PM-interval-from-MTBF worksheet

1. Pull the last 24 months of CMMS failure records for the asset class (e.g., "100–150 hp process fan bearings, this plant").
2. Compute demonstrated MTBF: total run-hours across the fleet of that asset class ÷ number of failures. Example: 6 identical fans, 24 months, 3 bearing failures across the fleet, ~6,500 run-hours/fan/year → (6 × 2 × 6,500) / 3 ≈ 26,000 hours MTBF.
3. Set the PM/inspection interval at 0.5–0.7× MTBF: 13,000–18,200 hours, tightened toward the low end if the environment (dust, moisture, vibration-prone mounting) is worse than the fleet average.
4. Convert to a calendar interval at expected annual run-hours (6,500 hrs/yr here): 13,000/6,500 ≈ 2 years, 18,200/6,500 ≈ 2.8 years — set the inspection at every 24 months, not the vendor's generic 36-month default.
5. Revisit the MTBF calculation annually; a single new failure in a 6-unit fleet moves the estimate materially and the interval should move with it.
