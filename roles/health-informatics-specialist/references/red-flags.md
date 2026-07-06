### A quality measure rate is calculated from structured EHR data with no check for relevant unstructured/scanned documentation
- **Usually means:** Results documented only as scanned attachments or free text are invisible to the automated calculation, potentially undercounting the true numerator.
- **First question:** Has a manual chart review sample been run to check whether relevant results exist outside the structured/coded fields the automated calculation reads?
- **Data to pull:** Sample of non-numerator patient charts, checking for relevant results in unstructured/scanned form.

### A measure specification's exclusion criteria weren't checked against a sample of denominator patients
- **Usually means:** Patients who should be excluded (per the steward's specification) may be incorrectly included, or vice versa, materially skewing the reported rate.
- **First question:** Has a sample of denominator patients been manually checked against every exclusion criterion in the measure steward's specification?
- **Data to pull:** Measure steward's exact exclusion criteria, sample of denominator patient charts.

### A clinical decision support alert has an override rate above roughly 90%
- **Usually means:** Alert fatigue — clinicians are dismissing the alert reflexively rather than evaluating it each time, which is itself a patient safety concern regardless of the alert's original intent.
- **First question:** What specific criteria trigger this alert, and could they be narrowed to target only the subset of cases where the alert is actually clinically actionable?
- **Data to pull:** Alert firing and override rate data, criteria driving alert triggers.

### A newly implemented CDS alert's override rate hasn't been reviewed since go-live
- **Usually means:** Alert fatigue may already be developing without anyone checking, since override rates typically need to be actively monitored rather than assumed acceptable by default.
- **First question:** When was this alert's override rate last reviewed, and what was the trend?
- **Data to pull:** Historical override rate data since implementation.

### An interoperability exchange shows a data element as "missing" from a source system known to actually capture it
- **Usually means:** A terminology/code-mapping gap (e.g., a local lab code not mapped to LOINC) is a more likely explanation than a genuine data gap.
- **First question:** Is the local code for this data element correctly mapped to the standard vocabulary required for the exchange?
- **Data to pull:** Local code and its mapping (or lack of mapping) to the standard vocabulary (LOINC/SNOMED CT/RxNorm).

### An HL7 v2 to FHIR (or similar) system integration maps fields one-to-one without validation against real message samples
- **Usually means:** The two standards' different data models could cause silent data loss or misinterpretation for concepts that don't map directly field-to-field.
- **First question:** Has this mapping been validated against actual message samples from both systems, or only against the specification documents?
- **Data to pull:** Sample HL7 v2 messages and their corresponding FHIR resource output for the same clinical events.

### A quality measure report doesn't document its methodology or known data limitations
- **Usually means:** Downstream users of the report may rely on the number beyond what the underlying data actually supports.
- **First question:** Does the report state which data elements were included, their structured/unstructured status, and any known gaps?
- **Data to pull:** The report's methodology section (or its absence).

### A discrepancy found in a manual validation sample isn't extrapolated to the full population
- **Usually means:** The true scale of a data quality issue may be understated if the sample finding is treated as an isolated case rather than projected across the relevant population.
- **First question:** What is the discrepancy rate found in the sample, and has it been extrapolated to estimate the full population's likely true rate?
- **Data to pull:** Sample size, discrepancy count, total relevant population size.
