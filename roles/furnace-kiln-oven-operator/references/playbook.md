# Playbook

## Temperature survey worksheet

Fill when a load configuration is new or has changed from a previously validated setup.

| Sensor position | Time to reach set-point | Notes |
|---|---|---|
| Control sensor (standard position) | t = 90 min | Standard control point |
| Pack center | t = 105 min | Slowest-heating point — 15 min lag vs. control |
| Pack edge (near door) | t = 85 min | Fastest-heating point |
| Pack corner | t = 95 min | Intermediate |

**Rule:** soak time is measured from the SLOWEST point in the load, not the control sensor. Cycle end time = slowest point's time-to-setpoint + specified soak duration.

| Field | Value |
|---|---|
| Specified soak time | 60 min |
| Slowest point reaches set-point at | t = 105 min |
| Cycle must continue until | t = 165 min |
| Naive (control-sensor-based) end time | t = 150 min — WOULD UNDER-SOAK by 15 min |

## Soak-time calculation table

| Scenario | Soak time basis |
|---|---|
| Load configuration previously validated, uniformity confirmed | Control sensor reaching set-point (validated to represent whole load) |
| New or changed load configuration, not yet surveyed | Run temperature survey first — do not assume control sensor represents the load |
| Survey shows meaningful lag (>5% of total cycle time, or per process-specific threshold) between control sensor and slowest point | Soak time measured from the slowest point's arrival at set-point |
| Survey shows all points reaching set-point within an acceptable narrow window | Control sensor basis acceptable; document survey confirming this for future reference |

## Atmosphere verification checklist

1. Confirm gas flow rate is set/scaled appropriately for the current chamber free volume and load configuration (denser loads may need adjusted flow).
2. Verify actual atmosphere composition via oxygen analyzer, dew point meter, or equivalent — not flow indication alone.
3. Confirm the atmosphere monitoring instrument's calibration is current before trusting its reading.
4. Verify composition meets spec BEFORE the critical soak period begins, and monitor throughout if the process requires continuous verification.
5. Document the actual composition readings (not just "atmosphere on") in the cycle log.

## Ramp rate and cycle documentation checklist

1. Confirm the material's specified maximum ramp rate before starting heat-up or cool-down.
2. Program or manually control the rate to stay within that limit throughout the ramp phase.
3. Log actual achieved ramp rate, not just the programmed target, in case of any deviation.
4. At cycle end, log full achieved profile: actual ramp rate, actual set-point achieved, actual soak time (and basis — control sensor vs. surveyed slowest point), and atmosphere composition data.
5. Attach the complete cycle log to the load's traveler/quality record before the load proceeds to the next step.
