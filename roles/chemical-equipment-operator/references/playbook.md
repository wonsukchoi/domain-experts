# Playbook

## Exotherm-response worksheet

Fill during any exothermic reagent addition; retain with the batch record.

| Field | Value |
|---|---|
| Batch # | 6604 |
| Reagent | A |
| Total planned quantity | 200 kg |
| Planned duration / rate | 90 min / 2.22 kg/min |
| Temp spec | ≤45°C |
| Cumulative added at deviation | 112 kg |
| Elapsed time at deviation | 45 min |
| Temp at deviation | 48°C (3°C over spec) |
| Trend: stable elevated or actively rising? | Actively rising — STOP triggered |
| Action taken | Addition stopped; cooling increased |
| Peak temp during hold | 49.5°C at t=48 min |
| Temp returned to spec at | 44°C at t=55 min |
| Resumed addition rate | 1.6 kg/min (vs. original 2.22 kg/min) |
| Remaining quantity / new duration | 88 kg / 55 min |
| Total batch time (actual vs. planned) | 110 min vs. 90 min planned |
| Analytical release testing required? | Y — temperature excursion occurred |

## Batch deviation disposition table

| Deviation type | Default disposition |
|---|---|
| Sequence deviation (reagent added out of order) | Hold for process chemistry evaluation before any analytical decision — order can determine reaction pathway |
| Temperature excursion during addition | Hold for analytical impurity-profile test before release, regardless of visual/physical inspection result |
| Timing deviation (addition faster/slower than spec, no temp excursion) | Evaluate against known process sensitivity; may be low-impact if temperature stayed in spec throughout |
| Quantity deviation (over/under-charge) | Hold for recalculation of expected yield/stoichiometry and analytical verification |
| Equipment/instrumentation deviation (e.g., a sensor fault suspected) | Verify instrumentation before trusting any other reading from the same event; may require re-test with verified instrumentation |

**Rule:** "batch looks fine visually" is never sufficient disposition on its own for a documented deviation — pair it with the appropriate analytical or chemistry-based evaluation before release.

## Lockout/tagout and containment readiness checklist

1. Before any equipment entry/service: confirm hazardous energy sources (electrical, mechanical, chemical, pressure) are isolated per LOTO procedure — do not rely on visual assessment of "looks empty/purged."
2. Verify purge/clearance status through the procedure's specified method (gas testing, pressure verification), not assumption.
3. Confirm lock/tag is applied by the person performing the work, with group lockout procedures followed if multiple workers are involved.
4. On a scheduled interval (per facility EHS program): verify secondary containment integrity (dikes, basins, double-wall systems) — check for damage, blocked drains, correct valve positions.
5. Verify spill response kit contents, expiration/condition, and correct sizing for the chemicals present in the area — not just presence of a kit.
6. Document all verification steps with timestamp and signature before proceeding with entry/service or closing out the readiness check.
