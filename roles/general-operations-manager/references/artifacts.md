# Operations diagnostic artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Bottleneck analysis (filled — see Worked example in SKILL.md for full narrative)

| Step | Volume/month | Capacity/month | Slack | Bottleneck? |
|---|---|---|---|---|
| Sales (deals closed) | 85 | — (target 80) | — | No |
| Fulfillment — standard orders | 63 | 70 | +7 | No |
| Fulfillment — rush orders | 22 (promised by sales) | 8 (actual rush capacity) | −14 | **Yes — the real constraint** |

**Rule applied:** overall fulfillment throughput (78/month against a 75 target) looked healthy on the dashboard, masking the narrow rush-capacity sub-constraint that was actually driving customer complaints.

## 2. RACI template (filled example, rush-order capacity check initiative)

| Task | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Build real-time rush-capacity indicator | Ops systems team | VP Operations | Fulfillment lead, Sales lead | Sales reps |
| Update sales workflow to check indicator before promising rush delivery | Sales ops | VP Sales | Fulfillment lead | Account executives |
| Monitor rush-capacity utilization post-launch | Fulfillment lead | VP Operations | — | VP Sales |

**Rule applied:** each row has exactly one Accountable owner — no task has two people who could each assume the other is driving it.

## 3. Process map / handoff worksheet (filled example)

| Step | Owner | Input required | Output | Gap identified |
|---|---|---|---|---|
| Deal negotiation | Sales | Standard terms sheet | Signed contract with delivery terms | Rush terms offered without a capacity check |
| Order intake | Fulfillment | Signed contract | Scheduled fulfillment slot | No visibility into promised rush terms until order already committed |
| Fulfillment execution | Fulfillment | Scheduled slot | Delivered order | Rush slots oversubscribed relative to actual capacity |

**Rule applied:** the map traces the actual sequence and identifies the specific gap (no capacity visibility at the negotiation step) rather than describing the documented, idealized process.

## 4. 5 Whys root cause worksheet (filled example)

| Why # | Question | Answer |
|---|---|---|
| 1 | Why are complaints rising? | Rush orders are frequently late. |
| 2 | Why are rush orders late? | Fulfillment can't process them fast enough at the promised volume. |
| 3 | Why is fulfillment overcommitted on rush orders? | Sales is promising more rush deliveries than fulfillment's rush capacity supports. |
| 4 | Why is sales promising more than capacity supports? | Sales has no visibility into current rush-capacity availability when negotiating terms. |
| 5 | Why is there no visibility? | No shared system or check exists between sales and fulfillment for rush-specific capacity — only overall throughput is tracked. |

**Rule applied:** the analysis continues past the first plausible cause (fulfillment being slow) to the actual systemic root (missing shared capacity visibility), which is where the fix belongs.
