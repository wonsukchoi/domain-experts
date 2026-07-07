# Epidemiologist — Vocabulary

### Attack rate
The proportion of an exposed (or total) population that becomes ill during a defined outbreak period — cases divided by population at risk.
**In use:** "The chicken salad attack rate was 82% among exposed guests versus 5% among unexposed."
**Common misuse:** Treated as synonymous with incidence rate in an ongoing, non-outbreak population — attack rate is specific to a bounded outbreak population and time window.

### Relative risk (RR)
The ratio of attack rate (or incidence) in the exposed group to the attack rate in the unexposed group, from a cohort study.
**In use:** "RR of 16.2 for the chicken salad exposure is far beyond what background variation would produce."
**Common misuse:** Calculated from a case-control study, where it isn't directly obtainable — case-control studies yield an odds ratio, not a relative risk, unless a full cohort's exposure distribution is known.

### Odds ratio (OR)
The ratio of the odds of exposure among cases to the odds of exposure among controls, from a case-control study.
**In use:** "With an OR of 8.4 and a 95% CI of 3.1–22.7, the association survives even a conservative reading."
**Common misuse:** Reported as if numerically equal to relative risk when the disease isn't rare in the source population — the rare-disease assumption is a precondition for the approximation, not a formality.

### Attributable risk
The absolute difference in attack rate (or incidence) between the exposed and unexposed groups — the excess risk directly attributable to the exposure.
**In use:** "Attributable risk of 77 percentage points means removing the exposure would have prevented nearly all the illness among that group."
**Common misuse:** Confused with relative risk — attributable risk is an absolute difference (percentage points), relative risk is a ratio; a huge relative risk on a rare baseline can still mean a small attributable risk.

### Population attributable fraction (PAF)
The proportion of all cases in the total population (not just the exposed) that are attributable to the exposure, accounting for what fraction of the population was actually exposed.
**In use:** "Even with a relative risk of 16, the population attributable fraction is only 27% because just a third of guests ate the implicated dish."
**Common misuse:** Applied at the individual level ("this person's illness is 27% likely due to X") — PAF is a population-level statistic, not an individual probability.

### Case definition
The explicit clinical, lab, and epidemiologic (time/place/person) criteria used to classify someone as a case, typically tiered confirmed/probable/suspect.
**In use:** "We widened the case definition to include probable cases once lab confirmation lagged behind the case-finding effort."
**Common misuse:** Left implicit or changed mid-investigation without documenting the change — a shifting case definition invalidates before/after case-count comparisons.

### Epi curve
A histogram of case count by date (or time) of symptom onset, used to infer the pattern of exposure.
**In use:** "The epi curve's single sharp peak at 14 hours points to a point-source exposure, not ongoing transmission."
**Common misuse:** Plotted by report date or diagnosis date instead of onset date — reporting delays distort the curve's shape and can manufacture a false multi-peak appearance.

### Point-source outbreak
An outbreak where all cases share a single, time-limited exposure — producing a single narrow epi-curve peak roughly one incubation period after the exposure.
**In use:** "The single 14-hour peak is textbook point-source, consistent with a preformed toxin."
**Common misuse:** Assumed whenever there's one identified culprit food, even when the curve shows a longer tail suggesting a continuous or repeated exposure (e.g. an ongoing contaminated water supply) rather than a single event.

### Propagated outbreak
An outbreak sustained by person-to-person (or vector-to-person) transmission, producing successive epi-curve peaks spaced roughly one incubation period apart.
**In use:** "The three peaks two days apart, tracking documented household contacts, mark this as propagated, not point-source."
**Common misuse:** Missed when investigators stop at the first peak and don't check whether later cases have a plausible secondary-transmission link to earlier ones.

### Confounding
A distortion of the observed exposure-outcome association caused by a third variable associated with both the exposure and the outcome, not on the causal path between them.
**In use:** "Age confounded the crude association — after stratifying by age group, the odds ratio dropped from 4.2 to 1.3."
**Common misuse:** Used loosely to mean any bias — confounding specifically requires the third variable be associated with both exposure and outcome and not be a downstream effect of the exposure (which would make it a mediator, not a confounder).

### Selection bias
A distortion introduced by how cases or controls were identified or chose to participate, making them unrepresentative of the true source population.
**In use:** "Recruiting controls from the same hospital as the cases introduced selection bias — hospitalized controls aren't representative of the general population's exposure rate."
**Common misuse:** Conflated with confounding — selection bias arises from the sampling/enrollment process itself, not from an uncontrolled third variable in an otherwise representative sample.

### Recall bias
Differential accuracy or completeness of exposure reporting between cases and controls, typically because cases search their memory harder for an explanation.
**In use:** "Recall bias is a real risk here — interviewed three weeks post-exposure, cases who've been thinking about 'what made me sick' may over-report unusual foods."
**Common misuse:** Assumed to always inflate the association — recall bias can also dilute a true association if cases simply forget a genuinely causal but unremarkable exposure.

### Sensitivity (surveillance)
The proportion of true cases in the population that a surveillance system actually detects and reports.
**In use:** "A system relying only on hospital admissions has low sensitivity for a mild, mostly outpatient illness."
**Common misuse:** Confused with positive predictive value — sensitivity asks what fraction of true cases are caught; PPV asks what fraction of reported signals are true cases. A system can be high on one and low on the other.

### Mantel-Haenszel estimate
A pooled, confounder-adjusted measure of association calculated across strata, weighting each stratum by its precision.
**In use:** "The Mantel-Haenszel pooled odds ratio of 6.8 confirms the association holds after adjusting for age."
**Common misuse:** Skipped in favor of reporting only the crude estimate when a plausible confounder is known — the crude number is presented as the answer when the stratified estimate is the one that should drive the conclusion.
