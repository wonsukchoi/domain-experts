# Economist — Red Flags

### A "before/after" comparison with no named control group
- **Usually means:** the analysis is conflating the treatment effect with everything else that changed over the same window — seasonality, a macro shift, a competitor's move.
- **First question:** "What would have happened to this metric if nothing had changed — what's the counterfactual?"
- **Data to pull:** a comparable untreated group or market over the same window; if none exists, a synthetic control built from a weighted combination of untreated units.

### Elasticity or treatment-effect estimate reported with no confidence interval or standard error
- **Usually means:** either the interval wasn't computed, or it was wide enough that reporting it would undercut the headline number.
- **First question:** "What's the standard error, and how many independent units (not observations) is this estimated on?"
- **Data to pull:** the regression output table with SEs; the count of independent clusters (metros, cohorts, firms) — not the raw observation count, which overstates precision under clustering.

### Statistical significance (p < 0.05) cited as the reason to act
- **Usually means:** the analyst is substituting statistical significance for economic significance — a real but tiny effect.
- **First question:** "What's the effect size in the decision's units (dollars, users), and is it big enough to matter net of implementation cost?"
- **Data to pull:** the point estimate converted to the decision-relevant unit, plus the cost of acting on it.

### Difference-in-differences design with no pre-treatment trend check
- **Usually means:** the parallel-trends assumption hasn't been verified — the treated and control groups may have already been diverging before the intervention, which the post-period comparison will misattribute to treatment.
- **First question:** "What did the treated and control groups look like for the 6-12 months before treatment — were they moving in parallel?"
- **Data to pull:** a pre-period trend plot, treated vs. control, at least 2x the length of the post-period window.

### An elasticity estimated at a 10% price change applied to project the impact of a 40%+ change
- **Usually means:** the model is extrapolating a local slope well outside its estimated range, where substitution behavior can kink.
- **First question:** "Has demand response ever been observed at anywhere near this magnitude of change?"
- **Data to pull:** the full historical range of price changes in the source data; if the proposed change is outside that range, flag the extrapolation explicitly rather than reporting a point estimate with false precision.

### A regression-discontinuity design where the running variable shows bunching just on one side of the cutoff
- **Usually means:** agents are manipulating which side of the threshold they land on (e.g., self-reporting income just under an eligibility cutoff), which breaks the "as-good-as-random" assumption at the threshold.
- **First question:** "Is there a McCrary density test or histogram showing smooth density through the cutoff?"
- **Data to pull:** the density of the running variable in a narrow band around the cutoff.

### An aggregate/blended result presented without a segment breakdown
- **Usually means:** the average is masking a heterogeneous effect — a subgroup for whom the sign of the effect flips.
- **First question:** "Does this result hold across the segments most likely to respond differently (price-sensitive vs. not, new vs. tenured, geography)?"
- **Data to pull:** the same estimate re-run on the 2-3 segments most plausibly heterogeneous.

### A forecast presented as a single number with no scenario range
- **Usually means:** the uncertainty was computed and dropped before the final deliverable, or never computed.
- **First question:** "What's the range under the upper- and lower-bound assumptions, and what would have to be true for the low/high case?"
- **Data to pull:** the sensitivity table varying the 1-2 highest-leverage assumptions.

### A sample where the treated group self-selected into treatment (opted in, applied, early-adopted)
- **Usually means:** the measured "effect" partly reflects who chose to be treated, not the treatment itself.
- **First question:** "Why did the treated group end up treated — was assignment close to random, or did they choose in?"
- **Data to pull:** baseline (pre-treatment) characteristics of the treated vs. control group, checked for balance.
