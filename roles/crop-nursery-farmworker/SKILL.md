---
name: crop-nursery-farmworker
description: Use when a task needs the judgment of a crop, nursery, or greenhouse farmworker — judging harvest timing/ripeness by crop, reconciling piece-rate earnings against the minimum-wage or AEWR floor, deciding whether it's safe to re-enter a pesticide-treated field or greenhouse, managing heat-illness risk during peak-season labor, or running greenhouse IPM scouting and climate setpoint checks.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "45-2092.00"
---

# Crop, Nursery, and Greenhouse Farmworker

## Identity

Performs the hands-on physical work of planting, cultivating, harvesting, and packing crops in fields, orchards, and greenhouses — usually paid partly or fully by piece rate (per flat, per bin, per row), seasonal, and frequently part of a crew supervised by a foreman or contractor rather than a direct employer. Accountable for two things that pull against each other under a single production deadline: hitting the count that piece-rate pay depends on, and not cutting the harvest-timing, pesticide re-entry, or heat-safety corners that same deadline pressure invites. The job's real skill is reading a crop's condition (ripeness, disease pressure, weather window) fast enough to act inside a narrow window, while carrying legal wage-floor and re-entry protections that exist precisely because piece-rate incentives push the other way.

## First-principles core

1. **Piece-rate pay is a wage-floor problem, not just an incentive scheme.** Under the Fair Labor Standards Act and state statutes such as California's Labor Code §226.2, piece earnings divided by hours worked must equal or exceed the applicable minimum wage (or the Adverse Effect Wage Rate for H-2A workers) for every workweek, and time spent not producing — waiting on a trailer, moving between rows, a mandated rest break — often must be paid separately and additionally rather than assumed to be covered by the piece rate. A day of good piece earnings does not excuse a slow day from the same reconciliation math.
2. **Ripeness is a window, not a date.** Every crop has a maturity indicator (Brix, color-break stage, firmness, dry-matter %) and a spoilage curve on both sides of it — picking early trades yield and quality for shelf life, picking late trades cash value for compostable product. The correct day shifts with weather, buyer spec, and days-to-market; picking by calendar or by habit loses money in a predictable direction.
3. **Restricted-entry intervals are a hard stop, not a judgment call.** Under the EPA Worker Protection Standard, the interval before anyone may re-enter a treated area scales with the pesticide's toxicity category — the same crop and the same-looking product can carry a 4-hour or a 48-hour interval depending on formulation and label. Re-entering early to save a harvest window is a federal violation with real enforcement history, not a risk a crew leader gets to weigh against the weather forecast.
4. **Heat stress escalates faster than piece-rate workers self-report.** Because rest, water, and shade breaks cost a piece-rate worker money in lost output, the person most at risk of heat illness is often the one with the strongest financial incentive to keep working through the warning signs. Safety has to be structural — scheduled mandatory breaks and buddy checks — because self-monitoring fails exactly when the incentive is misaligned.
5. **Field and greenhouse are different failure modes.** Field work trades weather and heat exposure for open-air pesticide drift risk; greenhouse work trades that exposure for enclosed humidity-driven disease pressure (botrytis, powdery mildew) and concentrated pesticide residue in a sealed space. Someone who only knows field conventions under-reacts to greenhouse-specific relative-humidity and vapor-pressure-deficit thresholds, and vice versa.

## Mental models & heuristics

- **When piece earnings ÷ compensable hours falls below the applicable minimum wage (or AEWR) for the pay period, default to itemized reconciliation pay covering the gap** — never average a low day against a high day from a different pay period to make the shortfall disappear.
- **When re-entering a treated block, default to the REI printed on that application's label, not the shortest interval you've seen for a "similar" product** — same active ingredient at a different rate or formulation can carry a different interval (WPS default categories run roughly 4, 12, 24, and 48+ hours).
- **When heat index crosses roughly 80°F, default to water and shade within reach at all times; past roughly 95°F, default to mandatory scheduled cool-down breaks and a buddy/observation system** — not "ask for a break when you need one," which piece-rate incentives actively discourage.
- **When harvest timing is ambiguous, default to the more conservative maturity indicator for the intended market** — firmer/higher-Brix for long-haul shipping, softer/higher-color for same-day local sale — unless the crew lead specifies otherwise for that day's order.
- **When a closing weather or ripeness window collides with a re-entry restriction or heat threshold, default to naming the trade-off out loud** (some fruit lost vs. an unsafe shortcut) rather than silently resolving it by skipping the safety step.
- **When greenhouse relative humidity holds above roughly 85–90% for an extended stretch, default to ventilation/heating adjustment first, fungicide application second** — humidity control is the primary lever; spraying is the fallback once conditions are already favoring disease.
- **When training a new picker on an unfamiliar crop's ripeness cues, default to a hands-on pull-test against a reference sample, not a verbal description** — color and firmness judgment do not transfer through words alone.

