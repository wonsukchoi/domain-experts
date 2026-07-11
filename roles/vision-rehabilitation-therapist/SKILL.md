---
name: vision-rehabilitation-therapist
description: Use when a task needs the judgment of a vision rehabilitation therapist / orientation and mobility specialist / low vision therapist — running a functional vision assessment, sequencing long-cane or ADL skills training after vision loss, prescribing a low-vision optical or electronic device, or evaluating a client's readiness for street-crossing or bioptic-driving training.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "29-1122.01"
---

# Vision Rehabilitation Therapist

> Reasoning aid for the judgment calls of a vision rehabilitation therapist (CVRT), orientation and mobility specialist (COMS), or low vision therapist (CLVT) — not a substitute for licensed ophthalmological diagnosis, ACVREP-certified practice, or the treating eye care provider's sign-off. Device prescriptions, travel-training clearances, and driving-eligibility calls belong to the certified practitioner working the case; jurisdiction (state DMV statutes, funding-agency rules) varies and must be verified directly.

## Identity

A CVRT/COMS/CLVT works for a state agency for the blind, a rehabilitation hospital, a school district, or private practice, taking a client from an ophthalmologist's diagnosis to functional independence in reading, daily living tasks, and independent travel. Accountable for whether the client can actually perform the task in their own environment — not for a chart score or a device sale. The defining tension: the job's entire value is teaching people to take on real risk (crossing streets, handling medication, using a stove) competently, while a referring physician, family, or funding agency often wants risk minimized to zero; refusing to negotiate that risk with the client is itself a failure of the job.

## First-principles core

1. **Clinical acuity and functional vision are different measurements, and neither predicts the other reliably.** A 20/70 Snellen result can be fully functional in high-contrast, well-lit, static indoor tasks and non-functional outdoors in glare with moving traffic — the acuity chart doesn't test contrast sensitivity, glare tolerance, or visual field, all of which drive real-world task success.
2. **Independence is a negotiated risk level, not an eliminated one.** A client who chooses to cross a busy intersection alone after training, knowing the actual failure modes and consequences, has exercised the autonomy the whole discipline exists to protect; a therapist who blocks that because it feels safer to control has substituted their risk tolerance for the client's and produced a client who can't function without supervision.
3. **Vision loss triggers a grief-and-adjustment process that gates skill acquisition** — a client still in denial or acute grief will not retain cane technique or ADL instruction regardless of teaching quality; psychosocial readiness has to be assessed and, where absent, addressed before or alongside skills training, not assumed to resolve itself.
4. **The device is not the intervention — the device plus the strategy plus the environment is.** A magnifier, cane, or CCTV handed over without matched illumination, technique training, and task-specific practice gets abandoned; abandonment rates for unsupported low-vision device dispensing run high enough that "did they keep using it three months later" is the real success metric, not "did they accept the device."
5. **Central-field loss and peripheral-field loss are different rehabilitation problems, not the same diagnosis at different severities.** Macular disease (central scotoma) calls for eccentric-viewing and preferred-retinal-locus training; glaucoma or retinitis pigmentosa (peripheral loss) calls for systematic scanning and cane-arc technique for missed lower obstacles — applying one generic "vision loss protocol" to both produces training that doesn't transfer.

## Mental models & heuristics

- **When functional performance and chart acuity disagree, default to a task-based functional vision assessment in the actual environment** (contrast sensitivity, glare, lighting) unless the diagnosis itself is unstable or unconfirmed, in which case route back to the eye care provider first — training on stale or wrong visual data wastes both sides' time.
- **When prescribing a low-vision device, default to the lowest magnification that clears the target task's acuity requirement plus a reading-fluency reserve, unless the task is high-precision (medication labels, insulin dosing)**, where reserve should be generous — overpowered magnification narrows field of view and working distance and is the single most common cause of device abandonment.
- **When sequencing cane travel training for an adventitiously blinded adult, default to indoor skills → sighted-guide fade → quiet residential routes → business-district routes → signaled intersections, unless the client retains significant usable vision**, in which case start with visual-motor integration and an adapted mobility device (support cane, ID cane) rather than the full long-cane progression built for clients with no useful travel vision.
- **When deciding cane vs. guide dog, default to matching the client's typical daily pace, distance, and environment, not stated preference alone** — a dog matched to a person who walks under 2 mph in a low-traffic rural area is a common cause of early dog return; the guide dog school's own intake criteria exist for this reason.
- **When a referral shows no ophthalmology visit in the last 12 months and the underlying condition is progressive, default to requesting updated acuity/field data before finalizing the training plan** unless the delay itself would deteriorate skills already in progress — training against stale visual status risks building technique around a visual field that no longer exists.
- **When a client repeatedly reschedules or stalls at a specific training milestone (street crossing, cane transition from sighted guide), default to treating it as an unresolved psychosocial signal first, a scheduling problem second.**
- **When productivity pressure from a funding agency pushes toward shortening the case, resist compressing the psychosocial-readiness step** — skills taught before readiness predict poor carryover and repeat referrals, which cost the agency more billable time than the step it tried to skip.

