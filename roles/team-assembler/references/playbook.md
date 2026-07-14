# Playbook

## Cycle-time/takt reporting worksheet

Fill and report to team lead when cycle time consistently deviates from takt time.

| Field | Value |
|---|---|
| Station | Station 6, Wire Harness |
| Takt time | 45 sec |
| Standard cycle time | 40 sec |
| Observed actual cycle time | 52 sec |
| Deviation | +7 sec (+15.5% over takt) |
| Duration of deviation | ~1 hour |
| Suspected cause | New connector supplier, higher insertion force |
| Individually compensated? | Flag if yes — this is the failure mode to avoid |
| Reported to team lead? | Y — timestamp |
| Corrective action | Insertion-assist tool introduced |
| Post-fix cycle time | ~42 sec — confirm restored to within takt |

## Stop-the-line decision table

| Situation | Pull andon/stop? |
|---|---|
| Suspected defect on current or incoming unit | Yes — always, regardless of pace/break/shift-end proximity |
| Missing or defective required part | Yes — escalate, don't substitute or skip |
| Upstream station's output looks different from normal pattern, outside documented acceptable range | Yes — flag for check |
| Variation within a documented limit sample/boundary sample range | No — normal variation, no action needed |
| Personal difficulty keeping pace with takt time (no quality issue) | No stop needed — report the pace issue through normal channel, not andon |
| A standard work step skipped or modified to keep pace | Yes — this itself is a quality-risk event requiring report, even without a separate defect found |

## Standard-work deviation containment checklist

1. Identify the specific step deviated from and the exact time window it occurred.
2. Pull the production sequence log to identify which specific units were produced during that window.
3. Estimate or confirm what proportion of units in that window were actually affected (not all units in a window are necessarily affected — verify, don't assume 100%).
4. Route affected units for inspection or rework addressing the specific deviation (not a generic re-inspection).
5. Fix the root cause driving the deviation (tooling, training, process) separately from the containment action — both are required, neither substitutes for the other.
6. Document the full event: deviation, window, affected units, root cause, corrective action, and containment disposition.
