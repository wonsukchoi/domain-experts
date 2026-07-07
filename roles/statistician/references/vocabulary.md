# Vocabulary

### Statistical power
The probability that a test correctly detects a true effect of a specified size, given the sample size and significance threshold — conventionally targeted at 80% or 90%.
**In use:** "This study was powered at 80% to detect a 10% relative lift — if the true effect is smaller than that, we'd likely miss it even though it's real."
**Common misuse:** Treating "underpowered" and "no effect" as the same conclusion — an underpowered null result means the study couldn't reliably detect the effect size in question, not that no effect exists.

### p-value
The probability of observing data at least as extreme as what was measured, assuming the null hypothesis is true — not the probability the null hypothesis itself is true.
**In use:** "p=0.03 means, under the assumption of no true effect, we'd see a difference this large or larger 3% of the time by chance alone."
**Common misuse:** Interpreting p-value as "the probability the result is due to chance" or "the probability the null hypothesis is true" — both are inversions of what a p-value actually conditions on.

### Multiple comparisons problem
The inflation of the overall false-positive rate that occurs when many hypothesis tests are run and each is evaluated at the same nominal significance threshold without adjustment.
**In use:** "We ran 20 subgroup tests at α=0.05 uncorrected — the chance at least one comes back 'significant' by pure chance is already around 64%."
**Common misuse:** Assuming correction is only needed for tests explicitly labeled as a "multiple testing" study — any set of tests examined for the same underlying question (including unreported exploratory ones) contributes to the true error rate.

### MCAR / MAR / MNAR (missing data mechanisms)
Missing Completely At Random (missingness unrelated to any variable), Missing At Random (missingness depends only on observed variables), Missing Not At Random (missingness depends on the unobserved value itself).
**In use:** "Dropout correlates with baseline severity, which we did observe — that's MAR, not MCAR, so we can condition on severity in the imputation model."
**Common misuse:** Defaulting to MCAR because it's the simplest case to analyze (complete-case deletion is unbiased under MCAR) — MCAR is a strong, testable-in-part assumption, not a safe default.

### Confidence interval
A range constructed such that, under repeated sampling, the stated percentage (e.g. 95%) of such intervals would contain the true parameter value.
**In use:** "The 95% CI for the lift is [0.4%, 2.1%] — even the low end is a meaningful improvement, which the point estimate alone wouldn't tell you."
**Common misuse:** Stating "there's a 95% probability the true value is in this interval" for a single computed interval — the 95% describes the long-run procedure across repeated samples, not a probability statement about this specific fixed interval.

### Effect size
A standardized or raw measure of the magnitude of a difference or relationship, distinct from and reported alongside statistical significance.
**In use:** "The effect is significant at p<0.01, but Cohen's d is 0.08 — that's a trivial effect size regardless of the p-value."
**Common misuse:** Omitting effect size entirely and treating a significant p-value as sufficient evidence that an effect matters practically.

### Randomized controlled trial (RCT) vs. observational study
An RCT assigns treatment via randomization, supporting causal claims; an observational study measures existing group differences, supporting association claims only (absent strong identification assumptions).
**In use:** "This is an observational cohort, not an RCT — we can report the association, but calling it causal would need to defend against confounding by indication."
**Common misuse:** Using causal language ("X reduces Y") for observational findings without a design or method (instrumental variables, regression discontinuity) that specifically addresses confounding.

### Alpha-spending function
A pre-specified rule for how much of the total significance threshold (alpha) is "spent" at each interim look in a sequential trial, so cumulative false-positive risk across all looks stays at the nominal level.
**In use:** "We're using an O'Brien-Fleming alpha-spending boundary, so the interim look only gets to spend α≈0.003 — that's why it looks so conservative at the first check."
**Common misuse:** Checking a live experiment repeatedly against a flat 0.05 threshold at every look and calling it a "sequential design" — without an actual spending function, repeated 0.05 checks inflate the true error rate.

### Winner's curse
The tendency for an effect estimate that just barely cleared a significance threshold (especially in an underpowered study) to overestimate the true effect size.
**In use:** "It's underpowered and just barely significant — expect the replication effect size to be smaller; this is a textbook winner's-curse setup."
**Common misuse:** Treating a barely-significant result from a small study as a solid estimate of effect magnitude, rather than recognizing that conditioning on significance in a low-power design systematically inflates the observed effect.

### Type I / Type II error
Type I: rejecting a true null hypothesis (false positive). Type II: failing to reject a false null hypothesis (false negative, related to 1 − power).
**In use:** "Lowering α to reduce Type I error without increasing sample size just trades it for a higher Type II error rate — power drops."
**Common misuse:** Discussing only Type I error control (significance level) while ignoring that tightening it, holding sample size fixed, directly increases Type II error / reduces power.
