# Data Entry Keyer — Red Flags

### Exception-flag rate drops sharply (>50%) while keying speed rises in the same period
- **Usually means:** Ambiguous fields being resolved by guess instead of flagged, to protect throughput numbers; less often, a genuine process/template improvement.
- **First question:** What changed — a new template with clearer fields, or just pressure to hit quota?
- **Data to pull:** Shift-level flag-rate and speed trend over 4-6 weeks; a genuine improvement shows a gradual, explainable trend, not a sudden step change.

### A single field accounts for >3x its share of a batch's key-verification discrepancies
- **Usually means:** A form-design or template ambiguity (unclear format, no input mask), not a keyer-performance issue.
- **First question:** Is this field handwritten, low-contrast, or ambiguous in a way the other fields aren't?
- **Data to pull:** The field's discrepancy log against source images — look for a shared misreading pattern, not random scatter.

### Two independently keyed values match but both are inconsistent with an adjacent field
- **Usually means:** A shared misreading of a genuinely ambiguous source character/format — key-verification defends against random error, not shared misreading.
- **First question:** Would a different keyer, reading fresh, plausibly make the same misread?
- **Data to pull:** The source-document image and any cross-referenceable adjacent field that could confirm or contradict the keyed value.

### A keyer's exception-flag rate is a statistical outlier — far above or far below the team average
- **Usually means (below average):** Guessing instead of flagging. **Usually means (above average):** Genuinely harder assigned documents, or appropriately conservative flagging — not necessarily a problem.
- **First question:** Is this keyer assigned a harder document mix, or the same mix as peers?
- **Data to pull:** Document-type assignment log alongside the flag-rate comparison — an outlier on the same document mix as peers needs a different conversation than one on a harder mix.

### A batch fails full-verification threshold and is spot-checked instead of fully re-verified
- **Usually means:** Time pressure overriding the documented QC procedure.
- **First question:** Was the Re threshold actually crossed, or is this a borderline Ac/Re case needing a judgment call?
- **Data to pull:** The defect count from the sample against the batch's Ac/Re thresholds (see playbook.md's acceptance-sampling table).

### A new source-document template goes into full-speed production without a reduced-speed pilot batch
- **Usually means:** The error-rate baseline for the new format is unknown, so any elevated error rate won't be caught until it's already in a full batch.
- **First question:** Has this template — or a close variant — run in production before, with a known error profile?
- **Data to pull:** Prior error-rate history for this exact template, if any exists.

### An "independent" double-key verification shows suspiciously few discrepancies given the field's known difficulty
- **Usually means:** The second keyer referenced the first keyer's entry (defeating the independence of the check) rather than genuinely re-keying blind.
- **First question:** Did the second keyer have visual or system access to the first entry while keying?
- **Data to pull:** The verification-system's workflow log — confirm the second entry was keyed without the first entry visible.

### Missing or blank fields are being filled with a default/placeholder value instead of flagged
- **Usually means:** A well-intentioned attempt to "complete" the record that actually destroys the information that the field was genuinely blank or illegible on the source.
- **First question:** Is there a documented rule authorizing this specific inference, or is this an unauthorized guess?
- **Data to pull:** The organization's documented exception-handling procedure — check whether this substitution is an authorized rule or an ad hoc choice.
