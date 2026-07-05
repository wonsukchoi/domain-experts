# Vocabulary

Terms generalists reliably misuse. Format: definition, practitioner usage, the common misuse.

### Cycle service level vs. fill rate
- **Definition:** cycle service level is the probability of not stocking out during a single replenishment cycle. Fill rate is the percentage of *units demanded* that ship from stock, across all cycles.
- **In use:** "We're quoting 97.5% cycle service level, which at this demand CV works out to roughly 98.5% fill rate — don't repeat the fill-rate number as if it were the service level we set the z-score against."
- **Common misuse:** using "95% service level" to mean either number interchangeably. They require different z-score/loss-function math and produce different safety-stock figures for the same target — quoting one while having calculated the other silently changes the buffer.

### Safety stock
- **Definition:** inventory held above expected demand during lead time, sized to absorb demand and lead-time variability at a target service level.
- **In use:** "Safety stock here is 221 units because lead-time CV is 33% — that's a supplier reliability number, not a demand number, so renegotiating delivery windows moves it more than any forecast improvement would."
- **Common misuse:** treating it as a flat percentage or weeks-of-supply add-on instead of a number derived from σ_d and σ_L. "Add 20% buffer" is a guess dressed as a policy.

### Reorder point (ROP) vs. order-up-to level (S)
- **Definition:** ROP is the inventory level that triggers a fixed-quantity order under continuous review. Order-up-to level is the target inventory position reached under periodic review, where the order quantity varies each cycle.
- **In use:** "This DC reviews on a weekly truck schedule, so we need the order-up-to formula with the review period folded into the variance term — using a plain ROP formula here understates the buffer by a full week of exposure."
- **Common misuse:** applying the continuous-review (Q, R) safety-stock formula to a system that actually reviews periodically, which omits the review-interval term and understates the buffer — the single most common sizing error in practice.

### Economic order quantity (EOQ)
- **Definition:** the order quantity minimizing the sum of ordering cost and holding cost, assuming a fixed cost per order and a constant demand rate: Q* = √(2DS/H).
- **In use:** "EOQ says 1,312 units, about four weeks of demand — consistent with the discrete total-cost comparison, but I'm trusting the discrete table over the formula because freight here is a truckload-flat-rate step function, not a fixed order cost."
- **Common misuse:** applying EOQ mechanically when the real ordering cost isn't fixed — LTL priced per cwt and TL priced per flat rate up to capacity both violate EOQ's core assumption, and the formula will quietly recommend an interval a real total-cost comparison would reject.

### Total landed cost
- **Definition:** the full cost of getting a unit to its point of use — freight, duties/customs where applicable, handling, and the carrying cost of the inventory the mode and cycle choice require — not the freight quote alone.
- **In use:** "The intermodal quote is 15% cheaper than truckload, but factor in the extra four days of transit variability and the safety stock it forces, and truckload is the lower landed cost."
- **Common misuse:** comparing modes or carriers on the freight rate line item only, which reliably favors slower or less reliable options that push cost into inventory carrying and stockout risk instead of the freight line.

### Bullwhip effect (as it applies to a node's own data)
- **Definition:** the amplification of demand variability moving upstream through a supply chain, driven by batching, order-timing, and each node reacting to the node immediately below it rather than to true end demand.
- **In use:** "Our order variance to the supplier is 2.4× the sell-through CV for this product family — before I size safety stock off our own order history, I need the sell-through series instead."
- **Common misuse:** treating a node's own order-to-supplier history as if it were a clean demand series for safety-stock math, quietly buffering against self-inflicted variance rather than real demand.

### NMFC freight class vs. weight (LTL pricing)
- **Definition:** LTL rates are driven primarily by NMFC class, which is set mostly by freight density (lb per cubic foot), handling difficulty, and value — weight alone is a secondary factor.
- **In use:** "This part is bulky and light — 4 lb/cubic foot — so it prices at class 125 regardless of the fact that the pallet only weighs 300 lb; repackaging to raise density to 6 lb/cubic foot would drop it to class 85 and cut the rate more than any carrier negotiation would."
- **Common misuse:** quoting or negotiating LTL rates by weight alone, missing that a density/class change is usually the larger lever.

### Center of gravity (network design)
- **Definition:** the demand-weighted geographic centroid of shipment volume, used as a starting candidate site for a new distribution node.
- **In use:** "The center-of-gravity centroid points near Atlanta, but that's a starting hypothesis — it still needs to be checked against actual carrier lane access, labor market, and inbound supplier proximity before it's a site recommendation."
- **Common misuse:** treating the centroid as the answer rather than a first candidate, and weighting it by customer count instead of shipment volume, which lets a handful of small, distant accounts distort the site recommendation.

### Coefficient of variation (CV)
- **Definition:** standard deviation divided by the mean — a scale-free measure of relative variability, used to compare variability across SKUs or lead times with very different average magnitudes.
- **In use:** "Absolute σ looks bigger for the high-volume SKU, but its CV is lower — it's actually the more predictable item once you normalize for its size."
- **Common misuse:** comparing raw standard deviations across SKUs of very different average demand and concluding the larger-σ item is "more variable," when its CV may be smaller.

### Demand sensing vs. demand planning
- **Definition:** demand planning produces a statistical forecast from historical demand over a medium-to-long horizon; demand sensing incorporates near-real-time signals (recent orders, POS, weather, short-term indicators) to adjust the near-term forecast.
- **In use:** "Base the safety stock and ROP on the demand-planning forecast's variance; use demand sensing only to trigger a short-term expedite decision, not to reset the standing safety-stock number."
- **Common misuse:** conflating the two and re-deriving standing inventory parameters (safety stock, ROP) from short-horizon sensing noise, which reacts to signals too short-lived to represent the variability the buffer needs to cover.

### Censored demand
- **Definition:** observed sales during a stockout period, which understate true demand because unfilled demand isn't recorded as a sale.
- **In use:** "Exclude the three weeks we were out of stock from the σ_d calculation — that data is censored, not evidence demand dropped."
- **Common misuse:** feeding raw sales history straight into a variance calculation without checking for stockout periods, which understates both mean demand and its variability and can recreate the very stockout it's meant to prevent.
