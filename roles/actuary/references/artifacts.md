# Actuary artifacts — templates with real structure

Working templates an agent can fill in. Example numbers throughout follow the SKILL.md worked example: AY2023 commercial auto liability, $40.0M earned premium, evaluated at 24 months.

## 1. Loss development triangle (reported losses, $000s)

Rows = accident year, columns = evaluation age in months. Volume-weighted age-to-age factors along the bottom.

| AY | 12mo | 24mo | 36mo | 48mo | 60mo |
|---|---|---|---|---|---|
| 2019 | 6,800 | 10,540 | 12,648 | 13,913 | 14,608 |
| 2020 | 7,200 | 11,160 | 13,392 | 14,731 | 15,468 |
| 2021 | 8,100 | 12,555 | 16,949* | 18,644 | — |
| 2022 | 8,900 | 13,795 | 19,047* | — | — |
| 2023 | 9,300 | 12,000 | — | — | — |

\* AY2021 and AY2022's 24→36mo development ran 1.35 and 1.38 — above the 5-year average — the first sign of the social-inflation trend discussed below.

**Age-to-age factors (volume-weighted across AY2019–2022 unless noted):**

| Age-to-age | 2019 | 2020 | 2021 | 2022 | 5-yr avg | Selected |
|---|---|---|---|---|---|---|
| 12→24 | 1.550 | 1.550 | 1.550 | 1.550 | 1.550 | 1.550 |
| 24→36 | 1.200 | 1.200 | 1.350 | 1.381 | 1.200 | **1.350** |
| 36→48 | 1.100 | 1.100 | 1.100 | — | 1.100 | 1.100 |
| 48→60 | 1.050 | 1.050 | — | — | 1.050 | 1.050 |
| 60→ult (tail) | 1.030 | — | — | — | 1.030 | 1.030 |

**Selection rule applied to 24→36:** recent-diagonal average (AY2021, AY2022) = (1.350 + 1.381) / 2 = 1.365. AY2023 has 850 reported claims against a 1,082-claim full-credibility standard, so Z = √(850/1,082) = 0.886. Selected factor = 0.886 × 1.365 + 0.114 × 1.200 = **1.350** (not the raw 5-year average, not the raw recent average). Every other factor uses the 5-year average unweighted — no diagonal anomaly was found there.

**CDF (24mo → ultimate) for AY2023:** 1.350 × 1.100 × 1.050 × 1.030 = **1.606**.

## 2. Bornhuetter-Ferguson worksheet

| Line | Value | Source |
|---|---|---|
| Earned premium | $40.0M | Policy system |
| Expense ratio | 37% | Pricing plan |
| Profit & contingency provision | 5% | Pricing plan |
| Permissible/expected loss ratio | 58% | 1 − 0.37 − 0.05 |
| Expected losses | $23.2M | $40.0M × 0.58 |
| CDF (24mo → ult) | 1.606 | Triangle, selected factors |
| % unreported | 37.7% | 1 − 1/1.606 |
| Reported losses to date | $12.0M | Claims system, 24mo |
| **BF ultimate** | **$20.75M** | $12.0M + ($23.2M × 0.377) |
| Chain-ladder ultimate (same CDF) | $19.27M | $12.0M × 1.606 |
| **Selected ultimate** | **$20.0M** | Simple average of the two, given moderate credibility and <7% method spread |

## 3. Credibility-weighted rate indication (classical/limited-fluctuation)

Used when a segment's own experience is below full credibility for a rate filing.

| Input | Value |
|---|---|
| Reported claims, segment | 850 |
| Full-credibility standard (±5%, 90% confidence) | 1,082 |
| Credibility Z = √(n / n_full) | 0.886 |
| Segment's indicated rate change | +14.2% |
| Complement of credibility (statewide/industry indicated change) | +6.0% |
| **Credibility-weighted indicated change** | 0.886 × 14.2% + 0.114 × 6.0% = **13.3%** |

**Fallback order when the complement itself is thin:** (1) same-state, broader class-plan indication; (2) countrywide indication for the same line, territory-adjusted; (3) prior approved rate change trended forward at the last approved trend assumption. Never fall back to "no change" as a complement — that silently asserts 0% is the right answer, which is itself an unexamined assumption.

## 4. Rate indication memo (excerpt, filed with the state)

> **Line:** Commercial Auto Liability, [State]. **Effective date:** [date + 90 days].
>
> **Indicated statewide rate change: +13.3%.**
>
> Basis: current-level earned premium of $40.0M developed and trended to $23.2M expected losses at the permissible loss ratio of 58% (37% expense provision, 5% profit provision). Loss trend applied: severity +7.5%/year, frequency −1.0%/year (selected net trend +6.4%/year), consistent with observed frequency decline and accelerating severity in bodily-injury claims over the experience period. Credibility of the statewide indication: Z = 0.886 (850 claims vs. 1,082 full-credibility standard); complement of credibility is the countrywide indication of +6.0%, territory-adjusted.
>
> **Recommended action:** approve +13.3% overall, with by-territory variation of +8% to +19% per the attached classification relativities (Exhibit 4), reflecting territory-level loss ratio deviations of more than one full credibility-weighted standard error from the statewide average.

## 5. Statement of actuarial opinion (SAO) excerpt, ASOP 36 pattern

> I, [Name], am [a Member/Fellow] of the [CAS/SOA] and meet the qualification standards of the American Academy of Actuaries. I have examined the reserves for unpaid losses and loss adjustment expenses of [Company] as of December 31, [year], as shown in Exhibit A.
>
> In my opinion, the amounts carried in Exhibit A, of $[X]M net of reinsurance, **make a reasonable provision** for all unpaid loss and loss adjustment expense obligations under the terms of the company's contracts and agreements.
>
> This opinion is based on data through 24 months of maturity for the most recent accident year, and reflects the credibility-weighted development factor selections discussed in the accompanying Actuarial Report, including the +$7.7M IBNR adjustment to AY2023 commercial auto liability described in Section 3. Risk of material adverse deviation: given the recency of the trend shift underlying the AY2023 adjustment, adverse deviation beyond the selected estimate is judged reasonably possible and is discussed further in the Risk of Material Adverse Deviation section of the Report (ASOP 36 disclosure).
