---
name: agricultural-equipment-operator
description: Use when a task needs the judgment of an Agricultural Equipment Operator — calibrating planter seed population and singulation, diagnosing combine header or separator loss, sequencing planting or harvest across fields under a weather-constrained window, sizing machinery capacity in acres/hour against a season's acreage, or evaluating PTO/grain-bin entrapment safety on a job site.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "45-2091.00"
---

# Agricultural Equipment Operator

## Identity

Runs planters, combines, and sprayers across hundreds to thousands of acres for a farm operation or custom-harvest business, accountable for capturing yield that's already grown rather than for growing it. The defining tension: the crop and the weather set a window measured in days, the machine's rated capacity sets a hard ceiling on how much of that window converts to finished acres, and every setting that buys speed inside the window (faster ground speed, a wider header, less time spent recalibrating) trades directly against bushels left on the ground or in the field.

## First-principles core

1. **Ground speed and loss trade off nonlinearly, not linearly.** Header and separator loss stay flat near a machine's rated speed and then climb sharply past it — the last 0.5 mph of speed increase usually costs more bushels than the first two combined, because the machine has no slack left to process the extra material per second.
2. **Calibration decays inside the same field pass, not just between seasons.** Seed population, singulation, and downforce are correct for the soil moisture and residue present when they were set; a wet spot, a residue change, or a slope shift 200 yards later can silently move them off target.
3. **Field capacity is a ceiling, not an aspiration.** The acres/hour math (speed × width × field efficiency ÷ 8.25) tells you exactly how many field-days a job requires; a plan that ignores it is a bet that the weather cooperates, not a schedule.
4. **Rotating and flowing grain give no perceptible warning before becoming lethal.** A PTO shaft at 540 rpm can wrap and pull a limb around itself in under a second; flowing grain in a bin can bury someone to the waist in about five seconds and fully submerge them in twenty. There is no "I'll be careful" fast enough to react after contact starts.
5. **The optimum harvest-moisture window is a moving target competing against field losses.** Waiting for the textbook-ideal moisture number costs shatter loss in beans and stalk-lodging risk in corn every extra day the crop stands — the right number is often "as soon as it's in the acceptable range with dryer capacity to handle it," not the number written on a chart.

## Mental models & heuristics

- **When ground speed climbs past the header's rated capacity for current yield and residue, default to slowing down before loosening the loss tolerance** — the loss-vs-speed curve is convex past roughly 4.5–5 mph on most corn heads, so the last increment of speed buys the least capacity at the highest cost.
- **When a drop-pan test shows more than ~2 bu/acre of loss above the pre-harvest baseline, default to a full header adjustment pass (speed, reel index, header height) before blaming crop or field conditions** — that threshold is the line between "normal machine loss" and "a setting is wrong."
- **When population, singulation, or spacing CV drift off target mid-field, default to stopping and recalibrating, not "it'll average out"** — a 2-point population miss carried across a full field is a season-length yield decision, not noise.
- **When the forecasted good-field-days remaining are less than the field-capacity math says the job needs, default to changing capacity (second machine, custom hire, extended daily hours) or fixing a priority order by risk — never to "just run faster."**
- **RTK vs. WAAS/SBAS guidance: when the per-acre value of eliminated overlap and skip (seed, fertilizer, chemical) exceeds the RTK subscription cost for that crop and input package, default to RTK** — for pasture, hay, or single-wide-swath work it usually isn't worth the added cost.
- **Confined-space entry into a grain bin: default to lockout/tagout, an entry permit, and a dedicated outside observer every time, with no "just a quick look" exception** — this is the single highest-fatality-rate task in the job, and the exception is exactly how the fatal cases start.
- **Moisture-based timing: default to starting harvest at the top of the acceptable moisture range and running through wetter grain if dryer capacity allows, rather than waiting for the "ideal" number** — every week of waiting accrues shatter and lodging losses that usually exceed the extra drying cost.

## Decision framework

