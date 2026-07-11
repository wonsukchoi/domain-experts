# MRI Technologist Playbook

Filled parameter tables and decision sequences. Facility policy, scanner vendor documentation, and manufacturer device labeling always override anything here.

## Zone system entry rules

| Zone | Access control | What crosses the boundary here |
|---|---|---|
| I | Public (waiting/reception) | No MR-specific screening |
| II | Interface between public and controlled area (interview/screening room) | Screening form completed, ferromagnetic items identified for removal |
| III | Restricted, badge/escort only (control room, prep) | Hand-wand re-screen of patient and any accompanying person; all loose ferromagnetic items secured outside |
| IV | The magnet room itself | Only screened patient, screened staff, and confirmed MR Conditional/Safe equipment enter; door closed during scan |

- The 5-gauss line (the fringe-field contour where the static field first becomes physiologically and ferromagnetically significant) conventionally marks the Zone III/IV boundary per ACR siting guidance; detector setpoints below that facility-specific line still trigger the same mandatory re-screen.
- Anyone entering Zone IV who was not personally screened at Zone III (a second staff member, a parent, emergency responder) gets the full screening form and hand-wand, no exception for perceived urgency.
- A Zone III→IV re-screen is required every entry, not once per visit — an item retrieved from a bag between screening and the table is unscreened.

## Implant / device screening sequence

1. Ask the open-ended question first ("has anything ever been placed in or on your body") before the checklist — patients underreport when asked yes/no about a specific device list.
2. For any named implant, obtain the exact manufacturer and model, not just the device class ("pacemaker" is not enough; "Medtronic Azure XT DR MRI SureScan" is).
3. Cross-check the model against manufacturer MR-status documentation or an implant database (e.g., MRIsafety.com). Three possible results:
   - **MR Safe** — no field strength restriction from the device itself.
   - **MR Conditional** — scan permitted only under the specific field strength, gradient, and SAR conditions in the labeling; deviate from any one condition and the conditional clearance no longer applies.
   - **MR Unsafe**, unknown, or unverifiable — treat as contraindicated pending confirmation or an explicit emergent risk-benefit decision by the ordering clinician and radiologist, documented as an exception.
4. For cardiac implantable electronic devices (pacemaker/ICD) labeled MR Conditional: pre-scan device interrogation, programming to the labeled MRI mode, continuous monitoring per facility protocol, and post-scan re-interrogation before the patient leaves.
5. Document the verified model, MR-status source checked, and clearance decision in the record — a screening that isn't documented is, for QA purposes, a screening that didn't happen.

## SAR mode ceilings (IEC 60601-2-33 / FDA guidance)

| Mode | Whole-body SAR | Head SAR | Local (any 10g tissue) | Requires |
|---|---|---|---|---|
| Normal Operating | 2.0 W/kg (6-min rolling average) | 3.2 W/kg | 10 W/kg (head/torso), 12 W/kg (extremity) | Default mode, no added sign-off |
| First Level Controlled | 4.0 W/kg | 3.2 W/kg | Same local limits, tighter monitoring | Physician acknowledgment; monitored physiologic parameters for at-risk patients |

- Default protocol edits (TR, flip angle, echo train length) against the ceiling of the mode the scanner is actually running in — not the higher First Level Controlled number, unless that mode has been explicitly invoked and signed off for this patient.
- When predicted SAR for a new sequence, combined with the trailing rolling-average window, would exceed the active mode's ceiling: extend TR first, then reduce flip angle, before reducing averages/resolution — in that preference order, since TR/flip-angle changes cost the least diagnostic signal per W/kg recovered.

## Gadolinium agent NSF-risk classes (ACR Manual on Contrast Media)

| Class | Example agents | NSF risk at reduced GFR | Technologist action |
|---|---|---|---|
| Group I | Gadodiamide, gadopentetate dimeglumine, gadoversetamide | Highest reported NSF association | If GFR <30 or unknown/AKI: do not administer without radiologist sign-off; flag before injecting |
| Group II | Gadobutrol, gadoterate meglumine, gadoteridol, gadobenate | Low to negligible reported association, even at reduced GFR | Administer per standard weight-based dosing; still document current GFR/creatinine in the record |
| Group III | Gadoxetate disodium and similar limited-data agents | Insufficient data to fully classify | Treat with Group I-level caution absent facility-specific guidance |

- Standard gadolinium dosing is weight-based (commonly 0.1 mmol/kg for extracellular agents at 1.0 mmol/mL concentration); confirm the programmed power-injector volume against the patient's current weight, not a prior visit's weight on file.
- A prior uneventful gadolinium administration is not a substitute for checking current renal function — GFR can decline between visits.

## Motion / artifact triage order

1. Confirm patient positioning and coil placement matched the protocol before blaming the sequence.
2. Check for gross patient motion on the scout/localizer before running the full diagnostic sequence — catch it before spending the full acquisition time.
3. If a sequence comes back non-diagnostic (motion, wrap, incomplete coverage), repeat it immediately while the patient is still positioned, rather than sending it forward and hoping the radiologist can work around it.
4. Escalate a repeat pattern (same artifact across multiple patients same day) to physics/service before assuming it's patient-specific.
