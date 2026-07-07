# Clinical Data Manager — Vocabulary

### Query
A formal, tracked request to a site to confirm or correct a specific data point, with a stated discrepancy and due date.
**In use:** "That transposed dosing date needs a query against site 07, not a silent correction."
**Common misuse:** Generalists treat "query" as a synonym for "question" — a query is a specific auditable workflow object with an open/resolved lifecycle, not an informal ask.

### Edit check
A programmed rule in the EDC that flags a data value as potentially erroneous (range check, cross-form logic check, missing-value check).
**In use:** "The edit check on baseline creatinine only fires above 1.5 mg/dL — anything below that slips through unflagged."
**Common misuse:** Assuming edit checks catch all data errors; they only catch the error classes they were explicitly written to detect.

### CRF / eCRF
Case Report Form / electronic Case Report Form — the structured form a site uses to record protocol-required data for each subject/visit.
**In use:** "The eCRF's adverse event page needs a conditional field for severity grading before this can go live."
**Common misuse:** Treating the CRF as a data-entry convenience rather than the contractual data-collection instrument defined by the protocol — every field traces back to a protocol requirement.

### CDASH
Clinical Data Acquisition Standards Harmonization — a CDISC standard for naming and structuring CRF fields to align with downstream SDTM mapping.
**In use:** "Build the new CRF to CDASH so SDTM mapping is mechanical instead of a rebuild."
**Common misuse:** Confusing CDASH (collection-stage standard) with SDTM (submission-stage standard) — they serve different points in the pipeline.

### SDTM
Study Data Tabulation Model — the CDISC standard format regulators expect for submitted trial datasets.
**In use:** "This CRF field doesn't map cleanly to an SDTM domain — that's going to be a manual reconciliation burden every analysis cycle."
**Common misuse:** Assuming SDTM mapping is a downstream statistician concern with no bearing on CRF design — a CRF built without SDTM in mind creates recurring mapping debt.

### Database lock (soft / hard)
Soft lock freezes data entry but allows corrections via a formal unlock/query process; hard lock blocks any change without a fully documented unlock justification.
**In use:** "We're at soft lock for the interim analysis — final hard lock waits until the SAP's locked-variable list is reconfirmed."
**Common misuse:** Using "lock" as a single binary state — soft and hard lock carry materially different correction procedures and risk profiles.

### Source data verification (SDV)
The process of confirming CRF-entered data against the original source document (chart, lab report, patient diary).
**In use:** "That query resolution needs SDV — the site re-entered the same value without checking the source."
**Common misuse:** Treating a site's "confirmed correct" response as equivalent to SDV having actually occurred.

### Data Management Plan (DMP)
The study's governing document specifying CRF completion instructions, edit-check specs, external reconciliation rules, and the lock/unlock procedure.
**In use:** "That orphaned-lab-result gap is a DMP defect — log it for the amendment, not just a one-off fix."
**Common misuse:** Treating the DMP as a static onboarding document rather than a living spec that gets amended when gaps like missing edit checks are found.

### Reconciliation
The cross-check of CRF data against an external data source (lab, ePRO, IRT, safety database) to confirm consistency, run independently of the query process.
**In use:** "Zero open queries doesn't mean clean — reconciliation hasn't run against the lab feed yet."
**Common misuse:** Conflating an empty query queue with completed reconciliation — they check different things.

### IRT
Interactive Response Technology — the system managing randomization and drug/kit dispensing logistics.
**In use:** "IRT shows a dose adjustment that the drug accountability log doesn't reflect — that's a reconciliation query against both systems."
**Common misuse:** Assuming IRT records are automatically authoritative over site-entered data rather than an independent source requiring its own reconciliation.

### 21 CFR Part 11
The FDA regulation governing electronic records and signatures, requiring a full audit trail for any data change.
**In use:** "That correction needs a reason code and timestamp in the audit trail — Part 11 doesn't allow silent overwrites."
**Common misuse:** Treating Part 11 compliance as an IT/validation concern only, rather than something that shapes how every correction is made day to day.

### Clean data / clean-data sign-off
A formal declaration, following full reconciliation, that a defined dataset (or the full database) is ready for lock.
**In use:** "Clean-data sign-off names the residual open items and their disposition — it's not a claim of zero issues."
**Common misuse:** Treating "clean" as "zero discrepancies ever existed" rather than "all known discrepancies have a documented resolution or disposition."

### Alpha-spending / GCDMP
Good Clinical Data Management Practices — the SCDM's industry-standard guidance document for data management processes across the trial lifecycle.
**In use:** "Our query-aging thresholds are set per GCDMP guidance, not an internal guess."
**Common misuse:** Treating GCDMP as regulatory law (it's an industry practice standard, not an FDA regulation) — Part 11 is the actual regulatory requirement.

### Protocol deviation (data-management-visible)
An instance where actual conduct diverged from the protocol, surfaced through data patterns (e.g., visit window violations, missing required assessments).
**In use:** "That out-of-window visit isn't a query — it's a protocol deviation, route it to the clinical team, not just the CRF correction workflow."
**Common misuse:** Data managers "fixing" a deviation-driven data anomaly through a query alone, without flagging the deviation itself to the clinical/regulatory team.
