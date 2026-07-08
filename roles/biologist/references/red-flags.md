# Red flags

### N reported as "number of measurements" rather than number of independently randomized units
- **Usually means:** repeat weighings, repeat imaging passes, or multiple offspring/cells from the same litter/culture well are being counted as independent data points — pseudoreplication.
- **First question:** "At what level was treatment actually randomized — dam, cage, well, or plot — and how many of those units are there?"
- **Data to pull:** the randomization log or treatment-assignment sheet showing which physical units received which treatment.

### No power calculation reported, or sample size described only as "consistent with prior lab practice"
- **Usually means:** N was set by convention, budget, or animal availability, not by a stated effect size and power target.
- **First question:** "What effect size and power was this N calculated to detect, and can you show the calculation?"
- **Data to pull:** the power-analysis worksheet or software output (G*Power log, `pwr` script) dated before data collection began.

### A "no significant difference" result with no achieved-power statement
- **Usually means:** the study was underpowered to detect the effect size that would have mattered, and a null result is being reported as if it meant "no effect."
- **First question:** "At this N, what power did the study actually have to detect the pre-specified effect size?"
- **Data to pull:** post hoc achieved-power calculation using the actual N and the originally stated (not post hoc chosen) effect size.

### Single-cohort positive result described as an established finding, with no independent replication
- **Usually means:** one lab, one cohort, one p-value below 0.05 is being treated as proof rather than as a hypothesis that has cleared a single bar.
- **First question:** "Has this been independently replicated in a separate cohort or a different lab?"
- **Data to pull:** the manuscript's methods/discussion section for any replication cohort, and a literature check for independent confirmation.

### Data collection start date predates the IACUC/IBC/permit approval date
- **Usually means:** work began under schedule or funding-deadline pressure before the required protocol was approved, making the data unusable regardless of quality.
- **First question:** "What is the approval date on the protocol, and what is the first data-collection timestamp in the notebook?"
- **Data to pull:** the IACUC/IBC approval letter (with protocol number and effective date) and the lab notebook's first dated entry.

### "Reduction" cited to justify an N that traces back to a budget line, not a variance-reduction step
- **Usually means:** the 3Rs framework is being invoked post hoc to rationalize an underpowered design rather than describing an actual step taken to shrink variance (better controls, repeated-measures design, tighter protocol).
- **First question:** "What specific design change reduced variance enough to justify this N at the target power?"
- **Data to pull:** the IACUC protocol's statistical-justification section and any pilot-study variance estimate used in the power calculation.

### Analysis run on pooled raw measurements instead of unit-level means or a mixed-effects model
- **Usually means:** the statistical model doesn't match the design's cluster structure (litter, cage, plot, site), inflating degrees of freedom and shrinking p-values artificially.
- **First question:** "Is litter/cage/plot entered as a random effect, or are all raw measurements pooled as if independent?"
- **Data to pull:** the analysis script or statistical output showing the model specification (fixed and random effects).

### Federal wildlife-collecting permit application submitted less than 30 days before planned field start
- **Usually means:** state scientific-collector permits are being requested before the required federal permit is on file, which will delay or block the state approval and the whole field season.
- **First question:** "Is the federal USFWS (or equivalent) permit already approved, and when was it submitted relative to the state application?"
- **Data to pull:** USFWS ePermits submission and approval timestamps, cross-checked against the state permit application date.

### Manuscript or press summary states a single-study result as "scientists have shown" or "proves"
- **Usually means:** normal single-study uncertainty is being flattened into certainty language for a broader audience, ahead of replication.
- **First question:** "Does the underlying claim rest on one study, and does the language reflect that?"
- **Data to pull:** the press release or abstract text alongside the number of independent studies/cohorts actually supporting the claim.

### Effect size used in the power calculation was chosen after seeing pilot or preliminary data with no adjustment
- **Usually means:** an optimistic effect size from a small, noisy pilot is being carried into the main study's power calculation, understating the true required N.
- **First question:** "Was the effect size for this calculation pre-registered or literature-derived, or is it the pilot's observed effect taken at face value?"
- **Data to pull:** the pilot dataset's sample size and confidence interval on the effect estimate used.

### Blinding and randomization are described in the methods but not documented at the point of data collection
- **Usually means:** blinding/randomization was intended but reconstructed after the fact rather than logged contemporaneously, so it can't be verified against a bias claim.
- **First question:** "Where in the notebook is the randomization sequence or blinding key recorded, and when was it generated relative to data collection?"
- **Data to pull:** the dated randomization/blinding log or code-generation script, compared against the data-collection timestamps.

### More than one manuscript revision changes the stated primary outcome or effect size after the fact
- **Usually means:** outcome switching — the analysis was run on multiple endpoints and the one that reached significance was promoted to "primary" after seeing the results.
- **First question:** "What was the pre-specified primary outcome, and does it match what's reported as primary in this draft?"
- **Data to pull:** the original protocol, pre-registration, or grant aims page listing the primary outcome before data collection.
