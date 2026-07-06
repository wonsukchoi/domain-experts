# Financial Risk Specialist — Playbook

## VaR and expected shortfall calculation (filled example)

| Step | Calculation | Value |
|---|---|---|
| Portfolio value | | $50,000,000 |
| Asset A weight / volatility | 50% / 1.5% daily | |
| Asset B weight / volatility | 50% / 1.0% daily | |
| Normal correlation | | 0.3 |
| Portfolio variance | 0.25×0.000225 + 0.25×0.0001 + 2×0.25×0.3×0.015×0.01 | 0.0001038 |
| Portfolio volatility | √0.0001038 | 1.02% |
| **1-day VaR (95%, z=1.65)** | $50M × 1.65 × 0.0102 | **$840,300** |
| **Expected shortfall (≈1.25× VaR)** | $840,300 × 1.25 | **$1,050,375** |

## Correlation stress test (filled example, continuing above)

| Step | Calculation | Value |
|---|---|---|
| Stressed correlation | | 0.9 |
| Stressed portfolio variance | 0.25×0.000225 + 0.25×0.0001 + 2×0.25×0.9×0.015×0.01 | 0.0001488 |
| Stressed portfolio volatility | √0.0001488 | 1.22% |
| **Stressed 1-day VaR** | $50M × 1.65 × 0.0122 | **$1,006,335** |
| **Increase over normal-condition VaR** | $1,006,335 − $840,300 | **$166,035 (~20% increase)** |

**Use:** Always recompute the risk figure under a stressed correlation assumption — the increase from normal to stressed conditions is itself the key finding, showing how much diversification benefit would evaporate in a crisis.

## Risk limit comparison table (filled example)

| Scenario | VaR estimate | Limit | Status |
|---|---|---|---|
| Normal correlation (0.3) | $840,300 | $900,000 | Within limit |
| Stressed correlation (0.9) | $1,006,335 | $900,000 | **Breach by $106,335** |

**Limit derivation:** $900,000 = 0.45% × $200,000,000 capital base (board-approved daily risk appetite).

**Use:** Report both scenarios side by side against the limit — a normal-condition figure within limit can mask a real problem that only shows up once correlation stress is applied.

## Hedge basis risk quantification checklist

1. Identify the hedge instrument and the underlying exposure it's meant to offset.
2. Compare key terms: maturity/tenor, underlying reference asset, notional size.
3. Pull historical basis behavior (price divergence between hedge and exposure) over relevant periods, including stress periods if available.
4. Calculate hedge effectiveness (percentage of exposure movement actually offset) rather than assuming 100% based on gross notional match.
5. Report net exposure after the hedge, explicitly stating the residual basis risk — never describe a position as simply "hedged" without this figure.

## Reverse stress test design checklist

1. Define an unacceptable loss level (e.g., a threshold that would breach regulatory capital requirements or trigger a going-concern issue).
2. Work backward: what combination of market moves, correlation shifts, and liquidity conditions would produce that loss level?
3. Check whether any component of that combination has historical precedent, or represents a genuinely novel (but plausible) scenario.
4. Compare the reverse stress test's implied scenario against current historical stress scenarios already in use — if it's not already covered, add it to the standing stress test suite.

## Risk report — filled example

> **Portfolio Risk Report — Equity Book, [Date]**
> Normal-condition 1-day VaR (95%): $840,300 (within $900,000 limit). Expected shortfall: $1,050,375.
> Stress test (correlation moved from 0.3 to 0.9, crisis-convergence scenario): stressed 1-day VaR: $1,006,335 — **breaches the $900,000 limit by $106,335.**
> **Finding: The portfolio's normal-condition risk profile appears within limit, but stressed correlation assumptions reveal a real limit breach. Recommend reducing position size or adding a hedge to bring stressed VaR within the approved limit, and escalate to the risk committee.**
