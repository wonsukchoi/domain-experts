# Artifacts

Filled templates for the three documents a pension scheme manager produces most: the funded-status sensitivity analysis, the glide-path policy, and the trustee de-risking memo.

## Funded-status sensitivity analysis (filled example)

```markdown
# Funded Status Sensitivity — Q3 Review

Current position:
  Assets: $850M
  Liabilities (PV): $900M
  Funded status: 94.4%
  Liability duration: 14.0 years
  Bond sleeve duration: 8.0 years (60% of assets, $510M)
  Equity/growth allocation: 40% ($340M)

Sensitivity to discount rate (± 100bp):

Scenario         | Liability impact | Bond sleeve impact | Net funded-status move
-----------------|-------------------|----------------------|------------------------
Rates -100bp      | +$126M (+14%)     | +$40.8M (+8%)         | -$85.2M (worsens)
Rates +100bp      | -$126M (-14%)     | -$40.8M (-8%)          | +$85.2M (improves)

Sensitivity to equity return (± 20%, rates held constant):

Scenario         | Equity impact     | Net funded-status move
-----------------|-------------------|------------------------
Equities -20%      | -$68M              | -$68M (worsens)
Equities +20%       | +$68M              | +$68M (improves)

Interpretation: the plan's largest single funded-status risk is the 6-year
duration mismatch between liabilities (14yr) and the bond sleeve (8yr) —
not equity market performance. A rate-down scenario alone produces a
larger funded-status hit than a 20% equity drawdown.
```

## Glide path policy (filled example)

```markdown
# Investment Policy — LDI Glide Path

Funded status tier    | Growth allocation | LDI/bond allocation | Bond duration target
-----------------------|---------------------|------------------------|------------------------
Below 80%                | 55%                  | 45%                     | Duration-neutral (match available budget)
80% - 90%                | 45%                  | 55%                     | 80% of liability duration
90% - 100%                | 35%                  | 65%                     | 95% of liability duration
100% - 105%                | 25%                  | 75%                     | Full liability duration match
Above 105%                | 15%                  | 85%                     | Full match + consider annuity buyout for
                          |                      |                          | tranches of retiree liabilities

Rules:
- Allocation shifts trigger automatically when funded status crosses a
  tier boundary on two consecutive quarterly measurements (avoids
  whipsawing on a single volatile reading).
- Sponsor credit rating below investment grade triggers an immediate
  review of the current tier's growth allocation, independent of the
  funded-status trigger — sponsor risk can override the mechanical glide
  path in the de-risking direction, never in the risk-adding direction.
- Any deviation from the tier's stated allocation requires trustee
  committee sign-off with documented rationale.
```

## Trustee de-risking memo (filled example, condensed)

```markdown
# Memo: Recommended Duration Extension — Q3 2026

To: Trustee Committee
Re: Response to proposed equity increase (40% -> 55%)

Summary: We recommend REJECTING the proposed equity increase and instead
extending bond sleeve duration from 8 to 13 years, reducing equity
allocation from 40% to 35%.

Why now: Sponsor credit rating downgraded BBB -> BBB- last month. This
reduces the plan's effective backstop — sponsor capacity to fund a
shortfall via additional contributions is weaker than at our last review.
This is the wrong moment to add funded-status volatility via equity risk;
it's the right moment to reduce the volatility we're least equipped to
absorb (rate risk via the duration mismatch).

Quantified tradeoff:
  Current 100bp rate-down exposure: -$85.2M funded status impact
  Post-extension 100bp rate-down exposure: -$9.8M funded status impact
  Cost: forgone equity risk premium, estimated 1.2%/year expected return
  reduction on the reallocated $42.5M (40%->35% shift)

Recommendation stands regardless of near-term market direction — this is
a risk-capacity decision tied to sponsor credit, not a market call.
```
