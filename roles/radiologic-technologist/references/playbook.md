# Radiologic Technologist Playbook

Filled protocols and workflows for the exam types and situations that come up daily. Use as executable checklists, not descriptions.

## Technique-chart adjustment workflow

Start from the facility's caliper-measured technique chart, then apply corrections in this order — each step changes the input to the next:

1. **Measure part thickness with calipers at the level of the AEC chamber(s)**, not by visual estimate. A 3 cm estimation error at the low end of a chart (e.g., extremity vs abdomen) changes bracket selection entirely.
2. **Confirm AEC applicability.** AEC is valid only when the anatomy of interest overlies an active chamber and part thickness falls within the vendor's calibrated range (typically ~10-35 cm for abdomen/chest chambers). Outside that range, or for any pediatric/small-adult exam, switch to manual technique from the chart's matching thickness bracket.
3. **Apply the 15% rule when kVp must move for penetration or contrast reasons:** a 15% kVp increase ≈ doubling mAs in receptor exposure. Example: 70 kVp/8 mAs → 80 kVp/4 mAs preserves exposure while reducing patient motion blur risk (shorter exposure time at same mAs/kVp combination is not implied — mAs must also drop for exposure time to shorten).
4. **Adjust for grid use.** Below ~10-12 cm part thickness, remove the grid — scatter contribution is low enough that grid use only adds dose without a contrast benefit. Above that threshold, an 8:1-12:1 grid is standard for abdomen/spine/pelvis.
5. **Check post-exposure EI/DI against the vendor's target range before releasing the patient.** If out of range, check positioning and collimation first (chamber coverage, field size) before assuming kVp/mAs was wrong — see red-flags.md.

## Pediatric dose-reduction quick reference

Facility pediatric chart, abdomen/chest, by weight band (illustrative structure — calibrate to local equipment):

| Weight band | kVp adjustment vs adult | mAs adjustment vs adult | Grid |
|---|---|---|---|
| <15 kg | ~10-15% (1 step down) | ÷8 | Remove |
| 15-30 kg | -10% | ÷4 | Remove |
| 30-50 kg | -5% | ÷2 | Remove or low-ratio (6:1) |
| >50 kg | Adult chart | Adult chart | Standard (8:1-12:1) |

Gonadal/fetal shielding: per AAPM PP 32-A (2019), do not place by default. Exceptions where shielding remains appropriate: exam field does not include pelvis anatomy relevant to the clinical question, and shield placement will not risk obscuring the region of interest.

## Contrast reaction response ladder

Escalate in this order; do not skip a rung because the reaction "seems mild":

1. **Mild (limited hives, itching, nausea):** Stop injection if still running. Stay with patient, notify radiologist, monitor vitals every 5 min x 3. Document reaction grade and agent/lot number.
2. **Moderate (diffuse urticaria, mild bronchospasm, hypotension with symptoms):** Stop injection, call radiologist to bedside or code team per facility protocol, IV access maintained, oxygen and antihistamine/epinephrine per facility emergency protocol — administered by physician or per standing order, not technologist discretion.
3. **Severe (laryngeal edema, hypotension with loss of consciousness, cardiac arrest):** Activate emergency response (code team), begin BLS if indicated, continue per facility's contrast reaction emergency algorithm until responders arrive.

Pre-screening before any contrast study: prior contrast reaction history (strongest single predictor of recurrence — premedicate or switch to non-ionic/lower-osmolar agent per radiologist order, do not simply "monitor closely"), renal function (eGFR) for iodinated and gadolinium-based agents, and metformin use for iodinated contrast per facility renal-risk protocol.

## MRI safety screening — four-zone model

Applied at every entry point, not just the first time a patient is escorted back:

- **Zone I** — public access, no screening required (waiting area).
- **Zone II** — interface between public and controlled areas; screening questionnaire completed here (implants, prior surgery, metal fragments, pregnancy status, occupation history for metalworkers/machinists).
- **Zone III** — restricted access; only screened personnel and patients past Zone II clearance. No ferromagnetic objects (oxygen tanks, non-MR-safe equipment, personal phones/keys) cross into Zone III.
- **Zone IV** — the magnet room itself; final visual/verbal re-confirmation of screening immediately before the patient enters, every time, even for a same-day repeat exam — the projectile risk resets with every entry, not once per patient encounter.

Any implant without documented MR-conditional status: treat as a screening failure requiring device documentation (make/model/implant card) before scanning, not a judgment call at the console.

## Repeat/reject rate QA workflow

1. Log every repeated exposure with reason code (positioning, exposure, patient motion, equipment, artifact, other) at the time of the repeat, not retrospectively.
2. Calculate repeat/reject rate monthly per room: (repeated images / total images) x 100. IAC/ACR accreditation benchmarks generally expect this under 8%, with 10% as a common facility action threshold.
3. When a room trends above threshold, pull the reason-code breakdown before assigning a cause. Positioning-code clustering points to a specific technologist or a specific exam type; exposure-code clustering across multiple technologists on one room points to AEC calibration or grid/SID alignment drift — verify with a physicist before retraining staff.
4. Re-baseline after any hardware service (detector replacement, tube change, collimator service) — a post-service spike is a calibration signal, not a competency signal.

## Trauma/non-ambulatory positioning fallback order

When the standard view cannot be obtained (patient cannot stand, cannot rotate, cannot hold breath):

1. Attempt the standard projection with assistance/immobilization first.
2. If truly not obtainable, substitute the next-best projection that answers the same clinical question (e.g., cross-table lateral for a suspected C-spine injury when the patient cannot be moved, decubitus for an obstruction series when the patient cannot stand for upright).
3. Document explicitly why the standard view was not obtained — the radiologist reading the substituted view needs that context to weight what's absent, not just what's present.
4. Never force a position against a suspected fracture or instability to "match the standard view" — the substituted view exists precisely because forcing it is the higher-risk choice.
