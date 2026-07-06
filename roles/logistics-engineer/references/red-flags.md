### A facility location decision is based on minimizing average distance to customers alone
- **Usually means:** The recommendation may not reflect the full cost picture, since facility fixed costs and inventory carrying cost changes can offset or exceed freight savings from a shorter average distance.
- **First question:** Has total landed cost (facility fixed cost + freight + inventory carrying cost) been modeled for this location option, or just distance/freight cost alone?
- **Data to pull:** Facility fixed cost estimate, freight cost estimate, inventory carrying cost estimate for the proposed location.

### A center-of-gravity model's output coordinates are treated as the final site selection
- **Usually means:** Real road distances, available real estate, labor market depth, and infrastructure access haven't been validated against the model's simplified straight-line/weighted-centroid output.
- **First question:** Has this specific location been validated against real road network distances and site-level constraints, or is it still just the model's raw output?
- **Data to pull:** Center-of-gravity model output, real estate/labor market/infrastructure data for the specific candidate site.

### A facility-count decision (adding or consolidating DCs) is justified by freight savings alone
- **Usually means:** The analysis may be missing the offsetting facility fixed cost increase and inventory carrying cost impact from splitting or consolidating inventory pools.
- **First question:** What is the total cost comparison across facility-count options, including fixed cost and inventory carrying cost changes, not just the freight cost difference?
- **Data to pull:** Facility fixed cost, freight cost, and inventory carrying cost estimates for each facility-count option being compared.

### A warehouse's fast-moving (A) items are slotted far from the pack/ship station
- **Usually means:** Unnecessary pick travel time is being added to the highest-volume picks, compounding into real labor cost at scale.
- **First question:** Has this facility's items been classified by pick velocity (ABC), and does the current slotting plan reflect that classification?
- **Data to pull:** SKU-level pick velocity/frequency data, current warehouse layout/slotting plan.

### Facility or equipment capacity is sized against average daily demand
- **Usually means:** The facility is likely undersized for peak-period conditions, risking bottlenecks, overtime costs, or missed service levels during seasonal or promotional peaks.
- **First question:** What is peak-period demand for this facility, and how does the current capacity plan compare to it, not just to average demand?
- **Data to pull:** Historical peak demand data, current facility/equipment capacity specifications.

### An inventory carrying cost estimate for a multi-facility network doesn't account for the loss of risk-pooling benefit
- **Usually means:** Splitting inventory across more locations generally requires more total safety stock to maintain the same service level, and omitting this effect understates the true cost of adding facilities.
- **First question:** Has the safety stock requirement been recalculated for the multi-facility scenario, accounting for the loss of pooling benefit, or is it assumed unchanged from the single-facility baseline?
- **Data to pull:** Current safety stock levels and service level targets, demand variability data by region.

### A network redesign recommendation doesn't show the cost comparison across multiple facility-count options
- **Usually means:** The recommendation may reflect a single evaluated scenario rather than the actual cost-minimizing option across a reasonable range of alternatives.
- **First question:** Has the total cost been modeled across a range of facility counts (e.g., 1, 2, 3, 4), or only for the specific option being proposed?
- **Data to pull:** Total cost estimates for each facility-count option in the reasonable range.

### A capacity plan doesn't specify a stated service-level buffer above peak demand
- **Usually means:** Without an explicit buffer, the plan may be sized right at peak with no margin for demand variability above historical peak levels.
- **First question:** What service-level buffer (percentage above historical peak) is built into this capacity plan?
- **Data to pull:** Historical peak demand and its year-over-year variability, stated buffer percentage in the capacity plan.
