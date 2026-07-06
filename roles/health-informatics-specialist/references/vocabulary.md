### eCQM (Electronic Clinical Quality Measure)
A quality measure specification designed to be calculated automatically from structured EHR data, defined by a measure steward (e.g., CMS) with precise numerator, denominator, and exclusion logic.
**In use:** "The A1c control eCQM's denominator requires patients 18-75 with a diabetes diagnosis and a qualifying encounter."
**Common misuse:** Approximating a measure's numerator/denominator/exclusion logic rather than following the steward's exact specification, which can materially shift the reported rate.

### HEDIS (Healthcare Effectiveness Data and Information Set)
A set of standardized performance measures developed by NCQA, widely used by health plans to report quality and effectiveness of care.
**In use:** "This measure follows HEDIS technical specifications for the reporting year."
**Common misuse:** Treating HEDIS and eCQM specifications as interchangeable when they can have different technical requirements even for similarly named measures.

### Structured data (coded data)
Clinical information captured in a standardized, discrete field using a controlled vocabulary (e.g., a LOINC-coded lab result, an ICD-10-coded diagnosis), as opposed to free text or scanned documents.
**In use:** "The A1c result needs to be captured as structured, LOINC-coded data, not just noted in a progress note."
**Common misuse:** Assuming a clinical fact documented anywhere in the chart (including free text or scanned attachments) is automatically available to an automated quality measure calculation, which typically only reads structured/coded fields.

### LOINC (Logical Observation Identifiers Names and Codes)
A standardized vocabulary for identifying laboratory and clinical observations, used to enable interoperable exchange of lab results across systems.
**In use:** "This lab test needs to be mapped to its correct LOINC code before it will transmit meaningfully to the receiving system."
**Common misuse:** Assuming a hospital's internal lab code is automatically understood by an external system without an explicit, correct LOINC mapping.

### SNOMED CT
A comprehensive clinical terminology standard covering diagnoses, findings, procedures, and other clinical concepts, used for structured documentation and interoperability.
**In use:** "The diagnosis needs a SNOMED CT code for this decision support rule to trigger correctly."
**Common misuse:** Relying on free-text diagnosis entry without a coded SNOMED CT (or ICD-10) equivalent, which prevents automated systems (measures, alerts) from recognizing the diagnosis.

### RxNorm
A standardized nomenclature for clinical drugs, used to enable interoperable exchange of medication information across systems.
**In use:** "The medication list needs RxNorm codes to support accurate drug-interaction checking across systems."
**Common misuse:** Relying on a local or brand-specific medication naming convention without mapping to RxNorm, causing medication-related decision support or interoperability to miss matches.

### Clinical decision support (CDS) alert
A system-generated prompt within an EHR intended to guide clinical decision-making at the point of care, such as a drug interaction warning or a preventive care reminder.
**In use:** "This CDS alert fires whenever a new prescription conflicts with an existing medication."
**Common misuse:** Designing alerts broadly enough that they fire on low-risk or already-considered situations, contributing to alert fatigue and high override rates.

### Alert fatigue
The phenomenon where clinicians, overwhelmed by frequent or overly broad alerts, begin dismissing them reflexively without evaluating their clinical relevance each time.
**In use:** "The 94% override rate on this alert is a clear sign of alert fatigue, not a training gap."
**Common misuse:** Responding to a high alert override rate with clinician retraining or compliance messaging instead of redesigning the alert's specificity.

### HL7 v2
An older, widely used healthcare messaging standard using pipe-delimited segments to exchange clinical data (e.g., admission/discharge/transfer messages) between systems.
**In use:** "The ADT message in HL7 v2 format needs to be mapped to the equivalent FHIR resource for the new interface."
**Common misuse:** Assuming HL7 v2 messages map field-for-field to FHIR resources without validating the underlying data model differences.

### FHIR (Fast Healthcare Interoperability Resources)
A modern healthcare interoperability standard using RESTful web services and structured resources (typically in JSON or XML) to exchange clinical data.
**In use:** "The new integration uses FHIR resources instead of HL7 v2 messages for exchanging patient data."
**Common misuse:** Treating a FHIR integration as a drop-in replacement for an existing HL7 v2 interface without validating that all needed clinical concepts map correctly between the two standards.

### Numerator / denominator / exclusion (measure logic)
The precise components of a quality measure specification: the denominator defines the eligible population, the numerator defines the subset meeting the quality criterion, and exclusions remove specific patients from consideration for defined clinical reasons.
**In use:** "The exclusion criteria remove hospice patients from the denominator before calculating the rate."
**Common misuse:** Applying a general or approximate understanding of who should be included/excluded rather than following the measure steward's precise, literal specification.
