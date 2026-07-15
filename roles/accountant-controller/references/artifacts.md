# Reconciliation & close artifacts

Filled templates a controller actually produces. Real structures with plausible numbers, not descriptions of what to include.

## Month-end close checklist (fixed calendar, day-of-close columns)

| Day | Task | Owner | Sign-off |
|---|---|---|---|
| BD 1 | Cutoff memo distributed (last shipment/receipt date for the period) | Controller | — |
| BD 2 | AP sub-ledger closed, accruals booked for unbilled expenses | AP lead | Controller |
| BD 2 | AR sub-ledger closed, revenue cutoff testing performed | AR lead | Controller |
| BD 3 | Payroll accrual booked (days worked but unpaid at period end) | Payroll | Controller |
| BD 3 | Fixed asset roll-forward updated, depreciation posted | Staff accountant | Controller |
| BD 4 | Bank reconciliations completed for all accounts | Staff accountant | Controller |
| BD 4 | Intercompany balances confirmed and eliminated (if applicable) | Controller | CFO |
| BD 5 | Balance sheet account reconciliations (all accounts) reviewed | Controller | CFO |
| BD 5 | Flux analysis prepared for all P&L lines >5% variance | Staff accountant | Controller |
| BD 6 | Financial statements drafted | Controller | — |
| BD 7 | Management review of draft financials | CFO | — |
| BD 8 | Financials finalized and distributed | Controller | CFO |

A close that consistently lands on BD 8 and starts sliding to BD 12+ is the earliest, cheapest signal something in the process broke — see red-flags.md.

## Materiality worksheet (quantitative screen)

| Base | Value | Common threshold | Materiality cutoff |
|---|---|---|---|
| Pretax income | $900,000 | 5% | $45,000 |
| Total revenue | $12,400,000 | 0.5%–1% | $62,000–$124,000 |
| Total assets | $8,200,000 | 1% | $82,000 |

Rule applied: use the lowest of the relevant bases for a conservative screen, then overlay qualitative factors (related-party, trend-reversing, covenant-affecting, or fraud-indicative items are treated as material regardless of dollar size).

**Example application:** a $52,000 unreconciled AR variance is under the total-assets threshold ($82,000) but over the pretax-income threshold ($45,000) — the more conservative base governs, so it's treated as material and escalated to the CFO before the close finalizes, not resolved quietly at the staff level.

## Flux analysis template (P&L, month-over-month)

| Line | Prior month | Current month | $ variance | % variance | Explanation |
|---|---|---|---|---|---|
| Revenue | $1,020,000 | $1,065,000 | +$45,000 | +4.4% | Two new customer contracts started mid-month; annualizing to ~$540K. |
| COGS | $410,000 | $475,000 | +$65,000 | +15.9% | One-time $52K freight surcharge from a carrier rate change; remainder is volume-driven. |
| Gross margin % | 59.8% | 55.4% | −4.4pt | — | Driven entirely by the freight surcharge above; underlying margin unchanged. |
| G&A | $180,000 | $182,500 | +$2,500 | +1.4% | Normal — within threshold, no explanation required. |

Threshold for requiring a written explanation: any line moving >5% and >$10,000 absolute. Below either bar, no explanation is required — this is what keeps flux analysis from becoming a full narrative every month.

## Bank reconciliation template

| Item | Amount |
|---|---|
| Bank statement balance (3/31) | $1,908,920 |
| + Deposits in transit | $61,300 |
| − Outstanding checks | ($84,200) |
| = Adjusted bank balance | $1,886,020 |
| GL cash balance (3/31, before correction) | $1,845,690 |
| Unreconciled variance | $40,330 |
| Root cause: reverse duplicate AP wire (JE-2026-0347) | +$41,850 |
| Root cause: record unrecorded wire fees (JE-2026-0348) | ($1,520) |
| GL cash balance (3/31, after correction) | $1,886,020 |
| Residual unreconciled amount | $0 |

The template only closes when the residual line is $0 and every reconciling item traces to a named, dated cause — a rec with a residual "plug" line is not a completed reconciliation.

## Allowance for doubtful accounts roll-forward

| | Amount |
|---|---|
| Beginning balance (Jan 1) | $124,000 |
| + Provision for the period | $38,000 |
| − Write-offs | ($22,000) |
| = Ending balance (Mar 31) | $140,000 |
| AR balance (Mar 31) | $2,860,000 |
| Allowance as % of AR | 4.9% |

Re-test annually (minimum) against actual write-off experience: if trailing-12-month write-offs run consistently below the allowance rate, the rate is stale and overstates the reserve; consistently above, it's understated and the P&L provision needs to catch up before year-end, not get caught in a single Q4 true-up.
