# CFO working vocabulary

Terms a finance leader uses daily and precisely. Format: definition → how a practitioner says it → common misuse. US-GAAP context.

**Bookings vs. billings vs. revenue vs. ARR** — Bookings = total contract value signed in the period (a sales metric, not GAAP). Billings = what you actually invoiced. Revenue = what GAAP lets you recognize as earned (ASC 606). ARR = the annualized run-rate of active recurring contracts, a point-in-time snapshot.
In use: "We booked $2.4M TCV, billed $1.1M of it, recognized $190K in-quarter, and it added $800K to ARR."
Misuse: treating these as interchangeable. A 3-year $3M deal is $3M bookings, $1M billings (annual invoicing), ~$83K first-month revenue, and $1M ARR. Announcing "we did $3M this quarter" from that deal is how credibility dies.

**Working capital vs. cash** — Working capital = current assets minus current liabilities: the cash tied up in (or released by) operating timing — AR, inventory, AP, deferred revenue. Cash is the balance in the bank.
In use: "We're profitable but working capital ate $600K this quarter — DSO stretched and we prepaid the insurance renewal."
Misuse: assuming profit ≈ cash flow. A fast-growing company with net-60 customers gets *less* cash the faster it grows; a prepaid-SaaS company gets *more* (negative working capital is a feature there).

**Burn (gross vs. net) and runway** — Gross burn = total monthly cash out. Net burn = cash out minus cash in. Runway = cash ÷ net burn, in months.
In use: "Gross burn is $1.8M, net burn $350K, so 24 months of runway — but that assumes collections hold."
Misuse: quoting runway off a stale burn number, or dividing by *average* historical burn when burn is accelerating. Runway is forward-looking or it's fiction.

