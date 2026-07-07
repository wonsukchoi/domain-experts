# Procurement Clerk — Vocabulary

### Three-way match
The control process of comparing a purchase order, a receiving report, and a vendor invoice to confirm quantity and price agree across all three before releasing payment.
**In use:** "The three-way match caught it — invoice billed for 500 units but receiving only shows 485 received."
**Common misuse:** Treated as complete when only two of three documents are checked (commonly PO-to-invoice, skipping the receiving report), which misses exactly the discrepancy type — under-delivery billed as full delivery — the third check exists to catch.

### Blanket purchase order
A single PO authorizing multiple releases/purchases from a vendor up to a ceiling amount over a defined period, rather than issuing a new PO for every transaction.
**In use:** "We're at 91% of the blanket PO's ceiling with three months left in the period — flag it before we hit an unauthorized-overspend situation."
**Common misuse:** Treated as a spending target to hit rather than a ceiling not to exceed, leading to either premature exhaustion or unnecessary purchases to "use up" the remaining balance.

### Vendor master file
The system record of a vendor's identifying, banking, and contact information used to process payments to them.
**In use:** "Any change to the vendor master file's banking details needs an independent verification call before it takes effect."
**Common misuse:** Treated as routine data maintenance rather than a fraud-control point — it's one of the highest-value targets for payment-redirection schemes precisely because a small, quiet change there redirects every future payment.

### Receiving report / receiving exception
The document recording what was actually received against a PO, including any variance (shortage, overage, damage) from what was ordered.
**In use:** "The receiving exception notes 15 units refused for damage — that's why the invoice quantity doesn't match."
**Common misuse:** Entered as a copy of the PO quantity without an actual physical count, which defeats its purpose as an independent check in the three-way match.

### Requisition
An internal request to purchase goods or services, requiring approval before being converted into a purchase order.
**In use:** "The requisition was approved at the department-manager level — that's the right tier for this dollar amount."
**Common misuse:** Confused with the PO itself; a requisition is the internal ask, the PO is the external commitment to a vendor — a requisition without matching approval authority shouldn't become a PO.

### Fictitious-vendor scheme
A fraud pattern where a nonexistent or shell vendor is added to the vendor master file and invoiced against, diverting payments to the fraudster.
**In use:** "New-vendor additions get a second independent approval specifically to guard against a fictitious-vendor scheme."
**Common misuse:** Assumed to require an outside hacker — the majority of documented cases involve an insider with vendor-master-file access exploiting weak separation-of-duties controls.

### Payment tolerance
A small, policy-defined acceptable variance (dollar amount or percentage) between matched documents that doesn't block automatic payment release.
**In use:** "This invoice is $4.50 over the PO due to a rounding difference — that's within our $10 tolerance, release it."
**Common misuse:** Set too loosely, turning the three-way match into a rubber stamp for any variance under a large tolerance band rather than catching genuine discrepancies.

### Structuring (requisition-level)
Deliberately splitting a purchase or setting a requisition amount just under an approval-tier threshold to avoid a higher level of required approval.
**In use:** "Three requisitions from the same requester, each $50 under the $5,000 approval threshold, in the same week — that pattern needs a look."
**Common misuse:** Dismissed as coincidence on a single instance rather than tracked as a pattern across a requester's history, where repetition is the actual signal.
