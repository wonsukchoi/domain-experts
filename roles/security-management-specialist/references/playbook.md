# Security Management Playbook

## CARVER-style asset scoring template

Score each candidate asset/facility 1-5 on each dimension; sum out of 30. Threshold for a dedicated control plan: >=20.

| Asset | Criticality | Accessibility | Recoverability | Vulnerability | Effect | Recognizability | Total |
|---|---|---|---|---|---|---|---|
| Data center | 5 | 3 | 2 | 4 | 5 | 2 | 21 |
| Executive office suite | 4 | 2 | 4 | 2 | 4 | 4 | 20 |
| Main lobby / reception | 2 | 5 | 5 | 3 | 2 | 5 | 22 (deters, low-impact) |
| Loading dock | 3 | 4 | 4 | 4 | 3 | 1 | 19 |
| Records/supply room | 2 | 3 | 5 | 3 | 1 | 1 | 15 |

Note: high Accessibility/Recognizability with low Criticality/Effect (lobby) scores high but needs deterrence-class controls, not hardening-class — CARVER ranks attention, not spend type.

## Guard-force cost model (example, 6-post campus)

| Post | Coverage | Rate | Annual cost |
|---|---|---|---|
| Main gate | 24/7 (3 shifts) | $28/hr | $245,280 |
| Lobby/reception | 16/7 (2 shifts, business hours + evening) | $26/hr | $151,840 |
| Loading dock | 8/5 (business hours) | $27/hr | $56,160 |
| Mobile patrol (campus-wide) | 24/7 (1 roving) | $29/hr | $254,040 |
| **Total (4 of 6 posts shown)** | | | **$707,320** |

Response-time target should be specified per post, not just coverage hours: e.g. "Tier-1 alarm (data center, executive floor) — guard on scene <4 min; Tier-2 (perimeter) — <8 min." A patrol density recalculated from response-time targets, not from a flat headcount request, is the deliverable finance should see.

## Multidisciplinary threat-assessment intake protocol

1. **Intake trigger:** any report from HR, a manager, security, or a coworker of concerning behavior (explicit threat, escalating anger, fixation, weapons comment, documented anger-management flag tied to an adverse employment action).
2. **Immediate triage (within 2 hours of report):** security lead determines if there's an imminent physical threat — if yes, law enforcement contacted first, before internal process continues.
3. **Team convened within 24-48 hours:** security, HR, legal, EAP (or equivalent). Each brings their lane: security (physical risk factors, access), HR (employment history, prior complaints), legal (any protective order or legal history), EAP (voluntary support options).
4. **Risk tier assigned:** Low (monitor, EAP offer, no access change) / Medium (access restriction pending review, increased patrol awareness, documented check-in cadence) / High (immediate access revocation, law enforcement liaison, possible restraining-order support for affected employees).
5. **Documented review cadence:** Medium and High tiers reviewed at 30/60/90 days minimum, or on any new signal.
6. **Closure requires team sign-off**, not a single function's decision — security cannot unilaterally close a High-tier case, nor can HR overrule a security-flagged physical risk without documented rationale.

## Executive protection tiering

| Tier | Exposure profile | Coverage |
|---|---|---|
| Tier 0 | No public identification, low-crime-index locations only | Standard corporate security awareness training, no dedicated detail |
| Tier 1 | Publicly identified with company, moderate travel to average-crime-index cities | Advance-work for travel (venue/route review), no standing detail |
| Tier 2 | Publicly identified with a specific controversial decision (layoffs, litigation, activist campaign), or travel to elevated-crime-index/politically unstable regions | Dedicated travel protection detail, residential security review |
| Tier 3 | Documented specific threat (naming the individual) or sustained elevated public controversy | Full-time protective detail, threat-intelligence monitoring, residential hardening |

Reassess tier at least annually and immediately after: a public controversy naming the executive, a layoff announcement they're publicly tied to, or any direct threat received through any channel.

## Access-control tiering by consequence

| Tier | Example spaces | Control | Audit cadence |
|---|---|---|---|
| Tier 1 (severe consequence) | Data center, executive floor, R&D lab | Badge + PIN or biometric, mantrap/anti-tailgate, logged entry reviewed weekly | Weekly automated, monthly manual spot-check |
| Tier 2 (moderate consequence) | Finance office, HR records room | Badge only, logged | Monthly automated review |
| Tier 3 (low consequence) | General office floors, break rooms | Badge only | Quarterly review |
| Tier 4 (public-facing) | Lobby, visitor areas | Reception check-in, visitor badge with escort requirement | Ongoing visual, no log review needed |

A badge audit flags: badge-out with no matching badge-in within the shift (possible held-door/tailgate), repeated after-hours access with no scheduled reason, and access attempts at a terminated employee's badge ID.
