# Playbook

Filled protocols with real thresholds. Defaults, not laws — deviate consciously and document why.

## 1. Cath lab contrast ceiling (Cigarroa formula) and staging decision

**Formula:** Max contrast (mL) = 5 × body weight (kg) / serum creatinine (mg/dL), capped at 300 mL regardless of the calculated number.

| Weight (kg) | Creatinine (mg/dL) | Calculated max | Lab alert (75%) |
|---|---|---|---|
| 70 | 1.0 | 350 → capped 300 | 225 |
| 80 | 1.4 | 286 | 214 |
| 90 | 2.0 | 225 | 169 |
| 60 | 2.5 | 120 | 90 |

**Live tracking sequence during a case:**
1. Calculate the ceiling and alert line before the case starts; write both on the procedure log header.
2. After every injection, add the injector-logged volume to a running total on the log — not from memory at the end.
3. At the alert line (75% of ceiling), verbally flag the operator with the current total, the ceiling, and remaining margin.
4. Before adding a second vessel or a repeat run, project the additional volume needed and re-check against remaining margin, not just the current total.
5. If the projected total after the next step would leave under ~10% of the ceiling as margin, default to staging the remainder to a second session (typical spacing: 48-72 hours, with IV hydration and a repeat basic metabolic panel first) unless the case is unstable (STEMI, ongoing ischemia) and the physician elects to proceed.

## 2. Anticoagulation (ACT) protocol during PCI

| Regimen | Bolus | Target ACT | Recheck interval |
|---|---|---|---|
| Unfractionated heparin, no GPIIb/IIIa | 70-100 U/kg | >250-300 s | Every 30 min, and before any balloon/stent step |
| Unfractionated heparin + GPIIb/IIIa inhibitor | 50-70 U/kg | 200-250 s | Every 30 min |
| Bivalirudin | 0.75 mg/kg bolus, 1.75 mg/kg/hr infusion | 300-350 s | Per infusion protocol; less frequent recheck if infusion running |

**Sequence:** draw baseline ACT before any heparin → bolus per regimen → recheck at 5 min post-bolus to confirm target hit → redose in 1,000-2,000 U increments if under target → recheck every 30 min for the duration of the case → hold any balloon/stent deployment until a fresh in-range value is confirmed.

## 3. LV chamber quantification — normal ranges (ASE/EACVI 2015)

| Measure | Normal (male) | Normal (female) | Mildly abnormal |
|---|---|---|---|
| LVEF, biplane Simpson's | 52-72% | 54-74% | 41-51% (M) / 41-53% (F) |
| LV end-diastolic diameter | 4.2-5.9 cm | 3.8-5.2 cm | 5.9-6.3 cm (M) |
| Interventricular septal thickness | 0.6-1.0 cm | 0.6-0.9 cm | 1.1-1.3 cm |

**Measurement fallback order (most to least preferred):** (1) biplane Simpson's method of discs on adequately traced endocardial borders → (2) contrast-enhanced border definition (Definity/Lumason) when ≥2 contiguous segments are untraceable → (3) 3D volumetric acquisition when available and geometry is distorted (regional wall-motion abnormality, aneurysm) → (4) visual/gestalt estimate, reported explicitly as a visual estimate with the reason a trace wasn't obtainable, never presented as equivalent to a traced number.

## 4. Diastolic function grading algorithm (Nagueh/ASE 2016, simplified)

Four variables, evaluated together — no single value grades diastolic function alone:

| Variable | Threshold |
|---|---|
| Septal e' | <7 cm/s abnormal |
| Lateral e' | <10 cm/s abnormal |
| Average E/e' | >14 abnormal (suggests elevated LV filling pressure) |
| LA volume index | >34 mL/m² abnormal |
| Peak TR velocity | >2.8 m/s abnormal |

**Grading:** 0-1 of 4 abnormal → normal diastolic function. 2 of 4 abnormal → indeterminate (correlate clinically or add stress/Valsalva maneuvers). 3-4 of 4 abnormal → diastolic dysfunction present; grade I-III severity requires the additional mitral inflow E/A ratio and deceleration-time table in the full ASE algorithm.

**Caveat before applying e' cutoffs:** in LVH, LBBB, or a paced rhythm, septal e' is unreliable in isolation — use lateral or averaged e' and weight the LA volume index and TR velocity more heavily.

## 5. Carotid stenosis grading (SRU consensus, 2003)

| ICA PSV (cm/s) | ICA/CCA PSV ratio | ICA EDV (cm/s) | Stenosis category |
|---|---|---|---|
| <125 | <2.0 | <40 | Normal / <50% |
| 125-230 | 2.0-4.0 | 40-100 | 50-69% |
| >230 | >4.0 | >100 | ≥70%, less than near-occlusion |
| Variable, may be low | — | — | Near-occlusion (visual + waveform pattern) |
| No flow detected | — | — | Total occlusion |

**Discordance rule:** if grayscale plaque burden and PSV disagree, re-verify Doppler angle (must be ≤60°, ideally 60° exactly) and sample-volume placement before trusting either number; a contralateral high-grade or occluded ICA can compensatory-elevate PSV on the side being read, inflating the apparent grade.

## 6. ABI interpretation and reflex testing

| ABI | Interpretation | Reflex |
|---|---|---|
| 1.00-1.40 | Normal | None |
| 0.91-0.99 | Borderline | Repeat post-exercise |
| 0.41-0.90 | Mild-moderate PAD | Segmental pressures/waveforms |
| ≤0.40 | Severe PAD | Segmental pressures + consider vascular surgery referral |
| >1.40 | Noncompressible (calcified vessels) | Toe-brachial index (toe vessels calcify later) |

## 7. Access-site closure device selection sequence

1. Confirm puncture site with a femoral angiogram before selecting a closure device — never select by palpation or sheath size alone.
2. If common femoral artery puncture, no significant calcification at the site, and vessel diameter ≥5 mm: collagen plug or suture-mediated closure device is appropriate.
3. If puncture is at or above the inguinal ligament, into the SFA/profunda bifurcation, or through heavy calcification: default to manual/mechanical compression or a surgical approach, not a closure device — device failure and retroperitoneal bleed risk rise sharply outside validated anatomy.
4. Document the confirming angiogram image reference alongside the device used, so the choice is auditable after the fact.
