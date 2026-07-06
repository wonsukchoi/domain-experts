# Credit analyst artifacts — templates with real structure

Filled templates using the ABC Fabricators facts from the SKILL.md worked example: $18M-revenue custom metal fabricator, $3.0M new equipment term loan requested on top of a $2M revolver ($1.2M drawn) and $1.8M existing term debt.

## 1. Credit memo template (filled)

**Borrower:** ABC Fabricators, Inc. — custom metal fabrication, 22 years operating, $18.0M TTM revenue.
**Facility requested:** $3.0M term loan, 5-year, straight-line amortization, to fund a CNC fabrication line.
**Existing exposure:** $2.0M revolver ($1.2M drawn), $1.8M term loan (4 years remaining, $360K/yr principal).
**Purpose:** Equipment purchase to add capacity for an existing customer contract.
**Primary repayment source:** Operating cash flow from continuing fabrication operations.
**Secondary repayment source:** First lien on the financed equipment (recommended — requested as unsecured).

**Financial summary (TTM, $000s):**

| Line | Amount |
|---|---|
| Revenue | 18,000 |
| Reported EBITDA | 2,160 |
| + Owner comp normalization (evidenced: market-comp survey) | 180 |
| + One-time litigation settlement (evidenced: settlement agreement) | 60 |
| **Adjusted EBITDA** | **2,400** |
| Maintenance capex | 150 |
| Cash taxes | 180 |
| Current assets / current liabilities | 4,200 / 2,600 |

**Leverage and coverage — base case:**

| Ratio | Calculation | Result | Covenant floor/cap |
|---|---|---|---|
| Debt/EBITDA | $6,000 / $2,400 | 2.50x | ≤3.00x |
| DSCR | ($2,400−180−150) / (470+960) | 1.45x | ≥1.25x |
| FCCR | 2,070 / (1,430+80) | 1.37x | ≥1.20x |
| Current ratio | 4,200 / 2,600 | 1.62x | RMA NAICS median ~1.5–2.0x |

**Leverage and coverage — stress case (loss of top customer, −$360K EBITDA):**

| Ratio | Result | Covenant floor/cap | Headroom |
|---|---|---|---|
| Debt/EBITDA | 2.94x | ≤3.00x | 0.06x (was 0.50x) |
| DSCR | 1.20x | ≥1.10x | 0.10x (was 0.20x) |

**Strengths:** Base-case leverage and coverage both clear covenants with margin; owner-comp and litigation addbacks independently evidenced, not asserted; current ratio in line with RMA benchmark for the borrower's NAICS code.

**Weaknesses / mitigants:** Top customer = 28% of AR, 15% of EBITDA — stress-case DSCR compresses to the covenant floor. Mitigated by: (1) securing the new term loan on the equipment (not granted in the request), (2) a quarterly-tested minimum FCCR covenant at 1.20x, (3) a springing cash sweep (50% of excess cash flow) if any customer exceeds 25% of trailing-12 revenue.

**Recommendation:** Approve at $3.0M, secured, with the covenant package above. Do not approve unsecured as requested.

**Risk rating recommendation:** Pass — internal grade 4 of 10. Driver: adequate base-case coverage, but customer concentration compresses stress-case DSCR to the floor rather than leaving a cushion; grade 3 requires either a contractual concentration mitigant or the structure above being in place and tested for two quarters.

## 2. Ratio-spread table (3-year trend, for the same borrower)

| Metric | Year -2 | Year -1 | TTM | Direction / read |
|---|---|---|---|---|
| Revenue ($000s) | 15,400 | 16,800 | 18,000 | Growing, decelerating (9.1% → 7.1% YoY) |
| Gross margin | 24.8% | 24.1% | 23.6% | Down 120bps over 2 years — watch, not yet a flag (threshold is 300bps) |
| Adjusted EBITDA margin | 12.9% | 13.0% | 13.3% | Stable |
| Debt/EBITDA | 2.9x | 2.7x | 2.5x (post-close) | Improving pre-close; new debt resets it up modestly |
| DSCR | 1.38x | 1.41x | 1.45x | Stable, base case only |
| Current ratio | 1.55x | 1.58x | 1.62x | Stable, in line with RMA median |
| DSO | 46 days | 49 days | 52 days | Rising — tie to the customer-concentration finding, not treated as independent |
| AR concentration (top customer) | 24% | 26% | 28% | Rising trend — the driver behind the stress-case structuring, not just the current level |

## 3. Borrowing base certificate (illustrative, for the existing $2.0M revolver)

| Line | Amount ($000s) | Advance rate | Available |
|---|---|---|---|
| Gross accounts receivable | 2,850 | — | — |
| Less: over-90-day AR | (210) | — | — |
| Less: related-party AR | (0) | — | — |
| **Eligible AR** | **2,640** | 80% | 2,112 |
| Gross inventory | 1,450 | — | — |
| Less: obsolete/slow-moving (>180 days no movement) | (180) | — | — |
| **Eligible inventory** | **1,270** | 50% | 635 |
| **Total borrowing base** | | | **2,747** |
| Facility commitment | | | 2,000 |
| **Availability (lesser of base or commitment, less drawn)** | | | **800** (2,000 commitment − 1,200 drawn; base supports full commitment) |

**Reading it:** the base ($2,747K) exceeds the $2,000K commitment, so the revolver is fully supported today. The number that matters going forward is the eligible-AR trend — at the current 28%-concentration customer, a slow-pay event pushing that receivable past 90 days would remove it from eligibility and cut the base by roughly $600K (28% of eligible AR × 80% advance rate), which would bind before the commitment does.

## 4. Global cash flow worksheet (owner-guaranteed credit)

| Line | Business | Personal (guarantor) | Combined |
|---|---|---|---|
| Cash flow available for debt service | $2,070K | $95K (K-1 distributions + W-2, net of personal living expense estimate) | $2,165K |
| Debt service obligations | $1,430K (this borrower's facilities) | $72K (personal mortgage + auto, excluding the business guarantee itself) | $1,502K |
| **Global DSCR** | 1.45x | — | **1.44x** |

**Reading it:** in this case the guarantor's personal position doesn't materially change the picture — global DSCR (1.44x) tracks business-only DSCR (1.45x) closely because personal obligations are modest relative to personal cash flow. The worksheet exists precisely to catch the cases where it *doesn't* track — a guarantor carrying two other guaranteed businesses or a large personal mortgage can turn an adequate business DSCR into an inadequate global one, and that's only visible if the personal side is pulled and computed every time, not just when something looks off.
