# CFO artifacts — templates with real structure

Working templates an agent can fill in. Example numbers throughout are for a $20M ARR SaaS company, ~110 employees, burning ~$350K/month, $8.5M cash. US-GAAP context.

## 1. 13-week cash flow forecast

Direct method (actual cash in/out, not P&L accruals). Maintained weekly; week 1 becomes "actual" every Monday and a new week 13 is added. Owner: controller builds, CFO reviews. Forecast-to-actual variance in weeks 1–2 should stay under 5%; if it doesn't, fix the collections/AP inputs before trusting anything else.

**Structure:** rows = cash lines, columns = 13 weekly buckets + a total column. All figures $000s.

| Line | Wk1 (Jul 6) | Wk2 | Wk3 | Wk4 | Wk5 | Wk6 | Wk7 | Wk8 | Wk9 | Wk10 | Wk11 | Wk12 | Wk13 | 13-wk total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Beginning cash** | 8,500 | 8,357 | 8,682 | 8,214 | 7,891 | 8,395 | 8,208 | 7,760 | 7,442 | 7,905 | 7,676 | 7,214 | 6,871 | 8,500 |
| **Receipts** | | | | | | | | | | | | | | |
| — AR collections (existing invoices) | 310 | 640 | 180 | 220 | 890 | 240 | 160 | 210 | 820 | 260 | 190 | 230 | 610 | 4,960 |
| — New bookings cash (annual prepay) | 60 | 90 | 45 | 0 | 120 | 75 | 40 | 55 | 130 | 60 | 45 | 50 | 140 | 910 |
| — Other (interest income, refunds) | 8 | 0 | 0 | 8 | 0 | 0 | 8 | 0 | 0 | 8 | 0 | 0 | 8 | 40 |
| **Total receipts** | 378 | 730 | 225 | 228 | 1,010 | 315 | 208 | 265 | 950 | 328 | 235 | 280 | 758 | 5,910 |
| **Disbursements** | | | | | | | | | | | | | | |
| — Payroll + taxes (bi-weekly) | 0 | 620 | 0 | 625 | 0 | 625 | 0 | 630 | 0 | 630 | 0 | 640 | 0 | 3,770 |
| — Benefits (monthly, 1st) | 95 | 0 | 0 | 0 | 96 | 0 | 0 | 0 | 96 | 0 | 0 | 0 | 97 | 384 |
| — Rent (monthly, 1st) | 48 | 0 | 0 | 0 | 48 | 0 | 0 | 0 | 48 | 0 | 0 | 0 | 48 | 192 |
| — SaaS/hosting (AWS ~15th) | 120 | 35 | 210 | 40 | 118 | 32 | 215 | 38 | 122 | 35 | 218 | 40 | 125 | 1,348 |
| — Contractors/agencies | 40 | 30 | 45 | 25 | 35 | 30 | 50 | 25 | 40 | 30 | 45 | 25 | 35 | 455 |
| — Insurance, legal, other AP | 35 | 45 | 28 | 40 | 32 | 45 | 30 | 40 | 35 | 42 | 28 | 38 | 35 | 473 |
| — Sales tax / est. income tax | 0 | 0 | 85 | 0 | 0 | 0 | 90 | 0 | 0 | 0 | 92 | 0 | 0 | 267 |
| — Debt service (interest, monthly) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| — Capex | 0 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 25 |
| **Total disbursements** | 521 | 405 | 693 | 551 | 506 | 502 | 656 | 583 | 487 | 557 | 697 | 623 | 550 | 7,331 |
| **Net cash flow** | (143) | 325 | (468) | (323) | 504 | (187) | (448) | (318) | 463 | (229) | (462) | (343) | 208 | (1,421) |
| **Ending cash** | 8,357 | 8,682 | 8,214 | 7,891 | 8,395 | 8,208 | 7,760 | 7,442 | 7,905 | 7,676 | 7,214 | 6,871 | 7,079 | 7,079 |
| Memo: revolver availability | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | 2,000 | — |
| Memo: total liquidity | 10,357 | 10,682 | 10,214 | 9,891 | 10,395 | 10,208 | 9,760 | 9,442 | 9,905 | 9,676 | 9,214 | 8,871 | 9,079 | — |

**Reading it like a CFO:** the intra-month sawtooth (payroll weeks vs. collection weeks) is normal — what matters is the trend of the trough. Trough here is $6.87M in week 12; if the trough trends down more than one payroll cycle ($625K) per quarter beyond planned burn, something in collections or spend has slipped. Weeks 5/9/13 spike because most invoices are monthly-anniversary annual prepays landing early in the month.

