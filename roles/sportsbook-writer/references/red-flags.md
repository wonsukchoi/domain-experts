### A bet requested within seconds of a posted cutoff, especially from an unfamiliar patron or over a phone/kiosk channel
- **Usually means:** an honest late arrival who simply misjudged the clock; second most likely is an attempt to bet with knowledge of an outcome the writer doesn't yet have (past-posting).
- **First question:** what does the system clock show for cutoff versus right now, to the second — not what the writer's watch or the TV broadcast shows?
- **Data to pull:** the book management system's cutoff timestamp for that event and the ticket-write timestamp log for the window.

### A final score or race result that lands exactly on the posted number
- **Usually means:** a routine key-number push, most common at 3 and 7 in NFL spreads.
- **First question:** is the number on the ticket the exact final margin, not a rounded or remembered one?
- **Data to pull:** the official result source approved for grading and the exact line printed on the ticket.

### A patron's cash-out pattern sitting just under the W-2G thresholds across multiple tickets in one session
- **Usually means:** coincidence from normal bet sizing; second most likely is deliberate structuring to avoid a W-2G or a related cash-reporting trigger.
- **First question:** across this patron's tickets today, does any single win or the aggregate pattern actually clear both the $2,000 and 300x tests, even if no individual ticket does?
- **Data to pull:** the patron's ticket history for the gaming day via player-tracking ID, if enrolled.

### Heavy one-sided handle on a line that hasn't moved in the last 30–60 minutes despite live action
- **Usually means:** the line accurately reflects consensus and the imbalance is normal square-money noise; second most likely is unaddressed sharp action the book hasn't reacted to yet.
- **First question:** what share of the handle (not just bet count) is on the heavy side, and is it concentrated in a small number of large, fast-placed bets (a sharp signature) or spread across many small ones (square money)?
- **Data to pull:** the handle-by-side report and average bet size on each side for the event.

### A parlay or teaser ticket that printed with fewer legs than the patron requested
- **Usually means:** a same-game correlation block silently rejected one leg; second most likely is a keying error.
- **First question:** does the printed ticket match exactly what the patron asked for, leg by leg, before they leave the window?
- **Data to pull:** the system's correlation-rule log for that ticket ID.

### A reconciliation variance at shift close, of any size
- **Usually means:** a specific mis-keyed ticket, misgraded push, or miscounted transfer; second most likely (and much less common) is theft.
- **First question:** retracing chronologically, which single transaction in the shift log accounts for the variance?
- **Data to pull:** the shift's full ticket log with timestamps, cross-referenced against the cage transfer slips.

### A win that clears $5,000 but fails the 300x multiplier test
- **Usually means:** a straightforward large moneyline or total-odds win that doesn't trigger a W-2G but may still trigger 24% federal backup withholding under the separate $5,000 rule.
- **First question:** has the backup-withholding question been checked independently of the W-2G reporting test — they are not the same trigger?
- **Data to pull:** current IRS Form W-2G instructions' withholding threshold and the patron's TIN-on-file status.

### A patron repeatedly asking what amount "avoids paperwork"
- **Usually means:** genuine curiosity about tax rules; second most likely is an explicit attempt to structure bets or cash-outs around a known reporting threshold.
- **First question:** is this a one-off question or a pattern across visits/sessions for this patron?
- **Data to pull:** patron history if tracked; otherwise, document the request in the shift report regardless of outcome.

### A same-game teaser or parlay priced at the standard card rate that crosses both key numbers (3 and 7) on multiple legs
- **Usually means:** the writer is quoting a stale or default price without checking current book policy on stacked-key-number teasers, which are priced differently at many books specifically because the win rate on them is materially higher than a standard teaser.
- **First question:** does current book policy carry a separate (higher-vig) price for teasers crossing both 3 and 7 on a leg?
- **Data to pull:** the book's current teaser pricing sheet, not the general parlay card.

### A layoff request routed after the line has already moved significantly, rather than before
- **Usually means:** the imbalance was surfaced late; second most likely is the writer sat on a known imbalance hoping it would self-correct.
- **First question:** when did the handle imbalance first cross the internal limit, and when was it escalated?
- **Data to pull:** the handle-by-side timeline for the event versus the layoff-request timestamp.

### A ticket graded as "no action" or refunded that a patron disputes as a loss they should have won, or vice versa
- **Usually means:** an unmet bet condition (postponed event, "must start" pitcher scratched) that the patron either wasn't aware of or is testing; second most likely is a genuine grading error.
- **First question:** does the ticket's printed conditions (start requirement, postponement rule) match how it was graded?
- **Data to pull:** the exact bet-condition text printed on the ticket and the book's posted rules for that bet type.
