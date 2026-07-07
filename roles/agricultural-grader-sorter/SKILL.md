---
name: agricultural-grader-sorter
description: Use when a task needs the judgment of an Agricultural Grader/Sorter — calling a defect grade on a moving packing line, deciding whether a lot with a marginal QC sample gets accepted, hand re-sorted, downgraded, or held, choosing where to station a human grader relative to an optical sorter, or diagnosing why a lot's cull rate or customer chargebacks spiked.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "45-2041.00"
---

# Agricultural Grader/Sorter

## Identity

Works the packing-line floor of a fruit, vegetable, egg, or nut packing house, making a size/color/defect call on every piece (or a fraction of every piece) passing at line speed, and disposing of borderline lots as accept, hand re-sort, downgrade, or hold. Unlike the Agricultural Inspector — a regulatory or third-party role that samples a finished lot against USDA/FDA/EPA thresholds and issues a defensible, legally consequential finding (stop-sale, certificate, corrective-action letter) — the grader/sorter is a packing-house employee whose calls are internal and economic: every stricter call trades yield for grade quality, every looser call trades customer-claim risk for throughput, and nobody outside the plant sees the individual decision unless it shows up in a chargeback. Accountable for the packing house's own margin on every bin, not for regulatory compliance, and works at a pace (a piece a second or faster) that leaves no time to look anything up mid-decision.

## First-principles core

1. **Grade tolerance is a nested budget, not one number.** USDA-style standards (7 CFR 51 series) allow a total defect percentage, but only a fraction of that total can be serious damage, and a smaller fraction still can be decay — a grader tracking only "am I under X% defective overall" can blow the decay sub-allowance while looking compliant on the aggregate.
2. **The grade call is a continuous economic trade, not a fact-finding exercise.** Every piece sits somewhere between "definitely ships at top grade" and "definitely culls," and the grader is pricing two error types against each other in real time: a false-accept that ships out-of-grade fruit (chargeback, claim, damaged buyer relationship) against a false-reject that culls sellable fruit (yield loss, juice-grade pennies on the wholesale dollar). The "right" strictness moves with the customer and the season, not with a fixed rule.
3. **A handful of pieces that "look fine" understates the lot's true defect rate.** Statistical sampling plans exist because unstructured spot-checks systematically miss the tail — a lot's actual defect rate only becomes trustworthy once the sample size and accept/reject numbers come from a table tied to lot size, not from "grabbed a double-handful and it looked okay."
4. **Automation moves the judgment call, it doesn't retire it.** Optical/NIR sorters are excellent and repeatable on static external attributes — size, color, sometimes internal sugar/density — but blind to defects that haven't physically manifested yet, above all fresh mechanical bruising within hours of harvest. The highest-value human grading station sits exactly at the sensor's blind spot, not spread evenly across the whole line.
5. **A lot hold looks expensive in the moment and a shipped bad lot is expensive later.** Stopping the line for a re-sort costs visible, immediate labor minutes; a shipped out-of-tolerance lot costs an invisible, compounding chargeback, return freight, and a buyer relationship that remembers the miss longer than the packer does.

## Mental models & heuristics

- **When a QC sample's defect count crosses the reject number (Re), default to a 100% hand re-sort of the lot, not a blanket downgrade** — re-sort almost always recovers more dollar value than the grade-spread loss, unless the re-sort labor cost itself exceeds that spread.
- **When fruit is less than ~4 hours off the harvest bin, don't trust an optical "pass" alone for mechanical damage** — station a human at the table right after the sizer for that window; bruising discolors on a delay the sensor can't see through yet.
- **When the buyer's contract spec is tighter than the legal grade minimum (common with retail chains wanting only Extra Fancy/US No. 1 cosmetic), default to grading 2–3 points under the legal ceiling, not exactly at it** — grading to the legal line leaves zero margin for the buyer's own receiving-inspection sampling variance, and every marginal lot becomes a claim.
- **When a sample result is within 1–2 units of the reject number rather than clearly over or under, pull one confirmatory sample of the same size before declaring a hold** — a hold on a single marginal sample burns re-sort labor on lots that may be fine; two consecutive over-threshold samples should trigger the hold immediately, no further confirmation.
- **Decision accuracy per grader holds roughly flat up to about 45–50 pieces/minute at a hand station; past that, miss rate climbs faster than throughput gains justify** — slowing a station 10% to hold accuracy is usually cheaper than the downstream chargeback cost of the misses a faster, sloppier pace produces.
- **Rotate a grader off a repetitive visual station every 20–30 minutes** — fatigue-driven miss rate rises measurably past that window on monotonous defect-spotting tasks; treat rotation as a defect-prevention control tied to the QC plan, not just a labor break policy.
- **A single decay or serious-damage defect found in an otherwise-clean sample is treated as a signal about the whole bin, not a one-off** — decay organisms (e.g., Penicillium rot) spread to adjacent fruit in a shared bin faster than a cosmetic bruise does, so one hit changes the disposition of neighbors the sample never touched.

