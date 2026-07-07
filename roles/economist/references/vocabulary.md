# Economist — Vocabulary

### Elasticity
The percentage change in a dependent variable (quantity demanded) per 1% change in an independent variable (price), holding other factors fixed.
**In use:** "The elasticity is -1.2, so a 10% price increase costs us about 12% of volume."
**Common misuse:** treating a single elasticity as a constant that applies at any magnitude of price change, when it's a local estimate fit near the observed price range.

### Identification strategy
The specific argument for why an observed correlation reflects a causal effect — the natural experiment, instrument, or discontinuity that isolates the treatment from confounders.
**In use:** "Our identification strategy is the staggered metro rollout — it gives us a difference-in-differences design with a clean control group."
**Common misuse:** running a regression and calling the coefficient "the effect" without naming what would have to be true (no omitted confounders, no reverse causation) for that interpretation to hold.

### Difference-in-differences (DiD)
A design comparing the change over time in a treated group against the change over the same period in an untreated control group, isolating the treatment effect from common trends.
**In use:** "DiD gives us -1.2 once we net out the control metros' organic growth."
**Common misuse:** applying it when the pre-treatment trends visibly diverge — the method assumes parallel trends absent treatment, and it's an assumption to test, not a formality to skip.

### Regression discontinuity (RD)
A design exploiting a sharp, arbitrary threshold in assignment (an eligibility cutoff) to compare units just above and just below it, which are treated as as-good-as-randomly assigned near the cutoff.
**In use:** "Since eligibility cuts off at a 680 credit score, we can RD around that threshold."
**Common misuse:** trusting the design without checking for manipulation (bunching) of the running variable near the cutoff, which invalidates the as-good-as-random assumption.

### Instrumental variable (IV)
A variable correlated with the treatment but uncorrelated with the outcome except through the treatment, used to isolate causal variation when treatment is otherwise confounded.
**In use:** "Rainfall on election day is our instrument for turnout — it affects turnout but shouldn't otherwise affect policy views."
**Common misuse:** using a weak instrument (low first-stage correlation with treatment) without reporting the first-stage F-statistic, which can produce a badly biased and falsely precise estimate.

### Natural experiment
A real-world event or policy that creates as-good-as-random variation in treatment without the researcher designing an RCT.
**In use:** "The staggered price rollout across metros was a natural experiment we could exploit."
**Common misuse:** calling any before/after comparison a "natural experiment" when there was no meaningfully random or exogenous assignment mechanism — most before/after comparisons are not natural experiments.

### Statistical significance vs. economic significance
Statistical significance measures whether an effect is distinguishable from zero given sampling noise; economic significance measures whether the effect size is large enough to matter for the decision.
**In use:** "It's statistically significant at p<0.01, but at 0.3% of revenue it's not economically significant enough to act on."
**Common misuse:** treating a low p-value as sufficient justification to act, without separately checking the magnitude against the cost of acting.

### Confidence interval
A range constructed from the data such that, under repeated sampling, it would contain the true parameter at the stated rate (e.g., 95%).
**In use:** "The 95% CI is -1.5 to -0.9 — the point estimate of -1.2 isn't the only plausible value."
**Common misuse:** reporting only the point estimate and dropping the interval in the final deliverable, which transfers unstated estimation risk to the decision-maker.

### Parallel trends assumption
The core assumption behind difference-in-differences: absent treatment, the treated and control groups would have moved in parallel.
**In use:** "We plotted six months of pre-period data to check parallel trends before trusting the DiD estimate."
**Common misuse:** assuming it holds by default rather than testing it against pre-treatment data — it is the single most commonly violated assumption in applied DiD work.

### Selection bias
Bias introduced when the treated group differs systematically from the control group for reasons related to the outcome, typically because units self-selected into treatment.
**In use:** "Early adopters aren't a random sample — comparing them to non-adopters overstates the effect because of selection bias."
**Common misuse:** assuming any observational comparison is selection-bias-free simply because the sample size is large — sample size doesn't fix a biased sampling mechanism.

### Deadweight loss
The loss of total economic surplus (consumer plus producer) caused by a market distortion, such as a tax or a price set away from the market-clearing level.
**In use:** "The proposed tax raises $4M in revenue but creates roughly $600K in deadweight loss from reduced transaction volume."
**Common misuse:** treating any transfer (e.g., a tax that moves money from buyers to the government) as deadweight loss, when only the reduction in transaction volume itself represents lost surplus.

### Heterogeneous treatment effect
A treatment effect that varies systematically across subgroups, rather than applying uniformly.
**In use:** "The blended elasticity is -1.2, but it's heterogeneous — the price-sensitive quartile is -2.1 and the rest are -0.85."
**Common misuse:** reporting only the average treatment effect when the policy decision would change if the heterogeneity were disclosed (a segment for whom the sign flips).

### Synthetic control
A method for constructing a counterfactual for a single treated unit (one market, one country) by weighting untreated units to match its pre-treatment trajectory.
**In use:** "With only one treated market, we built a synthetic control from a weighted basket of five comparable markets."
**Common misuse:** using it with too few pre-treatment periods to establish a credible match, producing a counterfactual that fits noise rather than the true underlying trend.

### Reverse causation
When the presumed effect variable actually influences the presumed cause variable, inverting the intended causal story.
**In use:** "Higher marketing spend correlates with higher revenue, but it's plausible causation runs the other way — successful periods get bigger marketing budgets."
**Common misuse:** ruling out reverse causation by assumption rather than by design (timing structure, instrument, or experiment that fixes the direction).
