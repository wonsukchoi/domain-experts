# Red flags

### Screening program's positive predictive value under 10% in the population it's deployed on
- **Usually means:** the test was validated on a higher-prevalence (often referral/specialist) population, or the screening population's true base rate is lower than assumed when the program was budgeted.
- **First question:** what base-rate population was the sensitivity/specificity pair originally measured on, and does it match this rollout's population?
- **Data to pull:** the original validation study's population characteristics and prevalence, versus this program's actual confirmed-case rate over its first 500–1,000 screens.

### Program readout uses relative risk reduction with no baseline rate stated
- **Usually means:** either an oversight, or the baseline rate is small enough that stating it would undercut the headline number.
- **First question:** what is the absolute rate in the unscreened/untreated arm, and what is the number needed to treat/screen?
- **Data to pull:** the source study's absolute event rates in both arms, not just the reported RR or "% reduction."

### Case count rising while testing volume or reporting requirements changed in the same window
- **Usually means:** a surveillance artifact (more testing finds more cases) rather than a true incidence increase.
- **First question:** did the case definition, testing eligibility, or mandatory-reporting rule change at or before the point the count started rising?
- **Data to pull:** testing volume (denominator) over the same period, plotted alongside case count, not case count alone.

### Biological monitoring values trending upward over 3+ consecutive tests while each stays under the single-test regulatory limit
- **Usually means:** an exposure source that MRP-style single-value triggers were never designed to catch (this is exactly what the three-test average trigger exists for).
- **First question:** what is the 3-test rolling average, and does it cross the average-based trigger even though no single value does?
- **Data to pull:** the worker's full biological monitoring history and the applicable standard's average-based trigger clause, not just the most recent single result.

### OSHA recordable incidence rate improving year-over-year but still 2–3x the NAICS industry benchmark
- **Usually means:** the site is regressing from an unusually bad baseline, not approaching an acceptable rate — "improving" and "acceptable" are being conflated.
- **First question:** where does this year's rate sit against the industry benchmark, not just against the site's own prior year?
- **Data to pull:** BLS/OSHA NAICS-code incidence-rate benchmark for the same year, matched to the site's own recordable log (OSHA 300).

### Cost-effectiveness analysis for a novel prevention program reports under roughly $5,000 per QALY
- **Usually means:** an undercounted harm/cost in the model, an inflated baseline risk assumption, or double-counting of averted downstream costs as both cost savings and health benefit.
- **First question:** what discount rate and time horizon were used, and were harms of the intervention itself (false positives, overdiagnosis, procedure complications) included in the denominator?
- **Data to pull:** the full model's cost and QALY inputs line by line, not just the headline ratio.

### Aeromedical waiver or Special Issuance requests spiking for one condition across a single squadron or cohort in a short window
- **Usually means:** either a genuine common exposure (environmental, a new duty-station hazard) or a documentation/coding artifact from a policy or examiner change.
- **First question:** is the spike concentrated in one examiner's caseload or one unit's exposure history, or spread evenly across the population?
- **Data to pull:** waiver requests broken out by examiner, unit, and exposure history over the preceding 12 months.

### Epidemic curve shows a single tight point-source-looking spike but new cases keep appearing past 2 incubation periods
- **Usually means:** the point-source hypothesis is wrong, or there is an ongoing common-source exposure (e.g., a contaminated reservoir still in use) rather than a one-time event.
- **First question:** is there a continuing source still accessible to new cases, versus a single past exposure event?
- **Data to pull:** exposure history and access dates for the cases appearing after the expected point-source tail should have ended.

### A screening or surveillance case definition changed mid-program with no dated changelog
- **Usually means:** a well-intentioned refinement that will be mistaken later for a true trend change, because nobody can tell which cases were counted under which definition.
- **First question:** what date did the definition change, and can cases be re-classified retroactively under both definitions to check whether the trend survives?
- **Data to pull:** the definition-change log and a re-run of the trend line using only the post-change definition applied consistently backward.

### A worker or examinee's most recent single biological or clinical value dropped just under a removal/waiver threshold right before a scheduled retest
- **Usually means:** either a true, benign improvement, or short-term behavior/exposure modification timed to the test (e.g., hydration loading, brief reassignment before testing).
- **First question:** does the drop match a plausible physiological or exposure-control explanation, or does it coincide suspiciously with the retest date alone?
- **Data to pull:** exposure/task assignment log in the days immediately preceding the test, compared to the routine assignment.

### A cluster of a rare condition (3+ cases) in one small subgroup gets dismissed as "not statistically significant yet"
- **Usually means:** correct math applied to the wrong question — a rare-disease cluster in a small denominator will almost never hit conventional significance quickly, and waiting for it to do so before investigating trades an early, cheap look for a late, expensive one.
- **First question:** what is the expected background count for this subgroup's size and time window, and how far does the observed count exceed it, regardless of p-value?
- **Data to pull:** expected incidence for the subgroup's size from population baseline rates, plus the units' shared exposures.