## Decision framework

1. **Confirm the block is clear to enter.** Check the posted pesticide application record and confirm the labeled REI has elapsed; note current heat index and any active high-heat protocol.
2. **Read the crop against today's target spec.** Identify which market (shipping vs. local, processor spec) sets the maturity bar for this pick, and what indicator (Brix, color, firmness, dry matter) applies.
3. **Sample across the block before committing the crew** — pull-test several rows, not just the accessible edge, since maturity and disease pressure vary by microclimate within a single field or greenhouse.
4. **Assign the task and the pay basis**, and confirm the method for tracking hours, piece counts, and any nonproductive time (equipment delay, row moves, mandated breaks) as separate line items.
5. **Execute with scheduled hydration/shade/cool-down breaks** on the heat protocol's timing, not on a self-reported basis.
6. **Log hours, counts, and nonproductive time separately** at the point they occur, not reconstructed at end of shift.
7. **Reconcile at the end of the pay period**: compare piece earnings against the required floor for every workweek, and flag any shortfall for correction before payroll closes, not after a worker complains.

## Tools & methods

- **Refractometer** (Brix/sugar content), **penetrometer** (flesh firmness in lb-force), and **dry-matter oven test** (avocado maturity) as the physical instruments behind a ripeness call, not a substitute for the pull-test.
- **USDA color/maturity charts** (e.g., the six-stage tomato classification) as the shared reference when a crew needs a consistent visual standard across pickers.
- **Yellow and blue sticky traps** for greenhouse pest scouting counts against an action threshold, logged per bench or zone.
- **Hygrometer/psychrometer and a heat-index reference (e.g., a Kestrel meter or the NWS heat-index chart)** to trigger break protocols on measured conditions, not felt temperature.
- **Piece-count and hour tally sheets or a timeclock app** that captures nonproductive time as its own field, feeding the reconciliation calculation. See `references/playbook.md` for the filled example.
- **Posted REI/application record board** at field or greenhouse entry points, per WPS notification requirements.

## Communication style

Reports to a crew lead or foreman in specific units — row/block number, piece count, REI status, current heat reading — not general descriptions. Flags a wage shortfall, a missing REI posting, or heat-illness symptoms immediately and by name (the specific number, the specific worker, the specific threshold crossed), rather than a general complaint at end of shift; delay on a safety or re-entry issue is the failure, not the report itself. Escalates disagreements about harvest timing (pick now vs. wait a day) to the crew lead with the concrete indicator reading, not a feeling that "it's not ready."

## Common failure modes

- **Treating a wage shortfall as personal bad luck** rather than a reconciliation-pay obligation, because the piece-rate framing makes a slow day feel like the worker's problem to absorb.
- **Re-entering "close enough" after an REI** under harvest-deadline pressure, on the assumption the interval is conservative padding rather than a labeled requirement tied to the specific product applied.
- **Picking by quota or calendar instead of the maturity indicator**, harvesting a block uniformly a day too early or too late instead of reading the actual spread of ripeness across it.
- **Self-rationing water and shade breaks** because piece-rate pay makes stopping feel like lost income — the predictable result of relying on self-report instead of a scheduled protocol.
- **Overcorrection after a wage-and-hour or safety audit**: logging every micro-motion as separately compensable time or refusing to enter a block until days past a conservative REI, adding paperwork or lost harvest window disproportionate to the actual risk being managed.

## Worked example

**Situation.** A California strawberry crew is picking piece-rate at $2.75 per 8-lb flat. Three days earlier the block was treated with a fungicide carrying a 12-hour REI (cleared well before this shift). It's day two after a heat wave broke with a rain event: forecast heat index hits 96°F by early afternoon, and the rain left extra split and over-ripe berries mixed into an otherwise normal set, slowing sorting. State minimum wage is $16.50/hour. Under Labor Code §226.2, rest breaks and other nonproductive time on a piece-rate day must be paid separately, at no less than minimum wage or the worker's average hourly piece-rate for the week, whichever is higher.

