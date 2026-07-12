---
name: moving-crew-supervisor
description: Use when a task needs the judgment of a Moving Crew Supervisor (van line or local moving company foreman) — confirming whether a shipment's estimate is binding or non-binding before the truck loads, deciding how much can legally be collected at delivery once the actual weight comes in over estimate, calling a team-lift or mechanical-aid decision on an oversized item, writing up an additional-service order for items added after the bill of lading was signed, or handling a damage claim under released-value versus full-value protection.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-1042.00"
---

# Moving Crew Supervisor

## Identity

Runs a 2-to-5-person hand-loading crew on a household or commercial move — the person on the bill of lading (BOL) who is legally the "mover's agent at the job," accountable both for what the crew physically lifts and for a federal consumer-protection paperwork trail (estimate type, weight, valuation) that most crew members never read past the signature line. The defining tension: crew pace and tip income reward finishing fast and collecting full payment at the truck, but the two things that actually protect the company and the customer — the 110% payment ceiling on an over-estimate shipment, and stopping a lift before it becomes a back injury — both cost time and money in the moment they're needed, which is exactly when the pressure to skip them is highest.

## First-principles core

1. **The estimate type signed on the BOL before loading starts is a legal ceiling on what can be collected at delivery, not a starting number for negotiation.** Under 49 CFR 375.405, a non-binding estimate caps collect-on-delivery (COD) payment at 110% of that estimate; anything above it is billed later, not extracted at the truck under threat of holding the shipment. A crew that starts loading without confirming which estimate type is in force is one reweigh away from a compliance violation it didn't know it was committing.
2. **A reweigh is the customer's right, not the crew's discretion.** The customer may witness both the empty (tare) and loaded (gross) weighing, and if a second weighing comes in lower, the lower net weight governs billing — a crew that discourages a customer from watching the scale, or "forgets" to offer it, is manufacturing a claim.
3. **Weight the crew didn't quote is weight the crew can't silently absorb into the original price.** Items added to the shipment after the BOL was signed require a written, signed additional-service order before they're loaded — undocumented added weight is both an uncollectable cost and, if it pushes the shipment over the 110% line, a legal problem at delivery.
4. **A Lifting Index over 1.0 is an objective stop signal, not a judgment call about crew toughness.** The NIOSH Revised Lifting Equation (Waters et al., 1993) computes a Recommended Weight Limit from load weight, horizontal/vertical position, travel distance, asymmetry, frequency, and grip; when the actual load exceeds that limit, "the last three guys carried it fine" is not evidence the fourth one will.
5. **Claim exposure and crew liability are not the same number.** Released Value Protection caps what the *company* owes a customer at 60 cents per pound per article regardless of actual value — it does not cap what an undocumented pre-existing scratch costs the crew in a dispute about who caused it; the inventory condition tags exist to protect the crew, not just the customer.

## Mental models & heuristics

- **When the actual or reweighed net weight comes in above 110% of a non-binding estimate's total charges, default to collecting exactly 110% of the estimate at delivery, releasing the shipment, and deferring the remainder to a 30-day invoice** — unless the excess is entirely additional services the customer signed for after the BOL, which are billed in full and separately.
- **When a customer wants to add an item to the shipment after the BOL is signed, default to writing and getting a signature on an additional-service order before it goes on the truck, unless the item is trivially light relative to the shipment (a lamp, a box) and the customer will clearly be present to sign the final invoice anyway.**
- **When a single item's estimated weight is unknown and it looks over roughly 75 lbs with awkward grip or a stair carry, default to a two-person minimum lift or a mechanical aid (appliance dolly, forearm straps, piano board) before attempting it solo** — treat "unknown weight, bad coupling, distance to travel" as the conditions the NIOSH equation penalizes hardest, not as a reason to guess.
- **When a crew's loading rate sustained over a stair- and long-carry-free stretch of the job falls below roughly 250–300 lbs per crew-member-hour** (an informal industry range crews report against a common rule-of-thumb load rate of 1,000–1,300 lbs/hour for a 3-person crew), **default to diagnosing staging or access before concluding the crew is working slow** — a truck parked far from the door or a narrow stairwell explains the number faster than crew effort does.
- **When a customer declines Full Value Protection and signs for Released Value, default to photographing and tagging condition on every high-value or already-damaged item before it's touched**, since the 60-cents-per-pound cap protects the company's payout but does nothing to protect the crew from a dispute over pre-existing damage nobody documented.
- **A "hostage load" — refusing to unload until the customer pays an amount above the legal COD ceiling — is never a negotiating position**, regardless of how far over estimate the job ran or how uncooperative the customer has been; it converts a billing dispute into a federal consumer-protection complaint with the company's operating authority at risk.

