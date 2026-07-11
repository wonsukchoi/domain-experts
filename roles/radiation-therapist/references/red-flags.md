# Radiation Therapist — Red Flags

### CBCT/portal setup shift exceeding the site's single-fraction action level (commonly >5mm translational for conventional treatment, >1–2mm for SRS/SBRT)
- **Usually means:** Random day-to-day setup variance; second most likely, a true anatomic change (bladder/rectal filling, weight loss, tumor response, edema).
- **First question:** Is this an isolated outlier, or does it follow the same direction as the shifts on the prior 2–3 fractions?
- **Data to pull:** Shift-magnitude/direction log for the last 3–5 fractions; weight and anatomy notes since simulation; physicist/physician notification record.

### Sustained same-direction shift trend over 3+ consecutive fractions, even when each individual shift stays within the action level
- **Usually means:** Anatomic change in progress (rectal/bladder filling pattern, tumor shrinkage, weight loss) that will eventually cross the action level if unaddressed.
- **First question:** What does the CBCT show has physically changed compared with the simulation-day and fraction-1 reference images?
- **Data to pull:** Cumulative shift log plotted by fraction; bowel-prep/bladder-filling compliance; physician flag for possible replan.

### Skin or mucosal reaction reaching CTCAE grade ≥3 (confluent moist desquamation, bleeding with minor trauma) earlier than the site/fractionation's typical dose milestone
- **Usually means:** Individual radiosensitivity or a comorbidity (diabetes, smoking, concurrent chemotherapy); second most likely, a bolus, setup, or dose-delivery error concentrating dose to skin.
- **First question:** Is the reaction distributed as expected for the treated field, or does its location suggest a geographic miss or bolus placement issue?
- **Data to pull:** Field/bolus documentation for the fraction(s) in question, cumulative skin dose if calculable, prior grade trajectory.

### Cumulative delivered fractions or dose not matching the prescription at a scheduled chart-check milestone
- **Usually means:** Missed fractions from patient no-shows, illness, or machine downtime without a documented makeup plan.
- **First question:** Is there a physician-approved makeup plan on file, and does it preserve the intended overall treatment time?
- **Data to pull:** Record-and-verify fraction/dose count, missed-day log with reasons, physician gap-management note.

### Patient-reported acute symptom (new pain, bleeding, neurologic change) inconsistent with the expected toxicity timeline for the current fraction and site
- **Usually means:** Expected toxicity presenting atypically early; second most likely, a geographic miss, wrong-field delivery, or an unrelated new pathology.
- **First question:** Does the symptom's location and timing match the treated field and the expected dose-response curve for this site?
- **Data to pull:** Treated-field documentation for recent fractions, imaging comparison to reference, physician same-day notification.

### Daily machine QA reading (output constancy, laser alignment, imaging isocenter) trending toward but not yet crossing the TG-142 tolerance limit over consecutive days
- **Usually means:** Gradual beam or mechanical drift that will cross tolerance if not recalibrated; second most likely, a measurement or environmental artifact (temperature/pressure not corrected).
- **First question:** Is today's reading part of a multi-day trend, or an isolated fluctuation within normal day-to-day variation?
- **Data to pull:** Physicist's QA trend log against the tolerance table, environmental correction factors, last full calibration date.

### Immobilization device that is visibly loose, warped, or ill-fitting compared with the simulation-day fit
- **Usually means:** Patient weight change since simulation; second most likely, device degradation from repeated use (thermoplastic mask stretching, cushion compression).
- **First question:** How much has the patient's weight changed since simulation, and is the fit failure affecting measurable setup reproducibility on imaging?
- **Data to pull:** Weight log since simulation, shift-magnitude trend since the fit issue was first noticed, physician/physicist resimulation decision.

### Two-identifier or pre-beam time-out check skipped, rushed, or disagreeing between staff
- **Usually means:** Workflow shortcut under schedule pressure — the single highest-risk precursor to a wrong-patient or wrong-site delivery.
- **First question:** What specifically caused the check to be skipped or rushed — scheduling pressure, unfamiliarity with the patient, or a system/interface issue?
- **Data to pull:** Time-out compliance audit for the unit/shift, schedule density at the time of the incident, staffing level.

### Imaging frequency delivered does not match the physician-ordered protocol (daily CBCT ordered but only weekly performed, or extra imaging beyond the order with no documented reason)
- **Usually means:** Workflow/scheduling lapse; second most likely, unnecessary imaging dose creep from over-cautious re-imaging without a protocol basis.
- **First question:** What does the physician's order actually specify for this patient, and does the delivered imaging log match it?
- **Data to pull:** Physician imaging order, imaging log by fraction, cumulative imaging dose if the mismatch is toward over-imaging.

### A boost field, replan, or physician-ordered plan change not yet reflected as the active plan in the record-and-verify system before the next fraction
- **Usually means:** Plan-transfer or communication lapse between planning/dosimetry and the treatment unit — carries direct risk of treating the wrong field or dose.
- **First question:** Has the new plan been physically approved and locked in the record-and-verify system, or only verbally communicated?
- **Data to pull:** Plan approval timestamp and approver, R&V system active-plan field, physician/dosimetrist sign-off documentation.
