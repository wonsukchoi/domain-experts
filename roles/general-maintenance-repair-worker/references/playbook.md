# Playbook

Filled templates for triaging a queue, checking a trade boundary, running a PM schedule, and handing a job off to a licensed sub.

## Hazard-tier triage matrix

Sort every open ticket into one row before sequencing anything. Age breaks ties only inside a tier — it never promotes a ticket across tiers.

| Tier | Example issue | Target response | Default action |
|---|---|---|---|
| Safety | Active water/gas leak, exposed live wiring, breaker trips twice on reset, loose grab bar/handrail, structural crack widening | < 1 hour, same-visit | Stabilize (shutoff, lockout, isolate) immediately; DIY if within boundary, escalate same day if not |
| Compliance | No heat in cold season, no hot water, blocked fire egress, missing smoke/CO detector, pest infestation past threshold | 24–48 hours (often statute-driven — check local habitability code) | Diagnose today; escalate if boundary hit, otherwise repair before end of SLA window |
| Occupant-impact | Appliance down (dishwasher, garbage disposal), GFCI nuisance trip, one AC zone out in mild weather, minor plumbing drip | 3–5 business days | Batch with same-day tickets if capacity allows; otherwise schedule within SLA |
| Cosmetic | Squeaky hinge, flickering common-area light, scuffed paint, loose cabinet handle | Next PM cycle (≤ 30 days) | Defer to routine rounds; never displaces a higher tier for being older |

## Trade-boundary checklist

Run this on every ticket *before* opening a wall, panel, line, or fixture. Any single "yes" means stop diagnosing and move to escalation with an interim safety action.

| Check | Yes → | Interim safety action |
|---|---|---|
| Does it require opening a sealed refrigerant circuit? | Escalate — EPA Section 608 certification required by federal law (40 CFR Part 82), independent of any state license. | Do not disturb line-set connections; note suspected refrigerant leak/charge issue for the HVAC sub. |
| Does it involve cutting, joining, or pressure-testing a gas line? | Escalate — almost no state handyman exemption covers gas work at any dollar amount. | Shut off the gas valve at the appliance or meter if a leak is suspected; ventilate; do not operate switches nearby. |
| Does it involve altering overcurrent protection (breaker/fuse sizing) or opening the main service panel beyond a simple device swap? | Escalate — licensed electrician; a second trip on reset confirms a load fault, not a nuisance. | Lock out the breaker (LOTO), tag "do not energize," leave equipment de-energized. |
| Is the repair structural (load-bearing wall, foundation, roof framing) or does it visibly affect a load path? | Escalate — structural engineer or licensed contractor sign-off. | Rope off/restrict access if there's a collapse or fall risk. |
| Does the job plausibly require a building permit (water heater replacement, panel upgrade, structural alteration, most gas work)? | Escalate — permit-triggering work voids the handyman exemption regardless of price. | Document current condition with photos before any further action. |
| Is the combined labor-and-material cost approaching or exceeding the state's handyman exemption threshold? | Escalate or get a contractor's estimate — thresholds are commonly $300–$1,000 (CA: $500 under B&P Code §7048); verify locally, don't assume the number from a different state. | None specific — this is a cost/licensing check, not a hazard one. |

If every check comes back "no," the ticket is DIY-cleared — proceed to sequencing.

## Preventive maintenance schedule (220-unit example property)

| System | Frequency | Example task | Est. time |
|---|---|---|---|
| HVAC filters (common + in-unit) | Monthly (seasonal peak), quarterly otherwise | Replace 1"–2" filters, check condensate drain for algae/clog | 10 min/unit |
| Smoke/CO detectors | Semi-annual | Test, replace battery, log serial/expiry, note any unit past 10-yr detector life | 5 min/unit |
| GFCI outlets (kitchens/baths/exterior) | Quarterly | Press test/reset button, confirm trip-and-reset cycle | 3 min/outlet |
| Water heaters | Annual | Flush sediment, test TPR valve operation, check for tank bulging/rust weep | 20 min/unit |
| Pool/mechanical room equipment | Monthly | Visual inspect motor mounts, listen for bearing whine, confirm bonding grid intact (NEC 680) | 30 min |
| Fire extinguishers / egress lighting | Monthly (visual), annual (certified service) | Confirm charged gauge, unobstructed egress path, emergency lighting battery test | 15 min/floor |
| Roof/gutters | Semi-annual (spring/fall) | Clear debris, check flashing, note ponding | 2 hrs/building |

**Target ratios:** PM completion rate ≥ 85% of scheduled tasks per month; open work-order backlog ≤ 4 weeks of tech-hours (roughly 2 weeks is the healthy target, 4+ weeks is the point where reactive-emergency volume starts climbing the following quarter). Both are stated industry heuristics, not fixed regulatory numbers — track them locally and adjust to the property's actual failure history.

## Escalation handoff note (filled example)

> **To:** ABC Plumbing (licensed, on-call)
> **Property / unit:** Maplewood Apartments, Unit 114
> **Reported:** Mon 6:00am, water pooling around water heater base
> **Observed:** Steady drip from the tank's bottom seam, not the TPR valve or a fitting — TPR valve tested dry and seats correctly on manual lift.
> **Ruled out:** TPR valve (not the source), supply/return fitting connections (all dry, hand-tight and no weep).
> **Suspected cause:** Tank corrosion/failure at the seam — replacement, not a repair.
> **Current state:** Water and gas supply to the unit shut off at 6:20am; tenant relocated to Unit 118 (vacant) pending replacement; area mopped, fan running to prevent mold.
> **Action needed:** Tank replacement — this exceeds the state handyman exemption and requires a permit in this jurisdiction; requesting quote and earliest install slot.
> **Photos attached:** tank base, valve, shutoff location.

## State handyman-exemption thresholds (illustrative — verify locally)

| State (example) | Threshold (labor + material) | Notes |
|---|---|---|
| California | $500 | Void if a permit is required (Bus. & Prof. Code §7048); gas/structural work not covered regardless of amount. |
| Texas | No statewide general contractor license for residential handyman work below most trade-specific thresholds | Electrical, plumbing, and HVAC still require trade-specific state licenses regardless of job price. |
| Florida | $500–$1,000 range depending on locality/trade | Electrical and plumbing licensing enforced at the state level (DBPR); local exemption amounts vary. |

This table is a starting orientation, not a compliance reference — the only reliable number is the one published by the property's own state contractor licensing board, checked before any job that's close to a threshold.
