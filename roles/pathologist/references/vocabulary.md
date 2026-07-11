# Vocabulary — terms a generalist misuses

### Synoptic report
A structured, checklist-format report with discrete required and conditional fields (defined by CAP Cancer Protocol templates) for reportable malignancies, distinct from free-text narrative description.
**In use:** "The tumor board needs the synoptic fields filled, not just the diagnosis line — the registry pulls from those fields directly."
**Common misuse:** Treating the synoptic checklist as a bureaucratic formality layered on top of "the real diagnosis," rather than the primary structured data that tumor registries and treatment-eligibility algorithms actually consume.

### Margin (positive / negative / close)
The distance between tumor and the inked resection edge; "positive" means tumor touches the ink, "negative" means it does not, "close" is a qualitative flag pending a measured distance.
**In use:** "Deep margin is negative at 1 mm — no tumor on ink, so per SSO-ASTRO no re-excision is indicated for the invasive component."
**Common misuse:** Assuming any margin under 2 mm automatically requires re-excision regardless of tumor type — the 2 mm threshold is the DCIS standard (SSO-ASTRO-ASCO 2016); invasive carcinoma uses the "no ink on tumor" standard (SSO-ASTRO 2014), a materially different rule.

### Discordance (frozen-permanent)
A disagreement between the intraoperative frozen-section diagnosis and the final permanent-section diagnosis on the same tissue.
**In use:** "That was a minor discordance — atypical on frozen, low-grade malignant on permanent — not a benign-to-malignant reversal."
**Common misuse:** Treating every wording change between frozen and permanent as equivalent; QA tracking distinguishes minor discordance (same management implication) from major discordance (would have changed the surgery performed).

### Grade vs. stage
Grade describes how abnormal the tumor cells look under the microscope (a biological property); stage describes how far the disease has spread anatomically (a distribution property).
**In use:** "It's a Grade 3 tumor but only Stage I — high-grade biology caught early."
**Common misuse:** Using "grade" and "stage" interchangeably in conversation, which conflates two independent axes — a low-grade tumor can present at a high stage, and vice versa.

### Ancillary testing
Any test beyond routine H&E morphology (immunohistochemistry, molecular/genomic testing, special stains) used to refine or confirm a diagnosis.
**In use:** "The differential from H&E is carcinoma versus lymphoma — ancillary IHC (keratin vs. CD45) will settle it."
**Common misuse:** Ordering a broad ancillary panel as a substitute for building a morphologic differential first, rather than as a targeted test of a specific, already-narrowed hypothesis.

### Gross description
The pathologist's macroscopic examination and documentation of a specimen — dimensions, orientation, inking, sectioning — performed before any microscopic diagnosis.
**In use:** "The gross exam determines every block we can ever look at — get the inking and sectioning right before anything else."
**Common misuse:** Treating grossing as clerical prep work ahead of "the real diagnosis" under the microscope, when grossing decisions are irreversible and directly limit what can ever be diagnosed.

### Tumor heterogeneity
The presence of biologically distinct regions (grade, genomic profile) within a single tumor, meaning a small sample may not represent the whole.
**In use:** "Biopsy showed Gleason 6, but given tumor heterogeneity, the prostatectomy specimen came back Grade Group 2 — that's an expected upgrading pattern, not an error."
**Common misuse:** Treating a needle-biopsy grade or genomic result as a complete, final characterization of the entire tumor rather than a sample from potentially one region of it.

### Sign-out
The pathologist's act of finalizing and releasing the official diagnostic report, as distinct from any preliminary or verbal read given earlier in the workup.
**In use:** "That was a preliminary intraoperative read — sign-out won't happen until the permanent sections and stains are back."
**Common misuse:** Treating a verbal or preliminary intraoperative impression as carrying the same certainty and finality as the signed report.

### Amended report
A report formally revised after initial sign-out, tracked by CAP QA programs in two distinct categories: clerical (demographic/labeling error) and diagnostic (changed interpretation).
**In use:** "That amendment was clerical — wrong date of birth — not a diagnostic change, so it doesn't count against the diagnostic-accuracy metric."
**Common misuse:** Reporting all amendments as a single undifferentiated count, which conflates a typo fix with a changed cancer diagnosis and makes the QA metric meaningless.

### Immunohistochemistry (IHC) control
Tissue known to be positive and negative for a given marker, run on the same slide or batch, used to validate that a stain result is technically reliable before it is interpreted biologically.
**In use:** "Before reading that TTF-1 as negative, check the control ran clean on this batch."
**Common misuse:** Interpreting a stain result at face value without first confirming the positive and negative controls on the same run behaved as expected.

### Fixation time
The duration a specimen spends in formalin before processing, which directly affects tissue morphology and the reliability of downstream IHC/molecular testing.
**In use:** "ER/PR testing needs 6-72 hours of fixation per CAP/ASCO guideline — under- or over-fixed tissue gives an unreliable result regardless of the stain protocol."
**Common misuse:** Assuming any formalin exposure counts as "fixed," without regard to whether the duration falls inside the validated window for the specific ancillary test being ordered.

### Second opinion / consult
A formal request for another pathologist — often a subspecialist — to review a case, standard practice for rare, borderline, or high-stakes diagnoses.
**In use:** "This is an unusual soft-tissue tumor — sending it to a sarcoma subspecialist before finalizing, not because the read is in doubt but because it's routine for this entity."
**Common misuse:** Treating a consult request as an admission that the requesting pathologist couldn't do the job, rather than as a routine quality practice for a defined category of difficult or high-stakes cases.

### Reflex testing
A predefined rule in the laboratory information system (LIS) that automatically triggers an additional test when a diagnosis meets specified criteria (e.g., automatic mismatch-repair/MSI testing on a new colorectal cancer diagnosis).
**In use:** "MMR IHC should have reflexed automatically on that colon cancer — check whether the LIS rule actually fired."
**Common misuse:** Assuming a reflex test happens automatically as a matter of general practice, without verifying the specific triggering rule is actually configured and active in that lab's system.
