### Two "redundant" links or devices haven't been traced through their full physical path
- **Usually means:** A shared conduit, entry point, switch, or power source could create a hidden single point of failure despite apparent redundancy at the layer being reviewed.
- **First question:** Has the complete physical path (conduit, cabling, entry point, power) for each redundant path been traced and confirmed independent?
- **Data to pull:** Physical infrastructure diagrams, conduit/entry point documentation for each path.

### Capacity planning is based on 24-hour average utilization
- **Usually means:** The actual peak/busy-hour utilization could be much higher than the average suggests, masking real congestion risk during the hours that matter most.
- **First question:** What is the busy-hour (peak-period) utilization specifically, not the 24-hour average?
- **Data to pull:** Time-of-day utilization breakdown, not just an aggregate average.

### Network segmentation boundaries are defined by department/organizational structure
- **Usually means:** The segmentation may not actually reflect real trust boundaries or traffic isolation needs, potentially allowing a compromise to spread more broadly than intended.
- **First question:** Does this segmentation boundary correspond to an actual trust zone or traffic isolation requirement, or just to where a department happens to sit?
- **Data to pull:** Data flow and trust requirements between systems/areas, current VLAN/subnet assignment rationale.

### Real-time traffic (VoIP, video) shares a link with bulk data traffic and no QoS is configured
- **Usually means:** Call/video quality could degrade during busy periods even if total link bandwidth appears sufficient, since real-time traffic isn't being prioritized.
- **First question:** Has the specific bandwidth reservation needed for real-time traffic's peak concurrent load been calculated, and is QoS marking/prioritization configured to protect it?
- **Data to pull:** Concurrent real-time traffic load estimate, current QoS configuration (or its absence).

### A routing protocol was selected based on team familiarity rather than topology scale or convergence requirements
- **Usually means:** The chosen protocol may not scale well or may have a slower failure-convergence time than the topology actually requires.
- **First question:** Does this protocol match the network's actual scale (single-domain vs. multi-site/multi-provider) and required convergence time after a failure?
- **Data to pull:** Network topology scale and site count, required/tested convergence time.

### A failure scenario (single link or device down) hasn't been actively tested
- **Usually means:** The redundancy design's actual failover behavior is unverified — it may not perform as expected when a real failure occurs.
- **First question:** Has a controlled failure test been performed to confirm the expected failover behavior actually occurs?
- **Data to pull:** Failover test results (or their absence), expected vs. actual failover time if tested.

### A network design change was made with no documentation of its redundancy or capacity rationale
- **Usually means:** Future engineers may not understand why the design was built a certain way, risking an uninformed change that reintroduces a previously solved problem.
- **First question:** Is there design documentation explaining the redundancy path, capacity sizing basis, and segmentation rationale for this network?
- **Data to pull:** Existing network design documentation (or its absence).

### A link's growth headroom is based on current busy-hour utilization with no buffer for projected growth
- **Usually means:** The link may reach saturation sooner than expected if demand grows as projected, without an explicit buffer built in.
- **First question:** What growth rate is projected for this traffic, and does the current capacity plan include a buffer above today's busy-hour peak to accommodate it?
- **Data to pull:** Historical growth trend for this traffic type, current capacity plan's stated buffer (or lack thereof).
