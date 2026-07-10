# Vocabulary

### Three-way match
Reconciliation of the purchase order, the receiving report, and the invoice before payment releases.
**In use:** "Invoice's on hold — PO says 200 units, receiving only logged 180, so it fails three-way match until warehouse confirms the short-ship."
**Common misuse:** Treating it as a two-document comparison (PO vs. invoice) and skipping the receiving report — which defeats the control, since it means paying for something no one independently confirmed arrived.

### Blanket PO
A standing purchase order with a dollar ceiling and a term, drawn down incrementally through releases rather than issued as a single one-time buy.
**In use:** "We've got $8,800 left on the Q3 MRO blanket, but at this burn rate it won't make it to week 13."
**Common misuse:** Reading the remaining balance as free money available on demand, instead of a shrinking ceiling that needs its drawdown rate tracked against the term remaining.

### Maverick spend
Purchases made outside the approved contract, vendor list, or PO process.
**In use:** "That's maverick spend — right vendor, but nobody cut a PO before the goods shipped."
**Common misuse:** Assuming it only applies to buying from an unapproved vendor; it equally covers buying from the *right* vendor through the *wrong* process, like skipping the PO step entirely.

### Match tolerance
The pre-set variance band (a percentage, a flat amount, or both) within which a PO-to-invoice difference auto-clears instead of triggering a hold.
**In use:** "Tolerance here is 2% or $25, whichever's bigger — this is 1.8%, let it through."
**Common misuse:** Treating the tolerance as a target to negotiate up to, rather than an exception threshold — which lets genuine small-but-real variances ride right at the edge of the band undetected.

### Remit-to address
The specific address or bank account payment is actually routed to, which may differ from the vendor's general business address.
**In use:** "The invoice header address is unchanged, but the remit-to on file just switched — that's the one that needs a callback."
**Common misuse:** Conflating it with the vendor's mailing or headquarters address; fraud specifically targets the remit-to field precisely because it's the one most people don't think to separately verify.

### Requisition
An internal request to purchase something, submitted before any vendor commitment exists.
**In use:** "The requisition's been sitting three days — still needs a budget code before I can cut the PO."
**Common misuse:** Using "requisition" and "PO" interchangeably; the distinction matters because a requisition creates no vendor-facing obligation, while a PO does.

### Receiving report (goods receipt)
The documented, independent confirmation that ordered goods or services actually arrived, distinct from the PO and the invoice.
**In use:** "Goods receipt logged 180 units against a 200-unit PO — that's the short-ship the invoice hold is about."
**Common misuse:** Recording it straight off a packing slip without physical or verbal confirmation, which collapses the "independent" part of the check the three-way match relies on.

### Debit memo
A deduction a buyer-side clerk initiates against a vendor's account for a shortage, return, or overcharge, rather than waiting for the vendor to issue a credit memo.
**In use:** "Vendor short-shipped 20 units — cutting a debit memo for the difference instead of waiting on their credit memo."
**Common misuse:** Assuming only the vendor can adjust the balance via a credit memo, missing that the buyer's side can initiate the deduction directly.

### Segregation of duties (SoD)
The control principle that no single person can complete requisition, approval, receiving, and payment authorization alone.
**In use:** "SoD flags this — same person requested and received against their own PO."
**Common misuse:** Treating it as satisfied by "two signatures" on a document, without checking whether the specific role combination (e.g. approver who is also the receiver) still violates the principle.

### Price variance vs. quantity variance
Two distinct categories of match failure that route to different owners — price variance to the buyer, quantity variance to receiving or the warehouse.
**In use:** "That's a price variance, route it to the buyer — the quantity already ties out fine."
**Common misuse:** Bucketing every mismatch as a generic "doesn't match the PO" exception, losing the routing distinction that determines who actually needs to resolve it.

### Incoterms / freight terms
Contract terms fixing who owns and pays for goods at each point in transit.
**In use:** "Freight's 18% of the merchandise total, but our signed terms are FOB origin — that shouldn't be on this invoice at all."
**Common misuse:** Treating the freight charge as negotiable line-item detail at invoice time, when it's actually fixed by whatever Incoterm the signed vendor agreement specifies.
