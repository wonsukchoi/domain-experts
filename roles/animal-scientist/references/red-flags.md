# Animal Scientist — Red Flags

### Feed-conversion ratio worsens by more than 10% period-over-period with no ration change
- **Usually means:** intake-measurement error (scale drift, unweighed refusals) or subclinical illness; less commonly, an ingredient-lot nutrient shift.
- **First question:** "Has anyone re-verified the scale calibration and the refusal weighback since the last good FCR period?"
- **Data to pull:** scale calibration log, daily refusal/orts records, recent herd health/treatment log.

### A single EPD is used to justify a breeding decision without checking correlated traits
- **Usually means:** the buyer is selecting on the trait that's easiest to market (commonly growth) without checking whether it's antagonistic to calving ease or milk.
- **First question:** "What does the full index or the correlated-trait EPDs look like, not just the headline number?"
- **Data to pull:** full EPD panel and the breed association's economic-index value for the bull or sire in question.

### A ration is formulated entirely from NRC book values with no current feed-tag analysis
- **Usually means:** the formulation is built on average, not actual, ingredient nutrient content — real risk when hay or silage lots vary by cutting or harvest year.
- **First question:** "When was the last feed-tag analysis run on the actual lot being fed?"
- **Data to pull:** most recent feed-tag lab analysis for each major ingredient.

### A proper-use or stocking calculation reuses last year's forage-production number
- **Usually means:** the current season's production hasn't been re-measured, and precipitation-driven variance makes last year's number unreliable.
- **First question:** "Has forage production been clipped or estimated for this season specifically?"
- **Data to pull:** current-season forage clipping or production-estimate data.

### Calving-ease scores decline in the two calving seasons following a growth-focused sire selection
- **Usually means:** selection pressure on growth/weaning-weight EPDs without an offsetting calving-ease weight has shifted birth weights upward.
- **First question:** "What was the birth-weight EPD trend on sires selected over the last two breeding cycles?"
- **Data to pull:** sire EPD history for birth weight and calving ease direct, correlated with calving-difficulty records.

### A least-cost ration formulation shows a nutrient exactly at its minimum with no margin
- **Usually means:** the formulation is optimized tightly to cost, leaving no buffer for measurement error or intake variability — a small negative deviation pushes the animal below requirement.
- **First question:** "Is this margin intentional, or did the solver just happen to land exactly on the constraint?"
- **Data to pull:** the LP solution's slack/shadow-price output for each nutrient constraint.

### Ingredient substitution is made "by rule of thumb" after a price spike, without rerunning the formulation
- **Usually means:** someone swapped a cheaper ingredient assuming similar nutrient content, which is rarely true across ingredient categories.
- **First question:** "Was the substitution checked against the actual nutrient profile of the new ingredient, or just its price?"
- **Data to pull:** nutrient analysis of both the original and substitute ingredient.

### A performance problem is attributed to genetics or ration formulation within one production cycle
- **Usually means:** genetics and formulation changes take a full cycle to show results — a same-cycle explanation is more likely a measurement, health, or environment issue.
- **First question:** "What changed in management or health status this cycle, before assuming it's genetic or nutritional?"
- **Data to pull:** health/treatment records and environmental conditions (weather, pen density) for the affected period.

### A single range-condition or body-condition score is used to justify a major stocking or feeding change
- **Usually means:** a one-time score can't distinguish a recovering from a declining trend — the decision needs at least two comparable readings.
- **First question:** "Is there a prior comparable score to establish trend direction, or just this one reading?"
- **Data to pull:** body-condition or range-condition scoring history for the same group/site.
