# Radiation Therapist — Vocabulary

### PTV (Planning Target Volume)
The volume that adds a calculated margin around the CTV to account for setup uncertainty and internal organ motion, defining the actual treated volume the beam is aimed at.
**In use:** "The PTV margin here is 9mm because that's what our own setup-verification data says our systematic and random error actually is for this technique."
**Common misuse:** Treating the PTV as a generic safety buffer for "just in case," rather than a specific number derived from measured departmental uncertainty — a technique with tighter daily imaging and immobilization earns a smaller, not arbitrary, margin.

### CTV (Clinical Target Volume)
The GTV (visible/palpable tumor) plus a margin for suspected microscopic disease extension, defined by the physician based on tumor biology, not by imaging or setup uncertainty.
**In use:** "The CTV includes a 1cm margin around the visible tumor for microscopic spread, before we even add the setup-uncertainty margin to get to PTV."
**Common misuse:** Conflating CTV margin (disease-biology judgment) with PTV margin (setup/motion uncertainty) — they answer different questions and are set by different people using different data.

### Action level
A pre-defined threshold (e.g., a shift magnitude, or a machine-QA tolerance-table value) that separates "correct and proceed" from "hold and escalate."
**In use:** "That shift is under our 5mm action level, so we correct and treat — no need to call the physicist for this one."
**Common misuse:** Treating the action level as the only signal that matters, ignoring a sub-threshold trend across several fractions that is itself diagnostic of anatomic change.

### Medical event (NRC, 10 CFR 35.3045)
A specific regulatory category: a treatment delivered to the wrong patient or wrong site, or with a total dose differing from the prescribed dose by 20% or more, triggering a fixed 24-hour notification requirement.
**In use:** "That dose discrepancy is under 20% of the prescription, so it's a QA incident-review item, not a reportable medical event."
**Common misuse:** Calling any delivery error a "medical event" informally — the term has a specific regulatory threshold and reporting clock, and using it loosely can trigger or skip processes that don't actually apply.

### BED (Biologically Effective Dose)
A calculated value (BED = nd[1 + d/(α/β)]) that allows comparison of different fractionation schemes on a common biological scale, accounting for the fact that tissues respond differently to fraction size.
**In use:** "Before assuming the hypofractionated regimen is 'less dose,' compare the BED — the biological effect on the tissue that matters can be very similar despite a lower total physical dose."
**Common misuse:** Comparing two regimens by total physical Gray alone ("40Gy vs 50Gy, so 40 is less treatment") without accounting for fraction size and the relevant α/β ratio, which is what actually determines biological equivalence.

### IGRT (Image-Guided Radiation Therapy)
The practice of acquiring verification imaging (kV, MV portal, or CBCT) immediately before treatment to confirm and correct patient/target position relative to the plan.
**In use:** "This is a daily-IGRT prostate protocol — we get a CBCT every fraction, not just weekly portals."
**Common misuse:** Assuming IGRT alone guarantees accuracy — the imaging only helps if the resulting shift is interpreted against the correct action level and trend, not just acquired and corrected mechanically every time.

### SGRT (Surface-Guided Radiation Therapy)
Continuous optical tracking of the patient's external skin surface, used for initial setup, breath-hold monitoring, and intrafraction motion detection.
**In use:** "SGRT confirmed she held her breath consistently at the same surface position for all three DIBH fractions today."
**Common misuse:** Treating SGRT as a substitute for X-ray/CBCT verification of internal target position — skin surface and internal anatomy (bladder filling, tumor position) can decouple even when the surface tracking looks perfectly stable.

### DIBH (Deep Inspiration Breath Hold)
A respiratory-gating technique in which the patient holds a full inspiration during beam-on, most commonly used in left-breast treatment to move the heart away from the treatment field.
**In use:** "Her DIBH level was verified within 2mm of the reference on the pre-treatment surface scan before we started the beam."
**Common misuse:** Treating DIBH as simply "ask the patient to hold their breath" rather than a monitored, reproducibility-verified technique requiring a surrogate signal check before every beam-on.

### On-treatment visit (OTV)
A scheduled clinical checkpoint (commonly weekly) at which the physician or advanced practice provider examines the patient, grades toxicity, and reviews imaging/dose progress.
**In use:** "Flagging this for the OTV isn't enough — the symptom is outside the expected timeline, so it goes to the physician today, not at Thursday's scheduled visit."
**Common misuse:** Treating the OTV as the only checkpoint for clinical findings, deferring an acute or atypical symptom to the next scheduled visit instead of escalating same-day.

### CTCAE grade
The Common Terminology Criteria for Adverse Events scale (v5.0 currently), which defines specific, reproducible criteria for grading toxicity severity (e.g., radiation dermatitis grades 1–4) rather than free-text description.
**In use:** "That's a grade 2 dermatitis — moist desquamation confined to the skin folds — not grade 3 yet, since it hasn't spread beyond the folds."
**Common misuse:** Eyeballing severity with adjectives ("looks pretty red") instead of applying the specific distinguishing criteria between adjacent grades, which changes whether same-day escalation is required.

### Record-and-verify (R&V) system
The software layer (e.g., Aria, Mosaiq) that locks treatment-machine parameters to the physician-approved plan and blocks delivery if a parameter doesn't match.
**In use:** "The boost field won't deliver until dosimetry pushes the approved plan into the R&V system — that's the hard stop, not just a scheduling tool."
**Common misuse:** Treating the R&V system as scheduling software — it is the primary interlock preventing a wrong-parameter or wrong-plan delivery, and a plan verbally approved but not yet active in R&V is not yet safe to treat.

### Overall treatment time
The total calendar span (not just fraction count) over which a full course is delivered, which for some disease sites has its own biological significance independent of whether every individual fraction was delivered on-tolerance.
**In use:** "One missed fraction is fine dosimetrically, but if it extends overall treatment time past what the prescription assumed, that needs a physician-approved makeup plan, not just a shrug."
**Common misuse:** Assuming that as long as all prescribed fractions eventually get delivered, timing doesn't matter — for time-sensitive disease sites, a stretched-out overall treatment time can reduce biological effectiveness even with the full dose eventually delivered.

### Bolus (radiation therapy)
A tissue-equivalent material placed directly on the skin to shift the dose buildup region closer to the surface, used when the physician wants full dose at or near the skin rather than the natural skin-sparing effect of megavoltage beams.
**In use:** "Bolus is ordered for the scar this week only — don't apply it on the days the order doesn't specify or the skin dose will be higher than intended."
**Common misuse:** Treating bolus as an optional comfort or coverage measure applied at the therapist's discretion rather than a physician-ordered, fraction-specific parameter that changes the actual delivered skin dose.
