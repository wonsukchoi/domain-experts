# Technical Writer — Vocabulary

### Diátaxis
A documentation framework classifying content into four types by reader need: tutorials (learning by doing), how-to guides (accomplishing a specific goal), reference (looking up facts), and explanation (understanding context/why).
**In use:** "This page is trying to be a tutorial and a reference at once — split it before we touch anything else."
**Common misuse:** Treated as a rigid template every page must fit, rather than a diagnostic lens for figuring out what a struggling page is actually failing to do.

### Docs-as-code
A workflow where documentation lives as plain-text files in the same version-control repo as the source code, reviewed via pull request and built/tested by the same CI pipeline.
**In use:** "The docs PR failed CI because the example endpoint now returns a different error shape."
**Common misuse:** Assumed to mean "docs are in Markdown," when the load-bearing part is that docs are versioned and tested alongside code, not just stored in a similar file format.

### Minimalism (technical communication)
John Carroll's principle that documentation should support real tasks immediately, let users start acting right away, and build on what they already know rather than front-loading complete conceptual coverage.
**In use:** "Cut the three paragraphs of background — get them to a working call in the first five lines."
**Common misuse:** Confused with "write less," when it actually means "sequence toward action first," which sometimes requires more total content, just reordered.

### Information architecture
The structural organization of a documentation set — how pages are grouped, linked, and named so a reader can predict where to find something without searching.
**In use:** "The IA has three different pages named 'Authentication' in different sections — that's why search results are useless."
**Common misuse:** Treated as a one-time design exercise instead of something that needs re-auditing as content grows.

### Style guide
A codified set of rules for terminology, voice, formatting, and structure, used to keep a large or multi-author documentation set consistent.
**In use:** "Per style guide, we use 'select' not 'click' since not all input is mouse-based."
**Common misuse:** Applied as a grammar-correctness checklist rather than a consistency tool — style debates get raised on pages that have a real accuracy gap sitting untouched.

### Doc drift / staleness
The divergence between what documentation describes and what the system actually does, accumulating as the system changes without a corresponding doc update.
**In use:** "This page hasn't drifted yet, but it will the moment someone changes the default timeout without a docs PR."
**Common misuse:** Treated as an inevitable cost of time passing, when it's actually a process gap — drift rate tracks directly to whether docs are in the same release pipeline as code.

### Coverage audit
A systematic comparison of what should be documented (e.g., every API endpoint) against what actually has a doc page, distinguishing "no page" from "page exists but is inaccurate."
**In use:** "The coverage audit found 75% nominal coverage, but a quarter of the 'documented' set has examples that no longer run."
**Common misuse:** Reported as a single coverage percentage without separating undocumented from stale — the two have very different remediation priority.

### Task orientation
Structuring content around what the reader is trying to accomplish rather than around the system's internal organization or feature list.
**In use:** "Reorganize this from 'API objects' to 'things you can do' — nobody arrives here wanting to read about the Webhook object in the abstract."
**Common misuse:** Assumed to only apply to tutorials, when reference pages also benefit from being findable by task ("how do I cancel a subscription") not just by object name.

### Progressive disclosure
Presenting only the information needed for the immediate step, with deeper detail available on demand (a link, an expandable section) rather than all at once.
**In use:** "Put the retry-backoff algorithm details behind a link — most readers just need to know 'yes, we retry.'"
**Common misuse:** Used as an excuse to bury information that most readers actually do need up front, mistaking "shorter page" for "better progressive disclosure."

### Changelog / release notes
A chronological record of what changed in each release, distinct from reference docs (which describe current-state behavior only).
**In use:** "Check the changelog before assuming this endpoint always required that header — it was added in v2.3."
**Common misuse:** Conflated with reference documentation; a changelog entry is not a substitute for updating the reference page to reflect the new current behavior.

### API reference vs. guide
A reference page answers "what does this call take/return" with no narrative; a guide (how-to) answers "how do I accomplish X" using one or more calls in sequence.
**In use:** "That's reference material — move the step-by-step onboarding flow to its own guide."
**Common misuse:** Writers default to reference-only documentation because it's easier to generate from a spec, leaving no guide for how the pieces combine to accomplish anything.

### Error-message documentation
Documentation specifically indexed by the error codes/messages a system produces, so a user who hits an error can search the exact text and find a resolution path.
**In use:** "Every 4xx response should map to a doc page — right now half our error codes have no corresponding explanation anywhere."
**Common misuse:** Treated as optional polish rather than a primary support-deflection surface — error-message pages are often the highest-traffic, highest-value pages in a doc set.

### Single-sourcing
Maintaining one canonical version of a piece of content and reusing/transcluding it everywhere it's needed, rather than copy-pasting and letting copies drift independently.
**In use:** "The rate-limit numbers are single-sourced from one file now — no more three pages disagreeing on the limit."
**Common misuse:** Attempted at the prose level (copying whole paragraphs) instead of at the fact level (a single source of truth for numbers/values that gets referenced), which is harder to maintain and drifts anyway.

### Doc linter
An automated tool (e.g., Vale, alex) that checks prose against style-guide rules — terminology consistency, passive voice, inclusive language — as part of CI.
**In use:** "The linter caught three instances of 'simply' — we don't use that word, it's dismissive to a stuck reader."
**Common misuse:** Mistaken for a completeness or accuracy check; a linter catches style violations, not whether the documented behavior is still true.
