# Food Science Technician — Vocabulary

Working vocabulary generalists (production floor, front office) reliably misuse. Format per term: definition, how a technician actually uses it, the common misuse.

## Calibration vs. verification

- **Definition:** Calibration adjusts an instrument against a known reference to correct its readings; verification is a check, without adjustment, that confirms the instrument is still reading correctly right now.
- **Practitioner usage:** "The meter's calibrated on schedule, but I still verify against the buffer at the start of every run — calibration tells you it was right yesterday, not right now."
- **Common misuse:** Treating "it's on the calibration schedule" as equivalent to "it's correct today." An instrument can be scheduled-current and still drifted enough to matter between checks.

## Accuracy vs. precision

- **Definition:** Accuracy is how close a result is to the true value; precision is how close repeated results are to each other, regardless of whether they're close to the true value.
- **Practitioner usage:** "Triplicate came back 0.834/0.836/0.839 — tight precision — but if the instrument's out of tolerance, all three could be precisely wrong."
- **Common misuse:** Citing tight replicate agreement alone as proof a result is "good," without a calibration/verification check confirming the instrument isn't consistently biased.

## Out-of-spec (OOS) vs. out-of-trend (OOT)

- **Definition:** OOS means a single result falls outside the defined specification limit. OOT means a result, while still inside spec, breaks the established pattern for that process (a control-chart signal).
- **Practitioner usage:** "It's not OOS, it's OOT — still inside the 0.85 limit, but it's the seventh point trending up, and that's worth a look before it becomes OOS."
- **Common misuse:** Only tracking OOS and ignoring OOT, which discards the earlier and cheaper warning signal a control chart exists to provide.

## Retain sample vs. reserve sample

- **Definition:** A retain sample is held from a specific production lot for the shelf-life period, for retest or investigation purposes. A reserve sample (sometimes used interchangeably in casual speech, but distinct in a validated system) is held specifically to support a recall investigation or regulatory request.
- **Practitioner usage:** "Pull from the retain for the OOS retest — don't touch the reserve, that's earmarked for a possible regulatory pull."
- **Common misuse:** Using the two terms interchangeably in casual conversation, which in an audited system can mean pulling from the wrong sample population and breaking the chain of custody for whichever purpose the untouched sample was reserved for.

## Chain of custody

- **Definition:** The documented, unbroken record of who collected a sample, when, and every subsequent handling/storage step until it's tested or discarded.
- **Practitioner usage:** "The result's not usable — there's a four-hour gap in the storage log between receiving and testing, chain of custody's broken."
- **Common misuse:** Treating chain of custody as a paperwork formality rather than a precondition for the result meaning anything; a broken chain invalidates an otherwise perfectly executed test.

## Environmental monitoring zones (Zone 1–4)

- **Definition:** A tiered classification of surfaces by proximity to exposed product — Zone 1 is direct food contact, Zone 4 is outside the processing area entirely — used to scope pathogen-surveillance swabbing.
- **Practitioner usage:** "It's a Zone 3 positive, not Zone 1 — no immediate line stop, but it goes into the vector-swabbing investigation before we close it out."
- **Common misuse:** Treating a Zone 2/3 positive as low-urgency because it isn't touching product yet, missing that it signals a harborage point that can migrate toward Zone 1 over time.

## Corrective action vs. preventive action (CAPA)

- **Definition:** Corrective action addresses the root cause of a problem that already occurred; preventive action addresses a potential problem identified before it occurs (e.g., from a trend or near-miss).
- **Practitioner usage:** "Retraining on SOP-114's equilibration step is the corrective action for this deviation; adding a chamber-timer alarm to prevent early reads on every unit is the preventive action."
- **Common misuse:** Filing a corrective action that only fixes the immediate instance (retrain one person) without a preventive action addressing the systemic gap (no alarm, so the next rushed technician makes the same error).

## Triangle test vs. duo-trio test

- **Definition:** Both are forced-choice sensory difference tests. The triangle test presents three coded samples (two identical, one different) with a 1-in-3 chance of a correct guess; the duo-trio test presents a reference plus two coded samples with a 1-in-2 guess chance.
- **Practitioner usage:** "We ran a triangle, not duo-trio, specifically because the 1-in-3 guess rate needs fewer panelists to reach significance than the duo-trio's 1-in-2."
- **Common misuse:** Treating the two as interchangeable "difference tests" without accounting for the different required panelist counts and significance tables each one uses.

## Positive control / negative control

- **Definition:** A positive control is a sample known to produce a positive result, run alongside test samples to confirm the method/reagent is working; a negative control is known to produce a negative result, confirming the method isn't producing false positives.
- **Practitioner usage:** "Plate came back all-negative, but so did the positive control — that's a dead reagent lot, not a clean batch."
- **Common misuse:** Skipping the positive-control run to save time, which means an all-negative micro result can't be distinguished from a failed test.

## HorRat (Horwitz ratio)

- **Definition:** The ratio of a method's observed reproducibility (RSDr, relative standard deviation) to the value predicted by the Horwitz equation for that analyte concentration — a normalized way to judge whether a method's precision is reasonable for the level being measured.
- **Practitioner usage:** "HorRat's running about 1.1 on this assay, which is within the 0.5–2.0 band AOAC treats as acceptable — the precision's fine even though the raw RSD looks high at this trace concentration."
- **Common misuse:** Judging a method's precision by a fixed %RSD threshold regardless of concentration, when the Horwitz relationship predicts naturally higher %RSD at trace levels — a raw RSD that looks alarming can still be a HorRat well within range.

## Composite sample vs. grab sample

- **Definition:** A composite sample combines multiple sub-samples (across time, location, or units) into one representative sample; a grab sample is a single sample taken at one point in time/location.
- **Practitioner usage:** "Moisture spec is checked on a composite across the batch because a grab sample from one spot won't catch mix inhomogeneity."
- **Common misuse:** Using a grab sample result to characterize an entire batch for a parameter (like moisture in an unevenly mixed product) that's known to vary within the batch, then treating a local anomaly as a batch-wide failure or pass.
