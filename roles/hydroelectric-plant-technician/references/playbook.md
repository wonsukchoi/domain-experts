# Playbook

## Head-to-operating-range recalculation worksheet

Fill whenever reservoir head changes meaningfully.

| Field | Value |
|---|---|
| Unit | Unit #H-2 |
| Reference head | 100 ft |
| Reference safe/efficient flow range | 800-1,200 cfs |
| Current head | 85 ft (-15%) |
| Recalculated safe/efficient flow range at current head | 600-900 cfs |
| Prior flow setpoint | 1,000 cfs |
| Status vs. new range | OUTSIDE (above 900 cfs max) — cavitation risk |
| Adjusted flow setpoint | 750 cfs (within new range) |
| Estimated output impact | ~15-20% reduction vs. 1,000 cfs at proper head |
| Environmental minimum flow | 400 cfs — confirmed satisfied at 750 cfs |

**Rule:** never hold a flow setpoint unchanged across a meaningful head change — recalculate the safe/efficient range for the new head using the turbine's characteristic curves before setting the new operating point.

## Governor tuning verification checklist

1. Confirm the governor's current deadband and response speed settings against specification.
2. Perform or review a recent actual/simulated frequency response test (not just steady-state operation observation).
3. Check for hunting/oscillation signs (too-narrow deadband) or sluggish/absent response to real deviations (too-wide deadband or slow response speed).
4. If tuning appears incorrect, adjust and re-verify with another response test before considering it resolved.
5. Document test date, parameters checked, and results — schedule periodic re-verification per the plant's maintenance schedule, not just after a complaint or grid operator concern.

## Environmental flow compliance table

| Field | Value |
|---|---|
| Mandated minimum flow | 400 cfs |
| Current operating flow | 750 cfs |
| Margin above minimum | 350 cfs (87.5% above minimum) |
| Compliance status | Satisfied |

**Rule:** verify this table's compliance status BEFORE finalizing any generation schedule optimization — environmental flow is a hard constraint checked first, not balanced against generation output as a competing consideration.
