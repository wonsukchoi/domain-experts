# Network/systems administrator working vocabulary

Terms a network/systems admin uses precisely and a generalist blurs together. Format: definition → how a practitioner says it → common misuse.

**Blast radius** — The set of systems, users, or sites actually affected if a given change goes wrong, as distinct from the set it was intended to touch. A property of how the rollout is staged, not of how good the change is.
In use: "The WAF rule itself is fine — the blast radius is the problem, it's going to every edge node in one push with no canary."
Misuse: treating blast radius as a fixed property of the change ("it's just a config tweak, low risk") instead of a variable set by the rollout plan — a trivial-looking change pushed everywhere at once has the same blast radius as a risky one.

**Canary** — A small, deliberately low-impact subset of the fleet that receives a change first, with a defined bake window before the change proceeds to the rest, so a defect surfaces on a few sites instead of all of them.
In use: "Flash the two lowest-impact regional offices as canary, four-hour bake, then batch two."
Misuse: calling a rollout "canaried" when the first batch is 25% of the fleet or the "bake window" is skipped because a deadline is close — a canary only does its job if it's small and if it's actually watched before the rest proceeds.

**Bake window** — The fixed monitoring period after a change reaches a canary or batch, before the rollout is allowed to continue, during which specific signals (protocol reconvergence, reconnect success rate) are watched for a regression.
In use: "24-hour bake on batch two before we touch the remaining sites — BGP and VPN reconnect rate both have to hold."
Misuse: treating the bake window as a calendar delay to satisfy change management rather than an active check against named failure signals — nobody actually looks at the metrics during it.

**Out-of-band (OOB) management** — A path to reach and administer a device (console server, cellular failover, dedicated management VLAN) that does not depend on the production network path the device itself provides or that could fail alongside it.
In use: "Confirm the console-server path into those two sites is on its own circuit before we flash anything — we can't recover over the same VPN service we're about to break."
Misuse: assuming the admin VPN or jump box counts as out-of-band when it in fact terminates on the same device, link, or power circuit as what's being changed — it only counts as OOB if it survives the specific failure being planned for.

**Rollback trigger** — The specific, pre-committed condition (a metric threshold or state check) that ends a rollout and reverts, decided before the push starts rather than judged in the moment.
In use: "Trigger's written into the ticket: any batch site failing OSPF reconvergence inside the bake window, or reconnect success under 98% of baseline."
Misuse: proceeding on a vague "we'll pull it if something looks wrong" instead of a number decided in advance — without a pre-committed threshold, the person watching the bake window under incident pressure tends to explain away the first bad signal instead of reverting.

**KEV clock** — The 14-calendar-day (internet-facing) or 45-day (everything else) remediation deadline that starts once a CVE is added to CISA's Known Exploited Vulnerabilities catalog, per Binding Operational Directive 22-01 — distinct from a CVSS score or a routine patch cycle.
In use: "CVSS 9.8 isn't what's driving the timeline — it's on the KEV list now, so the clock is 14 days, internet-facing."
Misuse: treating a high CVSS score alone as the deadline-setter, or assuming the KEV deadline means "patch everything tonight" rather than "complete a staged rollout inside this window" — the clock sets the outer bound, not the rollout method.

**RFC 1918 overlap** — Two private (non-routable) address ranges in use on networks that are about to be connected (merger, tunnel, peering) that happen to cover the same address space, causing silent routing conflicts once connected.
In use: "Before that tunnel goes up, pull both address plans — if they're both sitting on 10.0.0.0/8 unscoped, we have an overlap problem, not a routing problem."
Misuse: diagnosing the resulting intermittent connectivity loss as a hardware or protocol fault and re-troubleshooting the tunnel for weeks, instead of checking for address-space overlap first — the symptom looks like flaky routing, not like a numbering conflict.

**Route withdrawal (BGP)** — A router or backbone announcing that it can no longer reach a given prefix, removing it from the routing table; this can take down services (like DNS resolvers) that depend on those addresses without anything being wrong with the service itself.
In use: "The DNS servers didn't fail — their prefixes got withdrawn in the backbone audit, so nothing could route to them."
Misuse: treating "DNS is down" as a DNS-layer problem and restarting resolver services, when the actual fault is a routing-layer withdrawal upstream that just presents as a naming failure.

**Toil** — Manual, repetitive operational work that scales linearly with the size of the system and produces no lasting improvement once done — as distinct from work that, once completed, removes the need to do it again.
In use: "Restarting that service by hand every on-call rotation is toil — it's not part of the job, it's the thing we haven't automated yet."
Misuse: treating recurring manual fixes as an unavoidable fact of the role rather than a backlog item to eliminate — Google SRE's toil cap (roughly half an engineer's time) is a target to push under, not a description of normal workload.

**Ticket opened:closed ratio** — The month-over-month trend between how many incidents/tickets are opened versus closed; a rising ratio is read as a staffing or process signal at the team level, not evidence about any individual's performance.
In use: "The ratio's been climbing three months straight — that's a capacity conversation with the business, not a coaching conversation with the on-call engineer."
Misuse: responding to a rising ratio by telling individual admins to work faster or clear tickets quicker, when the trend is a team-level staffing or automation signal that individual effort can't fix.

**ASV scan** — A vulnerability scan run by a PCI-accredited Approved Scanning Vendor against internet-facing, cardholder-data-environment systems, required quarterly under PCI DSS 11.3.2; an internal or unaccredited scan does not satisfy the requirement even if it finds the same issues.
In use: "That's a Tenable internal scan, not an ASV scan — it doesn't count toward the quarterly PCI requirement even though it flagged the same CVE."
Misuse: treating any vulnerability scan as interchangeable with the compliance-mandated ASV scan, or treating a passing quarterly ASV scan as current coverage — a new KEV-listed CVE the following week isn't covered by last quarter's clean result.

**Password rotation vs. compromise-triggered rotation** — NIST 800-63B guidance: rotate credentials only on suspected or confirmed compromise, not on a fixed calendar; favor length (64+ characters permitted) over composition rules.
In use: "We're not resetting the fleet's passwords on the 90-day GPO — that's calendar rotation, not a response to an actual compromise indicator."
Misuse: treating scheduled rotation itself as a security control that stops credential-stuffing attacks, when in practice it mainly trains users into predictable incremental password patterns (Password1!, Password2!) without addressing the actual compromise risk.

**Incident Command (IC) structure** — A named-commander model for major incidents: one person coordinating, a goal-setting meeting at the start, fixed-interval leadership updates, and work executed in capped time blocks rather than open-ended debugging.
In use: "We're standing up IC for this — I'm commander, hourly updates to leadership, work in one-hour blocks."
Misuse: running a major incident as an open Slack channel with whoever's available typing fixes in, and calling that "incident response" — without a named commander and a fixed update cadence, work stretches into an unstructured all-nighter instead of a bounded, communicated process.

**Change/CAB ticket** — The change-advisory-board artifact of record for a fleet-wide push: scope, rollout stages, rollback trigger, and deadline, written and approved before the first canary goes out, not reconstructed afterward as documentation.
In use: "Ticket's filed before batch one — scope, canary sites, bake windows, and the rollback trigger are all in it already."
Misuse: treating the CAB ticket as a formality filled in after the work is done, or as a place to write "will roll out carefully" instead of the actual canary/bake/rollback numbers — the point is that the plan exists and is reviewable before anything ships, not that a form got completed.
