# Compliance program playbook — filled templates

Working structures an agent can populate directly, not descriptions of what they should contain. Context throughout: the same $8.2B regional bank BSA/AML program used in the SKILL.md worked example, plus one healthcare-compliance variant where the mechanism differs materially.

## 1. Compliance risk heat map

Scored likelihood (1–5) × impact (1–5) per business line/product; refresh at least annually and after any new product launch. Score ≥15 = top-tier monitoring priority (full-population coverage, not sampling).

| Business line / product | Likelihood | Impact | Score | Monitoring tier | Last refreshed |
|---|---|---|---|---|---|
| Commercial cash-intensive accounts (import/export, check cashers) | 4 | 5 | 20 | Full coverage, real-time alerts | Jan 2026 |
| Correspondent banking (foreign FI relationships) | 3 | 5 | 15 | Full coverage, quarterly EDD refresh | Jan 2026 |
| Retail consumer deposits | 2 | 2 | 4 | Sample-based, 2% monthly | Jan 2026 |
| Wire transfers >$50K | 3 | 4 | 12 | Full coverage, next-day review | Jan 2026 |
| Third-party payment processors | 4 | 4 | 16 | Full coverage, monthly EDD | Jan 2026 |
| Retail small-business lending | 2 | 3 | 6 | Sample-based, 5% quarterly | Jan 2026 |

**Rule attached to the map:** any product scoring ≥15 gets full-population monitoring; a resourcing shortfall gets solved by narrowing scope on <10 first, never by thinning coverage on a ≥15 line to spread headcount evenly. If two products both score 16, the tiebreaker is dollar volume at risk, not which business unit complains louder.

## 2. Alert-tuning cadence

Quarterly review of the transaction-monitoring system's scenario thresholds, driven by false-positive rate, not gut feel.

| Scenario | Alerts/month | Cases opened | False-positive rate | Action |
|---|---|---|---|---|
| Structuring (sub-threshold cash pattern) | 340 | 28 | 91.8% | Hold — FP rate high but true-positive yield (structuring is a felony) justifies the noise; do not raise threshold |
| Rapid movement of funds (in-and-out <48hr) | 890 | 12 | 98.7% | Raise dollar threshold from $5K to $15K; current tuning catches payroll/ACH noise, not laundering |
| High-risk-geography wire | 210 | 41 | 80.5% | Hold — geography list is regulator-driven, not discretionary |
| Dormant-account reactivation | 155 | 3 | 98.1% | Retire scenario or narrow to accounts dormant >18 months (currently triggers at 6 months, too broad) |

**Rule:** a false-positive rate above ~95% on a scenario that produces close to zero regulatory-grade findings over two consecutive quarters is a retuning candidate; a high FP rate on a scenario tied to a felony-level pattern (structuring, sanctions) is not retuned down just to reduce workload — the asymmetry in what's missed if under-tuned outweighs analyst time saved.

## 3. SAR / mandatory-filing workflow

| Day | Step | Owner |
|---|---|---|
| 0 (detection) | Alert/referral logged; SAR clock starts | Monitoring analyst |
| 0–5 | Initial triage: contain exposure, pull account/customer file, beneficial ownership check | Case analyst |
| 5–15 | Investigation: transaction history, KYC file, external checks (adverse media, sanctions lists) | Case analyst + BSA Officer |
| 15–20 | Draft SAR narrative; peer review | Case analyst → BSA Officer |
| 20–25 | Management sign-off; enhanced monitoring flag set if account stays open | BSA Officer |
| 25–30 | File with FinCEN; confirm acknowledgment receipt | BSA Officer |
| Day 30 | Hard deadline (60 if no subject identified) | — |

**Escalation trigger inside the workflow:** if investigation isn't substantially complete by day 20, escalate to BSA Officer for a go/no-go on filing with available information rather than waiting past the deadline for a complete picture — an incomplete-but-timely SAR is compliant; a complete-but-late one is a separate violation.

## 4. SAR narrative template (filled)

> **Filing institution:** [Bank name, EIN]. **Subject:** [Business name, EIN, account #]. **Activity dates:** Feb 5–Feb 26, 2026. **Total amount:** $133,400 across 14 transactions.
> **Narrative:** Subject conducted 14 cash deposits ranging $9,200–$9,900 (average $9,528.57) across three branch locations over a 22-day period, with no two transactions occurring on the same business day and no individual or same-day-aggregated transaction reaching the $10,000 CTR reporting threshold. The consistent sub-threshold sizing, cross-branch distribution, and even day-spacing are consistent with structuring to avoid CTR filing requirements under 31 U.S.C. § 5324. [Institution] reviewed transaction and account history for the preceding 12 months and found no comparable pattern prior to Feb 5, 2026. Beneficial ownership on file was last certified [date]; refresh initiated independent of this filing. Account remains open under 90-day enhanced monitoring pending further activity review.

## 5. Regulatory exam finding tracker (MRA/MRIA-style)

| Finding # | Description | Rating | Committed date | Status | Independent retest |
|---|---|---|---|---|---|
| 2025-EX-03 | Beneficial-ownership refresh cycle exceeds 12-month policy on 18% of sampled high-risk accounts | MRA | Jun 30, 2026 | On track — 62% remediated | Not yet (gate before closure) |
| 2025-EX-07 | Wire-transfer dual-control exception log incomplete for Q4 2025 | MRA | Mar 31, 2026 | Past due — escalate to committee | N/A, overdue |
| 2025-EX-11 | Training completion rate for BSA refresher below 95% policy floor (89% actual) | Self-identified | Apr 15, 2026 | Closed, retested | Passed, Apr 22, 2026 |

**Rule:** a finding is not closed on "remediation implemented" — it's closed on independent retest confirming the fix holds under a live sample, dated after the remediation date, by someone other than the person who built the fix.

## 6. Training completion dashboard (by unit, not org-wide average)

| Business unit | Headcount | Completed | Rate | Avg completion time | Flag |
|---|---|---|---|---|---|
| Retail branch staff | 240 | 238 | 99.2% | 34 min | none |
| Commercial relationship managers | 45 | 39 | 86.7% | 41 min | below 95% floor — escalate to unit head |
| Wire operations | 18 | 18 | 100% | 6 min | flag — completion time implies click-through, not engagement; spot-check comprehension |
| Executive leadership | 12 | 9 | 75.0% | — | escalate to CEO/board directly, not through normal channel |

**Rule:** a 100% completion rate paired with a completion time under half the median for that module is treated as a data-quality flag, not a success — it usually means click-through without reading, and gets a comprehension spot-check before being reported up as compliant.

## 7. Variant note — healthcare compliance (HIPAA breach path)

Same contain → scope → classify-clock → remediate → root-cause order, different clock and threshold: a breach affecting ≥500 individuals requires notification to HHS OCR and local media within 60 days of discovery (not detection of root cause); under 500, annual OCR log suffices but individual notification is still due within 60 days. The materiality question changes too — "material" here is defined by whether unsecured PHI was accessed, viewed, or acquired, not by dollar exposure, so a $0-loss access event can still be a reportable breach if PHI was viewed without authorization.
