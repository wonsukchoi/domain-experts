# Correspondence Clerk — Playbook

## Queue aging-bucket triage (10-business-day SLA)

| Bucket (days since receipt) | Items | Action |
|---|---|---|
| 10+ | 6 | Work first, every shift, before any newer bucket — already at or past SLA |
| 6–9 | 12 | Work second, oldest-within-bucket first |
| 3–5 | 14 | Work if time remains after the above two buckets are cleared or substantially reduced |
| 0–2 | 8 | Work last — freshest items have the most SLA runway |

Rule: never let bucket order invert based on which items look quick. A 10+ day item that takes 15 minutes still goes before a 0–2 day item that takes 5 minutes.

## Template currency check (run before using any template referencing a rate, policy, or deadline)

| Template | Last reviewed | Currency window | Status |
|---|---|---|---|
| Benefit-amount-confirmation | 2026-05-02 | 90 days | Current (within window) |
| Fee-schedule-notice | 2026-01-10 | 90 days | **Stale — verify against source system before use, then flag for review** |
| Standard-acknowledgment (no rates/policy referenced) | n/a | No currency window — content doesn't reference changeable figures | Always current |

A template with no rate/policy/deadline content (a pure acknowledgment or receipt-confirmation letter) doesn't need a currency window — the staleness risk only applies to templates carrying figures or clauses that can change underneath them.

## Variable-field cross-check (filled example)

| Field | Template placeholder | Value pulled | Source | Cross-checked against | Match? |
|---|---|---|---|---|---|
| Recipient name | {{name}} | J. Alvarez | Case file header | Inquiry letter signature | Yes |
| Account number | {{acct_no}} | 8834-201 | Case management system | Prior correspondence on file | Yes |
| Current benefit amount | {{amount}} | $1,284.00 | Source system (benefits ledger) | Inquirer's letter states $1,248.00 | **No — inquirer's figure is a stale system entry, corrected 2026-02-14; use source-system figure** |
| Response deadline referenced in letter | {{deadline}} | 2026-08-15 | SLA calculator (receipt date + 10 business days) | Manually recount business days | Yes |

Any field marked "No match" gets resolved before the letter goes out — either the source system is right and the letter explains the discrepancy (as in the amount row above), or the source system itself needs correcting and the letter waits.

## Escalation-criteria decision table

| Inquiry characteristic | Template-suffices or escalate | Why |
|---|---|---|
| Inquirer disputes a fact the template assumes as settled (e.g., "I never received that notice") | Escalate | Templates aren't written to resolve factual disputes — a caseworker needs to investigate |
| Inquiry references legal action or a regulator complaint | Escalate | Outside clerk authority regardless of how routine the underlying question looks |
| Inquiry is a straightforward status/confirmation request matching a template's documented scope | Template suffices | This is exactly what templates are built for |
| Inquiry involves a vulnerable-population flag (elder, guardianship, active crisis) per policy | Escalate | Policy-mandated regardless of how simple the substantive question is |
| Inquiry asks a question the template answers, but also raises an unrelated second question outside template scope | Template answers the first part; escalate the second | Don't silently drop the part a template can't cover |

## Fallback position when no template fits and escalation queue is backed up

1. Send a brief acknowledgment (not a substantive answer) confirming receipt and stating a caseworker will respond, if policy allows an acknowledgment-only response within SLA.
2. If acknowledgment-only isn't policy-compliant for this inquiry type, flag to a supervisor as an SLA-risk item rather than drafting a template response that doesn't actually fit — a late accurate answer is recoverable, a fast wrong one often isn't.
