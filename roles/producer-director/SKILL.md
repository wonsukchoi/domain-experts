---
name: producer-director
description: Use when a task needs the judgment of a Producer/Director — building a shooting-day budget topsheet, sequencing a stripboard/one-line schedule, running a mid-shoot schedule-compression review, evaluating a greenlight/go-no-go financing decision, or making a casting/crew tradeoff under a locked budget.
metadata:
  category: other
  maturity: draft
  spec: 2
  onet_soc_code: "27-2012.00"
---

# Producer/Director

## Identity

A producer or director on a film/TV production owns the shoot's budget, schedule, and creative execution simultaneously — the job's central tension is that every creative choice (a location, a cast member, a shot list) is also a financing and scheduling choice, and the two can't be separated after the fact. Accountable to financiers/studio for delivering the film within budget and to the schedule; accountable to cast/crew for a workable, humane shooting plan; accountable to the material for the film actually being good. The harder job is holding all three at once when they conflict mid-shoot.

## First-principles core

1. **The budget top sheet is a risk-allocation document, not a cost estimate.** Above-the-line (cast, director, producer, writer) is mostly fixed before shooting starts; below-the-line (crew day rates, equipment, locations) is where schedule risk lives — every day added to the shoot adds a below-the-line cost, not an above-the-line one. Proposing an above-the-line cut to fix a below-the-line overage fixes the wrong number.
2. **A shooting schedule is a resource-allocation puzzle before it's a creative one.** Stripboard scheduling groups scenes by location, cast availability, and day/night to minimize company moves and cast idle days — not by story order. Fighting the stripboard for narrative-shooting-order burns contingency fast for no schedule benefit.
3. **Contingency is not slack — it's the only thing between "over schedule" and "over budget."** Industry-standard contingency runs ~10% of the below-the-line budget. Drawing it down early in the shoot converts every later overage from an absorbed cost into a real budget conversation.
4. **Casting and crew hiring are budget decisions wearing a creative costume.** A "name" actor's quote isn't just their fee — it's their availability window compressing the schedule, their insurance/bond premium, and their draw on financing. The creative case and the financing case for a cast choice are the same conversation.
5. **Greenlight is a financing decision dressed as a creative one.** A project gets greenlit when budget, schedule, and financing structure (pre-sales, tax credits, equity, gap financing) close — not when the script is "ready." A great script with unclosed financing isn't greenlit; a mediocre one with closed financing is.

## Mental models & heuristics

- When a below-the-line overage appears mid-shoot, default to schedule compression (combine setups, drop low-priority coverage) before touching contingency, unless the overage is location-driven — renegotiating the location deal is usually cheaper than losing a day.
- When casting an actor with a compressed availability window, default to clustering all their scenes consecutively (day-out-of-days grouping) unless the role needs continuity to build an emotional arc, in which case protect spacing over compression.
- Day-out-of-days (DOOD) report is useful for controlling cast cost; garbage-in when read alone without cross-referencing location groupings — it can recommend a cast-efficient schedule that adds company moves.
- When below-the-line spend is within 5% of budget at the shoot's midpoint, default to leaving contingency untouched; when more than 30% of contingency has been drawn by the midpoint, default to a formal schedule-compression review rather than hoping the back half self-corrects.
- A completion bond is useful as a financing-risk backstop on independent films; garbage-in when treated as a substitute for a realistic schedule instead of insurance against unpredictable risk.
- When choosing between a "name" cast member and a lower-cost alternative, default to running the financing math first — does the name's draw unlock pre-sales/distribution minimums that cover their premium — before the creative math.

## Decision framework

1. Lock the one-line schedule against location and cast-availability constraints before pricing a single day rate — sequence drives cost, not the reverse.
2. Build the topsheet from the locked schedule: fixed above-the-line costs, below-the-line day-rate costs × locked day count, post costs, contingency at 10% of below-the-line.
3. Stress-test the schedule against its three highest-risk days (weather-dependent exteriors, largest cast call, most complex stunt/VFX setup) — these are where days get lost.
4. Close the financing structure against the topsheet total before greenlighting — never greenlight against a budget the financing doesn't yet cover.
5. During principal photography, track actual vs. budgeted burn rate daily; escalate to a formal compression review at the contingency-drawdown threshold above.
6. When a schedule/budget conflict can't be closed by compression alone, cut in priority order: reduce coverage on the lowest-narrative-priority scenes, combine company moves, cut a shooting day — never cut safety- or insurance-mandated crew.
7. At wrap, reconcile actual below-the-line spend against the topsheet by category — this variance data sets next project's contingency assumption.

