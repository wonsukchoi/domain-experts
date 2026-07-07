# Translator/Interpreter — Playbook

## MTPE (machine-translation post-editing) decision table

| Raw MT error density (per 1,000 words, domain content) | Recommended path | Typical throughput | Typical rate vs from-scratch |
|---|---|---|---|
| < 15 errors | Light PE (fix errors that mislead/embarrass only) | ~9,000-10,000 words/day | ~30% of from-scratch rate |
| 15-30 errors | Full PE (bring to human-parity quality) | ~6,000-7,000 words/day | ~50% of from-scratch rate |
| 30-50 errors, terminology-concentrated | Load client glossary/termbase into MT engine, re-sample before quoting | — | — |
| > 50 errors, or errors spread across grammar/mistranslation (not just terminology) | Treat MT as unusable draft; quote from-scratch | ~2,000-2,500 words/day | 100% (baseline rate) |

Always re-sample after loading a glossary — terminology-concentrated error density often drops sharply once domain terms are supplied; grammar/mistranslation-concentrated density usually does not improve much from a glossary alone (it reflects language-pair/engine limits, not missing vocabulary).

## Throughput & rate reference table (illustrative — calibrate per language pair)

| Work type | Throughput (words/day) | Rate (relative to from-scratch = 100%) |
|---|---|---|
| From-scratch translation, general | 2,000-2,500 | 100% |
| From-scratch translation, highly technical/legal | 1,200-1,800 | 110-130% |
| Full post-editing (MTPE) | 6,000-8,000 | 45-55% |
| Light post-editing (MTPE) | 9,000-12,000 | 25-35% |
| Consecutive interpretation | half the "words" throughput of simultaneous, same content | typically billed per half-day/full-day, not per word |
| Simultaneous interpretation | real-time (1:1 with speech) | typically billed per half-day/full-day, higher rate than consecutive per hour |

## Certified translation statement (filled template)

> **CERTIFICATE OF TRANSLATION ACCURACY**
>
> I, [Full Name], certify that I am fluent in the English and German languages, and that the attached document is a true and accurate translation of the document titled "[Source Document Title]," dated [Source Date], from German to English, to the best of my knowledge and ability.
>
> Translator: [Full Name]
> Credential: ATA-Certified Translator, German→English, Certification #[XXXXX]
> Date: [Date]
> Signature: _______________________
>
> [Notary block, if required by receiving institution — confirm requirement before delivery; not all certifying bodies require notarization on top of a translator's sworn statement.]

Before sending, confirm against the *receiving institution's own stated requirement* (USCIS, a specific court, a vital-records office) — the elements above cover the common baseline, but some institutions require additional notarization, a specific credential (court-certified vs ATA-certified), or a particular statement wording.

## Back-translation QA worksheet (filled example)

| Segment | Original source (EN) | Target translation (DE) | Back-translation (DE→EN, independent linguist) | Drift? |
|---|---|---|---|---|
| Warning 1 | "Do not operate without protective guard installed." | "Nicht ohne installierten Schutzschild betreiben." | "Do not operate without an installed protective shield." | No — meaning preserved |
| Warning 2 | "Disconnect power before servicing." | "Vor der Wartung den Strom trennen." | "Disconnect the power before maintenance." | No — meaning preserved |
| Dosage note | "Apply no more than twice daily." | "Nicht öfter als zweimal täglich anwenden." | "Do not apply more than twice a day." | No — meaning preserved |

A flagged drift on any safety, legal-obligation, or dosage segment routes back to the original translator for revision before delivery — it does not get silently corrected by the QA reviewer, since the discrepancy itself is diagnostic of where the first translator's reasoning went wrong.
