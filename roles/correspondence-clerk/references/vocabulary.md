# Correspondence Clerk — Vocabulary

### SLA clock
The countdown from an inquiry's receipt date to its required response deadline, expressed in business days.
**In use:** "This one's on day 9 of a 10-day SLA clock — it goes to the top of today's queue."
**Common misuse:** Treating the clock as starting when a clerk picks the item up rather than when it was received — that gap is exactly what causes items to breach without anyone noticing until the deadline.

### Aging bucket
A queue-triage category grouping open items by how long they've been waiting, used to decide processing order.
**In use:** "Anything in the 10+ bucket gets worked before we touch the 0–2 bucket, no exceptions."
**Common misuse:** Reordering within or across buckets based on which item looks quickest to close, which inverts the entire point of bucket-based triage.

### Template currency window
The maximum interval a template can go without review before it must be re-verified against current policy/rate before use.
**In use:** "This fee-schedule template's currency window is 90 days and it's at 94 — verify against the current rate table before you send it."
**Common misuse:** Applying a currency window to every template uniformly, when only templates referencing rates, policy, or deadlines actually carry staleness risk — a pure acknowledgment letter doesn't need one.

### Variable field
A placeholder in a template meant to be filled with case-specific data (name, account number, dollar amount, date) before the letter is finalized.
**In use:** "Three variable fields on this one — name, account number, and benefit amount — all three need a source-system pull, not a guess."
**Common misuse:** Filling a variable field from the inquirer's own letter instead of the source system, which propagates the inquirer's error (or a stale figure) straight into the official response.

### Cross-check
Verifying a variable field's value against a second, independent source before finalizing, distinct from simply confirming the field isn't blank.
**In use:** "The read-back confirmed the amount field wasn't empty, but nobody cross-checked it against the ledger — that's how the wrong figure went out."
**Common misuse:** Conflating a read-back (checking the letter reads coherently) with a cross-check (verifying a specific figure against an independent source) — they catch different classes of error.

### Escalation
Routing an inquiry to a caseworker or supervisor because it falls outside every available template's documented scope, made as an intake decision rather than a post-hoc rescue.
**In use:** "This one disputes a fact the template assumes as settled — escalate it now, don't draft a template response and hope it holds."
**Common misuse:** Treating escalation as a failure or a last resort after a template attempt goes wrong, rather than a first-pass classification decision that saves a full SLA cycle when made early.

### Template scope
The documented set of facts and circumstances a given template is written to correctly address.
**In use:** "The facts here are just outside this template's scope — it assumes a single account holder, and this inquiry has two."
**Common misuse:** Stretching a template to cover facts adjacent to its documented scope on the assumption that "close enough" customization will bridge the gap.

### Regret register
A running log of response letters later found to be wrong, kept to identify defective templates before they produce a wave of similar errors.
**In use:** "Two entries in the regret register this month both point to the same fee-schedule template — that's a template problem, not a coincidence."
**Common misuse:** Using the register only to track individual clerk mistakes rather than looking across entries for a shared root cause like a single bad template.

### FIFO triage
First-in-first-out processing order — working the oldest eligible item in the queue before newer ones, absent an explicit priority override.
**In use:** "We're strict FIFO here unless something's flagged high-priority — size and complexity don't jump the line."
**Common misuse:** Assuming FIFO means "in the order I happen to open them," rather than the queue's actual receipt-date order, which requires checking the aging report rather than the visual list order.

### Priority flag
A policy-defined marker (legal referral, regulator complaint, vulnerable-population indicator) that overrides normal FIFO queue order.
**In use:** "This one's got a vulnerable-population flag — it jumps the queue regardless of its actual age."
**Common misuse:** Applying informal priority judgment ("this one seems urgent") in place of the policy-defined flag list, which produces inconsistent triage across clerks.

### Closed vs. resolved
"Closed" means a response was sent; "resolved" means the inquiry's underlying question was actually answered or the issue actually addressed — the two aren't always the same event.
**In use:** "It's closed — we sent the letter — but it's not resolved, because the letter only answered half the inquiry. Flag the rest for follow-up."
**Common misuse:** Treating "sent a response" and "handled the inquiry" as synonyms, which lets a partially-answered inquiry disappear from tracking as if it were fully done.

### Boilerplate
The fixed, non-variable language in a template that doesn't change from letter to letter.
**In use:** "The boilerplate explaining the appeals process is fine as-is — it's only the amount field that needs updating."
**Common misuse:** Assuming boilerplate never needs review because it "isn't variable," when boilerplate can itself go stale if it describes a process or right that has since changed.
