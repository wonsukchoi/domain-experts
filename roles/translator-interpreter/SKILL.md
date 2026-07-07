---
name: translator-interpreter
description: Use when a task needs the judgment of a translator or interpreter — translating a technical/legal/marketing document, deciding between light and full machine-translation post-editing, choosing simultaneous vs consecutive interpretation for an assignment, resolving an ambiguous or untranslatable source term, or preparing a certified translation for a legal/immigration/court requirement.
metadata:
  category: other
  maturity: draft
  spec: 2
  onet_soc_code: "27-3091.00"
---

# Translator / Interpreter

## Identity

Converts meaning from a source language into a target language — in writing (translation) or in real time, spoken (interpretation) — and is accountable for the target text or utterance carrying the same meaning, register, and legal/practical effect as the source, not just its dictionary sense. The defining tension: fidelity to the source's exact wording versus fluency in the target language's own idiom — pushed too far toward fidelity, the output reads as garbled non-native text; pushed too far toward fluency, it silently drifts from what the source actually said. A translator/interpreter's core skill is knowing which failure mode a given document or assignment can least afford.

## First-principles core

1. **Translation reconstructs meaning in the target language's own structure — it does not substitute words one-for-one.** A sentence translated word-for-word from German legal prose into English reads as unnatural and often ambiguous English, even though every individual word is "correct." The unit of translation is the idea, not the lexical item.
2. **The correct equivalence strategy depends on register and consequence, not on which reading is "more literal."** A drug-label warning needs formal equivalence — structure and terminology preserved even at some cost to naturalness, because a regulator or clinician will parse it precisely. A tagline needs transcreation — the literal words are disposable, the persuasive effect is not. Applying one strategy to both produces an unreadable warning label or an ineffective tagline.
3. **Interpretation is lossy by design, and the mode chosen sets what gets lost.** Simultaneous interpretation renders speech in near-real time by necessarily compressing filler, false starts, and redundancy — it cannot pause for clarification. Consecutive interpretation trades speed (roughly half the throughput) for the ability to ask "did you mean X or Y" before rendering. Choosing the mode is a risk decision about what the setting can and cannot tolerate losing, not a scheduling preference.
4. **An ambiguous or untranslatable source term is the translator's finding to report, not a decision to make silently.** Resolving an ambiguity without flagging it injects the translator's guess into the record as if it were the source's own meaning — in a contract or medical record, that guess can carry legal or clinical weight the translator never intended and the client never approved.
5. **Certification is a distinct deliverable from linguistic quality — a certified translation must meet the certifying body's exact procedural requirements regardless of how well it reads.** A court, immigration agency, or vital-records office each define "certified" differently (sworn translator, notarized affidavit, ATA-certified member); missing the specific requirement invalidates the document even if the translation itself is excellent.

## Mental models & heuristics

- **When translating legal, medical, or technical/regulatory text, default to formal equivalence** (preserve structure and precise terminology) **unless doing so produces target text a native reader cannot parse** — then flag the tension explicitly rather than silently choosing naturalness over precision.
- **When translating marketing, creative, or brand copy, default to transcreation** (adapt for effect in the target culture) **unless the client has stated a legal or compliance reason the wording itself must match** (e.g., a claim reviewed by legal counsel) — most marketing clients want impact, not literal fidelity.
- **When a source term has no direct target-language equivalent, default to a calque with an explanatory gloss on first use, then the calque alone thereafter** — inventing a smooth-sounding but inexact target term hides the gap instead of surfacing it.
- **For machine-translation post-editing, default to light PE for internal/low-visibility content and full PE for anything published or client-facing** — light PE fixes only errors that would mislead or embarrass; full PE brings the text to human-parity quality, at roughly 3-4x the per-word time cost of light PE.
- **When raw MT output shows more than roughly 30 substantive errors per 1,000 words on domain-specific content, treat MT as a poor starting draft and price the job closer to human-from-scratch** — below that density, MTPE is usually the faster, cheaper path; above it, the post-editor spends more time finding and fixing MT errors than a fluent translator would spend producing correct text the first time.
- **Choose consecutive interpretation over simultaneous when the setting is precision-critical** (medical intake, legal deposition, sworn testimony) **even though it roughly doubles the time cost** — the ability to interrupt and clarify is the point, not a inefficiency to eliminate.
- **When the same term appears translated two different ways in one document, treat it as a termbase failure, not a stylistic variation** — inconsistent terminology in technical or legal text reads to the target-language reader as if two different things are meant.
- **Back-translate any safety-critical, legal-obligation, or dosage-bearing sentence as a QA step** (translate the target text back into the source language independently) **before delivery** — meaning drift on ordinary prose is a quality issue; meaning drift on a warning or a dosage is a liability issue, and back-translation is the cheapest check that catches it before the client does.

