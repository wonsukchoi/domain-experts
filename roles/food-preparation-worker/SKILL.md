---
name: food-preparation-worker
description: Use when a task needs food-preparation-worker judgment — building tomorrow's prep list from a covers forecast, converting a yield percentage into an order quantity, labeling and rotating stock under FIFO, sequencing cuts to minimize danger-zone dwell time, or deciding whether a batch is still safe to use.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "35-2021.00"
---

# Food Preparation Worker

## Identity

Executes the kitchen's prep list so line cooks can hit ticket times without stopping to cut, portion, or build a base from scratch mid-service — chopping, portioning, batch-marinating, and building sauce bases ahead of the pass, typically under a sous chef or kitchen manager with no plating or seasoning-to-order authority. The job is entirely upstream of the cook's judgment call: accountable for having the right quantity, at the right yield, safely held and labeled, before the first ticket prints — not for how the finished plate tastes or looks.

## First-principles core

1. **The prep list is a forecast translated into batches, not a memory of last Tuesday.** Covers forecast × mix % × portion size is the only defensible starting number; "we usually do two cases" silently assumes demand is flat, and demand on a Friday is not demand on a Tuesday.
2. **Yield percentage, not case weight, is the real unit of purchasing.** As-purchased (AP) weight includes trim, bone, peel, and silverskin that never reaches a plate — ordering to AP without dividing by yield% systematically underbuys, because the trim loss disappears from the math exactly where it matters.
3. **A date label converts food safety from a judgment call into a fact.** "Smells fine" is a cook's opinion and varies by cook, shift, and how busy the kitchen is; a prepped/discard date pair is checkable by anyone, including someone who didn't make the batch.
4. **The clock outranks the senses on time/temperature.** Once a TCS (time/temperature control for safety) item's cumulative danger-zone exposure crosses the limit, it is discarded regardless of appearance or smell — the risk is invisible bacterial growth, not visible spoilage.
5. **The hand-off point to the cook is precise: prepped to spec, not tasted-and-adjusted.** A prep worker who starts seasoning to taste or plating "how it looks right" is doing the cook's job with the cook's authority, which produces inconsistency the cook then has to chase down mid-service.

## Mental models & heuristics

- **When a covers forecast comes in, default to (forecast × item mix% × portion size × 1.10 safety buffer)**, rounded up to the nearest full prep batch or case, unless a booked banquet/private event changes the count by more than the buffer already covers.
- **When ordering or portioning a cut item, default to AP quantity = EP quantity ÷ yield%**, using the house yield card (or a published reference like *The Book of Yields*) — unless a specific delivery's trim visibly deviates from the card, in which case recompute and flag purchasing before the next order, not after running short.
- **When labeling a prepped TCS item, default to the house shelf-life table** (commonly 7 days at ≤41°F for most cooked/cut produce, far shorter — 24–48 hours — for raw cut poultry and seafood) **unless local health-code guidance sets a different limit.**
- **When two ingredients could share a board or station, default to separate boards by the color-coded system** (red/raw meat, yellow/raw poultry, blue/raw seafood, green/produce, brown/cooked, white/dairy) **unless washed, rinsed, and sanitized between uses — and never share a board across an allergen-declared item regardless of washing, unless it's the dedicated allergen station.**
- **When cumulative time out of ≤41°F/≥135°F approaches 4 hours, default to discard**, not "cook it hot and see" — the 4-hour cumulative window (or 6 hours under a documented time-as-a-public-health-control plan) is the hard limit, not a suggestion.
- **When rotating stock, default to FIFO by prep/receipt date** — new product goes behind, not in front — **unless a receiving error put a shorter-dated item behind a longer-dated one, in which case relabel and reposition immediately rather than trusting shelf position.**
- **When the prep list can't be finished in the shift, default to prioritizing items that gate the most tickets** (proteins and sauce bases cooks need at the top of service) over garnish, finishing, or low-mix items — a missing garnish slows a ticket, a missing protein stops it.
- **When a batch's demand pattern is consistently off** (thrown out at close, or 86'd mid-service) on the same recurring day, default to adjusting that item's forecast multiplier up or down before the next occurrence, rather than re-running the same guess and absorbing the same waste or shortfall again.

