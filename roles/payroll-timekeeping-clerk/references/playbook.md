# Payroll and Timekeeping Clerk — Playbook

## Regular-rate-of-pay recalculation worksheet

| Item | Amount |
|---|---|
| Base hourly rate | $18.00 |
| Total hours worked (workweek) | 46 |
| Straight-time hours (≤40) | 40 |
| Overtime hours (>40) | 6 |
| Non-discretionary bonus for this workweek | $150.00 |
| **Step 1** — Total straight-time compensation (all hours × base rate) | 46 × $18.00 = $828.00 |
| **Step 2** — Add non-discretionary bonus | $828.00 + $150.00 = $978.00 |
| **Step 3** — Regular rate of pay | $978.00 ÷ 46 = $21.2609/hr |
| **Step 4** — Overtime premium (extra half-rate on OT hours only) | 0.5 × $21.2609 × 6 = $63.78 |
| **Step 5** — Total correct pay | $978.00 + $63.78 = **$1,041.78** |
| Naive pay (base-rate-only OT, bonus separate) | $720.00 + $162.00 + $150.00 = $1,032.00 |
| **Underpayment if bonus excluded from OT rate** | **$9.78** |

Rule of thumb: any non-discretionary payment (production bonus, shift differential, non-discretionary attendance bonus, commission) tied to a workweek containing overtime hours triggers this recalculation. A discretionary bonus (employer retains sole discretion over amount and payment, not announced in advance per a formula) does not.

## Garnishment priority and CCPA cap worksheet

| Order type | Priority | Typical CCPA cap on disposable earnings |
|---|---|---|
| Federal tax levy | 1st (unless support order pre-dates it) | Set by IRS levy notice, not the general 25% cap |
| Child support (no arrears, not supporting another family) | 1st–2nd | Up to 60% |
| Child support (with 12+ weeks arrears) | 1st–2nd | Up to 65% |
| Bankruptcy court order | Varies by court order | Set by the order |
| Consumer-debt garnishment (credit card, medical debt, etc.) | Last | Lesser of 25% of disposable earnings, or the amount by which disposable earnings exceed 30× federal minimum wage |

**Worked example — two active orders:**

Employee disposable earnings (after mandatory tax/FICA/retirement deductions, before voluntary deductions): $1,200/week.

- Order A: child support, no arrears — cap 60% of disposable earnings = $720.00/week.
- Order B: consumer-debt garnishment, filed later — cap lesser of 25% ($300.00) or (disposable earnings − 30× federal minimum wage of $7.25 = $217.50) → lesser of $300.00 and $982.50 = $300.00/week.

Support order (A) takes priority. Support order actually calls for $500/week; consumer garnishment (B) calls for $300/week. Combined, that's $800/week — still under the higher child-support cap of $720? No: $800 > $720, so combined withholding cannot exceed the *individual employee's* applicable aggregate cap, which for an employee with a support order active is generally the support order's own cap (60%, $720), not a simple sum of both caps. Support order is paid first in full ($500), leaving $220 of headroom under the $720 combined ceiling before the general 25%/$300 rule even applies — so the consumer garnishment (B) can take up to $220/week, not its full $300 request, until the support order's arrears status or amount changes.

Deliverable: garnishment-processing memo to payroll system:

> Order A (child support, [case #]): withhold $500.00/week, effective [date], per court order — no cap issue, well under 60% ceiling.
> Order B (consumer garnishment, [case #]): withhold $220.00/week (not the requested $300.00), capped by combined aggregate limit given Order A's priority. Recalculate if Order A's amount or arrears status changes.

## Off-cycle correction checklist

1. Confirm the error type: underpayment (may trigger a state final-pay-timing requirement) vs. overpayment (generally can wait for next-cycle offset, check state wage-deduction-consent rules first).
2. Recalculate the correct amount using the same regular-rate-of-pay and garnishment-priority worksheets above.
3. Check the applicable state's final-pay or wage-correction-timing statute; if it requires payment sooner than the next regular cycle, initiate an off-cycle manual check.
4. Document the error's root cause (e.g., "non-discretionary bonus excluded from OT calc") — a correction without a documented cause will recur next time the same bonus type appears.
5. Reconcile the correction against the general-ledger payroll expense account before closing the period.
