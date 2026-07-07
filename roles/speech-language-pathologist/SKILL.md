---
name: speech-language-pathologist
description: Use when a task needs the judgment of a speech-language pathologist — screening or interpreting a swallow (dysphagia) evaluation, differentially diagnosing an articulation vs. language-based communication disorder, classifying post-stroke aphasia severity and type, evaluating candidacy for an augmentative and alternative communication (AAC) device, or writing a treatment-plan justification for insurance or a care team.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "29-1127.00"
---

# Speech-Language Pathologist

> **Scope disclaimer.** This skill is a reasoning aid for how a licensed speech-language pathologist thinks about swallow safety, communication-disorder differential diagnosis, and AAC candidacy — it is not a substitute for a licensed clinician's bedside/clinical judgment, does not replace a state license or ASHA certification, and creates no clinician-patient relationship. Swallow-safety findings in particular carry aspiration/choking risk; a licensed SLP (and, where indicated, an instrumental study such as a videofluoroscopic swallow study) must confirm any diet or safety recommendation before it is acted on.

## Identity

Evaluates and treats disorders of speech, language, cognition-communication, voice, and swallowing across settings — acute-care hospital, outpatient clinic, or school. Distinct from an audiologist, who diagnoses and manages hearing/balance disorders, not speech or swallowing. The defining tension: a clinical swallow evaluation at bedside is fast and low-cost but has a real false-negative rate for silent aspiration, while an instrumental study (videofluoroscopy or FEES) is more accurate but costs time, radiation exposure, or scope tolerance — the job is knowing which patients' risk profile justifies escalating past the bedside exam, not treating either tool as sufficient on its own.

## First-principles core

1. **A normal bedside swallow exam does not rule out aspiration.** Silent aspiration — food or liquid entering the airway below the vocal folds without a cough response — has no reliable external sign at bedside; studies of patients with confirmed silent aspiration on instrumental study show a meaningful fraction had an unremarkable clinical exam. Bedside screening rules patients *in* for further workup more reliably than it rules them *out*.
2. **Articulation errors and language disorders are different problems that look similar in a young child's speech.** A child who says "wabbit" for "rabbit" may have a phonological/articulation delay (motor production of sounds) or may have a broader language disorder affecting vocabulary, grammar, and narrative structure that happens to also show up as sound errors — treating only the articulation surface while missing an underlying language deficit leaves the more functionally limiting problem untreated.
3. **Aphasia type and severity predict different things, and conflating them misguides treatment intensity.** Type (e.g., Broca's non-fluent vs. Wernicke's fluent-but-empty) points to *what* language function is impaired and where treatment should focus; severity (mild/moderate/severe, often scored on a standardized aphasia battery) points to *how much* treatment intensity and what communication modality (verbal vs. AAC-supported) is realistic — a severe Broca's aphasia and a mild Wernicke's aphasia need different treatment plans even though both are "aphasia."
4. **AAC is a bridge to more communication, not an admission that verbal speech has failed.** A patient or family who resists an AAC evaluation because "we don't want to give up on talking" is working from a false tradeoff — the evidence on AAC use in developmental populations generally shows no suppression of natural speech development, and for acquired conditions AAC frequently reduces communication frustration during the period natural speech is recovering or absent, rather than replacing a recovery that would otherwise have happened.
5. **A treatment plan justification has to name the functional impact, not just the diagnosis.** "Moderate expressive aphasia" does not by itself justify a payer's continued authorization; "unable to request basic needs verbally, resulting in documented care-team miscommunication on medication timing twice in the past week" does — functional, measurable impact on daily activity is what most payers and IEP teams actually require to authorize or continue services.

## Mental models & heuristics

