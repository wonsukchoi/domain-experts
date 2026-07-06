# Network Support Specialist — Playbook

## 1. Severity/scope triage matrix (filled example)

| Signal | Scope | Tier | Response target | Resolution target |
|---|---|---|---|---|
| Single user, one app slow | 1 user | P3 | 4 business hours | 3 business days |
| One team's shared drive unreachable | ~15 users, 1 segment | P2 | 30 minutes | 4 hours |
| Site-to-site VPN down, branch isolated | 1 site, all users | P1 | 15 minutes, calendar clock | 2 hours |
| Core switch down, multiple sites affected | Multi-site | P1 | 15 minutes, calendar clock | 2 hours |

**Rule applied:** tier is set by scope × business impact, evaluated before any diagnosis starts. A single VP complaining loudly about a personal laptop is still P3; a quiet ticket reporting a whole floor down is P1 regardless of tone. Response clock and resolution clock are tracked separately — hitting the 15-minute response target (acknowledged, triage started) does not stop the resolution clock.

## 2. Duplex/speed mismatch counter check (filled example)

Suspected port: `Gi1/0/14`, nominally 1 Gbps, throughput measured at ~85 Mbps.

| Side | Configured | Interface counters (30-sec sample) |
|---|---|---|
| Switch port `Gi1/0/14` | Auto (negotiated: 100 Mbps/half) | Late collisions: 1,204; CRC errors: 3 |
| Host NIC | Forced 100 Mbps/full | Input errors: 0; FCS errors: 891 |

**Diagnosis:** classic duplex mismatch signature — the half-duplex side (switch) shows late collisions, the full-duplex side (host) shows CRC/FCS errors. Neither side alone shows both, which is why checking only one side clears the wrong suspect.

**Fix:** set both ends to the same explicit value — `speed 1000` / `duplex full` on the switch port, remove the forced 100/full override on the NIC, let both auto-negotiate or both hard-set to match. Never leave one end auto and one end forced — that mismatch is what produced this fault.

**Verify:** re-sample counters for 5 minutes post-fix; late collisions and FCS errors must both read 0 (not just "lower"), and measured throughput must return to ≥900 Mbps before closing the ticket.

## 3. MTU sweep procedure (filled example, second scenario)

Symptom: RDP sessions to a remote office connect but the screen freezes on any window resize; small clipboard pastes work fine.

| Step | Command | Result |
|---|---|---|
| 1. Baseline sweep | `ping -M do -s 1472 10.20.1.1` | Timeout (no reply) |
| 2. Binary search down | `ping -M do -s 1236 10.20.1.1` | Reply received |
| 3. Narrow | `ping -M do -s 1354 10.20.1.1` | Timeout |
| 4. Narrow | `ping -M do -s 1295 10.20.1.1` | Reply received |
| 5. Confirm boundary | `ping -M do -s 1324 10.20.1.1` | Reply received (largest working payload) |
| 6. Effective path MTU | 1324 payload + 28 (ICMP/IP header) | **1352 bytes** |
| 7. Packet capture during step 1 | `tcpdump icmp` on sender during the 1472-byte test | Zero ICMP Type 3 Code 4 replies seen — confirms black hole, not a slow/lossy link |

**TCP MSS to clamp:** 1352 − 20 (IP) − 20 (TCP) = **1312 bytes**.

**Fix command (edge router):** `ip tcp adjust-mss 1312` on the WAN-facing interface.

**Escalation note (to firewall team):** path is silently dropping ICMP Type 3 Code 4 between 10.20.1.1 and HQ; MSS clamping is a workaround, not the root-cause fix — request ICMP Fragmentation Needed passthrough be restored on the path.

## 4. DHCP scope exhaustion calculation (filled example)

Reported: ~40 devices on the Guest VLAN self-assigning `169.254.x.x` addresses.

| Field | Value |
|---|---|
| Scope range | 192.168.50.10 – 192.168.50.254 |
| Total addresses in range | 245 |
| Reserved/excluded (printers, APs, static) | 30 |
| Usable pool | 215 |
| Active leases at time of report | 213 |
| Lease utilization | 213 / 215 = **99%** |
| Average lease duration configured | 24 hours |
| Devices renewing/re-requesting per hour (lease churn) | ~18 |

**Threshold applied:** utilization ≥90% is the trigger to treat this as scope exhaustion rather than a one-off server hiccup; 99% confirms it. MAC randomization on mobile devices (each reconnect can present as a "new" client) is checked as a churn multiplier before assuming raw device count grew — pull the DHCP server's lease log and count *distinct MAC prefixes*, not just lease-table rows, to separate randomization noise from real growth.

**Remediation options, in fallback order:**
1. Shrink lease duration (24h → 4h) to recycle idle leases faster — no-cost, fastest to apply, may not be enough if raw device count has genuinely grown.
2. Reclaim excluded-but-unused addresses in the range.
3. Extend the scope (e.g., add 192.168.50.2–192.168.50.9 after confirming they're not gateway/reserved).
4. Segment onto a second VLAN/scope if device count has structurally outgrown the /24 — last resort, requires a change window.

**Verify:** utilization back under 80% for 24 hours and zero new APIPA reports before closing.

## 5. Broadcast storm / BPDU Guard check (filled example)

| Step | Check | Result |
|---|---|---|
| 1. Confirm timescale | Broadcast/multicast rate on uplink | Spiked from ~50 pps to ~40,000 pps in under 10 seconds |
| 2. Identify loop candidate | `show spanning-tree` on affected switches | Port `Fa0/8` (edge, wall jack) shows repeated STP topology-change notifications |
| 3. Check edge-port protections | `show run interface Fa0/8` | No `spanning-tree bpduguard enable`, no `spanning-tree portfast` configured |
| 4. Physical trace | Cable trace on the wall jack behind `Fa0/8` | Patch cable looped from one wall jack back to an adjacent jack on the same switch |

**Fix:** remove the looped cable immediately (stops the storm); then configure `spanning-tree portfast` + `spanning-tree bpduguard enable` on all identified edge ports (not just this one) so a future accidental loop on any edge port auto-disables the port instead of storming the segment.

**Verify:** broadcast/multicast rate back under ~100 pps baseline for 15 minutes; confirm BPDU Guard is active fleet-wide on edge ports via `show run | include bpduguard`, not just the one port that caused this incident.

## 6. Ticket resolution note — filled template

> **Resolution — [one-line symptom] (Ticket #[id], P[tier])**
> Root cause: [confirmed cause, not the reported symptom].
> Evidence: [specific counter/capture/report that proves it — name the exact numbers].
> Fix applied: [exact change, exact values].
> Verified: [end-to-end functional check, not a re-test of the original narrow symptom].
> Residual risk: [what the fix does NOT cover, and what's escalated separately, to whom].
