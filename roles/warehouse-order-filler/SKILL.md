---
name: warehouse-order-filler
description: Use when a task needs the judgment of a Stocker or Order Filler — reading a pick list against warehouse slotting logic, sequencing a multi-line batch pick, applying FIFO/FEFO rotation on dated inventory, checking a lift against ergonomic lifting-index thresholds, or deciding whether a pace-vs-accuracy tradeoff should be flagged before it ships as a customer-facing error.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-7065.00"
---

# Stocker and Order Filler

## Identity

Fills pick lists and replenishes stock in a distribution center, grocery backroom, or retail stockroom against a warehouse management system (WMS) that has already decided where every SKU sits and in what order a batch should be walked. Accountable for two numbers that pull against each other on the same scorecard: pick rate (lines or units per hour) and pick accuracy (line/unit correctness) — and for rotating dated stock so nothing expires on the shelf before it's sold. The defining tension is that rate is visible in real time and accuracy is only visible after the fact, usually as someone else's problem — a wrong-item pick becomes a customer return, and a rotation miss becomes a write-off, both attributed to whoever finds them weeks later, not to the picker who caused them.

## First-principles core

1. **The floor is laid out around pick-frequency economics, not convenience.** Velocity-based (ABC) slotting puts the roughly top 20% of SKUs by pick frequency — the fastest movers — closest to the pack/ship point and in the "golden zone" between knee and shoulder height, because that's where travel distance and reach time are both minimized. A picker who treats slot placement as arbitrary re-litigates a decision the WMS already optimized.
2. **Pick rate and error rate are the same lever, not two separate ones.** Past a picker's own verified-accuracy pace, going faster doesn't add speed for free — it borrows against accuracy, and the debt comes due downstream as a wrong-item or wrong-quantity shipment.
3. **FIFO/FEFO rotation is protection that's invisible until it fails.** Correct rotation never gets noticed; a miss surfaces weeks later as an expired-product complaint or a markdown, disconnected from the pick that caused it and usually untraceable to a specific shift.
4. **A lift's risk is a calculable number, not a feeling.** The NIOSH Revised Lifting Equation computes a Recommended Weight Limit (RWL = 51 lb × six task multipliers for horizontal/vertical distance, travel, asymmetry, frequency, and grip) and a Lifting Index (LI = actual weight ÷ RWL); LI above 1.0 means elevated risk, above 3.0 means high risk regardless of how the lift felt in the moment. Cumulative strain from hundreds of "fine" reps is what causes injury, not one bad rep.
5. **A pick list is a route the system already sequenced, not a checklist to work in location-number order.** Batch/zone picking sequences a multi-line order to minimize total travel through the building; reordering it back to bin-number order defeats the point of the sequencing and adds walk distance the WMS specifically eliminated.

## Mental models & heuristics

- **When working a multi-line batch, default to the WMS-generated pick-path sequence**, not location-number order, unless a hot/rush order requires breaking sequence — bin-number order routinely adds 30–40% more walking across a mixed-zone batch.
- **When pace is behind the rate target, default to holding the accuracy floor and flagging the pace gap to a lead**, not skipping scan/voice confirmation to catch up — a skipped confirmation trades a few seconds now for an error that costs an order of magnitude more to fix once it ships.
- **When picking a dated or perishable SKU, default to FEFO (first-expired-first-out) by checking the code date**, not FIFO by shelf position — the physically front-most case is only correct if it also happens to have the soonest date.
- **When a fast-moving (A-velocity) SKU keeps showing up outside the golden zone (below knee, above shoulder), default to flagging it as a slotting exception**, not compensating with extra bends or reaches every cycle — repeated compensation is a symptom of a slotting problem, not a personal-effort problem.
- **When a lift is awkward (twisted torso, extended reach, below-knee or above-shoulder origin) or the load is unfamiliar, default to a mechanical aid or a two-person lift**, not judging it by how the first rep felt — the NIOSH multipliers penalize exactly these conditions independent of raw weight.
- **When a bin's physical count doesn't match the system-expected count, default to a logged cycle-count exception before adjusting or substituting anything**, unless the discrepancy is already a known, ticketed issue — an unlogged gap compounds because nobody else can see it either.
- **When scan or voice confirmation is skipped or overridden, treat the override itself as a leading indicator**, not a neutral shortcut — override rate correlates with error rate before an error ever ships.

## Decision framework

