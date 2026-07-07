# Word Processor / Typist — Playbook

## Numbers/names/dates verification pass (run separately from the general read-through)

| Element type | What to check against | Common failure mode |
|---|---|---|
| Dollar amounts | Source document/contract, not the dictated round-off | Dictated round number vs. a more precise figure elsewhere in the file |
| Proper names | Prior correspondence history, spelling given at first mention | Homophone-plausible misspelling (Kessler/Kessner, Stephen/Steven) |
| Dates | Source document; internal consistency (does "next Tuesday" match a stated date?) | Transcribing a relative date literally without resolving it to an actual date |
| Case/file numbers | Source document, not memory of "similar" numbers from other files | Transposed digits, especially in sequences of 4+ digits |

## Version-reconciliation checklist

1. List every draft file in circulation for this document (by filename, modified date, and any embedded comments).
2. Identify whether any file contains an explicit sign-off (a reviewer's initialed comment, an email confirming "approved," a version marked "FINAL" by the actual approver — not just filename text).
3. If two files conflict and only one has a sign-off, the signed-off version wins regardless of which is more recently modified.
4. If no file has an explicit sign-off, do not guess — flag to the requester and hold.
5. Once resolved, note which source file was used in the delivery note, so the next person doesn't have to redo this reconciliation.

## Style-template application order

1. Apply built-in paragraph/character styles (heading levels, body text, block quotes) rather than manual formatting — this is what makes a template-wide change (e.g., "make all headings blue") a five-second fix instead of a per-paragraph hunt.
2. Match numbering/lettering schemes to the document's established pattern (don't restart or switch schemes mid-document without a clear structural reason).
3. Match table formatting (borders, header shading, column-width conventions) to prior tables in the same document or template.
4. Only after styles are applied, do a manual-formatting sweep to catch anything a style couldn't cover (e.g., an inline emphasis that isn't part of the template's character styles) — and keep this list short; manual overrides should be the exception, not the norm.

## Ambiguity-flagging format (dictation/handwriting)

```
Flagged at [location/timestamp]: dictation/handwriting reads as "[best guess]"
Alternative reading(s): "[alternative]"
Why ambiguous: [audio unclear / handwriting could be either / context doesn't resolve it]
Action needed: confirm before finalizing
```

Filled example (from the worked example in SKILL.md):

```
Flagged at 4:12 in dictation: "cc: J. Kessler"
Alternative reading: "cc: J. Kessner"
Why ambiguous: file has correspondence history for both names on different matters
Action needed: confirm correct recipient before sending — cc field left blank pending confirmation
```

## Delivery note template

```
Produced from: [exact source filename/version]
Approved-version basis: [what confirms this is the right source — reviewer comment, sign-off email, explicit confirmation]
Open items: [anything still needing author confirmation, or "none"]
Style/template used: [template name/version, any noted deviations]
```