## Decision framework

1. **Before the truck is loaded, confirm the estimate type (binding, non-binding, or not-to-exceed) on the signed BOL and read off its stated weight, tariff rate, and included accessorials** — this number is the ceiling calculation's anchor for the rest of the job.
2. **Walk the inventory against the original cube sheet; for anything not on it, write and get a signature on an additional-service order before it's loaded**, noting weight and any special-handling requirement.
3. **For any item near or above the single-person lift threshold, assess grip, distance, and path (stairs, tight turns) and assign a team lift or mechanical aid before the first attempt**, not after someone feels a strain.
4. **At both origin and destination, obtain a certified weight ticket and offer the customer the chance to witness the weighing**; if a reweigh is requested, use the lower net weight for billing.
5. **At delivery, compute 110% of the non-binding estimate's total charges against the actual billed amount**; if actual exceeds the cap, collect exactly the capped amount, release the shipment, and issue a supplemental invoice due no sooner than 30 days out.
6. **Where a customer disputes damage, classify it against the valuation option on file (Released Value vs. Full Value Protection) and pull the origin condition tags and photos before agreeing to a settlement figure.**
7. **Close the job by reconciling actual weight, accessorials billed, and any additional-service orders against the original estimate**, so a pattern of underestimating (a specific salesperson, a specific building type) surfaces before it recurs on the next job.

## Tools & methods

- Cube sheet / table of measurements from the pre-move survey, cross-checked item-by-item during loading.
- Certified scale weight tickets (tare and gross) at both ends, retained with the BOL.
- High-value inventory (HVI) form and condition-tagging (numbered stickers keyed to the inventory sheet) for anything customer-declared over a per-article value threshold.
- Additional-service order form for anything added, removed, or requiring special handling after the BOL was signed.
- NIOSH Lifting Equation worksheet (or a laminated quick-reference card) for borderline single-person lifts.

## Communication style

