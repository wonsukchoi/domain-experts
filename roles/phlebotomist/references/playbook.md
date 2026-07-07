# Phlebotomist — Playbook

## Order-of-draw reference (CLSI GP41)

| Order | Tube type | Cap color | Additive | Why this position |
|---|---|---|---|---|
| 1 | Blood culture bottles | Yellow (SPS) | Sodium polyanetholesulfonate | Sterility — drawn before any other puncture-adjacent tube contact |
| 2 | Coagulation | Light blue | Sodium citrate | Most sensitive to additive carryover; must precede clot activator/anticoagulant tubes |
| 3 | Serum (with or without clot activator) | Gold/red (SST) | Clot activator, gel separator | Clot activator can affect downstream anticoagulated tubes if drawn earlier |
| 4 | Heparin | Green | Sodium/lithium heparin | — |
| 5 | EDTA | Lavender/purple | K2EDTA | Chelates calcium — carryover into citrate tube would corrupt coag results if drawn earlier |
| 6 | Glycolytic inhibitor | Gray | Sodium fluoride/potassium oxalate | Fluoride carryover inhibits enzymes used in other tests |

**Discard-tube rule:** if using a winged/butterfly set and the FIRST tube of the sequence is a coagulation (citrate) tube, draw a discard tube (any non-additive or same-type tube) first to clear ~0.5–1 mL of tubing dead-space air. Skip this step if the citrate tube is not first in the sequence, or if the collection set has a built-in air-eliminator.

## Fill-volume rejection thresholds

| Tube type | Minimum acceptable fill | Consequence of underfill |
|---|---|---|
| Citrate (coag) | 90% of stated draw volume | Falsely prolonged PT/INR — reject below threshold |
| EDTA | ~75–80% (analyzer-dependent) | Dilution effect on CBC indices; check local SOP |
| SST/serum | No hard minimum, but insufficient volume for requested tests = reject | Insufficient quantity, not a ratio problem |
| Gray (fluoride) | ~75–80% (analyzer-dependent) | Dilution affects glucose accuracy |

**Worked check:** citrate tube nominal volume 2.7 mL → minimum acceptable = 2.7 × 0.90 = 2.43 mL. A measured fill of 1.9 mL = 70.4% → **reject, recollect.**

## Specimen-rejection decision table

| Defect observed | Reject whole panel? | Notes |
|---|---|---|
| Visible hemolysis (pink/red plasma) | No — reject analyte-specific (K+, LDH, AST) unless whole tube grossly hemolyzed | Check lab's hemolysis-index cutoff before broad rejection |
| Clot present in anticoagulated tube | Yes, that tube | Clot indicates additive/blood didn't mix — inversion or fill-timing failure |
| Underfilled citrate (<90%) | Yes, that tube (coag results only) | Other tubes from the same draw unaffected if independently adequate |
| Wrong tube type for ordered test | Yes, that tube | Recollect in correct tube; do not attempt to "make do" |
| Missing/illegible label, or label doesn't match requisition | Yes, entire specimen | Cannot verify patient identity — this is a patient-safety rejection, not a quality one |

## Difficult-venipuncture escalation sequence

1. **Attempt 1** — standard site (antecubital preferred), standard technique.
2. If unsuccessful: reassess — different site (opposite arm, hand), consider butterfly set for small/fragile veins.
3. **Attempt 2** — new site, adjusted technique.
4. If unsuccessful after 2 attempts: **stop.** Escalate to a second phlebotomist, a vascular-access specialist, or (in some facilities) a nurse with IV-line draw capability.
5. Document: sites attempted, technique used, reason for escalation — so the next attempt doesn't repeat a known-failed approach.

## Filled example — accessioning/rejection note

```
Specimen Rejection Notice

Patient: [MRN redacted]
Ordering provider: Dr. [name]
Test ordered: PT/INR
Tube received: Light blue (citrate), fill volume 1.9 mL
Required minimum: 2.43 mL (90% of 2.7 mL nominal)
Fill percentage: 70.4%

Disposition: REJECTED — underfilled citrate tube. Additive-to-blood ratio outside
acceptable range; PT/INR result would be falsely prolonged if run on this specimen.

Action taken: Recollection requested. Ordering unit notified at [time].
Phlebotomist: [initials]. Discard-tube protocol confirmed used for recollection
(butterfly set, citrate tube drawn second in sequence).
```
