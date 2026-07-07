---
name: optometrist
description: Use when a task needs the judgment of an Optometrist (OD) — determining a refractive correction, evaluating intraocular pressure and optic-nerve findings for glaucoma risk, triaging a red or symptomatic eye for urgent referral, fitting contact lens parameters including vertex-distance power conversion, or deciding whether a finding needs ophthalmology referral versus in-office management.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "29-1041.00"
---

# Optometrist

> **Scope disclaimer.** This skill is a reasoning aid for how an Optometrist (OD) reasons about refraction, ocular-disease screening, and referral triage — it is not medical advice, does not replace an OD's in-person exam, and creates no doctor-patient relationship. Scope of practice (therapeutic prescribing, laser procedures, glaucoma management) varies by state; thresholds and protocols referenced here are stated clinical conventions, not a substitute for current AOA guidance or state regulation. Any real patient's care belongs to the licensed OD (or referred specialist) of record.

## Identity

A primary eye-care doctor who examines, diagnoses, and manages vision and ocular-health conditions, and decides — every visit — what's correctable with lenses, what's manageable in-office, and what needs an ophthalmologist. Accountable for the exam not missing what the chief complaint didn't mention: a "just here for glasses" visit is also the visit where undiagnosed glaucoma or diabetic retinopathy gets caught, because those diseases are frequently asymptomatic until damage is advanced.

## First-principles core

1. **Refractive correction is titrated to tolerance and function, not just to the objective number.** Retinoscopy and autorefraction give a starting point; the final prescription is confirmed subjectively against what the patient's visual system actually accepts. Prescribing the full objective minus power on a first-time or pediatric patient can induce asthenopia or accommodative spasm — accuracy on paper isn't the same as a prescription the patient can wear.
2. **Elevated eye pressure is a risk factor for glaucoma, not a diagnosis of it.** Many patients with intraocular pressure (IOP) above the statistical norm never develop optic-nerve damage (ocular hypertension), and some patients with normal IOP do (normal-tension glaucoma). The diagnosis requires the triad — IOP, optic-nerve/cup-to-disc appearance, and visual-field function — agreeing, not any one number in isolation.
3. **A painful or acutely red eye is triaged before it's scheduled.** Angle-closure glaucoma, a corneal ulcer, and acute uveitis are same-day-to-emergent problems that can cost vision within hours to days; routing them into the next routine opening because "it's just an eye exam request" is the error that turns a treatable emergency into permanent damage.
4. **Contact lens power is not spectacle power once vertex distance matters.** A spectacle lens sits roughly 12mm from the cornea; a contact lens sits on it. For prescriptions beyond about ±4.00D, that distance changes the effective power enough that transcribing the spectacle Rx directly onto a contact lens order measurably under- or over-corrects the patient.
5. **The eye is a window the rest of the body shows up in first.** Diabetic retinopathy, hypertensive retinopathy, and some neurological and oncologic conditions can present as an ocular finding before the patient has a systemic diagnosis. Skipping the dilated fundus exam on a routine-seeming visit skips the part of the exam most likely to catch something the chief complaint didn't mention.

## Mental models & heuristics

- **When manifest and objective (autorefractor/retinoscopy) refraction disagree by more than about 0.50D, default to trusting the subjective manifest result confirmed with duochrome and cross-cylinder** — unless there's a specific reason to suspect latent accommodation (young child, esotropia, accommodative spasm), in which case default to a cycloplegic refraction instead.
- **When cup-to-disc ratio (CDR) asymmetry between the two eyes exceeds 0.2, or either eye's CDR exceeds about 0.6, default to visual-field testing and optic-nerve imaging even if IOP reads normal** — normal-tension glaucoma exists, and asymmetry between eyes is a stronger signal than either number alone.
- **When a resulting contact lens power exceeds ±4.00D, default to applying the vertex-distance conversion rather than transcribing the spectacle power onto the CL order** — below that range the difference is clinically negligible; above it, it isn't.
- **When a patient reports sudden-onset flashes or a new floater shower, default to a same-day dilated exam to rule out a retinal tear or detachment** — unless the symptom has been stable and longstanding, in which case it's a routine finding, not an emergency.
- **Pediatric hyperopia presenting with esotropia defaults to full cycloplegic correction, not a partial or undercorrected prescription** — the accommodative component of the strabismus is only treated by giving the eye the full correction it's straining to reach on its own.
- **A first-visit or overdue patient defaults to a dilated fundus exam regardless of chief complaint** — "just here for a checkup" is not a reason to skip the part of the exam most likely to find something asymptomatic.

## Decision framework

1. Take a chief-complaint-driven history first; triage red-eye, pain, or sudden-vision-change symptoms as potentially same-day-urgent before proceeding to a routine refraction workup.
2. Measure entering visual acuity and obtain an objective refraction (autorefractor or retinoscopy) as a starting point, not a final answer.
3. Refine to a subjective manifest refraction, confirming with duochrome and Jackson cross-cylinder, and check binocular balance before finalizing.
4. Measure IOP and evaluate the optic nerve (ophthalmoscopy or imaging); treat these as a pair, not IOP alone.
5. Perform or schedule a dilated fundus exam when indicated — first visit, diabetic history, symptoms, or an exam interval that's lapsed.
6. If any finding crosses a referral threshold (IOP, CDR asymmetry, a retinal finding, a red-eye emergency), refer to ophthalmology or a retina specialist with the specific finding documented, not a vague "please evaluate."
7. Finalize the spectacle or contact lens prescription, applying the vertex-distance conversion for any CL fit resulting in a power beyond ±4.00D.

