# Dragline and Excavating/Loading Machine Operator — Playbook

Filled reference sequences: bank-yardage production calculation, swing-angle cycle-time correction, bucket-to-truck pass-count matching, and ground bearing/berm verification.

## 1. Bank-yardage production calculation

Bucket capacity is rated heaped/loose; pit plans and reserve figures are in bank cubic yards (bcy). Convert every cycle before comparing to plan.

| Input | Typical range | Source/note |
|---|---|---|
| Bucket fill factor, virgin bank | 0.85–0.95 | material breaks cleanly, fills bucket near-completely |
| Bucket fill factor, rehandled/blocky cast spoil | 0.65–0.75 | already-broken, loosely piled material fills less completely per pass |
| Swell (load) factor, common earth | ~1.25 (load factor ~0.80) | Caterpillar Performance Handbook, confirm vs. site geotechnical data |
| Swell (load) factor, blasted rock | ~1.50 (load factor ~0.67) | Caterpillar Performance Handbook |
| Swell (load) factor, clay | ~1.35 (load factor ~0.74) | Caterpillar Performance Handbook |

**Working steps:**

1. Take the bucket's rated heaped capacity in cubic yards.
2. Multiply by the fill factor appropriate to the current face material (virgin bank vs. rehandle/blocky) to get loose cubic yards actually captured per cycle.
3. Divide by the site's swell factor for that material to convert loose cy to bank cy per cycle.
4. Multiply bank cy per cycle by cycles per hour (see Section 2 for the swing-angle-corrected cycle time) to get bank cy/hr.
5. Multiply by effective operating hours for the shift (rated shift length × operating efficiency, commonly 80–90% after delays, moves, and breaks) to get bank cy for the shift.
6. Compare against the pit plan's target bcy for the current face and swing configuration — a gap traces to fill factor, swell factor, swing angle, or effective-hours loss; isolate which one before reporting.

**Worked figures (illustrative — see SKILL.md worked example for the full derivation):**

- 60 cy bucket × 0.85 fill factor = 51 loose cy/cycle.
- 51 ÷ 1.25 swell factor = 40.8 bcy/cycle.
- 40.8 bcy × 49.7 cycles/hr (120° swing, see Section 2) = 2,028 bcy/hr.
- 2,028 × 6.8 effective hours = 13,790 bcy for the shift.

## 2. Swing-angle cycle-time correction

Cycle time (dig + swing-loaded + dump + swing-empty) is minimized near a 90° swing arc between dig face and dump point; time lengthens as the actual angle departs from that optimum.

| Swing angle | Cycle-time correction vs. 90° baseline | Resulting cycle time (50 sec baseline) |
|---|---|---|
| 90° (optimum) | 0% | 50.0 sec |
| 100° | +15% | 57.5 sec |
| 110° | +30% | 65.0 sec |
| 120° | +45% | 72.5 sec |
| 130° | +60% | 80.0 sec |

Correction factor used: approximately +1.5% cycle time per degree of swing beyond 90°, a stated heuristic reflecting that swing time dominates total cycle time and scales roughly with angle past the optimum arc — confirm against the specific machine's OEM cycle-time table rather than applying this table blind, since boom length, hoist speed, and material also shift the baseline.

**Working steps:**

1. Confirm the actual swing angle for the current face-to-dump geometry (not the plan's assumed angle) by pit survey or engineering confirmation.
2. Establish the machine's baseline cycle time at 90° swing from its OEM spec or the site's historical cycle-time log for that machine.
3. Apply the correction table (or the site's own swing-time table if one exists) to get the actual expected cycle time.
4. Convert to cycles/hour (3,600 ÷ cycle time in seconds) for the production calculation in Section 1.
5. If the corrected cycle time implies a production shortfall against plan of more than roughly 10–15%, flag the swing-angle/spoil-placement configuration to pit engineering rather than absorbing it as a performance variance.

## 3. Bucket-to-truck pass-count matching

| Truck rated payload | Bucket size | Target pass count | Notes |
|---|---|---|---|
| 240 ton (218 t) | 25 cy (heaped) | 4 passes | ~60 t/pass at typical fill/density |
| 240 ton (218 t) | 35 cy (heaped) | 3 passes | tighter tolerance, watch for overload on pass 3 |
| 320 ton (290 t) | 35 cy (heaped) | 4 passes | |
| 320 ton (290 t) | 25 cy (heaped) | 5–6 passes | outside target range — flag as undersized bucket for this fleet |

**Working steps:**

1. Estimate loose cubic yards delivered per pass: bucket rated capacity × fill factor for current material.
2. Convert to tons using the material's loose density (site-specific; overburden and coal densities differ materially — confirm before estimating payload).
3. Divide the truck's rated payload by tons-per-pass to get target pass count.
4. If target pass count falls outside roughly 3–5, treat it as a bucket/truck fleet-sizing mismatch, not a per-load adjustment — flag to the pit engineer with the specific truck/bucket combination and the calculated pass count.
5. On the loading floor, count actual passes against the target each load; a load finishing under target pass count with a full-looking body risks overload — verify against payload monitor data before releasing the truck, don't estimate by eye alone.

## 4. Ground bearing and berm verification

**Ground bearing (tub/crawler repositioning):**

1. Before walking a dragline or tracking a shovel/excavator onto any surface not previously confirmed for this specific position — fill, recently placed spoil, ground with visible moisture — request a bearing-capacity confirmation from pit engineering rather than assuming compacted appearance equals confirmed bearing.
2. Compare the machine's specified ground bearing pressure (tub/pontoon or track, from OEM spec, commonly in the range of tens of psi for large walking draglines depending on machine weight and shoe/pontoon area) against the confirmed bearing capacity of the surface — the move proceeds only if capacity exceeds the machine's pressure with an engineered margin, not a bare majority.
3. If bearing capacity is unconfirmed and cannot be confirmed before the move is needed, treat the position as not cleared — hold the move, don't proceed on the assumption that the ground "looks the same as" a previously cleared position nearby.
4. Log any settlement, list, or unusual resistance during a walk or track move immediately and stop further movement until pit engineering has assessed it.

**Berm height at dump points (per 30 CFR §77.1605(k) and the parallel Part 56 provision):**

1. Measure the berm or bank at the dump point against the mid-axle height of the largest self-propelled unit that dumps there — not the average truck in the fleet, the largest.
2. If measured height is below that threshold, treat the dump point as closed until the berm is rebuilt — do not substitute operator caution (slower approach, spotter) for the physical berm requirement.
3. Re-verify berm height after any equipment traffic, weather event, or extended idle period at the dump point — berms degrade with use and aren't a one-time-built, permanently compliant feature.
4. Log the measured height (not a qualitative "looks okay") at each shift's first use of the dump point.
