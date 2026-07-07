# Correspondence Clerk — Red Flags

### Queue item at or past 10 of a 10-business-day SLA with no draft started
- **Usually means:** the aging-bucket triage order was inverted (fresh items worked first) or the item was miscategorized and skipped during intake sorting.
- **First question:** when did this item last get touched, and why did items received after it get worked first?
- **Data to pull:** queue system's item-touch history and the day's processing order log.

### Same template produces a second incorrect letter within a short window
- **Usually means:** the template itself is defective (stale rate/policy, wrong conditional logic), not that two different clerks made the same unrelated mistake.
- **First question:** what specifically was wrong in both letters, and is it the same field or clause both times?
- **Data to pull:** the template's last-reviewed date and the two flagged letters side by side.

### Variable field contains a bracketed placeholder (e.g., "{{amount}}") in a letter marked as sent
- **Usually means:** the field wasn't populated before finalizing, and the read-back check either didn't happen or only skimmed formatting, not content.
- **First question:** did this letter go through the pre-send read-back step, and did that step actually catch anything on this letter?
- **Data to pull:** the send log and whichever quality-check step exists for that queue.

### Inquirer's stated fact in their letter contradicts the source system's current figure
- **Usually means:** either the source system was updated after the inquirer's original notice went out (common, benign) or there's a genuine data error in the source system (less common, needs correction, not just an explanatory letter).
- **First question:** when was the source-system figure last updated, and does that update date predate or postdate the inquirer's letter?
- **Data to pull:** the source system's field-level change history for that account/case.

### A template hasn't been reviewed in over 90 days and references a rate, fee, or regulatory deadline
- **Usually means:** the policy or rate behind the template may have changed without the template being updated to match.
- **First question:** has the underlying rate/policy/regulation this template references changed since the last review date?
- **Data to pull:** the current version of the source policy/rate schedule, compared line by line against the template's language.

### Clerk's daily closed-item count is high but the queue's average age is climbing
- **Usually means:** items are being selected by ease rather than by age — high throughput on easy items while old items sit.
- **First question:** what's the age distribution of what got closed today versus what's still open?
- **Data to pull:** a same-day aging-bucket breakdown of closed items versus the current open-queue snapshot.

### An escalated item sits with no caseworker response past a defined follow-up interval
- **Usually means:** the escalation went into a queue nobody is actively monitoring, or it was miscategorized as lower priority than it is.
- **First question:** who owns this escalation queue, and when was it last reviewed?
- **Data to pull:** the escalation queue's assignment log and last-activity timestamp.

### Inquiry involves a policy-flagged vulnerable-population indicator but was processed with a standard template
- **Usually means:** the intake classification step was skipped or the flag wasn't checked before template selection.
- **First question:** was the vulnerable-population flag visible at intake, and if so, why wasn't it acted on?
- **Data to pull:** the case file's flag history and the intake classification record for this item.

### Two consecutive letters to the same recipient give inconsistent answers to what appears to be the same question
- **Usually means:** either the underlying facts genuinely changed between letters (needs the second letter to explain the change) or one of the two letters used stale data.
- **First question:** what changed in the source system between the two response dates?
- **Data to pull:** both letters plus the source-system change log spanning the two response dates.

### A dollar amount or deadline in a finalized letter doesn't match the value in the source system it was supposedly pulled from
- **Usually means:** the field was typed from memory, copy-pasted from a different case, or transposed during entry rather than pulled fresh from the source system.
- **First question:** does the source system currently show a different value than what's in the letter, and if so, by how much?
- **Data to pull:** the source-system field value at the time the letter was drafted, and the letter's actual text.
