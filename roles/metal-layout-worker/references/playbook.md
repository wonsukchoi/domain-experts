# Playbook

## Datum-referenced vs. chained-measurement comparison worksheet

Use to illustrate why datum-referencing is required for multi-feature layouts.

| Feature | True position | Chained method result | Chained error | Datum-referenced result | Datum-referenced error |
|---|---|---|---|---|---|
| Hole 1 | 2.000" | 2.005" | +0.005" | 2.005" | +0.005" |
| Hole 2 | 4.000" | 4.008" | +0.008" | 4.005" | +0.005" |
| Hole 3 | 6.000" | 6.011" | +0.011" | 6.005" | +0.005" |
| Hole 4 | 8.000" | 8.014" | **+0.014" (exceeds ±0.010")** | 8.005" | +0.005" (within tolerance) |

**Key insight:** datum-referenced error stays constant (bounded by the tool's own systematic error); chained error compounds with each additional step. Always use datum-referenced measurement unless the print explicitly specifies a mate-relative dimension.

## Machining allowance reference table (illustrative — always use the job's specific process routing)

| Subsequent operation | Typical allowance to add beyond finished dimension |
|---|---|
| No further operation (final layout) | 0 — mark to finished dimension exactly |
| Standard grinding finish | 0.010"-0.030" typical, per shop standard/material |
| Rough machining before finish pass | 0.030"-0.125" typical, per process and material |
| Welding distortion allowance | Per shop's welding distortion standard — varies significantly by joint/material |

**Rule:** always confirm the actual required allowance against the part's specific process routing and shop standard — this table is illustrative, not a substitute for the job's actual specification.

## Surface preparation checklist

1. Clean the surface plate and workpiece of debris, oil, and residue before positioning the part.
2. Verify the surface plate itself is undamaged and within its calibration/verification schedule.
3. Apply layout dye evenly across the area to be scribed; recoat any thin or uneven sections before proceeding.
4. Allow dye to dry per manufacturer instructions before scribing, if required.
5. For tight-tolerance work, allow workpiece and tools to reach room/reference temperature (verify elapsed time since last thermal exposure) before final precision marking.
6. Zero and verify precision tools (height gauge, calipers) against a known standard before beginning layout.
