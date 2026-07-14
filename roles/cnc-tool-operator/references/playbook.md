# Playbook

## Trend-monitoring worksheet

Fill during production run; update at each sampling interval.

| Part # | Measurement | Spec | Deviation from prior reading | Trend direction |
|---|---|---|---|---|
| 20 | 25.000mm | 25.00±0.02mm | — | baseline |
| 40 | 25.005mm | | +0.005mm | rising |
| 60 | 25.010mm | | +0.005mm | rising, confirmed |
| 80 | 25.015mm | | +0.005mm | rising, confirmed |
| **Extrapolated crossing point** | **~part 100** | (25.02mm limit) | rate: 0.00025mm/part | — |
| **Action** | Tighten sampling to every 5 parts starting part 85 | | | |
| 85, 90, 95 | record actual | | | |
| Offset correction applied at | part 95, -0.015mm | | | |
| Post-correction monitoring | continue tightened interval through part 120 to confirm flattening | | | |

## Tool wear vs. work-holding diagnostic table

| Symptom | Points to tool wear | Points to work-holding |
|---|---|---|
| Gradual, consistent drift in one direction across many parts | ✓ | |
| Sudden jump or inconsistency between consecutive parts with no gradual trend | | ✓ |
| Drift matches expected wear curve for this tool/material | ✓ | |
| Drift resumed/reset after a fixture cleaning or repair | | ✓ |
| Multiple features on the same part all drifting together (not just the one this tool cuts) | | ✓ (possible whole-part positioning issue) |
| Only the single feature this specific tool cuts is drifting | ✓ | |

## First-article inspection checklist

1. Confirm the setup is complete: correct program revision, correct tool list and offsets, fixture installed and clamped per spec.
2. Run one part through the full cycle.
3. Measure every dimension called out on the print/spec — not a subset, and not a visual check.
4. Record results against spec on the first-article inspection report.
5. If any dimension fails, do not proceed to production — diagnose and correct before running a second first-article attempt.
6. Only after a first-article part fully passes: release the setup for production quantity.
7. Repeat first-article inspection after any subsequent setup change (tool change, fixture change, program revision) during the same job, not just at the very start.

## Alarm response checklist

1. Note the alarm code/description before clearing it.
2. Physically inspect the tool for damage or breakage.
3. Physically inspect the in-process part for damage, incomplete features, or dimensional anomaly.
4. If tool or part condition is questionable, do not resume the cycle — address the tool/part issue first.
5. Only after confirming both tool and part are in acceptable condition, clear the alarm and resume.
6. Log the alarm, its cause (if determined), and the inspection results before continuing production.
