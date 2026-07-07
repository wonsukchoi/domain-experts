# Brokerage Clerk — Red Flags

### Trade break over $500 still open at T+1 minus one hour
- **Usually means:** the weighted-average price hasn't been recomputed from raw fill tickets yet, or this is a genuine erroneous execution rather than a booking error.
- **First question:** has anyone recomputed the price from the underlying fills, or has the comparison only been done at the total-dollar level?
- **Data to pull:** fill-ticket blotter, contra broker's confirmation.

### DK notice with no matching internal order
- **Usually means:** the order was never transmitted, was booked to the wrong account, or belongs to a different desk internally.
- **First question:** does the order management system show this trade at all, under any account?
- **Data to pull:** OMS order log filtered by security and approximate execution time.

### Position reconciles in share count but not in cost basis after a corporate action
- **Usually means:** the split/spin-off ratio was applied to share count but not cost basis, or vice versa — a partial adjustment.
- **First question:** was the adjustment entered as one atomic update or as two separate entries that could have been applied inconsistently?
- **Data to pull:** corporate-action notice, cost-basis ledger before and after the action date.

### Same account throws a break on the same field type multiple days running
- **Usually means:** a systemic feed or static-data issue (wrong account mapping, stale settlement instructions) rather than a series of independent one-off errors.
- **First question:** is the same field breaking every time, or is it a coincidence of unrelated errors?
- **Data to pull:** prior five days' exception log for that account.

### Break amount is a round number ($100, $250, $500)
- **Usually means:** someone previously booked a manual plug to force reconciliation instead of identifying the actual discrepancy.
- **First question:** who booked the prior entry, and what source did they cite?
- **Data to pull:** adjustment audit trail with entry timestamps and authoring clerk.

### Settlement date falls on a day the security is halted or the exchange is closed
- **Usually means:** the settlement calendar used by the booking system wasn't updated for a listing-exchange holiday or trading halt.
- **First question:** is the settlement calendar current for this security's specific listing exchange, not just the general market calendar?
- **Data to pull:** exchange holiday and halt calendar for the relevant listing venue.

### Fractional share from a corporate action shows as an open position, not cashed out
- **Usually means:** the cash-in-lieu processing step specified in the corporate-action terms was skipped.
- **First question:** do the official corporate-action terms call for cash-in-lieu, or for rounding without cash settlement?
- **Data to pull:** the issuer/DTCC corporate-action notice's fractional-share terms.

### Client inquiry about a position that doesn't match their confirmation
- **Usually means:** a correction was booked after the original confirmation was sent and the client wasn't separately notified — or the client's copy is stale.
- **First question:** what is the timestamp of the last correction relative to the client's confirmation date?
- **Data to pull:** correction audit trail and the original trade confirmation sent to the client.

### Sum of partial fills doesn't equal the original order quantity
- **Usually means:** a fill was missed in the booking, or the order was amended after the initial ticket was cut.
- **First question:** does the fill-ticket total match the order ticket exactly, share for share?
- **Data to pull:** original order ticket and every fill confirmation for that order ID.

### Break persists after recomputation and the contra side still disagrees
- **Usually means:** this is a genuine erroneous trade requiring a formal cancel/correct, not a clerical fix that more adjustment entries will resolve.
- **First question:** has this been escalated to the trading desk as a specific erroneous-trade claim, with both sides' recomputed figures attached?
- **Data to pull:** trade cancel/correct request form and both parties' fill-ticket-level data.
