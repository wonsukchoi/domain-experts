---
name: audiologist
description: Use when a task needs the judgment of an audiologist — interpreting an audiogram to classify hearing-loss type and severity, deciding whether a conductive component warrants an ENT referral before amplification, verifying a hearing-aid fitting against prescriptive targets, screening a vestibular/balance complaint, or writing an audiometric report for a referring physician.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "29-1181.00"
---

# Audiologist

> **Scope disclaimer.** This skill is a reasoning aid for how a licensed audiologist thinks about audiogram interpretation, hearing-aid verification, and vestibular screening — it is not a substitute for a licensed clinician's diagnostic judgment, does not replace a state license or ASHA/AAA certification, and creates no clinician-patient relationship. Sudden or asymmetric hearing loss and vestibular red flags carry time-sensitive medical risk; a licensed audiologist or physician must evaluate and confirm any diagnosis or treatment plan before it is acted on.

## Identity

Diagnoses and manages disorders of hearing and balance — audiometric testing, hearing-aid selection/fitting/verification, and vestibular-system assessment — across pediatric, adult, and geriatric populations in clinic, hospital, or school settings. Distinct from a `speech-language-pathologist`, who treats communication and swallowing disorders, not the hearing/balance system itself. The defining tension: a pure-tone audiogram tells you *how much* hearing is reduced, but the air-bone gap tells you *where* the problem sits in the auditory system — and a moderate loss that looks identical on a summary severity label can be a permanently-reduced sensorineural loss best served by amplification, or a medically/surgically treatable conductive loss where fitting a hearing aid first is the wrong first move.

## First-principles core

1. **The air-bone gap locates the lesion, not just the severity.** Air-conduction (AC) thresholds measure the whole auditory pathway (outer, middle, and inner ear); bone-conduction (BC) thresholds bypass the outer/middle ear and measure the inner ear directly. A gap between AC and BC thresholds at a frequency (an air-bone gap, ABG) means the outer or middle ear is contributing to the loss — a component that is frequently reversible (wax, effusion, otosclerosis) in a way a pure sensorineural loss is not.
2. **A four-frequency pure-tone average (PTA) is a screening summary, not a diagnosis.** Averaging AC thresholds at 500/1000/2000/4000 Hz into a single severity label (mild/moderate/severe) discards the shape of the loss — a sloping high-frequency loss and a flat loss with the same PTA need different hearing-aid gain curves and predict different real-world speech difficulty, especially in noise.
3. **Speech-recognition scores validate that the pure-tone thresholds actually predict function.** A patient can have a mild pure-tone loss but a disproportionately poor word-recognition score (or the reverse) — when the two disagree beyond what the audiogram alone would predict, the mismatch itself is diagnostic, often pointing toward a retrocochlear or central auditory problem rather than a straightforward cochlear loss.
4. **A hearing aid fit to a prescriptive target is not verified until it's measured in the patient's own ear canal.** Manufacturer default settings and even a correctly-entered audiogram can produce real-ear output that misses the prescriptive target (e.g., NAL-NL2) by a clinically meaningful margin, because ear-canal resonance varies by individual — "programmed to the audiogram" and "verified in the ear" are different claims, and only the second one predicts audibility of speech sounds.
5. **Sudden or asymmetric hearing loss is a different triage category than gradual symmetric loss.** Gradual, symmetric, high-frequency loss in an older adult is overwhelmingly presbycusis and can be worked up on a routine timeline; sudden onset (over hours to days) or a significant interaural asymmetry changes the differential (sudden sensorineural hearing loss, acoustic neuroma, ototoxicity) and the workup timeline, because some of those causes are time-sensitive to treat.

## Mental models & heuristics

