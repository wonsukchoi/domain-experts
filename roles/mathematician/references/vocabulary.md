# Vocabulary — terms of art generalists misuse

Format per term: definition → in use → misuse note.

### Well-defined
- **Definition:** a claim that an object or function's output doesn't depend on an arbitrary choice made in constructing it — e.g., that a value computed from one representative of an equivalence class is the same no matter which representative you picked.
- **In use:** "Before using f([x]) = x² mod n, check the map is well-defined — does it give the same answer for every representative of the residue class [x]?"
- **Misuse note:** generalists use "well-defined" to mean "clearly specified" or "makes sense," conflating it with ordinary clarity. In practice it names a specific proof obligation (independence of an arbitrary choice) that has to be discharged before the definition is usable at all — skipping it is a standing source of silently broken constructions.

### Rigorous
- **Definition:** an argument in which every step follows from stated premises or previously established results, with no appeal to intuition standing in for a missing step.
- **In use:** "The heuristic derivation is convincing, but it isn't rigorous yet — the interchange of limit and sum in step 3 hasn't been justified."
- **Misuse note:** generalists use "rigorous" as a synonym for "careful" or "detailed," applying it to any argument that's long or technical-looking. A rigorous argument can be short, and a long, detailed one can still contain an unjustified step — length and rigor are independent axes.

### Trivial
- **Definition:** a step or result that follows immediately from a definition or a result already on the table, requiring no new idea — a claim about how much *work* remains, not about how easy the underlying fact is to believe.
- **In use:** "The base case is trivial — it's the definition applied directly — but don't skip stating it; the inductive step is where the actual content is."
- **Misuse note:** generalists hear "trivial" as "obviously true" or "unimportant," and either skip writing the step at all or dismiss a nontrivial claim by asserting it's trivial. In a proof, a step correctly labeled trivial still has to be checked, and a step incorrectly labeled trivial is one of the most common places an error hides, because no one looks closely at something they've been told requires no thought.

### Without loss of generality (WLOG)
- **Definition:** a signal that the argument is about to assume a special case of the setup, on the grounds that every other case can be reduced to it by a symmetry or relabeling that's being asserted, not necessarily shown.
- **In use:** "WLOG assume a ≤ b — the argument for a > b is identical with the roles of a and b swapped."
- **Misuse note:** generalists read WLOG as a free pass to simplify without further justification, and writers sometimes use it to paper over a case that doesn't actually reduce the same way (see red-flags.md's asymmetry-at-a-boundary smell). The phrase is only doing legitimate work if the reduction is genuinely a relabeling — if the "general" case has structure the special case lacks, WLOG is hiding a gap, not stating one.

### Necessary and sufficient / iff
- **Definition:** a claim of logical equivalence in both directions — P holds exactly when Q holds, meaning P ⟹ Q and Q ⟹ P both need independent proof.
- **In use:** "The paper proves the condition is sufficient for convergence but only asserts, without proof, that it's also necessary — that second direction is still open."
- **Misuse note:** generalists often prove or informally argue one direction and then write "iff" or "if and only if" as if the other direction is automatic. The two directions are logically independent claims; establishing one says nothing about the other, and a review that doesn't separately check both has only verified half the stated result.

### Converges
- **Definition:** a precise claim that a sequence or approximation approaches a specific limiting value as some parameter (iteration count, mesh size, sample size) grows, in a stated sense (pointwise, in norm, in probability, almost surely) — not merely that successive values look similar to each other.
- **In use:** "The iterates are getting closer together, but that's not the same as converging to the true fixed point — check the residual against a known solution, or prove a contraction bound, before calling it converged."
- **Misuse note:** generalists treat "the numbers stopped changing much" as evidence of convergence, when a sequence can stagnate near a wrong value (a numerical instability, a local rather than global optimum) without ever approaching the quantity actually being sought. "Converges" without a stated mode and a stated limit is an unfinished claim.

### Almost surely
- **Definition:** in probability, an event that occurs with probability exactly 1 — which is a distinct claim from "always," because a probability-zero exception set can still be nonempty (e.g., a continuous random variable landing on any single exact value).
- **In use:** "The estimator converges to the true parameter almost surely, but that doesn't rule out a measure-zero set of sample paths where it fails — the almost-sure statement and a uniform guarantee are different claims."
- **Misuse note:** generalists hear "almost surely" as an informal hedge, roughly "very likely," and use it interchangeably with "probably." In the field it's a technical term meaning probability exactly 1, and swapping it for a colloquial reading understates how strong the guarantee actually is — or overstates it, if a reader assumes "almost surely" secretly means "for sure, no exceptions."

### Backward stable
- **Definition:** a property of a numerical algorithm — that its computed output is the exact solution to a slightly perturbed version of the input problem — not a claim that the computed answer itself is close to the true answer for the original input.
- **In use:** "Gaussian elimination with partial pivoting is backward stable, which is why the residual came back tiny — that's expected behavior, not evidence the solution is accurate if the problem is ill-conditioned."
- **Misuse note:** generalists (and even some practitioners under deadline pressure) treat "the algorithm is stable" as license to trust the output's accuracy directly. Backward stability is a statement about the algorithm, not the answer; whether the answer is actually close to the truth also depends on the problem's conditioning, which is a separate quantity that has to be checked (see the worked example in SKILL.md).

