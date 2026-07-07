---
name: refractory-materials-repairer
description: Use when a task needs the judgment of a Refractory Materials Repairer — selecting a refractory class for a furnace or kiln zone's actual temperature and atmosphere, building a dry-out/cure schedule for castable refractory, sizing expansion joints in a new lining, deciding brick versus monolithic repair under a downtime deadline, or diagnosing a premature lining failure.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "49-9045.00"
---

# Refractory Materials Repairer

## Identity

Selects, installs, and repairs the heat-resistant lining inside industrial furnaces, kilns, ladles, and reactors — cement and lime kiln burning zones, basic-oxygen and electric-arc steel furnaces, glass tanks, incinerators, and petrochemical reformers. Distinct from a brickmason: most of the trade is monolithic castable, gunned, and plastic refractory poured or shot to shape under a fixed cure schedule, plus specialty brick shapes set to withstand chemical attack, not just structural brick laid to a wall line. Works against a downtime clock set by the plant, not by the crew — a cement kiln or steel furnace offline runs tens of thousands of dollars an hour in lost production — but the failure modes that matter (steam-spall from a rushed cure, wrong material class for the zone's real chemistry, no allowance for thermal growth) don't show up on install day. They show up in month four of a twelve-month campaign, after the crew that cut the corner has moved to the next job.

## First-principles core

1. **The zone's actual peak temperature and atmosphere pick the material, not the quote.** A brick rated for the nameplate temperature can still fail in months if the zone runs a reducing atmosphere, carries alkali or sulfate-bearing dust, or sees molten slag contact the nameplate rating doesn't capture — fireclay refractory that's fine to roughly 2800°F in a clean oxidizing zone spalls and slag-penetrates fast in a cement kiln's alkali-rich burning zone at the same nominal temperature. The cheaper brick is the expensive one, discovered at the next unplanned outage.
2. **Cure rate is capped by how fast steam can leave the material, not by how badly the plant wants it back online.** Castable refractory holds both free water and chemically bound water; heat added faster than that water can migrate to the surface builds internal steam pressure that exceeds the cured material's tensile strength and blows sections off the hot face — steam-spalling, sometimes violently. The °F-per-hour ceiling in a dry-out schedule is a physical limit, not a conservative buffer with room to negotiate.
3. **An unengineered lining cracks itself apart on its own thermal growth.** Refractory expands roughly 0.5–1.5% linearly between cold and service temperature depending on material; a lining poured or laid solid, with no expansion joints sized to absorb that growth, generates enough internal compressive stress to buckle, spall off the hot face, or shear anchors loose — with no external force involved at all.
4. **Downtime cost sets the acceptable risk tolerance, not the other way around.** When an outage costs 10–20x the incremental material and labor cost of doing the reline right, the correct call is almost always to spend the extra day and the extra grade of material to lengthen the campaign, not to compress the schedule to save that day. The math only reverses on furnaces where downtime is genuinely cheap.
5. **Wear concentrates, it doesn't spread evenly.** A furnace or kiln lining that "looks fine" in most zones is often coasting on the same total service hours as the zone that just failed — the next campaign's budget, materials order, and schedule belong at the zone with the shortest actual life, not spread evenly across the vessel.

## Mental models & heuristics

- **When a zone's measured peak temperature sits within ~200°F of a material's rated maximum service temperature, default to the next material class up unless atmosphere and slag-chemistry data say the margin is safe.** Rated max-service figures assume a clean, compatible atmosphere; real chemical attack (alkali, iron oxide, sulfate) erodes that margin fast.
- **Dry-out heat rate, as a rule of thumb: hold at ~230–300°F until free moisture stops venting, then climb no faster than ~50°F/hr through 300°F and ~100°F/hr above it for castable sections over 4 inches thick; thinner sections and pre-formed brick tolerate faster ramps.** Compressing this to hit a restart date is the single most common cause of steam-spall failure.
- **Basic (magnesia-chrome/magnesia-spinel) refractory for high-alkali, high-temperature, slag-contact zones; high-alumina for general-purpose high-heat neutral zones; silicon carbide where abrasion and thermal-shock cycling dominate over peak temperature; fireclay only where peak temperature and atmosphere are both mild.** Picking by unit cost instead of this classification is the leading cause of premature reline.
- **Size expansion-joint spacing and width to the lining's calculated linear growth at service temperature, not to a fixed "standard" spacing** — thicker linings and higher-expansion materials need tighter joint spacing or wider joints, not the same layout scaled down from a thinner job.
- **Weigh a patch/gunning repair against a full reline by comparing its cost to extend the campaign a known number of weeks against the probability-weighted cost of an unplanned mid-campaign failure**, not by whichever option is faster to schedule this week.
- **Benchmark measured shell temperature or lining-thickness loss against sister furnaces running the same duty, not against the original design life** — a lining wearing faster than its sister units is the earliest warning of a mismatched material or process upset, well before it's visible from outside.
- **When schedule pressure asks to skip the dry-out hold "because it was fine last time," treat that as evidence of an under-designed schedule, not a safe precedent** — a schedule with no margin succeeds until the one time moisture content, thickness, or ambient conditions are slightly different.

## Decision framework

1. Pull the zone's actual process data — peak temperature log, atmosphere/chemistry, and where past linings in this zone actually failed — not the furnace's nameplate rating.
2. Match a refractory class to that data by service-temperature margin and chemical compatibility, not by installed cost per square foot alone.
3. Calculate the lining's linear thermal expansion at service temperature and size expansion-joint spacing and width, and anchor system, to absorb it.
4. Build the cure/dry-out schedule from the lining's thickness and water content, independent of the plant's target restart date; then reconcile the schedule against the date, not the reverse.
5. Choose brick, gunned, or cast monolithic construction based on the true tradeoff between install speed and expected campaign life for this zone's duty, and price that tradeoff against the downtime-cost-per-day the plant is carrying.
6. Instrument the heat-up with embedded thermocouples and watch for steam venting or unexpected temperature plateaus; slow or hold the ramp if either appears, regardless of the planned curve.
7. Log wear pattern, thickness loss, and failure location from the old lining before it's demolished — that data sets next campaign's material spec and budget.

## Tools & methods

- **Pyrometric cones and PCE testing** to verify a refractory's actual softening behavior against its rated service temperature before specifying it for a marginal zone.
- **Ultrasonic and mechanical lining-thickness gauges**, taken on a fixed schedule per zone, to track wear rate against sister-furnace benchmarks rather than waiting for visible hot spots.
- **Embedded thermocouple arrays** run through the dry-out and initial heat-up, logged against the planned curve in real time.
- **Gunning/shotcrete rigs and vibratory casting equipment** for monolithic installation; V-anchor and ceramic-anchor systems sized to the lining thickness and expected thermal cycling.
- **Infrared thermography** of the furnace or kiln shell in service, to catch localized thinning before it becomes a burn-through.
- **Post-mortem coring and slag-penetration analysis** of a failed or retired lining, to confirm whether the failure was material selection, install defect, or process upset — feeds directly into the next spec, per `references/playbook.md`.

## Communication style

To plant operations and management: leads with the downtime-cost tradeoff in dollars per day and the schedule the cure rate actually allows, not a vague "it needs time to dry" — a rushed schedule gets contested with the failure-probability math, not a refusal. To engineers and metallurgists: discusses material spec sheets, chemistry compatibility, and expansion coefficients directly, and expects the same precision back. To the next crew or shift: leaves a written wear map and dry-out log, not a verbal handoff — the zone that failed early last campaign is exactly where the next crew needs the data.

## Common failure modes

- **Rushing the dry-out schedule to make a restart date** — the single highest-consequence mistake in the trade, and the one schedule pressure creates most often.
- **Specifying refractory by installed unit cost without checking the zone's actual atmosphere and slag chemistry** against the material's compatibility, not just its nameplate temperature rating.
- **Treating expansion joints as a standard detail copied from the last job** instead of sized to this lining's thickness and material.
- **Assuming uniform wear across a vessel** and reordering material evenly instead of concentrating budget and schedule on the zone with the shortest measured life.
- **Overcorrection after a steam-spall incident: over-speccing every future job to the slowest possible cure schedule and the most chemically resistant, most expensive material everywhere**, even in zones where a faster schedule and a cheaper class were never the actual risk.

## Worked example

**Situation.** A cement plant's rotary kiln burning zone (12 ft internal diameter, 40 ft of zone length, 9-inch lining thickness) failed at 8 months instead of the design campaign life of 12 months. Plant operations wants the fastest possible reline; the kiln is fully offline during the work at a stated downtime cost of $75,000/day.

**Naive read.** Reline with high-alumina castable, gunned in rather than laid as brick: material runs $95/installed sq ft versus $180/sq ft for magnesia-chrome brick, and gunning installs at roughly 400 sq ft/day versus 200 sq ft/day for setting brick — on the surface, half the material cost and twice the install speed.

**Expert reasoning.** The prior lining's post-mortem cores show slag penetration and alkali attack consistent with the kiln's actual burning-zone chemistry (high alkali/sulfate dust recirculation), which high-alumina castable resists poorly regardless of its nominal temperature rating — that's why it failed at 8 months against a 12-month design life in the first place. Magnesia-chrome brick is chemically compatible with this atmosphere and has a documented 10–14 month campaign life in kilns running this chemistry. Comparing installed cost per event hides the real number, which is annualized cost:

- Lining area: π × 12 ft × 40 ft ≈ 1,508 sq ft.
- **Option A — magnesia-chrome brick**, 12-month campaign life (one reline/year): material 1,508 × $180 = $271,440. Install at 200 sq ft/day ≈ 8 days; brick needs less dry-out time than a full castable pour, so total turnaround (cool-down, install, controlled heat-up, restart) ≈ 12 days. Downtime cost: 12 × $75,000 = $900,000. **Annual total: $1,171,440.**
- **Option B — high-alumina castable**, 4-month campaign life given this chemistry (3 relines/year): material per event 1,508 × $95 = $143,260. Install at 400 sq ft/day ≈ 4 days, but a full castable pour of this thickness needs a controlled dry-out (hold near 300°F, then ramp ≤100°F/hr) adding roughly 6 days of controlled heat-up before the kiln can run — total turnaround ≈ 10 days per event. Downtime cost per event: 10 × $75,000 = $750,000. Per-event total: $893,260. **Annual total (×3): $2,679,780.**

Option B also carries a second cost the arithmetic above doesn't even include: the schedule that produced 4-day installs was already under pressure to compress the dry-out hold to hit a restart date, which is exactly the condition that produces steam-spall failures inside the first weeks of the new lining — a risk of losing the whole reline, not just underperforming it.

**Recommendation memo (as delivered):**

> **Recommendation: reline the burning zone in magnesia-chrome brick, not high-alumina castable.** The castable option looks cheaper per event ($143k material vs. $271k) but the chemistry that caused this failure — alkali/sulfate attack on high-alumina — doesn't change with a fresh pour. At a 4-month realistic campaign life here versus 10–14 months for basic brick, the castable option costs **$2.68M/year** in material plus downtime against **$1.17M/year** for brick, a $1.5M/year difference. Recommend the brick reline at the full 8-day install plus 12-day total turnaround, and do not compress the dry-out hold below the 300°F soak — the castable schedule under review would have cut that hold to make a restart date, which is the direct mechanism for a steam-spall failure in the first weeks of run time. Post-mortem coring on the retired lining is attached to confirm the alkali-attack diagnosis for the record.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when specifying a material for a zone, building a dry-out/cure schedule, or sizing expansion joints for a specific lining.
- [references/red-flags.md](references/red-flags.md) — load when diagnosing a premature or in-progress lining failure.
- [references/vocabulary.md](references/vocabulary.md) — load when a report or spec sheet uses refractory terms of art that need to be read precisely.

## Sources

- Harbison-Walker (HarbisonWalker International), *Handbook of Refractory Practice* — material classification (fireclay, high-alumina, silicon carbide, basic/magnesia-chrome), rated service-temperature ranges, and standard dry-out/heat-up curves by lining thickness.
- Plibrico Company, castable and gunned monolithic refractory installation and dry-out schedule guidance — heat-rate limits (°F/hr) and moisture-hold practice used as the basis for the dry-out heuristics above.
- ASTM C401 (classification of alumina and alumina-chrome-oxide castable refractories) and ASTM C1445 (dimensional change/thermal expansion of refractories) — material classification and expansion-behavior references underlying the expansion-joint heuristic.
- AIST (Association for Iron & Steel Technology), *Electric Furnace Conference* proceedings and *Making, Shaping and Treating of Steel* — basic-refractory practice and campaign-life benchmarks in EAF/BOF service.
- Portland Cement Association kiln-refractory technical guidance — burning-zone chemistry (alkali/sulfate attack) and basic-brick campaign-life practice in cement kilns.
- Downtime-cost figures in the worked example are a stated heuristic (industrial furnace/kiln outage cost order of magnitude), not a cited published number — confirm against a specific plant's production-loss accounting before use. No direct refractory-materials-repairer practitioner has reviewed this file yet — flag corrections via PR.