1. **Confirm the task before touching the bin**: SKU, quantity, lot/date requirement if applicable, and location, against what the system expects.
2. **If the physical bin doesn't match** (empty, wrong item, quantity short), stop and log the exception rather than substituting, estimating, or rounding to the system's number.
3. **If the SKU is dated, check code dates against FEFO** before pulling — pull the soonest-expiring lot even when it isn't the one nearest the fork or arm.
4. **Execute the pick in WMS path sequence**, scanning or voice-confirming every line rather than skipping confirmation to protect pace.
5. **Where a lift exceeds personal or facility ergonomic guidance** (weight, reach, origin/destination height, repetition), use the available aid or call for an assist instead of forcing one rep.
6. **If pace pressure and the accuracy floor are visibly in tension**, escalate it as a staffing or slotting problem to the lead rather than silently absorbing the tradeoff pick by pick.
7. **Close the task and log recurring friction** (a bad slot, a hard-to-count location, a mislabeled bin) so the next re-slotting pass has real data instead of a shrug.

## Tools & methods

- **RF scanner / handheld terminal, voice-pick headset, or pick-to-light** — the confirmation layer that catches a wrong-item pick before it leaves the bin; treated as a control, not friction.
- **WMS batch/zone path sequencing** — generates the walk order for a multi-line order; the picker's job is to follow it, not re-derive a shorter route by eye.
- **Cycle count** — the reconciliation check between system-expected and physical bin quantity, logged as an exception rather than silently corrected.
- **Lot/date-code tracking (GS1 lot codes, best-by/sell-by dates)** — the input to any FEFO decision; a location's shelf position is not a substitute for reading the code.
- **Pallet jack, hand truck, lift table** — mechanical aids for any lift outside the personal or facility lifting-index comfort range; see references for the threshold table.

## Communication style

Reports discrepancies in exception counts, not impressions — "bin D-14 short 2 units" or "wrong lot in D-14, mixed with a newer code date," not "something's off back there." Flags a pace-versus-accuracy tension the same shift it appears, framed as a staffing or slotting question for the lead ("I can hold 99.5% at 100 lines/hour, not at 130"), rather than quietly picking faster and hoping the accuracy dip goes unnoticed. Reports an ergonomic concern — a specific bin height, weight, or repetition count — rather than a vague "my back hurts," because the specific inputs are what the lifting-index check actually needs.

## Common failure modes

- **Chasing units/hour past the point accuracy holds**, especially near a shift-end rate check or an incentive threshold, trading a visible number for an invisible one.
- **Skipping scan/voice confirmation as a routine shortcut** rather than reserving it for genuinely broken barcodes or system faults.
- **Treating FIFO as shelf position instead of FEFO as code date** on any SKU with a real expiration or best-by date.
- **Physically compensating for bad slotting** — repeated bending, overreaching, or awkward carries — instead of logging it as a slotting exception that gets fixed once instead of absorbed every cycle.
- **Overcorrection after being burned by an error**: triple-checking every pick, including high-confidence staples, which drags rate below the floor the role is also accountable for. The fix is targeted verification on the actual risk points (dated SKUs, look-alike items, quantity-sensitive lines), not blanket re-checking.
- **Reading a valid pick as proof a lift is safe** — a lift that "felt fine" today can still carry a Lifting Index above 1.0 and be one of hundreds of reps that add up to a cumulative-strain injury.

## Worked example

