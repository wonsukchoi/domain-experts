# Credit analyst working vocabulary

Terms this desk uses precisely. Format: definition → how a practitioner says it → common misuse.

**DSCR (debt service coverage ratio)** — Cash flow available for debt service (typically EBITDA minus cash taxes minus maintenance capex) divided by total debt service (interest plus scheduled principal) for the period.
In use: "DSCR is 1.45x on the base case, but only 1.20x once we strip the top customer — that's the number driving the covenant package."
Misuse: computing it off unadjusted EBITDA (ignoring maintenance capex and cash taxes), which overstates coverage — a business reinvesting heavily in capex can show strong EBITDA-based coverage while having almost no actual cash left for debt service.

**Leverage (Debt/EBITDA)** — Total interest-bearing debt divided by EBITDA (adjusted, with evidenced addbacks only); the headline measure of how many years of earnings it would take to retire the debt.
In use: "We're at 2.5x post-close; the covenant caps us at 3.0x, so there's room for one more equipment financing before we trip it."
Misuse: comparing leverage multiples across borrowers with different cash-flow volatility as if 3x means the same risk everywhere — a recurring-revenue business can safely carry more leverage than a project-based one at the identical multiple.

**FCCR (fixed charge coverage ratio)** — Similar to DSCR but the denominator adds fixed obligations beyond scheduled debt service — most often operating lease payments — since EBITDA already nets those out as an operating expense.
In use: "FCCR is 1.37x against a 1.20x covenant floor — the lease payment is what widens the gap from DSCR."
Misuse: using DSCR and FCCR interchangeably when the credit agreement specifies one — they diverge meaningfully for a borrower with sizeable lease obligations, and citing the wrong one in the memo misstates actual covenant headroom.

**Global cash flow** — Combined analysis of business cash flow and the personal cash flow of an owner/guarantor, used when the credit relies on a personal guarantee.
In use: "Business DSCR is fine at 1.4x, but on a global basis, once you add his two rental-property mortgages, combined coverage drops to 1.05x."
Misuse: skipping it for closely held companies because the business financials "look fine" — the guarantee exists precisely because the bank expects to need the personal side someday, so it should be underwritten now, not discovered at default.

**Risk rating (internal grade)** — The bank's internal score (often a 1–10 numeric scale, with 1–6 typically "Pass" grades) summarizing probability of default for a specific borrower, mapped to the regulatory classification below.
In use: "Recommending a 4 — Pass, but not a 3, given the concentration issue we haven't mitigated yet."
Misuse: treating the rating as a single number derived from one ratio (usually leverage or DSCR) rather than the analyst's synthesis of repayment capacity, collateral, and structure under both base and stress cases.

**Pass / Special Mention / Substandard / Doubtful / Loss** — The regulatory (OCC-aligned) classification scale for problem-credit severity: Pass is satisfactory; Special Mention has potential weaknesses meriting management's close attention; Substandard has a well-defined weakness that jeopardizes repayment; Doubtful makes full collection improbable; Loss is considered uncollectible.
In use: "This one's trending toward Special Mention next quarter if the covenant breach isn't cured — flag it now, not after the test date."
Misuse: using "Substandard" loosely to mean "risky" — it's a defined regulatory term tied to specific criteria (a well-defined weakness that jeopardizes orderly repayment), not a synonym for "we're a little worried."

**Borrowing base** — The maximum draw available on an asset-based revolver, computed as eligible collateral times an advance rate (e.g., 80% of eligible AR plus 50% of eligible inventory), after excluding ineligible collateral.
In use: "Borrowing base supports a $1.8M draw against the requested $2M line — we're structuring the facility to the smaller number."
Misuse: applying the advance rate to gross AR/inventory instead of eligible collateral — over-90-day receivables, related-party receivables, and obsolete inventory don't count and inflate the apparent availability if left in.

**Covenant headroom** — The cushion between a borrower's actual ratio and the level at which a covenant breaches.
In use: "Only 8% headroom on the leverage covenant at the last test — that's the one to watch, not the DSCR covenant sitting at 25%."
Misuse: monitoring headroom only at the trailing test date rather than projecting it forward — by the time the actuals breach, the borrower is negotiating a waiver from a position of weakness instead of having a conversation ahead of it.

**Maintenance capex vs. growth capex** — Maintenance capex replaces existing capacity (keeps the business as-is); growth capex adds new capacity or capability.
In use: "Only the $150K maintenance piece comes out of CFADS — the CNC line is growth capex, funded by the new facility itself, not a drag on existing coverage."
Misuse: netting all capex out of cash available for debt service, which understates coverage for a borrower making a one-time expansion investment, or netting none out, which overstates it for a borrower under-investing in upkeep.

**Addback** — An adjustment to reported EBITDA to reflect a claimed one-time or non-economic item (owner comp above market rate, a litigation settlement, a bad-debt writeoff).
In use: "We accepted the owner-comp addback against a market-comp survey; we rejected the 'one-time' consulting fee since it's shown up three years running."
Misuse: accepting addbacks on the borrower's assertion alone — every addback needs independent evidence or it should be excluded from adjusted EBITDA.

**Repayment source (primary vs. secondary)** — Primary source is operating cash flow generated by the business; secondary source is collateral liquidation or guarantor support if the primary source fails.
In use: "Primary repayment is operating cash flow; secondary is the equipment lien — that's why we're securing the term loan instead of leaving it unsecured."
Misuse: writing "adequately collateralized" in a memo as if it answers the underwriting question — it answers a different one (recovery if things go wrong), and a memo that leads with collateral instead of the primary source is usually compensating for a repayment-capacity analysis that wasn't done.

**Concentration risk** — Repayment dependency on a single customer, supplier, product line, or geography large enough that its loss materially impairs the borrower's cash flow.
In use: "28% of AR from one customer means we underwrite this as two obligors, not one."
Misuse: measuring concentration only against revenue and missing AR concentration, which can be higher and more immediately dangerous (a slow-pay or bankruptcy at that customer hits cash directly).

**Springing covenant** — A covenant that only activates once a triggering condition is met (e.g., a cash sweep that only applies once customer concentration exceeds a stated threshold, or a covenant that only tests once revolver utilization crosses a level).
In use: "We don't need a standing concentration covenant if the springing cash sweep at 25% concentration does the same job with less friction day to day."
Misuse: assuming a springing covenant is weaker than a standing one — it can be a more precisely targeted protection, activating exactly when the risk it addresses actually materializes.