## Decision framework

1. **Confirm medical stability and pull current diagnosis, prognosis, acuity, and visual field data** from the treating eye care provider before any functional work begins.
2. **Run a functional vision assessment in the client's real tasks and environments** — reading, cooking, curb detection, signage — not only in a clinic setting; note where functional performance diverges from the chart numbers and why (contrast, glare, field).
3. **Assess psychosocial stage, prior rehabilitation history, and support system** before committing to a training sequence; a client in acute grief gets a different plan than one two years post-diagnosis and already adapted.
4. **Set a small number of client-prioritized, observable goals** (e.g., "read prescription labels independently," "cross the two intersections between home and the bus stop") rather than a generic full-service package.
5. **Sequence instruction to match onset type, field-loss pattern, and readiness** — central vs. peripheral loss, congenital vs. adventitious, low vision vs. no usable vision each drive a different technique and device path.
6. **Verify carryover in the actual target environment before advancing complexity** — a skill demonstrated in a controlled lesson that fails on the client's actual commute is not yet learned; document trial-by-trial success, not impression.
7. **Plan reassessment checkpoints tied to the diagnosis's trajectory** — a stable congenital condition needs a maintenance check; a progressive condition (wet AMD, diabetic retinopathy) needs scheduled re-assessment because the device and route plan will go stale.

## Tools & methods

- Functional vision assessment protocol: acuity at habitual working distance, Pelli-Robson or Mars contrast sensitivity chart, glare testing, visual field confirmation against the ophthalmology report.
- Long cane fitting and technique instruction (two-point touch, constant-contact, diagonal/Hoover technique), adapted mobility devices, dog-guide-readiness referral against the guide-dog school's own intake criteria.
- Low vision optical devices (hand and stand magnifiers, illuminated stand magnifiers, bioptic telescopes) and electronic devices (portable and desktop video magnifiers/CCTVs), selected against the magnification calculation in `references/playbook.md`, not by trial-and-error handoff.
- Structured Discovery and Systematic (graduated) Instruction — the two competing O&M teaching methodologies; pick per client per `references/vocabulary.md`, don't default to one out of habit.
- ADL (activities of daily living) instruction: label systems, medication management, non-visual and adapted cooking technique, braille/large-print/screen-reader instruction.
- Expanded Core Curriculum (ECC) domain checklist for pediatric caseloads — nine areas beyond academics; see `references/playbook.md` for the filled prioritization matrix.
- Individualized Written Rehabilitation Program (IWRP) / IEP goal documentation — funder- and school-district-facing, must carry measurable trial data, not impression language.

## Communication style

With the treating ophthalmologist/optometrist: clinical register — acuity, field, diagnosis-specific implications, requests for updated data before proceeding. With the client and family: plain-language, task-anchored ("here's the specific thing we're working toward and by when"), explicit about what risk they're choosing when they choose independence. With funders and case managers: outcome-and-trial-data register tied to the IWRP goal sheet — "crossed the residential intersection independently in 3 of 3 trials," never "doing well" or "making progress." Documentation is written to survive an audit, not to read well.

## Common failure modes

- **Treating vision loss as monolithic** — applying the same cane sequence or device logic to central-scotoma and peripheral-field-loss clients, which fails to transfer for either.
- **Over-prescribing magnification** — handing over more power than the acuity-reserve calculation requires, which narrows the field of view enough that the device gets shelved.
- **Skipping psychosocial readiness** — pushing skills training on a client still in denial, then documenting the failed carryover as the client's non-compliance rather than a sequencing error.
- **Zero-risk paternalism** — refusing to advance a client to street-crossing or bioptic-driving training because it feels safer to the therapist, without honestly quantifying the actual risk and negotiating it with the client.
- **The overcorrection of the above**: having learned "dignity of risk," clearing a client for independent travel or driving without the actual field/acuity/technique data supporting it — autonomy language used to skip a step, not just paternalism used to add one.
- **Documentation that won't survive an audit** — "client is making good progress" instead of trial counts and environments, which collapses under a funding agency's chart review.

## Worked example

**Setup.** Client: 72-year-old with wet age-related macular degeneration, referred for low vision therapy. Goal (client-stated, priority-ranked): read prescription labels and personal mail independently. Clinical data from ophthalmology: distance acuity OD 20/200, OS 20/400 (non-dominant); central scotoma OU confirmed by Amsler grid; Pelli-Robson contrast sensitivity 1.05 log units (normal range ≈1.65–2.00 log units). Near acuity at habitual 40 cm reading distance with current correction: 20/200 equivalent — client can identify large newspaper headlines only.

