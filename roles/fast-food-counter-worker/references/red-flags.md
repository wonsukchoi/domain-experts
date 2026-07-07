# Red flags

Smell tests a front-counter worker or their MOD should catch in the first pass over a shift's numbers or a complaint log.

### Order accuracy below roughly 90–92% for a single register over a shift

- **Usually means:** The read-back step is being skipped under speed pressure, or modifiers are being entered as free text instead of discrete line items the kitchen display can read.
- **First question:** Was the read-back performed on the flagged orders, or were they taken during a rush where it was visibly rushed or dropped?
- **Data to pull:** POS modifier-entry log for the flagged tickets against the kitchen-display record of what was actually made.

### Order-to-window time trending up with no corresponding rise in order volume

- **Usually means:** A menu or POS change added friction at order-taking, or the worker is compensating for accuracy problems by double-checking every entry instead of using the read-back once.
- **First question:** Did anything change on the ordering side (menu update, new modifier options, POS version) around when the trend started?
- **Data to pull:** Order-taking-phase timer data, separated from kitchen production time and window/handoff time.

### Suggestive-sell attach rate at or near 0% for a specific register login over a shift

- **Usually means:** The script prompt is being skipped entirely, most often under speed pressure or because the worker doesn't believe it matters.
- **First question:** Is this one shift's rush conditions, or a pattern across this login's shifts regardless of volume?
- **Data to pull:** POS suggestive-sell prompt log by login, cross-referenced against that shift's order-to-window times.

### Suggestive-sell attach rate more than roughly 15 points above the store average for one worker

- **Usually means:** The worker is repeating the prompt after a decline rather than making one attempt, which slows the line more than the extra attach rate is worth.
- **First question:** Is the second attempt happening after every decline, or only on a subset of orders?
- **Data to pull:** Timestamped POS log showing prompt count per order for that login.

### Till variance recurring on the same register login across three or more shifts

- **Usually means:** A training gap on count-back or terminal reconciliation at that specific login, less often deliberate skimming — either way it's a pattern, not a one-off.
- **First question:** Is the same person logged into this register each time the variance appears?
- **Data to pull:** Per-login variance history for the last two weeks, matched against shift schedule.

### A guest complaint resolved by giving away product beyond the worker's own authorization ceiling

- **Usually means:** The worker comped or refunded above their ceiling to end an argument rather than escalating to the MOD, which the comp/void log should show as a mismatch between amount and approver level.
- **First question:** Was the MOD actually called, or does the log show the worker's own login approving something above their line?
- **Data to pull:** Comp/void log filtered by approver login against the store's stated authorization ceiling.

### An allergen question logged as answered directly by counter staff with no reference to the ingredient card

- **Usually means:** A guess was given instead of a deferral, often because the worker felt pressure not to slow the line by saying "let me check."
- **First question:** Does the worker's account of the answer match what's actually printed on the ingredient card for that item?
- **Data to pull:** Ingredient reference card/app version in use that shift, compared against what the worker states they said.

### Multiple wrong-order complaints clustering on the same headset or kiosk-assist station in one shift

- **Usually means:** Audio quality or screen-legibility problems at that specific station, less often a single worker's skill gap — worth ruling out the equipment before the person.
- **First question:** Do the complaints trace to one worker across stations, or one station across workers?
- **Data to pull:** Complaint log tagged by station and by worker for the shift in question.

### A worker's shift log shows zero allergen deferrals over a long stretch of shifts at a high-question-volume location

- **Usually means:** Either genuinely no allergen questions came up (possible at some locations) or questions are being answered from memory instead of logged as deferrals — worth distinguishing before assuming compliance.
- **First question:** Does this worker recall being asked allergen questions this month, and if so, what did the deferral log show?
- **Data to pull:** Allergen-deferral log entries for this worker against total shifts worked in the period.

### Read-back step timing showing near-zero elapsed time between order entry and total stated

- **Usually means:** The read-back is being said too fast to be a real confirmation, or skipped and the timer only reflects the total being stated.
- **First question:** Does the POS or headset recording show the actual words used, or only the timestamp gap?
- **Data to pull:** Headset call recording (if available) or POS keystroke timing for a sample of orders from that login.
