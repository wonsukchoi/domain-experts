# Booth Cashier Playbook

Filled procedures with real thresholds and slip sequences. Defaults, not laws — every property's MICS can set a tighter number; when in doubt, the property's written procedure wins over anything below.

## 1. Opening and closing a booth bank

### Opening (start of shift)

1. Count the imprest bank issued by the cage against the cage's fill slip, in front of the outgoing/relieving cashier if one exists. Standard opening bank for a slot-floor booth: **$2,000–$3,000**, denomination mix weighted toward $1s, $5s, $20s, and rolled coin/tokens if the property still runs coin.
2. Sign the count sheet; note any pre-existing discrepancy on the slip itself before accepting the bank — an unsigned discrepancy at handoff becomes your discrepancy at close.
3. Log the opening total and starting drawer float in the booth's shift log.

### Running the shift

4. Every transaction gets a slip or a scan at the moment it happens: TITO ticket redeemed → validated by the SDS, not hand-keyed; cash-for-token sale → drawer updates same transaction; hand pay → W-2G/ID capture before cash leaves the drawer; fill → triplicate slip signed before the machine reopens.
5. Running balance = opening + cash in − payouts − fills issued out, checked mentally at each transaction, not reconstructed at close.

### Closing (end of shift)

6. Stop transactions, count the drawer twice independently (cashier, then a second person if the property requires dual close — commonly required above a **$5,000** bank).
7. Reconcile: `closing count = opening + cash-in − TITO payouts − hand pays + fills received`. A variance of any size gets written up on the spot, not carried forward "to check tomorrow."
8. File the count sheet, all fill slips, all W-2G forms, and any MTL entries together — a balanced drawer with missing paperwork is not a clean shift.

## 2. Hand-pay threshold table

| Trigger | Requirement | Source / basis |
|---|---|---|
| Slot jackpot ≥ $2,000 (single line, single spin) | W-2G form completed, 2 forms of ID captured before cash released | IRS Form W-2G instructions — threshold raised from $1,200 for wins after Dec 31, 2025 |
| Bingo/keno win ≥ separate per-game threshold (lower than slots — check current W-2G instructions by game) | Same W-2G/ID requirement, game-specific line | IRS Form W-2G instructions |
| Hand pay ≥ property's supervisor line (commonly $10,000, sometimes lower — e.g. $5,000 on some tribal/state MICS) | Floor supervisor countersignature required before payment, cashier does not pay solo | State/tribal MICS, modeled on Nevada Reg. 6 |
| Any hand pay where the drawer can't cover it | Emergency fill from cage, triplicate fill slip, cage + booth cashier signatures, supervisor witness if fill exceeds property's witness line (commonly $500) | [stated heuristic] — confirm against property procedure |
| Machine malfunction indicator lit ("tilt") on a jackpot | Do not pay. Lock the machine, call slot tech and supervisor, verify the malfunction voids or honors the win per posted machine rules before any cash moves | Standard slot-floor procedure |

## 3. TITO ticket redemption — decision sequence

1. Scan the barcode at the redemption unit. If it validates against the SDS for the printed amount: pay.
2. If it fails to validate: **do not hand-key the amount.** Check for a torn/smudged barcode (rescan up to 2–3 times, different angle) before escalating.
3. If it still fails, or the printed machine number/date/time look inconsistent with the ticket's issue pattern (e.g. a "same day" ticket printed at a timestamp during a known system outage): decline redemption, hold the ticket, call a slot tech and a supervisor.
4. If the ticket is expired (property policies typically void unredeemed tickets after 30–180 days, check the posted expiration on the ticket itself): direct the patron to the cage redemption/unclaimed-property process, do not pay from the booth.
5. Log any declined or escalated ticket with the ticket's validation number, even if it's ultimately honored after manual verification — the log is what protects the cashier if the same ticket resurfaces.

## 4. Fill procedure (machine restock — currency or tokens)

1. Cashier determines the machine needs a fill (hopper running low, or a large payout is about to exceed hopper capacity).
2. Cage prepares a triplicate fill slip: amount, denomination breakdown, machine number, date/time.
3. Fill delivered to the machine by cage runner or booth cashier per property policy; **counted by two people** at the machine before the hopper door closes.
4. Both counters sign the fill slip. One copy stays with the machine's internal drop box, one goes to the booth's shift paperwork, one returns to the cage/count team.
5. Machine reopens for play only after the fill slip is fully signed — an open machine with an unsigned fill is a control gap the next hard count will flag.

## 5. MTL / structuring watch — when to log

Log an MTL/ACL entry (patron ID + amount + time + window) when:

- A single cash-out or cash-in at your booth is at or above the property's internal MTL line (commonly **$2,500–$3,000**) — [stated heuristic, confirm property threshold].
- You recognize a patron who has already transacted elsewhere that gaming day and the combined total crosses the same line — check the shared log/SDS alert, don't rely on memory of a face.
- A patron makes several transactions at your window in succession that individually sit just under the MTL line (e.g. three $2,400 cash-outs in twenty minutes) — this is the classic structuring pattern; log each one and flag the pattern to a supervisor regardless of whether any single leg crosses the line.

Never tell a patron the threshold number or that their activity is being logged — MTL logging is a routine back-office control, not a customer-facing negotiation, and disclosing the exact line invites deliberate structuring around it.

## 6. Counterfeit-suspect handling

1. Run bills $50 and up under the pen/UV light at intake — before the bill enters the drawer's stack, not during the close-out count.
2. If a bill fails or looks visually wrong (color, paper feel, missing security thread under UV): do not confiscate it. Politely ask the patron for an alternate form of payment while showing it to a supervisor.
3. If the supervisor concurs it's suspect: follow property procedure for retaining vs. returning it (varies by state — some require surrender to law enforcement, some allow return with a refusal to transact). Log the denomination, serial number if legible, and the transaction context.
4. If it's already in the drawer before doubt arises (found at count): it goes into the shift's shortage/loss report, not quietly absorbed into "cash over/short."
