# Braided-funding playbook — templates with real structure

Filled with Bridgeway Community Services' FY26 numbers: a $4.2M-budget agency running permanent supportive housing (PSH, HUD CoC-funded), rapid re-housing (RRH, state ESG plus county funds), and outpatient behavioral-health case management (Medicaid FFS, a county block grant, and a foundation general-operating grant).

## 1. Braided-budget reconciliation (indirect-cost gap)

The recurring problem: government grants cap the administrative/indirect dollars they'll pay well below the organization's real indirect rate. The gap has to be named and assigned to a specific source — it does not net out on its own.

| Funding source | Award | Admin/indirect cap | Recoverable indirect | Direct program cost |
|---|---|---|---|---|
| HUD CoC (PSH) | $1,800,000 | 7% of award (24 CFR 578.63) | $126,000 | $1,674,000 |
| State ESG + county (RRH) | $900,000 | 7% of award (24 CFR 576.21) | $63,000 | $837,000 |
| Medicaid FFS (case mgmt.) | $700,000 | none — embedded in billed rate | $0 | $700,000 |
| County MH block grant | $500,000 | 12% of award | $60,000 | $440,000 |
| Foundation general-operating grant | $300,000 | unrestricted — no cap | flexible | $300,000 |
| **Total** | **$4,200,000** | | **$249,000 capped-recovery** | **$3,951,000 MTDC** |

**True indirect need:** at Bridgeway's 10% de minimis rate (2 CFR 200.414) applied to $3,951,000 modified total direct costs (MTDC) = **$395,100**.

**Gap:** $395,100 − $249,000 recoverable from capped sources = **$146,100**, which must come from the one uncapped source — the $300,000 foundation general-operating grant. That leaves $153,900 of the foundation grant's $300,000 for direct flexible use (bridge funding for drawdown lag, unbudgeted client emergency needs, the board-designated reserve).

**Reading it like a program director:** the $249,000 "recovered" line is a ceiling set by funders, not a measure of actual overhead cost — it will not move even if the agency's real overhead (finance, HR, IT, facilities) grows. Every new restricted grant added to the portfolio without its own uncapped counterpart shrinks the $153,900 flexible cushion further. If the foundation grant is ever reduced or not renewed, the $146,100 gap has nowhere else to land except a real cut to overhead capacity — track this ratio (uncapped flexible dollars ÷ total indirect gap) every budget cycle, not just when a grant is up for renewal.

## 2. Indirect cost rate election

Two paths under 2 CFR 200.414, decided once and then followed for the life of that election:

| | 10% de minimis rate | Negotiated Indirect Cost Rate Agreement (NICRA) |
|---|---|---|
| Setup cost | None — election is automatic if never negotiated a rate before | Requires a cost allocation study/proposal submitted to the agency's cognizant federal agency; 2–6 months to negotiate |
| Typical resulting rate | Flat 10% of MTDC | Often 12–18% of MTDC for agencies with real facilities/admin overhead, sometimes lower for very lean operations |
| Best for | Agencies whose real overhead is close to 10%, or that can't absorb the negotiation cost/time | Agencies whose real overhead is materially above 10% and that expect $2M+/year in federal pass-through funding for several years |
| Bridgeway's situation | Currently on de minimis | A cost study estimated Bridgeway's real overhead rate at ~13.5% of MTDC — negotiating a NICRA would recover an incremental ~$138,000/year (3.5% × $3,951,000) from federal sources, but the county block grant and foundation grant aren't obligated to honor a NICRA above their own stated caps, so only the HUD and Medicaid-adjacent federal share would benefit |

**Rule of thumb:** negotiate a NICRA when federal direct-funded MTDC exceeds roughly $2M/year for 3+ years and the gap between de minimis and the real rate is more than 2–3 points — under that, the negotiation cost and multi-month lag aren't worth it.

## 3. Caseload / staffing model

| Program | Staffing-model ratio | Budgeted FTEs | Target caseload | Current actual caseload | Status |
|---|---|---|---|---|---|
| PSH intensive case management | 1:20 (CSH guidance, high-acuity PSH) | 6.0 FTE case managers | 120 clients | 142 clients (23.7:1) | 1.18x ratio — monitor |
| RRH case management | 1:17 (shorter-term, lower-acuity) | 3.0 FTE | 51 households | 71 households (23.7:1) | 1.39x ratio — approaching escalation threshold |
| Outpatient behavioral health | 1:25 (non-intensive) | 8.0 FTE | 200 clients | 268 clients (33.5:1) | 1.34x ratio — approaching escalation threshold |

**Vacancy-adjusted staffing:** Bridgeway's trailing-12-month case-management turnover is 44%. Budgeting 6.0 FTE for PSH assuming full staffing ignores that, at 44% annual turnover with an average 11-week vacancy-to-fill cycle, each position sits open roughly 0.44 × 11/52 = 9.3% of the year, so the program actually operates at ~5.4 FTE most of the year (6.0 × (1 − 0.093)) — the 120-client target caseload was never realistic against the budgeted headcount; it was realistic only against a headcount the org rarely has filled. Rebuild the target caseload from the vacancy-adjusted FTE (5.4 × 20 = 108), and treat the difference between 120 and 108 as the actual overflow the program absorbs, not a temporary staffing gap.

**Escalation threshold:** at 1.4x the staffing-model ratio sustained for a full quarter, open a hiring-or-scope conversation with the board/ED — do not wait for a caseload-driven incident to force it.

## 4. Drawdown / reimbursement calendar

| Grant | Basis | Draw frequency | Typical lag (submission → cash) | Bridgeway's bridge |
|---|---|---|---|---|
| HUD CoC (PSH) | Reimbursement, via eLOCCS | Monthly | 5–10 business days | $150,000 revolving line of credit |
| State ESG (RRH) | Reimbursement, state portal | Quarterly | 30–45 days | Same line of credit |
| Medicaid FFS | Claims-based | Bi-weekly billing cycle | 14–21 days | Cash reserve (target 60 days unrestricted opex) |
| County MH block grant | Advance, quarterly | Quarterly | Received in advance — no bridge needed | n/a |
| Foundation grant | Milestone/annual disbursement | Annual | Received on schedule per grant agreement | n/a |

**Rule:** any reimbursement-basis grant more than 45 days past the end of its billing period without a submitted draw is a standing escalation item at the monthly finance meeting — the lag compounds, since the next period's draw can't be prepared cleanly on top of an unreconciled prior one.

## 5. Outcome reporting — logic model skeleton (PSH, HUD APR-aligned)

| Inputs | Activities | Outputs | Outcomes (HUD APR-reportable) | Bridgeway's CQI-only metric (not funder-reported) |
|---|---|---|---|---|
| 6.0 FTE case managers, $1.8M HUD CoC grant, master-leased units | Housing placement, weekly case management contact, benefits enrollment | Units leased-up within 30 days of referral; contacts completed per month | % exits to permanent housing (HUD target: ≥80% of exits); % retaining housing ≥12 months | Median days from first missed contact to re-engagement attempt (internal early-warning metric, not funder-required) |

**Why the CQI-only column exists:** the funder's metric (exits to permanent housing) rewards a narrow definition of success and creates pressure to under-enroll higher-risk referrals who are less likely to hit it. Tracking re-engagement speed internally gives the program a defensible answer when a harder-than-average intake cohort produces a lower exit rate in a given APR period — the CQI data shows the program caught disengagement early rather than let it become an unexplained miss.
