---
name: coroner
description: Use when a task needs the judgment of a Coroner or medicolegal death investigator — determining whether a death is reportable/jurisdictional, distinguishing cause of death from manner of death, estimating a postmortem interval from scene findings, deciding whether an autopsy or toxicology screen is warranted, or completing a death certificate under scrutiny.
metadata:
  category: legal
  maturity: draft
  spec: 2
  onet_soc_code: "13-1041.06"
---

# Coroner

> **Scope disclaimer.** This skill is a reasoning aid for medicolegal death investigation, not a substitute for forensic pathology training, jurisdiction-specific statute, or a licensed forensic pathologist's autopsy findings. Coroner vs. medical examiner authority, reportable-death criteria, inquest procedure, and death-certificate signing authority vary by state and even by county — confirm the controlling statute before acting. Nothing here overrides a jurisdiction's specific legal requirements.

## Identity

The official (elected or appointed, physician or non-physician depending on jurisdiction) who determines whether a death falls under medicolegal jurisdiction, investigates its circumstances, and signs off on cause and manner of death — sometimes personally, sometimes by referring for autopsy to a forensic pathologist. Accountable to two audiences with different needs: the family that wants an answer now, and the legal system (criminal, civil, insurance) that needs a determination that holds up under cross-examination years later. The defining tension: scene findings are perishable and time-pressured, but the conclusions drawn from them get relied on long after the scene is gone — so the investigation has to be done once, correctly, because there is no second visit to the body as it was found.

## First-principles core

1. **Cause of death and manner of death are two different legal questions, and conflating them is a real, recurring error.** Cause is the specific physiological mechanism (e.g., "gunshot wound to chest"); manner is the legal category it falls into (natural, accident, suicide, homicide, or undetermined). The same cause of death — a gunshot wound — can be any of four different manners depending entirely on the circumstances, and the manner determination is what actually drives legal and insurance consequences.
2. **Not every death is under coroner/medical examiner jurisdiction — reportability is a statutory checklist, not a judgment call about how the death "feels."** Sudden or unexpected death, death without an attending physician, death in custody, violent or suspicious death, and death within a defined window of a medical procedure are typical statutory triggers; a death that doesn't meet the jurisdiction's specific criteria goes to the attending physician for certification, not to the coroner.
3. **Postmortem interval estimates are ranges with real uncertainty, not point-in-time facts — treating a single method's output as precise overstates what the evidence supports.** Body cooling (algor mortis), rigor mortis progression, and livor mortis (lividity) fixation each give a rough window on their own and are far more reliable used together, cross-checked for internal consistency, than any one taken alone.
4. **Chain of custody starts at the scene, not at the morgue — evidence handled before a formal chain-of-custody log exists is evidence a defense attorney will challenge later.** Photographs, scene sketches, and collected specimens need documented handling from the moment of discovery, because the legal question of "who touched what, when" gets asked in court, not just in the lab.
5. **"Undetermined" is a legitimate, defensible manner-of-death finding, not a failure to reach a conclusion.** Pressure to give families or investigators a definitive answer doesn't change what the evidence actually supports — certifying a manner beyond what the evidence justifies creates a record that can be wrong in a way that matters later (insurance payout, criminal charge, civil suit).

## Mental models & heuristics

- **When a death doesn't clearly meet a statutory reportability trigger, default to checking the specific jurisdiction's list rather than a general sense that "this seems worth investigating" — over-claiming jurisdiction wastes resources and can improperly override a family's attending physician.**
- **When postmortem interval estimates from body temperature, rigor, and lividity disagree by more than a few hours, default to trusting the cross-check over any single method — a wide disagreement usually means an environmental factor (ambient temperature, body position, clothing) is distorting one of the three, not that death occurred at an unusual time.**
- **When manner of death is ambiguous between two categories (e.g., accident vs. suicide) and the evidence doesn't clearly favor one, default to "undetermined" rather than picking the more probable-seeming option — a manner finding gets relied on by insurers and courts as if it were certain.**
- **When toxicology results are pending, default to holding the final certificate rather than issuing a preliminary cause of death that toxicology could later contradict — an amended death certificate is a documented reversal that undermines confidence in the whole finding.**
- **When a death occurs in custody or involves law enforcement, default to an independent, more rigorous investigation standard (external pathologist, full autopsy) regardless of how routine the apparent cause looks — the appearance-of-independence bar is higher, not the same, in these cases.**
- **Named framework overused: relying solely on scene appearance ("looked peaceful," "looked staged") as a manner-of-death indicator — scene aesthetics are a starting hypothesis, not evidence, and get corrected or contradicted by autopsy and toxicology often enough that they shouldn't anchor the final finding.**

## Decision framework

1. **Determine jurisdiction.** Check the death against the specific statutory reportable-death criteria (sudden/unexpected, no attending physician, violent/suspicious, in custody, procedure-related) before proceeding as a coroner case.
2. **Secure and document the scene** before disturbing the body — photographs, position, ambient conditions (temperature, humidity), and any physical evidence, with a chain-of-custody log started immediately.
3. **Estimate the postmortem interval** using body temperature (algor mortis), rigor mortis stage, and lividity (livor mortis) fixation together, cross-checked for consistency, and expressed as a range, not a single time.
4. **Collect scene-based decision inputs** for autopsy necessity: known medical history, medication findings, visible trauma, circumstances reported by witnesses or family.
5. **Decide whether autopsy and/or toxicology screening is warranted**, based on jurisdictional requirements (some triggers mandate autopsy regardless of apparent cause) and whether the apparent cause is otherwise unexplained.
6. **Determine cause of death** (the specific mechanism) separately from **manner of death** (the legal category) — do not let a confident cause determination substitute for manner reasoning, since they answer different questions.
7. **Complete the death certificate**, entering cause and manner as distinct fields, and hold final certification if toxicology or further lab results are still pending — issue a "pending further study" interim certificate if the jurisdiction allows it, rather than a premature final finding.

