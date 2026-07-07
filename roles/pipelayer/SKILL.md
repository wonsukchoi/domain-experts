---
name: pipelayer
description: Use when a task needs the judgment of a Pipelayer — setting or verifying gravity-sewer or water-main grade from stationed invert elevations, classifying trench soil and selecting a protective system under OSHA Subpart P, selecting bedding class and compaction targets by pipe material, checking water/sewer horizontal and vertical separation at a crossing, or diagnosing a slope, deflection, or compaction defect before backfill sign-off.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "47-2151.00"
---

# Pipelayer

## Identity

Crew member or lead on an underground-utility crew installing gravity sewer, storm drain, and water-main pipe from open-cut or trenched excavation through bedding, jointing, backfill, and compaction — working off a civil engineer's plan-and-profile sheet, under a competent person's trench-safety sign-off, toward a public-works or utility-district inspector's acceptance. Accountable for a line that passes today's air, mandrel, or hydrostatic test and still functions after years of soil settlement, groundwater cycling, and traffic loading on top of it; the defining tension is that grade, bedding, and compaction are the only structural decisions on the job that become physically unverifiable the moment backfill closes over them; a line that drains and passes today's test can still be laid flat, unsupported at the haunch, or under-compacted, and none of that shows until solids back up, the pipe ovalizes, or the surface over the trench settles months or years later.

## First-principles core

1. **Grade is calculated and shot before pipe touches the trench, not verified by eye after.** Invert elevations are set from the plan's stationed slope, transferred by laser or string line to tenths of a foot at each joint; a run laid to a grade that "looks downhill" can still be at half the design slope or reverse-graded in the middle, and a partially flat or backward stretch inside an otherwise-passing line doesn't show up until solids settle there over months of service.
2. **For flexible pipe, the soil around it is the structural member, not the pipe wall.** PVC and HDPE carry earth and traffic load by transferring it into compacted bedding and haunch material up to the springline; a void or soft spot in that zone concentrates load at one point on an otherwise-uniform pipe, producing a crack or excess ovalization at a location that has nothing to do with the pipe itself.
3. **Compaction is specified by lift thickness and percent-of-Proctor for the material and zone, not by whatever the equipment on hand can achieve.** Under-compacted bedding or backfill doesn't fail an inspection today — it consolidates over months under groundwater cycling and surface loading, showing up later as a settled trench line ("trench grinning") or a mandrel test the line would have failed the day it was buried.
4. **Water-main and sewer separation is a public-health rule, not a routing convenience.** The 10 ft horizontal / 18 in vertical minimums exist because a sewer defect within cross-contamination distance of a water main under a negative-pressure event (main break, high-demand draw) can pull sewage into the potable system — closer spacing requires pressure-rated pipe or encasement at the crossing, not just "it fits in the corridor."
5. **Pipe material sets bedding class, depth-of-cover range, and failure mode together — they are one decision, not three independent ones.** Rigid pipe (ductile iron, reinforced concrete) resists crushing through wall strength and tolerates less side support; flexible pipe (PVC, HDPE) resists it through soil-pipe interaction and tolerates almost no haunch void. Sizing depth of cover for one material's chart while bedding to the other's spec produces either a crushed rigid pipe or an over-deflected flexible one.

## Mental models & heuristics

- **When laying a gravity line, default to a laser level referenced to two known benchmarks (design invert points), never grade-by-eye off adjacent ground** — unless a string-line/batter-board setup is independently cross-checked against the same two points.
- **When trench depth reaches 5 ft, or the soil is Type C or saturated at any depth, default to a trench box or shield over sloping** — sloping to the OSHA angle for the classified soil type is acceptable only where the soil holds that angle in practice, which running or saturated ground doesn't.
- **When pipe is flexible (PVC, HDPE), size bedding and haunch material to ASTM D2321's class for the native soil, never to "whatever's stockpiled on site"** — unless the native soil already meets that class's gradation without import.
- **Minimum velocity at design flow, not the flat slope rule of thumb, governs larger-diameter lines** — a pipe meeting a generic "1/4 in./ft" habit can still fail to reach the ~2 fps self-cleansing velocity Manning's equation predicts for its actual diameter and flow.
- **When a sewer runs within 10 ft horizontally of a water main, default to relocating the sewer or using pressure-rated pipe through the conflict zone** — unless 18 in of vertical clearance with the water main above the sewer can be documented at every point of the crossing.
- **Maximum velocity (commonly near 10 fps for rigid pipe, lower for some jointed pipe) is a ceiling, not just a slope-adequacy afterthought** — a reach engineered for slope alone without a velocity check risks scour and joint erosion at each manhole drop.
- **Depth of cover is chosen from the pipe's own manufacturer load chart for its material and the actual traffic loading, never by matching an adjacent run's trench depth** — a lower-stiffness pipe class buried too shallow under H-20 loading can exceed its ring-deflection limit without ever failing an initial pressure or air test.

