# Vocabulary

Terms generalists reliably misuse in HIM/coding/ROI work. Format per term: definition, practitioner usage, common misuse.

### Minimum necessary standard

- **Definition:** the HIPAA requirement (45 CFR §164.502(b)) that a disclosure include only the information reasonably necessary to accomplish the stated purpose — it does not apply to a patient's request for their own record.
- **In use:** "The insurer asked for the whole chart to review one denied claim — minimum necessary means we send the encounter in question, not five years of history."
- **Common misuse:** treating minimum necessary as a courtesy or a fee-avoidance tactic rather than a legal ceiling on every non-patient disclosure; also wrongly applying it to the patient's own access request, where it doesn't apply at all.

### Present on admission (POA) indicator

- **Definition:** a code-level flag (Y/N/U/W) stating whether a diagnosis was present at the time of inpatient admission, used to separate pre-existing conditions from hospital-acquired ones for both clinical accuracy and reimbursement (hospital-acquired conditions can reduce payment).
- **In use:** "POA is U on the pressure ulcer — documentation doesn't say whether it was present at admission, and that's a query, not a guess."
- **Common misuse:** defaulting every ambiguous case to "N" to avoid a query, which understates hospital-acquired-condition risk in the wrong direction and is itself a coding error.

### Case Mix Index (CMI)

- **Definition:** the average MS-DRG relative weight across a facility's discharges over a period — a proxy for average patient acuity and a direct driver of average reimbursement per case.
- **In use:** "CMI is up 0.15 this quarter — before we call that a win, pull the query audit on the accounts that drove it."
- **Common misuse:** reporting CMI as a pure quality or productivity metric without checking whether the increase is real acuity/documentation improvement or a coding/query practice drifting toward upcoding — the number is silent on which.

### DNFB (Discharged Not Final Billed)

- **Definition:** accounts where the patient has been discharged but the bill hasn't dropped — held up by a documentation gap, unresolved query, coding backlog, or edit failure.
- **In use:** "DNFB is at 6.2 days facility-wide — that's real cash sitting on the table, and it's mostly query holds, not coder capacity."
- **Common misuse:** treating DNFB purely as a coding-department productivity metric, when the underlying holds are frequently upstream (physician documentation, signature turnaround) and not something faster coding fixes.

### Compliant query vs. leading query

- **Definition:** a compliant query presents clinical indicators and offers a closed or open option set (including "clinically indeterminate") without naming the suspected diagnosis first; a leading query suggests the answer.
- **In use:** "'Does the patient have sepsis?' is leading — rewrite it to cite the labs and vitals and offer confirmed/ruled-out/indeterminate as options."
- **Common misuse:** believing a query is compliant as long as it's polite or open-ended in tone — leading-ness is about whether the diagnosis is named before the evidence, not about wording softness.

### Upcoding vs. undercoding

- **Definition:** upcoding assigns a higher-specificity or higher-reimbursement code than the documentation supports; undercoding assigns a lower one than the documentation actually supports, understating both reimbursement and clinical acuity.
- **In use:** "This isn't conservative coding, it's undercoding — the documentation clearly supports the MCC and we're leaving it off the claim."
- **Common misuse:** treating undercoding as a "safe" default after an upcoding audit finding; it's a distinct compliance and revenue-accuracy problem, not a corrective overcorrection.

### Unbundling (vs. NCCI edit)

- **Definition:** billing components of a procedure separately when a National Correct Coding Initiative (NCCI) edit says they should be bundled into a single code, absent a documented, medically justified reason to override the edit.
- **In use:** "The -59 modifier overrides the NCCI bundling edit here, but only if the operative note documents a genuinely separate procedure — otherwise this is unbundling."
- **Common misuse:** applying a modifier as a default unlock for the edit rather than checking whether the documentation actually supports a distinct, separately billable service.

### Accounting of disclosures