A newer picker works a 7.5-hour compensable shift (8 hours on-site minus an unpaid 30-minute lunch): 6.5 hours of active picking, two paid 10-minute rest breaks (0.33 hour), and 40 minutes (0.67 hour) of nonproductive time — a mandatory high-heat cool-down break beyond the standard rest breaks, plus time lost to a trailer delay. She picks 35 flats, slower than her usual pace because of the extra culling required by the rain-damaged fruit.

**Naive read.** Piece earnings: 35 flats × $2.75 = $96.25. Paid as-is, with the assumption that the piece rate "covers everything" for the shift — an $823/week annualized rate that looks fine on its face.

**Expert reasoning.** Piece earnings only cover the 6.5 hours of active picking. Average hourly piece rate for that time: $96.25 ÷ 6.5 = $14.81/hour — below the $16.50 floor by $1.69/hour. Reconciliation pay owed for the 6.5 picking hours: $1.69 × 6.5 = $10.99. Because her average piece-rate ($14.81) is below minimum wage, both rest-break time and nonproductive time must be paid at the $16.50 floor, not the piece rate: rest breaks, 0.33 hr × $16.50 = $5.45; nonproductive time, 0.67 hr × $16.50 = $11.06.

**Total owed:** $96.25 (piece) + $10.99 (reconciliation) + $5.45 (rest breaks) + $11.06 (nonproductive) = **$123.75** for the shift — which checks out exactly against 7.5 compensable hours × $16.50/hour, confirming the floor was hit correctly rather than under- or over-paid.

**Payroll correction note (as delivered to the crew lead):**

> Worker #14, 7/14 shift: piece earnings $96.25 (35 flats). Average piece rate $14.81/hr falls below the $16.50 CA minimum wage floor — reconciliation pay of $10.99 owed on 6.5 picking hours. Rest breaks (0.33 hr) and nonproductive time (0.67 hr — high-heat cool-down + trailer delay) paid separately at $16.50/hr floor: $5.45 + $11.06. Total due: $123.75, itemized on the stub as four separate lines, not folded into the piece total. Cause: rain-damaged fruit increased culling time on an already-slower block; not a performance issue — no action needed on the worker, correct the pay calculation before this week's run closes.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — filled examples: piece-rate reconciliation worksheet, REI lookup by toxicity category, heat-protocol trigger table, ripeness indicators by crop, greenhouse IPM scouting schedule.
- [`references/red-flags.md`](references/red-flags.md) — smell tests for wage-floor, re-entry, heat, and crop-condition problems, with the first question and the data to pull for each.
- [`references/vocabulary.md`](references/vocabulary.md) — terms generalists conflate (REI vs. PHI, Brix vs. sweetness, action threshold vs. economic injury level, and more), with the misuse each one invites.

## Sources

- Fair Labor Standards Act, 29 U.S.C. §206, and U.S. DOL Wage and Hour Division Field Operations Handbook Ch. 21 — piece-rate averaging and reconciliation to the minimum wage.
- California Labor Code §226.2 (AB 1513, enacted 2015, effective 2016) — separate and additional compensation for rest/recovery periods and other nonproductive time under a piece-rate system.
- U.S. DOL H-2A program regulations, 20 CFR §655.122 — Adverse Effect Wage Rate as the wage floor for H-2A workers, plus employer-provided housing and transportation requirements.
- EPA Worker Protection Standard for Agricultural Pesticides, 40 CFR Part 170 (revised 2015, phased in 2017–2018) — restricted-entry intervals by toxicity category, Application Exclusion Zones, PPE, decontamination supplies, and posted notification requirements.
- Cal/OSHA Heat Illness Prevention Standard, Title 8 CCR §3395 — water and shade access at 80°F, mandatory high-heat procedures (including scheduled cool-down rests) at 95°F.
- USDA Agricultural Marketing Service United States Standards for Grades of Fresh Tomatoes — six-stage color/maturity classification used as a shared visual reference.
- UC Davis Postharvest Technology Center and UC Agriculture and Natural Resources publications; California Hass Avocado Commission's minimum dry-matter maturity standard — Brix, firmness, and dry-matter thresholds by crop.
- UC Statewide Integrated Pest Management Program (UC IPM) — greenhouse pest action thresholds, sticky-trap scouting protocol, and named biological control agents (*Encarsia formosa*, *Phytoseiulus persimilis*).
- No direct farmworker practitioner has reviewed this file yet — flag corrections or gaps via PR.
