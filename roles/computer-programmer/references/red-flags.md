### Spec gives fewer than 3 worked examples for a stated rule
- **Usually means:** the author validated the rule mentally against one or two cases and didn't enumerate the boundary; second likeliest: the rule was copy-pasted from a similar-but-not-identical prior spec.
- **First question:** "Can you give me the expected output for an empty/max/concurrent case, since none is shown?"
- **Data to pull:** the spec's own example table; a diff against the previous spec version if one exists.

### Legacy function's inline comment contradicts its actual return value
- **Usually means:** the comment was never updated after a fix; second likeliest: the "fix" that broke the comment's promise was itself a workaround for a caller's bug.
- **First question:** "Who calls this, and does their handling assume the comment or the actual behavior?"
- **Data to pull:** call-site grep across the codebase; git blame on both the comment and the return statement.

### Two spec sections reference the same field with different constraints
- **Usually means:** the spec was authored by two people over time without a merge review; second likeliest: one section describes an old version, the other the intended new one.
- **First question:** "Which section supersedes — is this a versioning gap or two rules that both need to hold?"
- **Data to pull:** spec revision history / changelog if tracked.

### Code coverage is 100% but no test asserts a specific numeric boundary value
- **Usually means:** tests exercise the code path, not the spec's stated threshold; second likeliest: the threshold was hardcoded without a test for the off-by-one case ($50.00 vs $50.01).
- **First question:** "Is there a test where the input is exactly at the threshold, not just above or below it?"
- **Data to pull:** coverage report cross-referenced against the spec's stated numeric constants.

### A code-generation tool's output compiles and passes existing tests on the first try for a nontrivial spec clause
- **Usually means:** the clause was simple enough that generation got lucky; second likeliest: the existing test suite doesn't yet cover the new clause, so "passing" proves nothing about the new behavior.
- **First question:** "Did I write a new test for this clause specifically, or am I relying on tests that predate it?"
- **Data to pull:** diff of the test suite alongside the diff of the implementation.

### More than 2 rounds of "quick clarifying questions" sent in the same day for the same spec section
- **Usually means:** the section is genuinely underspecified and needs a rewrite, not a trickle of Q&A; second likeliest: the questions weren't batched, wasting the analyst's attention budget.
- **First question:** "Should this section go back for a rewrite instead of another round of patches-via-Q&A?"
- **Data to pull:** the thread history for that section.

### Cyclomatic complexity of a single function exceeds ~10 (McCabe)
- **Usually means:** the function is doing two or more spec clauses' worth of logic in one place; second likeliest: error-handling branches were bolted on ad hoc instead of designed in.
- **First question:** "Does each branch map to a distinct spec clause, or are unrelated rules tangled together?"
- **Data to pull:** static analyzer complexity report for the file.

### A "bug fix" to legacy behavior has no corresponding written confirmation from a domain owner
- **Usually means:** the behavior was assumed to be a bug based on code-reading alone, without checking a downstream consumer's dependence on it; second likeliest: it really is a bug, but the fix has no paper trail if it turns out to break something.
- **First question:** "Who signed off that this is a bug and not an undocumented feature someone relies on?"
- **Data to pull:** ticket/approval trail for the change; consumer list from the characterization test's log-derived input set.
