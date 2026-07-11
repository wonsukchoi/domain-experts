# Physiatry playbook

Filled protocols and worked tables — populate with the patient in front of you, don't redesign the structure each time.

## IRF admission screen

1. **Diagnosis check against the CMS 13 qualifying conditions** (42 CFR §412.29): stroke; spinal cord injury; congenital deformity; amputation; major multiple trauma; hip fracture; brain injury; neurologic disorders (MS, Parkinson's, muscular dystrophy, motor neuron disease, polyneuropathy); burns; active polyarticular rheumatoid/psoriatic arthritis unresponsive to outpatient management; systemic vasculitides with joint involvement; and hip/knee replacement meeting bilateral, BMI≥50, or age≥85 criteria. "Debility" or "deconditioning" alone does **not** qualify — a qualifying diagnosis must also be present in the chart.
2. **Participation-tolerance check**: can the patient tolerate 3 hours/day or 15 hours/week of therapy across at least 2 disciplines? If not yet, a subacute/SNF stop first is the safer plan than an IRF admission likely to fail utilization review.
3. **24-hour physician availability and nursing need check**: does the patient need daily physician oversight and 24-hour rehab nursing (medically complex, not just functionally impaired)? If the acuity doesn't require it, a lower level of care may be more appropriate regardless of diagnosis.
4. **Document the admission FIM and the specific functional deficits driving the admission** — this is the baseline every later projection and payer conversation is built from.

## FIM / length-of-stay projection table

| Step | Calculation | Worked value |
|---|---|---|
| Admission FIM | motor (13 items × 1–7) + cognitive (5 items × 1–7) | 40 + 25 = 65/126 |
| Target discharge FIM | unit's UDSMR benchmark for impairment group + admission FIM band | 100/126 |
| Gain needed | target − admission | 100 − 65 = 35 |
| Benchmark efficiency | UDSMR published points/day for impairment group | 1.8 pts/day |
| Projected LOS | gain needed ÷ efficiency, rounded up | 35 ÷ 1.8 = 19.4 → 20 days |
| Day-4 checkpoint | actual points gained ÷ days elapsed | 6 ÷ 4 = 1.5 pts/day |
| Re-projected LOS from day 4 | (target − FIM at day 4) ÷ observed efficiency | (100 − 71) ÷ 1.5 = 19.3 → day 4 + 20 ≈ day 23 |

**Re-projection rule**: recompute from the observed rate once at least 3–4 days of data exist. If the observed rate is below benchmark, screen for a reversible cause (pain, depression, sedating medication, undiagnosed infection) before accepting a lower discharge target.

## Spasticity chemodenervation planning table

| Input | Value | Note |
|---|---|---|
| Patient weight | 62 kg | |
| Per-kg cap | 6 units/kg | 6 × 62 = 372 units |
| Absolute cap | 400 units | whichever cap is lower binds — here, 372 |
| Medial gastrocnemius | 75 units | primary equinus contributor |
| Lateral gastrocnemius | 50 units | |
| Soleus | 75 units | |
| Subtotal | 200 units | 75+50+75 = 200, well under 372 |
| Reserve for tibialis posterior (if varus persists) | 40 units | 200 + 40 = 240, still under 372 |

**Muscle-selection default**: inject the muscles driving the specific functional block (e.g., equinovarus at heel-strike), not every spastic muscle in the limb — a muscle with useful residual tone for standing or transfers is a candidate to leave alone even if its Ashworth score is elevated.

## Autonomic dysreflexia workup sequence (SCI at or above T6)

1. **Sit the patient up and loosen restrictive clothing/devices** first — this alone can drop BP meaningfully while the workup proceeds.
2. **Check the bladder first**: is the catheter kinked, clamped, or the leg bag full? Straight-cath or flush an indwelling catheter if unclear.
3. **Check the bowel second**: digital rectal exam for impaction, using topical anesthetic before the exam to avoid worsening the reflex.
4. **Check the skin third**: pressure injury, ingrown toenail, tight clothing, or a burn under the level of injury.
5. **If BP remains ≥20–30 mmHg above the patient's known baseline systolic after steps 1–4**, treat pharmacologically (short-acting antihypertensive, e.g., nitroglycerin paste or nifedipine per institutional protocol) while continuing the search — do not wait for the stimulus to be found before treating the elevated pressure.
6. **Document the stimulus found and resolved** — recurrent unexplained episodes need urology/GI referral for an occult cause (stone, fissure).

## Rancho Los Amigos-staged TBI management table

| Rancho level | Behavioral presentation | Management default |
|---|---|---|
| I–II (no response / generalized response) | No purposeful response, or generalized response to stimuli | Sensory stimulation program, family education, prevent complications (contracture, pressure injury) |
| III–IV (localized / confused-agitated) | Localizes to stimuli or is agitated, non-purposeful, easily overstimulated | Low-stimulation environment, safety/restraint minimization, redirect rather than orient-drill |
| V–VI (confused-inappropriate / confused-appropriate) | Follows simple commands inconsistently to consistently, needs cueing | Structured, simplified tasks with consistent routine; begin goal-directed therapy |
| VII–VIII (automatic-appropriate / purposeful-appropriate) | Appropriate in familiar settings, generalizes with cueing to independent | Community re-entry planning, cognitive-communication therapy, driving/return-to-work evaluation |

**Rule**: reassess the Rancho level at each team conference — it does not move monotonically forward, and a plan built for day-30 expectations on a patient still at level III wastes both the patient's tolerance and the team's time.

## K-level prosthetic prescription table

| K-level | Definition | Prescription implication |
|---|---|---|
| K0 | No ability or potential to ambulate/transfer safely, prosthesis doesn't enhance quality of life or mobility | Prosthesis not typically justified |
| K1 | Household ambulator, fixed cadence | Basic prosthesis, single-axis or SACH foot |
| K2 | Limited community ambulator, can traverse low-level environmental barriers | Multi-axial foot/ankle for uneven terrain |
| K3 | Unlimited community ambulator, variable cadence | Energy-storing foot, may include microprocessor components |
| K4 | Exceeds basic ambulation, high impact/stress/energy | Prosthesis optimized for athletic or high-demand activity |

**Assignment rule**: assign from demonstrated trial performance (temporary prosthesis or PT functional assessment), not from the patient's stated pre-amputation activity level — a prescription written above demonstrated function is a documented denial risk with Medicare and most payers that mirror its criteria.
