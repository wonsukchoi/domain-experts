# Procurement Clerk — Red Flags

### Invoice total matches PO total but quantity received doesn't match PO quantity
- **Usually means:** a short shipment, damaged/refused goods, or a partial delivery being billed as if complete.
- **First question:** does the receiving report quantity match the invoice quantity, independent of whether the dollar totals happen to match?
- **Data to pull:** receiving report, PO, invoice line-item detail.

### Vendor-banking-detail change request arrives via email with urgency language
- **Usually means:** most often legitimate, but this exact pattern is the leading vector for business-email-compromise payment-redirection fraud.
- **First question:** can this be verified through a phone number sourced independently of the email itself?
- **Data to pull:** existing vendor-file contact information, prior correspondence history with this vendor.

### New vendor added and first invoice paid within the same week
- **Usually means:** could be a legitimate fast-onboarding need, but also matches the pattern of a fictitious-vendor scheme designed to move quickly before controls catch up.
- **First question:** is there a signed vendor agreement/W-9 on file, and was the new-vendor addition independently approved by someone other than the requester?
- **Data to pull:** vendor-onboarding approval record, W-9/agreement, requester's approval authority level.

### Same vendor generates repeated three-way-match exceptions
- **Usually means:** either a systemic pricing/quantity-communication problem with that vendor, or a deliberate pattern of over-billing that individual exceptions don't reveal in isolation.
- **First question:** what's the exception rate for this vendor compared to the average vendor over the same period?
- **Data to pull:** exception log filtered by vendor, trend over the last 6-12 months.

### Blanket PO balance depletes far faster than the elapsed period percentage
- **Usually means:** either usage is legitimately front-loaded (seasonal demand), or purchases are being made outside the original scope/intent of the blanket PO.
- **First question:** does the spend pattern match a known seasonal or project-driven reason?
- **Data to pull:** blanket-PO release history by date and requester, original PO scope/justification.

### Requisition approved at a dollar amount just below an approval-tier threshold
- **Usually means:** could be coincidental, but repeated instances just under a threshold suggest deliberate structuring to avoid a higher approval level.
- **First question:** does this requester have a pattern of requisitions clustering just under approval thresholds?
- **Data to pull:** requisition history for the requester, approval-tier policy thresholds.

### Receiving report is entered with no corresponding physical count discrepancy ever noted, across a high-volume period
- **Usually means:** possibly a genuinely accurate receiving process, but also a pattern consistent with receiving reports being entered without an actual physical count (rubber-stamping).
- **First question:** is there a sampling/audit process confirming receiving reports reflect actual counts, not just PO quantities copied over?
- **Data to pull:** receiving-report entry timestamps versus delivery timestamps, periodic physical-count audit results.
