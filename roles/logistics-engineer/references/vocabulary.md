### Center-of-gravity (weighted centroid) model
A facility location technique that calculates a demand-weighted geographic point minimizing aggregate distance to customer or supply locations, used as a starting search area rather than a final site.
**In use:** "Center-of-gravity analysis points us to a search area in the central Midwest — now we need to validate actual sites within it."
**Common misuse:** Treating the model's output coordinates as the final facility location decision without validating against real road distances, real estate, and infrastructure.

### Total landed cost (network design)
The full cost of a facility location or network configuration, including facility fixed cost, inbound and outbound freight, and inventory carrying cost — the actual basis for comparing network design options.
**In use:** "Total landed cost for the 2-DC option comes in at $12.2M, only marginally better than the 1-DC option's $12.4M."
**Common misuse:** Comparing network design options on freight cost alone, missing how facility fixed cost and inventory carrying cost move in the opposite direction.

### Risk pooling (inventory)
The statistical benefit of holding safety stock in a single consolidated location rather than split across multiple locations, since aggregate demand variability is proportionally lower than the sum of variability at each individual location.
**In use:** "Splitting inventory into two regional DCs loses the risk-pooling benefit, requiring more total safety stock to hit the same service level."
**Common misuse:** Assuming inventory carrying cost stays flat when splitting a single facility into multiple locations, without accounting for the additional safety stock the loss of pooling requires.

### ABC classification (velocity-based slotting)
A method of categorizing inventory items by pick frequency/velocity (A = fastest-moving, C = slowest), used to determine warehouse layout and slotting priority.
**In use:** "A-items are slotted closest to the pack station; C-items are placed in the back of the facility."
**Common misuse:** Slotting a warehouse alphabetically, by vendor, or by arrival order instead of by actual pick velocity data, adding unnecessary travel time to high-volume picks.

### Facility fixed cost
The costs of operating a distribution facility that don't vary directly with volume — rent/lease, base equipment, and fixed labor — which generally increase in aggregate as facility count increases.
**In use:** "Splitting into two DCs roughly doubles our fixed facility overhead, even though each facility is individually smaller."
**Common misuse:** Assuming fixed costs scale down proportionally when splitting one large facility into multiple smaller ones, ignoring the duplicated overhead each additional facility introduces.

### Peak-period capacity sizing
Sizing a facility, equipment, or labor plan against historical or projected peak demand (with a stated buffer), rather than average demand.
**In use:** "This facility's conveyor capacity is sized to handle 140% of peak holiday volume, not average daily volume."
**Common misuse:** Sizing capacity to average daily demand, leading to bottlenecks or costly overtime/temp labor during seasonal or promotional peaks.

### Service-level buffer
An additional margin built into a capacity or inventory plan above the baseline (peak demand or average demand plus safety stock), intended to absorb demand variability beyond historical norms.
**In use:** "We're building in a 15% buffer above last year's peak to account for expected growth."
**Common misuse:** Sizing a plan exactly to historical peak with no stated buffer, leaving no margin if actual demand exceeds the historical benchmark.

### Network optimization
The broader analytical process of determining facility count, location, and assignment of customer demand to facilities that minimizes total logistics cost.
**In use:** "Network optimization modeling across five facility-count scenarios shows the 3-DC configuration as the cost-minimizing option."
**Common misuse:** Evaluating only one or two facility-count scenarios instead of a broader range, potentially missing the actual cost-minimizing configuration.

### Throughput (warehouse/facility)
The volume of units or orders a facility or piece of equipment can process within a given time period, used as the basis for capacity planning.
**In use:** "Current throughput capacity is 8,000 units/hour, but peak demand requires closer to 11,000 units/hour."
**Common misuse:** Reporting throughput capacity without comparing it explicitly against the peak demand it needs to support, rather than average demand.
