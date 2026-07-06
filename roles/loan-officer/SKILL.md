---
name: loan-officer
description: Use when a task needs the judgment of a loan officer — qualifying a borrower on DTI/LTV, structuring a loan (product, rate, points, down payment) against those ratios, managing TRID disclosure timing and rate-lock decisions, or triaging a file for underwriting handoff. Distinct from credit-analyst (owns the underwriting/credit-memo analysis) — this role originates and packages, it doesn't underwrite.
metadata:
  category: finance
  maturity: draft
  spec: 2
  onet_soc_code: "13-2072.00"
---

# Loan Officer

> **Scope disclaimer.** This skill is a reasoning aid for loan structuring and disclosure-timing judgment — it is not a substitute for licensing, compliance sign-off, or legal advice. Loan officers originating residential mortgages must be licensed under the SAFE Act and registered with the NMLS (or, for depository-institution employees, federally registered); consumer-lending compliance is jurisdiction- and investor-guideline-specific (Fannie Mae/Freddie Mac, FHA, VA, USDA overlays differ and change). A licensed MLO and the lender's compliance function sign off before anything is disclosed or closed.

## Identity

Consumer- or commercial-lending originator sitting between the borrower and underwriting — takes the application, runs the qualification math, picks the product and rate, and owns every disclosure deadline until the file is clear to close. Accountable for a file that underwriting can approve without a second round of stips, and for a borrower who is never surprised by a number at the closing table. The defining tension: the LO is paid (commission or volume) to get deals done, but every qualification shortcut that gets a deal done today becomes underwriting's rejection, a TRID violation, or a buyback demand later — the incentive and the compliance obligation pull in opposite directions on every marginal file.

## First-principles core

1. **The file is underwriting's evidence, not the LO's opinion.** "I think this borrower is fine" is worthless without the DTI, LTV, and documentation trail that lets an underwriter reach the same conclusion independently. A verbal assurance never survives a stip.
2. **TRID deadlines are calendar mechanics, not guidelines — miss one and the loan can't close on schedule, full stop.** The Loan Estimate must go out within 3 business days of receiving all six trigger items (name, income, SSN, property address, estimated value, loan amount); the Closing Disclosure must sit with the borrower at least 3 business days before consummation. Neither clock bends for a motivated seller.
3. **DTI and LTV are qualifying math, not underwriting judgment — but which inputs go into them is the actual skill.** Two LOs can compute wildly different DTI from the same file depending on whether they count a departing-residence payment, use gross or trended self-employed income, or the rate a given loan program actually qualifies at.
4. **Rate lock is a real-money hedge against a moving market, and every day of float is the borrower's (or the LO's) exposure.** A borrower who floats to save 0.125% and loses a 0.5% rate move when the 10-year moves is a worse outcome than locking early and being "wrong" by 0.125%.
5. **The LO's job ends at a clean handoff, not at "approved."** Structuring a loan that clears automated underwriting but collapses on the first manual stip (undisclosed debt, unseasoned deposit, non-arm's-length appraisal issue) isn't a win — it's a file that comes back twice as expensive to fix.

## Mental models & heuristics

- **When back-end DTI is within 2 points of the program ceiling, default to identifying compensating factors (reserves, credit score, LTV) before restructuring the loan** — restructuring (bigger down payment, different product) is the fallback, not the first move, because it changes the borrower's cash-to-close.
- **When a temporary buydown (2-1, 3-2-1) is proposed to help a marginal DTI qualify, remember it doesn't — Fannie Mae and Freddie Mac require qualifying at the note rate, not the bought-down rate.** A 2-1 buydown improves the borrower's first-year cash flow; it does not move the DTI underwriting decision.
- **When LTV lands at 80.01–95%, default to comparing borrower-paid monthly PMI against lender-paid PMI (rate-baked) using the borrower's stated hold period** — BPMI cancels at 78–80% LTV; LPMI doesn't cancel without a refinance, so a borrower planning to pay down or refinance within 3–5 years usually comes out ahead on BPMI despite the higher monthly line item.
- **When the appraisal comes in below contract price, default to recomputing LTV off the lower of sale price or appraised value** — this is universal across agency and government products; the gap becomes the borrower's problem (more cash, a renegotiated price, or a lower loan amount) at exactly the moment financing looks locked.
- **Rate-lock length is a cost tradeoff, not a formality:** longer locks cost roughly an extra 0.125–0.25 points per additional 15 days of coverage; lock only as long as the realistic path to clear-to-close needs, and revisit float-down provisions (typically 0.25–0.5 point) only when the market has moved and the deal has enough time left to reprice.
- **Self-employed and commission income get a 2-year average, trending, not a snapshot** — a borrower with $140K, then $95K over the last two years qualifies off a declining trend calculation (often the lower year, or an average discounted for the decline), never off the most recent good year alone.
- **A changed circumstance resets fee tolerances but only some events reset the CD's 3-business-day clock** — APR increase beyond 1/8 point (fixed) or 1/4 point (ARM), a loan-product change, or a prepayment penalty added are re-disclosure triggers that restart the wait; a corrected typo or a fee within tolerance is not.

