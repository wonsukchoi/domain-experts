# Proofreader / Copy Marker — Red Flags

### Round-1 error rate above roughly 1 error per page on a document that's supposedly proof-ready
- **Usually means:** the file skipped or rushed a copyedit pass, or was re-typeset from a corrected file that reintroduced old errors.
- **First question:** "Was this file copyedited, or did it come straight from layout after a content change?"
- **Data to pull:** the editorial-pass history/version log for this document.

### A correction-verification round finds zero new issues on a document with significant layout changes
- **Usually means:** the checker only re-read the marked lines instead of the full pages the corrections sit on — regressions are common enough that "zero found" on a heavily-revised document is itself suspicious.
- **First question:** "Did the check cover the full page around each correction, or just the marked line?"
- **Data to pull:** which pages had layout shifts (text reflow, caption repositioning) from the round-1 corrections.

### The same error type appears on 3 or more pages
- **Usually means:** a template, style-sheet, or hyphenation-dictionary setting problem, not N unrelated human errors.
- **First question:** "Is this the same root cause repeating, or genuinely unrelated instances?"
- **Data to pull:** the correction log filtered by error description, sorted by page.

### A number, name, date, or price "looks wrong" but there's no independent source to check it against
- **Usually means:** either a genuine error that needs the author/editor to confirm, or a correct-but-unusual figure the proofreader lacks context for (a per-unit price on a bulk item, a foreign-market date format).
- **First question:** "Is there a source document (price list, style sheet, prior edition) I can check this against before querying it?"
- **Data to pull:** the reference source for the figure in question, if one exists.

### A query from a prior round has no response and the deadline is approaching
- **Usually means:** the query got lost in email, or the person who can answer it is unavailable — not that it's resolved.
- **First question:** "Has anyone actually confirmed this, or did the deadline just arrive?"
- **Data to pull:** the query log with response status, not just the correction log.

### The document is a final pre-press file (blueline/press-ready PDF) and a price, date, or legal-disclaimer field hasn't been independently double-checked
- **Usually means:** the zero-tolerance items got the same scrutiny as routine text instead of a dedicated verification pass.
- **First question:** "Has every price/date/disclaimer field on this page been checked against its source independently of the general read-through?"
- **Data to pull:** a checklist of all price/date/legal fields on the document, separate from the general proof mark-up.

### A proofreader is rewriting sentences rather than marking-and-querying
- **Usually means:** scope creep from proofreading into editing, which reintroduces the risk the earlier edit passes were meant to close out.
- **First question:** "Is this a factual/mechanical correction, or a style rewrite that should go back to the editor?"
- **Data to pull:** the specific mark and whether it changes meaning/wording beyond a factual or mechanical fix.

### Sign-off happens with open queries still unresolved elsewhere in the document
- **Usually means:** schedule pressure is overriding the hold-for-open-queries rule.
- **First question:** "Which pages have open queries, and were they excluded from this sign-off?"
- **Data to pull:** the query log's open/resolved status at the moment of sign-off.

### A correction was applied to the wrong instance of a repeated term/number
- **Usually means:** a find-and-replace was used without scoping it to the specific flagged instance, silently changing a different, correct instance elsewhere.
- **First question:** "Was this correction applied by search-and-replace across the whole document, or only at the marked location?"
- **Data to pull:** every other occurrence of the changed term/number in the document, checked post-correction.
