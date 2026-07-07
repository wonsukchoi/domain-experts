# Occupational Health and Safety Specialist — Playbook

## TRIR / DART rate calculation

Formula: **Rate = (Count × 200,000) / Total hours worked**. The 200,000 constant normalizes to 100 full-time workers per year (100 × 2,000 hrs).

| Metric | Count | Hours worked | Rate | Notes |
|---|---|---|---|---|
| TRIR (Total Recordable Incident Rate) | 14 recordables | 612,000 | 4.58 | All OSHA-recordable injuries/illnesses |
| DART (Days Away/Restricted/Transfer) | 6 DART cases | 612,000 | 1.96 | Subset of recordables with lost/restricted time — severity signal |
| LTIR (Lost Time Incident Rate) | 3 lost-time cases | 612,000 | 0.98 | Most severe subset |

**Reading the spread:** TRIR 4.58 vs DART 1.96 means ~43% of recordables involved lost/restricted time — check this ratio against facility history; a rising DART share at flat TRIR means severity is increasing even if frequency isn't.

## Noise dose → TWA conversion (OSHA 5-dB exchange rate)

```
TWA (dBA) = 16.61 × log10(Dose% / 100) + 90
```

| Measured dose | TWA | vs. 85 dBA action level | vs. 90 dBA PEL |
|---|---|---|---|
| 50% | 85.0 dBA | At action level | Below PEL |
| 100% | 90.0 dBA | Above | At PEL |
| 155% | 93.2 dBA | Above | **Exceeds PEL** |
| 200% | 95.0 dBA | Above | Exceeds PEL — engineering controls required |

Feasibility review triggers automatically at 100% dose (PEL exceedance) — hearing conservation program alone (audiometric testing + hearing protection) is not a substitute for evaluating feasible engineering controls at this threshold.

## Hierarchy-of-controls costing template

| Rank | Control type | Example (Station 4 noise) | Cost | Time to implement | Exposure reduction |
|---|---|---|---|---|---|
| 1 | Elimination | Retire the stamping process entirely | N/A | N/A | 100% — rarely feasible |
| 2 | Substitution | Replace pneumatic ejector with hydraulic | $61,000 | 8 weeks | ~8 dB |
| 3 | Engineering | Acoustic die enclosure | $34,000 | 6 weeks | ~12 dB |
| 3 | Engineering | Operator relocation + remote control | $9,500 | 2 weeks | ~6 dB (distance) |
| 4 | Administrative | Job rotation to limit shift-length exposure | $0 | Immediate | Reduces dose-hours, not source |
| 5 | PPE | Double hearing protection (plug + muff) | ~$200/worker/yr | Immediate | Depends on fit/compliance |

**Selection rule:** recommend the highest-ranked option that is technologically and economically feasible for this specific operation; state explicitly which lower-rank control bridges the gap until the permanent fix lands.

## Root-cause investigation format (5-Why, filled example)

**Incident:** Employee STS (Standard Threshold Shift) flagged on annual audiogram, Press Station 4.

1. **Why did the STS occur?** → Operator was exposed to 93.2 dBA TWA, above the 90 dBA PEL.
2. **Why was exposure above PEL?** → 2022 ejector retrofit changed the noise source profile; no re-sampling occurred after the change.
3. **Why wasn't it re-sampled after the retrofit?** → Facility noise-sampling program runs on a fixed 3-year cycle with no trigger for equipment modifications.
4. **Why is there no modification trigger?** → EHS program was designed around a calendar cadence, not an event-based cadence.
5. **Root cause:** Sampling program lacks an equipment-change trigger — fix the program, not just this station.

## Incident investigation report — filled excerpt

```
FINDING: Press Station 4 noise exposure — 93.2 dBA TWA, exceeds 90 dBA PEL.
Classification: STS recordable, sampling-interval failure (not PPE non-compliance).

Data:
- Personal dosimetry: 155% dose, full 8-hr shift, [date]
- Prior sampling: [date, 3+ years prior] — pre-retrofit baseline
- PPE compliance record: 98% wear rate, current fit-test on file

Recommended controls (by hierarchy):
1. Immediate — double hearing protection, effective [date]
2. 2 weeks / $9,500 — operator relocation, remote ejector control
3. Pending capital approval / $34,000 — acoustic die enclosure

Root cause: noise re-sampling cycle (3yr) has no equipment-modification
trigger. Corrective action: add modification-triggered re-sampling
within 12 months of any equipment change. Owner: EHS Manager. Due: [date].

Residual risk: Stations 1-3 (same ejector model) unassessed post-retrofit.
Sampling scheduled within 30 days — tracked as separate action item.
```