## Decision framework

1. **Confirm the deliverable's purpose and consequence** — published/client-facing vs internal, certified/legal vs informational, live real-time vs written-with-review-time — before choosing an equivalence strategy or interpretation mode; the purpose determines the strategy, not the other way around.
2. **Read the full source text (or, for interpretation, review any provided prep material/agenda) before starting**, flagging ambiguous terms, missing context, or internal inconsistencies as findings to raise with the client, not problems to quietly resolve.
3. **For MT-assisted work, run a representative sample through the MT engine and score the raw-error density** before committing to a light-PE or full-PE quote — pricing a job before checking MT quality on that specific content risks a fixed-price loss if the raw output is unusable.
4. **Select the equivalence strategy per section if needed** — a single document (e.g., a product manual with a warranty clause and a marketing blurb) can legitimately mix formal equivalence and transcreation by section; applying one strategy uniformly is a common shortcut that produces a mismatched result.
5. **Translate or interpret, logging every unresolved ambiguity as a translator's note or client query** rather than resolving it in-line without a trace.
6. **Run QA proportional to stakes** — a second-linguist review or back-translation for legal/medical/safety content; a self-review pass against the termbase for lower-stakes material.
7. **For certified deliverables, complete the certification statement in the exact format the receiving institution requires** (sworn affidavit, notarization, ATA-certified stamp) — confirmed against that institution's stated requirement, not a generic certification template.

## Tools & methods

CAT (computer-assisted translation) tools — SDL Trados, memoQ, Wordfast — for translation memory (TM) reuse and fuzzy-match leverage across a project; termbases/glossaries maintained per client or domain to enforce terminology consistency; MT engines (DeepL, Google NMT, domain-tuned engines) as a first-pass draft source for MTPE workflows; ISO 18587 as the reference standard distinguishing light vs full post-editing; back-translation as an independent QA technique for high-stakes segments; ATA (American Translators Association) certification exam and code of ethics as the US professional-credential benchmark. Filled rate tables, MTPE decision tables, and a certification-statement template live in `references/playbook.md`.

## Communication style

To clients: explain equivalence tradeoffs in terms of consequence, not linguistic theory — "a literal rendering here would read as a threat in the target culture" lands better than "formal equivalence is inappropriate here." Quote turnaround in words-per-day against a stated throughput benchmark, not a vague estimate, so a client requesting an unrealistic deadline can see the gap themselves. Flag ambiguities and translator's notes as a short, itemized list attached to the deliverable — not buried as inline brackets scattered through the text, and not omitted to look more finished than the source material actually supports. To end-readers of a published translation: keep in-text notes to the minimum necessary for legal/safety clarity; a translation cluttered with translator commentary undermines the fluency it's supposed to deliver.

## Common failure modes

- **Word-for-word literal translation** that is technically accurate term-by-term but unreadable or ambiguous as connected target-language prose.
- **Silently resolving a source ambiguity** instead of flagging it — especially costly in contracts, medical records, and technical specifications where the "wrong" reading carries consequence.
- **Applying one equivalence strategy uniformly to a mixed-register document**, producing either a stiff marketing section or an unnervingly casual legal clause.
- **Treating all MT output as equally ready for light post-editing regardless of measured error density** — pricing and staffing a full-PE-quality job at light-PE effort because the raw MT "looked fine" on a quick skim.
- **Skipping certification-format verification**, delivering a linguistically sound translation that a court or agency rejects because it lacks the specific attestation format required.
- **Overcorrection: annotating every minor stylistic choice as a translator's note**, which buries the one flag that actually matters (a genuine ambiguity affecting meaning) in noise the client learns to skim past.

## Worked example

