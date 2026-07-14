# Playbook

## Column temperature-pressure diagnostic worksheet

Fill when a product quality issue appears with individually in-range readings.

| Field | Value |
|---|---|
| Unit | CDU Unit 3 |
| Product | Kerosene draw |
| Spec | Flash point ≥38°C |
| Lab result | 34°C — FAIL |
| Draw tray temp (current) | 185°C |
| Draw tray temp normal range | 180-200°C — within range |
| Column top temp (current) | 115°C |
| Column top temp normal range | 110-130°C — within range |
| Column pressure (current) | 1.6 bar(g) |
| Column pressure normal | 1.2 bar(g) |
| Column pressure limit | 2.0 bar(g) — no alarm triggered |
| Pressure deviation | +0.4 bar(g) from normal |
| Estimated cut-point shift (stated heuristic: ~8-10°C per 0.4 bar) | ~9°C lighter |
| Effective cut point at current conditions | ~176°C equivalent (vs. intended 185°C reference) |
| Root cause | Overhead condenser fouling raising system backpressure |
| Corrective action | Raise draw tray setpoint to ~194°C to restore equivalent cut point; flag condenser for cleaning |

## Tank gauging correction table (illustrative — always use current API MPMS tables)

| Step | Description |
|---|---|
| 1. Observed level | Read tank level via gauge tape or automatic tank gauge |
| 2. Strapping table conversion | Convert level to observed volume using tank's calibrated capacity table |
| 3. Temperature measurement | Measure product temperature at time of gauging |
| 4. API gravity measurement | Measure or obtain product's API gravity at observed temperature |
| 5. Volume correction factor (VCF) | Look up VCF from API MPMS Chapter 11 tables using temperature and API gravity |
| 6. Net standard volume | Observed volume × VCF = net volume at standard reference temperature (typically 60°F/15.6°C) |

**Rule:** never report the Step 2 (observed) volume as a final custody transfer figure — the Step 6 corrected volume is the commercial basis of the transaction.

## Startup/shutdown deviation checklist

1. Confirm the current step in the documented startup/shutdown sequence before taking any action.
2. Compare actual readings against this specific step's expected range, not a general steady-state range.
3. If any reading falls outside the expected range for this step, stop and check before proceeding to the next step — do not apply steady-state troubleshooting judgment to bypass the check.
4. Document the deviation, the check performed, and the resolution before resuming the sequence.
5. If the deviation cannot be resolved by the documented procedure, escalate to the shift supervisor/engineering rather than improvising a path forward.

## Relief valve lift investigation checklist

1. Confirm whether the lift was a planned/scheduled test or an unplanned event.
2. For an unplanned lift: pull DCS trend data for the period leading up to the lift — what control loop, setpoint, or equipment condition allowed pressure to reach the relief setpoint?
3. Identify whether the root cause is a control system issue, an operator action, or an equipment fault.
4. Document root cause and corrective action before considering the event closed — pressure returning to normal is not the same as the event being resolved.
5. If root cause isn't identified, escalate rather than resuming normal operation on the assumption it was a one-off event.
