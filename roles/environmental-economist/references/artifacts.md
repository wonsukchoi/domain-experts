# Environmental Economist — Artifacts

Filled templates for the three most common deliverables: a regulatory impact analysis (RIA) benefit-cost worksheet, a hedonic/travel-cost model specification table, and a natural resource damage assessment (NRDA) equivalency worksheet.

## 1. Regulatory impact analysis (RIA) benefit-cost worksheet

Rule: baghouse filter retrofit, 300 MW coal plant. Capital $45M (20-yr life), operating $3M/yr. PM2.5 reduction 500 tons/yr.

| Line item | Value | Method / source |
|---|---|---|
| Capital cost (annualized, 3%) | $3.025M/yr | $45M ÷ annuity factor 14.877 (20yr, 3%) |
| Capital cost (annualized, 7%) | $4.248M/yr | $45M ÷ annuity factor 10.594 (20yr, 7%) |
| Operating cost | $3.000M/yr | Facility engineering estimate |
| **Total annualized cost (3% / 7%)** | **$6.025M / $7.248M** | Sum of above |
| Avoided premature deaths | 12/yr | Regional concentration-response function, PM2.5 |
| VSL (2023, income-adjusted) | $9.6M | EPA Guidelines for Preparing Economic Analyses, updated |
| Mortality benefit | $115.2M/yr | 12 × $9.6M |
| Avoided asthma exacerbations | 340/yr | Concentration-response function, morbidity endpoint |
| Cost-of-illness per event | $500 | Published cost-of-illness literature |
| Morbidity benefit | $0.17M/yr | 340 × $500 |
| **Total annual benefit** | **$115.37M/yr** | Sum of mortality + morbidity |
| **Net benefit (3% / 7%)** | **$109.35M / $108.12M** | Benefit − annualized cost |
| **Benefit-cost ratio (3% / 7%)** | **19.1:1 / 15.9:1** | Benefit ÷ annualized cost |
| % of benefit from dominant category (mortality) | 99.9% | Disclosed per standard practice — see red-flags.md |

**Distributional table (fill per affected geography):**

| Geography | % of exposed population | % of avoided-mortality benefit | Poverty rate vs. regional average |
|---|---|---|---|
| Census tract nearest facility | 22% | 60% | 2.3x |
| Remainder of modeled exposure area | 78% | 40% | 1.0x (baseline) |

## 2. Hedonic price model specification table

Use to document a hedonic regression valuing an environmental attribute (hazard proximity, air quality, waterfront access) via housing price.

| Component | Specification | Notes |
|---|---|---|
| Dependent variable | ln(sale price) | Log form for elasticity interpretation |
| Environmental variable | Distance to hazard (miles), or AQI at time of sale | The variable of interest — coefficient is read as implicit price |
| Structural controls | Square footage, lot size, age, bedrooms, bathrooms, condition | Standard hedonic housing controls |
| Neighborhood controls | School district rating, crime rate (incidents/1,000 residents), distance to CBD | Omit any of these and the environmental coefficient likely picks up their effect instead |
| Fixed effects | Sale year, census tract or school zone | Controls for market-wide trends and unobserved neighborhood quality |
| Sample restriction | Arm's-length sales only, ± N years around policy/event | Excludes foreclosures, intra-family transfers |
| Robustness check | Re-estimate with spatial fixed effects or a matched-pair (border) design | Tests whether the coefficient survives tighter geographic controls |
| Output to report | Coefficient, standard error, implied $ value per unit of the environmental variable, sample N | Implied value = coefficient × mean sale price (for log-linear form) |

## 3. Natural Resource Damage Assessment — Habitat Equivalency Analysis (HEA) worksheet

Scenario: oil spill injures 30 acres of coastal marsh; recovery to full ecological function projected at 15 years absent restoration, or 5 years with active restoration.

| Line item | Value | Method |
|---|---|---|
| Injured habitat | 30 acres | Field assessment, injury delineation survey |
| Baseline (uninjured) service level | 100% | Reference marsh comparison |
| Interim service loss, no restoration | 30 acres × 15 years × avg. 55% service loss over recovery curve | Debit side — discounted to present value of service-acre-years lost |
| Discounted service-acre-years lost | 141.6 (at 3% discount rate) | Sum of annual (acres × % loss) discounted to year 0 |
| Restoration project (candidate) | 20 acres created marsh, 5-year ramp to 100% service | Credit side |
| Discounted service-acre-years gained (per acre) | 3.64 | Sum of annual service fraction over ramp-up, discounted |
| **Required restoration scale** | **141.6 ÷ 3.64 ≈ 38.9 acres** | Debit service-acre-years ÷ credit service-acre-years per acre |
| Restoration shortfall vs. candidate project | 38.9 − 20 = 18.9 acres | Candidate project undersized — needs expansion or a second parcel |

**Deliverable line (claim summary):** "Based on Habitat Equivalency Analysis, the injury represents 141.6 discounted service-acre-years of lost marsh function. The proposed 20-acre restoration project provides 72.8 discounted service-acre-years (20 × 3.64), covering 51% of the debit — an additional 18.9 acres of equivalent restoration, or a second parcel of comparable scale, is required to make the public whole."
