# Playbook

## Peck-drilling decision worksheet

Fill for any drilling operation to determine cycle type.

| Field | Value |
|---|---|
| Drill diameter | 0.500" |
| Hole depth | 3.000" |
| Depth-to-diameter ratio | 6:1 |
| Threshold for peck drilling | 3-5x diameter |
| Decision | Peck drilling required (6:1 exceeds threshold) |
| Peck increment | 0.375" (0.75x diameter) |
| Number of pecks | 8 |
| Coolant delivery | Through-tool (verify reaches tip each peck) |
| Estimated cycle time (peck vs. continuous) | ~95 sec (peck) vs. ~40 sec (continuous, if it had succeeded) |

**Rule:** always calculate depth-to-diameter ratio explicitly rather than judging by absolute depth alone — the ratio, not the raw depth number, determines whether peck drilling is needed.

## Reach-to-parameter reduction table (illustrative — always use the specific tool manufacturer's guidance)

| Reach-to-diameter ratio | Feed rate adjustment | Speed adjustment | Depth of cut adjustment |
|---|---|---|---|
| Up to 3:1 (short reach) | Standard | Standard | Standard |
| 3:1-5:1 (moderate reach) | Reduce ~15-20% | Reduce ~10% | Reduce ~15% |
| 5:1-8:1 (long reach) | Reduce ~30-40% | Reduce ~20% | Reduce ~30% |
| Over 8:1 (very long reach) | Consult tooling specialist; consider anti-vibration bar tooling | Significant reduction likely needed | Significant reduction likely needed |

**Rule:** these percentages are illustrative starting points — always verify against the specific boring bar/tooling manufacturer's reach-specific guidance and confirm with a test cut before committing to a full production run.

## Hole-start technique checklist

1. Confirm the workpiece surface at the drill entry point is flat and perpendicular to the drill axis (or use a starting technique appropriate for an angled surface).
2. Use a center drill, spot drill, or pilot hole where appropriate to establish a straight, supported starting point before the main drill engages.
3. Begin the main drilling operation at a reduced feed rate for the first portion of engagement, increasing to standard rate only once the drill is fully and straightly engaged.
4. Monitor for any early signs of wander (uneven cutting sound, vibration) in the first moments of engagement — address immediately rather than continuing and hoping it self-corrects.
5. Once the hole start is confirmed straight and well-established, proceed with the full drilling cycle (continuous or peck, per the depth-to-diameter decision).
