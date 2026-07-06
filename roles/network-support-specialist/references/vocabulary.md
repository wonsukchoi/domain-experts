# Network Support Specialist — Vocabulary

Terms generalists routinely misuse in tickets and escalations — not because the term is obscure, but because its precise scope gets blurred with an adjacent, looser idea.

### Duplex mismatch
**Definition:** A link where one end is set to half-duplex and the other to full-duplex (usually because one side auto-negotiates and the other is hard-set), so the link comes up and passes some traffic but collides under load.
**In use:** "Gi1/0/14 is showing late collisions on the switch side and CRC errors on the host — classic duplex mismatch, not a bad cable."
**Misuse note:** Generalists use it as a catch-all for "slow port," including cases that are actually a bad cable, a speed mismatch with matching duplex, or an oversubscribed uplink. A true duplex mismatch requires the specific two-sided signature (late collisions vs. CRC/FCS errors) — without both sides checked, calling it "duplex mismatch" is a guess, not a diagnosis.

### Late collision
**Definition:** A collision detected by a half-duplex Ethernet device after the first 64 bytes of a frame have already been transmitted — normal collisions happen early and are handled by CSMA/CD, late ones indicate the device didn't expect contention at all, which is the fingerprint of duplex mismatch.
**In use:** "Late collisions: 1,204 on the switch port over a 30-second sample — that's the half-duplex side of the mismatch."
**Misuse note:** Often reported interchangeably with "collision" generally. An ordinary (early) collision on a half-duplex segment is expected background noise; a *late* collision specifically means something is behaving as full-duplex against a half-duplex peer. Conflating the two makes a normal shared-segment counter look like an active fault.

### CRC error / FCS error
**Definition:** A frame arrived with a Frame Check Sequence that doesn't match its computed checksum, meaning the frame is corrupted — commonly caused by a duplex mismatch (on the full-duplex side), a bad cable, or electrical interference.
**In use:** "Host NIC shows FCS errors: 891 with zero late collisions — that's the full-duplex side of the same mismatch, not a separate cabling issue."
**Misuse note:** Treated as automatically meaning "bad cable." In a duplex mismatch it appears on the full-duplex side specifically because the half-duplex peer is colliding mid-frame — replacing the cable won't fix it, matching the duplex settings will. Which cause it is depends on which side shows the error and whether the counter clears after a cable swap or after a duplex fix.

### PMTUD black hole
**Definition:** A failure mode where Path MTU Discovery breaks because a device on the path drops the oversized packet *and* the ICMP "Fragmentation Needed" message meant to tell the sender to shrink future packets, so the sender never learns and keeps retransmitting the same oversized packet forever.
**In use:** "Small pastes work, window resize freezes RDP — that's the PMTUD black hole signature, confirm with an MTU sweep before touching the app."
**Misuse note:** Frequently reported as "the VPN is dropping packets" or "the link is unstable," which implies packet loss generally. A PMTUD black hole is not lossy — small packets succeed every time; only packets above the effective MTU fail, deterministically, every time. Treating it as intermittent loss sends the fix in the wrong direction (retry logic, QoS) instead of at the actual cause (ICMP being blocked).

### ICMP Type 3 Code 4 (Fragmentation Needed)
**Definition:** The specific ICMP message a router sends back to a sender when it must drop an oversized packet with the "don't fragment" bit set — it's the mechanism PMTUD depends on to work at all.
**In use:** "Packet capture during the failed 1472-byte test shows zero ICMP Type 3 Code 4 replies — confirms the black hole, not a slow link."
**Misuse note:** Generalists say "ICMP is blocked" as if all ICMP is one thing. A firewall can permit ping (Echo Request/Reply) while still blocking Type 3 Code 4 specifically, and vice versa — the two have to be checked separately in a capture, not inferred from whether `ping` itself works.

### MSS clamping
**Definition:** A router configuration (`ip tcp adjust-mss`) that rewrites the Maximum Segment Size field in the TCP handshake so endpoints negotiate a smaller segment size directly, bypassing the need for ICMP-driven PMTUD entirely.
**In use:** "TCP MSS clamped to 1360 on the VPN gateway so TCP self-limits segment size instead of relying on ICMP that's being dropped upstream."
**Misuse note:** Frequently presented as "the fix" for a PMTUD black hole, full stop. It's a workaround for TCP traffic only — UDP-based traffic on the same path has no MSS field and remains exposed to the same black hole. Closing the ticket after MSS clamping without escalating the actual ICMP-blocking policy leaves a real gap.