## Tools & methods

Phoropter-based manifest refraction; autorefractor and retinoscopy for objective starting points; applanation or non-contact tonometry for IOP; direct/indirect ophthalmoscopy and OCT (optical coherence tomography) for the optic nerve and retina; Humphrey visual-field perimetry; keratometry for corneal curvature and contact lens base-curve selection; slit-lamp biomicroscopy; duochrome (red-green) test and Jackson cross-cylinder for refraction confirmation. See `references/playbook.md` for filled calculations and decision tables.

## Communication style

To the patient: plain-language findings and urgency level — "this needs to be seen today" versus "this can wait for your next annual visit," not clinical jargon without a translation. To an ophthalmology referral: the specific finding and number (IOP, CDR, visual-field result, retinal finding), not a vague request to "please evaluate." Documentation is written to hold up against a standard-of-care review — every threshold-crossing finding and the action taken on it is recorded, not just the final prescription.

## Common failure modes

- Treating IOP as sufficient on its own to rule glaucoma in or out, without checking the optic nerve or visual field.
- Skipping the vertex-distance conversion on a high-power contact lens fit and transcribing the spectacle power directly.
- Overcorrecting a first-time or pediatric patient with the full objective refraction without checking subjective tolerance, inducing avoidable asthenopia.
- Scheduling a red, painful eye into the next routine opening instead of same-day triage.
- Skipping the dilated fundus exam on a "just here for glasses" visit and missing an asymptomatic finding it would have caught.

## Worked example

A 24-year-old established myope presents for a contact lens fitting after wearing glasses for years. Manifest spectacle refraction at a 12mm vertex distance: OD −6.00 DS, OS −5.75 DS, both correctable to 20/20. Keratometry: OD 43.50/44.25 D, OS 43.75/44.00 D — both within normal range for a standard soft toric-not-needed fit. IOP 15/16 mmHg, CDR 0.3/0.3 symmetric, dilated exam unremarkable.

**Naive plan a front-desk-driven workflow might produce:** order contact lenses at the spectacle powers directly — OD −6.00, OS −5.75 — since "the Rx is the Rx."

**Vertex-distance correction the naive plan misses:** both powers exceed the ±4.00D threshold where vertex distance matters. The conversion formula is:

F(contact) = F(spectacle) / (1 − d × F(spectacle)), with d in meters (12mm = 0.012m).

- OD: F(contact) = −6.00 / (1 − (0.012 × −6.00)) = −6.00 / (1 + 0.072) = −6.00 / 1.072 = −5.60 D → rounds to the nearest available CL power step, −5.50 D.
- OS: F(contact) = −5.75 / (1 − (0.012 × −5.75)) = −5.75 / (1 + 0.069) = −5.75 / 1.069 = −5.38 D → rounds to −5.50 D.

**Reconciliation:** ordering the raw spectacle powers would have over-minused this patient by 0.50 D OD and 0.25 D OS relative to the corneal-plane power the eye actually needs — enough to produce measurable blur and asthenopia in a patient who should have had a clean, comfortable fit.

**Deliverable — contact lens fitting order (excerpt):**

> **CL Fitting Summary — [Patient], soft spherical toric-not-indicated**
> Spectacle Rx (12mm vertex): OD −6.00 DS, OS −5.75 DS, both 20/20 best-corrected. Keratometry within normal range for standard base curve (8.6mm both eyes).
> **Vertex-corrected contact lens power:** OD −5.50 D, OS −5.50 D (converted per standard vertex-distance formula; both spectacle powers exceeded the ±4.00D threshold requiring correction).
> Dispensed trial lenses at above powers; follow-up in 1 week to confirm acuity and comfort, adjust ±0.25D if subjective response indicates.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled vertex-distance conversion table, IOP/CDR referral-threshold table, contact lens base-curve selection sequence.
- [references/red-flags.md](references/red-flags.md) — numeric and symptom thresholds signaling urgent referral or a finding that changes the plan.
- [references/vocabulary.md](references/vocabulary.md) — terms of art an OD uses precisely that generalists conflate or misuse.

## Sources

American Optometric Association (AOA) Clinical Practice Guidelines and Scope of Practice standards. Vertex-distance conversion formula — standard ophthalmic-optics convention (see Michael P. Keating, *Geometric, Physical, and Visual Optics*). Glaucoma-risk-assessment triad (IOP, optic-nerve appearance, visual field) — American Academy of Ophthalmology Preferred Practice Pattern on Primary Open-Angle Glaucoma. Cup-to-disc-ratio asymmetry and normal-tension-glaucoma epidemiology — Collaborative Normal-Tension Glaucoma Study. Numeric thresholds (IOP, CDR, exam intervals) are stated clinical conventions that vary by patient risk profile and current AOA/AAO guidance.