**Covenant headroom** — The cushion between actual performance and the level at which a debt covenant breaches (e.g., covenant requires ≥1.25x fixed-charge coverage, you're at 1.6x → ~28% headroom).
In use: "We've got 28% headroom on FCCR but only 12% on minimum liquidity — that's the one that binds."
Misuse: monitoring covenants on actuals only. Headroom is managed on the 4-quarter *projection*; by the time actuals breach, your options are a fee-laden waiver or default.

**Covenant-lite (cov-lite)** — Debt with few or no ongoing maintenance covenants (tested only on incurrence events, e.g., taking on more debt).
In use: "It's 100bps more expensive but cov-lite — worth it, given our bookings volatility."
Misuse: assuming cov-lite means consequence-free. Payment defaults, MAC clauses, and springing covenants (which activate when a revolver is drawn past a threshold) still apply.

**Quality of earnings (QoE)** — An analysis (standard in M&A diligence) of how much reported EBITDA/earnings is sustainable and cash-backed versus one-time items, aggressive accruals, or accounting choices.
In use: "Their adjusted EBITDA is $4M but the QoE will knock out half the addbacks — underwrite off $3M."
Misuse: taking "adjusted EBITDA" at face value. The adjustments *are* the negotiation.

**Operating leverage** — The degree to which revenue growth outpaces cost growth because costs are fixed; profit grows faster than revenue once past breakeven.
In use: "We finally have operating leverage — revenue up 40%, opex up 18%, so incremental margin is 60%+."
Misuse: using it to mean "debt leverage," or claiming it while every cost line still scales linearly with revenue. Also cuts both ways: high fixed costs mean a revenue miss hits profit disproportionately.

**Leverage (financial) and net debt** — Financial leverage = debt relative to earnings or equity, most often quoted as net debt (total debt minus cash) ÷ EBITDA.
In use: "We're at 2.1x net levered; the facility caps us at 3.0x, so ~$4M of incremental debt capacity."
Misuse: quoting gross debt when net is the relevant figure (or vice versa when cash is restricted), and comparing leverage multiples across businesses with different EBITDA volatility as if 3x means the same thing everywhere.

**WACC / cost of capital / hurdle rate** — WACC = the blended, after-tax cost of the company's debt and equity, weighted by mix. The hurdle rate is the minimum return an investment must clear — usually WACC plus a risk premium for the specific project.
In use: "At our WACC of ~12%, that 9%-IRR capex is value-destructive even though it's cash-positive."
Misuse: using the *debt* rate as the hurdle because it's visible and cheap. Equity is the expensive component precisely because it's not invoiced.

**NRR / GRR (net vs. gross revenue retention)** — GRR = revenue kept from existing customers excluding expansion (ceiling 100%). NRR = including expansion (can exceed 100%).
In use: "NRR is 108% but GRR is 84% — expansion from a few accounts is papering over a churn problem."
Misuse: quoting only NRR. A 110% NRR with 80% GRR and a 110% NRR with 95% GRR are completely different businesses.

**CAC payback and LTV:CAC** — CAC payback = months of gross-margin-adjusted revenue to recover the fully loaded cost of acquiring a customer (want <18 months mid-market, <12 SMB). LTV:CAC = lifetime gross profit ÷ acquisition cost (want >3x).
In use: "Payback stretched from 14 to 22 months this year — we're buying growth we can't finance."
Misuse: computing CAC on sales salaries only (exclude marketing and overhead and everyone's payback looks great), or LTV on revenue instead of gross profit.

**Rule of 40** — Growth rate % + profit margin % (usually FCF or EBITDA margin) should exceed 40 for a healthy SaaS business.
In use: "We're at 40 growth minus 21 margin = 19 — the board will ask what gets us back above 30."
Misuse: treating it as a law rather than a benchmark; a company at 80% growth and -35% margin (Rule of 45) is not automatically "healthier" than one at 25% and +10% — the first depends on capital markets staying open.

**Deferred revenue (contract liability)** — Cash collected for services not yet delivered; a liability, released to revenue as you deliver. The mirror of prepayment.
In use: "Deferred grew $900K — collections outran recognition, which is what a healthy annual-prepay motion looks like."
Misuse: reading deferred revenue as "money we owe back" (only true on termination-for-convenience clauses) or ignoring it as a growth signal — it's the most manipulation-resistant indicator of prepaid bookings momentum.

**RPO (remaining performance obligations)** — Total future contracted revenue not yet recognized, including amounts not yet billed. Broader than deferred revenue (which only covers what's been invoiced/collected).
In use: "Deferred is flat but RPO grew 30% — customers signed multi-year but we bill annually."
Misuse: conflating with backlog casually; under ASC 606 RPO is a defined, disclosable number, and for multi-year-deal businesses it's the honest forward-revenue view.

**Free cash flow (FCF) vs. EBITDA** — EBITDA approximates operating earnings before capital structure and non-cash charges; FCF = actual cash generated after capex (and, honestly computed, after capitalized software and working capital).
In use: "EBITDA-positive, FCF-negative — capitalized R&D and working capital eat the difference. Value us on FCF."
Misuse: "EBITDA is basically cash flow." It isn't, for anyone with capex, growth-driven working capital needs, or capitalized development costs — i.e., nearly everyone.

**Liquidity vs. solvency** — Liquidity = can you meet obligations as they come due (a timing question). Solvency = do assets exceed liabilities / is the business viable (a value question).
In use: "This is a liquidity problem, not a solvency problem — the revolver bridges it. Don't let it get described as the latter."
Misuse: interchangeable use. Solvent companies die of illiquidity routinely; the whole point of the 13-week forecast is preventing exactly that.

**Dry powder / debt capacity / dilution budget** — The financing the company *could* still access: undrawn facilities, additional leverage within covenant caps, and the equity dilution ownership will tolerate.
In use: "Doing this deal all-cash spends our dry powder; if the market turns, we've got no defensive raise left."
Misuse: evaluating each financing in isolation. Capital capacity is a shared budget across all future needs — offensive and defensive.

**Sandbagging / hockey stick / haircut** — Working slang. Sandbagging = deliberately low forecasts to guarantee beats. Hockey stick = a projection where everything improves conveniently after the near term. Haircut = discount applied to someone's number before relying on it.
In use: "Sales called $2.2M; I haircut new-logo 20% for the plan, and I don't fund the back-half hockey stick until Q1 actuals support it."
Misuse: not applying them — taking bottoms-up department forecasts at face value is a rookie planning error; every submitted number arrives with an agenda.
