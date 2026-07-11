# Neurology playbook

Filled protocols and scoring tables — populate with the patient in front of you, don't redesign the structure each time.

## Stroke code timeline (target metrics, AHA/ASA 2019)

| Milestone | Target from ED arrival | Why it matters |
|---|---|---|
| Door to physician | ≤10 min | Starts the clock on everything downstream |
| Door to CT (non-contrast) | ≤20 min | Rules out hemorrhage before any thrombolytic decision |
| Door to CT read | ≤45 min | Determines ASPECTS and tPA eligibility |
| Door to needle (tPA bolus) | ≤60 min (stretch goal ≤45 min) | Each minute saved ≈ 1.9M neurons (Saver 2006) |
| Door to groin puncture (thrombectomy, LVO) | ≤90 min | Applies when CTA confirms large-vessel occlusion |

**Weight-based alteplase dosing:** 0.9 mg/kg, max total 90 mg. 10% as IV bolus over 1 minute, 90% as infusion over 60 minutes.

Worked example at three weights:

| Weight | Total dose (0.9 mg/kg) | Bolus (10%) | Infusion (90%) | Check |
|---|---|---|---|---|
| 60 kg | 54.0 mg | 5.40 mg | 48.60 mg | 5.40 + 48.60 = 54.0 ✓ |
| 78 kg | 70.2 mg | 7.02 mg | 63.18 mg | 7.02 + 63.18 = 70.2 ✓ |
| 105 kg | 94.5 mg → capped at 90 mg | 9.00 mg | 81.00 mg | 9.00 + 81.00 = 90.0 ✓ (cap binds above ~100 kg) |

**Absolute contraindications to check before bolus:** active internal bleeding, prior intracranial hemorrhage, known intracranial neoplasm/AVM/aneurysm, ischemic stroke or head trauma within 3 months, suspected aortic dissection, platelet count <100,000, current anticoagulant use with INR >1.7 or elevated PT/PTT, or blood pressure not controllable below 185/110 despite treatment.

## Thrombectomy eligibility (large-vessel occlusion, extended window)

Standard window: ≤6 hours from last known well with confirmed LVO on CTA. Extended window (6–24 hours): requires perfusion imaging (CT perfusion or MRI-DWI/perfusion mismatch) meeting DAWN or DEFUSE 3 criteria — small infarct core relative to clinical deficit severity or perfusion deficit. Do not order perfusion imaging inside the standard window if it would delay the groin-puncture target; it's a tool for the 6–24h decision, not a routine add-on.

## TIA / minor stroke workup pathway

1. **Score for documentation, not for triage gating:** ABCD2 (Age ≥60: 1pt, BP ≥140/90: 1pt, Clinical unilateral weakness: 2pt / speech disturbance without weakness: 1pt, Duration ≥60min: 2pt / 10–59min: 1pt, Diabetes: 1pt; max 7). A score of 6–7 = high 2-day recurrence risk in the original validation, but same-day workup applies regardless of score.
2. **Same-day imaging:** MRI brain with DWI (more sensitive than CT for the small infarcts that confirm a "TIA" was actually a minor stroke), plus vascular imaging of the neck (carotid duplex or CTA) to find a surgically actionable stenosis.
3. **Cardiac workup:** ECG plus telemetry/prolonged monitoring (24–72h at minimum) to catch paroxysmal atrial fibrillation; echocardiogram if embolic source suspected and vascular workup is negative.
4. **Disposition rule of thumb:** ABCD2 ≥4, or any high-risk imaging/vascular finding, or unclear reliability for rapid outpatient follow-up → admit or observe. Low score with normal MRI-DWI, no significant stenosis, and same-day follow-up arranged → outpatient workup is reasonable case-by-case.

## First unprovoked seizure pathway

1. Confirm it was a true unprovoked seizure, not a mimic (syncope, psychogenic non-epileptic event, migraine with aura) — witness account of tonic-clonic activity, post-ictal confusion, and tongue biting/incontinence support a true seizure.
2. MRI brain with epilepsy protocol (thin cuts through the temporal lobes) + EEG (ideally within 24–48h, sleep-deprived if the first is normal and suspicion remains).
3. **Recurrence-risk fork:** normal MRI + non-epileptiform EEG → recurrence risk ~30–40% over several years (Krumholz/AAN-AES 2015) → default to *not* starting an anti-seizure medication, counsel on driving/safety restrictions per state law instead.
   Structural lesion on MRI, or epileptiform EEG, or prior significant brain insult (stroke, trauma, CNS infection) → recurrence risk climbs into the ~60%+ range → starting an ASM is reasonable to discuss with the patient.
4. Document the discussion and the patient's stated preference either way — this is a shared decision, not a protocol-only call.

## Status epilepticus drug ladder (time-based, from seizure onset — not from arrival)

| Time from onset | Action |
|---|---|
| 0–5 min | Ongoing seizure activity at 5 min meets the operational definition of status epilepticus — start treatment now, don't wait for a fixed duration to "confirm" it. |
| 5 min | First-line: benzodiazepine — lorazepam 0.1 mg/kg IV (max 4mg/dose, may repeat once) OR diazepam 0.15–0.2 mg/kg IV OR midazolam 10mg IM if no IV access. |
| 20 min | If still seizing: second-line IV ASM — fosphenytoin 20 mg PE/kg, OR valproate 40 mg/kg, OR levetiracetam 60 mg/kg (max 4500mg) — per AES 2016, no single agent shown clearly superior; choice driven by comorbidity (avoid valproate in known hepatic disease/pregnancy, avoid phenytoin load if cardiac conduction concern). |
| 40 min | If still seizing (refractory status): anesthetic-dose continuous infusion (midazolam, propofol, or pentobarbital) with continuous EEG monitoring and ICU-level airway management. |

## Peripheral localization table (pattern → likely site → confirming test)

| Pattern | Likely site | Confirming test |
|---|---|---|
| Distal, symmetric, stocking-glove sensory loss + reduced ankle reflexes | Length-dependent polyneuropathy | NCS: reduced sensory amplitudes distally; check A1c, B12, TSH, SPEP first (most common reversible causes) |
| Foot drop, normal reflexes, sensory loss over dorsum of foot only | Peroneal neuropathy at fibular head | NCS/EMG distinguishing peroneal-only conduction block from L5 root pattern |
| Ptosis + diplopia worsening through the day, normal pupils | Neuromuscular junction (myasthenia gravis) | AChR/MuSK antibodies, repetitive nerve stimulation or single-fiber EMG, ice-pack test |
| Ascending symmetric weakness + areflexia over days, recent GI/respiratory illness | Acute inflammatory demyelinating polyneuropathy (GBS) | LP (albuminocytologic dissociation), NCS, bedside FVC/NIF trend |
| Proximal weakness, normal sensation, elevated CK | Myopathy | CK, EMG (myopathic units), consider muscle biopsy if inflammatory myopathy suspected |
