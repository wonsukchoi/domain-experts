# Network/Systems Administrator — Playbook

## Staged rollout sequencing (canary → bake → batch), filled example

**Scope:** 40-device fleet, firmware/config push.

| Stage | Devices | Bake window | Go/no-go gate |
|---|---|---|---|
| Canary | 2 lowest-business-impact sites | 4 hours | BGP/OSPF neighbor count stable, VPN/session reconnect rate ≥98% of pre-change baseline |
| Batch 1 | 19 (50% of the 38 remaining) | 24 hours | Same gate as canary, plus zero new P2+ tickets tagged to the change |
| Batch 2 | 19 (remainder) | 24 hours post-push, formal close at 72 hours | Same gate; if clean, change ticket closes |

**Rollback trigger (define before push, not during):** any stage showing routing reconvergence failure, session/reconnect rate below 98% of baseline, or a P1 ticket tagged to the change within the bake window — revert that stage only, hold subsequent stages, do not advance the fleet.

**Sizing rule of thumb:** canary = smallest group that still exercises every device model/OS version in the fleet, never fewer than 2 (a single canary can't distinguish a device-specific fault from a change-wide one). Batch size for the remaining stages isn't a fixed multiplier — it's set by working backward from the deadline: split what's left into as few equal batches as the deadline's margin allows, so each stage still gets a full bake window. In the 40-device/14-day example, that's two 19-device batches at a 24-hour bake each, completing day 5 with 9 days of margin instead of one all-at-once push with none.

## Emergency same-day exception (KEV/active-exploitation deadline)

When a 14-day KEV clock or active-exploitation evidence forces same-day movement, canary stays but bake compresses:

| Stage | Devices | Bake window |
|---|---|---|
| Canary | 2 lowest-impact sites | 4 hours (compressed from 24) |
| Full remaining fleet | rest | rolled in one pass after canary bake clears |

Never skip the canary stage itself — compress the bake window, not the step count.

## Incident Command response sequence, filled example (P1 — total outage)

| T+ | Action |
|---|---|
| 0 min | Declare incident, name Incident Commander (IC). IC role ≠ person doing the fix. |
| 0–15 min | IC runs goal-setting meeting: current known state, hypothesis, who owns which layer (physical / routing / DNS / app), first fix-block owner assigned. |
| 15 min | First leadership update: impact statement, next update time (T+75), single next action. No technical narrative to leadership. |
| 15–75 min | Fix-block 1 (capped 60 min). Change applied only through confirmed-independent out-of-band path. |
| 75 min | Leadership update #2. If fix-block 1 didn't resolve: fix-block 2 begins, capped 60 min, different hypothesis or escalation to vendor/next-tier. |
| Every 60 min thereafter | Leadership update on the same cadence until resolved. |
| Resolution | IC declares incident closed, starts postmortem timeline from the incident log kept live during the event (not reconstructed after). |

**Fix-block discipline:** if a capped block doesn't resolve it, stop, reassess, don't silently extend into a second uncapped hour — that's how a 20-minute outage becomes an all-nighter.

## Out-of-band access independence check (run before any fleet-wide change)

1. Identify the primary path used to reach the device being changed (SSH over production VPN, web GUI over LAN, etc.).
2. Identify the recovery path if the primary change breaks routing/VPN/DNS.
3. Confirm the recovery path shares **zero** physical or logical dependency with what's being changed — different circuit, different power feed, console server or cellular OOB, not "the same VPN concentrator on a different port."
4. If step 3 fails, provision the independent path *before* the change ticket is approved, not during the incident it would have prevented.

## Backup job and monitoring coverage review checklist

- [ ] Every production server has a scheduled backup job — cross-reference asset inventory (IPAM/CMDB) against backup-tool job list; flag any host in inventory with no matching job.
- [ ] Last successful **restore test** per backup tier is ≤90 days old — a green "backup completed" status without a restore test only confirms bytes were written, not that they're usable.
- [ ] Backup job failure alerting routes to a monitored channel, not email-only — email-only alerts have a documented median time-to-notice of >24 hours in most shops.
- [ ] RPO/RTO stated per system tier (e.g., Tier 1: RPO 1 hr / RTO 4 hr; Tier 3: RPO 24 hr / RTO 24 hr) and actual last-backup timestamp checked against RPO, not just job-success status.
- [ ] Monitoring coverage: every device in IPAM has an active SNMP/agent poll — cross-reference monitoring-tool inventory count against IPAM device count; a gap here is dark infrastructure with no alerting.
- [ ] Alert thresholds reviewed against **busy-hour**, not 24-hour average utilization (see capacity table below) — an alert set at 90% of the 24-hour average will never fire before saturation during the actual peak window.
- [ ] Escalation path per alert severity documented and tested (paged the right person, at the right hour, within the last quarter) — an untested escalation path is the same as no escalation path during a 2 a.m. page.

## Circuit and capacity planning lead-time table

| Item | Typical lead time | Planning trigger |
|---|---|---|
| New WAN/ISP circuit order | 2–3 months | Start ordering at 4 months before needed, not when current circuit is already saturated |
| Data-center/office move — HVAC/cooling run-in | 48–72 hours before occupancy | Cooling must run and stabilize before equipment is powered on; filters replaced after move-in dust settles |
| Firmware/patch vendor release cadence (non-emergency) | Monthly maintenance window | Baseline cadence — overridden by KEV/compliance deadlines when one is active |
| Quarterly PCI ASV scan | Every 90 days | Must use an ASV-accredited scanner for internet-facing CDE systems; internal-only tooling doesn't satisfy the control |

## Busy-hour vs. average utilization comparison, filled example

| Metric | Value |
|---|---|
| 24-hour average utilization | 34% |
| Busy-hour utilization (8–10 AM) | **86%** |
| Capacity planning basis | Busy-hour figure (86%), not the average |
| Trigger for upgrade order | Busy-hour utilization crossing 80% sustained over 2 consecutive weeks — start the 2–3 month circuit-order lead time at that point, not at 95% |

## RFC 1918 overlap audit (network merger / acquisition)

1. Pull the full subnet list from both networks' IPAM/documentation of record.
2. Diff the two lists for any overlapping RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16), not just exact-match subnets — a /16 on one side can silently contain a /24 on the other.
3. For every overlap found, document it as a blocker for tunnel/peering standup — do not bring up the interconnect until renumbering or NAT is in place for the overlapping range.
4. Where renumbering isn't feasible before a deadline, use static NAT/1:1 translation as the fallback, documented in the change ticket with the overlapping ranges named explicitly.

## Password/access policy audit checklist (NIST 800-63B alignment)

- [ ] Rotation policy: confirm no blanket 90-day forced rotation remains on any GPO/IdP policy — rotation should trigger only on suspected/confirmed compromise.
- [ ] Minimum length ≥8 enforced, 64+ characters permitted (not blocked by an upper-bound policy relic).
- [ ] No composition-rule requirement (mandatory special character/number) still active — these correlate with predictable increment patterns, not stronger passwords.
- [ ] Breached-password screening enabled against a known-compromised-credential list at set time and at login.
- [ ] MFA required on all remote-access and privileged-account paths — check this before checking password policy detail, since MFA absence outweighs any password-policy fix.