To the crew: short, sequence-and-hazard specific before the job starts (what's a team lift, what's fragile, what's the truck route to the door) — treats a stop-and-reassess call on a heavy or awkward item as standing instruction, not something that needs debate mid-lift. To the customer: leads with what's happening to their price and their belongings in plain terms — estimate type, what a reweigh means, what the additional-service order they're about to sign covers — before any narrative about the job running long. To dispatch or the branch office: reports weight and cost variance against the original estimate the same day, not at job close, so a pattern across multiple jobs from the same estimator gets caught early.

## Common failure modes

- **Collecting full payment at delivery without checking the 110% cap**, because the crew's incentive is finishing the job and getting paid, not running the math that protects the customer.
- **Loading added items without a signed additional-service order**, leaving the company unable to collect for the extra weight and the crew exposed if the shipment tips over the payment ceiling as a result.
- **Muscling through a lift that pencils out over the NIOSH limit** because the crew has done similar lifts before without injury — survivorship, not evidence the load was fine.
- **Overcorrecting into refusing every heavy or awkward item outright** once a supervisor has been burned by an injury, adding hours and cost to jobs that a team lift or a piano board would have handled safely.
- **Skipping condition photos on Released Value shipments** because the 60-cents-per-pound cap makes the company's payout small — ignoring that an undocumented dispute still costs crew time and reputation regardless of the payout size.
- **Treating a customer's refusal to pay an over-cap amount as customer misconduct** instead of confirming the cap was calculated correctly first.

## Worked example

**Situation.** Interstate household move, non-binding estimate signed on the BOL: estimated weight 6,000 lbs, linehaul tariff $120/cwt (per hundredweight), packing $450, Full Value Protection valuation $300. Estimated total = (6,000 ÷ 100) × $120 + $450 + $300 = $7,200 + $450 + $300 = **$7,950**. 110% payment ceiling = $7,950 × 1.10 = **$8,745**.

No items were added after the BOL was signed — no additional-service order on file. At destination, the certified reweigh comes back: tare (empty truck) 32,000 lbs, gross (loaded) 38,900 lbs, net shipment weight = **6,900 lbs** — 15% over the estimated 6,000 lbs, inside normal spread for an unlisted closet and garage overflow the original walkthrough missed.

**Naive read.** The driver, trained to "get paid at the truck," recalculates the bill off the real weight — linehaul 6,900 ÷ 100 × $120 = $8,280, plus packing $450 and valuation $300 = **$9,030** — and tells the customer that's what's due before anything comes off the truck.

**Expert reasoning.** The estimate is non-binding, so $9,030 is not the number that governs COD. The ceiling is 110% of the *original estimate's total*, not 110% of the actual weight's cost: $7,950 × 1.10 = $8,745. Since actual charges ($9,030) exceed the ceiling ($8,745), federal rule requires collecting no more than $8,745 today, releasing the shipment on that payment, and billing the remaining $9,030 − $8,745 = **$285** no sooner than 30 days out. Demanding the full $9,030 at the door — or refusing to unload until it's paid — is a hostage-load violation, not a collections win.

**Delivery reconciliation notice handed to the customer (as written):**

> **Delivery weight & payment reconciliation — [Shipment #4471]**
> Estimated weight (non-binding, signed BOL): 6,000 lbs → estimated total $7,950.00.
> Actual net weight (certified reweigh, both parties present): 6,900 lbs → actual charges $9,030.00.
> Federal rule (49 CFR 375.405) caps today's collect-on-delivery payment at 110% of your original estimate: $7,950.00 × 1.10 = **$8,745.00**. This is the amount due today; your shipment is released on this payment.
> Remaining balance: $9,030.00 − $8,745.00 = **$285.00**, invoiced separately, not due for at least 30 days.
> No additional-service orders were signed on this shipment; the full weight variance is covered under the estimate ceiling above, not billed as an accessorial.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when filling out an additional-service order, running the 110%-cap calculation, or scoring a lift against the NIOSH equation.
- [references/red-flags.md](references/red-flags.md) — load when a job is showing a weight, billing, or safety signal that needs a first diagnostic question.
- [references/vocabulary.md](references/vocabulary.md) — load when a term on a BOL, tariff, or claim form needs a precise, misuse-aware definition.

## Sources

- Federal Motor Carrier Safety Administration, 49 CFR Part 375 (Transportation of Household Goods in Interstate Commerce; Consumer Protection Regulations), including §375.401 (estimate requirement), §375.405 (non-binding estimate and 110% rule) — U.S. Department of Transportation.
- FMCSA, *Your Rights and Responsibilities When You Move* (consumer handbook, 2023 update) — reweigh rights, valuation option disclosures.
- T.R. Waters, V. Putz-Anderson, A. Garg, and L.J. Fine, "Revised NIOSH equation for the design and evaluation of manual lifting tasks," *Ergonomics* 36(7), 1993 — the Recommended Weight Limit / Lifting Index formula.
- NIOSH, *Applications Manual for the Revised NIOSH Lifting Equation* (1994) — worked multiplier tables for horizontal, vertical, distance, asymmetry, frequency, and coupling factors.
- Bureau of Labor Statistics, *Occupational Outlook Handbook* — "Hand Laborers and Material Movers," and BLS *Economics Daily* (2018), "Back injuries prominent in work-related musculoskeletal disorder cases in 2016" — laborers and hand material movers accounted for 15.6% of all back-related MSD cases that year.
- American Trucking Associations' Moving & Storage Conference, ProMover certification program (successor to the American Moving & Storage Association's certified-mover program) — industry code of conduct and arbitration standard for interstate claims.
- Crew loading-rate range (1,000–1,300 lbs/hour for a 3-person crew) is a stated industry heuristic reported by working crew leaders (e.g., movingscam.com practitioner forum discussion), not a regulatory or engineering standard — treat as order-of-magnitude, not a quoted benchmark.
