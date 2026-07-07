### Characterization test
A test written by recording a legacy system's *actual* current output for given inputs, without judging whether that output is correct, so behavior can be locked in before modification.
**In use:** "We don't have a spec for this routine, so I wrote characterization tests off production logs before touching anything."
**Common misuse:** Treated as interchangeable with a regular unit test — a unit test asserts *intended* behavior from a spec; a characterization test asserts *observed* behavior with no claim it's correct.

### Clause coverage
The fraction of a spec's individually testable clauses (rules, boundary conditions, stated examples) that have a corresponding test, as opposed to line or branch coverage of the code.
**In use:** "Line coverage is 100%, but clause coverage is only 4 of 6 — the currency-conversion clause has no test."
**Common misuse:** Conflated with code coverage percentage; a function can be fully executed by tests while a specific documented rule inside it is never actually asserted.

### Cyclomatic complexity
A count of the number of linearly independent paths through a function's control flow, originally defined by Thomas McCabe as a proxy for how hard the function is to fully test and reason about.
**In use:** "This function's cyclomatic complexity is 14 — split it before adding the new discount tier."
**Common misuse:** Treated as a hard build-breaking gate rather than a signal; some legitimately branchy dispatch logic scores high without being genuinely hard to reason about.

### Spec traceability
The documented mapping from each requirement/spec clause to the specific test(s) that verify it, used to answer "is this requirement actually tested" rather than "is this line executed."
**In use:** "Pull up the traceability table before sign-off — QA wants to see which clause each test maps to."
**Common misuse:** Skipped as bureaucratic overhead; without it, "all tests pass" and "the spec is satisfied" quietly become treated as the same claim, when they aren't.

### Round-trip (on a spec)
Sending a batched clarification back to the spec's author and waiting for a written answer before implementing the ambiguous section, rather than guessing and proceeding.
**In use:** "That's a round-trip question, not something I should assume — batching it with the other two from section 4."
**Common misuse:** Done one question at a time instead of batched, which multiplies the analyst's response latency and trains them to deprioritize the thread.

### Boy Scout Rule
The practice of leaving code slightly cleaner than you found it whenever you touch it for another reason.
**In use:** "I renamed the two local variables while I was in there fixing the discount bug — Boy Scout Rule, nothing else changed."
**Common misuse:** Used to justify broad refactors bundled into a spec-driven change, which defeats its own purpose by making the diff harder to check against the spec.

### Assumption log
A running, versioned list attached to a deliverable stating every place an ambiguity was resolved by assumption rather than confirmation, and its current status (pending / resolved / scoped out).
**In use:** "Check the assumption log before you sign off — two items are still pending confirmation."
**Common misuse:** Treated as a one-time note at kickoff rather than a living artifact updated every commit; stale assumption logs give false confidence that everything's been confirmed.

### Boundary condition
An input at or adjacent to a stated threshold (exactly at the limit, one unit above, one below, empty, maximum) where off-by-one and rounding errors concentrate.
**In use:** "The spec says 'over $50' — I need a test at exactly $50.00 and $50.01, not just $65 and $30."
**Common misuse:** Assumed to be adequately covered by "large" and "small" example values, which miss the exact edge where the stated rule's wording (over vs. at-or-over) actually matters.

### Regression (in maintenance context)
A previously-correct behavior that breaks as a side effect of an unrelated change, detected by running the full existing suite rather than only new tests.
**In use:** "The new discount logic is spec-compliant, but it's a regression — it broke the existing tax-calculation test."
**Common misuse:** Used loosely for any new bug, when it specifically means breaking something that used to work, which is why full-suite runs (not just new-feature tests) are non-negotiable.

### Scoped out
A spec clause deliberately not implemented in the current deliverable, documented as such rather than silently omitted.
**In use:** "Non-USD orders are scoped out this release, flagged in the assumption log and the traceability table."
**Common misuse:** Confused with "forgotten" — the distinguishing feature is that it's written down and visible to whoever signs off, not just absent from the code.