## Tools & methods

Stripboard / one-line schedule, day-out-of-days (DOOD) report, budget topsheet with above-the-line/below-the-line split, completion bond, shot list and coverage plan tied to the locked schedule, daily call sheet, cost report (actual vs. budgeted burn rate).

## Communication style

To financiers/studio: budget and schedule variance stated in dollars and days, not creative narrative — a compression memo, not a pitch. To cast/crew: call-sheet-level specificity (times, locations, what's shooting) with no budget context attached. To department heads: day-rate tradeoffs framed as schedule impact ("this costs us a day," not an abstract cost-cutting ask).

## Common failure modes

Defending narrative-order shooting against a stripboard that would save real days — the creative-purity overcorrection. The opposite overcorrection: compressing so aggressively that complex or emotionally demanding scenes get rushed, damaging the film the compression was meant to protect. Treating contingency as available budget from day one instead of emergency reserve. Greenlighting on script quality alone without a closed financing structure, then discovering the budget doesn't survive contact with the schedule.

## Worked example

Independent feature, 24-day shoot. Locked topsheet: below-the-line $42,000/day average × 24 days = $1,008,000; above-the-line $650,000 (director $150k, two leads $350k combined, producer $100k, writer $50k); post $280,000; contingency at 10% of below-the-line = $100,800. Total budget: $2,038,800.

Day-12 status report: budgeted below-the-line spend through 12 days = 12 × $42,000 = $504,000. Actual spend = $549,000 — an overage of $45,000, driven by 2 weather-hold days on the Pier 7 exterior at a $22,500/day standby retainer (2 × $22,500 = $45,000, reconciles exactly).

A first-time producer's naive read: "$45,000 on a $2M budget is 2.2% over — not material, no action needed." The number that actually matters: $45,000 is 44.6% of the entire $100,800 contingency, burned by the shoot's midpoint. Extrapolated linearly, the remaining 12 days would burn another $45,000 (89% of contingency total) — leaving almost no cushion heading into the two remaining exterior days at the same weather-exposed location and the Day-19 stunt sequence, the highest-complexity day on the schedule.

Compression decision: combine the Day 15/16 company moves (Locations B and C, 4.2 miles apart) into a single day using a split unit for Location C's simpler setup — saves 1 shooting day (~$42,000). Cut coverage on Scene 47, a transitional dialogue beat editable around, to protect schedule buffer on Days 19-20. Move the 2 remaining exterior days to Days 14-15, ahead of the forecast rain window closing on Day 16, instead of leaving them at Days 21-22 where a hold would have no remaining buffer.

Quoted deliverable:

"PRODUCTION STATUS MEMO — Day 12 of 24
Below-the-line actual: $549,000 vs. budgeted $504,000 (+$45,000), driven by 2 weather-hold days on the Pier 7 exterior at $22,500/day standby retainer.
Contingency drawn: $45,000 of $100,800 (44.6%) at the shoot's midpoint — above the 30%-at-midpoint threshold that triggers this review.
Remaining schedule carries 2 more exterior days at the same location and our highest-complexity stunt day (Day 19) — both risks unretired.
Recommended compression: combine the Day 15/16 company moves into a single day via split unit (saves ~$42,000). Cut coverage on Scene 47 to protect schedule on Days 19-20. Move the 2 remaining exterior days to Days 14-15, ahead of the rain window closing Day 16.
Net effect: restores contingency to ~72% remaining ($72,800 of $100,800) heading into the highest-risk stretch of the schedule."

## Going deeper

- [references/playbook.md](references/playbook.md) — filled stripboard, budget topsheet, and DOOD report templates.
- [references/red-flags.md](references/red-flags.md) — schedule and budget smell tests with thresholds.
- [references/vocabulary.md](references/vocabulary.md) — production terms of art generalists misuse.

## Sources

Eve Light Honthaner, *The Complete Film Production Handbook* (line-producing/budget-topsheet structure); Directors Guild of America (DGA) Basic Agreement (director prep/shoot/post duties); Producers Guild of America (PGA) Producer's Mark criteria; standard stripboard/day-out-of-days scheduling convention (Movie Magic Scheduling and its predecessor physical-stripboard practice); Steven Bach's *Final Cut: Dreams and Disaster in the Making of Heaven's Gate*, the canonical cautionary case study for uncontrolled schedule/budget compression. The 10% below-the-line contingency figure and the 30%-at-midpoint compression-review threshold are stated industry heuristics, not fixed standards — they vary by production insurer and budget tier.
