# Playbook

## Yield-variance diagnostic worksheet

Fill when a batch's yield falls outside its spec's stated tolerance.

| Field | Value |
|---|---|
| Batch # | 8842 |
| Product | Chicken breast portions |
| Incoming raw weight | 500 lb |
| Trimmed output weight | 385 lb |
| Actual yield | 385/500 = 77% |
| Spec target / floor | 82% target, 80% floor (±2%) |
| Deviation from floor | 3 points under |
| Blade sharpening log check | Last sharpened: hrs ago vs. 4-hr schedule |
| Receiving QC — incoming lot fat/bone % | vs. typical for this supplier |
| Root cause identified? | Y/N — list contributing factors |
| Corrective action | e.g., resharpen blade, flag supplier lot to QA |
| Production hold required? | Y/N — hold only if root cause is uncontrolled/unexplained |

## CCP corrective-action decision table

| CCP type | Critical limit example | Standard corrective action |
|---|---|---|
| Chilling / cold-chain temperature | ≤40°F product surface temp | Hold product, verify chiller function, check cumulative time-temperature exposure across all stations against plan's allowance |
| Cooking (if applicable to product line) | Minimum internal temp/time per product | Hold product, verify cook equipment calibration, re-cook or reject per plan |
| Metal detection | Detector sensitivity setting per product | Stop line, isolate rejected product, investigate root cause (equipment wear, incoming material) before resuming |
| Allergen control point | Zero cross-contact tolerance | Immediate stop, full cleaning/verification per protocol, documented release before resuming that product |

**General rule:** every corrective action gets logged with timestamp, the specific out-of-range value, the action taken, and who authorized product release — never just a note that the issue was "resolved."

## Cumulative time-temperature exposure tracking example

| Station | Time entered | Time exited | Temp reading | Time above 40°F (this station) |
|---|---|---|---|---|
| Receiving/cooler | 06:00 | 06:15 | 36°F | 0 min |
| Cutting line | 06:15 | 06:35 | 39°F | 0 min |
| Trim/portioning | 06:35 | 07:05 | 41°F | ~12 min (portion of dwell above limit) |
| Post-trim scale | 07:05 | 07:10 | 41°F | (included above) |
| **Cumulative total above 40°F** | | | | **12 min** (allowance: 30 min) |

If cumulative total exceeds the plan's stated allowance, the product requires disposition per the HACCP plan (hold/reject), regardless of how the total accumulated across stations.

## Foreign-material reject investigation checklist

1. Isolate the rejected piece and the batch segment immediately surrounding it — do not discard before investigation.
2. Check upstream equipment (blades, conveyor components, fasteners) for wear, damage, or missing parts that match the detected material type.
3. Check incoming raw material records for any known foreign-material risk (e.g., a supplier notice, prior lot issues).
4. Confirm detector/X-ray sensitivity settings are at their specified calibration — not drifted or manually adjusted.
5. Document root cause before resuming the line; if root cause can't be confirmed, escalate to maintenance/QA before restarting rather than resuming on an unconfirmed assumption.