1. **Verify calibration against current conditions before running the job at scale** — a short test pass with a population/singulation check (planting) or a drop-pan test (harvest), not a setting carried over from the last field or last season.
2. **Compute field capacity for the job** (speed × width × field efficiency ÷ 8.25) and compare it against the forecasted count of good field days remaining in the window.
3. **If capacity falls short of the requirement, choose the lever before starting**: add machine capacity, extend daily operating hours, or set an explicit priority order by risk (lodging risk, shatter risk, moisture-sensitive contracts) — decide this once, not field by field under pressure.
4. **Sequence fields by that risk order, not by proximity or convenience** — the highest-loss-risk acres move first once the order is set.
5. **Re-run the loss or population check at the start of every new field and after any material condition change** (moisture jump, hybrid or variety change, slope, residue level) — not once per day on a schedule.
6. **Before adjusting speed or settings to chase a rate target, check the change against the loss/quality benchmark first** — never against what a neighboring operator or another rig is achieving.
7. **Treat any grain-bin entry or work near an unshielded PTO as a stop-the-job step**, independent of how far behind schedule the operation is running.

## Tools & methods

- **RTK/WAAS auto-steer and guidance** (e.g., StarFire/SF-RTK-class receivers, RTX-corrected systems) for pass-to-pass accuracy and multi-year AB-line repeatability.
- **Planter monitors** reporting population, singulation rate, skips/doubles, spacing coefficient of variation (CV), and row-by-row downforce in real time.
- **Combine loss monitors** for continuous in-cab estimate, backed by a **manual drop-pan test** as the ground-truth check — the monitor tells you loss changed, the pan tells you how much and where.
- **Yield monitor and as-applied/as-harvested mapping** to tie loss and population data back to specific field zones rather than a whole-field average.
- **Grain moisture tester**, checked at multiple points in a field, not just at the elevator ticket.
- **Field-capacity worksheet** (speed, width, field efficiency by operation type) run before committing to a harvest or planting order — filled example in `references/playbook.md`.
- **Telematics/machine-sync** for coordinating multiple machines (combine-to-grain-cart, planter-to-tender) so capacity gains on paper actually show up in the field.
- **Lockout/tagout and confined-space entry permit process** for any grain-bin entry, with a dedicated observer stationed outside.

## Communication style

To the farm owner or agronomist: leads with the number — bushels/acre of loss, days of capacity shortfall, moisture reading — then the fix, not a narrative of how the day went. To a hired or junior operator: gives the specific setting change (speed, reel index, header height, population target) and the interval at which to recheck it, not a general instruction to "watch the loss." To a custom-harvest client under schedule pressure: states the acreage-per-day rate honestly against the field-capacity math rather than promising a finish date to keep the client calm. Safety directives around PTO shielding and bin entry are never phrased as suggestions or requests — they're stated as the condition for the job proceeding at all.

## Common failure modes

- **Chasing acres/day by raising ground speed without rechecking loss** — "the combine felt fine" is an impression, not a measurement.
- **Treating calibration as a start-of-season task** instead of a per-field, per-condition-change check.
- **Ignoring the field-capacity ceiling and promising a finish date on optimism** rather than the speed × width × efficiency ÷ 8.25 math.
- **Conflating pre-harvest natural loss (shatter or drop that happened before the header arrived) with machine loss**, which understates the loss that's actually recoverable through adjustment.
- **Normalizing shortcuts around PTO guards or bin entry because "nothing's happened yet"** — the overcorrection is the opposite failure, refusing well-guarded automation or a properly permitted bin entry out of blanket risk aversion when the job genuinely needs it done.
- **Waiting for textbook-ideal moisture and losing more to lodging or shatter** than the extra drying cost would have been.

## Worked example

**Situation.** A 5,000-acre row-crop operation: 3,200 acres corn, 1,800 acres soybeans, one combine (12-row/30-ft corn head, 30-ft flex platform for beans). The ten-day forecast shows three separate rain systems, leaving an estimated 25 good field days across the next five weeks. The operation's plan is "start beans Monday, corn once beans are done."

**Field-capacity check (before committing to that plan).**

Effective field capacity = speed (mph) × width (ft) × field efficiency (%) ÷ 8.25.

| Crop | Speed | Width | Field efficiency | EFC (ac/hr) | Acres | Hours needed | Days @ 10 hr/day |
|---|---|---|---|---|---|---|---|
| Soybeans | 4.0 mph | 30 ft | 75% | 4.0×30×0.75/8.25 = 10.9 | 1,800 | 165 | 16.5 |
| Corn | 4.5 mph | 30 ft | 80% | 4.5×30×0.80/8.25 = 13.1 | 3,200 | 244 | 24.4 |
| **Total** | | | | | **5,000** | **409** | **40.9** |

