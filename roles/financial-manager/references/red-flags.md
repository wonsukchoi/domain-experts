# Red flags — what a CFO notices instantly

Smell tests with thresholds. Format per flag: the signal → what it usually means → first question to ask → data to pull. Any one of these can be innocent; two or three together is a pattern.

## Revenue quality

**DSO creeping up >15% QoQ (e.g., 48 → 56 days) with no billing-terms change.**
Usually means: collections discipline slipping, disputed invoices piling up, or — worse — deals booked with side letters / extended terms to hit the quarter.
First question: "Show me the five largest invoices past 60 days and why each is unpaid."
Pull: AR aging by customer, invoice dispute log, any non-standard payment terms granted in the last two quarters (check the CRM against the order forms — sales sometimes grants terms finance never sees).

**Deferred revenue flat or shrinking while bookings "grow."**
Usually means: bookings are being inflated (multi-year deals counted at TCV, pilots counted as closed-won), billing frequency quietly shifted from annual to monthly, or churn is offsetting new business. Deferred revenue is the balance sheet's polygraph for a prepaid-SaaS bookings story — cash-basis customers prepay, so real bookings growth shows up there.
First question: "Reconcile the bookings number to billings to the change in deferred revenue for the quarter."
Pull: bookings-to-billings-to-deferred waterfall, mix of annual-prepay vs. monthly billing on new deals, churn/contraction detail.

**Revenue growing but billings growing slower for 2+ quarters.**
Usually means: you're recognizing yesterday's sales; the forward indicator has already turned. Revenue is a lagging indicator in a subscription business — billings and net-new ARR lead by 2–4 quarters.
First question: "What's the net-new ARR trend by month, not quarter?" (Quarterly buckets hide a mid-quarter stall.)
Pull: monthly net-new ARR, pipeline coverage ratio for next quarter (want ≥3x), win rates by cohort.

**One customer crossing 20% of revenue or 25% of AR.**
Usually means: nobody engineered it — it accreted. It's now a solvency risk (their payment timing is your payroll) and a renewal-leverage problem.
First question: "When does their contract renew, and what's our exposure if they go 90 days slow-pay?"
Pull: contract terms, their payment history trend, whether the debt facility has a concentration covenant this trips.

## Margin and cost

**Gross margin down 200bps+ over two quarters with no pricing or mix change announced.**
Usually means: hosting/infra costs scaling faster than revenue (bad unit economics surfacing), support headcount creeping into COGS, or professional-services hours being given away inside "subscription" deals.
First question: "Bridge the margin decline: how much is infra, how much is people, how much is mix?"
Pull: COGS by component vs. revenue, AWS/GCP cost per customer trend, services hours delivered vs. sold.

**Opex growing at the same rate as revenue for 4+ quarters at scale.**
Usually means: no operating leverage — the model needs a fixed-cost base that revenue outgrows. If S&M, R&D, and G&A all scale linearly with revenue, you have a services business with SaaS multiples ambitions.
First question: "Which opex lines should be sub-linear from here, and what's the plan that makes them sub-linear?"
Pull: opex by function as % of revenue, trailing 8 quarters; revenue per employee trend (should be rising).

**Magic number below 0.5 for two consecutive quarters** (net-new ARR ÷ prior-quarter S&M spend).
Usually means: sales efficiency has broken — market saturation in the current segment, quota over-assignment, or a competitive shift. Above 0.75 you can keep investing; below 0.5, more S&M spend is burning cash to stand still.
First question: "Is this a top-of-funnel problem or a win-rate problem?" (The fixes are opposite.)
Pull: pipeline creation by source, stage-conversion rates vs. prior year, ramped-rep attainment distribution (median, not mean — one whale hides nine misses).

## Cash and balance sheet

**AP days stretching >10 days beyond stated terms without a negotiated change.**
Usually means: someone is quietly managing cash by sitting on bills — which is either an unflagged liquidity problem or an AP process breakdown. Either way, the CFO found out from the balance sheet instead of from the team, which is the real problem.
First question: "Are we paying slow on purpose? Who decided, and which vendors are affected?"
Pull: AP aging, vendor complaints/credit-hold notices, the 13-week forecast's disbursement assumptions vs. actuals.

**Cash burn beating plan while the P&L misses plan.**
Usually means: the "good" cash number is timing, not performance — collections pulled forward, payables stretched, annual prepays masking a bookings miss. It reverses, with interest, next quarter.
First question: "Bridge the cash beat: how much is P&L vs. working capital timing?"
Pull: indirect cash flow statement, change in AR/AP/deferred vs. plan.

**Covenant headroom below 20% on any covenant, or projected to breach within 4 quarters.**
Usually means: you are 1–2 soft quarters from your lender controlling the timeline. Waivers cost fees, rate bumps, and sometimes warrants — and cost triple when requested after the breach instead of before.
First question: "What's the covenant projection under the bear case, and when do we call the lender?" (Answer: at least two quarters before projected breach.)
Pull: covenant compliance model projected 4 quarters forward under bear-case assumptions, facility amendment/waiver provisions.

## Process and people (the meta-signals)

**The monthly close taking longer, or the numbers changing after being "final."**
Usually means: the accounting team is under-resourced or the systems broke at the current scale — and every number the company runs on is less trustworthy than it looks. A close that slips from day 8 to day 15 is a leading indicator of a restatement-class error.
First question: "What's on the close checklist that isn't getting reconciled, and since when?"
Pull: close calendar actuals for 6 months, list of accounts not reconciled monthly, post-close adjusting entries trend.

**Forecast accuracy degrading — sales forecast missing by >10% in either direction for 2+ quarters.**
Usually means: (misses) pipeline hygiene is fiction; (beats) sandbagging, which corrupts capacity planning just as badly. Consistent large beats and consistent misses are the same disease: the forecast process doesn't reflect reality.
First question: "Show me forecast-vs-actual by rep for the last 4 quarters — who's calibrated and who isn't?"
Pull: forecast snapshots (week 1 of quarter vs. actual), slipped-deal analysis, stage-aging in CRM.

**A department consistently under-spending its budget by >15%.**
Usually means: not frugality — either the plan they committed to isn't being executed (the hiring behind the revenue target isn't happening), or the budget was padded. Both invalidate the plan the board approved.
First question: "Is the under-spend a timing delay or a decision — and if hiring slipped, does the revenue target slip with it?"
Pull: budget vs. actual by line, headcount plan vs. actual starts, the revenue model's dependency on the delayed spend.

**Quality-of-earnings tells during diligence prep (or when reviewing an acquisition target):** EBITDA "adjustments" exceeding 20% of reported EBITDA, revenue spikes in quarter-end months, related-party transactions, or a change in revenue recognition policy in the last two years.
Usually means: the earnings are engineered for the transaction.
First question: "Walk me through each addback — which would a buyer's QoE firm disallow?"
Pull: monthly (not quarterly) revenue by customer for 24 months, addback support schedules, rev-rec policy memos, related-party list.
