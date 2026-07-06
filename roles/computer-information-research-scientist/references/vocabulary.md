### Ablation

A controlled experiment that removes or isolates one factor at a time against a fixed baseline to attribute a metric change to that specific factor, rather than to the sum of everything that changed alongside it.
**In use:** "Add a row for the batch-size change alone — we can't credit the module until the ablation isolates it."
**Common misuse:** Calling any before/after comparison an "ablation" when only one configuration was run — an ablation requires a table of intermediate configurations, not a single baseline-vs-final comparison.

### Reproducibility (vs. replicability)

Reproducibility means an independent party gets the same result using the *original* authors' code and data; replicability means an independent party gets the same result with *new* code and/or new data testing the same hypothesis — a stronger, more meaningful bar. The ACM's post-2020 terminology swapped which word means which, reversing the pre-2020 usage.
**In use:** "The code ran and matched — that's reproduced. We haven't shown it replicates on an independent implementation."
**Common misuse:** Using "reproducible" to mean "the underlying finding is true," when it only certifies that a specific artifact reruns to the same output — a bug can reproduce perfectly.

### Artifact badge (ACM)

A tiered certification (Available → Evaluated–Functional → Evaluated–Reusable → Results Reproduced → Results Replicated) attached to a paper's submitted code/data package, awarded by reviewers who actually exercise the artifact, not claimed by the authors.
**In use:** "We're targeting Evaluated–Functional — the Docker image is pinned and the eval script runs end to end."
**Common misuse:** Writing "artifacts available" in the paper without an actual reviewed submission, treating the aspiration as if it were the certification.

### Mathiness

Formal notation (equations, theorems, big-O statements) that dresses up an informal or unverified claim in the appearance of rigor without adding any precision the prose didn't already have — a named failure mode from Lipton & Steinhardt's "Troubling Trends" taxonomy, not a synonym for "too much math."
**In use:** "That theorem restates the intuition in symbols — cut it or make it actually load-bearing; right now it's mathiness."
**Common misuse:** Treating "the paper has equations" as itself a sign of rigor, when the test is whether the formalism proves something the prose claim didn't already establish.

### Statistical vs. practical significance

A p-value below threshold says an effect is unlikely to be pure noise given the sample; it says nothing about whether the effect size is large enough to matter for the claim being made. The two are independent axes, not a spectrum.
**In use:** "p < 0.01, but the effect is a 0.3-point gain on a 100-point scale — statistically real, practically negligible for the claimed use case."
**Common misuse:** Reporting a low p-value as if it settles whether a result is "significant" in the everyday sense of important, without separately reporting or reasoning about effect size.

### Speculation vs. explanation

Explanation is a causal account backed by controlled evidence (an ablation, a mechanism test); speculation is a plausible-sounding causal story offered without that evidence — a distinct register a draft must mark, per Lipton & Steinhardt, rather than blend into declarative prose.
**In use:** "We think the gain comes from better gradient flow — flag that as speculation, we haven't run the probe that would show it."
**Common misuse:** Writing a plausible mechanism in the same declarative voice as an established result, letting the reader infer it was tested when it was only hypothesized.

### Novelty (component vs. system)

Whether the *specific proposed idea* — isolated from every other change riding alongside it (data, tuning, scale, engineering) — is what's new, as opposed to the system as a whole being new because of an accumulation of untested auxiliary changes.
**In use:** "The pipeline is new, sure, but is the attention mechanism itself novel, or is that the part that's actually prior work with new hyperparameters?"
**Common misuse:** Claiming novelty for the paper's headline component when the actual delta from prior work is concentrated in incidental engineering choices the ablation hasn't separated out.

### Confound

A variable that changed alongside the variable of interest and offers an alternative explanation for the observed effect, making the causal attribution ambiguous unless it's controlled for or ruled out.
**In use:** "Training compute went up at the same time as the architecture change — that's a confound until we hold compute fixed."
**Common misuse:** Using "confound" loosely to mean any source of noise or uncertainty, rather than its specific meaning — a *co-varying* alternative cause that could produce the same result.

### IRB-equivalent review

A project-specific ethics and consent review process for a study involving human subjects' behavior or data, distinct from and not satisfied by a platform's general terms-of-service — the review is scoped to the specific intervention, not the platform's blanket data-use permission.
**In use:** "The platform's ToS covers general data use, but we still need IRB-equivalent sign-off — this experiment manipulates what users see."
**Common misuse:** Treating "users already agreed to the ToS" as sufficient ethical cover for an experiment that manipulates behavior or emotional state in ways the ToS was never scoped to anticipate.

### Broader Impacts (NSF)

A separately labeled statement in an NSF proposal addressing the societal benefit of the proposed work — distinct from, and not satisfied by, folding societal-benefit language into the Intellectual Merit narrative as unlabeled prose.
**In use:** "Broader Impacts needs its own labeled section — right now it's a paragraph buried inside Intellectual Merit, and that's a formatting rejection risk."
**Common misuse:** Treating Broader Impacts as a rhetorical flourish woven through the proposal rather than a mechanically separate, explicitly labeled section a program officer checks for before reading substance.

### Effect size

The magnitude of a measured difference (e.g., percentage points, Cohen's d), reported independent of whether that difference cleared a significance threshold — the number a reader needs to judge practical importance, which a p-value alone cannot supply.
**In use:** "State the effect size in the abstract, not just significant/not significant — a reviewer can't judge importance from a p-value alone."
**Common misuse:** Omitting effect size and reporting only significance, leaving the reader unable to distinguish a large practically important gain from a tiny but statistically detectable one.

### Overfitting to the benchmark

A model or method improving on a specific benchmark's test set in ways that don't transfer to the underlying capability the benchmark was meant to proxy — often via repeated benchmark-driven iteration (implicit test-set leakage) rather than a genuine capability gain.
**In use:** "We've iterated against this benchmark for six months — check on a held-out benchmark before claiming the capability generalizes."
**Common misuse:** Treating state-of-the-art on one benchmark as direct evidence of the general capability it was designed to measure, without checking transfer to a different benchmark or distribution.