**Situation.** A manufacturing client needs a 42,000-word equipment operation manual translated from English to German for EU market release, including a safety-warning section. Publication deadline is three weeks out. The client asks for a quote and wants to know whether machine translation can be used to hit the timeline.

**Naive read.** Quote human-from-scratch translation at a typical technical EN→DE throughput of roughly 2,000 words/day (stated industry heuristic) and a rate of $0.12/word: 42,000 ÷ 2,000 = 21 working days, cost = 42,000 × $0.12 = **$5,040**. Twenty-one working days does not fit inside a three-week (15 business-day) deadline — the naive read would tell the client the deadline is infeasible without adding translators.

**Expert reasoning.** Before quoting, run a 1,000-word sample from the manual's body text (excluding the warnings section) through the domain-tuned MT engine and score the raw output: 34 substantive errors per 1,000 words — 12 terminology, 9 mistranslation, 5 omission/addition, 8 grammar. That's above the roughly-30-error/1,000-word threshold that separates "MT as a usable draft" from "MT as noise," but not by a wide margin, and the errors are concentrated in terminology (fixable by loading the client's parts glossary into the MT engine and CAT termbase before the next pass). Re-running the sample with the glossary loaded drops the error density to 19/1,000 words — comfortably below threshold. Recommend full post-editing (publication-quality bar, since this is client-facing and EU-market-regulated) at a full-PE throughput of roughly 7,000 words/day and a rate of $0.06/word (standard ~50% discount off from-scratch pricing for full PE): 42,000 ÷ 7,000 = 6 working days, cost = 42,000 × $0.06 = **$2,520**. The safety-warning section (1,400 words) is carved out and translated from scratch by a second linguist at the formal-equivalence/from-scratch rate, then back-translated to confirm no meaning drift on the warning language — an additional 1 day and $168 (1,400 × $0.12).

**Reconciling the numbers.** Full-PE body (6 days, $2,520) + from-scratch safety section with back-translation QA (1 day, $168) = **7 working days total, $2,688 total** — versus the naive from-scratch quote of 21 days and $5,040. That's within the 15-business-day deadline with 8 days of buffer, at 47% of the naive cost, while still hand-translating and independently verifying the one section (safety warnings) where an MT error carries real consequence.

**Deliverable (quote sent to client):**

> **Re: EN→DE Technical Manual Translation — Quote & Timeline**
> Sample-tested the manual against our German technical MT engine: raw output showed 34 errors/1,000 words, concentrated in parts terminology. Loading your parts glossary into the engine and our termbase dropped that to 19/1,000 words — within range for full post-editing to publication quality.
> Recommended approach: full MT post-editing for the 40,600-word body (6 working days, $2,520), with the 1,400-word safety-warnings section translated from scratch by a second linguist and back-translated to confirm no meaning drift (1 working day, $168).
> Total: 7 working days, $2,688 — comfortably inside your 15-business-day deadline. A from-scratch translation of the full document would run approximately 21 working days and $5,040; we don't recommend it here given the deadline, and the safety section gets the from-scratch treatment regardless of which path we take on the rest.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when scoping an actual translation or interpretation project: filled MTPE decision table, throughput/rate comparison table, and a certified-translation statement template.
- [references/red-flags.md](references/red-flags.md) — load when a project or assignment feels off: signals with thresholds, the first question to ask, and what to pull to check.
- [references/vocabulary.md](references/vocabulary.md) — load for precise terms of art (formal/dynamic equivalence, transcreation, light/full PE) and where generalists misuse them.

## Sources

- American Translators Association (ATA) — certification exam framework and Code of Ethics and Professional Practice.
- Eugene Nida, *Toward a Science of Translating* (1964) — formal vs dynamic equivalence framework.
- ISO 18587:2017 — post-editing of machine translation output, the light vs full post-editing distinction used throughout.
- National Center for State Courts (NCSC) and federal court-interpreter certification programs — simultaneous vs consecutive interpretation-mode standards in legal settings.
- Throughput and rate figures (2,000 words/day from-scratch, 7,000 words/day full-PE, $0.12/$0.06 per-word rates, ~30-error/1,000-word MTPE threshold) are stated industry heuristics representative of commonly reported ranges for technical EN↔DE work, not fixed constants — actual figures vary by language pair, domain, and MT engine quality. No direct practitioner has reviewed this file yet — flag corrections via PR.
