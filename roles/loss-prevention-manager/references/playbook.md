# Loss prevention investigation and control playbook

Filled worksheets for the four recurring loss-prevention decisions: shrink decomposition, EBR triage scoring, apprehension evidentiary review, and investigation case filing.

## 1. Shrink decomposition worksheet

| Category | Definition | Typical detection method | This period's estimated share |
|---|---|---|---|
| External theft | Shoplifting, organized retail crime, burglary | EAS alarm data, video review, apprehension logs | 38% |
| Internal theft | Employee theft of cash/merchandise, sweethearting, collusion | EBR flags (voids, overrides, refunds), inventory variance by shift | 34% |
| Administrative/paperwork error | Receiving miscounts, pricing errors, damaged/unsellable goods not written off | Cycle count vs. POS reconciliation, receiving audit | 21% |
| Vendor shortage | Under-delivery from supplier billed as full delivery | Receiving count vs. invoice/PO reconciliation | 7% |

Rule: never propose an intervention (guard staffing, camera placement, audit process) until this table is filled for the specific location or region in question — the same aggregate shrink % can have a completely different breakdown store to store.

## 2. EBR (exception-based reporting) triage scoring

Score each flagged pattern to rank limited investigator hours:

```
Dollar-weighted score = (flag frequency) × (average dollar value per flag) × (deviation multiplier)

Deviation multiplier = flagged rate ÷ baseline/chain-average rate
```

| Flag pattern | Frequency/month | Avg $ per flag | Deviation multiplier | Score | Priority |
|---|---|---|---|---|---|
| No-receipt refunds, Store 12 | 340 | $46 | 3.8x | 59,432 | 1 |
| Register voids, Store 7, closing shift | 210 | $22 | 2.9x | 13,398 | 2 |
| Discount overrides, Store 3 | 480 | $8 | 1.6x | 6,144 | 3 |
| Refund-to-same-card pattern, Store 12 | 60 | $46 | 4.2x | 11,592 | 2 (tie, escalate alongside #2) |

Assign investigator time top-down by score, not by which flag type is easiest to review.

## 3. Apprehension evidentiary checklist (shoplifting)

All elements required before a stop — missing any one means documentation-only, no physical apprehension:

- [ ] Direct observation of the individual selecting or concealing merchandise
- [ ] Continuous, unbroken observation maintained from concealment through all points of sale
- [ ] Confirmation the item was not paid for (receipt check, POS log)
- [ ] Item still in the individual's possession at the point of the stop
- [ ] Stop conducted per company policy on tone, location (away from other customers), and permitted physical contact (none beyond a verbal request to return, absent jurisdiction-specific citizen's-arrest authority)
- [ ] Incident logged with time-stamped video reference within 24 hours regardless of outcome

If any box is unchecked: document the observation, do not stop, refer to camera system for pattern-building on a future visit instead.

## 4. Internal investigation case file template

```
Case #: <ID>
Opened: <date> | Category: internal / external / vendor / administrative
Subject(s): <employee ID(s) or N/A>
Flag origin: <EBR alert, cycle count variance, tip, other — cite specific report>
Dollar exposure estimate: <amount>, calculation: <show the math, not just a number>
Evidence collected: <video timestamps, transaction logs, witness statements>
HR/legal notified: <date>, present at interview: <yes/no, names>
Interview conducted per two-person rule: <yes/no>
Disposition: <termination recommended / restitution demand / law enforcement referral / no action — insufficient evidence>
Control gap identified: <what allowed this — e.g., override threshold too high, missing manager-PIN requirement>
Recommended control fix: <specific, with rollout scope — single store, region, chain-wide>
```

## 5. ORC (organized retail crime) escalation criteria

Escalate to a regional ORC task force or law enforcement referral, rather than treating as isolated shoplifting, when **two or more** of the following are present in the same review window:

- Same high-theft SKU category elevated across 3+ stores in the same region
- Loss events clustered within the same multi-week window across those stores
- Recovered/attempted merchandise resale identified on a secondary marketplace matching the SKU pattern
- Same vehicle, individual, or group identified across multiple stores' video
- Aggregate estimated loss across the pattern exceeds $50,000
