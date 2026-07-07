# Library Assistant, Clerical — Red Flags

### Shelf-reading error rate above 2-3% in one call-number range
- **Usually means:** A systematic misfiling pattern — shared Cutter-number digit-transposition, sub-range confusion — rather than random drift.
- **First question:** Do the flagged items share a common call-number pattern, or are they scattered with no shared cause?
- **Data to pull:** Sorted list of flagged items with full call numbers side by side.

### Hold sits past its pickup-window expiration (commonly 5-7 days) without being purged
- **Usually means:** The purge process was skipped for that day, or the patron-notification system failed to alert them in time.
- **First question:** Was the expiration notification actually sent, and when?
- **Data to pull:** Hold-expiration report cross-checked against the notification log.

### Same patron disputes a fine more than once in a short window
- **Usually means:** A system due-date recording error is recurring for that patron's account, not a pattern of dishonesty.
- **First question:** Does the ILS-recorded due date match the checkout receipt or in-transit scan log for each disputed transaction?
- **Data to pull:** Full transaction history for the patron across the disputed items.

### A reference question keeps producing "let me check" with no resolution
- **Usually means:** It has crossed from a locate-a-known-item question into a research/source-evaluation question and needs the librarian now, not after more searching.
- **First question:** Is the patron trying to find a specific item, or evaluate/synthesize which source is best for their need?
- **Data to pull:** None — this is a live triage call, escalate rather than research further.

### Class-set or bulk-checkout return count doesn't match the checkout manifest
- **Usually means:** An item was left in a classroom or is still in transit, not necessarily lost.
- **First question:** Does the return-scan count match the original checkout manifest count exactly?
- **Data to pull:** Checkout manifest against the return-scan log for that transaction.

### An item shows a "withdrawn" or "discard" status change nobody remembers approving
- **Usually means:** Someone applied a weeding decision without the librarian's sign-off, or a data-entry error miscoded the status.
- **First question:** Whose login applied the status change, and when?
- **Data to pull:** Item status-change audit log.

### In-transit item hasn't arrived within the expected inter-branch transfer window (typically 3-5 days)
- **Usually means:** It's lost in transit or misrouted to the wrong branch, not merely delayed.
- **First question:** Does it still show "in transit," or did the status silently revert to something else?
- **Data to pull:** Consortium inter-branch transfer log for that item.

### Multiple patrons report the same item "not on the shelf" despite the ILS showing it available
- **Usually means:** It's misshelved nearby, not actually missing — misshelved is far more common than lost or stolen.
- **First question:** Has a shelf-read been run on that call-number range recently?
- **Data to pull:** Date of the last completed shelf-read for that range.

### A fine-waiver request cites "policy" that doesn't match the current written fee schedule
- **Usually means:** The patron is remembering an outdated policy (many libraries changed fine structures, e.g. moving to fine-free, on a specific effective date) or a different branch's rule.
- **First question:** Which policy version and effective date is the patron citing?
- **Data to pull:** Current fee-schedule document with its effective date.
