# Cargo and Freight Agent — Red Flags

### Shipper-stated weight with no dimensions provided
- **Usually means:** the shipper hasn't measured the shipment, or is quoting a rough estimate that won't hold up against DIM-weight billing.
- **First question:** "Can you give me the exact dimensions, or should we schedule a measurement at pickup?"
- **Data to pull:** carrier's DIM divisor for the intended mode; a comparison of estimated actual weight vs. calculated DIM weight once dimensions arrive.

### Actual weight and DIM weight differ by more than ~20%
- **Usually means:** the shipment is unusually bulky (light/foamy/loosely packed) or unusually dense (compact machinery, liquids) relative to typical freight in its category.
- **First question:** "Is this commodity typically this light/heavy for its size, or could the dimensions or weight be off?"
- **Data to pull:** physical re-measurement if the discrepancy seems out of line with the stated commodity.

### Commodity description is generic ("parts," "supplies," "equipment")
- **Usually means:** the freight class hasn't been properly determined and is at risk of being reweighed/reclassed by the carrier after pickup, generating a surprise invoice adjustment.
- **First question:** "Do you have an NMFC item number for this, or can we calculate density from the actual dimensions and weight?"
- **Data to pull:** density calculation; carrier's reweigh-and-reclass fee schedule to show the shipper the cost of an unresolved classification.

### Shipper insists on the fastest mode without stating a hard deadline
- **Usually means:** either a genuinely urgent need, or a default assumption that faster is always better without weighing the cost.
- **First question:** "What happens if this arrives two days later than the fastest option — is there a real cost to that, or is faster just preferred?"
- **Data to pull:** cost delta between mode options, presented explicitly so the shipper is choosing with the number in front of them.

### International shipment with no HS code provided
- **Usually means:** the shipper hasn't classified the commodity for customs, risking a hold at the border or a duty reassessment.
- **First question:** "Has this commodity been classified under the Harmonized System before, or do we need to determine the HS code now?"
- **Data to pull:** HS code lookup; destination-country import restrictions for that code, if unfamiliar.

### Declared value seems low relative to the commodity described
- **Usually means:** the shipper is minimizing declared value to reduce insurance cost, without realizing it caps claim recovery.
- **First question:** "This declared value would cap any claim payout at that amount even if the actual replacement cost is higher — is that the value you want on record?"
- **Data to pull:** shipper's actual invoice/replacement-cost value for the commodity, for comparison.

### Damage claim reported more than 48 hours after delivery
- **Usually means:** either the damage was genuinely discovered late (concealed damage inside packaging), or the delivery-receipt exception step was skipped and the consignee is now trying to document after the fact.
- **First question:** "Was any exception noted on the delivery receipt at the time of delivery, or signed clean?"
- **Data to pull:** signed delivery receipt; any photos or notes made at time of delivery vs. photos taken now.

### Delivery receipt signed "clean" (no exception noted) despite a damage claim
- **Usually means:** the carrier's liability defense will point to the clean signature as evidence the shipment arrived undamaged — this is the hardest claim posture to win.
- **First question:** "Is the damage the kind that would have been visible from the outside of the packaging, or could it plausibly have been concealed damage discovered on unpacking?"
- **Data to pull:** packaging photos, carrier's concealed-damage claim policy (some carriers apply a shorter reporting window for concealed vs. visible damage).

### Freight class on the BOL doesn't match the calculated density
- **Usually means:** either a classification error at booking, or the shipment's actual composition changed after the quote (different packaging, added items) without updating the paperwork.
- **First question:** "Has anything about the shipment's packaging or contents changed since we quoted it?"
- **Data to pull:** current density calculation from actual shipped dimensions/weight, compared to the class quoted.

### Repeat shipper consistently underestimates weight on intake calls
- **Usually means:** a pattern worth flagging proactively rather than catching shipment-by-shipment — either they're rounding down out of habit, or their internal process for weighing/measuring is unreliable.
- **First question:** "I've noticed the last few shipments came in heavier than initially reported — is there a way to get a scale weight before you call in?"
- **Data to pull:** history of quoted-vs-actual weight variance across that shipper's recent shipments.
