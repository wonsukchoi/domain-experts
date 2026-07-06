# Red flags — what a purchasing agent checks reflexively

Smell tests with thresholds. Any one can be innocent; two or three together on the same requisition is a pattern worth escalating even below a mandatory referral trigger.

### Same vendor, two or more invoices in the same 5 business days, summing above the card single-transaction limit
- **Usually means:** a split purchase engineered (or backed into unintentionally) to keep each transaction under the P-card cap, rather than one requisition routed through the proper threshold.
- **First question:** "Why weren't these combined into a single PO before purchase?"
- **Data to pull:** P-card statement filtered by vendor and cardholder for the billing cycle, requisition history for the same vendor/department in the prior 30 days.

### Requisition cover note says "sole source" with no competing quotes attached and spend over $10,000
- **Usually means:** vendor familiarity or standardization preference dressed up as one of the four valid 2 CFR 200 conditions, when no genuine attempt to solicit alternatives occurred.
- **First question:** "Which of the four sole-source conditions applies here, specifically?"
- **Data to pull:** sole-source justification memo, market-research or vendor-search log (if any), prior awards to this vendor for the same category.

### PO issued citing a master agreement or contract number with no separate release or line-item authorization
- **Usually means:** the SKILL.md First-principles #2 error in the wild — contract-as-authorization instead of an instrument that actually obligates funds.
- **First question:** "Is this PO drawing against an active blanket release, or is the contract itself being treated as the authorization?"
- **Data to pull:** the master agreement's release mechanism clause, current blanket PO balance and expiration, this PO's line-item detail.

### Invoice quantity or unit price differs from the PO by any amount and payment is due within 3 days
- **Usually means:** AP is under deadline pressure to clear the payment cycle — the three-way-match hold discipline from SKILL.md's Mental models failing under a deadline.
- **First question:** "Has this mismatch been traced to receiving, pricing, or a data-entry error before we pay it?"
- **Data to pull:** PO line items, receiving report, vendor invoice, side-by-side field comparison (quantity, unit price, PO reference number).

### Procurement method selected is RFQ (price-only) for a purchase with no fixed spec sheet
- **Usually means:** the buyer defaulted to the faster instrument without confirming the requirement is standardized enough for price to be the sole deciding factor, likely to produce quotes that aren't comparable.
- **First question:** "Is the spec fixed enough that three vendors would quote on the identical item, or does this need an RFP?"
- **Data to pull:** the requisition's spec sheet or statement of work, comparable past buys in this category and which instrument they used.

### Cumulative departmental spend with one vendor crosses the simplified-acquisition or organizational competitive-bid threshold mid-fiscal-year with no aggregate tracking
- **Usually means:** individual POs were each authorized correctly on their own, but nobody rolled up the running total against the vendor, so the threshold was crossed without triggering the required competitive process.
- **First question:** "What's this vendor's year-to-date cumulative spend across all departments, not just this PO?"
- **Data to pull:** vendor-level spend report across all cost centers for the fiscal year, threshold table currently in effect.

### Requisition references a "qualified purchasing agent" no-bid exemption without confirming the approver's designation status
- **Usually means:** the First-principles #3 error — an elevated no-bid authority assumed from informal seniority or role title rather than an actual statutory appointment.
- **First question:** "Is the approving agent formally designated under this jurisdiction's statute, or assumed to be?"
- **Data to pull:** the jurisdiction's qualified-purchasing-agent designation record, the specific statute's threshold for the exemption.

### Off-contract (maverick) spend in a category exceeds roughly 20% of that category's total volume this quarter
- **Usually means:** a negotiated contract exists but isn't being used as the default purchasing path, either because it isn't visible to requesters or because a preferred non-contract vendor is being routed around it.
- **First question:** "Why are requisitions in this category not defaulting to the negotiated contract vendor?"
- **Data to pull:** category-level contract-compliance report (on-contract vs. off-contract spend), list of non-contract vendors used and requester justification if any.

### Vendor invoice unit price exceeds the negotiated contract rate by any margin, on a contract PO
- **Usually means:** a price increase was applied by the vendor without a corresponding contract amendment, or the wrong price list/version was used when cutting the PO.
- **First question:** "Does the vendor's invoiced rate match the currently executed contract amendment, or an earlier one?"
- **Data to pull:** current contract pricing schedule with amendment history, PO unit price, invoice unit price.

### Gift, meal, or event invitation from a vendor arrives while their quote is under active evaluation
- **Usually means:** the appearance-of-influence standard (Mental models bullet 6) is triggered here regardless of whether the buyer's judgment actually changed.
- **First question:** "Would a reasonable outside observer see this as capable of influencing the award, regardless of intent?"
- **Data to pull:** organization's gift/ethics policy threshold, timing of the gift relative to the RFQ/RFP evaluation window, current status of that vendor's bid.

### Sole-source cost/price analysis missing on a requisition above the organization's own trigger dollar amount
- **Usually means:** the buyer applied a remembered threshold from a different funding source or a prior policy version instead of checking the one that governs this purchase's actual funding source.
- **First question:** "Which policy's trigger amount governs this requisition's funding source, and is this figure current?"
- **Data to pull:** current organizational procurement policy threshold table, funding source designation on the requisition (federal grant vs. general fund vs. other).

### Receiving report logged but no corresponding invoice after 45+ days
- **Usually means:** either the vendor hasn't billed yet (routine) or goods were received against a PO that's since been closed or modified, leaving an open obligation nobody is tracking toward resolution.
- **First question:** "Is this PO still open, and has the vendor been contacted about the missing invoice?"
- **Data to pull:** PO status (open/closed) in the ERP, receiving report date, vendor billing history and standard invoice lag for this vendor.
