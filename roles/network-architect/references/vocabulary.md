### Single point of failure (SPOF)
Any single component (device, link, conduit, power source) whose failure would cause an outage, despite apparent redundancy elsewhere in the design.
**In use:** "Both ISP links share the same entry conduit — that's a hidden SPOF despite having two separate providers."
**Common misuse:** Confirming redundancy at one layer (e.g., two routers) without tracing the full physical and logical path for a shared point of failure elsewhere.

### Busy-hour utilization
The utilization level of a network link or resource during its actual peak usage period, as distinct from a 24-hour or longer-period average.
**In use:** "Busy-hour utilization is 87%, even though the 24-hour average is only 32%."
**Common misuse:** Using average utilization for capacity planning, which can mask near-saturation conditions during the specific hours that matter most to the business.

### Network segmentation (VLAN/subnet)
Dividing a network into isolated broadcast/trust domains to contain traffic, limit broadcast scope, and restrict how far a compromise or misbehaving device can propagate.
**In use:** "Segmentation here isolates the point-of-sale systems from the general office network, a genuine trust boundary."
**Common misuse:** Defining segmentation boundaries around organizational department names rather than actual trust zones and traffic isolation requirements.

### QoS (Quality of Service)
A set of techniques (traffic classification, marking, priority queuing) used to guarantee bandwidth and low latency for specific traffic types, typically real-time applications, over a shared link.
**In use:** "QoS marks voice traffic with DSCP EF, giving it priority queuing over bulk file transfers during busy periods."
**Common misuse:** Assuming sufficient total link bandwidth guarantees good real-time application performance without implementing QoS to protect that traffic from competing bulk traffic.

### DSCP (Differentiated Services Code Point)
A field in the IP header used to mark packets for specific QoS treatment, commonly used to prioritize real-time traffic like voice (often marked "EF," Expedited Forwarding).
**In use:** "Voice packets are marked DSCP EF to receive priority queuing across the network path."
**Common misuse:** Configuring QoS priority queuing without consistent DSCP marking end-to-end, so priority treatment is lost at some point along the path.

### Latency, jitter, and packet loss (real-time traffic budget)
The three key performance metrics for real-time applications (VoIP, video conferencing) — latency (delay), jitter (variation in delay), and packet loss — each with application-specific tolerance thresholds.
**In use:** "Voice quality needs latency under about 150ms one-way, jitter under about 30ms, and minimal packet loss."
**Common misuse:** Evaluating real-time application readiness based on available bandwidth alone, without measuring or budgeting for latency, jitter, and packet loss specifically.

### Routing protocol (OSPF, BGP)
The protocol used by network devices to determine and exchange information about the best path for traffic — OSPF is commonly used within a single administrative domain (enterprise network), BGP for routing between separate networks/providers or large multi-site environments.
**In use:** "OSPF handles routing within our campus network, while BGP manages routing between our sites and ISPs."
**Common misuse:** Selecting a routing protocol based on team familiarity rather than the network's actual scale, number of sites/providers, and required convergence time after a failure.

### Convergence time
The time it takes a network's routing protocol to detect a failure and recalculate paths so traffic resumes flowing, after a link or device failure.
**In use:** "This protocol's convergence time is under a second, meeting our requirement for minimal voice call disruption during a failover."
**Common misuse:** Assuming all routing protocols have similar convergence characteristics, when the choice significantly affects how quickly the network recovers from a failure.

### Failover testing
Deliberately simulating a link or device failure to verify that redundancy and routing design actually behave as expected.
**In use:** "Failover testing confirmed the standby link took over within 2 seconds, as designed."
**Common misuse:** Assuming a redundancy design works as intended based on its documentation alone, without actually testing a real failure scenario to confirm the expected behavior occurs.

### Growth headroom (capacity buffer)
Additional capacity built into a network design beyond current peak utilization, to accommodate projected traffic growth without requiring an immediate upgrade.
**In use:** "We're sizing this link with 40% headroom above current busy-hour peak to accommodate projected growth over the next 18 months."
**Common misuse:** Sizing capacity to exactly match current peak utilization with no buffer, risking saturation as soon as any growth occurs.
