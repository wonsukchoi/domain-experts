# Playbook

## Requisition-to-PO conversion checklist

Filled example for requisition R-33456 (gasket assortment, $6,300, requested by J. Alvarez, Maintenance):

| Check | Requirement | This requisition |
|---|---|---|
| Budget code valid | Code exists and has remaining balance this fiscal quarter | `MRO-4410` — valid, $8,800 remaining before this draw |
| Requester authorization limit | Requester's approval tier covers the amount | Alvarez tier-2 limit: $10,000 — covers $6,300 |
| Existing agreement coverage | Item is on an active blanket PO or contract | Yes — Blanket PO 4500-1187, MRO supplies, FY26 Q3 |
| Spec clarity | Item, quantity, unit of measure unambiguous | "Gasket assortment kit, 1 ea, per attached spec sheet" — clear |
| Delivery need-by date present | A date exists, not "ASAP" | 14 calendar days from release |

Outcome: covered by an existing blanket PO, so this becomes a **release** against 4500-1187, not a new PO — but see the drawdown tracker below before releasing.

## Match tolerance table

| Variance type | Tolerance | Action within tolerance | Action outside tolerance |
|---|---|---|---|
| Unit price | ≤2% or $25, whichever is greater | Auto-approve | Hold, route to buyer with PO price vs. invoice price and the delta |
| Quantity (invoice vs. receiving report) | ≤1 unit or 1%, whichever is greater | Auto-approve | Hold, route to receiving/warehouse to confirm actual count |
| Freight/handling | Must match signed Incoterm; no tolerance band — either it's chargeable per contract or it isn't | Approve if contract confirms buyer pays this leg | Hold, pull signed Incoterms clause before approving |
| New vendor (first 90 days) | No tolerance — hold regardless of size | N/A | Verify vendor onboarding is complete before releasing payment |

Example match run for invoice INV-88213 against PO 4500-1187-R7:

- PO unit price: $42.00/unit × 150 units = $6,300.00
- Invoice unit price: $42.75/unit × 150 units = $6,412.50
- Variance: $112.50, or 1.79% of the PO total
- Applicable tolerance: 2% of $6,300 = $126.00, versus the flat $25 floor — the greater of the two is $126.00
- $112.50 < $126.00 → within tolerance → auto-approve

## Blanket PO drawdown tracker

Filled example, Blanket PO 4500-1187 (MRO supplies, FY26 Q3, 13-week term, $50,000 ceiling):

| Week | Cumulative draws | Elapsed term share | Draw share | Flag? |
|---|---|---|---|---|
| 3 | $9,800 | 23.1% | 19.6% | No — draw share below term share |
| 6 | $24,500 | 46.2% | 49.0% | No — within a few points of pace |
| 9 | $41,200 | 69.2% | 82.4% | **Yes** — draw share exceeds term share by 13.2 points; projected total at current rate is $59,511 (19.0% over ceiling) |

Rule of thumb applied here: flag when cumulative draw share exceeds elapsed term share by more than 10 percentage points. At week 9, that gap is 13.2 points — over the line, which is what drove the escalation memo in SKILL.md's worked example.

## Vendor bank-detail change verification script

Used any time a vendor's remit-to address or bank routing/account number changes on an existing vendor master record.

1. **Do not process any pending payment to this vendor until verification completes.**
2. Pull the phone number on file from the vendor master record *as it existed before this change request* — never the number listed on the change request itself, and never a number provided in the same email thread.
3. Call that number and ask for accounts receivable or the vendor's finance contact by name (from the existing record, if known).
4. Confirm verbally: "Can you confirm you submitted a change to your remit-to bank details on [date], for an account ending in [last 4 digits]?"
5. If confirmed: log the callback (date, time, name, method) in the vendor master change log, then release the change.
6. If not confirmed, or the vendor has no record of the request: do not release the change or any pending payment; escalate immediately to the procurement supervisor and flag as suspected fraud.
7. Regardless of outcome, hold any payment already in the run for this vendor until the callback resolves — don't let a payment batch execute while verification is pending.
