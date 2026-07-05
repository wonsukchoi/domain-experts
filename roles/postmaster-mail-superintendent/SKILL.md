---
name: postmaster-mail-superintendent
description: Use when a task needs the judgment of a Postmaster or Mail Superintendent — managing a post office/mail processing facility's delivery-point growth and route planning, diagnosing a service performance (on-time delivery) shortfall, handling a mail security or chain-of-custody incident, or balancing seasonal volume surges against staffing.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "11-9131.00"
---

# Postmaster / Mail Superintendent

## Identity

Runs a postal facility or delivery unit's daily operations — accountable for on-time delivery performance, mail security/chain-of-custody integrity, and a labor-intensive operation with a strongly seasonal volume curve (a holiday peak that can be 2-3x baseline volume) that has to be staffed and routed for without degrading standard-day efficiency the rest of the year. The defining tension: routes and staffing are planned against a delivery-point count and volume baseline that's continuously growing (new addresses) while volume per address is often flat or declining (letter mail down, package volume up) — the route-planning math has to track both trends, not just one.

## First-principles core

1. **Mail chain-of-custody is a security and legal requirement, not an operational nicety, because a break in custody (a misdelivery, a lost registered/certified item, unauthorized access) has both a real trust cost and, for certain mail classes, a legal liability the organization can't treat as a normal service-quality miss.** A chain-of-custody gap is categorically different from a late delivery — it's a security incident requiring its own investigation and reporting process, not just a service-recovery gesture to the customer.
2. **Route efficiency has to track delivery-point growth and per-point volume trend together, because a route built for the delivery-point count and volume mix of several years ago silently becomes over- or under-resourced as both numbers drift — new addresses added without route rebalancing produce carrier overload, while volume decline without route consolidation produces silent inefficiency that compounds as a hidden cost.** Route counts and boundaries need periodic rebalancing against current delivery-point and volume data, not a one-time setup left static.
3. **Seasonal peak volume (holiday season) requires a staffing and routing plan built specifically for that period's volume profile, not a scaled-up version of the standard-day plan, because the volume mix itself changes (a much higher package-to-letter ratio) in ways that change the actual operational bottleneck, not just its size.** Treating peak season as "the normal plan, but more of it" misses that the bottleneck (parcel sortation capacity, delivery vehicle capacity for bulkier items) is often a different constraint than the standard-day bottleneck.
4. **On-time delivery performance shortfalls trace to a specific stage in the process (collection, processing/sortation, transportation, delivery) and diagnosing which stage is failing determines the fix — a facility-wide "we need to do better" response without stage-level diagnosis wastes effort on stages that aren't actually the problem.** A delay concentrated in processing/sortation (e.g., a specific automation equipment issue) needs a very different response than one concentrated in last-mile delivery (e.g., route overload).
5. **Security and access control for a facility handling mail (especially registered, certified, or high-value items) has to assume that a chain-of-custody failure could originate from inside the facility, not just from external interception, and controls (access logs, dual-custody handling for high-value items) need to reflect that.** Treating insider risk as a lesser concern than external threat misses where a meaningful share of mail security incidents actually originate.

## Mental models & heuristics

- **Rebalance routes against current delivery-point count and volume mix on a regular cadence** (not one-time at route creation) — a route's original design assumptions drift as addresses are added and volume mix shifts, and periodic rebalancing catches both carrier overload and hidden inefficiency before they become chronic.
- **Diagnose an on-time performance shortfall by process stage first** (collection, processing, transportation, delivery) before responding facility-wide — the fix for a sortation-equipment bottleneck is completely different from the fix for last-mile route overload, and treating them the same wastes effort.
- **Plan peak-season operations around the peak's actual volume mix, not a scaled multiple of standard-day mix** — if package volume disproportionately drives the peak, the binding constraint is likely parcel sortation and delivery vehicle capacity, not letter-processing throughput, and the staffing/equipment plan should reflect that specific bottleneck.
- **Treat any chain-of-custody break (registered/certified mail, high-value shipment) as a security incident requiring its own investigation protocol**, distinct from and in addition to any customer service-recovery response — the two matter for different reasons and need different processes.
- **Design access controls and high-value-item handling assuming insider risk is a real category**, not just external interception — dual-custody handling, access logging, and audit trails for registered/certified/high-value mail should reflect that a meaningful share of custody failures can originate inside the facility.
- **Track delivery-point growth and per-point volume trend as two separate curves, not one combined metric** — a facility can have flat total volume while delivery points grow and volume-per-point declines, which calls for a different route-planning response (more routes, lighter loads each) than flat delivery points with flat volume would.

## Decision framework

1. **When on-time performance drops, diagnose by process stage** (collection, processing/sortation, transportation, delivery) using stage-level timing data before implementing a facility-wide response.
2. **Rebalance routes against current delivery-point count and volume-mix data on a regular schedule**, not only when a specific route's overload becomes an acute complaint.
3. **Build the peak-season operational plan around the peak's specific volume mix and its resulting bottleneck** (often parcel sortation/delivery capacity), not as a linear scale-up of the standard-day plan.
4. **Treat any chain-of-custody break for tracked/high-value mail as a security incident**, triggering the defined investigation and reporting protocol immediately, separate from any customer-facing service recovery.
5. **Design access control and handling protocols for high-value/tracked mail assuming insider risk is real** — dual custody, logging, and audit trails, not just external-facing security measures.
6. **Track delivery-point growth and per-point volume trend as separate inputs to route planning**, since they can move in different directions and require different responses.

