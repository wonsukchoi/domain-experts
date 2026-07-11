# Playbook

Filled operational templates a technologist actually runs — adapt the numbers to the department's own protocols and license conditions, but the structure and thresholds are real starting points.

## 1. Radiopharmaceutical dose verification & administration checklist

Run before every dose, diagnostic or therapeutic — no exceptions for "routine" studies.

| Step | Check | Fail action |
|---|---|---|
| 1 | Two patient identifiers match order (name + DOB or MRN) | Stop; resolve before proceeding |
| 2 | Clinical indication on file supports the ordered study/isotope | Query ordering physician |
| 3 | Pregnancy status documented (if applicable) and lactation screen for I-131/I-123 | Stop; escalate to physician |
| 4 | Interference screen: recent barium (bone/GI studies), iodinated contrast (thyroid uptake/therapy), other radiopharmaceuticals within relevant half-lives | Reschedule or document accepted limitation |
| 5 | Medication holds per protocol (thyroid hormone before uptake, metformin per department contrast/renal protocol) | Confirm hold was followed or reschedule |
| 6 | Dose calibrator assay of the actual syringe/vial, at time of administration | If reading differs >10% from expected decay-corrected activity, re-measure with a second reference source before dosing |
| 7 | Record measured activity, time, and calibrator ID — not the ordered activity | N/A — this is the value of record |
| 8 | Injection-site monitoring active where quantification depends on a clean bolus (myocardial perfusion, renal, lymphoscintigraphy) | Confirm probe/detector is running before injection, not after |

## 2. I-131 therapy patient release assessment (reusable form)

Use whenever administered activity or measured exposure rate fails the Regulatory Guide 8.39 default table (33 mCi administered, or 7 mrem/hr at 1 m).

```
PATIENT: _______________          Rx ACTIVITY: _____ mCi (_____ GBq)
INDICATION: [ ] Remnant ablation  [ ] Graves' disease  [ ] Recurrent/metastatic disease

STEP 1 — DEFAULT TABLE CHECK
  Administered activity ≤ 33 mCi?              [ ] Yes → RELEASE, standard instructions
                                                 [ ] No → continue
  Measured exposure rate at 1 m ≤ 7 mrem/hr?    [ ] Yes → RELEASE, standard instructions
                                                 [ ] No → continue to Step 2

STEP 2 — CASE-BY-CASE CALCULATION
  Measured dose rate at 1 m (mrem/hr):           _____
  Effective half-life (hr) — pick the right population:
     Post-thyroidectomy ablation (little/no remnant): ~17 hr
     Graves' disease, intact gland:                    ~120–170 hr (5–7 days)
     Remnant + residual functioning tissue:             intermediate — use RSO/physicist estimate
  Occupancy factor for closest household contact:
     Spouse/partner, standard precautions given:  0.25
     Household member, precautions not yet given: 0.5
     Casual contact only:                          0.125
  Projected TEDE = dose rate × occupancy × (T_eff / ln 2)
     = _____ × _____ × (_____ / 0.693) = _____ mrem

  Result ≤ 500 mrem (5 mSv)?  [ ] Yes → RELEASE with written precautions (Step 3)
                               [ ] No → inpatient isolation until repeat calculation passes

STEP 3 — WRITTEN PRECAUTIONS (attach signed copy to chart per 10 CFR 35.75(c))
  [ ] Separate bedroom, minimum 3 nights
  [ ] Maintain >3 ft distance except brief necessary contact
  [ ] No close/prolonged contact with children or pregnant individuals, 5 days
  [ ] Separate bathroom, or double-flush after use
  [ ] Private vehicle for travel home
  [ ] Follow-up contact number provided

  Household includes pregnant member or child under 2? [ ] Yes → apply whichever of
  Step 1/Step 2 is MORE restrictive, regardless of which one technically passed.

TECHNOLOGIST: _______________  RSO CO-SIGNATURE: _______________  DATE: _____
```

## 3. Instrument QC schedule with tolerances

| Instrument | Test | Frequency | Tolerance | Fail action |
|---|---|---|---|---|
| Dose calibrator | Constancy (reference source) | Daily | ±10% of expected decay-corrected value | Re-check with second source; if confirmed, remove from service, call service tech |
| Dose calibrator | Accuracy (NIST-traceable sources) | Install, annual, post-repair/move | ±10% of certified value | Remove from service until corrected |
| Dose calibrator | Linearity (time-decay method) | Install, quarterly, post-repair/move | ±10% across clinical activity range | Restrict to activities within passing range or remove from service |
| Dose calibrator | Geometry | Install, post-repair/move | Documented correction factors per volume/geometry | Apply correction factors; do not use uncorrected |
| Gamma camera | Flood-field uniformity (intrinsic or extrinsic) | Daily | Per manufacturer spec, typically ≤5% integral uniformity | Pull camera from clinical schedule immediately |
| Gamma camera | Center of rotation (SPECT) | Weekly | Per manufacturer spec | Repeat; if still failing, service call before SPECT acquisitions |
| Well counter | Chi-square (constancy) | Daily/weekly per protocol | Statistical control per department SOP | Re-run; investigate if repeated failure |

## 4. Extravasation / infiltration detection and mitigation

**Immediate (0–5 minutes post-injection):**
1. Confirm bilateral injection-site probe or visual pinhole check shows activity clearing from the site, not pooling.
2. If pooling/high residual counts are seen: image the injection site in the field of view at every acquisition phase — don't crop it out. This is the difference between a confounded read and a documented, explainable one.
3. Note extravasation in the technical worksheet with an estimated severity (mild/moderate/severe by visual/count comparison to a matched normal injection) — this travels with the study to the reading physician.

**Downstream handling:**
- Myocardial perfusion: extravasated activity near the injection site can be misread as a chest-wall or breast finding; flag it explicitly so it isn't miscounted as myocardium.
- Renal/dynamic flow studies: an infiltrated line corrupts the time-activity curve used for quantitative function (e.g., differential renal function) — document and consider a repeat if the clinical question depends on the number, not just the image.
- Bone scan (Tc-99m-MDP): most extravasations, even visually significant ones, do not require patient recall — adverse tissue reactions at the injection site are rare in the published surgical/dosimetry literature — but document activity and estimated dose to the site per department policy so a pattern (bad line, bad technique) gets caught before it recurs.

## 5. FDG PET/CT patient preparation protocol

| Parameter | Requirement | If failed |
|---|---|---|
| Fasting | ≥4–6 hr prior to injection, water only | Reschedule same-day if feasible, else new appointment |
| Blood glucose | Ideally 100–140 mg/dL; must be ≤200 mg/dL to inject | >200 mg/dL: attempt correction (insulin per protocol) and re-check, or reschedule |
| Blood glucose, low end | ≥70 mg/dL | <70 mg/dL: treat hypoglycemia before proceeding, patient safety first |
| Strenuous exercise | None in prior 24 hr | Note deviation; myocardial/muscle uptake may be affected |
| Diabetic medication | Oral agents (including metformin) taken as prescribed per department protocol; type 1 diabetics hold morning short-acting insulin, continue basal | Confirm with patient before injecting; document any deviation |
| Uptake time | Standard 60 min ± 5 min from injection to scan start, consistent within a patient for serial comparison | If timing deviates >10 min from prior study, note in report — SUV is time-dependent and comparisons across mismatched uptake times are unreliable |
