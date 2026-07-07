# Playbook

Filled worksheets and rate tables for the five tasks this role executes most often: sizing a planting order, running a stocking survey, sizing fireline/fuel breaks, scheduling herbicide treatment, and planning daily crew production.

## 1. Planting density and seedling-order worksheet

Formula: `seedlings needed = acres × target trees-per-acre (TPA) × (1 + overage %)`. Overage covers cull stock, breakage in transit, and mortality expected before the trees ever go in the ground (typically 3–5% for bare-root, 2–3% for containerized).

| Species / product | Common spacing | Target TPA | Typical use case |
|---|---|---|---|
| Loblolly/slash pine, bare-root, industrial | 8×9 ft | ~605 | Southern pine plantation, pulp/sawtimber rotation |
| Loblolly pine, wide-spaced | 10×10 ft | ~435 | Longer sawtimber rotation, fewer pre-commercial thins needed |
| Douglas-fir, containerized (Pacific Northwest) | 10×10 ft | ~435 | Clearcut reforestation, mechanized site prep |
| Longleaf pine, containerized | 8×10 ft | ~545 | Restoration planting, higher survival priority over density |
| Hardwood (oak/walnut), bare-root | 12×12 ft | ~300 | Mast/timber hardwood restoration, wider spacing for crown development |

**Example order calc:** 40 acres, loblolly at 605 TPA, bare-root, 4% overage.
`40 × 605 = 24,200` base → `24,200 × 1.04 = 25,168` → order rounds to 25,200 (nursery ships in bundles of 25 or 50).

## 2. Stocking survey protocol (first-year and third-year)

- **Plot size:** 1/100-acre (radius 11.78 ft) or 1/50-acre circular plots, gridded or randomly placed at a density of roughly 1 plot per acre, minimum 20 plots per unit regardless of acreage.
- **Pass/fail threshold:** contract-specific, but 80% stocking (live seedlings at or above target density, or percent of plots with at least one live seedling for a "stocked/not-stocked" method) is the common state cost-share and industrial contract minimum at first-year exam.
- **Sub-area breakdown before ordering replant:** always tabulate plots by sub-area (slope position, skid-trail overlap, aspect, soil type) before deciding replant scope. A unit-wide average above threshold can still mask a sub-area failure that needs targeted replant; a unit-wide average below threshold can be driven entirely by one sub-area rather than requiring a full-unit redo.

| Sub-area | Plots | Expected (TPA × plot area) | Actual live | Survival % | Action |
|---|---|---|---|---|---|
| Skid-trail zone, 8 ac | 8 | 48 | 19 | 40% | Replant after scarification |
| Remaining unit, 32 ac | 32 | 192 | 158 | 82% | No action — above 80% threshold |
| **Unit total, 40 ac** | **40** | **240** | **177** | **74%** | Partial replant (skid-trail zone only) |

**Root-defect audit (run alongside any failed survey):** pull 200 seedlings at random from the failing sub-area, expose root systems, classify as straight/J-root/L-root/circling. A J+L rate above roughly 10–15% in the failing zone points to a planting-technique or soil-compaction cause; a rate in line with the rest of the unit points to a site factor (drought, browse, herbicide drift) instead.

## 3. Fireline and fuel-break width by fuel model

Per NWCG Fireline Handbook guidance, hand line and dozer line width and clearance scale with expected flame length, not a flat spec. Use the fuel model in effect for the section being lined, not the fuel model at the drop point.

| Fuel model (NFDRS) | Typical flame length | Minimum hand-line width | Clearance above line |
|---|---|---|---|
| Short grass (1) | 1–2 ft | 18 in to mineral soil | Waist-high both sides |
| Chaparral/shrub (4) | 6–12 ft | 3–4 ft to mineral soil | Full brush removal 6 ft both sides |
| Timber litter (9/10) | 2–4 ft | 2–3 ft to mineral soil | Overhead ladder fuels removed to 10 ft |
| Heavy slash (11/12) | 4–8 ft | 4–6 ft, dozer line preferred | Full slash removal 10 ft both sides |

**Rule of thumb applied:** minimum line width ≈ 1.5 × current flame length in light fuels, more in heavy/timber fuels where radiant heat and spotting distance both increase. A crew that measured a 4 ft flame length at 10am and cut a 6 ft line is in spec then; if wind pushes flame length to 8 ft by 1pm, that same line is now undersized and needs widening or the crew needs to disengage to a safety zone, not push the line under worse conditions.

## 4. Herbicide application rate table (common invasive targets)

| Target species/type | Method | Product/mode of action example | Rate | Timing window |
|---|---|---|---|---|
| Woody resprouter (e.g. tree-of-heaven, privet) | Cut-stump | Triclopyr, 20% in oil carrier | Apply to cut surface within 5 min of cutting | Dormant season (fall–winter) for best translocation, avoid heavy sap flow in spring |
| Woody resprouter, standing stems <6 in diameter | Basal bark | Triclopyr ester, 20–25% in oil | Full basal circumference to 12–18 in height | Year-round except when snow/water covers bark |
| Herbaceous invasive (e.g. Japanese knotweed) | Foliar systemic | Glyphosate, 2–5% solution | To wet, not runoff | Active growth, pre-flowering, avoid within 24 hr of rain |
| Invasive vine (e.g. kudzu) | Foliar systemic | Triclopyr or glyphosate mix, label rate | To wet, repeat treatment years 2–3 | Late-season active growth, before dormancy |

**Timing failure mode to check first:** a "treatment didn't work" report is more often a phenology mismatch (foliar systemic applied after the plant has begun translocating sugars to roots for dormancy, or cut-stump treatment applied to a species that sprouts from root suckers regardless of stump treatment) than an underdose. Confirm growth stage and species-specific resprout biology before increasing rate.

## 5. Daily crew production planning table

Base rate: 700–1,200 seedlings per planter per day on flat, loose, cleared ground with bare-root stock at typical industrial spacing. Adjust with terrain/condition multipliers, applied multiplicatively, not additively:

| Condition | Multiplier on base rate |
|---|---|
| Steep slope (>30%) | ×0.6–0.7 |
| Heavy slash/logging debris on site | ×0.7–0.8 |
| Containerized stock (heavier, larger hole) | ×0.85 |
| Compacted soil requiring scarification pass | ×0.6 |
| Rain/mud conditions | ×0.7 |

**Example:** base rate 900/day, steep slope (×0.65) and heavy slash (×0.75): adjusted rate = 900 × 0.65 × 0.75 ≈ 439/day per planter. A six-person crew planting a 40-acre, 24,000-seedling unit under these conditions needs `24,000 ÷ (6 × 439) ≈ 9.1 days`, not the 5 days a flat-ground estimate would suggest — schedule and cost the job off the adjusted rate, not the base rate, before quoting a completion date.
