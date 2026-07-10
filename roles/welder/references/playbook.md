# Playbook

## Heat input calculation (filled example)

Joint J-14, GMAW butt weld, 1" A36 plate, WPS-117 qualified range 20–35 kJ/in.

Formula: HI (kJ/in) = (Voltage × Amperage × 60) ÷ (Travel speed in ipm × 1,000)

| Scenario | Voltage | Amperage | Travel speed | Calculation | Heat input | In range? |
|---|---|---|---|---|---|---|
| As-planned | 25V | 220A | 12 ipm | (25×220×60)÷(12×1,000) | 27.5 kJ/in | Yes |
| As-run (sped up) | 25V | 220A | 18 ipm | (25×220×60)÷(18×1,000) | 18.3 kJ/in | **No — below 20 kJ/in minimum** |

Increasing travel speed alone, with no compensating amperage change, dropped heat input 33% below the qualified minimum — despite identical voltage and amperage settings.

## Carbon-equivalent preheat determination (filled example)

Formula: CE = C + Mn/6 + (Cr+Mo+V)/5 + (Ni+Cu)/15

Material cert for this heat of A36 plate: C = 0.20%, Mn = 1.00%, no significant Cr/Mo/V/Ni/Cu.

| Term | Value |
|---|---|
| C | 0.20 |
| Mn/6 | 1.00/6 = 0.1667 |
| Other terms | 0 (negligible alloy content) |
| CE | 0.20 + 0.1667 = 0.3667 ≈ 0.37 |

WPS-117 requires preheat for this thickness (1") when CE exceeds 0.40. At CE 0.37, this heat is under the threshold — no mandatory preheat for this specific material lot, though the WPS's stated minimum interpass still applies once multi-pass welding starts.

## Weld sequence / distortion control (filled example)

24-inch structural seam, single-sided groove weld, 3 passes required.

| Approach | Sequence | Expected result |
|---|---|---|
| Naive | Weld continuously from one end to the other, all 3 passes in the same direction each time | Heat concentrates progressively toward the finish end; seam bows toward the weld side by an amount proportional to accumulated heat imbalance |
| Planned | Backstep sequence: divide the 24" seam into 4 segments of 6"; weld segments in order 2 → 4 → 1 → 3, each segment welded in the reverse direction of travel | Heat input distributes across the length instead of concentrating at one end; measured distortion after welding stays within the project's flatness tolerance |

Rule applied: any seam over roughly 12 inches on a rigid section gets a segmented backstep or skip sequence planned before the first arc strike, not decided reactively after the first pass shows bowing.
