# Data Entry Keyer — Vocabulary

### Key-verify (two-key / double-key entry)
Independently keying the same source data twice, by two different keyers, then comparing the two results to catch discrepancies.
**In use:** "This batch is on financial fields, so it's key-verify — everything gets keyed twice, independently."
**Common misuse:** Treated as interchangeable with a single keyer proofreading their own work. It isn't — the value of key-verify is a second, independent pass, not a second look by the same person.

### Discrepancy rate
The percentage of field-entries where two independent keyings of the same field disagree.
**In use:** "Aggregate discrepancy rate came in at 0.8%, under target — but that's hiding a field-level problem."
**Common misuse:** Treated as a single pass/fail number. A low aggregate rate can hide a high rate concentrated in one or two fields — always break it out by field before accepting a batch.

### Exception (flag)
A field the keyer cannot confidently key from the source document — illegible, contradictory, or out of a documented valid range — routed to a queue for review rather than guessed.
**In use:** "The date field is smudged past readability — flag it as an exception, don't guess."
**Common misuse:** Treated as a failure or a sign of a slow keyer. A healthy, honest flag rate is a sign the keyer is following procedure, not a performance problem to minimize.

### KPH (keystrokes per hour) / records per hour
Throughput metrics used to measure keying production speed, distinct from accuracy metrics.
**In use:** "Her KPH is above team average, but I want to see the exception-flag rate before I call that a good thing."
**Common misuse:** Used alone as a performance metric. KPH without an accompanying accuracy or flag-rate metric tells you nothing about data quality — a high-KPH, low-flag-rate combination is the pattern to investigate, not celebrate by default.

### Acceptance sampling (AQL — Acceptable Quality Level)
A statistical method for deciding whether to accept or reject a completed batch based on the defect count found in a randomly drawn sample, rather than inspecting every record.
**In use:** "Sample size is 80 for this batch — pull 80 at random, not the first 80 keyed."
**Common misuse:** Sample drawn non-randomly (e.g., the easiest-to-read records, or the ones keyed first) — this defeats the statistical basis of the method and produces a falsely optimistic accept decision.

### Source document
The original paper or scanned record being keyed — the ground truth a keyed value is checked against.
**In use:** "Don't resolve the discrepancy by picking the value that looks more plausible — go back to the source document."
**Common misuse:** Treated as optional to re-check once a record is keyed. When two keyed values disagree, or a downstream user flags a likely error, the source document is the only authority — not the entry system's stored value, and not either keyer's memory of what they typed.

### Field-level rate vs. aggregate rate
The error or discrepancy rate calculated per individual field, versus the single rate calculated across the whole record or batch.
**In use:** "The aggregate rate looks clean at 0.8%, but the field-level rate on date-of-loss is 7.25% — nine times higher."
**Common misuse:** Only the aggregate rate is reported, which can pass a batch that has a serious, fixable problem concentrated in one field.

### Input mask / format validation
A data-entry-system feature that constrains what can be typed into a field (e.g., forcing a specific date format) or validates it against a rule before accepting the entry.
**In use:** "The date field has no input mask, so it silently accepts either DD/MM or MM/DD — that's the root cause of the discrepancy spike."
**Common misuse:** Assumed to guarantee correctness. A mask enforces format (that something looks like a date) but not accuracy (that it's the right date) — a keyer can still enter a validly-formatted wrong value.

### Batch
A defined group of source documents or records processed, verified, and released together as a unit.
**In use:** "Batch 14 failed the acceptance-sampling check — full re-verification before it's released."
**Common misuse:** Treated as an arbitrary administrative grouping. Batch boundaries matter for quality control — sampling and accept/reject decisions are made per batch, not per shift or per keyer, so a batch that mixes a hard and easy document type can hide a quality problem in the easy portion.

### Throughput quota
A production target (records or keystrokes per hour) a keyer is expected to meet.
**In use:** "The quota assumes clean typed source documents — this batch is handwritten, so it should run slower."
**Common misuse:** Applied uniformly regardless of source-document quality. A quota calibrated to clean, typed documents pushes error rates up when silently applied to a harder document mix (handwritten, low-contrast, or unfamiliar-format sources).