## 2. Board finance slide (quarterly pack)

One primary slide + one appendix table. Same layout every quarter; never reorder or redefine metrics silently.

**Slide layout (quadrants):**

| Top-left: Headline KPIs | Top-right: ARR bridge |
|---|---|
| ARR: $20.0M (+40% YoY) · NRR: 108% · Gross margin: 76% · Rule of 40: 40+(-21) = 19 | Opening $18.6M → New $1.9M → Expansion $0.7M → Contraction ($0.4M) → Churn ($0.8M) → Closing $20.0M |
| **Bottom-left: Cash & runway** | **Bottom-right: Plan vs. actual** |
| Cash $8.5M · Net burn $350K/mo (was $310K) · Runway 24 mo · Next raise: not before Q3-27 | Revenue: $4.9M vs $5.1M plan (-4%) · Opex: $6.2M vs $6.3M plan · Burn: $1.05M vs $0.95M plan (+11% — driver: 2 early sales hires + AWS overage) |

**Rules:** every variance >5% vs. plan gets a one-line driver, on the slide, not in Q&A. The worst number of the quarter (here, burn +11%) is stated with its cause and the corrective action. Appendix carries the full P&L, balance sheet, and the same 13-week cash summary the team runs internally — boards trust packs that show the actual operating tools.

## 3. Scenario model skeleton (base / bear / bull)

Three-column driver-based model; only assumptions differ, formulas identical. Refresh quarterly and before any financing decision. The bear case is the gating test for commitments — not the base.

**Assumption block (FY26, starting ARR $20M):**

| Driver | Bear | Base | Bull |
|---|---|---|---|
| New ARR bookings | $5.5M | $8.0M | $10.5M |
| Gross churn (annual) | 12% | 9% | 7% |
| Net revenue retention | 100% | 108% | 115% |
| Ending ARR | $24.2M | $28.0M | $31.5M |
| Gross margin | 73% | 76% | 78% |
| Sales hires (net adds) | 2 | 6 | 10 |
| Total headcount (year-end) | 112 | 124 | 138 |
| Avg monthly net burn | $500K | $350K | $420K* |
| Year-end cash (from $8.5M) | $2.5M | $4.3M | $3.5M |
| Runway at year-end | 5 mo | 12 mo | 8 mo† |

\* Bull burns more than base — growth is bought. † Bull's shorter runway is fine only because bull-case metrics support raising at will. The dangerous quadrant is bear-case burn with base-case hiring already committed.

**Trigger rules attached to the model (pre-committed, not decided in the moment):**
- If two consecutive quarters track bear on bookings → freeze non-quota hiring; cuts sized to restore 18-month runway within one quarter.
- If cash < $5M with no term sheet in hand → begin raise/RIF planning immediately.
- If tracking bull for two quarters → release the incremental hiring plan already pre-approved by the board.

## 4. Annual budget process calendar (calendar-year company)

| When | What | Owner | Output |
|---|---|---|---|
| Early Sep | Kickoff: CEO/CFO set top-down targets (ARR growth %, burn ceiling, Rule-of-40 floor) | CFO | 1-page targets memo |
| Mid Sep | Templates + headcount request forms to department heads; prior-year run-rates preloaded | FP&A | Dept budget workbooks |
| Early Oct | Bottom-up submissions due | Dept heads | First-pass consolidation (always 15–25% over target — plan for it) |
| Mid Oct | Reconciliation round 1: CFO + each dept head, cut to within ~8% of target | CFO | Revised submissions |
| Early Nov | CEO tiebreaker session on remaining gaps; sales capacity plan locked (quota × ramp × headcount must support the ARR target — check this math explicitly) | CEO/CFO | Near-final budget |
| Mid Nov | Board finance committee preview; incorporate feedback | CFO | Board-ready draft |
| Early Dec | Board approval | Board | Approved operating plan |
| Mid Dec | Load into GL/reporting; set comp letters and quotas effective Jan 1 | Controller/FP&A | Budget of record |
| Feb / May / Aug | Quarterly reforecast: current-year re-projection **replaces** budget for forward-looking decisions; original budget kept only for board variance reporting | FP&A | Rolling forecast |

**Process rules:** headcount is budgeted by named-role start month, not annual dollars — a January hire and an October hire at the same salary differ 4x in-year. Any in-year unbudgeted spend >$50K requires a written trade-off (what gets cut to fund it), not just approval.
