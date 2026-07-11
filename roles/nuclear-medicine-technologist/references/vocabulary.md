# Vocabulary

Terms generalists conflate or use loosely that technologists keep sharply separate.

### Physical half-life vs. biological half-life vs. effective half-life

**Physical half-life** is the fixed, isotope-specific decay constant (I-131: 8.02 days; Tc-99m: 6.02 hours) — physics only, unaffected by the patient. **Biological half-life** is how fast the body clears the material through excretion/metabolism, independent of decay. **Effective half-life** is the combination that actually governs how fast measured activity in or around a patient drops, and it's the number release and dosimetry decisions are built on.

**In use:** "Physical half-life for I-131 is always 8 days, but this patient's effective half-life is closer to 17 hours because there's no functioning gland left to retain it."

**Common misuse:** using the physical half-life to project release timelines or exposure decay — it systematically overestimates how long a patient remains a radiation concern for anything the body actively clears.

### Administered activity vs. prescribed (ordered) activity

**Prescribed activity** is what the physician's order and the radiopharmacy label state. **Administered activity** is what the dose calibrator measures immediately before injection — the number that actually went into the patient, after any decay or dispensing variance.

**In use:** "Ordered was 10 mCi; calibrator read 8.9 mCi at time of injection — that's what's charted."

**Common misuse:** charting the ordered activity as if it were confirmed, skipping the independent calibrator assay that's the actual point of the check.

### Extravasation vs. infiltration

**Extravasation** specifically means a vesicant or radioactive material leaking into surrounding tissue from a vascular injury during or after injection. **Infiltration** is the broader term for any IV fluid or medication entering tissue instead of the vein, vesicant or not. In nuclear medicine the terms are often used interchangeably, but the severity and reporting implications differ.

**In use:** "Probe shows 15% of the dose still at the injection site four minutes in — document as extravasation, not just 'slow uptake.'"

**Common misuse:** calling any high injection-site count "infiltration" without checking whether it's clearing normally over the first few minutes versus truly pooled.

### ALARA (As Low As Reasonably Achievable)

A radiation-protection principle: minimize dose to patients, staff, and the public, constrained by what's reasonably achievable for the clinical purpose — not an instruction to minimize activity or time without regard to whether the study still answers the clinical question.

**In use:** "ALARA doesn't mean the lowest dose that produces any image — it means the lowest dose that reliably produces a diagnostic one."

**Common misuse:** treating ALARA as license to under-dose a study, producing a noisy or nondiagnostic image that then requires a repeat exam — worse for cumulative patient dose than getting it right once.

### SUV (Standardized Uptake Value)

A semi-quantitative measure of radiotracer concentration in a region of interest, normalized to injected dose and patient body size (weight, lean body mass, or body surface area, depending on convention). It is not an absolute, unit-of-radioactivity measurement — it's a ratio built on several assumptions.

**In use:** "SUV of 6.2, but check the uptake time — that's only comparable to the prior scan if both were acquired at 60 minutes post-injection."

**Common misuse:** comparing SUVs across scans with different uptake times, different normalization conventions (body weight vs. lean body mass), or different scanners without correction — the number moves for reasons that have nothing to do with disease.

### Medical event (10 CFR 35.3045) vs. routine dosing variance

A **medical event** is an NRC/Agreement State-defined regulatory threshold — broadly, administered dose differing from the prescribed dose by more than 20% with an effective dose difference exceeding 0.05 Sv (5 rem), among other listed conditions — that triggers mandatory reporting and notification. A **routine dosing variance** (calibrator reading a few percent off the ordered activity) is normal and expected, not reportable.

**In use:** "That's an 8% variance, well under the medical-event threshold — document it and move on, no RSO escalation needed."

**Common misuse:** either dismissing a genuine threshold breach as "just a variance," or over-reporting every minor calibrator discrepancy as if it were a medical event — both erode the signal the reporting system is meant to carry.

### Occupancy factor

An assumed or measured fraction of time a household or public contact spends near a released radioactive patient, used in the case-by-case dose calculation for patient release (10 CFR 35.75). It is not the same as physical proximity at any single moment — it's a time-weighted average used to project total dose.

**In use:** "Spouse gets an occupancy factor of 0.25 with standard precautions — that's what makes the case-by-case calculation pass when the raw exposure rate alone wouldn't."

**Common misuse:** applying a single generic occupancy factor to every household contact regardless of actual living situation (a child sharing a bed is not the same occupancy as a coworker at a shared office).

### Dose calibrator QC: accuracy, constancy, linearity, geometry

Four distinct tests, not interchangeable terms. **Accuracy** compares the calibrator's reading of a NIST-traceable source to its certified value. **Constancy** checks day-to-day reproducibility against the same reference source. **Linearity** checks whether the reading stays proportionally correct across the clinical activity range (via time-decay method). **Geometry** checks whether sample volume/container shape affects the reading.

**In use:** "Daily constancy passed, but we're due for the quarterly linearity check before the next high-activity therapy dose."

**Common misuse:** treating a passing daily constancy check as evidence the calibrator is accurate across the full dose range — constancy only proves reproducibility at one reference activity, not correctness at therapy-level activities.

### Free pertechnetate / radiochemical purity

**Free pertechnetate** (unbound ⁹⁹ᵐTcO₄⁻) is technetium that failed to bind to the labeling kit's pharmaceutical and behaves like a different tracer entirely — visible in the thyroid, stomach, and salivary glands. **Radiochemical purity** is the QC measurement (thin-layer chromatography strip) of what fraction of activity is properly bound.

**In use:** "Labeling efficiency came back at 91% on the strip — under our 95% threshold, don't use this preparation for a bone scan."

**Common misuse:** assuming a kit is fine because it's within its use-by date — expiration date and actual labeling efficiency for that specific preparation are different questions, and only the QC strip answers the second one.

### Attenuation correction

A computational correction (typically CT-based on hybrid SPECT/CT or PET/CT systems) that adjusts raw counts for the fact that photons from deeper structures are absorbed by overlying tissue before reaching the detector, producing artifactually reduced counts in the absence of correction.

**In use:** "The inferior wall defect on the uncorrected images resolves on the attenuation-corrected set — that's diaphragmatic attenuation, not disease."

**Common misuse:** reading uncorrected images as if attenuation effects were pathology, especially inferior-wall "defects" in myocardial perfusion that are a well-known attenuation artifact in specific body habitus patterns.
