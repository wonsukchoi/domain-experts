# Red Flags

### Sample size chosen without a stated minimum detectable effect
- **Usually means:** budget or timeline drove the sample size, and power was never computed; second most likely — power was computed for a different (larger, easier-to-detect) effect than the one now being claimed.
- **First question:** what effect size was this sample size powered to detect, and at what power?
- **Data to pull:** the original power/sample-size calculation, or absence thereof; current traffic/enrollment rate to check feasibility.

### Primary endpoint changed after data collection began
- **Usually means:** the originally planned endpoint didn't show the desired result and a better-looking one was substituted; second most likely — a genuine, pre-data-collection protocol amendment that wasn't clearly documented.
- **First question:** is there a timestamped pre-registration or protocol amendment showing this endpoint was chosen before unblinding?
- **Data to pull:** pre-registration record or protocol version history with dates.

### More than 5 hypothesis tests reported with no correction method named
- **Usually means:** family-wise or false-discovery error rate was never controlled, so the reported significance levels understate the true false-positive risk; second most likely — correction was applied but not disclosed.
- **First question:** how many tests were actually run (including ones not reported), and what correction, if any, was applied?
- **Data to pull:** full list of comparisons attempted, not just the ones that reached significance.

### Sequential "peek and stop" testing with no pre-specified alpha-spending plan
- **Usually means:** the team is monitoring a live experiment daily and will stop as soon as p<0.05 appears, inflating the true false-positive rate well above nominal; second most likely — a legitimate group-sequential design exists but wasn't documented before the study started.
- **First question:** was a stopping rule and alpha-spending function specified before the first look, or is "significant" being checked ad hoc?
- **Data to pull:** monitoring log/dashboard access history showing look frequency, and any pre-registered stopping rule document.

### Missing data over 5% on the primary outcome with only complete-case analysis reported
- **Usually means:** the missingness mechanism was assumed MCAR without testing that assumption; second most likely — the missingness genuinely correlates with the outcome (informative dropout) and complete-case analysis is biased.
- **First question:** does missingness rate differ across treatment arms or correlate with any measured baseline variable?
- **Data to pull:** missingness rate by arm/subgroup, baseline characteristics compared between complete and incomplete cases.

### Statistically significant result reported with no effect size or confidence interval
- **Usually means:** the analysis conflates significance with importance, or the effect size is small enough that showing it would undercut the headline claim; second most likely — an oversight in reporting standards.
- **First question:** what is the point estimate and its confidence interval, in the outcome's original units?
- **Data to pull:** raw summary statistics (means/proportions, differences, CIs) behind the reported p-value.

### Post-hoc subgroup finding presented as a primary conclusion
- **Usually means:** an exploratory subgroup analysis (e.g. "worked in women over 50") was run after seeing overall null or weak results, then promoted to headline status; second most likely — a genuinely pre-specified subgroup that wasn't clearly labeled as such.
- **First question:** was this subgroup analysis specified in the original protocol/SAP, or identified after looking at the data?
- **Data to pull:** the pre-specified analysis plan's subgroup list, compared against what's being presented.

### Standard errors computed with simple-random-sample formulas on clustered or stratified data
- **Usually means:** the analyst used default software output without specifying the actual sampling/clustering structure (e.g. `lm()` instead of a mixed-effects or survey-weighted model); second most likely — the clustering is real but small enough to be judged negligible without checking the intraclass correlation.
- **First question:** what is the unit of randomization/sampling, and does the analysis model match it?
- **Data to pull:** the model specification used, and the design's actual clustering/stratification structure.
