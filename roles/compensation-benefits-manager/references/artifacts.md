# Compensation artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Band update and compa-ratio table (filled — see Worked example in SKILL.md for full narrative)

**L4 (Senior Software Engineer) band, before and after market refresh:**

| | Old band | New band |
|---|---|---|
| Minimum | $145,000 | $155,000 |
| Midpoint | $160,000 | $170,000 |
| Maximum | $175,000 | $185,000 |

**Current incumbents against new band:**

| Employee | Current pay | New compa-ratio | Action |
|---|---|---|---|
| Employee A (6 yr, top performer) | $168,000 | 0.99 | No change needed |
| Employee B | $146,000 | 0.86 → raised to $155,000 (0.91) | +$9,000 |
| Employee C | $149,000 | 0.88 → raised to $155,000 (0.91) | +$6,000 |
| Employee D | $151,000 | 0.89 → raised to $155,000 (0.91) | +$4,000 |
| Employee E | $153,000 | 0.90 → raised to $155,000 (0.91) | +$2,000 |
| New hire (candidate) | Offered $180,000 | 1.06 | Within new band, no exception |
| **Total incremental cost** | | | **$21,000/year** |

## 2. Total compensation statement (filled example)

| Component | Value |
|---|---|
| Base salary | $180,000 |
| Target annual bonus (15% of base) | $27,000 |
| Equity grant (4-year vest, annualized) | $22,500/year |
| 401(k) match (4% of base) | $7,200 |
| Health/dental/vision (employer contribution) | $9,600 |
| **Total compensation** | **$246,300** |

**Rule applied:** compare this total figure against market total-comp data for the role, not base salary alone against a base-only benchmark.

## 3. Pay equity audit summary (filled example)

| Step | Detail |
|---|---|
| Population | All L1-L6 individual contributors, engineering function, n=340 |
| Controls | Level, tenure (years), most recent performance rating, geography |
| Method | OLS regression, pay as dependent variable, protected characteristic as independent variable of interest alongside controls |
| Finding | 1.8% unexplained gap associated with one demographic group — below the 2-3% typical flag threshold, but tracked for trend across cycles |
| Action | No immediate remediation triggered at this threshold; flagged for the next quarterly audit to confirm it isn't trending upward |

**Rule applied:** run the audit on a regular cadence (this example: quarterly) regardless of whether a complaint has been raised, and track findings over time rather than treating any single cycle's result in isolation.

## 4. Off-cycle adjustment approval log (filled example)

| Date | Employee/role | Reason | Band check | Approved amount |
|---|---|---|---|---|
| This quarter | New L4 hire, candidate | Competing offer at $180,000 | Within updated $155K-$185K band (compa-ratio 1.06) | $180,000 — approved |
| This quarter | Existing L4 (retention risk) | Competing offer at $172,000 | Within updated band (compa-ratio 1.01) | $172,000 — approved |
| Prior quarter (hypothetical rejected example) | Existing L3 | Manager requested $10,000 bump "to keep morale up," no competing offer or market basis | Would push compa-ratio to 1.22, above any other L3 | Declined — redirected to next cycle's structured review |

**Rule applied:** every off-cycle request gets checked against the band and logged, whether approved or declined — an undocumented exception is exactly what an equity audit later flags as unexplained.
