# Credit Authorizer, Checker, and Clerk — Playbook

## Authorization worksheet (filled example)

| Field | Value |
|---|---|
| Credit limit | $5,000.00 |
| Posted balance | $3,200.00 |
| Pending hold 1 | $450.00 (gas station, day −3) |
| Pending hold 2 | $180.00 (hotel incidentals, day −1) |
| **Available credit** | **$1,170.00** |
| Requested amount | $1,250.00 |
| **Decision** | **Decline — $80.00 short. Offer $1,170.00 partial if merchant supports it.** |

Formula: `Available credit = Limit − Posted balance − Σ(pending holds)`. Always sum every open hold, not just the most recent one — a common miss is checking the newest hold and forgetting an older one is still open.

## Document-verification checklist (new-account application)

| Item | Required source | Status | Note |
|---|---|---|---|
| Identity | Government-issued photo ID matching application name/DOB | ✅ Verified | — |
| SSN/ITIN | Matches credit-bureau file | ✅ Verified | — |
| Stated income | Most recent pay stub, YTD figure annualized | ⚠️ Discrepancy | Stated $62,000/yr; pay stub YTD $18,200 through 14 pay periods (biweekly) annualizes to $33,800 |
| Employment | Employer name/start date matches pay-stub employer | ✅ Verified | — |
| Address | Matches a utility bill or bank statement dated within 60 days | ✅ Verified | — |

**Discrepancy resolution:** stated income ($62,000) vs. verified income ($33,800) is a 45% gap — large enough that this is the finding itself, not a rounding difference. Route: request a stipulation (most recent W-2, or a letter from employer confirming a raise/bonus not yet reflected in pay-stub YTD) before approving at the requested limit. Do not average or split the difference — approve at the verified figure's supportable limit, or hold for stipulation.

## Chargeback/dispute filing-window calculator

| Dispute type | Window start | Window length [heuristic — verify current rule] | Example |
|---|---|---|---|
| Reg E unauthorized electronic transaction | Date of the statement showing the transaction | 60 days | Statement dated May 5 → window closes July 4 |
| Card-network chargeback (goods not received) | Transaction date or expected delivery date | ~120 days (network-specific) | Transaction April 1 → window closes ~July 30 |
| Card-network chargeback (billing error) | Transaction/statement date | ~60–120 days (network- and reason-code-specific) | Varies — check the specific reason code's window before filing |

**Rule:** always compute the window-close date and compare against today's date *before* evaluating the dispute's substance. A dispute filed one day past the window is procedurally dead regardless of the merits — don't spend adjudication effort on it; route it to the "outside window, cannot process" category and communicate that plainly.

## Adverse-action reason-code mapping (excerpt)

| Underwriting rule fired | FCRA/ECOA principal reason to cite |
|---|---|
| Verified income below product's minimum threshold | "Income insufficient for amount requested" |
| Credit-bureau score below cutoff | "Insufficient credit score" (cite the specific score and the top factors from the bureau report, per FCRA disclosure requirement) |
| Debt-to-income ratio above threshold | "Excessive obligations in relation to income" |
| Insufficient credit history/length | "Limited credit history" |

Never substitute "does not meet our lending criteria" for the specific reason above — the specific reason is what the notice legally requires, and it's also the reason the applicant can actually act on (pay down debt, wait for credit history to build) rather than a dead end.
