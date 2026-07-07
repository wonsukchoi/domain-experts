# Teller — Playbook

## CTR filing trigger table

| Scenario | Aggregate cash that business day | CTR required? |
|---|---|---|
| Single withdrawal | $8,500 | No |
| Single withdrawal | $10,500 | Yes |
| Two withdrawals, same customer, same day, different windows | $6,000 + $5,000 = $11,000 | Yes — aggregate across the day, not per-transaction |
| Two withdrawals, same customer, two consecutive days | $9,500 + $9,500 | No CTR per day, but pattern is a structuring red flag — escalate |
| Cash deposit + cash withdrawal, same customer, same day | $6,000 deposit + $5,000 withdrawal | No — CTR aggregates cash-in and cash-out separately, not combined |

CTRs are filed by the bank's BSA/AML team, not the teller directly — the teller's job is flagging the aggregate-threshold event and forwarding transaction details, generally within the institution's same-day or next-day internal deadline (FinCEN's external filing deadline is 15 days from the transaction).

## Regulation CC hold-schedule reference

| Deposit category | Standard availability |
|---|---|
| Cash | Next business day |
| Wire transfer | Next business day |
| U.S. Treasury check (payee = depositor) | Next business day |
| State/local government check (payee = depositor, in-person deposit) | Next business day |
| Cashier's/certified/teller's check (payee = depositor, in-person deposit) | Next business day |
| Local check (same Federal Reserve check-processing region) | 2nd business day |
| Non-local check | 2nd business day (institutions may extend to 5th under some circumstances) |
| New account (open <30 days), deposits over $5,525 | Standard schedule for first $5,525; longer hold (up to 7 business days) permitted on the excess |
| Reasonable-cause exception (suspected fraud, redeposited check, repeated overdrafts) | Extended hold, must be documented and disclosed to customer with reason |

The first $225 of most check deposits must be available the next business day even when a longer hold applies to the rest.

## End-of-shift drawer-balancing procedure

1. Count physical cash by denomination; total it.
2. Pull the system-generated transaction log for the shift; total the net cash in/out.
3. Compare: physical count vs. (starting drawer balance + logged cash in − logged cash out).
4. If variance is $0: log balanced, done.
5. If variance is nonzero: sort the shift's transactions by dollar size descending; re-verify the top transactions (typically anything over a branch-set materiality threshold, e.g. $500) by comparing the physical transaction slip to the logged amount.
6. Trace the variance to a specific transaction where possible. If found, correct the underlying transaction (not just the drawer log) and notify the affected customer if they were shorted or overpaid.
7. If untraceable after re-verification, log as an unexplained variance with the shift's transaction count and total volume for context, and route to the branch manager per policy (many branches require manager notification above a set dollar threshold, e.g. $50).

## Filled fraud/compliance escalation worksheet

**Transaction:** Cash withdrawal request, $9,200, account ending 8823
**Date/time:** [date], 11:40 AM
**Teller observation:** Same account holder withdrew $9,000 in cash yesterday at 4:15 PM (different teller, same branch — visible in same-day/prior-day cross-lookup).
**Pattern match:** Two consecutive-day withdrawals just under $10,000, no other transaction activity from this account in the prior 90 days.
**Action taken:** Processed the withdrawal (legal transaction, correctly identified customer, no basis to refuse) and routed the pattern to the BSA/AML officer same day via internal escalation form.
**Escalation note to BSA/AML officer:**
> Account 8823: $9,000 cash withdrawal [date-1] 4:15 PM, $9,200 cash withdrawal [date] 11:40 AM. No prior cash-transaction activity in 90-day lookback. Pattern consistent with structuring (consecutive near-threshold withdrawals). Transactions processed as legally required; flagging for SAR review.
