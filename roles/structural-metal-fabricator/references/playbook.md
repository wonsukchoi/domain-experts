# Playbook

## Cumulative tolerance-stack calculation (filled example)

40-foot truss, 5 segments at 8 feet each, per-segment square tolerance ±1/16", overall assembly tolerance ±1/4" (0.25").

| Step | Value |
|---|---|
| Per-segment tolerance | ±1/16" (0.0625") |
| Number of segments | 5 |
| Worst-case cumulative deviation (same-direction error) | 5 × 0.0625" = 0.3125" |
| Overall assembly tolerance | ±0.25" |
| Overrun | 0.3125 − 0.25 = 0.0625" |
| Overrun as % of assembly tolerance | 0.0625 / 0.25 = 25% |

**Result:** Even with every segment individually passing its own ±1/16" check, the worst-case cumulative stack exceeds the project's overall ±1/4" tolerance by 25%. A cumulative check across the full 40-foot assembly — not just segment-by-segment — is required before proceeding to final weld.

## Racking (diagonal) check worksheet (filled example)

Rectangular steel frame, 20' × 10', squareness tolerance ±1/4" between the two diagonals.

| Measurement | Value |
|---|---|
| Theoretical diagonal (√(20² + 10²)) | √500 = 22.36 ft |
| Measured diagonal A (corner 1 to corner 3) | 22.38 ft |
| Measured diagonal B (corner 2 to corner 4) | 22.31 ft |
| Difference between diagonals | 22.38 − 22.31 = 0.07 ft = 0.84" |
| Squareness tolerance | ±0.25" |

**Result:** The two diagonals differ by 0.84", far exceeding the ±0.25" squareness tolerance — the frame is measurably out of square (racked) even if every individual member's cut length matches the drawing exactly. Correct before tacking; do not rely on member-length checks alone to confirm squareness.

## Fit-up sign-off record (filled example)

| Joint | WPS reference | Required root gap | Measured root gap | Alignment/mismatch | Status |
|---|---|---|---|---|---|
| J-1 | WPS-204 | 1/8" ± 1/32" | 1/8" | 0" mismatch | Approved for weld |
| J-2 | WPS-204 | 1/8" ± 1/32" | 3/16" | 0" mismatch | **Rejected — 1/16" over tolerance, re-cut or shim before proceeding** |
| J-3 | WPS-207 | 3/16" ± 1/32" | 3/16" | 1/16" mismatch (within allowed 1/8" max for this joint) | Approved for weld |

Each joint's sign-off states the specific measured values against the specific WPS's tolerance — not a general "fit-up looks good."
