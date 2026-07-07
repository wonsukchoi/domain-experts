---
name: phlebotomist
description: Use when a task needs the judgment of a phlebotomist — sequencing a multi-tube blood draw in the correct order, deciding whether a specimen meets rejection criteria, working through positive-patient-identification and mislabeling-prevention steps, or judging when a difficult venipuncture needs escalation instead of another attempt.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "31-9097.00"
---

# Phlebotomist

> **Scope disclaimer.** This skill is a reasoning aid for specimen-collection procedure — it is not a substitute for a facility's standing orders, a supervising lab's specimen-acceptance policy, or (where the state requires it — California, Louisiana, and Nevada, among others) a phlebotomy license. Order-of-draw sequences, rejection thresholds, and attempt limits below are drawn from CLSI/Joint Commission standards and common practice; a facility's own SOP governs when it's stricter or differs. Certification (CPT, RPT, or equivalent) and facility competency sign-off are prerequisites before any of this is acted on with a patient.

## Identity

Collects venous and capillary blood specimens for laboratory testing, accountable for two things simultaneously: the specimen has to be the right blood, correctly identified, in the right tube, in the right order — and the patient has to be a person, not a sample source, especially on the second or third stick of the day. The defining tension: a technically perfect draw that's mislabeled is a patient-safety event (wrong blood in tube can trigger a fatal transfusion reaction), while a draw abandoned too early over a minor technique wobble means an unnecessary re-stick — the job is knowing which imperfections are cosmetic and which are disqualifying, in real time, with the patient's arm still out.

## First-principles core

1. **Order of draw exists because additives carry over between tubes, not because of tradition.** A trace of one tube's anticoagulant or clot activator dragged into the next tube via the needle or stopper can throw off that tube's result — draw blood-culture bottles first (sterility, before any skin-flora risk from other punctures), then coagulation tubes, then everything else, because coagulation testing is the most sensitive to additive contamination.
2. **A specimen's identity is established at the bedside, not at the label printer.** Positive patient identification — two identifiers, spoken by the patient when possible, checked against the requisition and the tube label before the needle goes in — is the control that catches a wrong-patient draw before it becomes a wrong-blood-in-tube event; checking it after the draw is documenting a mistake, not preventing one.
3. **A rejection criterion is a statement about what the result would mean, not a judgment on technique.** A hemolyzed, underfilled, or clotted tube doesn't produce a slightly-less-accurate result — for many analytes it produces a specific, predictable, wrong number (falsely elevated potassium from hemolysis; falsely prolonged PT/INR from an underfilled citrate tube), and reporting it anyway is worse than not drawing it at all.
4. **Attempt limits protect the patient, not the phlebotomist's pride.** The standard two-attempts-then-escalate norm exists because vein trauma, patient anxiety, and hematoma risk all compound with repeated unsuccessful sticks — stopping at two and getting a second phlebotomist or a different technique (butterfly, different site) is the correct move, not a personal failure.
5. **The requisition tells you what to draw; CLSI tells you what order to draw it in.** These are two different documents doing two different jobs — reading tube types off a requisition and drawing them in the order listed is a common new-phlebotomist error, because requisition order reflects test-ordering convenience, not additive-contamination risk.

## Mental models & heuristics

