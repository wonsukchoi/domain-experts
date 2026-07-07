# Translator/Interpreter — Vocabulary

### Formal equivalence
A translation strategy that preserves the source text's structure, form, and precise terminology as closely as the target language allows, even at some cost to natural readability.
**In use:** "This is a drug label — formal equivalence, not transcreation; the regulator needs to be able to trace every term back to the source."
**Common misuse:** Treated as simply "more accurate" translation in general, when it's a strategy appropriate to specific registers (legal, regulatory, technical), not a universal default.

### Dynamic equivalence
A translation strategy (Eugene Nida) that prioritizes reproducing the source's effect and natural readability in the target language over preserving its exact structure.
**In use:** "The instructions read stiff in German — we need dynamic equivalence here, the reader just needs to understand what to do."
**Common misuse:** Confused with "loose" or "inaccurate" translation, when it's a deliberate strategy for content where naturalness matters more than structural fidelity.

### Transcreation
Adapting content's persuasive or emotional effect for a target culture, treating the literal source wording as fully disposable.
**In use:** "The tagline doesn't translate — we transcreated it into an idiom that lands the same joke in German."
**Common misuse:** Applied to legal or technical content where the literal wording actually matters, producing a rewrite that drops load-bearing precision.

### Back-translation
Independently translating a target-language text back into the source language, without reference to the original, to check whether meaning was preserved.
**In use:** "Back-translate the warning label before we ship — I want an independent check that nothing drifted."
**Common misuse:** Skipped on the assumption that a fluent-reading target text is automatically an accurate one; fluency and accuracy are independent properties.

### Translation memory (TM)
A database of previously translated source-target segment pairs, reused via fuzzy or exact matching to speed up and standardize future translations in the same domain.
**In use:** "This project has 40% fuzzy-match leverage from the TM — that cuts the effective new-word count significantly."
**Common misuse:** Assumed to guarantee consistency automatically; a TM only helps if segments are reviewed for context fit, not blindly auto-inserted.

### Termbase
A managed glossary of approved target-language terms for specific source terms within a domain or client, enforced during translation and QA.
**In use:** "The parts numbers keep getting mistranslated — we need the client's termbase loaded before the next pass."
**Common misuse:** Treated as optional reference material rather than an enforced constraint; without active enforcement, translators drift to individually "reasonable" but inconsistent choices.

### Light post-editing (light PE)
Machine-translation post-editing that corrects only errors serious enough to mislead or embarrass, without polishing style — the fastest, cheapest MTPE tier.
**In use:** "This is internal-only reference material — light PE is enough, we don't need publication polish."
**Common misuse:** Applied to client-facing or published content to save cost, producing text that is technically correct but reads as obviously machine-translated.

### Full post-editing (full PE)
Machine-translation post-editing that brings the output to human-parity quality — style, register, and terminology all corrected, not just outright errors.
**In use:** "This ships to end customers, so it's full PE — I want it indistinguishable from a from-scratch translation."
**Common misuse:** Assumed to always be faster/cheaper than from-scratch regardless of raw MT quality; above a certain raw-error density, full PE can cost more time than translating from scratch.

### Simultaneous interpretation
Real-time spoken interpretation delivered concurrently with the speaker, typically via headset in a booth, with no pause for clarification.
**In use:** "Book simultaneous for the conference panel — we need real-time delivery for a live multilingual audience."
**Common misuse:** Chosen by default for any live event regardless of precision requirements, when consecutive is the safer choice wherever an interruption for clarification matters more than speed.

### Consecutive interpretation
Spoken interpretation delivered after the speaker pauses, allowing the interpreter to ask clarifying questions before rendering — roughly half the throughput of simultaneous.
**In use:** "This is a deposition — consecutive, so counsel can hear exactly what was clarified before it's on the record."
**Common misuse:** Dismissed as simply "the slower, outdated mode," when its clarification capability is a deliberate accuracy feature, not a limitation.

### Sworn/certified translator
A translator credentialed by a professional body (e.g., ATA) or a jurisdiction (e.g., a court-appointed sworn translator) to produce translations accepted as official for legal, immigration, or court purposes.
**In use:** "This goes to USCIS — it needs a certified translator's statement attached, not just a fluent bilingual colleague's version."
**Common misuse:** Assumed to be a single universal credential; certification requirements vary by receiving institution and jurisdiction, and a credential valid for one purpose may not satisfy another.

### Register
The level of formality, technicality, or social distance encoded in language choice, which must match between source and target text for the same effect.
**In use:** "The source is casual internal Slack-speak — translating it into formal business German changes how the reader perceives the sender."
**Common misuse:** Overlooked in favor of purely lexical accuracy — a translation can get every word "right" and still misrepresent the speaker's tone entirely.

### Calque
A target-language term or phrase constructed by directly translating the components of a source-language term that has no direct target equivalent.
**In use:** "There's no German word for this software feature — we're using a calque with a gloss on first mention."
**Common misuse:** Used silently without a gloss, leaving the target-language reader to guess at a coined term's meaning.
