# Red flags — what a mathematician notices instantly

Smell tests with thresholds. Format per flag: signal → most likely cause(s) → first question → data to pull. Any one can be innocent; two or three together is a pattern.

### A step justified by "clearly," "obviously," or "by symmetry" at a point where an earlier case split introduced an asymmetry (a boundary, a degenerate parameter value, a sign change)
- **Usually means:** the author checked the generic case and is assuming the edge case transfers, but the very thing that made the case split necessary (the boundary/degeneracy) is exactly what breaks the symmetry argument.
- **First question:** "Walk me through this step for the specific case where [the parameter] hits the boundary — does the same argument literally go through, or does it need a separate check?"
- **Data to pull:** the case-split definition earlier in the proof, and whether the boundary case appears anywhere else with its own explicit treatment (if it never does, that's the tell).

### A lemma cited by more than 5 later results but itself proved in under a paragraph or relegated to an appendix with no worked detail
- **Usually means:** the lemma is treated as low-risk because it "feels standard," but its centrality means any error propagates to every downstream branch — review effort has been allocated inversely to actual risk.
- **First question:** "How many of this paper's main results actually depend on this lemma, and has anyone re-derived it independently rather than reading it?"
- **Data to pull:** the dependency count (grep citations of the lemma number through the rest of the manuscript), and the review notes/referee report to see if this specific lemma got dedicated scrutiny or was waved through with the rest.

### A computer-assisted proof described as "peer reviewed" with no stated fraction of the computation independently re-executed
- **Usually means:** the panel read and certified the human argument (the reduction to finitely many cases) but explicitly declined to re-run the computational part, and that distinction has been lost in how the result gets cited afterward.
- **First question:** "What fraction of the computation was independently re-executed on different code and different hardware, versus just read?"
- **Data to pull:** the referee report's own scope statement (most say this explicitly, e.g. the original Kepler conjecture panel's 99%-certain, computation-not-verified caveat), and whether an independent re-implementation exists and what it found.

### A numerically computed result reported to more decimal digits than 16 − log₁₀(κ(A)) allows, with only the residual cited as evidence of accuracy
- **Usually means:** the author is treating "small residual" as "accurate solution," which holds only when the problem is well-conditioned — for an ill-conditioned system a tiny residual is compatible with a wildly inaccurate computed answer.
- **First question:** "What's the condition number of the system this came from, and how many digits does that actually leave after accounting for it?"
- **Data to pull:** `cond(A)` (or the relevant problem's condition number analog) and the claimed digit count in the writeup, checked against the rule of thumb before the number goes into anything downstream.

### A PDE or ODE numerical result reported at a single mesh resolution with no convergence table across at least 2 refinement levels
- **Usually means:** the reported value hasn't been shown to be converging to anything — it could be a discretization artifact that would move if the mesh were refined, and there's no way to state an error bound without at least two resolutions to compare.
- **First question:** "What does this value do at half the mesh spacing — has anyone run it?"
- **Data to pull:** the solution at 2–3 mesh resolutions (or timesteps), the empirical convergence order computed from them, and whether that order matches the scheme's theoretical order (a mismatch signals a bug, not just slow convergence).

### A Monte Carlo estimate reported with more significant digits than its stated (or computable) standard error of √(N) justifies
- **Usually means:** the precision written down is aesthetic, not statistical — a result from N = 10,000 samples has a relative standard error around 1%, which caps meaningful precision at roughly 2 significant digits regardless of how many digits the code printed.
- **First question:** "How many samples, and what's the standard error on this specific number — does it support the digits being quoted?"
- **Data to pull:** N, the sample variance, the resulting standard error, and whether variance-reduction techniques (antithetic variates, importance sampling) were used and their effect reported.

### An arXiv preprint claiming a major result still being cited as established >3 years after posting with no refereed-journal publication and no independent replication noted
- **Usually means:** the result is sitting in the gap between "posted" and "the community has converged on it being correct" — priority has been established but not verification, and citations that treat it as settled are overstating its status.
- **First question:** "Has this been refereed anywhere, or independently re-derived by a group with no connection to the original authors, or is the only evidence that no one has yet found a flaw?"
- **Data to pull:** journal submission/publication status, any independent replications or alternative proofs in the literature, and the specific claim being relied on downstream (sometimes only a sub-result is actually needed, and that piece may be better-established than the whole paper).

### A disputed major proof where the disagreement has run more than 6 months without narrowing to a specific numbered line, lemma, or corollary
- **Usually means:** neither side has actually located the technical crux — the dispute is being argued at the level of "does the whole paper work," which never resolves, instead of at the level of one falsifiable claim.
- **First question:** "What is the single specific statement — by number — that this whole disagreement turns on?"
- **Data to pull:** the correspondence/preprint history between the disputing parties, and whether either side has produced a numbered counterexample or gap pinned to a specific line (the Scholze–Stix critique of the Mochizuki IUT proof is the reference case: years of broad dispute collapsed to Corollary 3.12 only after an in-person meeting).

### A formal-verification announcement ("fully verified in Lean/Coq/Isabelle") where the formal statement's hypotheses or conclusion differ from the informal theorem as published
- **Usually means:** the formalization verified a true statement, just not quite the one being claimed — a missing hypothesis, a weaker conclusion, or a differently-quantified statement can make the formal result correct but not equivalent to the headline claim.
- **First question:** "Read me the formal statement's exact hypotheses and conclusion — does it match the informal theorem word for word, or is there a gap?"
- **Data to pull:** the formal statement as written in the proof-assistant source, side by side with the paper's theorem statement, and the size ratio of the formalization to the original (a ratio far below the ~4x De Bruijn-factor norm often means something got simplified away, not that the formalization was unusually efficient).

### A grant proposal's Broader Impacts (or equivalent) section is textually identical, or near-identical, across two or more of the same author's different proposals
- **Usually means:** the section was copy-forwarded rather than re-derived from this specific project's actual impact pathway, which both weakens the proposal on its merits and is something program officers cross-check across an author's submission history.
- **First question:** "What in this specific project's broader impacts couldn't also be said about the last three proposals you submitted?"
- **Data to pull:** the author's prior 2–3 submitted proposals' corresponding sections for a side-by-side diff, and the specific NSF (or equivalent agency) page-cap and structural requirements to confirm the section is doing real work within its allotted space.
