# Brokerage Clerk — Vocabulary

### Trade break
Any mismatch between the two sides of a trade — in share quantity, price, settlement date, or account — discovered during the affirmation/matching process before settlement.
**In use:** "We've got a break on the MNO trade — quantity matches but the price is off by two cents a share."
**Common misuse:** Treated as a single undifferentiated category. A quantity break, a price break, and a settlement-date break have different likely causes and different resolution paths — lumping them together delays triage.

### DK (Don't-Know)
A notice from a contra broker stating they have no record of a trade you're claiming was executed with them — not a rejection of a trade they acknowledge but disagree with.
**In use:** "We got a DK from the contra desk on that RST trade — they're saying they never saw the order."
**Common misuse:** Confused with a routine unmatched or rejected trade. A DK specifically means the counterparty has zero record, which points toward a misrouting or fabrication issue, not a data-entry mismatch.

### Affirmation
The formal process (via DTCC's CTM or similar platform) where both sides of a trade confirm that the trade details agree, ahead of settlement.
**In use:** "That trade's still unaffirmed — we can't count on it settling on time until CTM shows a match."
**Common misuse:** Treated as automatic. Affirmation is a status that has to be actively reached; an unaffirmed trade close to settlement is a live risk, not a formality still pending.

### T+1
The standard settlement cycle for most U.S. equity trades — settlement occurs one business day after the trade date, per SEC Rule 15c6-1.
**In use:** "We're T+1 on this one, so anything open past today's cutoff is a fail, not a tomorrow problem."
**Common misuse:** Treated as a buffer ("we have a day to sort it out") rather than a hard deadline with its own fail-reporting and capital-charge consequences once missed.

### Corporate action
Any issuer-initiated event that changes the terms of an outstanding security — includes dividends, stock splits, reverse splits, mergers, spin-offs, and rights offerings, not dividends alone.
**In use:** "There's a corporate action on DEF — 3-for-2 split, record date next Friday, need to get the cost-basis adjustment queued."
**Common misuse:** Used as if it only means dividend payments. Splits, mergers, and spin-offs are corporate actions too, and each has a different required adjustment to share count and cost basis.

### Cost basis
The amount originally paid for a security, per share, used to calculate gain or loss on a future sale — adjusted for any corporate actions since purchase.
**In use:** "Cost basis has to come down to $40 a share after this split, not stay at $60 with the share count just going up."
**Common misuse:** Confused with current market value, or left unadjusted after a split/spin-off — producing a position that looks right in share count but is wrong for every future tax calculation.

### Weighted-average price
The execution price of a multi-fill order, computed as total dollar value of all fills divided by total shares filled — not a simple average of the distinct print prices.
**In use:** "Recompute it as weighted-average, not the average of the two print prices — that's where the $250 came from."
**Common misuse:** Calculated as the arithmetic mean of the print prices themselves, which misweights whichever fill size was larger or smaller relative to the others.

### Settlement fail
A formal status applied when a trade does not settle by its scheduled settlement date — distinct from a delay still being actively worked before the deadline.
**In use:** "That's not just late — it's a fail as of this morning, and it carries its own reporting requirement now."
**Common misuse:** Used loosely for any slow-moving reconciliation. A fail is a specific post-deadline status with capital and reporting consequences, not a synonym for "still pending."

### Give-up
An arrangement where an executing broker "gives up" a trade to a separate clearing broker named by the client, who then takes on the clearing and settlement obligation.
**In use:** "This was a give-up trade — the execution happened at Broker A, but it clears through us."
**Common misuse:** Assumed to mean the executing broker has no further obligation at all, when in practice the executing broker still bears responsibility for accurate trade details passed to the clearing broker.

### Ex-dividend date / record date
The record date is when the issuer checks its books to determine who receives a dividend or corporate-action entitlement; the ex-dividend date is the first trade date on which a buyer will *not* receive that entitlement — they are related but not the same date.
**In use:** "This trade executed before ex-date but won't settle until after record date — it goes through due-bill so the dividend follows the buyer."
**Common misuse:** Treated as interchangeable. Getting the two dates confused misallocates dividend entitlements between buyer and seller on trades that straddle the corporate-action timeline.

### Due-bill
A mechanism ensuring a security trades with its pending dividend or corporate-action entitlement attached when the trade executes before the entitlement is paid out but settles after the record date has passed.
**In use:** "That trade needs a due-bill — it was bought before ex-date but won't settle until after record date."
**Common misuse:** Assumed unnecessary once a trade has settled, when the due-bill obligation is determined by the relationship between trade date and record date, not settlement date alone.

### Fill ticket
The line-item record of an individual execution — one partial fill of a larger order — showing exact shares and price for that specific print.
**In use:** "Pull the fill tickets, not the blotter summary — the summary's averaging method is what's wrong here."
**Common misuse:** Treated as redundant with the summarized blotter entry, when the fill tickets are the actual source of truth the summary is (sometimes incorrectly) derived from.

### Plug
An unsubstantiated adjustment entry booked purely to force two sides of a reconciliation to match, without identifying which underlying line item was actually wrong.
**In use:** "Don't plug it — find which fill is actually causing the $250 gap first."
**Common misuse:** Treated as an acceptable shortcut for small amounts. A plug closes today's exception but leaves the real error in place to resurface, often at a worse time (audit, tax reporting, or a larger break later).
