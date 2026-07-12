# Floor surveillance and apprehension playbook

Filled worksheets for the four recurring floor-level decisions: shrink-zone rotation, the stop decision checklist, self-checkout exception review, and incident/chain-of-custody filing.

## 1. Heat-mapped floor rotation

Built from the prior period's EBR/shrink data by zone; walked on a visible but irregular schedule so presence isn't predictable enough to route around.

| Zone | Prior-quarter shrink rate | Rotation weight (min/hour) | Primary risk type |
|---|---|---|---|
| Electronics/cosmetics | 2.4% | 20 | External concealment, diversion teams |
| Self-checkout bank (6 lanes) | 1.9% | 15 | Scan avoidance, receipt fraud |
| Apparel/fitting rooms | 1.6% | 10 | Concealment, wardrobing setup |
| Front registers | 0.8% | 8 | Sweethearting, void/no-sale abuse |
| Stockroom/receiving door | 0.6% | 7 | Internal theft, vendor collusion |

Rule: total rotation minutes should track the shrink-rate ranking — a zone at 2.4% gets roughly 2.5x the walk-time of a zone at 0.8%, not an even split across zones because they're all "worth checking."

## 2. Stop decision checklist

All elements required before a physical stop — missing any one means documentation-only, no approach:

- [ ] Direct personal observation of the subject selecting or concealing the specific item(s)
- [ ] Continuous, unbroken observation maintained from concealment through every point-of-sale opportunity (no gap, no hand-off without a corroborating trained witness)
- [ ] Non-payment confirmed at register/self-checkout (receipt check or transaction log pull) before approach
- [ ] Item still in the subject's possession at the moment of the stop
- [ ] Risk assessment clear: no weapon indicator, group size manageable, location not overcrowded
- [ ] Stop plan set: position between subject and exit, verbal identification, name the specific item, no physical contact beyond a blocking position

If any box is unchecked: do not stop. Log the observation, bookmark video, and either continue floor-building the pattern for a later stop or hand off to the loss prevention manager.

## 3. Self-checkout exception review

Score lanes/subjects for review priority — post-payment stops are weaker cases, so pre-payment intervention is the priority queue:

```
Exception score = (skip-scan or weight-mismatch alerts this visit) × (item value) × (pre/post-payment multiplier)

Pre/post-payment multiplier: 1.5x if caught before payment screen clears, 0.6x if only caught after
```

| Lane | Alert type | Item value | Stage caught | Multiplier | Priority |
|---|---|---|---|---|---|
| SCO-3 | Weight mismatch, item swapped for cheaper barcode | $34.99 | Pre-payment | 1.5x | 1 — intervene now |
| SCO-1 | Skip-scan, bagged without scan | $12.99 | Post-payment (exited) | 0.6x | 3 — document, review loyalty history |
| SCO-5 | Skip-scan, repeated same card 3x this month | $18.50 avg | Post-payment | 0.6x, but pattern flag | 2 — refer to LP manager as possible ring, not one-off |

Rule: a single post-payment skip-scan is a documentation item, not a stop. Three or more from the same payment/loyalty ID in a month is a pattern referral, regardless of individual item value.

## 4. Incident report and chain-of-custody template

```
Incident #: <ID> | Date/time: <start–end> | Zone: <location>
Subject(s) observed: <description avoided in report where possible — use behavior, not appearance, as the identifier>
Behavior sequence observed: <camera-check, concealment, diversion, etc. — in order, with timestamps>
Continuous observation window: <start time> to <stop or loss-of-sightline time>
Non-payment verification: <receipt check / POS log / SCO transaction pull — cite specific record>
Stop conducted: <yes/no> | If yes: location relative to exit, time, physical contact (none beyond blocking, per policy: yes/no)
Item(s) recovered: <description, quantity, unit value, total value>
Item(s) NOT actioned (unobserved concealment, companion items, etc.): <description, value, reason not actioned>
Video bookmarks: <camera ID, timestamp ranges>
Chain of custody: <recovered item location, who has custody, transferred to — signature/timestamp for each handoff>
Police called: <yes/no, reason> | Escalated to LP manager: <yes/no, reason>
```

Rule: file the same shift, regardless of outcome — an observation that didn't result in a stop is still logged for pattern-building across future shifts.

## 5. Integrity shop checklist (internal theft floor check)

Undercover compliance check on a cashier, run periodically or when floor observation raises a flag (repeated no-scan pattern with a familiar "customer," stalled drawer during a specific person's checkout):

- [ ] Shopper purchases a marked/tracked item set of known value
- [ ] Confirm item is scanned and rung at full price, no unauthorized discount or void
- [ ] Confirm drawer reconciles to the transaction (no shortage logged against this till after)
- [ ] If a failure occurs: do not confront on the floor — document time, register, item, and route to LP manager for the two-person-rule interview process, not a specialist-led confrontation
