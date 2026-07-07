# Medical Scientist — Red Flags

### EC50/IC50 reported without the dose-response curve reaching a plateau on both ends
- **Usually means:** the value was extrapolated past the tested dose range, or the top/bottom dose wasn't wide enough to capture the true asymptotes.
- **First question:** "What are the actual top and bottom measured inhibition/response values, and at what doses?"
- **Data to pull:** the raw dose-response curve, not just the fitted parameter.

### Z'-factor below 0.5 on a screening plate whose hits are being reported
- **Usually means:** the assay's signal window is too narrow relative to its noise for that day's run — hits and misses from this run are unreliable.
- **First question:** "What was the Z'-factor on this specific plate/run, not the assay's historical best?"
- **Data to pull:** the plate's positive/negative control values and computed Z'.

### A biological claim's "n" is actually technical replicate count
- **Usually means:** the reported confidence interval reflects assay measurement noise, not true biological variance — it will look tighter than the real uncertainty.
- **First question:** "How many independent biological samples (separate animals, separate cell passages) does this n represent?"
- **Data to pull:** the raw data table with biological-replicate identifiers, not just the averaged summary.

### In vitro potency cited as evidence of in vivo efficacy with no exposure data referenced
- **Usually means:** the PK/PD link hasn't been established — the compound may never reach an active concentration at the target tissue.
- **First question:** "What is the measured free-drug concentration at the target tissue, and how does it compare to the in vitro IC50?"
- **Data to pull:** the PK study's tissue concentration-time data.

### Subjective endpoint (histopathology score, tumor palpation, behavioral score) scored unblinded
- **Usually means:** effect-size inflation from scorer expectation bias — one of the most common causes of preclinical results that fail to replicate.
- **First question:** "Was the scorer blinded to treatment group at the time of scoring?"
- **Data to pull:** the study protocol's blinding procedure and the scorer's group-assignment access log.

### A result is statistically significant but contradicts known target mechanism
- **Usually means:** an assay artifact, off-target effect, or a genuinely novel finding — indistinguishable without independent-method replication.
- **First question:** "Has this been replicated by a second, mechanistically independent assay?"
- **Data to pull:** results from an orthogonal assay type, not a repeat of the same one.

### GLP-level documentation applied to an exploratory hypothesis-generation study, or vice versa
- **Usually means:** either wasted budget/timeline (over-rigor on discovery work) or an unusable data package (under-rigor on a study meant for a regulatory submission).
- **First question:** "What is this specific study's intended downstream use — internal decision only, or does it feed a submission?"
- **Data to pull:** the study protocol's stated GLP status, confirmed before data collection started, not assigned retroactively.

### An underpowered in vivo study reported as "no significant difference = no effect"
- **Usually means:** the study lacked the sample size to detect anything but a very large effect — absence of significance isn't evidence of absence.
- **First question:** "What effect size was this study powered to detect, and what was the actual observed effect size and its confidence interval?"
- **Data to pull:** the a priori power calculation and the study's actual variance.

### A go/no-go recommendation collapses "target engagement," "efficacy," and "efficacy at achievable exposure" into one claim
- **Usually means:** the recommendation is overstating the evidence tier actually reached.
- **First question:** "Which of these three claims does the data in hand actually support?"
- **Data to pull:** the specific endpoint and study type behind each claim being made.

### A single biological replicate's result is presented as the program's finding
- **Usually means:** reproducibility hasn't been checked; the number could be a favorable outlier.
- **First question:** "How many independent biological replicates were run, and what's the spread across them?"
- **Data to pull:** all replicate values, not just the best or the first.

### Arithmetic mean reported across EC50/IC50 values from multiple replicates
- **Usually means:** the reported "average" is skewed high by log-normally distributed data, especially when replicate values span more than 2-3x.
- **First question:** "Was this averaged on the log scale (geometric mean) or the linear scale?"
- **Data to pull:** the individual replicate EC50/IC50 values to recompute on log scale if needed.
