### A port shows "connected" but throughput is under ~30% of rated link speed (e.g., a gigabit port sustaining ~10–100 Mb/s)
- **Usually means:** A duplex or speed mismatch between the port and its peer — one side auto-negotiates, the other is hard-set, or negotiation itself failed silently.
- **First question:** What do both ends' interface counters show — late collisions on one side, CRC/input errors on the other?
- **Data to pull:** `show interface` (or equivalent) error counters from both ends of the link, plus each side's configured speed/duplex setting.

### A transfer or session hangs only once payload size crosses a threshold (small requests succeed, large ones freeze — e.g., SSH connects but freezes on wide output, VPN passes pings but not bulk transfer)
- **Usually means:** A Path MTU Discovery black hole — an oversized packet needs fragmentation guidance via ICMP, and that ICMP reply is being dropped somewhere on the path.
- **First question:** What is the actual effective path MTU when swept directly, and did an ICMP Type 3 Code 4 reply come back for the oversized probe?
- **Data to pull:** `ping -M do` binary-search MTU sweep results; packet capture at the sender during a failed oversized-payload attempt.

### No ICMP Type 3 Code 4 message arrives back at the sender during an oversized-packet test
- **Usually means:** ICMP is being blocked outright somewhere on the path (commonly a firewall policy), not that the path is simply slow or the app is misbehaving.
- **First question:** Is ICMP explicitly permitted end-to-end on this path, or blocked as a blanket policy?
- **Data to pull:** Firewall/ACL rules governing ICMP on the suspected segment, packet capture confirming the missing reply.

### A fleet of clients has self-assigned 169.254.x.x (APIPA) addresses
- **Usually means:** DHCP scope exhaustion — the pool is out of leases, not a DHCP server outage, especially where MAC-randomizing devices inflate apparent device count.
- **First question:** What is the current lease count and churn rate against the pool size and exclusion ranges?
- **Data to pull:** DHCP scope utilization report, lease-duration and exclusion-range configuration, device count trend over the last 24–48 hours.

### Broadcast/multicast traffic saturates multiple switches within seconds, not minutes
- **Usually means:** A spanning-tree loop, most often from an edge port that lacks BPDU Guard and has been bridged (accidentally or via a rogue switch).
- **First question:** Which edge ports currently lack BPDU Guard, and did one of them just go into a forwarding loop?
- **Data to pull:** Spanning-tree port-state and BPDU Guard status per port, switch CPU/broadcast-rate graphs for the last few minutes.
