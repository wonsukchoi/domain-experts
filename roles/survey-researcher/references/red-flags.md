# Survey Researcher — Red Flags

### Response rate below 20% for a probability-based phone or mail survey
- **Usually means:** heavy nonresponse-bias risk, refusal-driven undercoverage of hard-to-reach subgroups.
- **First question:** does the survey have benchmark data (voter file, Census) to check whether respondents differ from nonrespondents on the outcome?
- **Data to pull:** AAPOR RR3 disposition codes, early-vs-late-responder comparison on key items.

### Mode switch between waves (phone → web, mail → phone) with no split-sample bridge study
- **Usually means:** the wave-over-wave trend line reflects a measurement artifact, not a real opinion shift.
- **First question:** was a parallel-mode pilot or bridge study run before switching?
- **Data to pull:** prior-wave methodology document, any available mode-effect pilot data.

### Raking weights with a design effect above ~2.0 or max individual weight above 5× the median
- **Usually means:** the achieved sample is being asked to represent population subgroups far outside its natural composition — unstable, high-variance estimates.
- **First question:** how many dimensions is the sample being raked to, relative to sample size?
- **Data to pull:** weight distribution histogram, Kish's deff calculation.

### Leading or loaded question wording (forbid/allow asymmetry, "Do you agree that experts say X")
- **Usually means:** the topline is measuring wording sensitivity, not underlying opinion.
- **First question:** was this question split-ballot or cognitively pretested?
- **Data to pull:** split-ballot experiment results, if any; question's edit history.

### Subgroup crosstab reported with an unweighted base under 30 respondents
- **Usually means:** the reported percentage is statistically unstable and reads as more precise than it is.
- **First question:** what is the actual unweighted base for that specific cell?
- **Data to pull:** full crosstab with base-size column, not just percentages.

### Opt-in or river-sample online panel reported with a formal margin of error
- **Usually means:** probability-sampling math (MOE) is being applied to a non-probability sample, manufacturing false precision.
- **First question:** is this a probability sample (known selection probability) or an opt-in panel?
- **Data to pull:** panel recruitment and selection methodology documentation.

### Topline shifts more than 5 points between waves with no corresponding real-world event
- **Usually means:** a methodology change (mode, wording, sample source, weighting scheme) is masquerading as an opinion shift.
- **First question:** did anything in the instrument or field method change between waves?
- **Data to pull:** wave-over-wave methodology comparison table.

### Nonresponse-bias analysis never run despite a response rate under 30%
- **Usually means:** the survey's actual bias is unknown and unaddressed, not merely undisclosed.
- **First question:** what auxiliary frame-level or benchmark data exists to compare respondents against nonrespondents?
- **Data to pull:** frame demographics vs. achieved-sample demographics, side by side.

### "Don't know" / refused responses silently excluded from the reported denominator
- **Usually means:** the topline overstates certainty and understates the true undecided share.
- **First question:** what percentage of respondents fell into DK/refused on this item?
- **Data to pull:** full response distribution including DK/refused counts.

### Entire field period falls within a narrow window coinciding with a major news event
- **Usually means:** the estimate captures a transient reaction rather than a stable underlying attitude.
- **First question:** what happened in the news cycle during the field dates?
- **Data to pull:** field-date range against a timeline of relevant news events.
