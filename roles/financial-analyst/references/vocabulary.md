# Financial analysis working vocabulary

Terms an analyst uses precisely. Format: definition → how a practitioner says it → common misuse.

**DCF (Discounted Cash Flow)** — A valuation method projecting future free cash flows and discounting them to present value using a rate reflecting the investment's risk, used to estimate intrinsic value independent of current market pricing.
In use: "The DCF comes in 35% above the trading comps — that gap needs an explanation before we trust either number."
Misuse: treating a DCF's output as objectively "the" value of an asset rather than a value conditional on its assumptions (growth rate, discount rate, terminal value) — change the assumptions and the DCF changes, often dramatically.

**WACC (Weighted Average Cost of Capital)** — The blended required return across a company's debt and equity financing, weighted by their proportion in the capital structure, commonly used as the discount rate in a DCF.
In use: "We used a 9.2% WACC here, reflecting this segment's higher risk profile than the corporate average."
Misuse: applying a single company-wide WACC to a specific project or division with a materially different risk profile than the overall company, understating or overstating that project's actual required return.

**Unit economics** — The revenue and cost attributable to a single unit of the business (one customer, one transaction, one store), checked independently of aggregate company-level numbers to see if the underlying business model is profitable at the unit level.
In use: "Aggregate revenue is growing 40% YoY, but unit economics show we lose $12 on every new customer in year one — growth is making the problem bigger, not smaller."
Misuse: trusting aggregate growth or aggregate profitability as evidence of a healthy business model without checking whether the underlying unit is actually profitable — fast growth can scale a money-losing unit economics problem.

**Opportunity cost** — The value of the next-best alternative use of the same capital or resource, the only cost that matters for evaluating whether a specific use of that capital/resource is the right one — as distinct from sunk cost, which is irrelevant to a forward decision.
In use: "The question isn't whether this project is profitable in isolation — it's whether it's a better use of this $3M than the next-best alternative."
Misuse: evaluating a project on standalone profitability without comparing it against what the same capital could earn in its next-best use, or factoring in money already spent (sunk cost) as if it were relevant to the forward decision.

**DSO (Days Sales Outstanding)** — The average number of days it takes a company to collect payment after a sale, a key indicator of collections health and a common driver of the gap between accounting profit and actual cash flow.
In use: "DSO jumped from 42 to 61 days this quarter — that's exactly why operating cash flow is negative despite a profitable P&L."
Misuse: reading a profitable income statement as sufficient evidence of financial health without checking DSO/AR trends, which can reveal a real, growing cash collection problem the P&L doesn't show.

**Sensitivity analysis** — Systematically varying a model's key input assumptions (one at a time or in combination) to see how much the output changes, used to identify which assumptions the conclusion is most dependent on.
In use: "The sensitivity table shows payback period swings from 14 to 34 months just from a 20% change in close rate — that's the assumption worth the most diligence."
Misuse: presenting only a base-case single-point output without a sensitivity table, hiding how much the conclusion actually depends on uncertain inputs.

**Variance analysis (volume/price/mix)** — Decomposing a budget-to-actual variance into its component drivers — volume (units changed), price (per-unit price changed), mix (the composition of what was sold changed), and one-time items — rather than reporting only the total dollar variance.
In use: "The $400K unfavorable variance is 80% price (competitive discounting) and 20% mix (more low-margin SKUs sold) — those need different corrective actions."
Misuse: reporting a variance's total dollar amount without decomposing its drivers, which can lead to the wrong corrective action since volume, price, and mix problems require different responses.

**Base rate** — The average historical outcome for a class of decision or event (e.g., most M&A destroys value, most new product launches fail), used as the default expectation that a specific case's narrative has to explicitly justify deviating from.
In use: "The base rate for this type of acquisition integration is a 60% chance of missing projected synergies — what specifically makes this deal different from that pattern?"
Misuse: accepting a compelling narrative for why "this time is different" without first checking what the base rate actually is and requiring the narrative to explain the deviation.

**Materiality (financial analysis context)** — The threshold above which a line item or discrepancy is significant enough to warrant detailed modeling or investigation, used to allocate analytical effort proportional to how much a line item could swing the decision, not how easy it is to model.
In use: "This cost line is 0.3% of the total budget — not worth building a detailed sub-model for, even though we happen to have great data on it."
Misuse: spending disproportionate modeling effort on an easy-to-model but immaterial line item while under-modeling a harder-to-forecast but much more consequential one.

**Terminal value** — The estimated value of all cash flows beyond a DCF's explicit forecast period, often representing the majority of a DCF's total value — meaning small changes in its underlying assumptions (long-term growth rate, exit multiple) can swing the valuation significantly.
In use: "Terminal value is 78% of this DCF's total value — the long-term growth assumption deserves as much scrutiny as the explicit forecast years."
Misuse: focusing diligence primarily on the explicit forecast period's assumptions while treating the terminal value's assumptions as a formality, when terminal value is often the dominant driver of the total valuation.
