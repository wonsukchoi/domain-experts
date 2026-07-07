# Survey Researcher — Vocabulary

### Sampling frame
The actual list or mechanism used to select respondents (a phone number list, a voter file, a panel database) — not the target population itself.
**In use:** "Our frame is the state voter file, so we're structurally missing unregistered adults from the start."
**Common misuse:** treating "frame" and "population" as interchangeable — the frame is what you can reach, the population is who you want to describe.

### Coverage error
The bias introduced when the sampling frame systematically excludes part of the target population.
**In use:** "A landline-only frame has real coverage error now that most under-40 households are cell-only."
**Common misuse:** assuming a large sample size fixes coverage error — it doesn't; a bigger sample of the wrong frame is still the wrong frame.

### Nonresponse bias
The distortion introduced when respondents differ systematically from nonrespondents on the outcome being measured.
**In use:** "Response rate dropped to 15%, but the nonresponse-bias check against the voter file shows the respondents still track the frame's age/party mix closely."
**Common misuse:** equating response rate directly with bias magnitude — low response rate is a risk signal, not a bias measurement.

### Total survey error (TSE)
The framework treating a survey estimate's error as the sum of sampling error, coverage error, nonresponse error, measurement error, and processing error.
**In use:** "The margin of error only covers the sampling-error slice of total survey error — coverage and nonresponse are unquantified here."
**Common misuse:** reporting margin of error as if it represents the survey's total uncertainty.

### Post-stratification
Adjusting sample weights so that known subgroup proportions (age, gender, region) match population targets, using a single weighting pass per variable or joint cell.
**In use:** "We post-stratified on age and got a 3-point shift in the topline."
**Common misuse:** confusing this with raking — post-stratification uses known joint-cell population proportions; raking iterates single-dimension marginals when the joint population distribution is unknown.

### Raking (iterative proportional fitting)
Adjusting weights iteratively across multiple marginal distributions (e.g., age, then gender, then region, repeated until convergence) when the joint population distribution isn't available.
**In use:** "We raked to age, gender, and education marginals since we don't have the joint Census table for all three."
**Common misuse:** raking to too many dimensions relative to sample size, producing unstable, extreme weights instead of a stable correction.

### Design effect (Kish's deff)
The ratio of the actual variance of a weighted/clustered estimate to the variance a simple random sample of the same size would have; deff > 1 means the effective sample size is smaller than the raw count.
**In use:** "Deff of 1.8 means our effective n is really about 555, not 1,000."
**Common misuse:** reporting confidence intervals computed as if the sample were an unweighted simple random sample, ignoring the design effect and understating the true margin of error.

### Margin of error (MOE)
The sampling-error-only precision estimate for a probability sample, typically reported at 95% confidence.
**In use:** "MOE is ±3.1% on the full sample, wider on the weighted subgroups."
**Common misuse:** applying MOE to a non-probability (opt-in) sample, where the mathematical assumptions behind the formula don't hold.

### Cognitive interviewing
A pretesting method where respondents think aloud while answering draft questions, surfacing misunderstandings or unintended interpretations before fielding.
**In use:** "Cognitive interviews showed half the pretest group read 'household income' as personal income — we reworded it."
**Common misuse:** skipping this step for "obviously clear" questions, which is exactly where wording ambiguity hides.

### Split-ballot experiment
Randomly assigning different question wordings or orderings to subsamples within the same field period to measure the wording/order effect directly.
**In use:** "The split-ballot test showed an 18-point gap between the 'allow' and 'forbid' phrasings."
**Common misuse:** treating a single wording as ground truth without testing whether an alternative phrasing would move the number.

### Response rate (AAPOR RR1–RR6)
A family of standardized formulas (from AAPOR's Standard Definitions) for calculating the proportion of eligible sample members who completed the survey, differing in how partial interviews and unknown-eligibility cases are treated.
**In use:** "We report RR3, which allocates a portion of the unknown-eligibility cases as eligible using an estimated eligibility rate."
**Common misuse:** citing an unlabeled "response rate" without specifying which AAPOR formula was used, making cross-study comparison meaningless.

### Mode effect
The measurement difference attributable to how a survey is administered (phone vs. web vs. in-person), independent of any real opinion change.
**In use:** "Self-reported drug use runs higher on web than phone — that's a mode effect, not a behavior change."
**Common misuse:** comparing trend lines across a mode switch without first isolating the mode effect via a bridge study.

### Panel conditioning
The change in respondent behavior or answers caused by repeated participation in the same survey panel over time.
**In use:** "Long-tenured panelists answer the brand-awareness battery differently — that's panel conditioning, not market change."
**Common misuse:** assuming a longitudinal panel's estimates are automatically more reliable than a fresh cross-sectional sample, ignoring that repeated exposure itself changes responses.

### Weight trimming
Capping extreme individual survey weights at a stated multiple of the median weight, then redistributing the trimmed mass, to prevent a few respondents from dominating the estimate.
**In use:** "We trimmed weights above 5× the median and redistributed proportionally — it cut the design effect from 2.3 to 1.6."
**Common misuse:** leaving raw raked weights untrimmed, letting one or two heavily-weighted respondents swing the topline disproportionately.