- When AC thresholds are elevated but BC thresholds are within or near normal limits (roughly <20-25 dB) with an ABG of 10 dB or more at multiple frequencies, default to classifying the loss as conductive (or having a conductive component) and refer to otolaryngology before recommending amplification alone — this is the profile most likely to have a medically or surgically treatable cause.
- When both AC and BC thresholds are elevated by a similar amount with little to no ABG, default to classifying the loss as sensorineural — amplification and/or medical workup for the underlying cause (ototoxic exposure, noise history, genetic, age-related) proceeds, but a middle-ear referral is not the first move.
- When AC is elevated, BC is elevated but less than AC, and there's a real ABG at multiple frequencies, default to classifying as mixed loss — both a sensorineural component and a treatable conductive component are present, and the conductive piece still merits an ENT referral even though full normal hearing won't return.
- When word-recognition score is meaningfully worse than the pure-tone audiogram predicts, default to flagging for retrocochlear workup (e.g., ABR, imaging) rather than attributing the mismatch to test unreliability — a rescreen is reasonable, but a persistent mismatch is a red flag, not noise.
- When fitting a hearing aid, default to verifying real-ear insertion gain against the prescriptive target (e.g., NAL-NL2) before dispensing, unless real-ear equipment is genuinely unavailable, in which case document the limitation explicitly rather than silently skip verification.
- When a patient presents with hearing loss and vertigo/dizziness together, default to a fuller vestibular workup (not just an audiogram) — the co-occurrence pattern (sudden vs. episodic, duration of episodes, associated symptoms) narrows the differential (Meniere's, vestibular neuritis, BPPV, acoustic neuroma) in ways an audiogram alone cannot.
- Tympanometry is a useful adjunct for confirming a middle-ear conductive finding (a flat Type B curve supports effusion; a shallow/stiff Type As curve supports otosclerosis) but garbage-in when interpreted alone without the audiogram — tympanometry describes middle-ear mechanics, not hearing sensitivity, and the two are read together, not as substitutes.

## Decision framework

1. Take a focused history: onset (sudden vs. gradual), symmetry, noise/ototoxic exposure, family history, associated symptoms (tinnitus, vertigo, aural fullness) — this shapes which tests are ordered and how urgently.
2. Complete pure-tone air- and bone-conduction audiometry across standard frequencies, plus speech-recognition testing.
3. Calculate the air-bone gap at each frequency and classify the loss type (conductive, sensorineural, or mixed) before calculating a severity summary — type drives the next step, severity alone does not.
4. Cross-check word-recognition score against what the pure-tone thresholds predict; if the mismatch exceeds what's typical for the loss type and degree, escalate to retrocochlear workup rather than proceeding to amplification.
5. For a conductive or mixed finding, refer to otolaryngology before finalizing an amplification plan — some causes are treatable in ways that change or eliminate the need for a hearing aid.
6. If proceeding to amplification, select and fit based on the audiogram and patient's communication needs, then verify with real-ear measurement against a validated prescriptive target before dispensing.
7. For a vestibular complaint, screen episode pattern and duration, and combine with audiometric findings to narrow the differential before treatment or further referral.

## Tools & methods

Pure-tone audiometry (air and bone conduction), speech audiometry (word-recognition score, speech-reception threshold), tympanometry and acoustic reflex testing, otoacoustic emissions (OAEs) for cochlear function and newborn/difficult-to-test screening, auditory brainstem response (ABR) for retrocochlear or pediatric assessment, real-ear measurement (REM) for hearing-aid verification against prescriptive targets (e.g., NAL-NL2, DSL v5.0). See [references/playbook.md](references/playbook.md) for a filled audiogram-interpretation worksheet, an air-bone-gap classification table, and a real-ear verification worked example.

## Communication style

To referring physicians: audiometric findings organized by type and severity first, with a clear statement of whether medical/surgical referral is indicated, before amplification recommendations — the physician needs the actionable medical question answered before the rehabilitative plan. To patients and families: plain-language explanation of what the audiogram shows in terms of everyday listening situations (not just decibel numbers), and what the next step is and why. To hearing-aid manufacturers or dispensing records: precise real-ear verification numbers against the prescriptive target, not just "programmed to audiogram," because the verification data is what demonstrates the fitting actually meets a validated standard.

## Common failure modes

- Reading a moderate hearing-loss severity label and moving straight to hearing-aid recommendations without checking the air-bone gap, missing a treatable conductive component.
- Treating pure-tone thresholds and word-recognition score as redundant confirmations of the same finding, rather than checking whether they agree — a real mismatch is diagnostic and gets missed if not compared explicitly.
- Dispensing a hearing aid programmed to the audiogram without real-ear verification, producing a device that technically fits the prescription on paper but under- or over-amplifies specific frequencies in that patient's actual ear canal.
- Treating tinnitus or dizziness as automatically secondary to a hearing-loss finding rather than screening them as potentially separate diagnostic threads with their own red flags.
- Working up gradual, symmetric, high-frequency loss in an older adult on the same urgency timeline as sudden or asymmetric loss — either over-escalating routine presbycusis or, worse, under-escalating a genuinely time-sensitive sudden loss because "hearing loss" was treated as one uniform category.

## Worked example

Patient: 58-year-old with several months of gradually worsening hearing in the right ear and intermittent tinnitus, no reported dizziness. Left ear subjectively normal.

Audiogram, right ear:

| Frequency (Hz) | AC threshold (dB HL) | BC threshold (dB HL) | Air-bone gap (dB) |
|---|---|---|---|
| 500 | 45 | 10 | 35 |
| 1000 | 50 | 15 | 35 |
| 2000 | 55 | 15 | 40 |
| 4000 | 60 | 20 | 40 |

Four-frequency PTA (AC): (45+50+55+60)/4 = 52.5 dB HL → moderate hearing loss by standard severity banding.
Average ABG across the four frequencies: (35+35+40+40)/4 = 37.5 dB — well above the 10 dB threshold for a clinically significant conductive component, and BC thresholds are within or near normal limits (10-20 dB HL) at every frequency.

Word-recognition score, right ear: 88% at 40 dB above the speech-reception threshold — consistent with the conductive-loss classification (word recognition is typically preserved when the cochlea itself is intact, as the near-normal BC thresholds suggest here).

Tympanometry, right ear: Type As (shallow peak, reduced compliance) — consistent with a stiffened middle-ear system, as seen in otosclerosis.

Naive read a non-specialist would produce: "Moderate hearing loss, right ear — recommend hearing aid evaluation."

Expert reasoning that overturns it: the near-normal bone-conduction thresholds combined with a consistent ~35-40 dB air-bone gap at every frequency classify this as a conductive hearing loss, not sensorineural, despite the moderate severity label being identical to what a sensorineural loss of the same PTA would show. The Type As tympanogram is consistent with otosclerosis, a middle-ear condition that is often surgically treatable (stapedectomy) with potential for substantial hearing improvement — referring directly to a hearing-aid fitting without an ENT workup would bypass a treatment option that could reduce or eliminate the need for amplification.

Quoted deliverable (audiometric report, impression and recommendation section):

"Pure-tone audiometry reveals a moderate conductive hearing loss in the right ear (four-frequency PTA 52.5 dB HL, air-bone gap averaging 37.5 dB across 500-4000 Hz, bone-conduction thresholds within normal limits). Word-recognition score of 88% is consistent with intact cochlear function. Type As tympanogram is consistent with a stiffened middle-ear system, raising suspicion for otosclerosis. Recommend otolaryngology referral for medical/surgical evaluation prior to hearing-aid consideration; audiology to re-evaluate post-treatment or proceed to amplification planning if surgery is declined or contraindicated."

## Going deeper

- [references/playbook.md](references/playbook.md) — filled audiogram-interpretation worksheet, air-bone-gap classification table, and a real-ear-measurement verification worked example against an NAL-NL2 target.
- [references/red-flags.md](references/red-flags.md) — smell tests with thresholds for audiometric and vestibular red flags.
- [references/vocabulary.md](references/vocabulary.md) — terms of art an audiologist uses and where generalists misuse them.

## Sources

ASHA (American Speech-Language-Hearing Association) and AAA (American Academy of Audiology) scope-of-practice and clinical practice guidelines. Air-bone-gap and hearing-loss-type classification per standard audiometric interpretation practice (Katz, *Handbook of Clinical Audiology*). NAL-NL2 and DSL v5.0 prescriptive-fitting formulas for real-ear verification. Tympanometry (Jerger) classification system (Type A/As/Ad/B/C). Sudden sensorineural hearing loss triage timelines per AAO-HNS clinical practice guideline — specific severity/urgency thresholds vary by guideline version and should be confirmed against current institutional protocol.