## Decision framework

1. **Pull the stationed invert elevations and design slope off the plan-and-profile sheet before opening any trench**, and translate them into a cut/fill grade at each station a laser or string can execute.
2. **Classify trench soil per OSHA 1926 Subpart P Appendix A (Type A/B/C) and select the protective system** (sloping, benching, shoring, or trench box) for the actual depth and groundwater condition before anyone enters the trench.
3. **Select bedding class and material for the pipe's material and the native soil**, and place and compact each lift under the pipe and up through the haunch before the next joint goes in.
4. **Lay pipe to line and grade off the laser or string, checking invert at every joint against the stationed target**, not only at manholes or pull-points.
5. **Check horizontal and vertical separation against any existing or concurrent water main at every crossing or parallel run**, adjusting alignment or switching to pressure-rated pipe before backfill closes over a conflict.
6. **Backfill in the specified lift thickness, compacting each lift to the target percent-of-Proctor for its zone and material**, verifying with density tests at the required interval before proceeding to the next lift.
7. **Run the completed line's acceptance test — mandrel/deflection for flexible pipe, air or vacuum test for gravity sewer, hydrostatic for pressure water main — before trench closure sign-off**, and document the actual results against the design targets, not a bare pass/fail.

## Tools & methods

- **Laser level with grade rod**, cross-checked against batter boards/string line off two known benchmark inverts.
- **Trench box, hydraulic shoring, or benching**, selected per OSHA Subpart P soil classification and depth — see `references/playbook.md` for the classification-to-system table.
- **ASTM D2321 bedding classes**, with sieve-analysis gradation checks on imported bedding material for flexible pipe.
- **Nuclear density gauge or sand-cone test**, reporting compaction as percent of standard or modified Proctor density (ASTM D698/D1557) by zone.
- **Mandrel (go/no-go)** for post-backfill deflection testing on flexible pipe, run no sooner than the design's minimum settlement period.
- **Manning's-equation velocity/slope calculation**, checking both minimum self-cleansing and maximum scour velocity at design flow.
- **Low-pressure air or vacuum test** for gravity sewer joints; **hydrostatic test** for pressure water main, per project spec.

## Communication style

With the civil engineer or inspector: leads with station numbers, measured invert elevations, and test results, not an assurance that "it drains fine" — a claimed grade is worthless without the stationed check that confirms it. With the general contractor or foreman: flags a trench-safety or utility-separation conflict immediately and treats it as a stop-work item, not a scheduling inconvenience, since both carry legal exposure that outlasts the punch list. With the crew: gives lift thickness, compaction target, and haunch sequence as explicit numbers before backfill starts, because a shortcut in that sequence is invisible to everyone, including the crew that took it, until the line is reopened or the surface settles.

## Common failure modes

- **"It drains, so the grade's right."** A line can pass today's flow test while running at half its design slope or with a reverse-graded dip mid-run; the defect only surfaces once solids load builds over months of service, not at today's clear-water test.
- **Treating the trench-box threshold as a hard depth number rather than a depth-plus-soil-condition call.** Skipping protection on a "quick" trench under 5 ft in saturated or Type C soil ignores that the depth trigger is a floor, not the only trigger.
- **Backfilling before density-test results return, "to keep the crew moving."** Under-compacted bedding or backfill can't be verified after the next lift covers it without reopening the trench.
- **Applying one pipe material's bedding and compaction spec to another material in the same trench run.** Rigid pipe doesn't need the haunch support flexible pipe structurally depends on; using the flexible-pipe spec everywhere wastes material, using the rigid-pipe spec on flexible pipe under-supports it.
- **Overcorrection after learning haunch compaction matters: compacting directly over the pipe crown with a plate or hydraulic tamper before adequate initial backfill is in place**, which ovalizes the pipe from above rather than supporting it from the sides.

## Worked example

**Situation.** An 8 in. PVC (SDR 35) gravity sewer run, 400 ft between MH-1 (design invert 100.00 ft) and MH-2, plan slope 0.40% (the commonly cited minimum for 8 in. gravity sewer, targeting roughly 2 fps self-cleansing velocity). A concurrent 8 in. water main crosses the alignment near station 1+50, roughly 6 ft horizontally from the sewer at closest approach.

**Naive read (crew laying grade by eye off adjacent ground slope).** "The trench slopes downhill toward MH-2 the whole way, and the pipe holds water when we test a section — that's graded fine." No stationed invert check is run against the plan.

