# Red Flags

### Implant screened by device class or brand only, no exact model recorded
- **Usually means:** Screening form was completed quickly under schedule pressure, or the patient couldn't produce a device card and staff didn't chase the model number.
- **First question:** "What is the exact manufacturer and model, and where's that documented — device card, prior op note, cardiology/surgical record?"
- **Data to pull:** Prior operative report, device card photo, cardiology or surgical clinic record, manufacturer implant database lookup.

### Detector or hand-wand flags a patient at the posted gauss threshold and the scan proceeds anyway
- **Usually means:** The flag was assumed to be a false positive under time pressure, or the item was believed already removed.
- **First question:** "Was the patient re-wanded after the flag, and what did the second pass show?"
- **Data to pull:** Screening log timestamp, detector calibration record, incident/near-miss report if one was filed.

### Predicted SAR for an edited sequence checked against the wrong mode's ceiling
- **Usually means:** Technologist recalled the First Level Controlled ceiling (4.0 W/kg) instead of the Normal Operating Mode ceiling (2.0 W/kg) actually active for that patient.
- **First question:** "Which SAR mode is this scanner running in for this patient, and is that documented as intentionally invoked?"
- **Data to pull:** Console mode setting log, physician sign-off record for First Level Controlled mode, sequence-by-sequence SAR log for the exam.

### Gadolinium dose calculated off a prior visit's recorded weight
- **Usually means:** Registration pulled the weight from the last visit's chart instead of a current weigh-in or verbal confirmation.
- **First question:** "When was this patient's weight last actually measured, and does it match what's programmed into the injector?"
- **Data to pull:** Registration weight timestamp, injector programmed volume, patient's stated current weight.

### GFR/creatinine missing or stale (>90 days) before a Group I gadolinium order
- **Usually means:** Renal function wasn't re-checked because the patient "had contrast before with no issue."
- **First question:** "What is the current GFR, and when was it drawn relative to today's exam?"
- **Data to pull:** Most recent basic metabolic panel/creatinine, ordering note, radiologist contrast-eligibility sign-off if GFR is borderline or unavailable.

### A "quench" reported as venting noise with the room re-entered before oxygen levels are confirmed
- **Usually means:** Loud cryogen venting was assumed cosmetic rather than a genuine quench event.
- **First question:** "Has facility engineering confirmed safe oxygen levels in the room before anyone re-enters?"
- **Data to pull:** Oxygen monitor log, engineering incident report, quench-pipe venting confirmation.

### Non-diagnostic sequence sent forward to the radiologist without a repeat attempt
- **Usually means:** Schedule pressure to clear the room outweighed the repeat-while-positioned option.
- **First question:** "Was the patient still on the table and available for an immediate repeat when the artifact was identified?"
- **Data to pull:** Exam timestamp log, sequence QA flag, radiologist's non-diagnostic callback if one was issued.

### Cardiac implantable electronic device scanned without a documented pre- and post-scan interrogation
- **Usually means:** Device rep or cardiology wasn't scheduled in time, and the scan proceeded on the assumption the device was "basically fine either way."
- **First question:** "Where is the pre-scan interrogation record, and who is doing the post-scan re-interrogation before discharge?"
- **Data to pull:** Device interrogation printout (pre and post), cardiology/device-rep sign-off, monitored-parameter log during the scan.

### Same artifact pattern recurring across multiple patients in one day on one scanner
- **Usually means:** Coil, gradient, or shim hardware issue rather than a run of unrelated patient-motion problems.
- **First question:** "Is this the same artifact signature on the same scanner across different patients today?"
- **Data to pull:** QA log across the day's exam list, physics/service ticket history for that scanner.