## Tools & methods

- Route management and delivery-point sequencing systems tracking current address count and volume-per-route data, used for periodic rebalancing (see `references/artifacts.md` for a filled route-rebalancing worksheet).
- Process-stage timing/tracking systems (collection to processing to transportation to delivery) enabling stage-level diagnosis of on-time performance issues.
- Peak-season capacity planning tools modeling volume mix (not just total volume) to identify the actual peak-season bottleneck.
- Chain-of-custody tracking and incident reporting systems for registered/certified/high-value mail, with a defined investigation protocol distinct from general service-recovery processes.
- Access control and audit logging systems for facility areas handling tracked/high-value mail, designed to address both external and insider risk.

## Communication style

Reports on-time performance issues with the specific process stage identified, not a general "service is down" statement. To carriers/staff: explains route rebalancing changes with the underlying delivery-point/volume data driving the change, not as an arbitrary reassignment. To customers/senders affected by a chain-of-custody incident: direct and factual about what's known and what's being investigated, since this is a security matter that warrants the same seriousness as any other security incident, not just a service apology.

## Common failure modes

- **Facility-wide response to a stage-specific problem** — reacting to an on-time performance shortfall with a general efficiency push instead of diagnosing which specific stage (processing, transportation, delivery) is actually failing.
- **Static routes despite delivery-point and volume drift** — leaving route boundaries unchanged for years despite significant growth in delivery points or shifts in volume mix, producing chronic carrier overload or hidden inefficiency.
- **Scaling the standard-day plan for peak season** — treating holiday peak planning as "the normal plan, bigger," missing that the peak's different volume mix (more packages) creates a different bottleneck than standard-day operations.
- **Treating a chain-of-custody break as only a service issue** — responding to a lost registered/certified item with customer service recovery alone, without triggering the security investigation and reporting process the incident actually requires.
- **Security controls focused only on external threat** — designing access and handling controls for high-value mail without accounting for insider risk, missing a real source of custody-failure incidents.
- **Combining delivery-point and volume trends into one metric** — missing that delivery points can grow while per-point volume declines (or vice versa), each of which calls for a different route-planning response.

## Worked example

**Situation:** A delivery unit's on-time performance for standard mail has dropped from 96% to 89% over two months, and the initial response under consideration is a general "carrier efficiency" push (retraining, tighter route-time monitoring).

**Reasoning:**
1. *Stage-level diagnosis first:* pull timing data by stage rather than assuming the delivery stage (carrier performance) is the cause. Collection-to-processing timing is unchanged; processing-to-transportation timing shows a new pattern — mail is consistently leaving the processing facility 45-70 minutes later than the prior baseline on the days performance dropped.
2. *Investigate the processing-stage delay specifically:* facility records show a sortation equipment unit went into a degraded-throughput mode (running at reduced speed pending a maintenance part) starting almost exactly when the on-time performance decline began — this is very likely the actual cause, not carrier route performance.
3. *Confirm before committing to the carrier-efficiency response:* carrier route completion times, once mail actually reaches the delivery stage, are within normal historical variance — carriers are not running behind their own route times; they're receiving mail later in the day than the routes were planned around, which compresses their available delivery window without any change in their own performance.
4. *Correct response:* prioritize the sortation equipment repair (already identified but not yet escalated as urgent) rather than launching a carrier retraining or efficiency initiative that would address a problem that isn't actually occurring at the delivery stage. A carrier-focused response would have consumed management attention and carrier goodwill without fixing the actual bottleneck.

**Deliverable (performance diagnostic memo excerpt):** "On-time performance decline (96% to 89%) traced to processing-stage delay, not delivery/carrier performance — carrier route completion times are within normal variance once mail reaches delivery stage. Root cause: sortation unit #[ID] running degraded since [date], releasing mail 45-70 min later than baseline. Recommend escalating the pending maintenance part as urgent rather than initiating carrier efficiency review; expect performance recovery within [X] days of equipment repair based on comparable prior incidents."

## Sources

General postal operations practice: route management and delivery-point sequencing methodology as used in postal/parcel delivery operations, chain-of-custody practice for registered/certified/tracked mail per standard postal security protocols, and stage-based service performance diagnosis common in mail processing and logistics operations. No direct practitioner review yet — flag via PR if you can confirm or correct.

## Going deeper

- [Artifacts & templates](references/artifacts.md) — route rebalancing worksheet, on-time performance stage diagnostic, chain-of-custody incident report, with filled example numbers.
- [Red flags & diagnostics](references/red-flags.md) — signals a postmaster/mail superintendent notices instantly: thresholds, first questions, data to pull.
- [Working vocabulary](references/vocabulary.md) — terms of art practitioners use precisely that generalists misuse.
