# Analysis Playbook

Operational playbooks with concrete steps and thresholds. These are defaults, not laws — but deviate consciously and say why in the writeup.

## 1. Experiment design + readout checklist

### Before launch

1. **Pre-register the hypothesis.** One primary metric, 2–4 guardrails, direction predicted. Everything else is exploratory and gets labeled as such in the readout.
2. **Power calculation — with real numbers, not vibes.** Example: baseline conversion 4.0%, minimum detectable effect (MDE) you'd actually act on = 5% relative (4.0% → 4.2%, absolute delta 0.2pp). With alpha = 0.05 two-sided and power 0.80:

   n per arm ≈ 2 × (z_0.975 + z_0.8)² × p(1−p) / δ² = 2 × (1.96 + 0.84)² × 0.04 × 0.96 / 0.002² ≈ **150,500 per arm**.

   At 100k eligible users/week split 50/50, that's ~3 weeks. If the PM wants an answer in 1 week, the honest options are: accept an MDE around 8–9% relative, find more traffic, or don't run it. Do not run underpowered and "see what happens" — an underpowered significant result has an inflated effect size (winner's curse) and a real chance of being sign-flipped.
3. **Fix the duration up front and commit.** Minimum one full weekly cycle (7 days), ideally two, to wash out day-of-week mix. No stopping early on a good p-value unless you pre-registered a sequential design (mSPRT, group-sequential bounds) — optional stopping under fixed-horizon stats is p-hacking with extra steps.
4. **Define exposure correctly.** Analyze users at the point of assignment (intention-to-treat), not at the point of feature usage. Conditioning on post-assignment engagement reintroduces the selection bias randomization exists to remove.

### At readout — gates in order; each must pass before the next number means anything

1. **SRM (sample ratio mismatch).** Chi-square goodness-of-fit of observed arm counts vs planned split. **Threshold: p < 0.001 → stop; the experiment is invalid.** Do not "note it and continue." Common causes: redirect-based assignment losing slow clients asymmetrically, bot filtering applied to one arm only, assignment logged after a crash-prone code path.
2. **Instrumentation sanity.** Per-user event volume per arm within ~1% for events the treatment shouldn't affect. Treatments that change page structure silently change event firing.
3. **Primary metric with CI, not just p.** Report "orders/user +2.1% (95% CI +0.6% to +3.6%)", never "+2.1%***".
4. **Guardrails.** Latency, crash rate, unsubscribes, long-horizon retention/repeat rate. A primary win with a tanked guardrail is "no" or "rework", not "ship with monitoring."
5. **Novelty/decay check.** Lift by days-since-first-exposure. If week-2 lift is under half of week-1 lift, steady state is materially smaller than the headline; extend the test or discount the number.
6. **Segments.** Only pre-registered segments are confirmatory. For exploratory digging, apply Bonferroni or Benjamini–Hochberg across everything examined and label results "hypothesis-generating."

### When to trust p = 0.03

p = 0.03 is weak evidence, not proof. Trust it more when the hypothesis was pre-registered and singular, the test was adequately powered, the effect size is plausible (a 40% lift from a button color is not), and it replicates directionally in a holdback. Trust it less when it's one of 15 metrics examined, the test was peeked at daily, or n is small. Under realistic prior odds that a typical product hypothesis is true (~1 in 3), p ≈ 0.03 corresponds to a false-positive risk around 20–30%, not 3%. One replication is worth ten asterisks.

## 2. Metric investigation: "metric X dropped 8%"

The actual triage order — cheapest and most likely explanations first. Most "drops" die at step 1 or 2.

1. **Instrumentation first (~half of all cases).** Check raw event volume for the underlying events, not the derived metric. Did a deploy ship near the inflection? Diff the event schema; check SDK version mix — a drop concentrated in one app version is a logging bug, not behavior. Check the ETL: late-arriving data makes the most recent 1–2 days always look down; never alert on a partial day.
2. **Definition/pipeline change.** Did anyone change the metric definition, a dimension table, a join, timezone handling, or bot filtering upstream? `git log` the dbt models feeding the metric for the two weeks before the drop.
3. **Mix shift.** Decompose: is the rate down within segments, or did the mix move toward low-rate segments? Cut by platform, geo, acquisition channel, new-vs-returning. Blended conversion down with every segment flat = mix shift (usually a marketing spend change), and the fix isn't a product fix.
4. **Seasonality/calendar.** Compare year-over-year and same-weekday, not to yesterday. Check holidays in top geos, school terms, paydays, and — perennially — daylight-saving boundaries breaking hour-based joins.
5. **Real effect last.** Only after 1–4 are excluded: correlate the inflection with product/pricing/competitor changes, find the funnel step where the loss concentrates, and check for overlapping experiment ramps (a 20% ramp of a −5% treatment moves the global metric −1%).

Write the finding as: what moved, when (to the day/hour), where it's concentrated, what's ruled out, best remaining explanation, confidence.

## 3. Causal inference when A/B is impossible

In order of preference:

- **Difference-in-differences** — treated and untreated groups observed before and after (e.g., feature launched in Germany only). **Requires parallel trends:** plot 8+ pre-periods; if pre-trends diverge, stop. Failure modes: an event hitting one group only during the window; treatment timing chosen *because* the group was trending (Ashenfelter dip). Cluster standard errors at the unit of treatment.
- **Synthetic control** — one (or few) treated units, many candidate controls (one country, one large customer). Build a weighted donor combination matching the pre-period; the post-period gap is the effect. Validate with placebo tests on donor units — if fake treatments show "effects" as large as the real one, you have nothing. Fails with short pre-periods (<12 points) or when no donor combo tracks the pre-trend.
- **Regression discontinuity** — treatment flips at a sharp threshold on a running variable (credit score ≥ 640, spend ≥ $100 for free shipping). Compare units just above vs just below. **Check manipulation:** McCrary density test at the cutoff — if units can precisely sort themselves across it (they will, if money is on the line), RDD is dead. Estimates are local to the threshold; don't extrapolate.
- **Propensity/matching methods** — last resort. They adjust only for *observed* confounders, which is exactly the assumption randomization exists to avoid. Fine for descriptive sizing; never sufficient alone for a ship/no-ship claim.

Every observational writeup names its identifying assumption in one sentence, plus what would violate it. If you can't write that sentence, you don't have a design — you have a regression.

## 4. Should this even be a model?

A gate, in order — a "no" at any step ends the project:

1. **Is there a decision and an action?** Who receives the prediction, what do they do differently at score 0.9 vs 0.2, what does the action cost? "It would be interesting" fails.
2. **Does a rule get 80% of the value?** "Flag accounts with no login in 30 days" often captures most of a churn model's actionable signal, ships in a day, and is debuggable by anyone. Build the model only if the rule demonstrably leaves money on the table.
3. **Is the label real?** "Churn" defined how, at what horizon, observable without waiting six months? A model with a proxy label optimizes the proxy.
4. **Does the intervention work?** A perfect churn predictor attached to an ineffective win-back email is worth $0. If untested, run the intervention experiment on a rule-based segment first.
5. **Is fresh, leak-free data available at scoring time?** Features present in the warehouse at training time but unavailable (or only post-outcome) at decision time are the most common silent killer.
6. **Who owns it in month 6?** Retraining cadence, drift monitoring, a named owner. No owner → it rots, silently.

If all six pass: start with logistic regression or gradient-boosted trees on 10–20 features, ship it behind the decision, and only then discuss anything fancier.
