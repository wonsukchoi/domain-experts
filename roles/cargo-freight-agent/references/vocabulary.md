# Cargo and Freight Agent — Vocabulary

### Dimensional weight (DIM weight)
A billing weight calculated from a shipment's cubic dimensions divided by a carrier-specific divisor, used when a shipment is bulky relative to its actual weight.
**In use:** "The pallet only weighs 380 pounds on the scale, but at these dimensions the DIM weight comes out to 694 — that's what gets billed."
**Common misuse:** Assuming actual (scale) weight always applies; generalists often quote off actual weight without checking whether DIM weight is higher.

### NMFC class (National Motor Freight Classification)
A standardized freight-classification system for LTL (less-than-truckload) shipping, driven primarily by density, with handling, stowability, and liability as secondary factors.
**In use:** "At 5.7 pounds per cubic foot, this lands around class 175 — that's a bulky-freight rate, not the baseline rate."
**Common misuse:** Treating "class" as a fixed property of a commodity type rather than a density-driven calculation that changes with how the freight is packaged.

### Freight density
Weight divided by cubic volume (typically expressed in pounds per cubic foot), the primary input to NMFC classification.
**In use:** "Recalculate the density — if it's packed tighter this time, the class and rate will come down."
**Common misuse:** Confusing density with weight alone; two shipments of identical weight can have very different densities (and classes) depending on volume.

### Bill of lading (BOL)
The legal contract of carriage between shipper and carrier, documenting piece count, weight, class, special instructions, and declared value.
**In use:** "The BOL has to match what we actually verified — if the class on it doesn't match the shipment's real density, that's a liability problem, not just a paperwork one."
**Common misuse:** Treating the BOL as a shipping label or internal reference document rather than the legal document that governs carrier liability.

### Reweigh and reclass
A carrier's post-pickup verification of a shipment's actual weight and freight class, which can trigger a billing adjustment (usually upward) if the original BOL was inaccurate.
**In use:** "If we don't verify the density before booking, expect a reweigh-and-reclass adjustment on the invoice."
**Common misuse:** Assuming the originally quoted class/weight is final once the shipment ships; carriers routinely re-verify and rebill.

### Declared value
The value a shipper states for a shipment on the BOL, which caps the carrier's maximum liability in the event of loss or damage — separate from and often lower than the commodity's actual replacement value.
**In use:** "The declared value is what caps any claim payout — if it's set too low, the shipper can't recover full replacement cost even with a clean claim."
**Common misuse:** Assuming declared value is a formality rather than a hard ceiling on claim recovery; assuming it equals actual/replacement value by default.

### Carmack Amendment
The federal law (49 U.S.C. § 14706) governing carrier liability for loss or damage to cargo in interstate U.S. domestic surface transportation.
**In use:** "For this domestic LTL shipment, Carmack sets the liability framework and the claim-filing window."
**Common misuse:** Applying Carmack's framework to international air or ocean shipments, which are governed by different liability regimes (Montreal Convention, Hague-Visby/COGSA respectively).

### Concealed damage
Damage to freight discovered after delivery and unpacking, not visible or noted at the time of delivery — subject to different (often shorter and stricter) claim-reporting requirements than visible damage.
**In use:** "This is concealed damage — the box looked fine at delivery, so we need to move fast on documentation before the carrier's reporting window closes."
**Common misuse:** Treating all damage claims identically regardless of whether the damage was visible at delivery or discovered later; concealed-damage claims face a higher evidentiary bar.

### HS code (Harmonized System code)
An internationally standardized numerical classification for traded products, used by customs authorities to determine duties, taxes, and import restrictions.
**In use:** "We need the correct HS code before this ships internationally, or it'll get held at customs."
**Common misuse:** Using a generic or approximate HS code instead of the commodity-specific one; an incorrect code can trigger customs delays or duty reassessment even if unintentional.

### Freight class rate multiplier
The relative rate difference between freight classes, reflecting that lower-density (higher-class-number) freight costs more per pound to ship than higher-density (lower-class-number) freight.
**In use:** "Class 175 freight prices out at roughly 1.2 to 1.5 times the baseline rate — that's why the bulky shipment costs more per pound than the dense one."
**Common misuse:** Assuming freight rate scales only with total weight, ignoring that class (density) materially changes the per-pound rate.

### Minimum connection time (MCT) — cargo/interline context
The minimum time required between connecting carriers or modes for a shipment to be reliably transferred without missing the connection; distinct from the passenger-travel MCT concept but analogous in function.
**In use:** "The interline connection between the trucking leg and the air leg needs at least the carrier's published MCT, or we should build in buffer."
**Common misuse:** Assuming a tight connection window shown as "technically possible" in a routing system is operationally reliable without buffer.

### Exception notation
A written note on a delivery receipt, made at the time of delivery, documenting visible damage, shortage, or other irregularity — the single strongest piece of evidence in a subsequent cargo claim.
**In use:** "Get an exception notation on the delivery receipt before the driver leaves — without it, this claim is much harder to win."
**Common misuse:** Treating a verbal complaint to the driver as equivalent to a written exception notation; only the written, signed notation carries evidentiary weight.
