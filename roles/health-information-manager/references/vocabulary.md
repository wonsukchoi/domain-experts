# Vocabulary

Terms of art in health information management and cancer/disease registry work, with the misuse a generalist commonly makes.

### Multiple Primary and Histology (MPH) Rules

SEER's site-specific rule set for deciding whether a second tumor is a new primary or a continuation of the first, based on site, histology grouping, and (for non-paired organs) timing.
**In use:** "The interval doesn't matter here — this is a paired-organ site, so it's multiple primaries under the MPH breast rule regardless of when the second tumor showed up."
**Common misuse:** Treating "same histology, short interval" as sufficient evidence of a single primary — the MPH rules override that intuition for specific site/organ combinations.

### Class of Case

A registry code (00–99 range) indicating whether and how a case is reportable at a given facility — whether it was diagnosed and/or treated there, and whether any part of first-course treatment happened elsewhere.
**In use:** "This is a Class of Case 21 — diagnosed elsewhere, first course of treatment here — so we abstract it but the diagnosis date traces to the outside facility's pathology report."
**Common misuse:** Assuming "the patient was seen here" is sufficient to make a case reportable and abstractable, without checking whether it meets the facility's actual class-of-case and reportability criteria.

### Analytic case

A cancer registry case where the diagnosis and/or all or part of first-course treatment occurred at the reporting facility, as opposed to a non-analytic case (diagnosed and treated entirely elsewhere, reported for informational purposes only).
**In use:** "Follow-up rate is measured against analytic cases only — the non-analytic cases don't count in that denominator."
**Common misuse:** Applying accreditation follow-up and timeliness benchmarks to the whole caseload instead of the analytic subset, which understates actual performance.

### Reportability

Whether a diagnosis meets the criteria (specific site, histology, and behavior codes) that a central or facility registry is required to collect, per NAACCR/state reporting rules.
**In use:** "Basal cell carcinoma of the skin isn't reportable to most central registries — don't put it in the case-finding queue."
**Common misuse:** Assuming "cancer" and "reportable" are synonyms; several diagnoses that are clinically malignant are explicitly excluded from standard reportability lists.

### Master Patient Index (MPI) / Enterprise Master Patient Index (EMPI)

The system of record matching every patient identifier and encounter to a single unique patient across one facility (MPI) or an entire health system/network (EMPI).
**In use:** "The EMPI match came back probabilistic, not deterministic — route it to manual review before merging."
**Common misuse:** Treating the MPI as a background IT system rather than a governed clinical-safety asset; a wrongful merge or an unresolved duplicate is a patient-safety incident, not an IT ticket.

### Deterministic vs. probabilistic matching

Deterministic matching requires exact agreement on specified identifiers (e.g., SSN + DOB + last name); probabilistic matching assigns a weighted confidence score across multiple partially-matching fields.
**In use:** "We don't auto-merge probabilistic matches below our validated confidence threshold — those go to a human reviewer."
**Common misuse:** Assuming a high probabilistic score is equivalent to a deterministic match for auto-merge purposes; the two carry different wrongful-merge risk profiles and should have different review requirements.

### Data Quality Management (DQM) Model

AHIMA's framework naming the specific dimensions of data quality (accuracy, accessibility, comprehensiveness, consistency, currency, definition, granularity, precision, relevancy, timeliness) so a defect can be named precisely instead of generically.
**In use:** "This isn't an accuracy problem — it's a granularity problem: the field captures 'diabetes' when the quality measure needs the ICD-10-CM subtype."
**Common misuse:** Calling every defect a generic "data quality issue" without naming which dimension actually failed, which makes the fix impossible to scope.

### Information Governance (IG)

The organization-wide framework establishing who has decision rights over data definitions, retention, access, and structural changes to the record — distinct from IT governance (systems) or clinical governance (care quality).
**In use:** "That's an IG decision, not an IT one — retiring this field needs governance-committee sign-off even though IT could technically do it in an afternoon."
**Common misuse:** Conflating information governance with IT governance or with a data dictionary; IG is about decision rights and accountability, not a technical inventory.

### USCDI (US Core Data for Interoperability)

The ONC-designated minimum set of data classes and elements required to be exchangeable between certified health IT systems.
**In use:** "USCDI requires this element be structured and exchangeable — but that's a transport requirement, not a guarantee the underlying value was captured correctly."
**Common misuse:** Treating USCDI/FHIR conformance as proof of data quality; standardized transport of a bad value is still a bad value.

### Minimum necessary standard

HIPAA's requirement that a disclosure include no more protected health information than the specific request or purpose justifies — the default for nearly every disclosure except the patient's own request for their own record.
**In use:** "The subpoena covers the orthopedic encounter only — minimum necessary means we don't send the whole chart."
**Common misuse:** Sending the entire record because it's simpler than reviewing scope, or because the requester "would have gotten it eventually."

### AJCC Stage Group

The overall cancer stage (e.g., Stage IA, IIA) derived by combining T (tumor extent), N (nodal involvement), and M (metastasis) categories per the AJCC Cancer Staging Manual's site-specific stage-grouping tables.
**In use:** "T2N0M0 for this site groups to Stage IIA — check the site-specific table, the grouping isn't the same across every cancer type."
**Common misuse:** Assuming T/N/M-to-stage-group logic is universal across cancer sites; the combination tables are site-specific and don't generalize.

### Case-finding

The systematic process of identifying every reportable case from all facility sources (pathology, radiation oncology, medical oncology, death certificates, outside referrals) before abstracting begins.
**In use:** "Our case-finding source list hasn't been reconciled against the outreach lab in over a year — that's a silent under-ascertainment risk, not an abstracting backlog."
**Common misuse:** Equating case-finding completeness with abstracting throughput; a registry can be fully caught up on abstracting while still missing cases because a source feed was never onboarded or quietly broke.

### Legal Health Record (LHR)

The formally defined subset of the full patient record designated as the official business record released in response to legal requests and audits — as distinct from the "designated record set" under HIPAA, which is broader.
**In use:** "That draft note isn't part of the Legal Health Record — it doesn't go out under a standard records request."
**Common misuse:** Assuming everything in the EHR is automatically part of the Legal Health Record; facilities define the LHR's scope explicitly, and it excludes certain draft or non-clinical content.

### Duplicate record vs. overlaid record

A duplicate is two separate medical record numbers for the same patient; an overlay is one record number incorrectly containing two different patients' data — the second is the more dangerous error because it isn't caught by duplicate-detection logic.
**In use:** "This isn't a duplicate-rate problem, it's an overlay — someone else's labs are inside this chart, which is worse and needs an immediate unmerge, not a routine merge review."
**Common misuse:** Using "duplicate" and "overlay" interchangeably; they require different detection methods and different urgency.

### Follow-up rate (registry)

The percentage of analytic cases for which the registry has current vital-status/disease-status information, tracked via mailed follow-up letters, physician contact, or National Death Index linkage — a Commission on Cancer accreditation benchmark.
**In use:** "Follow-up rate dropped below benchmark because we haven't run an NDI linkage batch since last year, not because patients stopped responding."
**Common misuse:** Treating a low follow-up rate purely as a patient-responsiveness problem rather than a process gap (missed NDI linkage cycles, outdated contact information never refreshed).