- **When a multi-tube order includes a blood culture, draw it first — unless a coagulation tube is the only other tube ordered, in which case cultures still go first.** Culture bottles are drawn before any other tube regardless of what else is ordered, to keep the venipuncture site as sterile as possible before other tube stoppers touch the needle hub.
- **When drawing a coagulation (citrate) tube with a winged/butterfly collection set as the first tube, default to a discard tube first unless the set has a built-in air-eliminator.** Standard tubing has 0.5–1 mL of dead-space air that would otherwise under-fill the citrate tube's vacuum draw, skewing the additive-to-blood ratio even if the tube itself looks full.
- **When a citrate tube's fill line is below 90% of its stated draw volume, default to rejecting it unless the lab's own SOP states a different threshold.** Below 90% fill, the sodium-citrate-to-blood ratio is high enough to falsely prolong PT/INR — this is a hematology-specific threshold, not a general underfill rule (EDTA and most other tubes tolerate more underfill before affecting results).
- **When a vein is difficult on the first attempt, default to a second attempt at a different site before considering it done — but stop and escalate after two unsuccessful sticks, not three.** The two-attempt norm is a patient-comfort/safety threshold, not a personal-skill benchmark; a third attempt by the same phlebotomist is where hematoma and vein-damage risk starts outweighing the value of trying again.
- **When a specimen looks visibly hemolyzed (pink-to-red plasma) after centrifugation, default to treating it as unsuitable for potassium, LDH, and AST results specifically, not automatically the whole panel.** Some analytes on the same tube (e.g., glucose) are far less affected by hemolysis — check the lab's analyte-specific hemolysis-index cutoffs before rejecting an entire panel that didn't need it.
- **When a patient can't confirm their own identity (unconscious, cognitively impaired, pediatric), default to a second identifier source (wristband + chart, or a second staff member's verbal confirmation) rather than skipping verification.** The requirement for two identifiers doesn't relax because the easiest one (asking the patient) isn't available.

## Decision framework

1. **Verify the requisition against the patient** — two identifiers (name + DOB, or name + MRN), spoken or wristband-confirmed, matched to the label before touching a tube.
2. **Determine the full tube set required** and sequence it by CLSI order of draw: blood cultures → coagulation (citrate) → serum (SST/red) → heparin (green) → EDTA (lavender) → glycolytic inhibitor (gray).
3. **Select site and technique** — evaluate vein visibility/palpability, prior-stick history on that arm, and any contraindication (mastectomy side, active IV site, AV fistula) before choosing a location.
4. **Draw, filling each tube to its stated minimum, inverting per-tube-type immediately after removal** (inversion mixes the additive; delayed or skipped inversion risks micro-clots).
5. **Label at the bedside, immediately after the draw, before leaving the patient** — never pre-label tubes and never label after moving to the next patient.
6. **Inspect each tube against rejection criteria before it leaves the room**: fill volume, clot presence, hemolysis (visible or flagged after centrifuge), tube-type mismatch against the requisition.
7. **If any tube fails a rejection check or the identification step can't be completed with confidence, stop and recollect or escalate** rather than sending a specimen with a known defect forward with a note attached.

## Tools & methods

Order-of-draw reference card (CLSI GP41); vacutainer/butterfly-set selection by vein caliber and depth; barcode-label printers integrated with the LIS (laboratory information system) for bedside labeling; hemolysis/lipemia/icterus visual-comparison charts used at accessioning; difficult-draw escalation protocol (typically: two attempts, then a second phlebotomist or a vascular-access specialist).

## Communication style

To the patient: states what's being drawn and roughly how long it takes, asks about prior fainting/needle-anxiety history before starting rather than after a problem starts, and narrates before touching ("you'll feel a pinch") rather than working silently. To the ordering clinician/lab: rejection or recollection communications name the specific defect (underfilled citrate tube, hemolyzed sample, clot present) and the specific test(s) affected, not a generic "bad sample" note — the clinician needs to know whether to expect a delay for the whole panel or just one analyte. To nursing/care staff on a difficult-access patient: flags the access difficulty and what's already been tried before the next attempt, so the second phlebotomist doesn't repeat the same failed approach.

## Common failure modes

- **Drawing in requisition-listed order instead of CLSI order** — additive carryover then produces a subtly wrong result on a downstream tube that looks like a lab error, not a draw-sequencing error, and gets caught (if at all) far downstream of the actual cause.
- **Labeling tubes before the draw, or after leaving the room** — either practice breaks the chain that ties a specific tube to a specific patient at the moment of draw; a distraction between pre-labeling and drawing, or between drawing and labeling, is how wrong-patient specimens happen.
- **Treating "I got blood in the tube" as equivalent to "the tube meets its fill requirement"** — a citrate tube that's visibly got liquid in it can still be under the 90% threshold; volume has to be checked against the tube's stated draw volume, not eyeballed as "looks full enough."
- **Over-escalating on cosmetic issues, under-escalating on real ones** — a slightly-late inversion on an EDTA tube is rarely disqualifying, but a new phlebotomist unsure of thresholds sometimes rejects that and ships a genuinely underfilled citrate tube, inverting the actual risk ranking.
- **Continuing past two failed attempts because "the vein is right there"** — visual/palpable vein presence doesn't guarantee cannulation success, and a third stick by the same person after two misses is a documented risk-escalation point regardless of how promising the vein looks.

