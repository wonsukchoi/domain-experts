# Procurement Clerk — Playbook

## Three-way-match worked table

PO #4471: 500 units × $97.00 = $48,500.00

| Document | Quantity | Unit price | Total | Status |
|---|---|---|---|---|
| Purchase Order | 500 | $97.00 | $48,500.00 | Authorized |
| Receiving Report | 485 (15 refused, damaged) | — | — | Variance: -15 units |
| Invoice | 500 | $97.00 | $48,500.00 | **Mismatch vs. receiving** |
| Correct payable | 485 | $97.00 | $47,045.00 | Hold invoice, request correction |

Variance: $48,500.00 − $47,045.00 = $1,455.00 (value of refused units) — do not release payment until either a corrected invoice or a resolution (replacement/credit) for the 15-unit shortage is documented.

## Vendor-master-file change-verification checklist

Before processing any change to a vendor's payment details, address, or new-vendor setup:

- [ ] Request received through a standard channel (not solely an email reply to an unsolicited message)
- [ ] Requester identity confirmed via a known, independently sourced contact method (phone number from the existing vendor file or a company directory — not a number supplied in the change request itself)
- [ ] Change matches a documented business reason (bank switch, address move, new vendor onboarding with a signed W-9/agreement on file)
- [ ] For banking-detail changes specifically: confirmation call placed to the vendor's previously verified contact before the change takes effect
- [ ] Change logged with date, requester, verifier, and verification method for audit trail

Urgency in the request ("needed today," "shipment on hold") is not a reason to skip verification — it's a common social-engineering lever specifically because it pressures skipping this checklist.

## Blanket-PO balance-tracking worksheet

| Blanket PO | Ceiling | Period | Elapsed % of period | Spent to date | % of ceiling spent | Flag? |
|---|---|---|---|---|---|---|
| #BPO-2201 | $250,000 | 12 months | 75% (9 of 12 months) | $228,000 | 91.2% | Yes — pace suggests early exhaustion, flag to purchasing agent |
| #BPO-2202 | $100,000 | 12 months | 75% | $41,000 | 41.0% | No — under-pace is normal if usage is seasonal, confirm with requester before flagging |

Flag when spent-percentage significantly exceeds elapsed-percentage (early-exhaustion risk) or significantly trails it near period-end (potential use-it-or-lose-it pressure or a requirement that changed) — either direction is worth a check-in with the purchasing agent, not a unilateral clerk decision to block or accelerate releases.