**Situation.** A grocery DC order filler is working an 8-hour shift against a facility pace goal of 110 lines/hour at a ≥99.5% line-accuracy floor. The current order (#48211) is a 40-line batch; line 22 calls for 6 cases of a dated dairy SKU from location D-14. At the time of this pick the filler has completed 38 lines in 24 minutes — 95 lines/hour, behind pace — with 362 lines remaining in the shift.

**Naive read.** Behind on rate with 362 lines to go: grab the 6 dairy cases from whichever part of D-14 is easiest to reach, and skip scan confirmation on straightforward lines for the rest of the shift to claw back time.

**Expert reasoning — FEFO first.** D-14 holds two lots: Lot 114 (packed 8/12, best-by 9/26), 4 cases remaining, slotted at the more awkward top shelf; Lot 118 (packed 8/20, best-by 10/4), 10 cases, slotted at easy reach height. The WMS pick task specifies SKU and quantity but not lot — a real gap, flagged for the lot-tracking backlog rather than silently worked around. FEFO calls for exhausting Lot 114 first: pull all 4 from Lot 114, then 2 from Lot 118, filling the 6-case requirement while clearing the soonest-expiring stock. Taking all 6 from the easier Lot 118 (the naive move) leaves 4 cases of Lot 114 sitting until someone notices near its 9/26 date — at 24 units/case and $2.10/unit wholesale, a 4-case, 96-unit lot marked down 50% at expiry risk is a $100.80 write-off (96 × $2.10 × 0.50) traceable to nobody, for zero time saved, since picking FEFO takes the same handling time as picking by reach.

**Expert reasoning — hold the scan line.** Skipping scan confirmation on the remaining 362 lines saves roughly 3 seconds per line: 362 × 3 sec = 1,086 sec ≈ 18.1 minutes, worth about $5.40 in labor time at an $18/hr rate. The facility's own QA data shows scan-compliant picking averaging 99.7% line accuracy versus 97.5% on override/skip-scan picks. Applied to the 362 remaining lines: at 99.7%, expected errors ≈ 362 × 0.3% ≈ 1; at 97.5%, expected errors ≈ 362 × 2.5% ≈ 9 — a difference of roughly 8 extra errors. Using the standard prevent-catch-ship cost escalation heuristic (roughly $1 to prevent at pick, $10 to catch at packing, $100 once it ships as a customer-facing error, including return freight, reship, and CS handling), 8 extra shipped errors risk roughly $800 in downstream cost to save $5.40 of pick time — about 148x the saved value. The correct move is to hold scan compliance and flag the pace gap to the lead instead of trading accuracy for speed.

**Resolution — exception log, as filed:**

> Order 48211, Line 22 (SKU 88410-Y, dairy 4-pack case).
> Bin D-14: Lot 114 (pack 8/12, best-by 9/26) qty 4 remaining; Lot 118 (pack 8/20, best-by 10/4) qty 10.
> Picked 4 from Lot 114 + 2 from Lot 118 per FEFO — WMS pick task does not enforce lot selection; flagging for lot-tracking gap.
> Scan-confirmed all 6 units individually; held scan compliance for remainder of shift despite pace deficit (95 lines/hr vs. 110 target at time of this pick).
> Rate note: cannot hold 110 lines/hr and 99.5% accuracy simultaneously at current staffing in this zone — requesting a second picker be routed to zone 3 rather than accepting the accuracy tradeoff.
> Logged by: [picker]. Shift lead notified: [initials].

The naive read treated the rate deficit as something to solve by cutting a corner on this pick; the expert read treated it as a staffing question to escalate, because the corner being cut wasn't free — it had a specific, quantifiable downstream cost that dwarfed the time it saved.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running a NIOSH lifting-index check, verifying a slotting/pick-path decision, or executing a FEFO pull step by step.
- [references/red-flags.md](references/red-flags.md) — load when reviewing a shift, a zone, or a picker's trend data for smell tests before an error or injury happens.
- [references/vocabulary.md](references/vocabulary.md) — load when a term (slotting, golden zone, FEFO, lifting index) needs a precise, misuse-aware definition.

## Sources

- Waters, T.R., Putz-Anderson, V., Garg, A. — *Applications Manual for the Revised NIOSH Lifting Equation*, NIOSH Publication No. 94-110 (1994) — RWL formula, the six task multipliers, and the Lifting Index thresholds (LI > 1.0 elevated risk, LI > 3.0 high risk) used throughout.
- Edward Frazelle, *World-Class Warehousing and Material Handling* (McGraw-Hill) — velocity-based/ABC slotting, cube-per-order index, and the golden-zone placement principle.
- James A. Tompkins et al., *Facilities Planning* (Wiley) — warehouse layout and slotting fundamentals underlying pick-path sequencing.
- Warehousing Education and Research Council (WERC), annual *DC Measures* benchmarking report — pick-rate (lines/hour) and pick-accuracy benchmarks across paper, RF, voice, and pick-to-light methods.
- FDA Food Code (2022 edition) — date-marking and stock-rotation requirements for time/temperature-control-for-safety foods, basis for the FIFO/FEFO distinction; GS1 US lot and date-coding standards for how lot/date codes are structured in practice.
- The "prevent-catch-ship" cost-escalation heuristic (a version of the cost-of-quality "1-10-100 rule" popularized in quality-management literature, e.g., Labovitz & Chang) — applied here as a stated heuristic for the pick-vs-ship error-cost comparison, not a facility-specific measured figure.
- Bureau of Labor Statistics, Survey of Occupational Injuries and Illnesses, warehousing (NAICS 493) sector data — basis for musculoskeletal-disorder/overexertion injuries being a leading injury category in high-volume manual order filling.
- No direct stocker/order-filler practitioner has reviewed this file yet — flag corrections or gaps via PR.