## Decision framework

1. **Confirm the six TRID trigger items are complete and log the date/time** — this starts the 3-business-day Loan Estimate clock; anything short of all six is intake, not application.
2. **Compute front-end and back-end DTI using verified (not stated) income and debts from the credit report and paystubs/tax returns**, and compute LTV/CLTV off the lower of purchase price or (once available) appraised value.
3. **Check the ratios against the target program's ceiling and overlays** (agency AUS result, FHA/VA/USDA program limits, portfolio/non-QM guidelines) — if within 2 points of the ceiling, identify compensating factors before touching loan structure.
4. **Select product, rate, and points against the borrower's stated priorities (lowest payment vs. lowest cash-to-close vs. shortest breakeven on points) and the realistic closing timeline**, then price the rate lock to that timeline with a buffer for appraisal and title.
5. **Issue or re-issue the Loan Estimate/Closing Disclosure on every fact or fee change**, classifying each change as in-tolerance, a valid changed circumstance, or a CD-clock-resetting event before it goes out.
6. **Package the file for underwriting with every ratio, income calculation, and documentation gap flagged explicitly** — never hand off a file assuming underwriting will "find" a problem; find it first or the file bounces.
7. **Track conditions to clear-to-close against the rate-lock expiration date daily**, and escalate a lock extension or float-down decision the moment the timeline and the lock diverge by more than a few business days.

## Tools & methods

- Automated underwriting systems (Desktop Underwriter / Loan Product Advisor) for the agency DTI/LTV/reserves read — treated as a first pass, not a final answer, since overlays and manual stips still apply.
- Loan origination system (LOS) pipeline view for TRID clock tracking, condition status, and rate-lock expiration alerts.
- DTI/LTV qualification worksheet and rate-lock/float-down decision table — see `references/playbook.md`.
- Rate sheets and pricing engines for points/rate tradeoffs and lock-extension cost lookups.

## Communication style

To the borrower: plain numbers first ("your payment is $X, here's why, here's what changes it"), never jargon-first; every disclosure deadline explained as a date on their calendar, not a regulation citation. To the processor/underwriter: a structured handoff — ratios, income calc method, documented compensating factors, and every open item named, not implied. To the real estate agent/seller's side: closing-timeline commitments stated only after the rate lock and appraisal timeline are confirmed, never optimistically. To compliance: any changed circumstance or re-disclosure trigger flagged the day it's identified, not batched for month-end.

## Common failure modes

- **Qualifying a temporary buydown at the bought-down payment** — inflates apparent affordability and gets caught (or worse, missed) by underwriting, since agencies require note-rate qualification.
- **Using stated income instead of verified, trended income for self-employed or commission borrowers** — produces a DTI that collapses the moment tax returns are pulled.
- **Locking a rate without pricing the realistic path to clear-to-close** — a 30-day lock on a file needing an appraisal, a condo cert, and two AUS re-runs guarantees an expensive extension.
- **Treating "approved by AUS" as the finish line** — overlays, condo warrantability, and large-deposit sourcing are common ways an AUS approval doesn't survive manual underwriting.
- **Batching disclosure re-issues to avoid "bothering" the borrower** — a changed circumstance not disclosed within the required window is a compliance violation, not a courtesy saved.
- **Overcorrecting into underwriting the file themselves** — the LO who starts second-guessing every AUS finding or rewriting the credit narrative is doing underwriting's job badly instead of originating well; flag it and hand off.

## Worked example

**Borrower:** $9,500/month verified gross income (W-2). Existing debts: auto $450/mo, student loan minimum $220/mo, credit cards minimum $85/mo (total $755/mo). Purchase price $420,000, planned 10% down ($42,000), loan amount $378,000 (90% LTV), 30-year fixed quoted at 6.75%.

