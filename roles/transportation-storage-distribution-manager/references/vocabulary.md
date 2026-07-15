# Logistics and distribution working vocabulary

Terms a distribution manager uses precisely. Format: definition → how a practitioner says it → common misuse.

**Order-to-delivery flow breakdown** — Decomposing total fulfillment time into its component stages (order processing, warehouse pick/pack, transit/delivery), used to identify where time is actually being lost rather than assuming the most visible stage is the constraint.
In use: "The flow breakdown shows warehouse processing grew from 14 to 38 hours while delivery time is flat — that's where the problem actually is."
Misuse: diagnosing a service-level problem by looking only at the most visible or most complained-about stage (usually last-mile delivery) without tracing the full flow to find where time is actually accumulating.

**Bottleneck (network context)** — The specific node or lane in a distribution network with the least capacity relative to demand, which determines overall network throughput/reliability regardless of how much excess capacity exists elsewhere.
In use: "Warehouse pick/pack capacity, not delivery trucks, is the actual bottleneck here — that's where the 700 orders/day gap is."
Misuse: investing in capacity at a node or lane that isn't the actual constraint, producing added cost without a corresponding improvement in overall network throughput.

**Safety stock (statistically calculated)** — Buffer inventory sized from actual demand and lead-time variability (e.g., using standard deviation of both) for a specific product/location, as distinct from an arbitrary flat-percentage buffer rule applied uniformly.
In use: "This SKU's safety stock is calculated from its actual demand variance — it's higher than the flat 10% rule would suggest because this product's demand is genuinely more volatile."
Misuse: applying the same flat safety stock percentage across all products and locations regardless of their actual demand and lead-time variability, producing both unnecessary carrying cost on stable items and stockout risk on volatile ones.

**Total landed cost** — The full cost of a transportation mode decision, including freight cost, inventory carrying cost during transit, and stockout/service-level risk cost — as distinct from freight cost alone.
In use: "The cheaper ocean freight option has a lower quote, but total landed cost is higher once the longer transit time's carrying cost and stockout risk are included."
Misuse: selecting a shipping mode based on the freight quote alone, missing that a cheaper, slower, or less reliable mode can cost more overall once carrying cost and service risk are properly accounted for.

**Service-level segmentation** — Matching transportation mode/speed to a product's actual urgency and value category, rather than applying one shipping standard uniformly across products with very different time-sensitivity.
In use: "High-value, time-sensitive SKUs ship expedited; low-urgency commodity items ship standard ground — that's deliberate segmentation, not an inconsistency."
Misuse: applying a single shipping policy uniformly across all product categories regardless of actual urgency, overspending on speed for low-urgency goods while potentially underserving genuinely time-sensitive ones.

**Cross-docking / flow-through** — Moving inventory directly from inbound receiving to outbound shipping with minimal or no intermediate storage, reducing cost and handling time where product characteristics and demand predictability support it, but requiring tighter coordination than store-then-ship.
In use: "This SKU has predictable, high-velocity demand — a good candidate for flow-through, versus lower-velocity items that still need a storage buffer."
Misuse: adopting flow-through for a product with unpredictable demand or unreliable inbound timing, where the tighter coordination requirement isn't actually supportable, risking service failures from insufficient buffer.

**Network capacity planning** — Proactively checking a distribution network's designed capacity against forecasted demand growth and pattern shifts (new channels, seasonal peaks, geographic expansion), rather than only reacting once a service-level metric has already visibly degraded.
In use: "We ran capacity planning against the projected 40% holiday volume increase and found this regional warehouse would be under-capacity by week 3 of peak — addressed before it became a customer-facing failure."
Misuse: only assessing network capacity reactively after a service failure has already occurred, missing the window where the growing gap could have been addressed proactively and more cheaply.

**Carrier performance scorecard** — Ongoing tracking of a carrier's on-time delivery rate, damage rate, and cost, used in both selection and ongoing relationship management, as distinct from a one-time rate negotiation.
In use: "This carrier's on-time rate has dropped from 96% to 89% over the last quarter — that's a scorecard trigger for a performance conversation, not just a renewal-time consideration."
Misuse: evaluating carrier relationships primarily at contract renewal based on price alone, without ongoing performance tracking that would surface a developing service issue earlier.

**Right-sized capacity fix** — A capacity addition calculated to match the actual measured gap (e.g., orders/day short of throughput), as distinct from an oversized fix (wasting cost) or an undersized one (leaving the problem partially unresolved).
In use: "4 additional pickers closes the exact 700 orders/day gap — a full second shift would add double the capacity we actually need."
Misuse: sizing a capacity fix by an available option (a full shift, a standard truck order) rather than by the actual measured gap, producing either wasted spend or an incomplete fix.

**Demand and lead-time variability** — The statistical spread (commonly measured by standard deviation) in how much and how fast demand or replenishment lead time actually varies for a specific product/location, the correct input for calculating safety stock rather than a flat assumption.
In use: "This product's lead-time variability is much higher than our other SKUs from the same supplier — that's why its safety stock calculation comes out higher despite similar demand volume."
Misuse: assuming similar products or locations have similar variability without checking actual data, applying a safety stock level calibrated to the wrong variability assumption.
