# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

## Statistical significance vs practical significance

- **Definition:** statistical significance says the observed effect is unlikely under the null (given the sample size); practical significance says the effect is big enough to matter for the decision.
- **Practitioner usage:** "It's significant at p = 0.01 but the lift is 0.15% on a metric where we need 2% to cover the maintenance cost — significant, not practical, don't ship."
- **Common misuse:** treating "significant" as "important." With 10M users per arm, a 0.05% lift will be highly significant and completely worthless; with 500 users, a genuinely large effect can be "not significant." Significance is a function of n as much as of the effect.

## Power vs confidence

- **Definition:** confidence level (1 − α) controls false positives — how often you'd cry wolf when there's no effect. Power (1 − β) controls false negatives — how often you'd detect an effect of a given size when it's really there.
- **Practitioner usage:** "We're at 80% power for a 5% relative lift — if the true effect is 2%, this test will probably miss it, and a null result won't mean much."
- **Common misuse:** reading a non-significant result from an underpowered test as "we proved there's no effect." Absence of evidence at 30% power is very close to no information at all.

## Correlation vs causation (product-data edition)

- **Definition:** correlation is co-movement; causation is what happens to Y when you intervene on X.
- **Practitioner usage:** "Users with the app installed retain 2× better — that's who chooses to install the app, not what the app does. We need a randomized prompt experiment to size the causal part."
- **Common misuse:** the standard product trap is "users who do X retain better → make everyone do X." Power users do everything more, so *every* feature correlates with retention. Feature-engagement correlations are close to worthless for roadmap decisions without an experiment or a credible identification strategy.

## Selection bias vs confounding

- **Definition:** selection bias — who ends up in your dataset (or arm) is related to the outcome; the sample misrepresents the population. Confounding — a third variable drives both the exposure and the outcome within the sample.
- **Practitioner usage:** "The NPS survey has selection bias — angry and delighted users respond, the middle doesn't. And the retention comparison is confounded by tenure: older accounts both use the feature more and retain better."
- **Common misuse:** using the terms interchangeably, which matters because the fixes differ — selection bias needs better sampling or reweighting; confounding needs randomization or adjustment for the confounder. Adjusting can't fix a sample that never contained the missing people.

## Precision vs recall vs the base rate

- **Definition:** precision — of everything flagged, how much is truly positive. Recall — of everything truly positive, how much got flagged. Both are meaningless for decisions without the base rate.
- **Practitioner usage:** "At a 1% fraud base rate, a classifier with 90% recall and 90% specificity still flags ~11 legitimate orders for every fraud caught — precision is only ~8%. Can ops handle that queue?"
- **Common misuse:** quoting "90% accurate" for a rare-event model (see red-flags.md), or tuning precision and recall in the abstract without asking what a false positive and a false negative each cost the business. The threshold is a business decision, not a modeling one.

## Point estimate vs interval

- **Definition:** the point estimate is the single best guess; the interval is the range of values compatible with the data at a stated confidence level.
- **Practitioner usage:** "Lift is +3% (95% CI −1% to +7%) — the interval includes zero, so 'the test showed +3%' overstates what we know. Decide as if the true value could be anywhere in that range."
- **Common misuse:** stripping the interval when the number travels upward in the org. "+3%" in the exec deck becomes a commitment; "+3% ± 4%" was information. Also: reporting 12.37% from a sample whose interval spans six points — precision theater.

## HARKing (Hypothesizing After the Results are Known)

- **Definition:** presenting a hypothesis discovered in the data as if it were predicted in advance.
- **Practitioner usage:** "Interesting subgroup result — but that's HARKed; log it as hypothesis-generating and we'll pre-register it for the next test."
- **Common misuse:** the readout that says "as expected, the effect concentrated in new mobile users" when nobody expected that before the data came in. HARKing converts exploratory noise into false confirmatory evidence, and it usually isn't dishonesty — it's memory quietly rewriting itself. Timestamped analysis plans exist because of this.

## Degrees of freedom (analytic / researcher)

- **Definition:** beyond the formal statistical quantity, "researcher degrees of freedom" are all the defensible-seeming choices in an analysis — metric definition, outlier rule, time window, segment, model spec — each of which nudges the result.
- **Practitioner usage:** "Between three exclusion rules, four windows, and two metric definitions, that's 24 versions of this analysis. Which was decided before looking at the outcome? Show me the sensitivity across the others."
- **Common misuse:** believing an analysis is objective because each individual choice was defensible. With enough forking paths you can reach p < 0.05 from pure noise without ever consciously cheating (Gelman & Loken's "garden of forking paths"). The tell of a trustworthy analysis is that it shows its conclusion is robust across the reasonable alternatives, not that it found one path to significance.