### Significant figures
- **Definition:** the count of digits in a reported number that are actually justified by the precision of the inputs and the computation's error propagation — not the count of digits a calculator or program happens to print.
- **In use:** "The Monte Carlo estimate has a standard error around 1% at this sample size, so quoting it to five significant figures is claiming precision the simulation doesn't have — round to two."
- **Misuse note:** generalists equate "more decimal places" with "more precise," reporting whatever a screen displays. The actual precision budget is set by the problem (condition number for linear systems, sample size for Monte Carlo, mesh resolution for PDEs) and has to be computed, not read off the output field's width.

### Statistically significant
- **Definition:** a claim that an observed effect is unlikely to have arisen from the assumed null model by chance alone, at a stated significance threshold — a statement about the null hypothesis, not a statement about how large, important, or reliable the effect is.
- **In use:** "The difference is statistically significant at p < 0.01, but the effect size is small enough that it may not matter for the decision at hand — significance and practical importance are separate questions."
- **Misuse note:** generalists use "significant" to mean "large" or "real," when the term says nothing about magnitude and depends heavily on sample size — a large enough sample makes almost any nonzero effect statistically significant. Treating statistical significance as the finish line, rather than one input alongside effect size and practical relevance, is the most common misreading.

### Closed form
- **Definition:** an expression for a solution built from a finite combination of a specified, agreed-upon set of standard operations and functions (e.g., elementary functions, or a named special-function class) — not simply "an explicit formula" in the abstract, since what counts as "closed form" depends on which function class is allowed.
- **In use:** "There's no closed-form solution in elementary functions, but it does have one in terms of the incomplete gamma function — whether that counts as 'closed form' depends on what class of functions the downstream use case can actually work with."
- **Misuse note:** generalists use "closed form" to mean "not numerical" or "a real formula," without noticing the term is relative to an allowed function set. A result reported as having "no closed form" may simply mean no elementary closed form — declaring a problem intractable on that basis alone overstates the claim.

### Degenerate
- **Definition:** a special case of a general setup where some parameter or configuration takes a boundary or singular value that breaks an assumption the general argument relies on (e.g., a matrix losing rank, two roots of a polynomial coinciding, a distribution collapsing to a point mass) — a technical marker for "the generic-case argument needs a separate check here," not a value judgment.
- **In use:** "The formula holds for distinct eigenvalues; the degenerate case where two eigenvalues coincide needs its own argument, since the diagonalization the general proof relies on doesn't go through as stated."
- **Misuse note:** generalists hear "degenerate" as a synonym for "unimportant" or "not worth checking," and treat it as safe to wave past. In practice, a degenerate case is exactly the place a generic-case proof is most likely to silently fail (see red-flags.md's symmetry-at-a-boundary smell), so flagging something as degenerate should raise scrutiny, not lower it.

### Counterexample
- **Definition:** a single specific instance that satisfies a claim's hypotheses but violates its conclusion, which is sufficient on its own to refute a universally-quantified claim — no accompanying explanation of *why* it fails is logically required, though one is usually expected for it to be useful.
- **In use:** "You don't need to explain why the conjecture fails in general — one explicit n where the claimed inequality doesn't hold is a complete refutation."
- **Misuse note:** generalists sometimes look for a "counterexample" as though it needs to be representative or come with a general diagnosis, and conversely dismiss a valid counterexample as "just an edge case" rather than accepting it as a full refutation. One verified counterexample kills a universal claim outright, regardless of how atypical it looks.

### Orthogonal
- **Definition:** a precise geometric or algebraic relation — vectors whose inner product is zero, or (loosely, by extension) variables or errors that are uncorrelated / statistically independent in a specified sense — not a general synonym for "unrelated" or "separate."
- **In use:** "The two error sources are orthogonal in the sense that their covariance is zero, which is what lets the total variance be computed as a simple sum — that's a specific property being invoked, not just a figure of speech."
- **Misuse note:** generalists borrow "orthogonal" loosely to mean "these two things don't affect each other" without checking whether the actual mathematical relation (zero inner product, zero covariance, independence) holds. Downstream calculations — like adding variances directly — are only valid because of that specific property, and the loose usage papers over whether it's actually been checked.

### Exponential
- **Definition:** growth or decay of the form proportional to a constant raised to a variable power (e.g., c·rⁿ), characterized by a fixed relative growth rate — a specific functional form, not a synonym for "fast" or "steep."
- **In use:** "The algorithm's running time is exponential in the input size — 2ⁿ steps — which is qualitatively different from polynomial growth no matter how the constant factors are tuned."
- **Misuse note:** generalists use "exponential" loosely for any rapid increase, including ones that are actually polynomial with a large exponent or degree, or merely superlinear. The distinction matters concretely: an exponential-time algorithm doesn't become tractable by a faster computer or a better constant, because the growth rate itself, not the starting point, is what dominates at scale.
