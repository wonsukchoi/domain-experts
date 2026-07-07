# Vocabulary

Terms generalists conflate or oversimplify — practitioners keep them precise because pace, accuracy, and rotation decisions depend on it.

## ABC / velocity slotting

Classifying SKUs by pick frequency (A = fastest-moving, roughly top 20% of SKUs, B = mid-tier, C = slow-moving bulk) and assigning warehouse location accordingly — fast movers closest to pack/ship and in the easiest-to-reach positions.

**In use:** "This SKU moved from a C to an A last quarter — it needs to be re-slotted into the golden zone before peak, not left where it's been sitting for two years."

**Common misuse:** treating slot assignment as a one-time setup decision rather than something that needs re-running against current velocity data as demand shifts.

## Golden zone

The vertical height range (roughly waist to shoulder, ~20–59 inches) where reach and lift effort are lowest and the NIOSH vertical-location multiplier is closest to 1.0 (ideal near 30 inches / 75 cm off the floor). A-velocity SKUs are slotted here specifically because that's where the combined travel-and-reach cost per pick is minimized.

**In use:** "That's an A-item sitting on the bottom shelf — it belongs in the golden zone, not down where every pick costs an extra bend."

**Common misuse:** assuming "golden zone" just means "easy to see," rather than a specific height range tied to a measurable reach-effort and injury-risk reduction.

## FIFO vs. FEFO

**FIFO** (first-in, first-out) rotates stock by receiving order — physically front-most or earliest-received goes first. **FEFO** (first-expired, first-out) rotates by code date instead, which is what actually matters for perishable or dated goods; the two only coincide when receiving order and expiration order happen to match.

**In use:** "Don't pick FIFO on this — check the code dates, because the case that came in later this week has an earlier best-by than the one that's been sitting up front since last week."

**Common misuse:** treating "rotate the stock" as always meaning shelf position, when any dated SKU needs the code date checked, not just the position in the bin.

## Lifting Index (LI)

The ratio of an actual lift's weight to its NIOSH-calculated Recommended Weight Limit (RWL) for that specific task geometry. LI ≤ 1.0 is an acceptable lift for most healthy adults; LI between 1.0 and 3.0 is elevated risk; LI above 3.0 is high risk regardless of how manageable the weight feels.

**In use:** "That case only weighs 35 lbs, but at that shelf height and twist angle the LI comes out to 1.5 — it needs an aid, not just a strong back."

**Common misuse:** judging a lift's safety by the raw weight alone, ignoring that reach distance, height, twist, and repetition frequency can push a moderate weight into elevated-risk territory.

## Recommended Weight Limit (RWL)

The NIOSH-calculated maximum weight for a specific lifting task, computed as 51 lb (the load constant) multiplied by six task-specific multipliers (horizontal distance, vertical origin height, vertical travel distance, asymmetry/twist, lift frequency, and grip/coupling quality). It is a task-specific number, not a fixed weight ceiling.

**In use:** "The RWL for this bin's geometry is only 23 lbs even though the case weighs 35 — that's an elevated-LI lift before anyone touches it."

**Common misuse:** quoting "51 pounds" as a general safe-lifting ceiling, when 51 lb is only the unadjusted constant before any of the six task multipliers are applied.

## Pick path / batch picking / zone picking

The sequence a WMS generates for working a multi-line order (or a batch of orders) through the building in the shortest practical route, typically serpentining through zones rather than following raw location-number order. Batch picking groups multiple orders into one walk; zone picking assigns a picker to a fixed zone and passes the order along.

**In use:** "Work it in the sequence the handheld gives you — that path is already optimized across all four zones this order touches."

**Common misuse:** reordering picks back to bin-number order for "simplicity," which discards the travel-distance optimization the WMS already computed.

## Line accuracy vs. unit accuracy

**Line accuracy** measures whether each line on an order (SKU + expected quantity) was picked correctly; **unit accuracy** measures correctness at the individual-unit level within a line. A facility can report a high line-accuracy rate while masking unit-level quantity errors that don't rise to a full wrong-line miss.

**In use:** "Our line accuracy looks fine at 99.6%, but pull the unit-level data — that's where the case-count-short errors are hiding."

**Common misuse:** citing an accuracy percentage without specifying which measure it is, since line and unit accuracy can diverge meaningfully on high-quantity lines.

## Scan compliance

The rate at which a picker completes the required scan or voice confirmation step per pick, versus skipping or overriding it. It functions as a leading indicator of error rate, visible before any error actually ships.

**In use:** "Her scan compliance dropped to 91% this week — check her accuracy numbers before this shows up as a customer complaint."

**Common misuse:** treating a scan/voice step as a formality that can be skipped on "obvious" picks, when override rate is one of the few metrics that predicts an error before it happens.

## Cycle count

A scheduled, partial physical inventory count of specific locations (rather than a full facility count) used to catch discrepancies between system-expected and actual on-hand quantity early and continuously.

**In use:** "Log it as a cycle-count exception instead of just correcting the pick — that gap needs to show up in the count history, not disappear silently."

**Common misuse:** quietly adjusting a pick to match whatever's physically in the bin without logging the discrepancy, which erases the data a lead needs to spot a pattern.

## Lot / code date

**Lot** identifies a specific production/receiving batch of a SKU; **code date** (best-by, sell-by, or use-by) is the date printed on that lot governing rotation priority. Multiple lots of the same SKU can sit in the same bin with different code dates simultaneously.

**In use:** "Same SKU, two lots in that bin — check which code date is closer before you pick either one."

**Common misuse:** assuming one SKU location has one uniform date, when replenishment routinely mixes multiple lots with different code dates in the same slot.

## Shrink

Inventory loss that isn't explained by a recorded sale or shipment — from damage, theft, mis-pick, or administrative error. A cycle-count discrepancy is a symptom that could trace back to shrink, a slotting error, or a receiving error, and the three require different fixes.

**In use:** "Before we call this shrink, rule out a mis-slot — check if a different SKU got putaway into this location by mistake."

**Common misuse:** labeling every inventory discrepancy "shrink" by default, which skips the step of checking whether it's actually a correctable process error instead.
