# Red flags

### Vendor bank/remit-to change with no callback verification
- **Usually means:** business-email-compromise fraud impersonating the vendor, or a legitimate update processed without the control step.
- **First question:** who confirmed this by phone, and using the number already on file — not the number printed on the change request or a linked invoice?
- **Data to pull:** vendor master change log timestamp compared against the next scheduled payment run for that vendor.

### Same-day PO-to-receipt cycle (0-day gap) more than 3 times in a month for one requester
- **Usually means:** paperwork created retroactively for a purchase that already happened informally — maverick spend dressed up as compliant.
- **First question:** who took delivery of the goods or service before the PO existed?
- **Data to pull:** PO creation timestamp versus receiving-document timestamp versus invoice date, for that requester over the trailing 90 days.

### Invoice price variance over 2% or $25 (whichever is greater) versus PO price
- **Usually means:** an unannounced vendor price increase, a wrong catalog price loaded at PO creation, or a new negotiated price the buyer hasn't updated in the system.
- **First question:** is there a signed contract or amendment that already approved this price?
- **Data to pull:** current signed pricing agreement or the most recent contract amendment for that vendor and item.

### Blanket PO drawn down past its elapsed-term share (e.g. 75%+ spent with 25%+ of the term remaining)
- **Usually means:** consumption was under-forecast at PO setup, or the item scope has quietly expanded beyond the original list.
- **First question:** has anything been added to what's being drawn against this PO that wasn't in the original scope?
- **Data to pull:** weekly drawdown trend for the PO versus the elapsed fraction of its term.

### Duplicate invoice number, or invoice amount within 5% of another paid invoice from the same vendor within 90 days
- **Usually means:** accidental duplicate payment risk, or a vendor re-submitting an already-paid invoice under a slightly different number.
- **First question:** does a payment history search on vendor plus amount return a prior match?
- **Data to pull:** AP payment history filtered by vendor and amount range, trailing 90 days.

### Requisition unconverted past 5 business days
- **Usually means:** a missing or invalid budget code, an unclear item specification, or a buyer backlog on the sourcing side.
- **First question:** which of the three is blocking this specific requisition?
- **Data to pull:** requisition queue aging report, sorted by days open.

### New vendor's first invoice arrives before vendor onboarding and the first PO are fully executed
- **Usually means:** the purchase already happened outside policy before the vendor was even set up in the system.
- **First question:** was anything ordered or received before this vendor record existed?
- **Data to pull:** vendor onboarding completion date versus the invoice date and the PO issue date.

### Receiving report quantity exceeds PO quantity by more than 10%
- **Usually means:** an over-shipment accepted at the dock without authorization, or a quantity typo at PO creation that's only now surfacing.
- **First question:** did anyone approve accepting more than what was ordered?
- **Data to pull:** original requisition quantity against the PO quantity against the receiving document quantity.

### Same person both approving and receiving on more than 20% of their own POs
- **Usually means:** a segregation-of-duties gap — one person controls both authorization and the physical/system confirmation of receipt, which is the exact combination the three-way match is designed to prevent.
- **First question:** does the approval matrix actually block this combination, or does it only look blocked?
- **Data to pull:** user role/permission report cross-referenced against the PO approval and receiving logs.

### Freight or handling line item exceeds 15% of the merchandise total with no contract term covering it
- **Usually means:** vendor padding the invoice, or the wrong Incoterm was applied at order entry.
- **First question:** what Incoterm does the signed vendor agreement specify for this shipment type?
- **Data to pull:** the signed vendor agreement's Incoterms clause.
