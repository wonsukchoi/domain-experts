# Financial Quantitative Analyst — Playbook

## Black-Scholes pricing and Greeks calculation (filled example)

| Input | Value |
|---|---|
| Spot price (S) | $100 |
| Strike (K) | $105 |
| Risk-free rate (r) | 5% |
| Time to expiry (T) | 0.25 years |
| Volatility (σ) | 25% |

| Step | Calculation | Value |
|---|---|---|
| d₁ | [ln(100/105) + (0.05+0.03125)(0.25)] ÷ (0.25×0.5) | −0.2278 |
| d₂ | d₁ − σ√T | −0.3528 |
| N(d₁) | | 0.4099 |
| N(d₂) | | 0.3621 |
| **Call price** | 100(0.4099) − 105(0.9876)(0.3621) | **$3.44** |
| **Delta** | N(d₁) | **0.4099** |
| **Gamma** | N'(d₁) ÷ (S·σ·√T) = 0.3887 ÷ 12.5 | **0.0311** |

## Gamma-adjusted vs. linear P&L estimate (filled example)

| Method | Formula | Result |
|---|---|---|
| Linear (delta-only) | Δ × ΔS | 0.4099 × 5 = **$2.05** |
| Gamma-adjusted | Δ × ΔS + ½ × Γ × ΔS² | 2.0495 + 0.5(0.0311)(25) = **$2.44** |
| **Understatement from ignoring gamma** | $2.44 − $2.05 | **$0.39 (~16%)** |

**Use:** Always calculate the gamma-adjusted estimate whenever the move size under consideration is large relative to the position's convexity — the linear-only estimate's error grows quadratically with move size.

## Backtest bias-check checklist

1. **Lookahead bias:** Does every data input used in the decision logic reflect only information genuinely available (without later revision) at that historical point in time?
2. **Survivorship bias:** Does the analysis universe include instruments/companies that failed, delisted, or were removed from an index at each historical point, not just the current membership list?
3. **Parameter-to-data ratio:** How many free parameters does the model have relative to the number of independent data points used to calibrate it?
4. **Out-of-sample validation:** Was a period held out entirely from calibration, and how does performance on that period compare to in-sample results?

**Use:** Run all four checks before trusting any backtest's headline Sharpe ratio or return figure — a strategy that fails any one of these can show an impressive in-sample result that doesn't reflect real-world performance.

## Monte Carlo convergence check (illustrative structure)

| Path count | Estimated price | Change from prior run |
|---|---|---|
| 10,000 | $3.61 | — |
| 50,000 | $3.47 | −$0.14 |
| 100,000 | $3.44 | −$0.03 |
| 500,000 | $3.44 | ~$0.00 (converged) |

**Use:** Keep increasing path count until the estimate stabilizes within an acceptable tolerance — a single fixed path count run, however large it seems, doesn't by itself confirm convergence without this kind of comparison across increasing counts.

## Pricing and risk memo — filled example

> **Option Pricing and Risk Report — 3M Call, K=$105, S=$100**
> Black-Scholes price: $3.44 | Delta: 0.4099 | Gamma: 0.0311
> P&L estimate for a $5 underlying move: **linear (delta-only) estimate $2.05 vs. gamma-adjusted estimate $2.44** — a 16% understatement if gamma is ignored.
> **Recommendation: For position sizing or scenario analysis involving moves beyond a small range, use the gamma-adjusted estimate, not delta alone.**