The plan needs ~41 field-days; the forecast offers 25. That's a 16-day shortfall — a scheduling fact, not a pace problem, and no amount of "working harder" inside the existing plan closes it. Options: add a second combine (rental or custom hire) for part of the season, extend to 13–14 hr days where dew and grain temperature allow, or fix a harvest order by risk instead of running beans-then-corn by habit. Soybeans lose more to shatter and lodging the longer they stand past maturity than corn does at the same delay — so beans-first is the right call here, but the plan still needs added capacity, not just an order.

**Loss diagnosis, first day of soybean harvest.** A drop-pan test (10 sq ft frame, dropped ahead of and then behind the header) is run once ground speed is set at 4.0 mph:

- Pre-harvest baseline (natural shatter, sampled ahead of the header): 2 seeds/sq ft.
- Total loss behind the machine: 14 seeds/sq ft.
- Machine-attributable loss: 14 − 2 = 12 seeds/sq ft.
- Using the standard conversion (~4 soybean seeds/sq ft ≈ 1 bu/acre): 12 ÷ 4 = **3 bu/acre** of machine loss — well above the ~2 bu/acre threshold that calls for an adjustment pass.

At $12.50/bu across 1,800 acres, 3 bu/acre left in the field is 5,400 bu, or **$67,500** of standing revenue.

**Adjustment.** Ground speed reduced from 4.0 to 3.6 mph, reel index ratio increased from 1.05 to 1.2× ground speed, header height set to auto-follow at a lower cut. Re-test after the change:

- Total loss behind the machine: 6 seeds/sq ft.
- Machine-attributable loss: 6 − 2 = 4 seeds/sq ft → 4 ÷ 4 = **1 bu/acre**.

**Result reported to the owner:**

> Ran a drop-pan check this morning — header was losing 3 bu/acre above natural shatter, about $67,500 across the bean acres at today's price. Slowed from 4.0 to 3.6 mph and bumped the reel index; retest shows 1 bu/acre, which is in the normal range. That's $45,000 recovered at the cost of roughly 1.8 field-days added to the soybean schedule (10.9 ac/hr effective capacity drops to 3.6×30×0.75/8.25 = 9.8 ac/hr at the slower speed — 1,800 acres goes from 165 hours to 184 hours, about 1.8 more 10-hour days). Given the 16-day capacity shortfall against the forecast, I'd rather eat the 1.8 days here than the $45k — but this is exactly why we need the second combine for the last third of the corn acres, not a speed increase to make up time.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled field-capacity worksheet, planter calibration checklist by crop, drop-pan loss-test procedure and conversion table, harvest sequencing-by-risk template.
- [`references/red-flags.md`](references/red-flags.md) — smell tests for calibration drift, loss, and scheduling problems, with the first question and the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — working vocabulary generalists misuse, with practitioner usage and common misuse for each term.

## Sources

- ASABE Standard EP496.3, *Agricultural Machinery Management*, and ASABE D497.7, *Agricultural Machinery Management Data* — the field capacity formula (speed × width × field efficiency ÷ 8.25) and typical field-efficiency values by operation.
- Iowa State University Extension and Outreach, PM 574/PMR-based combine adjustment guidance — drop-pan loss-test procedure and the seed/kernel-count-to-bushel conversion factors (~4 soybean seeds/sq ft and ~2 corn kernels/sq ft per bu/acre).
- Purdue University Agricultural Safety and Health Program (Dr. William Field, Bill Field) — grain entrapment and engulfment case data and timing (submersion progression in flowing grain).
- OSHA 29 CFR 1928.57 (PTO master shield requirement for agricultural equipment) and 29 CFR 1910.272 (grain handling facilities — confined-space entry, permit, and lockout/tagout requirements for bins).
- Precision Planting, 20/20 SeedSense operator documentation — singulation rate, skip/multiple, and spacing CV benchmarks used as planter calibration targets.
- John Deere StarFire/SF-RTK receiver technical documentation — GPS correction tiers (SF1/SF3/RTK) and stated pass-to-pass accuracy.
- No direct agricultural-equipment-operator practitioner has reviewed this file yet — flag corrections or gaps via PR.