### APIPA (169.254.x.x)
**Definition:** Automatic Private IP Addressing — a self-assigned address a Windows client falls back to only when a DHCP request goes completely unanswered, not when it's answered with an error.
**In use:** "~40 devices on the Guest VLAN show APIPA addresses — check lease utilization before assuming the DHCP server is down."
**Misuse note:** Reflexively reported as "DHCP server is down." APIPA fires from silence, which is consistent with the server being down but equally consistent with the server being up and simply out of leases (scope exhaustion) — the two require completely different checks (service status vs. utilization report) and get conflated because the client-side symptom looks identical either way.

### DHCP scope exhaustion
**Definition:** A condition where the usable address pool for a DHCP scope is fully leased out, so new or renewing clients get no offer at all — distinct from a DHCP server outage, misconfiguration, or a bad relay/helper address.
**In use:** "Lease utilization is 213/215 = 99% — that's scope exhaustion, not a server hiccup; pull distinct MAC prefixes before assuming raw device count grew."
**Misuse note:** Generalists jump straight to "expand the scope" as the fix. Before that, MAC-randomizing mobile devices can inflate apparent device count by presenting as a new client on every reconnect — the actual remediation order (shorten lease duration → reclaim unused addresses → extend scope → segment) depends on whether growth is real or an artifact of randomization noise, not just on the raw utilization percentage.

### BPDU Guard
**Definition:** A switch port feature that immediately error-disables an edge port the instant it receives a Bridge Protocol Data Unit (an STP control frame), on the assumption that a legitimate edge port (a PC, a printer) should never see one — because if it does, something (usually an unmanaged switch or a looped cable) has turned that access port into a bridge.
**In use:** "Fa0/8 has no BPDU Guard configured — that's how the looped patch cable was able to storm the segment instead of getting shut down in milliseconds."
**Misuse note:** Confused with STP itself or with Root Guard, which protect different things. BPDU Guard doesn't prevent loops in the core topology — it protects specifically against an edge port becoming an unintended bridge point. Configuring it fleet-wide on edge ports after one incident (not just the one port involved) is the actual fix; treating it as a one-off per-port patch leaves every other edge port exposed to the same failure.

### Broadcast storm
**Definition:** A self-reinforcing flood of broadcast/multicast traffic that saturates a switched segment within seconds, almost always caused by a Layer 2 loop with no spanning-tree protection to break it.
**In use:** "Broadcast rate spiked from ~50 pps to ~40,000 pps in under 10 seconds — that timescale itself is diagnostic of a loop, not a legitimate traffic surge."
**Misuse note:** Reported generically as "the network is slow" or "high traffic," which invites a bandwidth-upgrade response. The defining signature is the timescale (seconds) and the traffic type (broadcast/multicast, not unicast) — a genuine traffic surge from legitimate use ramps over minutes and is overwhelmingly unicast; conflating the two sends the response toward capacity planning instead of finding and removing a physical loop.

### Severity tier (P1/P2/P3)
**Definition:** A classification set by scope of impact and business impact, which in turn determines a response-time target (how fast the issue must be acknowledged and triage started) and a separately tracked resolution-time target — not a measure of how the report was escalated.
**In use:** "Scoped as P2 — a failing nightly backup with data-loss risk across multiple users, not a full outage, but time-sensitive enough that it can't wait for a P3 cycle."
**Misuse note:** Generalists conflate "response" with "resolution" as one clock — hitting the response target (acknowledged, triage started) does not stop the resolution clock. On the volume-vs-scope misuse itself, see First-principles core, principle 1.

### Root cause
**Definition:** The confirmed underlying condition that produced the reported symptom, established through a tested theory and evidence (a counter reading, a capture, a utilization report) — not a description of what stopped working.
**In use:** "Root cause: PMTUD black hole. Evidence: MTU sweep found effective path MTU of 1400 bytes; capture confirmed zero ICMP Type 3 Code 4 replies for oversized packets."
**Misuse note:** Ticket notes frequently record "root cause: the connection was hanging" — that's the symptom restated, not the cause. Without the specific evidence that proves *why*, the next responder on a recurrence has nothing to start from and re-runs the entire diagnosis from zero.

### Top-down / bottom-up / divide-and-conquer
**Definition:** Three entry strategies for a layered troubleshooting model — start at the application layer and work down, start at the physical layer and work up, or start at a middle layer (commonly Layer 3) and use the result to eliminate half the remaining possibilities regardless of outcome.
**In use:** "Site-wide symptom over one tunnel → divide-and-conquer at the network layer first, since a ping across the boundary halves the search space either way."
**Misuse note:** Treated as interchangeable "troubleshooting steps" rather than a choice matched to the symptom's scope. Rigidly defaulting to divide-and-conquer (or any one method) even when something physical was just visibly touched — a cable unplugged, a port moved — wastes time working outward layer by layer instead of checking the obvious point first.
