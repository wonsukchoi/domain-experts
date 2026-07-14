# Playbook

Filled templates and worked procedures — run these directly, don't treat them as descriptions of what to do.

## 1. Test-strip procedure and density table

Run at the start of a job (and again if mix, lift, or ambient temperature changes materially).

**Setup:** pave a representative 500–1,000 ft test section at the planned lift thickness and mix. Take density readings after each incremental pass count, at consistent offset from the joint/edge.

**Worked example — 1.5-in. lift, 9.5mm NMAS surface mix, 40°F ambient:**

| Pass count | Roller type / mode | Density (%Gmm) | Gain from prior step |
|---|---|---|---|
| Behind paver (0 passes) | — | 86.5% | — |
| 2 | Breakdown, vibratory | 92.1% | +5.6 |
| 4 | Breakdown, vibratory | 94.8% | +2.7 |
| 6 (4 breakdown + 2 intermediate) | + pneumatic | 95.6% | +0.8 |
| 8 (4+2+2 finish) | + static steel | 95.9% | +0.3 |
| 10 (4+2+4 finish) | + static steel | 95.95% | +0.05 |

Lock the pattern at the step where the marginal gain drops below roughly 0.5 percentage points per two-pass increment — here, 4 breakdown + 2 intermediate + 2 finish (8 total). Running to 10 passes buys almost nothing and adds roller time and finish-mark risk. Record the locked pattern (roller order, mode, speed, pass count) and the ambient/mix conditions it was validated under.

## 2. Rolling-pattern template by lift/mix

| Lift thickness | NMAS | Breakdown | Intermediate | Finish | Notes |
|---|---|---|---|---|---|
| 1.5 in. | 9.5 mm | 3–4 passes, vibratory steel | 2 passes, pneumatic | 2 passes, static steel | Thin lift — watch cooldown rate, keep breakdown roller within ~8 min of paver |
| 2.0 in. | 12.5 mm | 3–4 passes, vibratory steel | 2 passes, pneumatic | 2 passes, static steel | Standard surface course window |
| 3.0+ in. | 19–25 mm | 2–3 passes, vibratory steel (higher amplitude) | 2 passes, pneumatic | 1–2 passes, static steel | Base/binder course — more compaction window available; watch for over-rolling causing checking |

Rule of thumb for minimum compacted lift: **lift ≥ 3× NMAS (4× preferred)**. A 9.5 mm (0.375 in.) NMAS mix has a minimum workable lift around 1.1–1.5 in.; running it thinner risks aggregate crushing and rapid cooldown that never reaches the breakdown window's low end.

## 3. Longitudinal joint procedure

**Hot-side rolling (standard, non-echelon paving):**

1. Pave the first lane with an unsupported edge — roller overhangs about 6 in. past the edge on the first pass to compact it without pushing material off the edge entirely.
2. Pave the second lane, overlapping the first lane's mat by roughly 1 in. (25 mm) onto the compacted first-lane surface.
3. Roll the joint from the **hot side** (the just-placed second lane) in vibratory mode, with the roller drum overlapping about 6 in. onto the first (already-compacted, cooler) lane.
4. Target: joint density within 6 in. of the joint no more than ~2 percentage points below mainline mat density for the same lift. A reading below that triggers a pattern review (roller offset, timing, overlap width) before the next joint is built the same way.

**Echelon paving (two pavers running staggered, same shift):**

1. Stage pavers so the joint is placed and rolled while both lanes are still in the breakdown window — this beats hot-side rolling because both sides of the joint are compacted from full working temperature, not one hot and one already-set.
2. Roller crosses directly over the joint once both lanes have reached it, rather than working each lane's edge separately.

## 4. Trench-backfill and subgrade lift/compaction checklist

| Material | Compactor | Max lift (loose) | Target compaction |
|---|---|---|---|
| Granular bedding/backfill | Walk-behind reversible plate | 8–10 in. loose (≈6–8 in. compacted) | 95% Standard Proctor (ASTM D698) |
| Cohesive (clay) backfill | Rammer/tamper (not plate — plate skates on cohesive soil) | 6–8 in. loose | 90–95% Standard Proctor, check spec — cohesive soils are harder to over-compact-check |
| Subgrade under pavement structure | Vibratory roller (walk-behind or ride-on, sized to width) | 8–12 in. loose depending on roller class | 95–100% Modified Proctor (ASTM D1557) per pavement design spec |

**Procedure per lift:**

1. Place material at or below the compactor's rated effective lift depth — do not stack two lifts' worth of loose material to save a pass; the compactor's energy doesn't reach the bottom of an oversized lift, and the failure (settlement) shows up months later, untraceable to the shortcut.
2. Compact with overlapping passes (commonly 4–6 in. overlap between passes) until the target relative compaction is met — verify with a nuclear or sand-cone density test at a frequency set by the spec (commonly one test per lift per defined area, e.g., every 150–300 linear ft of trench).
3. Log the lift number, material, compactor, and test result before placing the next lift — a failed lower-lift test found after three more lifts are placed means removing all of them, not just the one that failed.

## 5. Thermal-segregation response

1. Scan mat temperature continuously behind the screed (thermal camera/profiler) or spot-check with an IR gun at regular intervals (e.g., every truckload or every 100 ft).
2. If the differential across the mat width exceeds roughly 25°F, do not respond by changing the roller pattern on the cold streak — that adds compactive effort where the mix is already stiffening, without closing the temperature gap.
3. Trace the cause: check truck-by-truck delivery temperatures at the hopper. A single truck running 20–30°F cooler than the rest of the string (long haul, uncovered load, delayed dispatch) is the most common cause.
4. Fix at the source — reject or reroute a persistently cold truck, add a material transfer vehicle to remix loads before the hopper, or tighten haul scheduling — and flag the already-placed cold-streak section for a targeted density check rather than assuming the roller pattern covered it.
