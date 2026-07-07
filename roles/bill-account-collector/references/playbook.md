# Bill and Account Collector — Playbook

## Pre-call compliance gate

Run before every dial:

| Check | Pass condition | If fail |
|---|---|---|
| Contact window | Current time is 8:00am-9:00pm in the debtor's local time zone | Do not dial; queue for next valid window |
| Call-frequency (Reg F 7-in-7) | Fewer than 7 calls to this debt in trailing 7 days, and no call already made to this debt in trailing 7 days if this would be a repeat contact within that window | Do not dial; note next eligible date |
| Cease-and-desist flag | No active written cease-and-desist on file | If flagged, only permitted contacts are: confirming cessation, notifying of a specific intended action (e.g., referral to legal) |
| Attorney-representation flag | No known attorney representation on file | If flagged, all contact routes through counsel only |
| Employer-contact restriction | No known employer prohibition on workplace contact | If flagged, do not call the workplace number |
| Dispute status | No unresolved FDCPA §1692g dispute filed within the 30-day validation window | If disputed and unresolved, pause collection-pressure language; validation documentation must be sent/received first |

## Portfolio aging-bucket triage (illustrative)

| Bucket | Days past due | Typical recovery-rate pattern* | Priority signal |
|---|---|---|---|
| Current | 1-29 | Highest | Self-cure likely without contact; light-touch reminder only |
| Early | 30-59 | High, drops steadily | Best return on proactive contact effort |
| Mid | 60-89 | Moderate, declining | Contact + payment-plan offer; watch for prior broken promises |
| Late | 90-119 | Low | Prioritize accounts with any recent partial payment or open communication over ones gone fully silent |
| Charge-off risk | 120+ | Lowest per account, but largest aggregate dollar exposure | Evaluate for settlement offer, payment plan, or write-off/legal referral |

*Recovery-rate percentages vary by portfolio type, debt origination channel (medical, retail, financial-services), and agency; validate against the specific portfolio's own historical performance rather than assuming these figures transfer.

## Payment-plan structuring sequence

1. Confirm balance and any applicable interest/fee terms with the debtor before proposing numbers.
2. Ask the debtor what monthly amount and start date is realistic — do not lead with the collector's target.
3. Apply a 10-15% cushion below the debtor's stated maximum capacity when the debtor volunteers a figure that seems aggressive relative to their described situation (e.g., a debtor under obvious financial stress offering to pay more than a comparable prior plan sustained).
4. Calculate the resulting number of installments: `balance ÷ monthly amount = number of payments` (adjust for any interest per account terms).
5. Confirm payment method (bank draft, card, mailed check) and exact first-payment date — a plan without a locked first date and method is not yet a confirmed plan.
6. Send written confirmation of the plan terms, including the required "this is an attempt to collect a debt" disclosure, within the same business day.
7. If a scheduled payment is missed, contact within 2-3 business days (not immediately, to allow for processing lag) before treating the plan as broken; on a genuine break, renegotiate cadence downward (e.g., monthly to biweekly) rather than repeating the same ask.

## Worked example: settlement-offer evaluation

An account with a $5,000 balance is 140 days past due, one collector contact attempt succeeded, and the debtor offers a lump-sum settlement of $3,000 today in exchange for the account being marked paid-in-full.

| Option | Recovered amount | Timing | Notes |
|---|---|---|---|
| Accept $3,000 lump sum | $3,000 (60% of balance) | Immediate | Certain recovery, avoids further aging/write-off risk |
| Counter at $3,750 lump sum | $3,750 (75% of balance) if accepted | Immediate if accepted | Reasonable counter given debtor's demonstrated willingness/ability to pay a lump sum at all |
| Decline, pursue full balance via payment plan | Up to $5,000 | 12-24 months, if plan holds | Higher total recovery only if plan completes; late-stage plans have materially lower completion rates than early-stage ones |

A collector authorized to settle within a discount band (commonly 20-40% off balance at this aging stage, per agency policy — verify against the specific authorization on file) would counter rather than accept the first offer outright, since a debtor who can produce $3,000 today has demonstrated more capacity than the opening offer reveals.

## Escalation routing

| Trigger | Route to |
|---|---|
| Formal or informal dispute of the debt amount | Validation/dispute process; pause pressure language pending resolution |
| Identity-theft or "not my debt" claim | Fraud queue; freeze active collection pending FTC/police report |
| Bankruptcy filing mentioned or confirmed | Legal/compliance immediately; automatic stay applies, halt all collection activity |
| Attorney representation stated | All future contact through counsel only |
| Hardship claim (job loss, medical, etc.) | Hardship-program review; do not continue standard payment-plan pressure until reviewed |
| Threat of self-harm or safety concern | Immediate escalation per agency crisis-response protocol, outside normal collection workflow |
