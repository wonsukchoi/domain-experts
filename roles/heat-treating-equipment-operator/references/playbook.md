# Playbook

## Case-depth diffusion calculation (filled example)

Furnace temperature 925°C, diffusion constant k=0.5 (verified: 0.5mm at 1 hour). Target case depth: 1.0mm.

| Step | Value |
|---|---|
| Verified relationship | depth = k × √(time), k = 0.5 |
| Check against prior batch | 0.5 × √1 = 0.5mm ✓ (matches observed result) |
| Target depth | 1.0mm |
| Solve for √(time) | 1.0 / 0.5 = 2.0 |
| Required time | 2.0² = 4.0 hours |
| Naive (linear doubling) time | 2.0 hours |
| Depth if naive 2-hour time used | 0.5 × √2 = 0.5 × 1.414 = 0.707mm |
| Shortfall vs. target | 1.0 − 0.707 = 0.293mm (29.3% short) |

**Comparison across target depths (same k=0.5):**

| Target depth | Required time (0.5 × √t = target) | Naive (linear) time from 1hr/0.5mm baseline |
|---|---|---|
| 0.5mm | (0.5/0.5)² = 1.0 hour | 1.0 hour (matches — this is the baseline) |
| 1.0mm | (1.0/0.5)² = 4.0 hours | 2.0 hours (50% short of required time) |
| 1.5mm | (1.5/0.5)² = 9.0 hours | 3.0 hours (67% short of required time) |
| 2.0mm | (2.0/0.5)² = 16.0 hours | 4.0 hours (75% short of required time) |

**Rule applied:** Because the relationship is square-root rather than linear, the gap between naive linear scaling and the actual required time grows dramatically larger as the target depth increases relative to the baseline — a shallow-depth error is forgivable, a deep-target error is not.

## Quench-delay tracking worksheet (filled example)

Alloy's maximum allowable quench delay: 15 seconds (per its documented hardenability requirement).

| Part | Furnace removal time | Quench immersion time | Actual delay | Within 15-sec limit? |
|---|---|---|---|---|
| Part A | 10:00:00 | 10:00:08 | 8 sec | Yes |
| Part B | 10:05:00 | 10:05:22 | 22 sec | **No — 7 sec over limit** |
| Part C | 10:10:00 | 10:10:11 | 11 sec | Yes |

**Result:** Part B's 22-second delay exceeds the alloy's 15-second maximum — flag for hardness re-verification, since the extended delay risks partial transformation before quenching began, potentially producing an inconsistent microstructure despite otherwise correct nominal process parameters.
