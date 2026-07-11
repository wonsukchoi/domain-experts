# Pretesting Playbook

Filled sequences, thresholds, and correction factors for the technician pretest chain. Load this when actually running or reviewing a workup, not for the conceptual model (that's in SKILL.md).

## 1. Pretest sequence, in order, with the confound check for each stage

| Stage | Test | Confound to check before recording as final | Threshold / action |
|---|---|---|---|
| 1 | History / chief complaint | Paraphrase drift — is this the patient's words or the scheduler's reason? | Quote verbatim; if it contradicts the referral reason, chart both |
| 2 | Visual acuity (distance, near, with correction) | Is the patient wearing current Rx? Pinhole if reduced from baseline | If pinhole improves ≥2 lines, refractive/media cause likely; if not, escalate |
| 3 | Lensometry (existing spectacles) | Is the lensometry reading consistent with the chart's last Rx? | >0.50 D discrepancy — re-verify, don't assume patient error |
| 4 | Pupils / EOM / confrontation fields | Any afferent pupillary defect (APD)? | Any APD — flag immediately, do not proceed to dilation without physician awareness |
| 5 | Tonometry (Goldmann or NCT) | Pachymetry on file this visit or ever? | No CCT on file in a glaucoma-risk patient — obtain pachymetry before finalizing IOP as "stable" |
| 6 | Pachymetry | — | See correction table below |
| 7 | Automated visual field (if ordered) | Reliability indices | See reliability table below |
| 8 | Angle assessment (van Herick or confrontation oblique illumination) | Any narrow-angle history | Grade ≤2 (angle width <1/4 corneal thickness) — hold dilation, flag for gonioscopy |
| 9 | Dilation (mydriatic/cycloplegic instillation) | Angle safety cleared in step 8 | Only after step 8 clears |
| 10 | Biometry (A-scan/optical) if ordered | Fellow-eye symmetry | See axial length table below |
| 11 | Imaging (OCT, fundus photo) | Media clarity, patient cooperation | Note signal strength/quality score; a scan below the device's stated quality floor is not a valid baseline |

## 2. Goldmann IOP corneal-thickness correction

Reference central corneal thickness (CCT): **~540 µm**. Correction factor: **~0.5 mmHg per 10 µm** deviation from reference (Doughty & Zaman meta-analysis).

```
corrected_IOP = measured_IOP + 0.5 * (540 - measured_CCT) / 10
```

Worked entries:

| Measured IOP (mmHg) | CCT (µm) | Deviation from 540 | Correction | Corrected IOP |
|---|---|---|---|---|
| 23 | 495 | -45 | +2.25 | 25.3 |
| 22 | 498 | -42 | +2.1 | 24.1 |
| 18 | 610 | +70 | -3.5 | 14.5 |
| 16 | 540 | 0 | 0 | 16.0 |

**Default:** pull pachymetry any time IOP lands in the 21–24 mmHg band, or any time it's the patient's first visit, or any time a glaucoma-suspect or glaucoma diagnosis is on the problem list — unless CCT is already charted from a prior visit and the cornea has no reason to have changed (no refractive surgery, no new corneal pathology since).

## 3. Visual field reliability gate

| Index | Reliable threshold | Action if exceeded |
|---|---|---|
| Fixation losses (FL) | <20% | Flag "unreliable — fixation," offer retest with re-instruction on the blind-spot check |
| False positives (FP) | <33% | Flag "unreliable — trigger-happy responses," field likely shows better sensitivity than real |
| False negatives (FN) | <33% | Flag "unreliable — fatigue/inattention," field likely shows worse sensitivity than real; consider shorter test (SITA Faster) on retest |

**Default:** if any single index exceeds its threshold, chart the test as unreliable and do not let it enter progression analysis (e.g., Guided Progression Analysis software) as a data point — unless the ophthalmologist has explicitly asked to bank it as a known-unreliable baseline for a patient who cannot physically test better (e.g., significant cognitive or motor limitation).

## 4. Angle assessment before dilation (van Herick grading)

| Van Herick grade | Angle width vs. corneal thickness | Dilation safety |
|---|---|---|
| Grade 4 | ≥1x corneal thickness | Safe to dilate |
| Grade 3 | 1/4–1/2 corneal thickness | Safe to dilate |
| Grade 2 | 1/4 corneal thickness | Hold — flag for gonioscopy before dilating |
| Grade 1 or slit | <1/4 corneal thickness | Do not dilate — physician must assess angle-closure risk first |

**Default:** any patient with no gonioscopy on file and a van Herick grade of 2 or below gets held from dilation and flagged, even if the visit's purpose was a routine dilated exam — a missed narrow angle converting to acute closure is a same-day ophthalmic emergency, and it doesn't reschedule.

## 5. Biometry — fellow-eye symmetry check

| OD axial length | OS axial length | Difference | Action |
|---|---|---|---|
| 23.45 mm | 23.52 mm | 0.07 mm | Within normal variation — proceed |
| 23.10 mm | 24.80 mm | 1.70 mm | Re-measure both eyes before finalizing IOL calc; check for prior surgery/trauma/staphyloma history explaining true asymmetry |
| 22.90 mm | 23.25 mm | 0.35 mm | Above the ~0.3 mm default flag — re-measure the outlier eye once before accepting |

**Default:** re-measure any pair with >0.3 mm difference and no documented anatomic reason (prior scleral buckle, staphyloma, amblyopia-related axial difference) before it goes into an IOL power calculation — a 1.0 mm axial length error translates to roughly 2.5–3.5 D of IOL power error, which is the single largest source of postoperative refractive surprise.

## 6. Escalate-now list (do not wait for the routine rotation)

- Sudden, painless vision loss reported in history.
- New afferent pupillary defect.
- IOP >30 mmHg in either eye, corrected or uncorrected.
- Van Herick grade 1/slit with a dilation order already in the chart.
- Patient describes flashes, new floaters, or a curtain/shade over vision.
