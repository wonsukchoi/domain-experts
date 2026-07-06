# Red flags & diagnostics

Signals an experienced computer and information research scientist notices instantly when screening a draft paper, proposal, or experiment plan. Load this when triaging a specific submission — not for general reasoning (that's `SKILL.md`).

### A single proposed component is credited with the entire headline gain and no ablation table appears
- **Usually means:** part or most of the improvement comes from a learning-rate schedule change, batch-size increase, or other riding-along tweak, not the proposed idea
- **First question:** "What's the accuracy delta with every other change reverted to baseline, one at a time?"
- **Data to pull:** the training config diff between baseline and final run, and any intermediate checkpoints that isolate each change

### A reported improvement is under 1 percentage point on a single seed/split with no variance reported
- **Usually means:** the effect is within noise from seed variance or eval-split sampling, not a real effect
- **First question:** "What's the standard deviation across at least 3 seeds, and does the gain exceed 2x that spread?"
- **Data to pull:** per-seed results table (raw, not just mean) and the eval-set size

### The Methods section contains an equation that doesn't recur anywhere else in the paper (in the algorithm, the code, or a subsequent derivation)
- **Usually means:** mathiness — notation added to signal rigor without adding precision beyond the surrounding prose
- **First question:** "What does this equation let a reader compute or predict that the prose alone didn't?"
- **Data to pull:** the equation's variable definitions and whether each variable is instantiated anywhere in the implementation

### A causal claim about model behavior ("the model learns to X because Y") has no intervention or ablation behind it
- **Usually means:** a plausible-sounding mechanistic story is being asserted as explanation when it's actually speculation
- **First question:** "What experiment would falsify this specific causal claim, and was it run?"
- **Data to pull:** the interpretability or ablation evidence (if any) cited for the mechanistic claim

### Reproducibility is claimed with the phrase "code available upon request" or "will be released"
- **Usually means:** nothing is actually packaged yet, and post-publication release rates for this phrasing are historically low (per the 2023-2025 aggregated studies, ~6% code-release rate in one 255-paper sample)
- **First question:** "What's the commit hash and repository URL right now, not at camera-ready?"
- **Data to pull:** the repository link, its last-commit timestamp, and whether it includes a pinned environment (Dockerfile, lockfile, or conda spec with hash)

### An NSF CISE Project Description draft is being reviewed for content before its page count and section labels are checked
- **Usually means:** the draft is at risk of administrative return before a program officer reads the substance
- **First question:** "Is this at or under 15 pages, and does the one-page Project Summary have Intellectual Merit and Broader Impacts as two separately labeled statements?"
- **Data to pull:** current page count per PAPPG-defined section and a checklist of required labeled headers

### An experiment manipulates what real users see, feel, or are shown, and the only clearance cited is the platform's general Terms of Service
- **Usually means:** a project-specific consent or IRB-equivalent review was skipped in favor of a blanket policy never scoped to cover behavioral manipulation
- **First question:** "Has this specific study design gone through an IRB-equivalent or ethics review, independent of the ToS?"
- **Data to pull:** the IRB-equivalent approval number/date, or its explicit absence, for this study

### A claimed "reproducible" result has no artifact submission tier stated (Available / Evaluated / Reproduced / Replicated)
- **Usually means:** reproducibility is being used as an adjective, not a badge the team is targeting or has earned
- **First question:** "Which ACM artifact badge tier are we targeting, and what's missing to clear it?"
- **Data to pull:** the artifact-evaluation checklist against the specific target badge's requirements

### A "surprising" result has a large effect size relative to a small sample or eval set (n < 100, or single held-out split)
- **Usually means:** the result is more likely a confound or overfit to the specific split than a genuine effect
- **First question:** "Does this replicate on an independent held-out split or a second dataset?"
- **Data to pull:** sample/eval-set size and results on any independent replication split attempted

### A safety-critical system relies on one verification method (e.g., a software test suite) with no independent check
- **Usually means:** a second, structurally different safeguard (hardware interlock, out-of-sample audit) was removed as "redundant" when it was actually the backstop for the first method's blind spots
- **First question:** "What independent verification method exists that doesn't share the same failure mode as the primary one?"
- **Data to pull:** the verification/test coverage report and a list of any interlocks or checks removed in the last revision

### A reviewer-facing rebuttal reframes a null or negative ablation result as a "limitation for future work" rather than revising the headline claim
- **Usually means:** the headline claim is being preserved past the point the evidence supports it
- **First question:** "Does the abstract's claim still hold once this negative ablation result is accounted for?"
- **Data to pull:** the ablation result in question and the exact wording of the abstract's claim

### A funding proposal's Broader Impacts section restates the Intellectual Merit content in different words rather than describing a distinct activity
- **Usually means:** the two required NSF statements aren't actually distinct, which reads as a box-checking exercise to a program officer
- **First question:** "What specific broader-impact activity (education, outreach, dataset/tool release to a wider community) exists independent of the research contribution itself?"
- **Data to pull:** the Broader Impacts paragraph text side-by-side with the Intellectual Merit paragraph

### A terminology dispute surfaces where a term of art ("reproduced" vs. "replicated," "significant" vs. "statistically significant") is used loosely across sections of the same paper
- **Usually means:** terminology misuse is blurring a distinction reviewers will hold the paper to
- **First question:** "Is this term used consistently with its ACM/field-standard definition everywhere it appears in the draft?"
- **Data to pull:** every instance of the term in the draft, checked against the standard definition
