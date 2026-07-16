# Demographer artifacts — templates with real structure

Working templates an agent can fill in. Numbers below are illustrative but internally consistent, styled after a mid-size US county/city planning engagement.

## 1. Cohort-component projection workbook (5-year age bands, 5-year horizon)

**Inputs sheet** — every projection run states these explicitly before any arithmetic:

| Input | Value | Source |
|---|---|---|
| Base year / vintage | 2025, Vintage 2025 estimate | Census Population Estimates Program |
| General Fertility Rate (births per 1,000 women 15–44/yr) | 56.2 | State vital records, 3-year average |
| Implied TFR | ≈1.58 | Derived from age-specific fertility rates |
| Survival ratio, birth → age 0–4 | 0.9935 | NCHS US Life Tables, current release |
| Survival ratio, 0–4 → 5–9 | 0.9975 | NCHS US Life Tables |
| Survival ratio, 60–64 → 65–69 | 0.9720 | NCHS US Life Tables |
| Net migration source | ACS 5-yr migration flows + IRS SOI county-to-county | Pooled to reduce small-area noise |

**Projection sheet** — one row per age band, four columns: base population, survival-adjusted survivors, net migration, projected population. Every row's math is shown, not just the result:

| Age band, 2030 | Source cohort, 2025 | Survival ratio | Survivors | Net migration | Projected 2030 |
|---|---|---|---|---|---|
| 0–4 | 6,125 births (5-yr total) | 0.9935 | 6,085 | +85 | 6,170 |
| 5–9 | 6,850 (age 0–4) | 0.9975 | 6,833 | +210 | 7,043 |
| 10–14 | 7,120 (age 5–9) | 0.9985 | 7,109 | +140 | 7,249 |
| 65–69 | 8,900 (age 60–64) | 0.9720 | 8,651 | +310 | 8,961 |
| 70+ | 6,340 (age 65–69) + 13,180 (age 70+) | 0.9550 / 0.7150 | 6,055 + 9,424 | +180 | 15,659 |

**Rule:** every band's survival ratio and migration figure gets its own cited source line, not a single "assumptions" paragraph at the top — a reviewer needs to be able to challenge one input without re-deriving the whole model.

## 2. Reconciliation-against-control-total worksheet

Run whenever a new decennial count or updated postcensal vintage becomes available, to check whether the components-based estimate for the intervening years held up.

| Component | Estimated (2020–2025) | Notes |
|---|---|---|
| Births | 30,850 | State vital records |
| Deaths | 24,110 | State vital records |
| Natural increase (Births − Deaths) | +6,740 | |
| Estimated net migration | +9,600 | ACS/IRS SOI, pooled |
| **Implied population change** | **+16,340** | Natural increase + migration |
| **Actual change (2020 Census → 2025 Vintage estimate, later reconciled against a new benchmark)** | **+15,890** | |
| **Residual (unexplained)** | **−450** | ≈2.8% of the implied change |

**Rule:** report the residual explicitly and attribute it to the most likely source — for a residual this size, migration estimation is almost always the weakest of the three components (birth and death registration are close to complete; migration is modeled, not directly counted) — rather than silently rebalancing the components to force a match.

## 3. Census undercount adjustment memo (excerpt)

> **Subject: Demographic Analysis Benchmark vs. 2020 Census Count, [County]**
>
> The 2020 Census count for [County] is 132,050. The independent demographic-analysis benchmark, built from vital-statistics births/deaths since the 2010 Census plus Medicare enrollment and IRS-based migration estimates, puts the expected population at 134,900 — implying a net undercount of approximately 2,850 (2.1%).
>
> The undercount is not distributed evenly across age groups: children 0–4 show the largest gap (an estimated 4.8% undercount, consistent with the national pattern of young-child undercount driven by complex/multi-generational households and joint-custody arrangements not resolved by a single-household census form), while the 65+ population shows a small net overcount (−0.6%), consistent with the historical pattern of more complete elderly enumeration.
>
> **Recommendation:** for any per-capita fund allocation or district-boundary work that weights young-child population, apply the demographic-analysis-benchmarked estimate rather than the raw 2020 count, and flag the 0–4 undercount specifically to the state's census-outreach program ahead of the next decennial cycle. Do not apply a flat 2.1% correction uniformly across all age bands — that would overcorrect the 65+ population and undercorrect the 0–4 population.

## 4. Scenario range for a projection deliverable

Never ship a single point estimate. Minimum structure — central case plus a migration-driven low/high band, since migration is consistently the least certain of the three components:

| Scenario | Net migration assumption | 2030 total population |
|---|---|---|
| Low | Net migration 40% below central case | 133,400 |
| **Central** | **As modeled (see workbook)** | **136,800** |
| High | Net migration 40% above central case | 138,600 |

**Rule:** state which single assumption drives the width of the band (here, migration) so the reader knows what evidence would narrow it — a new ACS release, updated SOI flow data, or a local economic development event that changes in-migration.