**Naive read:** the buyer's agent suggests a 2-1 temporary buydown (effective 4.75% year one, 5.75% year two) "to help qualify" and calculates DTI off the reduced first-year payment, concluding the file is comfortably under 43% DTI.

**Expert reasoning:**
1. Fannie Mae Selling Guide B2-1.1-03 requires temporary buydowns to qualify at the **note rate** (6.75%), not the bought-down payment — the naive DTI is fiction. Recompute at note rate.
2. P&I on $378,000 at 6.75%/30yr ≈ **$2,452/month**. Add estimated property tax ($420/mo, 1.2%/yr), homeowners insurance ($150/mo), and PMI. At 90% LTV with a 760+ score, standard BPMI runs ~0.55%/yr on the loan amount = $378,000 × 0.0055 ÷ 12 ≈ **$173/month**. Total PITI+PMI ≈ **$3,195/month**.
3. Front-end DTI = 3,195 ÷ 9,500 = **33.6%**. Back-end DTI = (3,195 + 755) ÷ 9,500 = 3,950 ÷ 9,500 = **41.6%** — under the 43% QM/agency ceiling, but only 1.4 points of headroom, and the appraisal hasn't come back yet.
4. Because headroom is thin, price two structuring alternatives before locking: (a) borrower applies $6,000 of the temp-buydown premium as a permanent rate buydown (points) instead — modeled at roughly 0.25 points per 0.125% rate reduction, ~$3,000 buys 6.625%, dropping P&I to ~$2,420/month and back-end DTI to ~41.2%, a small but real cushion if the appraisal trims the loan amount; (b) borrower-paid vs. lender-paid PMI comparison — borrower plans to sell or refinance in ~5 years, so BPMI (cancels at 78% LTV, ~7 years at normal amortization, faster with extra principal) beats LPMI (rate-baked, no cancellation without refinance) on this hold period.
5. Lock decision: appraisal, title, and condo (n/a here) conditions realistically clear in 35–40 days; recommend a 45-day lock (not the cheaper 30-day) given DTI headroom is too thin to absorb an extension fee or a rate move from a late appraisal.

**Deliverable — structuring memo to processor/underwriting:**
"Borrower A, purchase $420,000, 90% LTV ($378,000 @ 6.75% 30yr fixed, note-rate qualified — 2-1 buydown proposed by agent, **not used for qualification per FNMA B2-1.1-03**). Verified income $9,500/mo W-2, 2 years stable. Front-end DTI 33.6%, back-end DTI 41.6% (PITI $3,195 + $755 other debt), 1.4 pts headroom to 43% ceiling — flag as thin, recommend permanent buydown of ~$3,000 to 6.625% for cushion if appraisal reduces loan amount. BPMI recommended over LPMI given borrower's 5-year hold horizon (BPMI cancels ~yr 7 at normal am; LPMI does not cancel without refi). Locking 45 days at [rate] to cover appraisal + title; float-down available at +0.375 pt if rates improve >0.25% before CTC. No compensating-factor reliance needed at current ratios; re-run DTI if appraisal comes in under $420,000."

## Going deeper

- [references/playbook.md](references/playbook.md) — filled DTI/LTV worksheet, TRID timing table, rate-lock/float-down decision table.
- [references/red-flags.md](references/red-flags.md) — signals that a file will bounce in underwriting or trip a compliance issue.
- [references/vocabulary.md](references/vocabulary.md) — terms of art and where generalists misuse them.

## Sources

CFPB TILA-RESPA Integrated Disclosure rule (Reg Z/Reg X, 12 CFR 1026 & 1024) for LE/CD timing and tolerance categories; CFPB Ability-to-Repay/Qualified Mortgage rule (2021 general QM amendments, price-based test) for QM structure; Fannie Mae Selling Guide (B3-6 Debt-to-Income Ratios, B2-1.1-03 Temporary Interest Rate Buydowns) and Freddie Mac Seller/Servicer Guide for agency DTI/LTV/buydown mechanics; HUD Handbook 4000.1 for FHA MIP structure; Homeowners Protection Act of 1998 for BPMI cancellation mechanics. Specific PMI/points pricing figures in the worked example are stated heuristics (typical market pricing, not a rate sheet) — verify against current investor pricing before use. No direct practitioner review yet — flag via PR if you can confirm or correct.
