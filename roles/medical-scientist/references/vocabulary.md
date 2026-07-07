# Medical Scientist — Vocabulary

### EC50 / IC50
The concentration of a compound producing 50% of its maximal effect (EC50, effective concentration) or 50% inhibition (IC50). Derived from fitting a dose-response curve, not read directly off raw data.
**In use:** "The curve didn't reach a top plateau, so that EC50 is extrapolated — we need two more doses before I trust the number."
**Common misuse:** Treated as a directly measured value rather than a fitted parameter that requires the curve to reach both asymptotes to be reliable.

### Z'-factor
A statistic quantifying a screening assay's signal-to-noise separation between positive and negative controls on a given run, used to qualify whether that run's data is trustworthy.
**In use:** "Z' was 0.71 on this plate — the assay's qualified, we can trust the hit calls."
**Common misuse:** Cited from the assay's historical best performance rather than computed for the specific run whose data is being used.

### Biological replicate vs. technical replicate
Biological replicates are independent samples (separate animals, separate cell passages); technical replicates are repeated measurements of the same sample. They estimate different sources of variance.
**In use:** "That's three technical replicates on one cell passage — we don't have biological n yet."
**Common misuse:** Averaging technical replicates and reporting the count as biological n, understating true variance.

### GLP (Good Laboratory Practice)
A regulatory quality-system standard (21 CFR Part 58) for the conduct, documentation, and QA oversight of studies intended to support a regulatory submission. Distinct from general good scientific practice.
**In use:** "This tox study needs to run GLP — it's going in the IND package."
**Common misuse:** Treated as a general quality bar for "rigorous" science rather than a specific regulatory-submission requirement that doesn't apply to exploratory work.

### Dose-response curve
A plot of measured effect against compound concentration, typically fit with a four-parameter logistic model to extract EC50/IC50, Hill slope, and top/bottom asymptotes.
**In use:** "The Hill slope is way steeper than expected for a simple competitive mechanism — worth checking for cooperative binding or an assay artifact."
**Common misuse:** Reduced to just the EC50 number, discarding the shape information (plateau, slope) that signals whether the fit is trustworthy.

### Target engagement
Direct evidence that a compound is physically interacting with its intended target in a relevant system (cell or tissue), distinct from downstream functional effect.
**In use:** "We've shown target engagement in the cell assay — efficacy in the tumor model is the next question."
**Common misuse:** Used interchangeably with "efficacy," collapsing two distinct evidence tiers into one claim.

### PK/PD (pharmacokinetics/pharmacodynamics)
PK describes how a compound's concentration changes over time in the body (absorption, distribution, metabolism, excretion); PD describes the relationship between that concentration and its biological effect.
**In use:** "The PK/PD disconnect is the problem — plasma levels peak at 2 hours but the pathway readout doesn't move until 8."
**Common misuse:** Treated as a single combined metric rather than two separate measurements whose relationship (or lack of one) is itself the finding.

### Blinding
Concealing treatment-group assignment from the person scoring an outcome, to prevent expectation bias from influencing subjective measurements.
**In use:** "Histopathology scoring was done blind — the pathologist didn't see the treatment key until after grading."
**Common misuse:** Assumed to apply only to human clinical trials; skipped in preclinical studies with subjective endpoints where it matters just as much.

### Xenograft / syngeneic / PDX model
In vivo tumor models: xenograft implants human tumor cells into immunodeficient mice; syngeneic implants mouse tumor cells into immunocompetent mice (preserves immune system interactions); PDX (patient-derived xenograft) implants a patient tumor sample directly, preserving tumor heterogeneity.
**In use:** "We need a syngeneic model for this immuno-oncology compound — a xenograft in immunodeficient mice can't show us the immune-mediated effect."
**Common misuse:** Model choice treated as interchangeable rather than determined by whether the mechanism being tested requires an intact immune system.

### Tumor growth inhibition (TGI)
A percentage measure comparing treated-group tumor volume to control-group tumor volume at a fixed timepoint, used as a standard in vivo efficacy endpoint.
**In use:** "40% TGI at day 21 met our threshold, but the tumors regrew by day 35 — durability, not just peak effect, is the real question."
**Common misuse:** Reported as a single peak-timepoint number without checking whether the effect is durable or just a transient growth delay.

### Positive/negative control
A known-active or known-inactive reference included in every experimental run to validate that the assay is behaving as expected on that specific run.
**In use:** "The positive control didn't hit its expected window today — we're re-running the plate, not trusting these results."
**Common misuse:** Included in the protocol but not actually checked against historical performance before interpreting the experimental data from that run.

### Off-target effect
An observed biological effect caused by the compound acting on something other than its intended target, which can produce a real but misleading result.
**In use:** "The effect held at high concentration but vanished with the more selective analog — that's an off-target signature, not on-target pharmacology."
**Common misuse:** Ruled out by assumption rather than by testing a more selective compound or a genetic knockout/knockdown control.

### Geometric mean (for EC50/IC50 reporting)
The mean calculated on the log scale (or equivalently, the nth root of the product of n values), appropriate for log-normally distributed potency data.
**In use:** "Report the geometric mean IC50 across replicates, not the arithmetic mean — these values span more than 3x."
**Common misuse:** Arithmetic mean used by default, which skews high and misrepresents central tendency for log-distributed potency values.
