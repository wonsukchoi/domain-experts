# Red Flags

Smell tests a logistician catches before they become service failures or budget surprises.

### Reorder-point stockouts on the SKUs with the shortest, most reliable lead times
- **Usually means:** the ROP was set once from a stale average demand figure and never recalculated after a demand step-change, rather than a lead-time problem — a short, reliable lead time makes lead-time variance an unlikely cause.
- **First question:** "When was σ_d for this SKU-location last recalculated, and does the current mean demand still match the number the ROP was built from?"
- **Data to pull:** SKU-location demand history for the last 8–13 weeks vs. the window the current ROP was calculated from; date of last ROP update.

### Freight cost per unit rising while average shipment size shrinks
- **Usually means:** mode fragmentation — orders drifting toward more frequent, smaller LTL shipments instead of consolidated truckload, often because a service-level fix ("ship it now") became the default rather than the exception.
- **First question:** "What share of shipments on this lane are below truckload minimum weight, and has that share grown in the last two quarters?"
- **Data to pull:** shipment-size distribution by lane over 6 months; TMS mode-mix report.

### Safety stock expressed as a flat number of weeks across an entire category
- **Usually means:** the buffer was set by policy or convention rather than computed from σ_d/σ_L, which produces stockouts on high-variability items and dead stock on low-variability ones inside the same "2 weeks for everything" category.
- **First question:** "What's the demand CV spread within this category, and does one flat-weeks number make sense across that spread?"
- **Data to pull:** per-SKU demand CV within the category; current safety stock as computed vs. as held.

### Order quantities exactly matching supplier MOQ across many SKUs
- **Usually means:** ordering is being driven by the supplier's minimum, not by the EOQ/demand math — often fine for low-value C items, a red flag if it shows up on A items where MOQ well exceeds the calculated optimal order quantity.
- **First question:** "For the A-item SKUs ordering at MOQ, how far is MOQ above the calculated EOQ, and has anyone renegotiated it?"
- **Data to pull:** EOQ vs. MOQ vs. actual order quantity, by SKU, for the top-value decile.

### A DC's order variance to its supplier is much larger than the sell-through variance it's covering
- **Usually means:** bullwhip amplification — batching, forward-buying ahead of a price change, or reacting to the immediate downstream order rather than true demand.
- **First question:** "What's the CV of this DC's orders to its supplier versus the CV of the sell-through data it's meant to track?"
- **Data to pull:** order-quantity time series to the upstream supplier vs. POS/sell-through series for the same product, same window.

### High fill rate maintained alongside rising expedited-freight spend
- **Usually means:** the planning process is broken and premium freight is quietly paying for it — a fill-rate metric that looks healthy is masking a reorder point set too low or a forecast that's drifted, with air/expedite covering the gap.
- **First question:** "What fraction of this quarter's on-time fill rate depended on an expedited shipment that wasn't in the original plan?"
- **Data to pull:** expedited-freight spend and shipment count by SKU-location, trended quarter over quarter, cross-referenced against planned vs. actual mode.

### Chronic partial shipments or backorders concentrated on one lane or node
- **Usually means:** a genuine capacity constraint at that specific node or lane (dock capacity, carrier capacity, a single-source supplier's plant limit) rather than a network-wide shortage — adding capacity elsewhere won't fix it.
- **First question:** "Is this the actual bottleneck, or does fixing it just move the constraint to the next node downstream?"
- **Data to pull:** fill rate and backorder count by node/lane, not aggregated network-wide; throughput vs. capacity at the suspected constraint.

### Forecast error (MAPE) tracked only at an aggregated level, never SKU-location
- **Usually means:** nobody can actually tell which specific reorder points need updating — an aggregate MAPE of 12% can hide individual SKU-locations at 60% error offset by others near zero.
- **First question:** "Can you show me MAPE by SKU-location for the items driving the last three stockouts?"
- **Data to pull:** forecast-vs-actual at SKU-location grain for the period in question.

### Inventory turns and service level both declining in the same period
- **Usually means:** more inventory is being held (turns down) while it's the wrong inventory in the wrong place (service level also down) — usually a demand-mix shift or SKU proliferation the network hasn't adjusted to, not a simple "add more stock" fix.
- **First question:** "Is the excess inventory concentrated in different SKU-locations than the stockouts, or the same ones?"
- **Data to pull:** inventory-by-SKU-location vs. stockout-by-SKU-location for the same period, sorted to see if they overlap or diverge.

### A network-design or DC-count study justified on freight savings alone
- **Usually means:** the analysis is answering a cost question when the actual driver is a service-level commitment (same-day/next-day) that a pure cost model doesn't price — the NPV can come back negative and still be the wrong basis for the decision.
- **First question:** "Is there a service-level requirement this node exists to hit that isn't in the freight-savings number?"
- **Data to pull:** committed service-level SLAs by region alongside the freight/carrying cost model.