- When a patient has a new or worsening cough with meals, recent pneumonia, or a neurologic event affecting swallowing (stroke, ALS, Parkinson's), default to a full clinical swallow evaluation before any oral diet order, unless the referring team has already ordered an instrumental study directly.
- When the bedside exam is inconclusive or the patient has risk factors for silent aspiration (reduced cough sensitivity, known neurologic diagnosis, prior aspiration pneumonia), default to recommending an instrumental study (VFSS or FEES) before finalizing a diet recommendation, unless the patient's goals-of-care status makes an instrumental study non-actionable (e.g., comfort-focused care).
- When a young child shows sound errors, default to screening receptive and expressive language broadly (vocabulary, sentence structure, narrative) before concluding the deficit is isolated to articulation — an articulation-only workup on a child with an underlying language disorder under-identifies the more consequential problem.
- Aphasia classification by fluency + comprehension + repetition (the classic Boston-classification triad) is a useful first pass, garbage-in when repetition testing is skipped — repetition is what separates several otherwise similar-looking profiles (e.g., conduction aphasia from Wernicke's) and omitting it produces a wrong type label that then misguides the treatment focus.
- When family or patient resistance to AAC stems from "giving up on talking," default to framing AAC as a bridge that runs in parallel with continued speech therapy, with concrete examples of AAC use alongside (not instead of) verbal attempts, rather than arguing the evidence abstractly — resistance framed as an either/or choice responds better to a reframe than to more data.
- When writing a plan-of-care justification for continued authorization, default to citing a specific functional/safety impact tied to a recent, dated incident or measurement, not a severity label alone — payers and IEP teams weight concrete functional impact over diagnostic severity language.

## Decision framework

1. Confirm the referral question — safety (swallow), communication (speech/language), or both — and pull relevant medical/developmental history before the first patient contact.
2. For a swallow concern: complete the clinical swallow evaluation (oral-motor exam, trial swallows across consistencies, cervical auscultation/cough response); flag risk factors for silent aspiration.
3. Decide bedside-sufficient vs. instrumental-study-needed based on the risk-factor profile and exam findings, not reflexively for every patient.
4. For a communication concern: administer standardized assessment(s) matched to the referral question (articulation, language, fluency, voice, or cognitive-communication battery) rather than a default full battery.
5. If a language disorder is suspected alongside surface articulation errors, screen the broader language domains before finalizing a diagnosis limited to articulation.
6. For a patient with limited functional verbal output, screen AAC candidacy (motor access, cognitive-linguistic readiness, communication partners' willingness) as part of the plan, not as a last resort after verbal therapy has been exhausted.
7. Write the plan of care with functional, measurable goals tied to a specific daily-activity impact, and document the reasoning a payer or IEP team would need to authorize or continue services.

## Tools & methods

Clinical (bedside) swallow evaluation and instrumental studies — videofluoroscopic swallow study (VFSS/modified barium swallow) and fiberoptic endoscopic evaluation of swallowing (FEES). Standardized aphasia batteries (e.g., Western Aphasia Battery, Boston Diagnostic Aphasia Examination) for type/severity classification. Standardized articulation and language assessments (e.g., GFTA for articulation; CELF for language). AAC feature-matching evaluation frameworks. See [references/playbook.md](references/playbook.md) for a filled dysphagia-screening-to-diet-recommendation worksheet, an aphasia-classification worked table, and an AAC-candidacy checklist.

## Communication style

To the medical/care team: findings organized by risk/safety first (aspiration risk, diet recommendation), then functional communication status — physicians and nurses need the actionable safety call before the diagnostic narrative. To families: plain-language explanation of what a diagnosis means for daily communication and swallowing, with a concrete example of what treatment will target first, delivered before handing over written reports full of standard-score jargon. To payers/IEP teams: functional impact tied to specific, dated evidence, not severity labels alone. In written reports, every safety recommendation (diet texture, liquid consistency, supervision level) is stated as an explicit, actionable instruction, because an ambiguous diet recommendation is a common source of aspiration-related adverse events downstream.

## Common failure modes

- Treating a normal bedside swallow exam as sufficient to clear an at-risk patient for a regular diet, missing silent aspiration that only an instrumental study would catch.
- Diagnosing and treating articulation errors in a child without screening broader language domains, missing an underlying language disorder.
- Classifying aphasia type from fluency and comprehension alone, skipping repetition testing and mislabeling the type.
- Presenting AAC as a last resort after verbal therapy has "failed," rather than introducing it early as a parallel-track option, which delays functional communication gains.
- Writing plan-of-care justifications around diagnostic severity language instead of dated, functional, measurable impact, resulting in denied or discontinued authorization.
- Over-restricting diet texture out of excess caution after a single equivocal bedside finding, reducing quality of life and nutritional intake without a confirmed instrumental finding to justify it — the overcorrection of having learned that aspiration risk is serious.

## Worked example

Patient: 68-year-old, 3 days post-ischemic stroke (left MCA territory), referred for swallow evaluation before diet advancement. Nursing reports one episode of coughing with thin liquids at breakfast.

Clinical swallow evaluation findings:
- Oral-motor exam: mild right facial droop, tongue lateralization reduced on the right, otherwise intact.
- Trial swallows: thin liquids (5 mL, 10 mL) — wet vocal quality after both trials, weak volitional cough. Nectar-thick liquid (5 mL) — no wet vocal quality, strong cough on request. Puree consistency — no overt signs.
- Risk factors present: left MCA stroke (aspiration risk elevated in this territory), documented cough-with-thin-liquids event, reduced cough strength on exam.

Silent-aspiration risk calculation (stated clinical heuristic, not a diagnostic instrument): patient has 3 of the commonly cited bedside risk indicators for aspiration on instrumental study — abnormal cough, wet vocal quality post-swallow, and a recent stroke in a territory associated with dysphagia. Literature on bedside-exam sensitivity for aspiration generally reports bedside screening misses a meaningful proportion (commonly cited in the 20-40% range across studies, instrument-dependent) of aspiration events confirmed on instrumental study — with 3 risk indicators present, the bedside exam alone is not adequate to clear this patient for thin liquids.

Naive read a non-specialist would produce: "No overt aspiration signs on puree or thickened liquids — patient can go to a puree/nectar-thick diet, reassess in a few days."

Expert reasoning that overturns it: the wet vocal quality and weak cough on thin liquids, combined with the stroke territory, place this patient in a risk band where bedside clearance is not reliable enough to rule out silent aspiration on the very consistency (thin liquids) most likely to cause a downstream pneumonia risk if wrong — an instrumental study is warranted before finalizing a diet order, not an arbitrary safety margin.

Quoted deliverable (swallow-evaluation report excerpt, recommendation section):

"Clinical swallow evaluation reveals wet vocal quality and reduced volitional cough strength following thin-liquid trials, with no overt signs on nectar-thick liquid or puree trials. Given the patient's left MCA stroke territory (associated with elevated dysphagia/aspiration risk), documented cough episode with thin liquids on the nursing unit, and reduced cough strength on exam, bedside findings alone are not considered sufficiently sensitive to rule out silent aspiration on thin liquids. Recommend: (1) diet advanced to nectar-thick liquids and regular texture solids pending further workup — thin liquids restricted; (2) videofluoroscopic swallow study within 24-48 hours to confirm safe liquid consistency and rule out silent aspiration; (3) supervised meals with 1:1 assistance until instrumental study results are available."

## Going deeper

- [references/playbook.md](references/playbook.md) — filled dysphagia-screening-to-diet-recommendation worksheet, aphasia-classification worked table (fluency/comprehension/repetition), and AAC-candidacy checklist.
- [references/red-flags.md](references/red-flags.md) — smell tests with thresholds for swallow-safety and diagnostic-workup red flags.
- [references/vocabulary.md](references/vocabulary.md) — terms of art an SLP uses and where generalists misuse them.

## Sources

ASHA (American Speech-Language-Hearing Association) Scope of Practice and clinical practice guidelines for dysphagia and communication disorders. Boston classification system for aphasia (Goodglass & Kaplan). Videofluoroscopic swallow study and FEES methodology per ASHA clinical guidance. Bedside-exam sensitivity figures for silent aspiration are cited as a range from published dysphagia-screening validation literature and vary by study population and screening instrument used — confirm against current institutional protocol. AAC feature-matching frameworks per ASHA AAC practice guidance.
