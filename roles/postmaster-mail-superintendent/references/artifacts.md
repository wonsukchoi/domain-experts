# Artifacts & templates

Filled examples an agent can populate or execute against. Load this when producing an actual route rebalancing analysis, stage diagnostic, or custody incident report — not for general reasoning (that's `SKILL.md`).

## Route rebalancing worksheet

```
Route: [ID]                          Last rebalanced: [date]

Delivery points:
  At last rebalance: 420
  Current: 468 (+11.4%)

Volume per delivery point (avg pieces/day):
  At last rebalance: 3.2
  Current: 2.6 (-18.8%, letter mail decline offsetting point growth)

Estimated route time (points × per-point handling time + travel):
  At last rebalance: [X] hours
  Current estimated: [Y] hours

Rebalance trigger check: >10% change in delivery points OR >15% change in volume-per-point
since last rebalance -> THIS ROUTE QUALIFIES, schedule rebalance review.

Recommended action: [split route / merge with adjacent / adjust boundary — based on current
carrier time estimate vs. standard shift length]
```

## On-time performance stage diagnostic

```
Period: [date range]              Baseline on-time %: 96%              Current: 89%

Stage timing (compare current period vs. prior baseline):
  Collection -> Processing arrival: [baseline] vs. [current] — variance: [X]
  Processing -> Transportation release: [baseline] vs. [current] — variance: [X]
  Transportation -> Delivery unit arrival: [baseline] vs. [current] — variance: [X]
  Delivery unit arrival -> Delivered: [baseline] vs. [current] — variance: [X]

Stage with largest variance: [identify] -> investigate root cause at THIS stage specifically,
not facility-wide.

Carrier route completion time (once mail reaches delivery stage): [within normal variance? Y/N]
-> if Y, this confirms the issue is NOT at the delivery/carrier stage, redirect investigation.
```

## Chain-of-custody incident report

```
Item type: [registered/certified/high-value]         Tracking #: [ID]
Last confirmed custody: [location, time, who]
Point custody broken: [location/stage where item is unaccounted for]

Immediate actions:
  [ ] Facility search initiated
  [ ] Access logs pulled for the relevant time window and location
  [ ] Staff with access during the window identified
  [ ] Sender/recipient notified per policy

This is a SECURITY incident — route through security/investigation process in addition to any
customer service recovery, not instead of it.

Resolution: [item located / confirmed lost / under investigation]
Root cause (if determined): [external interception / internal process failure / other]
```
