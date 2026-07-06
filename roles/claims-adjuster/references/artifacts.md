# Claims-handling artifacts — filled templates

Working templates an agent can populate. Section 1 continues the auto total-loss claim from `SKILL.md` (2019 sedan, ACV $9,200, repair estimate $6,900, 75% percentage-threshold state) so that arithmetic stays internally consistent. Sections 2–5 use a separate, self-contained water-loss and auto-fraud pair of claims — each section's numbers reconcile within that section.

## 1. Total-loss worksheet (percentage-threshold state)

| Line | Value |
|---|---|
| Repair estimate | $6,900.00 |
| Actual cash value (ACV), per valuation report | $9,200.00 |
| Repair-to-ACV ratio | 6,900 / 9,200 = **75.0%** |
| State total-loss threshold (this state) | 75% |
| Threshold met? | **Yes — mandatory, not discretionary** |
| Salvage bid (pending, retained by insured) | $2,000.00 (estimate) |
| Settlement offer (retain vehicle) | 9,200.00 − 2,000.00 (salvage) − 500.00 (deductible) = **$6,700.00** |
| Settlement offer (surrender vehicle) | 9,200.00 − 500.00 (deductible) = **$8,700.00** |

**If this were a TLF (Total Loss Formula) state instead:** net estimated salvage value against the repair-plus-ACV comparison rather than against ACV alone. Same raw inputs, different test: repair ($6,900) + salvage ($2,000) = $8,900 vs. ACV ($9,200) → $8,900 < $9,200, so the same vehicle would **not** total under a TLF test at this salvage estimate, despite crossing the flat 75% threshold in a percentage-threshold state. The two frameworks are not interchangeable on the same numbers — always confirm which regime the state uses before running either math.

**Reserve entry (file note, verbatim):**
> "Repair estimate $6,900.00 vs. ACV $9,200.00 = 75.0%, meets [state] total-loss threshold per [statute cite]. Reserve set at $9,200.00 less estimated salvage $2,000.00 = $7,200.00 pending salvage bid confirmation. Salvage bid requested [date]; total-loss valuation letter to follow within [X] business days."

## 2. Xactimate-style line-item estimate (water loss, Category 2 / Class 3)

**Pricing note:** the unit prices below are illustrative, internally-consistent figures chosen to show the estimate's structure — line-item breakdown, O&P treatment, depreciation, net-check math. No verified public regional price-list figures were sourced for this section; don't reuse these unit prices as real pricing.

**Loss:** Washing-machine supply-line failure, kitchen (12' × 14' = 168 sf) and hallway (4' × 18' = 72 sf), hardwood flooring, Category 2 (grey water — contains contaminants, defaults up from Category 1 if source is a failed appliance line rather than a clean supply line break), Class 3 drying (>40% of materials in the affected area are wet, low-permeance assemblies).

| # | Line item | Qty | Unit price | RCV |
|---|---|---|---|---|
| 1 | Air mover, per day (5 units × 4 days) | 20 unit-days | $28.50 | $570.00 |
| 2 | LGR dehumidifier, per day (2 units × 4 days) | 8 unit-days | $65.00 | $520.00 |
| 3 | Antimicrobial/biocide application | 240 sf | $0.32 | $76.80 |
| 4 | R&R drywall, 2-ft flood cut | 120 sf | $3.35 | $402.00 |
| 5 | R&R hardwood flooring, kitchen | 168 sf | $11.85 | $1,990.80 |
| 6 | R&R baseboard | 60 lf | $4.10 | $246.00 |
| 7 | Detach & reset base cabinets | 1 ea | $310.00 | $310.00 |
| 8 | Paint walls, 2 coats | 240 sf | $1.15 | $276.00 |
| 9 | Haul debris / dumpster fee | 1 ea | $425.00 | $425.00 |
| 10 | Mitigation mobilization / equipment setup | 1 ea | $185.00 | $185.00 |
| | **Subtotal (mitigation + repair, before O&P)** | | | **$5,001.60** |
| 11 | Overhead & Profit, 10%+10% (GC-supervised repair lines 4–8 only: $3,224.80 base) | | 20% | $644.96 |
| | **Total RCV** | | | **$5,646.56** |
| 12 | Less recoverable depreciation — flooring line only (12 yrs age / 25-yr life = 48% of line 5) | | 48% of $1,990.80 | ($955.58) |
| | **ACV payment (issued now)** | | | **$4,690.98** |
| 13 | Less deductible | | | ($1,000.00) |
| | **Net check to insured, this cycle** | | | **$3,690.98** |

Recoverable depreciation of **$955.58** is released on submission of a paid invoice or contractor completion certificate showing the flooring was actually replaced — not on a verbal confirmation.

**Category re-check note:** source is a failed appliance supply line (Category 2 by default classification), and the loss sat approximately 18 hours before mitigation began — under the 24–48 hour degradation window, so no upgrade to Category 3 is warranted at this inspection. Re-inspect if drying extends past day 5 without meeting the drying goal (dry standard within 2% of unaffected material moisture content).

## 3. Reservation-of-rights letter (filled excerpt)

