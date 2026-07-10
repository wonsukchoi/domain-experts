# Red Flags

Smell tests for field logs, lab data, and QAQC batches. Format per flag: what it usually means, the first question to ask, the check to run.

### RQD computed using recovered core length as the denominator instead of total drilled run length

- **Usually means:** confusion between the recovery-% formula (recovered/drilled) and the RQD formula (sound pieces ≥10cm/drilled), or logging software defaulting to the wrong field.
- **First question:** "What number did you divide by — the drilled run length or the recovered length?"
- **Data to pull:** the raw run sheet (drilled length, recovered length, sound-piece tally) alongside the reported RQD; recompute by hand against the core box.

### Core recovery below ~90% inside the target interval, lithology logged continuously through the gap

- **Usually means:** the missing material — often the weakest, most fractured, or most altered rock — got silently assumed to match what's above and below it.
- **First question:** "Was the gap logged as a data gap with a probable cause, or interpolated?"
- **Data to pull:** driller's shift log for ground conditions at that depth, core box photos either side of the gap, recovery on the corresponding interval in adjacent holes.

### CRM (standard) result outside ±2 SD of certified value, or outside ±3 SD once

- **Usually means:** lab analytical drift, a mislabeled/mis-inserted standard, or a real batch contamination issue.
- **First question:** "Is this an isolated miss or the second consecutive CRM outside tolerance in this batch?"
- **Data to pull:** the CRM certificate sheet (certified mean and SD), the lab's control chart for that CRM over the last 10 batches, and which real samples bracket the failed standard in the submittal sequence.

### Blank result above 5–10× the lab's stated detection limit

- **Usually means:** cross-contamination in sample prep (crushing/pulverizing equipment not cleaned between high-grade and blank material) rather than a true field or lab issue with real samples.
- **First question:** "What ran through the prep line immediately before and after this blank?"
- **Data to pull:** the lab's prep sequence log for the batch; check whether the elevated blank clusters right after a known high-grade sample.

### Field duplicate pair RPD over ~30% at grades well above detection limit

- **Usually means:** sample heterogeneity (nugget effect) at the collection point, inconsistent splitting technique, or a genuine sampling-representativeness problem, not analytical error.
- **First question:** "Was this duplicate a true field split from the same interval, or two different intervals mislabeled as a pair?"
- **Data to pull:** the field log's split methodology note for that interval, particle size of the material split (coarser material drives worse RPD), and whether other duplicate pairs on the same program show the same pattern.

### Sample bag ID and field-log entry number mismatch discovered at lab receipt

- **Usually means:** the tag was written from memory at end-of-shift instead of at the point of sampling, or two samples were bagged out of sequence.
- **First question:** "When during the shift was this tag written — at collection or afterward?"
- **Data to pull:** the field log's timestamp sequence for that interval and the lab's chain-of-custody receipt sheet; check for an off-by-one pattern across the whole batch, which points to a systematic sequencing error, not one mistake.

### Portable XRF readings reported as final data with no same-shift CRM calibration check logged

- **Usually means:** the instrument's drift over the shift is unknown, so the readings carry unstated uncertainty.
- **First question:** "When was the last CRM check on this unit, and what was the result?"
- **Data to pull:** the instrument's calibration log for the shift; compare against the CRM's certified value and the manufacturer's stated drift tolerance.

### Every core break on a run logged as "mechanical" and rejoined

- **Usually means:** overcorrection after being trained on the mechanical-break issue — genuinely fractured, hazardous ground is being logged as intact, which is worse than the original understatement problem because it masks a real ground-support risk.
- **First question:** "Walk me through the break-surface criteria for the three largest rejoined pieces — texture, orientation, fit."
- **Data to pull:** the annotated break photos; check surface texture and orientation against the D6032 §6.3 criteria, not just piece count.

### Sieve analysis retained-mass total off from starting dry mass by more than ~0.5%

- **Usually means:** transcription error between the balance and the data sheet, or material lost/spilled during sieving.
- **First question:** "Does the discrepancy show up on one sieve or spread across the stack?"
- **Data to pull:** the raw balance printout or photo for each sieve fraction; rerun the sum by hand.

### Downhole deviation survey missing beyond the program's stated interval on an angled hole

- **Usually means:** the survey was skipped to keep the rig running, or the tool malfunctioned and wasn't flagged.
- **First question:** "What's the last confirmed survey depth, and how far below it is this sample interval?"
- **Data to pull:** the survey log against the drilling depth log; estimate azimuth/dip uncertainty accumulated over the un-surveyed interval before trusting any true-depth cross-section built from it.

### Field visual soil classification disagrees with the lab sieve/plasticity result

- **Usually means:** either the field call was made without running the full D2488 field-test sequence (dry strength, dilatancy, toughness), or the sample changed between field collection and lab receipt (drying, segregation in transit).
- **First question:** "Which D2488 field tests were actually run, and is the sample bag intact and unsegregated?"
- **Data to pull:** the field description sheet against the lab gradation/Atterberg results; note the delta for calibration, don't just silently accept the lab number without understanding the miss.
