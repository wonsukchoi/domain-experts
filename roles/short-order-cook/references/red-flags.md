# Red flags

Smell tests a short-order cook (or the manager reading over their shoulder) should catch fast, with the first question to ask and the data to pull before deciding anything.

### Ticket times climbing past ~10 minutes average during a rush that hasn't gotten busier

- **Usually means:** zone-batching has broken down and the cook is working the rail in strict arrival order under load, or griddle surface temp has drifted low from a run of cold product hitting one zone.
- **First question:** "Are you firing by zone right now, or by ticket order?"
- **Data to pull:** griddle surface temp across all three zones, and in/out timestamps for the last 20 tickets.

### Bacon or sausage par-hold visibly low with 20+ tickets of rush still ahead

- **Usually means:** no fresh par batch was started at the right lull, or the opening par was set from a slower morning than today's actual pace.
- **First question:** "What's the burn rate on par right now against the rush time left?"
- **Data to pull:** par-log entries for the shift, protein item counts over the last hour, and hold-time-since-cook on the current batch.

### The same egg order comes back to the pass window twice in one rush

- **Usually means:** a non-standard doneness ("over hard," "scrambled dry," "no runny yolk") got grouped into a standard batch instead of isolated and fired alone.
- **First question:** "Was that ticket flagged as non-standard before it went on the griddle?"
- **Data to pull:** the original ticket annotation and which batch/zone it was cooked in.

### A hot-held batch still on the line past roughly 4 hours

- **Usually means:** nobody is tracking hold-start time per batch — the cook is judging by "still hot to the touch" instead of a clock.
- **First question:** "When did this batch go into the well?"
- **Data to pull:** hold-start timestamps (verbal or written) for every batch currently in the steam table.

### Griddle probe reading noticeably below the dial setting

- **Usually means:** the dial hasn't been recalibrated against actual surface temp in a while, or a heavy batch just dropped that zone's temperature and nobody rechecked.
- **First question:** "When did you last probe this zone, not just read the dial?"
- **Data to pull:** probe reading versus dial setting, and time since the last large batch hit that zone.

### A new hire timing every plate against a stopwatch instead of visual doneness cues

- **Usually means:** training leaned on time targets instead of color/sheen/bubble cues, which breaks the moment ticket volume runs faster or slower than the training pace.
- **First question:** "What visual cue tells you this is done — not what the clock says."
- **Data to pull:** plate-return or remake rate for that hire versus tenured cooks over the same shift type.

### An item gets 86'd only after a ticket is already fired for it

- **Usually means:** par tracking is reactive — triggered by hitting zero stock — instead of burn-rate-based, which stalls the ticket that just fired and forces a remake conversation with the server.
- **First question:** "What was stock, and expected demand, fifteen minutes before this ticket fired?"
- **Data to pull:** the par-log trend for that item across the rush and the remaining-rush-time estimate at the moment it ran out.

### A consumer-advisory doneness item isn't distinguishable from the standard batch on the ticket

- **Usually means:** a POS/ticket-template gap, not a cook error — the disclosure obligation sits with the menu, but the cook has no flag on the printed ticket to isolate the item from batching.
- **First question:** "Does the ticket printer flag advisory items, or is that only on the paper menu?"
- **Data to pull:** the POS ticket template and a sample of tickets carrying advisory-doneness orders.

### The same spatula or tongs move between raw protein and the hot-hold reserve without a change

- **Usually means:** a cross-contamination gap between raw-handling and the par-hold finish step.
- **First question:** "Is there a separate utensil for the raw zone versus the hold/finish zone?"
- **Data to pull:** utensil count and placement at the station, and the last health-inspection notes on cross-contact.

### The rush-end par-usage log is missing or filled in as "same as always"

- **Usually means:** no feedback loop from actual demand back into the next shift's prep numbers — par gets set by habit, not by yesterday's burn rate.
- **First question:** "What did we actually use today versus what we prepped?"
- **Data to pull:** opening par versus closing leftover count by item, compared across the same day of week for the last 4 weeks.
