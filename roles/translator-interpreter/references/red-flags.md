# Translator/Interpreter — Red Flags

### MT engine shows >50 errors per 1,000 words on domain-specific content, spread across grammar and mistranslation, not just terminology
- **Usually means:** the language pair or domain is poorly represented in the MT engine's training data — a low-resource pair, or a highly specialized domain (patent claims, poetic/literary text) the engine wasn't tuned on.
- **First question:** is a domain-tuned or custom-trained engine available for this pair, or does the client have an existing termbase that could narrow the gap?
- **Data to pull:** the sample error log broken down by error type (terminology vs grammar vs mistranslation vs omission).

### Same source term translated two different ways within one document
- **Usually means:** no termbase was built, or an existing termbase wasn't consulted/enforced during translation.
- **First question:** was a termbase created for this project, and was it loaded into the CAT tool before translation began?
- **Data to pull:** the CAT tool's term-consistency QA report.

### Client requests "translate it literally" for marketing or brand copy
- **Usually means:** the client conflates literal wording with quality or accuracy, without realizing a literal rendering may be flat, confusing, or unintentionally comic in the target culture.
- **First question:** what is the actual goal of this copy — inform, or persuade? Does legal/compliance require exact wording for any specific claim within it?
- **Data to pull:** the brand voice/tone guide, and any specific claims flagged by legal as needing exact-wording preservation.

### Turnaround requested well below realistic throughput (e.g., 40,000+ words in 2-3 days with no MT/light-PE path viable)
- **Usually means:** the client doesn't know the realistic throughput benchmark for the content type, or the deadline was set without consulting a linguist.
- **First question:** what's driving the deadline — is phased or partial delivery an option, or can more linguists be added without breaking terminology consistency?
- **Data to pull:** a throughput calc (word count ÷ realistic words/day) laid next to the requested deadline.

### Certified translation requested with no stated receiving-institution requirement
- **Usually means:** the client assumes "certified" is a single universal standard, when courts, immigration agencies, and vital-records offices each define it differently (sworn translator, notarized affidavit, ATA-certified stamp).
- **First question:** which specific agency, court, or institution is requesting the certified translation, and what format do they specify?
- **Data to pull:** the receiving institution's own written instructions on certification format.

### Simultaneous interpretation booked for a legal deposition, sworn testimony, or medical intake
- **Usually means:** the booking process defaulted to the faster/cheaper mode without weighing that the setting may legally or clinically require the ability to interrupt for clarification.
- **First question:** does the proceeding's governing rules (court, deposition protocol, clinical intake standard) require or strongly prefer consecutive interpretation for accuracy and record purposes?
- **Data to pull:** the proceeding's interpreter-mode requirement, if one is specified in its governing rules.

### Post-editor's tracked changes show >90% of raw MT output accepted unchanged on technical or safety content
- **Usually means:** the post-editor is under-editing (skimming rather than verifying against source), not that the MT output was unusually clean — genuine full-PE work on technical content almost always touches more than 10% of segments.
- **First question:** does a spot-check of "unchanged" segments against the source text reveal missed errors?
- **Data to pull:** the CAT tool's edit-distance or change-tracking report, cross-checked against a manual spot sample.

### Back-translation of a safety, legal-obligation, or dosage segment reveals meaning drift
- **Usually means:** the translator over-adapted for fluency at the expense of precise meaning, or a source term was ambiguous and got resolved incorrectly.
- **First question:** which specific clause drifted, and does the drift change the practical instruction (e.g., a dosage frequency, a legal obligation)?
- **Data to pull:** the side-by-side back-translation comparison table.

### Legal or medical document assigned to a translator without subject-matter or jurisdictional certification
- **Usually means:** cost or schedule pressure bypassed a certification requirement that the receiving institution (court, insurer, regulator) will check.
- **First question:** does the intended use require a certified or sworn translator specifically, or is general professional competence sufficient?
- **Data to pull:** the certifying/receiving body's stated credential requirement.

### Interpreter given no prep material (glossary, agenda, speaker list) before a technical or medical assignment
- **Usually means:** the booking process treated interpretation as a commodity service rather than one requiring domain preparation, raising the error risk on specialized terminology.
- **First question:** was any prep material sent, and if not, can the assignment be pushed back long enough to send a glossary or agenda?
- **Data to pull:** timestamp of any prep material sent relative to the assignment date.
