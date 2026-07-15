# Red flags — what a distribution manager notices instantly

Smell tests with thresholds. Any single one can be innocent; two or three together are a pattern.

### A service-level complaint met with a capacity investment at the most visible stage (usually last-mile delivery) without tracing the actual order flow
- **Usually means:** the real constraint may be upstream (warehouse processing, order intake) rather than the stage the complaint is most visibly associated with — investing at the wrong stage adds cost without improving throughput.
- **First question:** "Where is time actually being lost across the full order-to-delivery flow, not just at the stage the complaint points to?"
- **Data to pull:** time breakdown by stage (order processing, warehouse pick/pack, transit) over the relevant period, trend for each stage separately.

### A flat, uniform shipping/service-level policy applied across products with very different urgency and value
- **Usually means:** the network is likely overspending on speed for low-urgency goods while potentially underserving genuinely time-sensitive ones.
- **First question:** "Does this product's actual urgency and value justify its current shipping mode, or is it just the default policy?"
- **Data to pull:** shipping mode/cost by product category, actual urgency/time-sensitivity data for each category.

### Safety stock levels set by a flat percentage rule rather than calculated from actual demand and lead-time variability
- **Usually means:** some products are likely carrying unnecessary inventory cost while others face avoidable stockout risk, since a flat rule doesn't reflect each product's actual variability.
- **First question:** "Is this safety stock level calculated from this product's actual demand/lead-time variance, or is it a flat rule applied uniformly?"
- **Data to pull:** current safety stock levels and their basis, actual demand and lead-time variability data by product/location.

### A transportation mode decision based on freight cost alone, with no total landed cost comparison
- **Usually means:** a cheaper shipping mode with longer or less reliable transit time may cost more overall once carrying cost, stockout risk, and service-level impact are included.
- **First question:** "What's the total landed cost comparison, not just the freight quote, between these shipping mode options?"
- **Data to pull:** freight cost by mode, transit time and reliability data, inventory carrying cost and stockout risk implications for each option.

### Network capacity assessed only reactively, after a service-level metric has already visibly degraded
- **Usually means:** demand growth or a channel/pattern shift likely outpaced the network's designed capacity well before the strain became visible, and the gap was allowed to compound before being addressed.
- **First question:** "What does actual volume growth look like against the network's designed capacity over the recent period, checked proactively rather than only after a visible failure?"
- **Data to pull:** volume trend by node/lane versus designed capacity, timing of when the current strain likely began versus when it was first flagged.

### A service commitment made to sales/customers with no check against actual current network capacity
- **Usually means:** the commitment may exceed what the network can reliably support, producing a gap that surfaces as a customer-facing failure rather than a proactively managed internal constraint.
- **First question:** "Has this specific commitment been checked against current network capacity data, or was it made without that check?"
- **Data to pull:** the commitment as stated, current capacity data for the relevant node/lane it depends on.

### A capacity fix sized without checking it against the actual measured gap
- **Usually means:** the fix risks being oversized (wasting cost) or undersized (leaving the gap partially unresolved) relative to what's actually needed.
- **First question:** "What's the measured gap (e.g., orders/day short of capacity), and does the proposed fix's added capacity match it?"
- **Data to pull:** the specific measured capacity gap, the proposed fix's actual capacity addition.

### A cross-docking or flow-through strategy adopted without checking product/demand predictability actually supports it
- **Usually means:** the tighter coordination flow-through requires may not be reliably executable for this product/demand profile, risking service failures from insufficient buffer.
- **First question:** "Does this product's demand predictability and the operation's execution reliability actually support flow-through, or does it need the storage buffer a simpler model provides?"
- **Data to pull:** demand predictability data for the product in question, current execution reliability for flow-through operations already in place.
