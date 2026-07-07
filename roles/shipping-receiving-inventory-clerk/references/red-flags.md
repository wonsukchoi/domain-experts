# Shipping, Receiving, and Inventory Clerk — Red Flags

### Received quantity differs from packing slip by more than the vendor's stated case-pack tolerance
- **Usually means:** a genuine short-ship or over-ship, not a counting error — case-pack tolerances (commonly ±1 unit per case-lot) exist precisely to absorb normal packing variance, so anything outside that band is a real discrepancy.
- **First question:** does the packing slip quantity match the PO quantity? If not, the discrepancy may originate at the vendor's order-entry, not the physical shipment.
- **Data to pull:** the PO, the packing slip, and the vendor's stated case-pack tolerance policy if one exists.

### Packing slip and PO disagree on item, quantity, or price and the goods have already been received
- **Usually means:** either a PO revision the vendor didn't get, or the vendor shipped against a stale or wrong PO number.
- **First question:** is there a more recent PO revision that supersedes the one on file?
- **Data to pull:** PO revision history, vendor order-confirmation email if one exists.

### Two consecutive cycle counts on the same SKU show unexplained variance
- **Usually means:** a recurring process problem (mislabeled bin, a picker consistently missing a scan step) rather than random counting error — random error doesn't repeat in the same direction twice.
- **First question:** is there an adjacent SKU with an offsetting variance suggesting a location swap?
- **Data to pull:** transaction history for both counts, bin-location map for adjacent SKUs.

### Cycle-count variance exceeds 2% of the SKU's on-hand quantity
- **Usually means:** worth escalating beyond a routine recount — small percentage variances are often transaction-timing noise, but anything above roughly 2% (a stated operational heuristic, not a fixed rule) is large enough to warrant checking for an unposted transaction or a genuine loss before adjusting.
- **First question:** does the transaction log for the count period reconcile the starting count to the system's current count?
- **Data to pull:** 30-day transaction history for the SKU, adjacent-location counts.

### A put-away task is completed but the receiving discrepancy record for that shipment is still open
- **Usually means:** disputed or unverified stock got shelved and mixed with good inventory before the discrepancy was resolved — this is the single most expensive failure mode in this role, since isolating the bad units after mixing requires a full bin recount.
- **First question:** which specific units from the disputed receipt were put away, and can they still be identified (lot number, receipt date) within the bin?
- **Data to pull:** put-away transaction log, receiving discrepancy record, lot/batch tracking if available.

### An outbound pick doesn't match the pick-list quantity and packing proceeds anyway
- **Usually means:** a substitution or a miscount is about to become a customer-facing shipping error.
- **First question:** was the pick discrepancy caught before or after the carton was sealed and labeled?
- **Data to pull:** pick list, order detail, packed-carton contents if still accessible.

### A shipment is quarantined for more than the facility's stated resolution window (commonly 3-5 business days) with no purchasing follow-up
- **Usually means:** the discrepancy report went to purchasing but didn't get prioritized — quarantined stock ties up dock/shelf space and delays the underlying order.
- **First question:** was the discrepancy report actually routed, or did it stall at the receiving desk?
- **Data to pull:** discrepancy-report timestamp and routing log.

### A SKU location holds two visually similar items (same box size, sequential part numbers, same color packaging)
- **Usually means:** elevated risk of a location swap during a rushed put-away or pick — this is a leading indicator to watch, not itself an error.
- **First question:** do the bin labels clearly distinguish the two SKUs, or only the smallest-print part number?
- **Data to pull:** bin-location map, put-away/pick error history for both SKUs.

### Physical inventory (annual/periodic full count) turns up a large variance on a SKU that passed its last cycle count clean
- **Usually means:** either the cycle count missed a location (partial-case, secondary bin) or a high-volume transaction period between counts wasn't adequately sampled.
- **First question:** how many locations does this SKU occupy, and were all of them included in the cycle count?
- **Data to pull:** full location list for the SKU, cycle-count scope documentation for the missed period.
