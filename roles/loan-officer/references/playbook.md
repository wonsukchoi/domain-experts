# Loan officer playbook — worksheets, timing, and lock tables

Filled templates for the three recurring mechanical jobs: qualifying the ratios, tracking TRID timing, and pricing the rate lock.

## DTI/LTV qualification worksheet

| Line | Source | Example value |
|---|---|---|
| Gross monthly income (verified) | Paystubs (2 most recent) + W-2s (2yr), or 1040s + Schedule C/K-1 trended 2yr for self-employed | $9,500 |
| Proposed P&I | Amortization at note rate — **never the bought-down or teaser rate** | $2,452 |
| Property tax (monthly) | County assessor / 1% of value if not yet assessed, escrowed | $420 |
| Homeowners insurance (monthly) | Quote or 0.35–0.5%/yr of dwelling value estimate | $150 |
| HOA dues (monthly, if any) | HOA cert / listing | $0 |
| Mortgage insurance (monthly) | See PMI/MIP table below | $173 |
| **Front-end housing payment (PITIA)** | Sum of above | **$3,195** |
| Recurring debt (min. payments only, >10 months remaining) | Credit report — exclude debts with <10 payments left per most agency guidelines | $755 |
| **Total monthly obligations** | PITIA + recurring debt | **$3,950** |
| Front-end DTI | PITIA ÷ gross income | 33.6% |
| Back-end DTI | Total obligations ÷ gross income | 41.6% |

**Program DTI ceilings (general, always check current AUS/overlay output):**

| Program | Back-end ceiling (typical) | Notes |
|---|---|---|
| Conventional (agency, AUS-approved) | 45–50% with strong compensating factors (reserves, 720+ score, <75% LTV) | 36–43% is "clean" without extra documentation |
| FHA | ~43% baseline, up to ~50–56.9% with compensating factors under HUD 4000.1 | Compensating factors documented explicitly in file notes |
| VA | No hard DTI ceiling — residual income test is primary; DTI is a secondary indicator | Residual income by region/family size, not a single ratio |
| QM (general, price-based test) | No fixed 43% hard cap post-2021 rule — qualifies if APR ≤ APOR + 2.25 pts (first-lien) | Replaces the old 43%-DTI-only general QM test; agency/GSE loans use agency ratios above regardless |

**LTV / mortgage insurance table:**

| LTV band | PMI/MIP treatment |
|---|---|
| ≤80% conventional | No PMI required |
| 80.01–95% conventional | BPMI or LPMI required; BPMI cancels automatically at 78% of original value (normal am. schedule) or on request at 80% (Homeowners Protection Act) |
| >95% conventional | Available on some agency programs with overlays; reserves/score requirements tighten |
| FHA, any LTV | Upfront MIP 1.75% of base loan amount (financed) + annual MIP ~0.55–0.75%/yr depending on term/LTV; MIP for LTV >90% lasts life of loan, ≤90% LTV cancels after 11 years |
| VA | No monthly MI; VA funding fee (upfront, financeable) varies by down payment % and first-use vs. subsequent use |

## TRID timing table

| Event | Deadline | Resets on |
|---|---|---|
| Loan Estimate (LE) issued | Within 3 business days of receiving all 6 trigger items (name, income, SSN, property address, est. value, loan amount) | N/A — this is intake-to-LE, one-time per application |
| Revised LE | Within 3 business days of a valid changed circumstance | Rate lock, changed circumstance affecting fees, new information changing eligibility |
| Closing Disclosure (CD) received by borrower | At least 3 business days before consummation | — |
| **CD clock restart triggers** | New 3-business-day wait required | APR increases >1/8 pt (fixed) or >1/4 pt (ARM); loan product changes (e.g., fixed→ARM); prepayment penalty added |
| **CD clock does NOT restart** | Same-day/next-day closing possible | Minor fee corrections within tolerance, non-numerical clerical corrections |
| Fee tolerance — zero tolerance | Cannot increase at all | Fees paid to lender/broker/affiliate, transfer taxes |
| Fee tolerance — 10% cumulative | Sum of this category can't increase >10% | Recording fees, third-party services borrower didn't shop (from lender's provider list) |
| Fee tolerance — no limit | Can change freely if borrower shopped or it's use-based | Prepaid interest, homeowner's insurance, initial escrow deposits, services borrower shopped for themselves |

## Rate-lock / float-down decision table

| Lock length | Typical cost vs. 30-day baseline | When to use |
|---|---|---|
| 15 days | ~0.125 pt cheaper | Refi with no appraisal/title contingency, file already clear-to-close pending |
| 30 days | Baseline | Purchase with appraisal already ordered, no condo/co-op review needed |
| 45 days | ~+0.125–0.25 pt | Standard purchase with appraisal + title + AUS conditions outstanding |
| 60 days | ~+0.25–0.375 pt | New construction, condo warrantability review, or any file with a known slow condition (e.g., trust review, non-arm's-length appraisal) |
| Float-down option | ~+0.25–0.5 pt added to lock cost | Add when market has been trending down and there's ≥2 weeks left before CTC to actually exercise it — worthless if added the week of closing |

**Decision rule:** price the lock to the realistic condition-clearing timeline, not the borrower's preferred closing date. If DTI/LTV headroom is under 2 points, prefer the next-longer lock tier over the cheaper one — an extension fee or a repriced rate on a thin file costs more than the extra lock points.

## Handoff checklist to underwriting

- [ ] DTI (front/back) computed off verified, trended (if self-employed) income — method stated explicitly
- [ ] LTV/CLTV computed off lower of price or appraised value, with appraisal date noted
- [ ] Compensating factors documented if within 2 points of program ceiling (reserves in months, credit score, LTV cushion)
- [ ] Large/undocumented deposits flagged with source-of-funds requested, not assumed
- [ ] Mortgage insurance type (BPMI/LPMI/MIP/funding fee) selected and rationale (hold-period based) noted
- [ ] Rate lock date, expiration, and float-down terms logged in LOS
- [ ] Any changed circumstance since initial LE logged with re-disclosure date
