# Proofreader / Copy Marker — Playbook

## Standard proofreader's marks (Chicago Manual of Style notation)

| Mark | Meaning | In-text symbol | Margin symbol |
|---|---|---|---|
| Delete | Remove character(s) | ⌐ struck through | ℈ |
| Insert | Add character(s) at caret | ∧ | text to insert, circled |
| Close up | Remove space | ⌣ (linking arcs) | ⌣ |
| Transpose | Swap order of two elements | ⤩ over the pair | tr |
| Stet | Ignore this mark, keep original | dots under struck text | "stet" circled |
| Spell out | Expand an abbreviation/number | circle the item | "sp" |
| New paragraph | Break here | ¶ before the word | ¶ |
| Run in | Join two paragraphs | connecting line | "run in" |
| Center | Center this element | brackets around it | "ctr" |
| Query | Flag for author/editor confirmation | ? in margin, item underlined | "qy" + note |

Every mark is keyed to a specific line; a mark with no clear line reference is not actionable by a typesetter and gets rejected back to the marker.

## Pass-scrutiny table by proof stage

| Stage | What's being checked | Tolerance for missed error | Typical turnaround |
|---|---|---|---|
| First galley / screen proof | Overall accuracy, first read against final copy | Moderate — more rounds expected | 1-3 business days |
| Second proof / correction-verification | Were round-1 marks applied cleanly; any regressions | Low — this round exists specifically to catch new issues | 1 business day |
| Blueline / press-ready PDF | Final, no further changes expected before plates | Zero for price/date/legal/safety content | Same day, often same-hour |
| Post-print spot-check (rare) | Sample-check a live print run for a press-drift defect | N/A — corrective action only, not proofing | Immediate escalation |

## Correction log (filled example)

| # | Page | Round found | Description | Type | Status |
|---|---|---|---|---|---|
| 1 | 3 | 1 | "recieve" → "receive" | Mechanical | Corrected, verified R2 |
| 2 | 12 | 1 | Double space after period | Mechanical | Corrected, verified R2 |
| 3 | 19 | 1 | Price listed $45.99, price list shows $49.99 | Factual (queried) | Confirmed $49.99, corrected R1→R2, **regression found R2** |
| 4 | 19 | 2 | Caption orphaned to new line after price fix | Mechanical (regression) | Corrected in R2 |
| 5 | 19 | 2 | SKU "LMP-2249" now reads "LMP-2429" | Factual (queried) | **Open — held for R3** |
| 6 | 22 | 2 | Double space introduced by hyphenation fix | Mechanical (regression) | Corrected in R2 |

Rows 4-6 exist only because round 2 re-checked full pages, not just marked lines — a marked-lines-only check would have missed all three.

## Systemic-issue escalation threshold

When the same error type recurs 3+ times across a document, stop marking individual instances after the third and instead write one escalation note to the typesetter/template owner:

> "Hyphenation is breaking mid-syllable at the right margin on pages 4, 9, 14, and 22 — same pattern each time (breaks after a double consonant). This looks like a hyphenation-dictionary setting issue rather than four unrelated typos. Recommend checking the InDesign hyphenation exceptions list before the next pass rather than hand-fixing each instance — a fifth or sixth occurrence is likely if the setting isn't the true cause."

This converts a 4-line item correction log into a 1-line root-cause note, and prevents a 7th or 8th instance from slipping through on a later page nobody spot-checked.
