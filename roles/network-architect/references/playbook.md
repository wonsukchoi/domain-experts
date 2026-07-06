# Computer Network Architect — Playbook

## Redundancy path trace checklist

1. Identify each "redundant" pair (links, devices, power sources).
2. Trace each path's complete physical route — cabling, conduit, building entry point.
3. Check whether both paths share any common physical infrastructure at any point.
4. Check power source independence — do both paths depend on the same power circuit or UPS?
5. If any shared point is found, document it as a single point of failure requiring remediation (physically diverse routing, separate power).

**Use:** A redundancy design is only as good as its weakest shared point — confirming redundancy at one layer (e.g., two ISPs) means nothing if both paths funnel through the same conduit.

## Busy-hour vs. average utilization comparison (filled example)

| Metric | Value |
|---|---|
| 24-hour average utilization | 32% |
| Busy-hour utilization (9-11 AM) | **87%** |
| **Capacity planning basis** | Busy-hour figure (87%), not the average |

**Use:** Always measure and report busy-hour utilization specifically — a 32% average can hide an 87% peak, and capacity decisions made on the average alone would understate real urgency.

## VoIP QoS bandwidth reservation calculation (filled example)

| Component | Value |
|---|---|
| Concurrent call capacity needed | 100 calls |
| Bandwidth per call (G.711 codec, including overhead) | ~87 kbps |
| **Total reserved bandwidth needed** | 100 × 87 kbps = **8.7 Mbps** |
| QoS marking | DSCP EF (Expedited Forwarding) for voice traffic |
| Remaining capacity | Available to data traffic on a best-effort basis |

**Use:** Calculate the specific bandwidth reservation for real-time traffic's peak concurrent load, and configure QoS to guarantee it — don't rely on "we have enough total bandwidth" as a substitute for this calculation.

## Routing protocol selection table

| Topology | Recommended protocol | Why |
|---|---|---|
| Single-domain enterprise network (one organization, one administrative control) | OSPF (or similar interior gateway protocol) | Fast convergence, suited to a single administrative domain |
| Multi-site / multi-provider network | BGP | Designed for control across separate autonomous systems and larger-scale routing policy needs |
| Small branch office, simple topology | Static routing or simple IGP | Avoids unnecessary protocol complexity for a topology that doesn't need it |

**Use:** Match the protocol to actual topology scale and convergence requirements — don't default to whichever protocol the team already knows best if it doesn't fit this network's actual scale.

## Network design findings memo — filled example

> **Network Architecture Review — HQ WAN and Voice**
> Redundancy: Both ISP links share a common physical entry conduit — **not truly redundant** as currently routed. Recommend diverse physical entry path for one provider.
> Capacity: 24-hour average utilization 32%, but **busy-hour (9-11 AM) utilization is 87%** — link is near saturation during actual peak usage, despite the average figure suggesting ample headroom.
> VoIP: 100 concurrent calls require 8.7 Mbps reserved bandwidth. **Recommend QoS (DSCP EF) prioritization** to protect voice quality during the busy-hour congestion window identified above.
> **Overall recommendation: Address the conduit-sharing redundancy gap, plan a capacity upgrade or traffic-shaping strategy based on the 87% busy-hour figure (not the 32% average), and implement QoS before adding further real-time traffic to this link.**
