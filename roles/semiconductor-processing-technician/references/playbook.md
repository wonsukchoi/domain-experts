# Playbook

## SPC control-chart worksheet

Fill per lot/step; retain with the MES lot record.

| Field | Value |
|---|---|
| Process step | Etch Step 3, Chamber ETC-12 |
| Target / process mean | 500 nm |
| Sigma (process std dev) | 5 nm |
| 3-sigma control limits | 485-515 nm |
| Spec limits | 475-525 nm |
| Sampling plan | every 3rd wafer, 9 of 25 |
| Last 8 readings | 502, 504, 505, 507, 508, 509, 511, 512 |
| Mean of last 8 | 507.25 nm |
| Rule check: 8 consecutive same side of centerline? | Y — hold required |
| Rule check: any point beyond 3-sigma? | N |
| Rule check: 2 of 3 beyond 2-sigma? | N |
| Action | Hold at this step; investigate before advancing |

## Western Electric rule reference table

| Rule | Pattern | Typical implication |
|---|---|---|
| Rule 1 | 1 point beyond 3-sigma | Acute process upset — check for a sudden hardware/recipe event |
| Rule 2 | 2 of 3 consecutive points beyond 2-sigma, same side | Early-stage drift, may precede a Rule 1 or Rule 4 violation |
| Rule 3 | 4 of 5 consecutive points beyond 1-sigma, same side | Moderate sustained shift |
| Rule 4 | 8 consecutive points on same side of centerline | Systematic drift (seasoning, consumable wear, sensor drift) |

## Lot hold/release decision checklist

1. Identify which rule(s) triggered and pull the full trend chart, not just the flagged points.
2. Check whether every flagged point still sits inside spec limits — note this separately from control-limit status; both matter for the disposition record.
3. Pull the chamber/tool consumable-age and PM log; compare against its qualified window for the parameter in question.
4. Determine pattern type: does the trend match a previously characterized, documented behavior (e.g., known seasoning curve), or is it unexplained?
5. If explained and all points remain in spec: disposition = release, with a corrective action scheduled (PM, requalification) before the condition risks crossing control limits.
6. If unexplained, or any point is outside spec: disposition = hold pending engineering investigation; do not advance past any irreversible step until resolved.
7. Log the disposition, its rationale, and any follow-up action in the MES lot history with a timestamp before the lot proceeds.

## Recipe-change verification checklist

1. Identify the current qualified process window for every parameter, not just the one being changed.
2. Confirm the proposed new value(s) fall inside that window.
3. If any proposed value falls outside the qualified window, route to process engineering for requalification — do not run it on production material as a live fix.
4. If inside the window, check for known parameter interactions (e.g., etch time vs. selectivity, RF power vs. uniformity) that the qualification data already characterizes.
5. Document the change, its qualified basis, and the metrology result it was intended to correct in the recipe change log.
