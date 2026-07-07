# Medical Transcriptionist — Playbook

## Silent-correction vs. flag decision table

| Ambiguity type | Example | Action | Why |
|---|---|---|---|
| Grammar/syntax only, no clinical content affected | "the the patient" (ASR stutter repeat) | Correct silently | No clinical meaning at stake |
| Well-established provider habit, confirmed by schedule/context | Surgeon always dictates "right" for this procedure type; today's schedule confirms right knee | Correct silently, first occurrence of a break in pattern still flagged | Established pattern + independent confirmation |
| Drug name, acoustically ambiguous, dose doesn't disambiguate | "hydralazine" vs. "hydroxyzine," dose consistent with either | Flag | Different drug classes, different risk profile |
| Drug name, acoustically ambiguous, dose disambiguates | Stated dose only fits one candidate drug's typical range | Flag anyway, cite the dose-mismatch reasoning in the query | Dose fit narrows likelihood, doesn't confirm intent |
| Laterality (left/right) unclear or contradicted elsewhere in dictation | Op note says "left" in one place, "right" in another | Flag | Wrong-site-surgery risk category |
| Numeric lab value implausible for stated context | "potassium 9.4" in a routine post-op note with no other acute findings mentioned | Flag | ASR commonly mishears digits; implausible value needs source confirmation |
| Date/transposed digit, resolvable from surrounding context | "March 3, 2065" in an otherwise-current-dated note | Correct silently, using the year/date pattern evident elsewhere in the note | Unambiguous once cross-referenced |

## Report-turnaround priority queue

| Report type | Typical priority | Reasoning |
|---|---|---|
| STAT (surgeon needs before next case, ED disposition pending) | Immediate, ahead of queue position | Blocks a downstream clinical decision |
| Discharge summary, same-day transfer | High | Receiving facility needs it at handoff |
| Discharge summary, routine | Same-day to next-business-day | Standard turnaround SLA |
| Operative note, non-urgent follow-up | Standard queue (FIFO within priority tier) | No immediate downstream block |
| Routine office-visit note | Standard queue | Lowest urgency tier absent a stated reason otherwise |

Sort within a tier by arrival order; sort across tiers by clinical use, not document type — a "routine" label on the order doesn't override an obvious urgency signal in the dictation content itself (e.g., "admit to ICU" in a note marked routine gets bumped).

## Flagged-query template

```
Transcription query — [document type], [patient MRN], dictated [date/time]:
At approximately [timestamp] into the dictation, [specific ambiguous term/value]
is unclear — [one-sentence reason: acoustic similarity / implausible value /
contradicts earlier statement]. [If applicable: dose/context reasoning narrowing
the candidates.] Please confirm [the specific fact needed] before this note is
finalized. Document held as draft pending your response.
```

The query names the exact word, its location, and the specific fact needed to resolve it — never a general "please clarify," which forces a full re-listen.

## Account style-guide setup checklist

- Confirm the account's stated silent-correction threshold in writing before applying the general table above — some accounts require flagging every drug/dose/lab-value ambiguity with zero exceptions regardless of provider-pattern confidence.
- Confirm the account's STAT/priority-tier definitions match the table above, or record the account-specific variant.
- Confirm which EHR field the flagged-query note routes to (secure message, chart comment, separate query-tracking system) — routing a query to the wrong channel produces the same delay as not flagging at all.