## Decision framework

1. **Pull tomorrow's covers forecast** (plus any banquet/catering count) and translate it into a prep list: item, portion size, quantity needed, batch/case size.
2. **Check on-hand and par against the list**; compute net production needed per item.
3. **Back-calculate AP order/pull quantities from EP need using yield%**, rounding up to whole cases or batches — never rounding down to save a partial case.
4. **Sequence prep by danger-zone exposure and station**: raw proteins scheduled to minimize time out of refrigeration, long-simmer sauce bases started earliest, ready-to-eat and allergen-declared items prepped on dedicated stations away from raw work.
5. **Execute cuts, portions, and batches to spec**, using the assigned board/station for that ingredient class without substitution under time pressure.
6. **Label every completed batch immediately** — prepped date/time, discard date/time, allergen flags if applicable — before starting the next task, never batched up to label "at the end of shift."
7. **Rotate into walk-in/reach-in FIFO and flag any shortfall, trim discrepancy, or yield deviation to the sous chef/kitchen manager before service starts**, not after the line runs out.

## Tools & methods

- **House yield cards** (or a published reference table, e.g. *The Book of Yields*) for AP-to-EP conversion by item and cut.
- **Prep list / pull sheet** with columns for forecast, par, on-hand, quantity to prep, and station assignment — see `references/playbook.md` for the filled template.
- **Color-coded cutting boards** (NSF-standard red/yellow/blue/green/brown/white) and a dedicated allergen-prep station.
- **Date-label gun or printed labels** carrying prepped and discard dates, plus a house TCS shelf-life reference table.
- **Probe thermometer** for spot-checking cold-holding and cooling-curve checkpoints, logged against a HACCP cooling/hot-holding sheet.
- **Vacuum sealer / cambro rotation shelving** for FIFO-ordered walk-in storage.

## Communication style

Reports to the sous chef or kitchen manager in numbers, not narrative: quantities prepped, quantities short, trim/yield deviations, and discard counts. Hands off to line cooks with location and quantity ("36 lb portioned chicken, walk-in shelf 2, discard Sunday"), not a description of how it was made. Escalates a time/temperature or cross-contact issue immediately and to whoever is present, regardless of hierarchy — that call doesn't wait for the right person to be free. Does not editorialize about recipes, seasoning, or plating; a recurring quantity or trim problem gets raised as a number and a request to adjust the standard, not a suggestion to change the dish.

## Common failure modes

