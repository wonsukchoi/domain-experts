# Vocabulary

### MR Conditional
A device labeling category meaning the item is safe to scan only under specific stated conditions (field strength, gradient slew rate, SAR, positioning) — not safe under any MR environment.
**In use:** "It's MR Conditional at 1.5T under the labeled SAR limit, but this order is for the 3T magnet, so the conditional clearance doesn't transfer."
**Common misuse:** Treating "MR Conditional" as a synonym for "MR Safe" and assuming the device is fine at any field strength or protocol once any conditional clearance exists.

### Zone III / Zone IV
The ACR's four-tier physical access system for an MR suite; Zone III is the restricted staff/screened-patient area outside the magnet room, Zone IV is the magnet room itself.
**In use:** "She flagged the detector in Zone III — full re-wand before she goes into Zone IV."
**Common misuse:** Treating Zone III as functionally equivalent to Zone II (general restricted area) rather than a hard screening checkpoint every single entry requires.

### SAR (Specific Absorption Rate)
The rate of RF energy deposited per kilogram of tissue during a scan, expressed in W/kg, bounded by regulatory ceilings that depend on the scanner's operating mode.
**In use:** "Trailing six-minute average is sitting at 1.85, we've got 0.15 W/kg of headroom before the Normal Operating ceiling."
**Common misuse:** Quoting the First Level Controlled ceiling (4.0 W/kg) as "the SAR limit" when the scanner is actually running in Normal Operating Mode (2.0 W/kg), understating how little headroom actually exists.

### NSF (Nephrogenic Systemic Fibrosis)
A rare but serious fibrosing condition linked to gadolinium-based contrast retention in patients with significantly reduced renal function, with risk varying sharply by agent class.
**In use:** "GFR's 22 and this is a Group I agent order — that needs a radiologist sign-off before we inject, not a substitution on our own."
**Common misuse:** Treating "no reaction last time" as equivalent to "cleared for contrast now," ignoring that renal function and agent class, not injection history, drive NSF risk.

### Group I / Group II gadolinium agents
The ACR Manual on Contrast Media's risk stratification of gadolinium-based contrast agents by their reported association with NSF at reduced renal function.
**In use:** "It's a Group II agent — gadobutrol — so we're proceeding on standard weight-based dosing; still logging the current creatinine either way."
**Common misuse:** Assuming all gadolinium agents carry the same NSF risk profile and applying a single blanket GFR cutoff regardless of which agent is ordered.

### Quench
The rapid, forced boil-off of a superconducting magnet's cryogen (helium), venting it out of the building; can be triggered deliberately in an emergency or occur unintentionally.
**In use:** "That's not just loud cryogen noise, that's a quench — clear the room and hold until engineering confirms oxygen levels."
**Common misuse:** Assuming any loud venting sound is routine cooling-system noise rather than escalating it as a potential life-safety event.

### First Level Controlled Operating Mode
An IEC 60601-2-33 SAR/gradient operating mode allowing higher exposure ceilings than Normal Operating Mode, permitted only with physician acknowledgment and added physiologic monitoring.
**In use:** "We'd need to formally invoke First Level Controlled and get sign-off before running this sequence at those parameters — we're not just going to assume we're already in it."
**Common misuse:** Citing the First Level Controlled ceiling as the applicable limit for a scan that was never actually escalated into that mode.

### Ferromagnetic detection system
Hand-held wand or walk-through/portal detectors used to physically screen patients, staff, and equipment for ferromagnetic material before Zone III/IV entry, as a check behind the paper/EHR screening form.
**In use:** "Screening form's clean, but she's still getting hand-wanded before the table — that's not optional."
**Common misuse:** Treating a completed screening questionnaire as sufficient on its own and skipping the physical detector pass under time pressure.

### Pulse sequence protocol
The named, parameterized set of sequences (e.g., T1, T2 FLAIR, DWI, T1 SPACE) run for a given exam type, each with its own TR/TE/flip-angle/coverage tradeoffs.
**In use:** "Swapping in T1 SPACE 3D shortens the exam but changes the SAR budget for the rest of the protocol — that's not a free substitution."
**Common misuse:** Treating protocol substitutions purely as time-savers without recomputing the safety and diagnostic-scope tradeoffs they carry.

### dB/dt (gradient slew rate)
The rate of change of the magnetic field gradient over time, bounded to limit peripheral nerve stimulation risk, independent of the SAR/RF heating limit.
**In use:** "Fast gradient-echo sequences push dB/dt harder than SAR — that's a separate ceiling, not the same number."
**Common misuse:** Conflating gradient-related limits (nerve stimulation) with RF-related SAR limits (tissue heating) as if one console warning covers both.

### Coil
The receive (and sometimes transmit) hardware placed on or around the anatomy being imaged, selected to match the exam's field of view and required signal-to-noise.
**In use:** "Wrong coil for this field of view — we'd be trading SNR for a shorter setup, and the radiologist needs the SNR for this indication."
**Common misuse:** Treating coil selection as a setup-convenience choice rather than a diagnostic-yield decision tied to the specific clinical question.

### MR Medical Director
The physician (typically a radiologist) formally designated to own site MR safety policy and clearance escalations, distinct from the reading radiologist on a given case.
**In use:** "This is an ambiguous device clearance — that goes to the MR Medical Director, not just whichever radiologist is reading today."
**Common misuse:** Assuming any radiologist on shift can make a site-level safety-policy exception rather than routing it to the designated MR Medical Director.