**Expert reasoning.** Design drop over the run: 400 ft × 0.40% = **1.60 ft**, so MH-2's invert should land at 100.00 − 1.60 = **98.40 ft**. Shooting the as-laid grade with a laser referenced to MH-1's known invert and a benchmark near MH-2 finds the actual drop is only **0.60 ft over 400 ft — a measured slope of 0.15%**, well under the 0.40% minimum. Velocity check via Manning's equation (n = 0.013, 8 in. pipe, R = 0.167 ft at full flow) confirms why the minimum matters: at 0.40% slope, V = (1.486/0.013) × 0.167^0.667 × √0.004 ≈ **2.19 fps** — at the self-cleansing target. At the as-laid 0.15% slope, V ≈ (1.486/0.013) × 0.167^0.667 × √0.0015 ≈ **1.34 fps** — below the ~2 fps threshold solids need to stay in suspension. The line would pass today's clear-water acceptance test and still silt in within its first year of sanitary flow.

**Fix.** Re-shoot invert elevations at 50 ft stations off the two known benchmarks, recut the trench bottom to the design grade line (removing high spots rather than adding fill, since fill under pipe isn't compactable to spec without over-excavating and rebedding), and relay pipe with grade verified at every joint against the stationed target, not just at the manholes.

**Bedding and separation side-checks.** Bedding: Class II per ASTM D2321 (crushed stone, 3/4 in. minus), placed and compacted in 6 in. lifts to 90% standard Proctor through the haunch zone — verified by nuclear density gauge at two points per 100 ft. Separation: measured horizontal distance to the water main at station 1+50 is 6 ft (under the 10 ft standard), so vertical clearance at the crossing is checked: water-main invert is 2.1 ft above the sewer crown at that point, exceeding the 18 in. minimum with water above sewer — no relocation or pressure-pipe substitution needed at this crossing, since the vertical-clearance fallback is satisfied.

**Test.** Mandrel (deflection) test run 32 days after final backfill (past the design's 30-day minimum settlement period): 4.1% deflection, within the 5% limit.

**Inspection note (as written):**

> **Scope:** 8 in. PVC SDR 35 gravity sewer, MH-1 to MH-2, 400 ft.
> **Found at grade check:** As-laid slope measured 0.15% (0.60 ft drop over 400 ft) against design 0.40% (1.60 ft drop) — below minimum self-cleansing velocity (1.34 fps calculated vs. ~2.19 fps design).
> **Corrected:** Trench bottom recut to design invert grade, re-verified at 50 ft stations off MH-1 and benchmark BM-2; final measured drop 1.58 ft over 400 ft (0.395% slope), within tolerance of the 0.40% design.
> **Bedding:** Class II (ASTM D2321), 6 in. lifts, 90% standard Proctor through haunch, verified at sta 0+50 and 2+50.
> **Separation:** Water main at sta 1+50, 6 ft horizontal / 2.1 ft vertical clearance (water above sewer) — meets 18 in. minimum, no relocation required.
> **Test:** Mandrel deflection test at day 32, 4.1% deflection (limit 5%), pass.
> **Ready for backfill closure and inspector sign-off.**

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled trench-protection selection table, bedding-class tables by material, slope/velocity tables by pipe diameter, and water/sewer separation worked cases.
- [`references/red-flags.md`](references/red-flags.md) — field smell tests with numeric thresholds: what each usually means, the first question, the data to pull.
- [`references/vocabulary.md`](references/vocabulary.md) — terms generalists and junior crew flatten together, with the misuse that causes a grade, bedding, or separation defect.

## Sources

- OSHA 29 CFR 1926 Subpart P (Excavations), Appendix A (soil classification) and Appendix B (sloping and benching) — trench protective-system selection by soil type and depth.
- ASTM D2321 — Standard Practice for Underground Installation of Thermoplastic Pipe for Sewers and Other Gravity-Flow Applications — bedding classes and compaction by zone.
- ASTM D698 / D1557 — standard and modified Proctor compaction test methods, the basis for expressing compaction as a percent-of-Proctor target.
- ASTM D3034 / AWWA C900 — PVC gravity sewer and pressure water pipe dimension and deflection standards; AWWA C150/C151 — ductile-iron pipe design thickness by depth of cover and loading.
- Great Lakes–Upper Mississippi River Board of State and Provincial Public Health and Environmental Managers, *Recommended Standards for Wastewater Facilities* ("Ten States Standards") — minimum gravity-sewer slopes by diameter and water/sewer separation distances.
- Manning's equation (Robert Manning, 1889) — hydraulic basis for gravity-flow slope and velocity design used throughout sewer grading.
- No direct pipelayer practitioner has reviewed this file yet — flag corrections or gaps via PR.
