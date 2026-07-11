# Radiation Therapist — Playbook

## PTV margin calculation (van Herk recipe)

Margin ≈ 2.5Σ + 0.7σ, where Σ is the population systematic (planning/setup-process) uncertainty and σ is the population random (day-to-day) uncertainty, both standard deviations in mm, measured from the department's own setup-verification data for a given technique.

Example — conventional pelvic IGRT, department-measured Σ = 3.0mm, σ = 2.0mm:

| Term | Value | Contribution |
|---|---|---|
| 2.5 × Σ | 2.5 × 3.0mm | 7.5mm |
| 0.7 × σ | 0.7 × 2.0mm | 1.4mm |
| **PTV margin** | | **8.9mm ≈ 9mm** |

A tighter-immobilization, daily-CBCT SRS/SBRT technique with Σ = 1.0mm, σ = 0.8mm gives 2.5(1.0) + 0.7(0.8) = 2.5 + 0.56 = 3.06mm ≈ 3mm — the reason SRS margins run a few millimeters while conventional pelvic margins commonly run closer to a centimeter: the margin is a direct function of how tightly that technique's own setup process actually reproduces, not a fixed rule of thumb.

## Setup-tolerance decision table (by technique)

| Technique | Imaging frequency | Single-fraction action level (translational) | 3-fraction trend flag | Rotational tolerance |
|---|---|---|---|---|
| Conventional (breast, pelvis, thorax, weekly portal) | Weekly portal | 5mm | Not typically tracked at this frequency | N/A |
| Conventional IGRT (daily CBCT, e.g., prostate) | Daily CBCT | 5mm | Flag if 3 consecutive fractions shift the same direction by ≥3mm cumulative and the third shift is ≥ the first | 3° |
| Cranial SRS (single/few fraction) | Daily CBCT/6D couch | 1–2mm | Any 2-fraction directional repeat is reviewed | 0.5–1° |
| Extracranial SBRT (lung, liver, spine) | Daily CBCT + gating/breath-hold verification | 2–3mm | Any 2-fraction directional repeat is reviewed | 1° |

Rule of thumb: within tolerance and no trend → correct and treat; within tolerance but trending → treat today if a fixed protocol rule was met (e.g., still ≤ action level) and escalate for next-day review; beyond tolerance → hold, re-image after correction, physicist/physician sign-off before treating.

## Chart-check reconciliation template (filled)

"Chart check at fraction [N] of [total]. Prescription: [total dose] Gy in [total fractions] fractions ([dose/fraction] Gy/fraction). Delivered to date: [N] × [dose/fraction] = [delivered dose] Gy. Remaining: [total − N] fractions × [dose/fraction] = [remaining dose] Gy. [Delivered] + [remaining] = [total dose] Gy — reconciles with prescription. Elapsed calendar days: [X] of [planned overall treatment time] Y days. Missed fractions: [count and dates], reason: [illness/machine downtime/holiday]. Makeup plan: [additional fraction(s) added / compressed schedule / physician-accepted gap] — approved by [physician name], dated [date]. Current on-treatment visit finding: [CTCAE grade] [toxicity type] at [site]."

Worked instance: prostate patient at fraction 26 of 39 (78.0 Gy / 2.00 Gy per fraction). Delivered: 26 × 2.00 = 52.0 Gy. Remaining: 13 × 2.00 = 26.0 Gy. 52.0 + 26.0 = 78.0 Gy — reconciles. Elapsed 34 calendar days of a planned 55-day overall treatment time (39 fractions, Monday–Friday, accounting for 2 holiday closures). One missed fraction (day 19, patient illness) with same-week makeup delivered day 24 — no net extension of overall treatment time. Current OTV finding: CTCAE grade 1 genitourinary urgency, no intervention beyond standard counseling.

## CTCAE skin/mucosal reaction quick reference (radiation dermatitis, abbreviated from CTCAE v5.0)

| Grade | Finding | Typical action |
|---|---|---|
| 1 | Faint erythema or dry desquamation | Continue treatment; standard skin-care instructions |
| 2 | Moderate-to-brisk erythema; patchy moist desquamation mostly confined to skin folds; moderate edema | Continue treatment; reinforce skin care, consider dressing for moist areas; physician aware at next OTV |
| 3 | Moist desquamation in areas other than skin folds; bleeding induced by minor trauma/friction | Same-day physician notification; possible treatment field/technique adjustment or bolus reassessment; wound-care order |
| 4 | Life-threatening; skin necrosis or ulceration of full-thickness dermis; spontaneous bleeding | Immediate physician notification; hold treatment pending evaluation |

A grade ≥3 finding, or any grade appearing earlier than the department's typical cumulative-dose milestone for that site and fractionation, is escalated the same day rather than at the next scheduled on-treatment visit.
