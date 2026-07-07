# Atmospheric Scientist — Red Flags

### Raw ensemble agreement quoted directly in a public product without calibration
- **Usually means:** the forecaster pulled the percentage straight from the ensemble output panel without checking the reliability diagram for that probability bin.
- **First question:** what does this model's reliability diagram say the 65-75% bin actually verifies at this season?
- **Data to pull:** seasonal reliability-diagram table for this model/parameter combination.

### Two guidance models disagree on timing by more than 3 hours inside the 24-hour forecast window
- **Usually means:** the synoptic pattern has a genuine bifurcation point (e.g., a shortwave phasing question) that hasn't resolved yet, not that one model is simply "wrong."
- **First question:** which model has better recent verification for this specific pattern type (e.g., closed-low progression, lake-effect banding)?
- **Data to pull:** last 5 cycles of both models' runs for this event, overlaid, plus each model's seasonal bias report for this synoptic category.

### Observations diverging from the most recent model run by more than one standard deviation of typical short-term forecast error
- **Usually means:** the model has already busted for this event and the next run cycle (often 6 hours out) is too slow to help the current decision.
- **First question:** what do the last 3 hours of radar/surface trend say, independent of any model?
- **Data to pull:** radar loop, surface obs time series, satellite trend.

### Ensemble spread narrowing sharply between consecutive runs without a corresponding physical forcing change
- **Usually means:** a numerical artifact or a single outlier member being resolved, not genuine increased confidence — verify the members didn't just converge on a shared bias.
- **First question:** did the synoptic-scale forcing (e.g., jet position, thermal gradient) actually change, or did the ensemble spread shrink for numerical reasons?
- **Data to pull:** member-by-member comparison across the last 2 cycles, synoptic analysis charts.

### Warning issued at a probability threshold below the hazard's calibrated cost-asymmetry trigger
- **Usually means:** threshold creep from local warning-fatigue pressure or a prior near-miss overcorrection, not a defensible cost/loss calculation.
- **First question:** what was the actual POD/FAR over the last season at this threshold, and does it justify the current trigger point?
- **Data to pull:** season verification stats (POD, FAR, CSI) at the current threshold.

### A public-facing product still uses raw meteorological jargon (CAPE, shear, vorticity) in the lead sentence
- **Usually means:** the discussion product was copy-pasted into the public product without a communication-style pass.
- **First question:** does the first sentence tell a non-meteorologist what to do?
- **Data to pull:** the draft product text itself, read against the plain-language template.

### Forecast bust with no logged root-cause entry within 24 hours
- **Usually means:** the specific reasoning error (wrong model trusted, missed observation trend, uncalibrated probability) will recur because it was never captured for the next similar setup.
- **First question:** which decision-framework step failed — guidance selection, calibration, or observation cross-check?
- **Data to pull:** the original forecast discussion text and the verification scorecard for the event.

### Impact-based briefing to an emergency manager leads with synoptic setup instead of the decision they face
- **Usually means:** the briefing was written for a meteorologist audience and handed off without a communication-style rewrite.
- **First question:** does the first sentence state the action window and confidence level?
- **Data to pull:** the briefing draft, timestamped against the decision deadline the emergency manager is working against.

### Categorical outlook level (Marginal/Slight/Enhanced/Moderate/High) cited without the underlying calibrated percentage
- **Usually means:** the tier is being used as if it were a precise probability rather than a communication shorthand, which strips the audience of the information needed to weigh their own risk tolerance.
- **First question:** what is the calibrated percentage and geographic corridor behind this tier?
- **Data to pull:** the outlook text's full probabilistic breakdown, not just the categorical label.
