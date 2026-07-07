# Office Clerk, General — Playbook

## Daily task-triage worksheet (filled example)

| Task | Est. min | Hard/Soft | Deadline | Decision |
|---|---|---|---|---|
| Phone coverage 12–1pm | 60 | Hard | Fixed block | Do |
| File 85 docs | 127.5 | Soft | None stated | Do |
| Enter 30 invoices | 120 | Soft | 48-hr window | Do |
| Order supplies | 20 | Soft | Monthly, not urgent | Do |
| Prep outgoing mail (12 pcs) | 36 | Soft | Same-day pickup at 4pm | Do |
| Vendor inquiry reply | 25 | Soft | No SLA | **Defer → tomorrow** |
| Q3 filing-audit summary | 90 | Soft | Friday EOD | **Defer → Thursday/Friday** |
| Rush shipping labels (arrives 2pm) | 45 | Hard | Same-day courier cutoff | Do (protected regardless of arrival time) |

**Sort order for the "Decision" column:** all Hard items first (committed, no negotiation); then Soft items ranked by consequence-of-delay (external-facing > internal > none) until remaining capacity is filled; anything left over is deferred, largest-low-consequence-item first.

**Capacity check:** Available minutes − sum(Hard) = remaining capacity for Soft items. If sum(Soft, undeferred) > remaining capacity, defer starting from the largest item with the lowest consequence-of-delay, not the smallest.

## Hard vs. soft deadline sorting method

Ask two questions for every item before scheduling it:

1. **"What happens if this slips to tomorrow?"** — If the answer names a specific external cost (a missed courier cutoff, a customer left waiting on a promised callback, a same-day filing requirement), it's Hard. If the answer is "nothing, really" or "someone might ask about it," it's Soft.
2. **"Did the requester state a deadline, or did I assume one?"** — An assumed deadline defaults to Soft until confirmed. A stated deadline with a real consequence is Hard.

Re-run this sort whenever a new item arrives mid-day — a 2pm rush request can outrank items already in progress if it's genuinely Hard.

## Escalation-trigger table

| Signal | Action |
|---|---|
| Same task-category deferred 1 time | Note it in the handoff; no escalation yet |
| Same task-category deferred 2 consecutive periods | Flag it explicitly to a supervisor as a capacity/staffing observation |
| A Hard-deadline item was nearly missed because Soft items crowded the schedule | Flag immediately — this is a process failure, not a one-off |
| Task-minute totals trending up over several weeks for one category (e.g. filing volume) | Flag with the trend data, not just "I'm busier" |

## Shift-handoff note template (filled)

> **Handoff — [Day]**
> Completed: [list, with any relevant confirmation — shipped/confirmed, filed count, records entered].
> Deferred to [when]: [item] — [one-line reason: no SLA / soft deadline / capacity].
> Flagged: [any pattern worth a supervisor's attention, with a number if possible — "this is the Nth week this category needed deferral"].