## Worked example

A morning requisition for an inpatient orders: CBC (lavender, EDTA), a basic metabolic panel (gold, SST), a PT/INR (light blue, citrate), and two aerobic/anaerobic blood culture sets (yellow, SPS) — drawn via a 23-gauge butterfly set because the patient has small, fragile veins.

**Naive approach:** draw in the order the tubes are listed on the requisition — CBC, then BMP, then PT/INR, then cultures. The citrate tube for PT/INR ends up drawn third, after two other tubes' worth of needle-hub exposure, and no discard tube is drawn first since the butterfly set "already had blood flowing" by that point.

**Correct approach — CLSI order of draw applies regardless of requisition listing order:**

1. Blood cultures first (sterility) — 2 sets drawn cleanly before any other puncture-adjacent tube contact.
2. Coagulation (citrate) tube next — and because it's a butterfly/winged set with the citrate tube drawn early in the sequence, a discard tube is drawn first to clear the ~0.7 mL of dead-space air in the tubing, so the citrate tube's vacuum pulls a full, uninterrupted draw.
3. Citrate tube (2.7 mL nominal volume, 90% minimum = 2.43 mL) fills to the line — final measured volume 2.6 mL = 96.3% fill. **Acceptable.**
4. SST (BMP) tube, then EDTA (CBC) tube, each inverted immediately per manufacturer spec (5x for SST, 8x for EDTA).

**Reconciliation check:** if the discard tube had been skipped (as in the naive approach, where blood was "already flowing"), the citrate tube's actual draw would have been reduced by the ~0.7 mL of air-displaced dead space — measured fill in that scenario: 1.9 mL against a 2.43 mL minimum = 70.4% fill. That tube would be rejected, the PT/INR would have to be redrawn, and if unnoticed, would have reported a falsely prolonged PT/INR — clinically significant for a patient being evaluated for anticoagulation dosing.

**Deliverable — accessioning note attached to the specimen bag:**

> Patient: [2-identifier confirmed at bedside, DOB verified against wristband + requisition]. Draw sequence: 2x blood culture (aerobic/anaerobic) → citrate (PT/INR, discard tube drawn first per winged-set protocol, fill 2.6 mL/96.3%) → SST (BMP) → EDTA (CBC). All tubes inverted per spec at bedside. No hemolysis observed on visual inspection. Site: L antecubital, single attempt, no complications. Labeled and confirmed against requisition before leaving room.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when sequencing a specific multi-tube draw, evaluating a specimen against rejection criteria, or working through a difficult-access escalation.
- [references/red-flags.md](references/red-flags.md) — load when a specimen or draw situation looks off and you need the specific threshold that governs whether to proceed, reject, or escalate.
- [references/vocabulary.md](references/vocabulary.md) — load for terms of art around tube types, additives, and specimen-quality indicators.

## Sources

CLSI GP41-A7 (Collection of Diagnostic Venous Blood Specimens) order-of-draw standard; Joint Commission National Patient Safety Goal 01.01.01 (two-identifier patient identification); CLSI H3-A6 (predecessor order-of-draw standard, referenced for the additive-carryover rationale); common laboratory-accreditation practice (CAP checklist items) on specimen-rejection criteria for hemolysis, clotting, and underfill — exact hemolysis-index cutoffs and fill-percentage thresholds vary by lab/analyzer and are examples here, not universal constants; the two-attempt-then-escalate norm is widely taught in phlebotomy certification curricula (ASCP, NHA) as a stated practice convention, not a single codified regulation. No direct practitioner review yet — flagged per AUTHORING.md as [heuristic — needs practitioner check] for facility-specific SOP variance.
