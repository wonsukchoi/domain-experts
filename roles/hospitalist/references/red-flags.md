# Red Flags

### Creatinine up >0.3 mg/dL within 48 hours on a patient not previously flagged
- **Usually means:** New acute kidney injury from a nephrotoxic drug (NSAID, IV contrast, vancomycin/aminoglycoside) or intravascular volume depletion from over-diuresis; second most likely is undiagnosed obstructive uropathy in an older patient.
- **First question:** What changed in the last 48 hours — new drug, contrast study, or a diuretic dose increase?
- **Data to pull:** Medication administration record for the window, cumulative net fluid balance for the last 3 days, and a bladder scan if output has dropped.

### LACE index ≥10 with a discharge plan written as "routine follow-up"
- **Usually means:** The discharge plan was written before the risk score was computed, or the score was computed but not translated into a different follow-up cadence — a documentation-process gap, not a clinical oversight.
- **First question:** Has anyone actually recalculated LACE since the day-1 estimate, using today's length of stay and final comorbidity list?
- **Data to pull:** Chart's discharge planning note timestamp vs. the LACE calculation timestamp — if the LACE note postdates the discharge order, the plan wasn't built on it.

### Discharge summary not transmitted within 48 hours of discharge
- **Usually means:** Dictation queued but not signed, or signed but not routed to the correct outpatient physician (wrong PCP on file, no PCP listed at all).
- **First question:** Is there a PCP or accepting outpatient provider on record at all, and is the routing address current?
- **Data to pull:** EHR message log for the discharge summary send event and its delivery/read receipt, not just the "signed" timestamp.

### Patient readmitted within 7 days of discharge for the same or a closely related problem
- **Usually means:** Incomplete resolution at discharge (discharged before the treatment target was actually met) or a medication reconciliation error at the transition; less commonly a genuinely new, unrelated process.
- **First question:** What was the discharge weight/vitals/labs relative to the stated discharge target, and does the readmission diagnosis match the index admission?
- **Data to pull:** Discharge summary's stated discharge criteria vs. the values actually documented on the day of discharge, and a side-by-side of discharge medication list vs. readmission medication list.

### Two or more "call if" parameters triggered by nursing without an order change in the last 12 hours
- **Usually means:** The physician is intentionally watching and waiting, or — more often — the parameters were set once on admission and never revisited as the clinical picture evolved.
- **First question:** When were these parameters last reviewed against the current trajectory, not just the admission-day baseline?
- **Data to pull:** Nursing call log against the order's last-modified timestamp.

### Verbal-only sign-out at shift change with no written I-PASS or equivalent note
- **Usually means:** Time pressure at end of shift, most common on the last shift of a stretch when fatigue is highest.
- **First question:** Can the incoming physician state the illness severity and the action list back in their own words right now, unprompted?
- **Data to pull:** EHR sign-out note's last-edited timestamp relative to actual shift-change time — a note edited days ago for a patient whose status changed today is stale, not current.

### Daily CBC/BMP ordered on a patient with no active issue those labs would change
- **Usually means:** Habitual order-set carryover from admission rather than an active pending decision.
- **First question:** What specific action changes based on today's result that wouldn't happen anyway?
- **Data to pull:** The order history — is this the same standing daily order from admission day, unmodified?

### Padua score not documented and no VTE prophylaxis ordered on a medical admission with reduced mobility
- **Usually means:** Prophylaxis was deferred to the admitting note template default rather than actively risk-stratified.
- **First question:** Has mobility status actually been assessed today, or is it inherited from the admission note?
- **Data to pull:** Current order set for VTE prophylaxis vs. the most recent mobility/nursing assessment.

### Admission status still listed as "pending determination" past hospital day 1
- **Usually means:** The two-midnight expectation was never explicitly documented, leaving the status to be decided retroactively by utilization review or, worse, by an auditor.
- **First question:** Has the medical-necessity line actually been written, separate from the clinical note?
- **Data to pull:** Utilization review's status log and the timestamp of the physician's documented two-midnight determination.

### Family or bedside nurse reports "something's off" while vitals and labs look normal
- **Usually means:** An early, not-yet-quantified deterioration — nursing gestalt frequently precedes measurable change by hours; second possibility is unaddressed pain, anxiety, or delirium not captured by standard vitals.
- **First question:** What specifically changed in the patient's behavior or appearance, in the reporter's own words?
- **Data to pull:** Trend of vitals over the last 12 hours (not just the last set) and a delirium screen (CAM) if not already done today.