- **Definition:** the HIPAA-required log of certain non-routine disclosures (not for treatment, payment, or healthcare operations) that a patient can request to see — who received their information, what was disclosed, and why.
- **Practitioner usage:** "That subpoena release goes in the accounting log; the referral to the cardiologist doesn't — that's routine treatment disclosure."
- **Common misuse:** logging every disclosure indiscriminately (burying the genuinely reportable ones) or, the opposite failure, skipping the log for a mandatory disclosure because it "felt routine."

### 42 CFR Part 2

- **Definition:** federal confidentiality regulations for substance use disorder (SUD) treatment records, more restrictive than HIPAA and requiring their own specific consent, independent of a general HIPAA authorization.
- **In use:** "The HIPAA authorization on file doesn't cover the SUD treatment notes — Part 2 needs its own consent naming the specific recipient and purpose."
- **Common misuse:** assuming a signed HIPAA authorization automatically covers SUD records; it doesn't, and releasing them on that basis is a Part 2 violation even when HIPAA compliance is otherwise clean.

### Legal health record vs. designated record set

- **Definition:** the legal health record is the specific, facility-defined set of documents that constitute the official business record for legal and disclosure purposes; the designated record set is the broader HIPAA-defined scope a patient has a right to access, which can include billing records and other items outside the legal health record.
- **In use:** "The patient has a right to the billing records under the designated record set even though billing isn't part of our legal health record definition."
- **Common misuse:** using the two terms interchangeably, which produces wrong answers on both what a court subpoena reaches and what a patient access request must include.

### MS-DRG vs. APR-DRG

- **Definition:** MS-DRG (Medicare Severity DRG) is CMS's Medicare-specific grouping system, driving Medicare inpatient reimbursement; APR-DRG (All Patient Refined DRG) is a broader severity-adjusted system many state Medicaid programs and quality-reporting systems use, with finer severity-of-illness and risk-of-mortality subclasses.
- **In use:** "This account's Medicare payment runs off the MS-DRG weight, but the state's quality report pulls APR-DRG severity subclass — they can move in different directions on the same chart."
- **Common misuse:** assuming one DRG system's CC/MCC capture rules transfer directly to the other; the severity-level logic and payer application differ.

### Spoliation

- **Definition:** the destruction or alteration of a record that is or should reasonably be known to be relevant to anticipated or pending litigation — a legal, not clinical, concept.
- **In use:** "This chart is on a litigation hold — it doesn't go into this month's destruction batch even though it's past the retention schedule."
- **Common misuse:** assuming the retention schedule alone governs destruction timing; an open litigation hold overrides the schedule regardless of how long past the retention period the record is.

### Master Patient Index (MPI): duplicate vs. overlay

- **Definition:** a duplicate is two separate medical record numbers for the same patient (fragmenting their history); an overlay is one medical record number that has been incorrectly populated with a mix of two different patients' data (actively dangerous — one patient's allergy or medication data appears under another patient's chart).
- **In use:** "That's not just a duplicate, it's an overlay — patient B's medication list is showing up under patient A's MRN, and that has to be corrected as a patient-safety event, not a routine MPI cleanup."
- **Common misuse:** treating overlays as a bigger version of the duplicate problem; they're categorically worse (active patient-safety risk) and require an urgent clinical-safety escalation, not the standard dedup queue.

### Redetermination vs. reconsideration (Medicare appeal levels)

- **Definition:** redetermination is the first-level Medicare appeal, decided by the same Medicare Administrative Contractor (MAC) that processed the original claim; reconsideration is the second level, decided by an independent Qualified Independent Contractor (QIC) that wasn't involved in the original decision.
- **In use:** "Redetermination came back unfavorable — file reconsideration with the QIC within 180 days, and this time lead with the NCCI citation, not just the clinical narrative."
- **Common misuse:** treating redetermination and reconsideration as the same review with two chances, rather than recognizing reconsideration is genuinely independent and worth strengthening the argument for, not just resubmitting.
