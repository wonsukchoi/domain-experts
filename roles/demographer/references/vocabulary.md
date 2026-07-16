# Vocabulary

Working vocabulary that generalists reliably misuse. Format per term: definition, how a practitioner actually uses it, the common misuse.

### Total Fertility Rate (TFR)

- **Definition:** the number of children a hypothetical woman would have if she experienced the current age-specific fertility rates throughout her childbearing years (typically 15–49) — a synthetic-cohort measure, not a count of any real woman's lifetime births.
- **In use:** "County TFR's at 1.58, well under the roughly 2.1 replacement level — but with the net migration we're seeing, that alone doesn't tell you the population's shrinking."
- **Common misuse:** treating TFR below replacement as a direct forecast of population decline, ignoring that it's a period synthetic-cohort measure and that migration and population momentum both operate independently of it.

### Population momentum

- **Definition:** the tendency of a population with a young age structure to keep growing for one to two generations after fertility falls to or below replacement level, because a large cohort of women has not yet passed through childbearing age.
- **In use:** "Fertility's been at replacement for a decade, but the population's still growing — that's momentum from the large cohort born in the 2000s aging into childbearing years."
- **Common misuse:** assuming replacement-level or sub-replacement fertility translates immediately into flat or declining population size.

### Cohort-component method

- **Definition:** the standard population-projection technique that ages each population cohort forward by applying survival ratios, adds births to new cohorts using age-specific fertility rates, and adds net migration by age — rather than extrapolating an aggregate growth rate.
- **In use:** "We're not extrapolating the trend line — running full cohort-component with current-vintage survival ratios and SOI migration flows so the age detail actually holds up."
- **Common misuse:** calling any age-blind trend extrapolation a "projection" interchangeably with a true cohort-component model; the two produce materially different answers whenever growth is age-concentrated.

### Net migration vs. gross migration

- **Definition:** net migration is in-migration minus out-migration for a geography; gross migration is the total volume of moves in each direction, which is always larger and can be large even when net migration is near zero.
- **In use:** "Net migration into the county's only +1,800 a year, but gross flows are closer to 14,000 each way — this is a high-churn labor market, not a quiet one."
- **Common misuse:** citing a small net migration figure as evidence of a stable or low-mobility population, when gross flows (and the turnover they imply for schools, housing, services) can be an order of magnitude larger.

### Standardized Mortality Ratio (SMR)

- **Definition:** the ratio of observed deaths in a population to the deaths expected if that population had the age-specific mortality rates of a standard reference population — used to compare mortality across places or groups with different age structures.
- **In use:** "SMR here is 1.14 against the state standard, so mortality's genuinely elevated even after we control for the fact that this county skews older."
- **Common misuse:** comparing raw crude death rates across two populations with different age structures and attributing the entire difference to a real mortality difference.

### Net Reproduction Rate (NRR)

- **Definition:** the average number of daughters a woman would have in her lifetime under current age-specific fertility and mortality rates — an NRR of 1.0 means each generation of women is exactly replacing itself.
- **In use:** "NRR's sitting at 0.76 — below-replacement, but that's a different statement than 'population is falling,' since it doesn't carry migration or the existing age structure."
- **Common misuse:** treating NRR the same way as TFR-vs-2.1, or treating either as a population-size forecast rather than a fertility/mortality-only replacement measure.

### Margin of Error (ACS)

- **Definition:** the 90%-confidence-interval range published alongside every American Community Survey estimate, reflecting sampling error from the survey design — smaller for large geographies and multi-year pooled estimates, often very large for small tracts or 1-year single-geography estimates.
- **In use:** "That 1-year ACS estimate for the tract has an MOE bigger than the estimate itself — we need the 5-year pooled number or we're reporting noise."
- **Common misuse:** reporting an ACS point estimate, especially for a small geography or subgroup, without checking whether the MOE makes the reported change or difference statistically meaningless.

### Vintage (postcensal) population estimate

- **Definition:** the Census Bureau's (or a state demographer's office's) annually updated population estimate for the years between decennial censuses, built by aging the last census forward with vital statistics and migration data — each year's release is a "vintage," and later vintages revise earlier years.
- **In use:** "Use the Vintage 2025 estimate, not the 2020 Census count — four years of births, deaths, and migration have moved that number."
- **Common misuse:** using the last decennial census count as "the current population" years after the census, especially in a fast-growing or fast-declining area where the gap compounds materially.

### Cohort survival ratio (school enrollment)

- **Definition:** in school-demography specifically, the ratio of enrollment in grade g in year t to enrollment in grade g−1 in year t−1 — a grade-progression-based method distinct from general population cohort-component projection, tracking retention, promotion, and migration of an actual enrolled cohort.
- **In use:** "Fifth-to-sixth-grade cohort survival ratio's been running about 0.97 the last three years — that's the number to apply, not a district-wide enrollment trend line."
- **Common misuse:** applying a district-wide enrollment growth rate to project a single grade's enrollment, instead of the grade-specific cohort survival ratio, which can diverge sharply by grade band (e.g., middle-to-high-school transitions where students leave for private or charter schools).

### Demographic analysis / dual-system estimation

- **Definition:** independent methods for estimating a census's coverage error — demographic analysis reconstructs an expected population from births, deaths, and migration records; dual-system estimation compares the census count against an independent post-enumeration survey to estimate the fraction missed or double-counted.
- **In use:** "Before we tell the county their population was undercounted, let's see what the demographic-analysis benchmark says — a single enumeration can't tell you its own error."
- **Common misuse:** inferring an undercount or overcount from a single count looking "low" relative to expectations, without an independent benchmark to actually measure the coverage error.

### Age heaping

- **Definition:** a data-quality artifact where reported ages cluster on round numbers (0, 5, 10, ...) because respondents round or estimate their age rather than reporting it exactly — common in self-reported or low-literacy-context survey and administrative data.
- **In use:** "That age distribution's got a huge spike at every multiple of five — before we trust the single-year age detail, check for heaping and consider smoothing."
- **Common misuse:** treating single-year age counts from a heaping-prone source as precise enough for single-year cohort-component work without first checking for and smoothing the heaping pattern.

### Crude rate vs. age-specific rate

- **Definition:** a crude rate (e.g., crude birth or death rate) is computed over the whole population regardless of age; an age-specific rate is computed within a defined age band (e.g., age-specific fertility rate for women 20–24).
- **In use:** "Crude birth rate's down, but that's mostly the population aging — age-specific fertility rates by band are basically flat."
- **Common misuse:** citing a crude rate change as evidence of a behavioral or fertility/mortality shift, when an age-structure shift alone can move the crude rate with no change in any age-specific rate.