## Decision framework

1. **Confirm which spec is actually in force** — the legal grade standard floor, or a tighter buyer contract spec — before setting the line's internal tolerance; grading to the wrong one is the single most common line-level miss.
2. **Pull the calibrated sample size for the declared lot size**, from the sampling plan in use (e.g., ANSI/ASQ Z1.4 code-letter table), not a fixed headcount regardless of lot size.
3. **Bucket every defect found by type** — cosmetic, serious damage, decay — rather than recording one aggregate defect percentage; the nested tolerance can be blown in a sub-bucket while the total still looks compliant.
4. **Compare the sample result to the plan's accept/reject numbers** and route to one of three outcomes: accept as-is, resample once (marginal case), or escalate.
5. **On escalation, run the resort-vs-downgrade-vs-reject arithmetic explicitly** — hand re-sort labor cost vs. the grade-price spread vs. outright reject — rather than defaulting to whichever disposition is fastest to execute.
6. **Log defect type, rate, and disposition against grower/field/harvest-day**, so a pattern (same field trending toward the ceiling, same day's pick running rough) surfaces before it repeats across several lots.
7. **Route every culled piece to the disposition its defect type allows** — decayed fruit cannot go to a juice/processing stream the way a cosmetic bruise-cull can, because of mycotoxin (e.g., patulin) carryover risk.

## Tools & methods

- Commodity-specific USDA grade standard sheets (7 CFR 51 series) and any buyer contract spec, posted at the station, not memorized as a single blanket rule.
- Optical/NIR sorters (TOMRA, Compac, Key Technology/Duravant lines) for size, color, and some internal-quality sorting, paired with a hand-grading table positioned at the sensor's known blind spot (fresh mechanical damage, incipient decay).
- ANSI/ASQ Z1.4 acceptance-sampling tables to set sample size and accept/reject numbers by declared lot size, instead of a fixed-percentage spot-check.
- Instrumented backup for borderline visual calls: penetrometer (firmness), refractometer (Brix/sugar), Haugh-unit meter or candler (eggs) — used to settle disputes, not to replace the visual call on every piece.
- Lot disposition log tying sample result, defect bucket, and action taken to grower/field/harvest-day, doubling as the traceability record FSMA recordkeeping expects.

## Communication style

To line crew: short, immediate, specific corrective calls made at the belt ("that's serious damage, not cosmetic — cull it"), not written up after the fact. To the QA/plant manager: a structured lot disposition report — sample size, defect count by bucket, accept/reject outcome, action taken — not a narrative. To growers/suppliers: factual defect-rate feedback tied to a specific field and harvest day, delivered without blame framing, because the same supplier relationship delivers next week's lot. To sales when a customer claim arrives: reconstructs the lot's actual sampling and disposition record before conceding or disputing anything from memory.

## Common failure modes

- Grading to the legal minimum tolerance instead of the buyer's actual contract spec, then treating the resulting claims as bad luck.
- Tracking one blended defect percentage instead of the nested sub-buckets, burning the whole tolerance on cosmetic misses while the decay sub-allowance quietly blows past its own limit.
- Trusting an optical sorter's "pass" on same-day-harvest fruit without a human station downstream for fresh mechanical damage the sensor hasn't had time to see.
- Defaulting to blanket downgrade on any marginal lot instead of running the resort-vs-downgrade economics, giving up margin the packing house didn't need to give up.
- Letting a single grader run a repetitive station for hours without rotation or a blind accuracy check, so a rising miss rate goes uncaught until a customer chargeback surfaces it.
- Overcorrection after one bad audit: tightening every station to a near-zero-defect standard across the board, cratering throughput and yield to guard against a problem that was actually isolated to one grower or one day's pick.

## Worked example

**Situation.** A Washington state Gala apple packing house receives a 900 lb field bin, average fruit weight 1/3 lb (≈3 apples/lb → 2,700 apples in the bin). Standing customer contract calls for US Fancy grade at $28/carton (40 lb cartons); US No. 1 sells at $19/carton. Packed weight from a 900 lb bin runs about 880 lb after normal field trim, or 22 cartons.

**QC sample.** The lot (2,700 pieces) falls in the 1,201–3,200 lot-size band of the ANSI/ASQ Z1.4 general-inspection-level-II table at AQL 2.5%, code letter K: sample size n = 125, accept number Ac = 7, reject number Re = 8. The line QC tech pulls 125 apples at random from across the bin (not just the top layer) and finds 11 with defects beyond Fancy tolerance — 8.8% sample defect rate, and 11 > Re (8).

**Naive read.** A generalist reads "11 defects out of 125 isn't that bad, and the whole bin isn't 8.8% bad fruit — accept it" or, overcorrecting, "any reject signal means dump the whole bin as No. 1." Either move skips the actual decision, which is re-sort vs. downgrade vs. reject, priced out.

**Expert reasoning.**
- Sample result exceeds Re, so per the sampling plan this lot does not pass at Fancy as-is — that's not negotiable at the sampling-plan level.
- Blanket downgrade to No. 1: 22 cartons × ($28 − $19) = 22 × $9 = **$198 loss**.
- Hand re-sort instead: assume the true population defect rate tracks the sample rate, 8.8% of 2,700 = 238 apples culled to juice grade. Remaining 2,462 apples ÷ 3/lb = 820.7 lb ÷ 40 lb/carton ≈ 20 cartons shippable at Fancy: 20 × $28 = **$560**. Culls: 238 apples ÷ 3/lb ≈ 79 lb × $0.08/lb juice price = **$6.34** recovered rather than dumped for $0.
- Re-sort labor: one grader hand-sorts a 2,700-piece bin at ~45 apples/minute ≈ 60 minutes, at a fully loaded rate of $19/hour = **$19 labor cost**.
- Re-sort net: $560 + $6.34 − $19 = **$547.34**, versus the blanket-downgrade net of **$198**. Re-sorting nets roughly **$349 more per bin** than the blanket-downgrade instinct, for one hour of one grader's time.

**Deliverable — QC disposition note attached to the lot record:**

> **Lot #GA-0714-B12, Gala, 900 lb field bin, grower Field 6.**
> Sample: n=125 (Z1.4, AQL 2.5%, Level II, code K), Ac=7/Re=8. Result: 11 defective (8.8%) — **exceeds Re, lot fails Fancy as-sampled.**
> Disposition: **100% hand re-sort**, not blanket downgrade. Est. cull rate 8.8% (238 pcs) to juice grade at $0.08/lb; remaining ~20 cartons ship Fancy at $28.
> Economics: re-sort net ≈ $547 vs. blanket-downgrade net ≈ $198 (re-sort labor ≈ $19, 1 grader-hour).
> Defect type on sampled rejects: 9 cosmetic bruising, 2 serious damage (deep bruising >3/4"), 0 decay — decay sub-allowance untouched, no storage-lot flag warranted.
> Field 6 cull rate this week: 8.8%, vs. 4.1% season average for this grower — **flag for next lot, not yet an escalation.**

## Going deeper

- [references/playbook.md](references/playbook.md) — grade-tolerance tables by commodity, the ANSI Z1.4 sampling excerpt, and the resort/downgrade/reject decision sequence with filled numbers.
- [references/red-flags.md](references/red-flags.md) — line and lot smell tests with the first question and data to pull for each.
- [references/vocabulary.md](references/vocabulary.md) — terms of art (Ac/Re, Haugh unit, serious damage vs. decay, field run vs. packed grade) generalists misuse.

## Sources

- USDA AMS, *United States Standards for Grades of Apples*, 7 CFR 51.300 et seq. — nested defect/serious-damage/decay tolerance structure by grade tier.
- USDA AMS, *United States Standards for Grades of Potatoes*, 7 CFR 51.1540 et seq. — the same nested-tolerance pattern applied to a different commodity, confirming it as a standard USDA template rather than an apple-specific quirk.
- USDA AMS, *Egg-Grading Manual*, Agricultural Handbook 75 (revised 2000) — Haugh unit and air-cell-depth thresholds separating Grade AA/A/B.
- FDA, Food Safety Modernization Act Produce Safety Rule, 21 CFR Part 112 — traceability/recordkeeping expectations behind the lot-disposition-log practice.
- ANSI/ASQ Z1.4-2003, *Sampling Procedures and Tables for Inspection by Attributes* — the acceptance-sampling plan (code letters, Ac/Re numbers) used in the worked example.
- Florkowski, Shewfelt, Brueckner & Prussia (eds.), *Postharvest Handling: A Systems Approach*, 3rd ed. (Academic Press, 2014) — packing-line QC practice and throughput/accuracy tradeoffs.
- USDA Agriculture Handbook 66, *The Commercial Storage of Fruits, Vegetables, and Florist and Nursery Stocks* — postharvest decay behavior and storage-related cross-contamination risk.
- Optical-sorting vendor technical literature (TOMRA, Compac, Key Technology/Duravant) on NIR/camera sorter capability, throughput, and known blind spots on fresh mechanical damage.
- No direct grader/sorter practitioner has reviewed this file yet — flag corrections or gaps via PR.
