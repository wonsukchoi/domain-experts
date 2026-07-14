# Electrician Helper — Playbook

Filled tables for a live rough-in or trim-out day. Numbers are worked examples against NEC 2023 (NFPA 70) tables — always re-derive from the actual box, conduit, and conductor count on the job, and confirm against the local adopted code cycle.

## 1. Box-fill calculation worksheet (NEC 314.16)

Conductor-volume allowance per conductor size (NEC Table 314.16(B)):

| Wire size | Free space per conductor |
|---|---|
| 14 AWG | 2.00 cu in |
| 12 AWG | 2.25 cu in |
| 10 AWG | 2.50 cu in |
| 8 AWG | 3.00 cu in |
| 6 AWG | 5.00 cu in |

Count units before multiplying:
- Each current-carrying and neutral conductor entering the box = 1 unit each (do not count conductors that pass through without splice, per 314.16(B)(1) — a straight-through conductor with no break or termination in the box).
- All equipment grounding conductors combined, regardless of count = 1 unit (at the largest ground conductor size present).
- All internal cable clamps combined (if present) = 1 unit (at the largest conductor size present).
- Each device strap/yoke (receptacle, switch) = 2 units (at the largest conductor size terminated on that device).
- Each isolated equipment-grounding conductor connected to a device that has its own separate ground termination = add 1 unit (rare case — most single devices only trigger the shared ground allowance above).

Worked example (box B, kitchen circuit): 3 cables × 2 conductors (hot+neutral) = 6 units, +1 grounds, +1 clamps, +2 device yoke = 10 units × 2.25 cu in (12 AWG) = **22.5 cu in required.**

## 2. Box capacity table (NEC Table 314.16(A), selected sizes)

| Box | Rated capacity |
|---|---|
| 4"×4"×1-1/2" square | 21.0 cu in |
| 4"×4"×2-1/8" square | 30.3 cu in |
| 4-11/16"×4-11/16"×1-1/2" square | 29.5 cu in |
| 4-11/16"×4-11/16"×2-1/8" square | 42.0 cu in |
| 3"×2"×2-1/2" device box | 10.0 cu in |
| 3"×2"×3-1/2" device box | 14.0 cu in |

Rule: if required volume > box capacity, upsize the box before mounting. There is no field fix once wire is dressed and terminated other than the same upsize with rework cost added.

## 3. Conduit fill table (NEC Chapter 9, Table 1 percentages + Table 4 EMT areas)

Maximum fill by conductor count:

| Conductors in raceway | Max fill % of conduit interior area |
|---|---|
| 1 | 53% |
| 2 | 31% |
| 3 or more | 40% |

Selected 40%-fill capacities for THHN conductors in EMT (from NEC Chapter 9 Table 4/Table 5, illustrative):

| EMT trade size | 12 AWG THHN, max qty at 40% | 10 AWG THHN, max qty at 40% |
|---|---|---|
| 1/2" | 12 | 9 |
| 3/4" | 22 | 16 |
| 1" | 35 | 26 |

Rule: count actual conductors against the table for the trade size on hand — don't estimate by eye. A pull that "looks like it'll fit" at 45–50% fill is outside the 40% cap and is a friction/tension problem waiting for the pull, not a code technicality.

## 4. Bend-degree tracking table (NEC 344.26, 360° cap between pull points)

| Run segment | Bend type | Degrees | Running total |
|---|---|---|---|
| Panel to first pull box | 90° sweep | 90° | 90° |
| First pull box to second | 90° + 45° offset | 135° | 225° |
| Second pull box to termination | 90° | 90° | 315° |

At 315° running total, one more 45° bend is the practical ceiling before a pull box is required — don't wait until the calculated 360° cap to add relief; friction becomes the limiting factor before the code maximum does on most real pulls.

## 5. Wire-pull lubrication guide

| Measured/estimated fill % | Lubricant guidance |
|---|---|
| Under 20% | Optional — light pull, unlikely to bind |
| 20–30% | Recommended, especially on runs with 2+ bends |
| Over 30% | Required — apply liberally along the pull, not just at the entry point |
| Any pull with visible resistance mid-pull | Stop, back off tension, add lubricant before continuing — do not increase pulling force to push through resistance |

## 6. GFCI/AFCI-required location quick reference (NEC 210.8, 210.12)

| Location | Protection required | Notes |
|---|---|---|
| Kitchen countertop receptacles | GFCI | All receptacles serving countertop surfaces, 210.8(A)(6) |
| Bathroom receptacles | GFCI | All receptacles, 210.8(A)(1) |
| Garage, outdoor, unfinished basement | GFCI | 210.8(A)(2), (3), (5) |
| Most 120V, 15/20A dwelling-unit branch circuits (bedrooms, living areas) | AFCI | 210.12(A) — check local amendments, coverage has expanded in recent code cycles |
| Kitchen small-appliance and laundry circuits | Often both GFCI and AFCI | Combination AFCI/GFCI breaker or device may be required — confirm against the adopted code cycle before staging |

Rule: confirm the staged device or breaker type against this table before the box is closed or the panel is dressed — a location miscategorized during staging is a callback, not a code judgment call for the helper to make solo.