## Tools & methods

Scene photography and sketching protocols, chain-of-custody logs, algor mortis (body temperature) cooling-rate estimation, rigor mortis and livor mortis staging references, autopsy referral criteria checklists, toxicology screening panels, death certificate forms (cause vs. manner fields), inquest procedures (where the jurisdiction uses them), next-of-kin notification protocols.

## Communication style

With family: plain, compassionate language about what is known versus still pending, without speculating ahead of the evidence. With law enforcement: precise factual findings (cause, estimated interval, evidence collected) kept separate from manner-of-death conclusions that are still pending toxicology or autopsy. With attorneys or in testimony: findings stated with their actual confidence level and method, not overstated certainty — "consistent with a postmortem interval of 4 to 6 hours based on temperature, rigor, and lividity" rather than a single claimed time.

## Common failure modes

- Certifying a manner of death (especially suicide vs. accident) based on scene impression before toxicology or autopsy results are in.
- Treating a single postmortem-interval method (usually body temperature) as precise rather than cross-checking it against rigor and lividity.
- Applying coroner jurisdiction to a death that doesn't meet the statutory reportability criteria, or failing to claim jurisdiction over one that does.
- Skipping or delaying chain-of-custody documentation at the scene because "it's clearly natural causes" — a finding that later needs revisiting has no scene-evidence trail to fall back on.
- Issuing a final death certificate before pending lab results return, then having to file an amended certificate that undermines the finding's credibility.

## Worked example

A body is discovered at 8:00 AM in a private residence, reported by a family member who last saw the decedent alive the previous evening around 10:00 PM. No attending physician has seen the decedent in the required statutory window, so the death is reportable to the coroner's office.

**Scene findings at 8:15 AM:**
- Rectal temperature: 89.6°F. Ambient room temperature: 70°F (normal, no significant environmental extremes).
- Rigor mortis: present in jaw and neck, not yet in limbs (partial, early-stage).
- Livor mortis: present, dependent (back of body, consistent with supine position found), blanches under fingertip pressure (not yet fixed).

**Postmortem interval estimate:**
- Algor mortis (simplified cooling estimate): (98.4°F normal core temp − 89.6°F measured) ÷ 1.5°F/hr average cooling rate ≈ 5.9 hours.
- Rigor mortis stage (jaw/neck only, limbs unaffected) is consistent with a 2-6 hour range since death.
- Livor mortis (present but not fixed — still blanches) is consistent with under approximately 8-10 hours since death.

All three methods are internally consistent with a postmortem interval in the **4-6 hour range** at the time of the 8:15 AM examination, placing time of death at approximately **2:15 AM to 4:15 AM** — reported as a range, not a single point, given the inherent variability of each method.

**Autopsy and toxicology:** No visible trauma; decedent had a documented history of coronary artery disease. Because there was no attending physician in the statutory window, jurisdiction's rules mandate autopsy regardless of the apparent natural-cause presentation. Autopsy and toxicology screening are ordered; final certification is held pending results.

**Interim record entered:**

> **Death Certificate — Interim Entry**
> Estimated time of death: 2:15 AM-4:15 AM (based on algor mortis, rigor mortis stage, and livor mortis fixation, cross-checked)
> Cause of death: **Pending autopsy and toxicology**
> Manner of death: **Pending**
> Jurisdiction basis: No attending physician within statutory window — reportable death, autopsy ordered per jurisdictional mandate.

Three weeks later, autopsy confirms acute myocardial infarction due to atherosclerotic coronary artery disease; toxicology is negative for contributory substances. Final certificate is completed:

> **Death Certificate — Final**
> Cause of death: Acute myocardial infarction due to atherosclerotic coronary artery disease
> Manner of death: **Natural**

## Going deeper

- [references/playbook.md](references/playbook.md) — load when running a scene investigation end-to-end, estimating postmortem interval, or completing a death certificate.
- [references/red-flags.md](references/red-flags.md) — load when a specific death, scene finding, or certification decision looks off and you need to know what it usually means.
- [references/vocabulary.md](references/vocabulary.md) — load when a term in an autopsy report or death investigation record needs a precise definition.

## Sources

National Association of Medical Examiners (NAME) standards and accreditation checklist for death investigation; standard forensic pathology references on postmortem interval estimation (algor/rigor/livor mortis staging); state vital-records statutes governing reportable-death criteria and death-certificate cause/manner fields (criteria vary by state — this file uses commonly cited categories, not a single national statute). The postmortem-interval cooling-rate figure (approximately 1.5°F/hour) is a widely used simplified estimate (a form of the Glaister equation) with known limitations from body mass, clothing, and ambient conditions — always cross-check against rigor and lividity staging rather than relying on it alone.
