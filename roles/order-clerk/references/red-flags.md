# Order Clerk — Red Flags

### Bare quantity with no unit stated, on a SKU the customer hasn't ordered before
- **Usually means:** the customer is assuming a unit (each, case, box) that may not match the system's default order unit for that SKU.
- **First question:** what unit did they mean, and does it match what the price list assumes?
- **Data to pull:** the SKU's order-UOM configuration and, if available, this customer's order history for similar items.

### Order total that doesn't match a rough mental estimate of quantity × unit price
- **Usually means:** a price-tier misapplication, a unit-of-measure error, or a stale price on the order.
- **First question:** which of the three (tier, unit, price-list currency) is off?
- **Data to pull:** the current price list and the pricing-policy note for the account (order-total vs. per-shipment tiering).

### SKU number and item description on the same line don't match
- **Usually means:** a transposed digit in a hand-keyed or verbally-given part number.
- **First question:** does the description match exactly one catalog item?
- **Data to pull:** a description-based catalog search; if ambiguous, contact the customer before entering.

### Order quantity exceeds on-hand inventory by more than the standard reorder lead time can cover before a stated deadline
- **Usually means:** a straight backorder won't meet the customer's need date; substitution or partial-ship needs to be offered now, not discovered at pick time.
- **First question:** is there a compatible substitute with sufficient stock?
- **Data to pull:** ATP report filtered to the deadline date, and the substitution cross-reference table for the SKU.

### Change or cancellation request arrives after the order's pick-ticket has printed
- **Usually means:** the order is already in the fulfillment pipeline; a "simple" change may require pulling it back from the warehouse floor.
- **First question:** has picking physically started, or just been queued?
- **Data to pull:** the order's current fulfillment-status flag in the system, not just its entry timestamp.

### Customer quotes a unit price that doesn't match the current price list
- **Usually means:** they're working from a stale price sheet, a verbal quote from a sales rep that was never entered as a contract price, or a promotional price that's expired.
- **First question:** is there a documented special price on file for this account/SKU combination?
- **Data to pull:** the account's contract-pricing table, if one exists, before assuming the customer is simply wrong.

### Order is for an unusually large quantity relative to the account's typical order size
- **Usually means:** either a legitimate large project, a fat-finger quantity entry error, or a misunderstanding of the order unit.
- **First question:** does the account's order history support an order this size, or is this a 10x-plus jump?
- **Data to pull:** the account's trailing 12-month order-size distribution.

### EDI-received order fails a line-item validation (unrecognized SKU, quantity of zero, missing unit)
- **Usually means:** a data-mapping error on the customer's side, not a real order intent problem.
- **First question:** is this a known mapping issue with this trading partner, or a new failure?
- **Data to pull:** the EDI error log and the trading-partner's item cross-reference file.

### Customer disputes an invoiced price after the order shipped
- **Usually means:** the tier-application policy (order-total vs. per-shipment) wasn't applied the way the customer expected, or wasn't communicated at order time.
- **First question:** was the pricing policy stated on the original confirmation?
- **Data to pull:** the original order confirmation and the account's pricing-policy terms.