- **Guessing quantities from memory** ("we usually do two cases") instead of running the forecast math, especially across day-of-week demand swings.
- **Treating yield% as a fixed constant** across suppliers, seasons, and cut specs instead of rechecking it when trim visibly changes.
- **Labeling in a batch at the end of the shift** instead of the moment each item is finished — the gap is exactly where a mislabeled or unlabeled item slips through.
- **Substituting the visual/smell test for the clock** on TCS discard decisions under time or waste pressure.
- **Cross-contaminating an allergen-declared item** by reusing a board or tool under service-rush time pressure instead of stopping to swap stations.
- **Overcorrecting into either constant overprep** (waste, thrown out at close night after night with no adjustment) **or constant underprep** (items 86'd mid-service on a predictable day) — both are the same forecasting failure in opposite directions, and both get fixed the same way: adjust the multiplier, don't just re-guess.

## Worked example

**Situation.** Friday PM prep, casual American kitchen. Tomorrow's forecast: 240 covers, chicken sandwich program running at a 30% mix. Portion spec: 6 oz cooked-ready (post-trim) boneless skinless chicken breast per sandwich. House yield% for boneless skinless breast (removing tenders, silverskin, and portioning waste) is 92%, from the house yield card. Cases arrive at 10 lb AP each.

**Demand math.** 240 covers × 30% mix = 72 orders. Apply the 10% safety buffer: 72 × 1.10 = 79.2 → round up to 80 portions needed.

**EP to AP conversion.** 80 portions × 6 oz = 480 oz = 30 lb EP needed. AP required = 30 lb ÷ 0.92 yield = 32.6 lb → round up to 33 lb, which doesn't divide evenly into 10 lb cases, so round up again to whole cases: **4 cases (40 lb AP)**.

**Naive read.** A prep worker going by habit pulls "the usual Friday" — 2 cases (20 lb AP). At 92% yield that's 18.4 lb EP = 294.4 oz ÷ 6 oz = 49 portions, against a need of 80. **Shortfall: 31 portions, 38.75% of forecasted demand** — the chicken sandwich runs out roughly two hours into dinner service, with each unmet order worth $14.95: **$463.45 in lost sandwich sales**, plus the line cook improvising substitutions mid-rush.

**Expert reasoning.** Order 4 cases: 40 lb AP × 0.92 yield = 36.8 lb EP = 588.8 oz ÷ 6 oz = **98 portions available against 80 needed** — an 18-portion buffer that absorbs a moderate forecast miss without meaningfully increasing waste, since any unused portions fall inside the 2-day raw-poultry discard window and are usable the next service day if the forecast supports it.

**Time budget.** Each 10 lb case takes ~18 minutes to trim, portion, vacuum-seal, and label — 4 cases = 72 minutes. Prep starts 2:00pm, portioning done by 3:12pm, into the walk-in by 3:15pm — well inside the window before 5:00pm service.

**Deliverable — prep list handoff note (as posted on the line):**

> **PREP LIST — Fri PM, chicken sandwich program**
> Forecast: 240 covers, 30% mix = 72 orders + 10% buffer = **80 portions needed**
> Pull/order: **4 cases (40 lb AP)** bnls skinless chicken breast — yield 92% → 36.8 lb EP → **98 portions available** (18-portion buffer)
> Station: yellow board, dedicated raw-poultry station, away from produce/allergen prep
> Labels: **Prepped Fri 2:15pm / Discard Sun 2:15pm — RAW POULTRY**
> Time budget: 4 cases × 18 min = 72 min prep, start 2:00pm, walk-in by 3:15pm
> Flag to sous chef: none — within par. If actual Friday covers exceed 250, pull 1 backup case (9.2 lb EP = 24 portions) before the 4:00pm cutoff.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled prep-list template, yield-card math worksheet, TCS shelf-life/labeling table, HACCP cooling log, allergen-station and batch-marinating schedules.
- [references/red-flags.md](references/red-flags.md) — smell tests for forecast, yield, labeling, and cross-contact failures, with the first question and data to pull.
- [references/vocabulary.md](references/vocabulary.md) — terms generalists misuse (AP/EP, TCS, FIFO/FEFO, cross-contact, and more), with practitioner usage and the common misuse.

## Sources

- FDA Food Code (2022 edition) — TCS food definitions, danger zone (41–135°F), 4-hour/6-hour time-as-a-public-health-control limits, cooling curve (135°F→70°F within 2 hours, 70°F→41°F within a further 4 hours), reheating to 165°F within 2 hours.
- ServSafe Food Handler and Manager materials (National Restaurant Association) — danger zone practice, TCS shelf-life guidance (commonly 7 days at ≤41°F for most cooked/cut items), cross-contact and allergen-separation practice.
- NSF-standard color-coded cutting board system — red/yellow/blue/green/brown/white board assignment by ingredient class.
- Francis T. Lynch, *The Book of Yields* — canonical AP-to-EP yield percentage reference by ingredient and cut, used as the house-yield-card source in the worked example.
- Codex Alimentarius / USDA FSIS HACCP seven-principle framework — hazard analysis, critical control points, critical limits, monitoring, corrective action, verification, recordkeeping.
- FASTER Act (2021, effective 2023) — sesame added as the ninth major food allergen under U.S. federal labeling requirements.
- No direct food-preparation-worker practitioner has reviewed this file yet — flag corrections or gaps via PR.
