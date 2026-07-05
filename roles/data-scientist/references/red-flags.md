# Red Flags

Smell tests for analyses, models, and dashboards. Format per flag: what it usually means, the first question to ask, the check to run.

## The dashboard nobody actioned

- **Usually means:** the metric isn't attached to a decision, or nobody trusts the number. Dashboards are exhaust; decisions are the product.
- **First question:** "What was the last decision anyone made differently because of this dashboard?"
- **Check:** pull view logs for 30 days. If views cluster around QBR prep and nothing else, it's reporting theater — archive it or attach a threshold + owner + action to each metric.

## 94% accuracy on a 95/5 imbalanced class

- **Usually means:** the model learned to predict the majority class. Predicting "not fraud" for everyone scores 95% on a 95/5 split; 94% is *worse* than the trivial baseline.
- **First question:** "What's the precision and recall on the minority class, and what's the base rate?"
- **Check:** confusion matrix; report precision/recall or PR-AUC (not ROC-AUC, which flatters imbalanced problems). Compare against the always-majority baseline and a one-feature logistic regression before crediting any lift.

## Train/test leakage signatures

- **Usually means:** the model saw the answer. Signatures: validation metrics that look too good (AUC 0.98 on a hard human-behavior problem), one feature dominating importance, or offline metrics that collapse on the first live week.
- **First question:** "For each feature, was this value knowable at the moment of prediction?"
- **Check:** audit top-10 features for post-outcome timestamps (e.g., `days_since_cancellation_call` in a churn model, `chargeback_flag` in fraud). Re-split by time (train on months 1–9, test on 10–12) instead of randomly — random splits leak through duplicated users and temporal correlation. If time-split performance drops sharply, you had leakage.

## Survivorship bias in cohort analyses

- **Usually means:** "average engagement rises with account age" is often just churners leaving the denominator — the survivors were always the engaged ones.
- **First question:** "Is the population at month 6 the same population that started at month 0?"
- **Check:** fix the cohort at entry and track *everyone*, counting churned users as zeros (or plot retention separately from per-survivor engagement). If the "improvement" disappears when churned users stay in the denominator, it was survivorship.

## Simpson's paradox in aggregated funnels

- **Usually means:** a mix change is masquerading as a rate change. Blended conversion can fall while every segment's conversion rises, if traffic shifted toward a low-converting segment.
- **First question:** "Does the direction hold within each major segment?"
- **Check:** decompose the blended rate by platform, channel, geo, new-vs-returning. Compute the counterfactual: last period's segment rates weighted by this period's mix. If that reproduces the drop, it's mix, and the remedy lives in marketing/acquisition, not the funnel.

## Seasonality read as trend

- **Usually means:** four up-weeks in November read as "growth inflection" is usually just Q4. Same for paydays, weekends, school calendars, Ramadan in relevant geos.
- **First question:** "What did this exact window look like last year?"
- **Check:** plot 13+ months so the eye can see the annual cycle; compare YoY and same-weekday. For anything decision-grade, run STL decomposition and look at the trend component, not the raw series. Never extrapolate a trend from a window shorter than one full seasonal cycle.

## P-hacking signatures in a readout

- **Usually means:** the hypothesis was found after the data was tortured. Signatures: p-values clustered just under 0.05; an oddly specific segment in the headline ("Android users in Canada who signed up on weekends, p = 0.048"); a metric that wasn't the pre-registered primary; a time window with suspiciously precise endpoints.
- **First question:** "How many metrics, segments, and windows were examined before this one, and was this the pre-registered primary?"
- **Check:** count the implicit comparisons and apply Benjamini–Hochberg across all of them — the finding usually dies. Ask for the analysis plan timestamp vs the data-pull timestamp. The definitive fix: treat it as hypothesis-generating and replicate in a fresh experiment. A real effect survives replication; a hacked one has a ~5% chance.