**Facts:** Same property, separate loss. Adjuster's moisture-mapping and mold-growth pattern on re-inspection indicate the leak was gradual rather than a sudden pipe burst — wood moisture content gradient (32% at the wall base tapering to 14% eight feet away) is consistent with slow seepage over several weeks, not a single event. Total estimated damage: $22,400. The policy excludes "continuous or repeated seepage or leakage of water... occurring over a period of 14 days or more" (Section I, Exclusion 3.f).

```
Re: Claim No. [XXXXXX] — Reservation of Rights

Dear [Insured],

We acknowledge your claim reported [date] for water damage at [address].
We are continuing to investigate this claim, and this letter is to advise
you that we are doing so under a full reservation of rights.

Specifically, our inspection on [date] found moisture patterns and mold
growth consistent with a leak occurring over an extended period rather
than a single sudden event. Your policy, Section I, Exclusion 3.f,
excludes loss caused by "continuous or repeated seepage or leakage of
water... occurring over a period of 14 days or more." Based on wood
moisture-content testing (32% at the source wall, tapering to 14% at
eight feet), our engineering consultant's preliminary opinion is that
the leak duration exceeds that 14-day threshold.

This letter reserves our right to deny coverage in whole or in part
under Exclusion 3.f, and under any other policy term that later proves
applicable, without waiving any of our rights under the policy or at
law. We are not denying your claim today. We have retained [engineering
firm] to determine leak duration and origin, and we expect their report
by [date]. We will notify you in writing of our coverage decision within
[X] business days of receiving that report.

Please contact [adjuster name/phone] with any questions or additional
information relevant to the duration or cause of this loss.

Sincerely,
[Adjuster], [Carrier]
```

**Why generic language fails here:** a reservation that only said "all terms and conditions of the policy apply" would not name Exclusion 3.f or the moisture-gradient facts triggering it — on later review that reads as no reservation at all, and the carrier loses the protection the letter was supposed to provide.

## 4. SIU referral form (filled)

**Loss:** Separate auto claim, rear-end collision, FNOL taken [date]; recorded statement taken 12 days later.

| Field | Entry |
|---|---|
| **Named indicator** | Narrative/estimate escalation between FNOL and recorded statement |
| **File evidence** | FNOL: claimant estimated "around $4,200 in damage, mostly the bumper." Recorded statement (day 12): claimant now describes "frame damage and a cracked wheel" with a shop estimate of $6,800 — a 61.9% increase ((6,800 − 4,200) / 4,200 = 0.619) with no new damage identified by the carrier's own inspection between the two dates. |
| **Secondary indicator** | Repair shop ("Precision Auto Body") appears on 3 unrelated claims filed with this carrier in the trailing 8 months, 2 of which also show post-FNOL estimate increases >40%. |
| **Verification step taken** | Cross-referenced shop name against carrier's claims database (query: repair-facility name, trailing 12 months) — returned 3 matches. |
| **NOT used as a standalone basis** | Claimant's demeanor in the recorded statement ("seemed nervous") — noted but explicitly excluded from the referral rationale; not a named indicator on its own. |
| **Recommended action** | Hold payment pending SIU review. Request supplemental damage photos and a second independent appraisal before authorizing the shop's revised estimate. Do not escalate to EUO at this stage — no cooperation-clause trigger yet, and the file doesn't yet show a specific sworn-testimony-worthy discrepancy beyond the estimate delta. |
| **Referred by / date** | [Adjuster], [date] |

## 5. Appraisal demand letter (filled)

**Facts:** Same water-loss claim as Section 2. Carrier's estimate: $5,646.56 RCV. Insured's public adjuster estimate: $9,850.00 RCV (74.5% higher: (9,850 − 5,646.56) / 5,646.56 = 0.745). Both estimates agree the loss is covered and agree on scope of rooms affected — the dispute is exclusively the dollar amount of repair, which is what the appraisal clause is for.

```
Re: Claim No. [XXXXXX] — Demand for Appraisal

Dear [Insured / Public Adjuster],

We have received your estimate of $9,850.00 for the water damage repairs
at [address], which differs materially from our estimate of $5,646.56
for the same scope of covered repairs. Because the disagreement between
us concerns solely the amount of the loss and not whether the loss is
covered, we are invoking the Appraisal provision of your policy.

Pursuant to that provision, we name [Appraiser Name, firm] as our
appraiser. Please name your own competent and impartial appraiser in
writing within 20 days of this letter. The two appraisers will then
select an umpire; if they cannot agree on an umpire within 15 days, either
of us may request that a judge of a court of record in [county] appoint
one. The appraisers will separately set the amount of loss; any
disagreement will be submitted to the umpire, and an agreement by any
two of the three will set the amount of loss. Appraisal determines the
dollar amount only — it does not decide coverage, which is not in
dispute on this claim.

Please confirm your appraiser's name and contact information within the
20-day window noted above.

Sincerely,
[Adjuster], [Carrier]
```

**Scope check before sending:** confirm the dispute is genuinely amount-only. If the public adjuster's higher estimate rests on a broader damage scope the carrier disputes (e.g., claiming Category 3 remediation the carrier's inspection didn't support), that is a coverage/scope disagreement, not an amount disagreement — appraisal is the wrong tool and the file needs a coverage opinion instead, not an appraisal demand.