**Naive read.** A generalist caregiver's plan: "20/200 vision, hand them a standard 3x drugstore hand magnifier."

**Expert reasoning.** Required magnification is not a guess — it's calculated from the acuity ratio plus a reading-fluency reserve. Target print for fluent (not just threshold) reading of prescription labels is set at a 20/40 equivalent. Base magnification to match the acuity gap: 200 ÷ 40 = **5x**. Sustained reading fluency (as opposed to bare letter identification) needs an acuity reserve of roughly 2x beyond the matching threshold — standard low-vision practice, not the client's threshold performance. Total required magnification: 5 × 2 = **10x**.

A standard 3x hand magnifier undershoots this by more than a factor of three (10 ÷ 3 ≈ 3.3x underpowered) and would fail the task even before accounting for contrast: the client's Pelli-Robson score of 1.05 is well below the normal 1.65–2.00 range, meaning the device also has to supply controlled illumination and contrast, which an uncontrolled handheld lens does not. Plan: dispense a 10x illuminated stand magnifier (or portable electronic video magnifier set to 10x with contrast-enhancement mode), set task lighting to ≈600 lux at the reading plane, and train eccentric viewing to locate and use a superior preferred retinal locus around the central scotoma before handing over the device for home practice.

**Reassessment after two training sessions.** Client reads 9 of 9 prescription labels correctly using the 10x device at 600 lux task lighting, spot-reading speed adequate for the task (not timed for continuous-text fluency, which was never the goal).

**Deliverable — functional vision assessment / device recommendation note (excerpt, as filed):**

> "Near acuity 20/200 OU at habitual distance; Pelli-Robson 1.05 log units (reduced, consistent with wet AMD). Target task: prescription label and mail reading. Calculated magnification requirement 5x (acuity match) × 2x (fluency reserve) = 10x. Dispensed: 10x illuminated stand magnifier; task lighting set to 600 lux. Eccentric viewing training completed, PRL identified superior to central scotoma. Outcome: 9/9 prescription labels read correctly at week 2 follow-up. Do not step down device power based on client request for something 'less bulky' without re-running the acuity-reserve calculation — a lower-power device will re-create the original task failure."

## Going deeper

- [references/playbook.md](references/playbook.md) — magnification calculation worked table, O&M skill-progression sequence with session thresholds, device-selection table, bioptic-driving state comparison, ECC domain prioritization matrix.
- [references/red-flags.md](references/red-flags.md) — smell tests across assessment, device fitting, travel training, and case documentation, each with the first question and the data to pull.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse, with the practitioner sentence and the common misuse.

## Sources

- Blasch, B.B., Wiener, W.R., & Welsh, R.L. (Eds.), *Foundations of Orientation and Mobility*, 3rd ed. (AFB Press) — standard O&M textbook; source for cane-technique taxonomy and the Hoover/Valley Forge origin of long-cane instruction.
- Corn, A.L. & Erin, J.N. (Eds.), *Foundations of Low Vision: Clinical and Functional Perspectives*, 2nd ed. (AFB Press, 2010) — source for the clinical-vs-functional-vision distinction and acuity-reserve prescribing logic.
- Hatlen, P., "The Core Curriculum for Blind and Visually Impaired Students, Including Those with Additional Disabilities," *RE:view*, 28(1), 1996 — origin of the Expanded Core Curriculum; ninth domain (self-determination) added 2003.
- ACVREP (Academy for Certification of Vision Rehabilitation and Education Professionals) — COMS, CVRT, and CLVT certification handbooks and scope-of-practice pages, https://www.acvrep.org/certifications — source for the 350-hour supervised-internship requirement and scope boundaries between the three certifications.
- AER (Association for Education and Rehabilitation of the Blind and Visually Impaired), https://www.aerbvi.org — personnel-preparation standards and professional consensus on ECC and O&M practice.
- American Optometric Association, *Care of the Patient with Visual Impairment (Low Vision Rehabilitation)*, consensus-based clinical guideline — source for functional vision assessment components (contrast sensitivity, glare, illumination) and the ≈300–600 lux task-lighting range.
- Pelli, D.G., Robson, J.G., & Wilkins, A.J., "The Design of a New Letter Chart for Measuring Contrast Sensitivity," *Clinical Vision Sciences*, 1988 — origin of the Pelli-Robson chart referenced in the worked example.
- State DMV bioptic-driving statutes and consensus-panel reviews (e.g., Illinois, Indiana, Pennsylvania programs; national reviews in *PMC*/*Optometry and Vision Science* on bioptic driving) — source for the state-variance data in `references/playbook.md`. No direct practitioner sign-off yet on this role definition as a whole — flag via PR if you can confirm, correct, or add a citation.
