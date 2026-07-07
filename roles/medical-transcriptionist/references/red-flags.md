# Medical Transcriptionist — Red Flags

### Drug name acoustically ambiguous and dose fits more than one candidate drug's typical range
- **Usually means:** ASR or human mishearing between two sound-alike drugs (e.g., hydralazine/hydroxyzine, clonidine/clonazepam) where the dictated dose doesn't clearly rule either candidate out.
- **First question:** Does the patient's medication history or allergy list elsewhere in the same note independently support one candidate over the other?
- **Data to pull:** Full medication-history section of the current note; prior notes for this patient if accessible in the same encounter.

### Laterality (left/right) stated inconsistently within the same document
- **Usually means:** A dictation slip, an ASR mishearing, or the provider genuinely operating on/examining a different side than earlier stated (rare but must be confirmed, not assumed away).
- **First question:** Does the surgical schedule, consent form, or imaging order (if accessible) confirm the intended side?
- **Data to pull:** Scheduling record for the encounter; any pre-procedure verification documentation.

### Numeric lab or vital-sign value implausible for the stated clinical context
- **Usually means:** ASR digit-substitution error (most common), less often a genuine critical value the provider is specifically calling out.
- **First question:** Does the surrounding dictation treat this as a critical/urgent finding, or does it pass without comment (suggesting the provider didn't intend to say something alarming)?
- **Data to pull:** The specific value against a normal reference range; whether the note's overall tone/plan is consistent with a critical value having occurred.

### Speech-recognition draft reads fluently but a clinical-logic mismatch exists
- **Usually means:** ASR substituted a plausible-sounding wrong word with full grammatical confidence — this is the most dangerous failure mode because it doesn't look like an error on a surface read.
- **First question:** Does this sentence's clinical content actually follow from the diagnosis/procedure stated elsewhere in the note?
- **Data to pull:** Diagnosis and procedure sections of the same document, cross-referenced against the sentence in question.

### Provider's established dictation pattern breaks for the first time
- **Usually means:** Either a genuine change (new medication, different side, updated plan) or a dictation slip — the break itself is the signal, regardless of which.
- **First question:** Is there independent confirmation elsewhere in the record for the new/different statement, or is it a single unconfirmed mention?
- **Data to pull:** Prior notes from the same provider for pattern baseline; current encounter's other documentation for confirmation.

### STAT-flagged report approaching its turnaround deadline with an unresolved query
- **Usually means:** A flagged ambiguity is blocking finalization of a time-critical document and the provider hasn't responded.
- **First question:** Has the query been escalated through a second channel (phone/page) beyond the initial message queue?
- **Data to pull:** Query timestamp, provider response-time SLA for this account, escalation contact.

### Abbreviation with more than one common expansion in context
- **Usually means:** An ambiguous abbreviation (e.g., "MS" for morphine sulfate vs. multiple sclerosis vs. musculoskeletal) dictated without disambiguating context.
- **First question:** Does the rest of the note's clinical context make one expansion clearly correct?
- **Data to pull:** Diagnosis list and current-medications section of the same note.

### Silent-correction rate unusually high for a single transcriptionist or account in a QA sample
- **Usually means:** Either genuinely low ambiguity in that provider's dictation style, or the transcriptionist is under-flagging to hit a turnaround-time target.
- **First question:** Does the QA sample's flagged-vs-silent ratio match the account's historical baseline?
- **Data to pull:** QA audit sample with error-severity classification (clinically-significant vs. stylistic), compared against account baseline.
