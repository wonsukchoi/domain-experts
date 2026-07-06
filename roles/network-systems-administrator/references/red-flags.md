# Red flags

### "The internet is down" ticket volume spikes org-wide within a 5-minute window
- **Usually means:** DNS resolution failure or a routing/BGP event upstream, not a true internet outage — a single naming or routing fault reads as total loss because every app depends on it.
- **First question:** Can any affected host resolve a name via a different resolver (8.8.8.8, a secondary internal DNS server) right now?
- **Data to pull:** Resolver query logs for SERVFAIL/NXDOMAIN spikes, and the BGP/route table diff for the last 30 minutes.

### A single fleet-wide push is scheduled for more than 20% of devices in one maintenance window
- **Usually means:** No canary or bake window was built into the change plan — the rollout risk was priced on the fix being correct, not on the blast radius if it isn't.
- **First question:** What is the canary group, and what is the rollback trigger if the bake window shows a regression?
- **Data to pull:** The CAB/change ticket's rollout section — canary size, bake duration, and named rollback threshold.

### Admin/recovery access (console server, out-of-band VPN, badge system) shares a network path or power circuit with the systems it's meant to recover
- **Usually means:** The recovery path will go down in the same incident it's needed for — this is the exact failure that locked Meta's own responders out during the Oct 2021 backbone outage.
- **First question:** If this device/circuit fails right now, can an admin still reach the console out-of-band?
- **Data to pull:** Out-of-band topology diagram or IPAM record showing the physical/logical path independence of console/cellular failover from production.

### A CVE lands in the CISA KEV catalog on an internet-facing system
- **Usually means:** The 14-calendar-day remediation clock has started and overrides the normal patch cycle — waiting for the next scheduled maintenance window will miss the deadline.
- **First question:** Is this asset internet-facing (14-day clock) or internal-only (45-day clock), and how many days of margin does the current staged-rollout plan leave?
- **Data to pull:** KEV catalog entry date, asset exposure classification, and the canary/batch schedule with elapsed-time total.

### Password policy still enforces rotation on a fixed calendar (e.g., every 90 days) with no compromise indicator
- **Usually means:** The policy is inherited from an old GPO baseline, not a current security control — NIST 800-63B (Rev. 4) recommends rotation only on suspected/confirmed compromise, and calendar rotation trains users into predictable increment patterns.
- **First question:** Has this policy been reviewed against 800-63B, or is it running because "it's always been 90 days"?
- **Data to pull:** Current password policy GPO/config and the date of its last security review.

### Two networks are being merged or peered without an RFC 1918 overlap audit
- **Usually means:** Overlapping private address ranges are present and will cause silent, intermittent routing failures weeks after the merge, not an immediate visible break.
- **First question:** Has every subnet on both sides been diffed for overlap before the tunnel or peering session goes up?
- **Data to pull:** IPAM export from both networks, sorted by CIDR, for an overlap diff.

### VPN reconnect success rate drops below 98% of pre-change baseline during a bake window
- **Usually means:** The firmware or config change just pushed has a negotiation or routing defect — this is a rollback trigger, not a metric to watch and wait on.
- **First question:** Does this cross the rollback threshold written into the change ticket, and has the next batch been held?
- **Data to pull:** VPN concentrator reconnect success-rate dashboard for the canary/batch group versus the pre-change 7-day baseline.

### A quarterly PCI ASV scan was run by an internal or unaccredited tool
- **Usually means:** The scan does not satisfy PCI DSS 11.3.2 regardless of whether it passed — the requirement is specifically an ASV-accredited external scan for internet-facing cardholder-data-environment systems.
- **First question:** Is the scanning vendor on the current PCI SSC ASV list for this quarter?
- **Data to pull:** ASV accreditation status and the scan report's vendor attestation.

### Backup job success-rate dashboard hasn't been checked in over 30 days
- **Usually means:** A silently failing backup job is indistinguishable from a healthy one until a restore is needed — job completion notifications get filtered or ignored long before anyone notices.
- **First question:** When was the last test restore actually performed, not just the last "job succeeded" notification?
- **Data to pull:** Backup job success/failure log for the last 30 days and the date of the last verified test restore.

### Monthly ticket backlog's opened-to-closed ratio has grown for 3+ consecutive months
- **Usually means:** A staffing or process gap, not an individual admin working too slowly — reading it as an individual performance issue misses the systemic signal.
- **First question:** Is the growth concentrated in one ticket category (pointing at a process fix) or spread evenly (pointing at headcount)?
- **Data to pull:** Ticket system's monthly opened-vs-closed count, broken out by category, for the last 6 months.

### The same manual step appears in every on-call rotation's runbook
- **Usually means:** Toil that should be automated, not a permanent fixture of the job — left unaddressed it consumes the time budget meant for the automation that would remove it.
- **First question:** How many on-call hours per rotation does this step currently cost, and is that pushing total toil over roughly half of available engineering time?
- **Data to pull:** On-call runbook step frequency log and cumulative toil-hours estimate per rotation.

### A WAN circuit order is placed less than 6 weeks before a planned office or data-center move date
- **Usually means:** The 2-3 month carrier lead time won't be met — the move date will slip or the site will open without connectivity, not a scheduling inconvenience that can be expedited.
- **First question:** What is the carrier's confirmed install date, and does it fall before or after the planned occupancy date?
- **Data to pull:** Circuit order confirmation with committed install date versus the project's occupancy timeline.
