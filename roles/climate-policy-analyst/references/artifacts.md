# Climate Policy Artifacts — Templates With Example Content

Real work products, filled in with plausible examples. Copy the structure, replace the content. The example jurisdiction throughout is a mid-size state agency ("State Environmental Agency," SEA) considering a medium/heavy-duty truck electrification rule and a companion carbon-pricing bill.

---

## 1. Benefit-cost memo

A benefit-cost memo exists so a legislator's staffer can defend a vote in one read. Lead with the corrected number, not the process.

```
MEMO — Benefit-Cost Review: Advanced Clean Trucks Rule (Draft RIA)
To: Sen. Committee on Environment staff · From: Policy Analyst · Date: 2026-03-04

BOTTOM LINE
Draft RIA shows BCR 0.68 (fails). Corrected for omitted co-pollutant
benefits, BCR is 1.08 at the central case, ~0.99-1.01 at the upper
discount-rate bound. Recommend proceeding with a floor amendment
requiring the co-pollutant supplement before final adoption.

NUMBERS
Direct GHG benefit:      50,000 tons CO2e/yr x $190/ton (SC-CO2, 2% rate,
                          EPA 2023) = $9,500,000/yr
Co-pollutant benefit:     NOx  120 tons/yr x $9,200/ton   = $1,104,000/yr
                          PM2.5  8 tons/yr x $560,000/ton = $4,480,000/yr
                          Subtotal                        = $5,584,000/yr
Total monetized benefit:                                    $15,084,000/yr
Annualized cost (vehicle premium + charging infra):         $14,000,000/yr
Benefit-cost ratio:                                          1.08

SENSITIVITY (disclose, don't bury)
At 2.5% discount rate: SC-CO2 ~$165-170/ton -> climate benefit alone
~$8.3-8.6M -> plus unchanged $5,584,000 co-pollutant benefit -> total
~$13.88-14.18M -> BCR ~0.99-1.01. Ratio is not stable across the full
discount-rate range; say so in the record now so it isn't discovered
in litigation.

WHAT WOULD CHANGE THE ANSWER
- If co-pollutant tons are revised down >30% in the final MOVES-model
  run, BCR falls back below 1.0 at the central case too.
- If charging-infrastructure cost estimates (currently a state DOT
  planning figure, not a competitive bid) come in >15% high, same result.

RECOMMENDATION
Proceed to committee vote on the corrected analysis. Amendment: require
SEA to publish the co-pollutant supplement and discount-rate sensitivity
in the final RIA before adoption, not after.
```

What makes this work: the bottom line is the first line, every dollar figure shows its per-ton input so it can be checked, and the sensitivity section is disclosed before anyone else finds it.

---

## 2. Regulatory comment letter (attacking the analytical defect, not the goal)

```
RE: Docket No. SEA-2026-0042 — Proposed Advanced Clean Trucks Rule

We support the emissions-reduction goal of this rulemaking. We comment
specifically on a defect in the draft Regulatory Impact Analysis (RIA)
that, if uncorrected, understates the rule's benefits and creates
litigation risk under [state APA cost-benefit requirement].

DEFECT: The draft RIA (Section 4.2, Table 4-3) monetizes only direct
CO2e reductions and does not monetize the co-emitted NOx and PM2.5
reductions from the same fleet turnover, despite SEA's own RIA
Guidance Document (2019), Section 3.1, requiring monetization of
"all quantifiable co-pollutant effects" for mobile-source rules.

CORRECTED ANALYSIS: Applying EPA's mobile-source benefit-per-ton
values (urban, non-attainment area) to the fleet emission factors
already in the docket (MOVES-model run, Appendix C) yields
$5,584,000/year in additional monetized benefit, raising the
benefit-cost ratio from 0.68 to 1.08 at the central discount rate.
[Full calculation attached as Exhibit A.]

REQUESTED ACTION: Republish the RIA with co-pollutant benefits
monetized per SEA's own guidance, and include the discount-rate
sensitivity (2%, 1.5%, 2.5%) required for consistency with current
OMB Circular A-4 practice, before this rule is finalized.

[Organization] · [Contact] · [Date]
```

The letter names the specific guidance document the agency already committed to following — that's what forces a response on the record instead of a form-letter dismissal.

---

## 3. Legislative one-pager (vote-count framing, not science framing)

```
ISSUE: SB 214 — Clean Trucks Standard
STATUS: Committee vote scheduled 2026-03-13. Currently 6-5 against
        on committee (one undecided: Sen. Ibarra, freight-district).

THE ASK: Vote yes on SB 214 as amended (co-pollutant RIA supplement
attached as a floor amendment).

WHY IBARRA'S VOTE IS WINNABLE: Freight district has three of the
five census tracts with the state's highest childhood-asthma ER
visit rates. The corrected RIA's PM2.5 benefit ($4.48M/yr) is
concentrated in exactly those tracts — this is a local, not global,
selling point for a freight-district vote.

OPPOSITION'S STRONGEST ARGUMENT AND OUR RESPONSE: "The RIA fails its
own cost-benefit test (0.68)." Response: that RIA omitted co-pollutant
benefits required by the agency's own guidance; corrected figure is
1.08. We are not disputing the agency's method, we are asking them to
follow it completely.

FALLBACK IF THE VOTE FAILS: Split the bill. Advance the charging-
infrastructure funding title alone (bipartisan support, no BCR fight)
and hold the sales-mandate title for the corrected RIA next session.
```

---

## 4. Carbon-pricing instrument comparison (tax vs. cap-and-trade, filled)

Used when leadership asks "which instrument" before a bill is drafted, not after.

| Dimension | Carbon tax | Cap-and-trade |
|---|---|---|
| Price/quantity certainty | Price certain, quantity varies | Quantity certain, price varies |
| Administrative complexity | Low — piggybacks on existing fuel/energy tax collection | High — needs allowance registry, auction mechanism, offset protocols |
| Revenue use as coalition tool | Rebate/dividend or general fund, simple to explain | Free allowances to affected industries buy votes, at the cost of a windfall-profit critique |
| Offset-integrity exposure | None (no offsets in a pure tax) | High if offsets are allowed — see additionality discount heuristic |
| Historical vote outcome | Washington State I-1631 (2018) failed at ballot; no enacted major U.S. economy-wide tax to date | RGGI (2009-present) and California AB 32 (2012-present) both enacted and operating |
| When to recommend | Political ask is administrative simplicity and transparent pricing, no need for a hard quantity target | Political ask is a binding quantity target (treaty/statute-linked) or industry needs allowance transition support to accept the bill at all |

**Note on the historical row:** it is not an argument that cap-and-trade is more passable in general — it reflects that both enacted U.S. programs used free allowance allocation to build the exact industry coalition a pure tax proposal has repeatedly failed to build. That's a specific, checkable political-economy fact, not a law of nature; a jurisdiction with a different industry mix or a dividend-focused coalition (i.e., not affected-industry buy-in) can flip the calculus toward a tax.
