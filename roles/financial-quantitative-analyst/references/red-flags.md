### A P&L or risk estimate uses delta alone for a potentially large move in the underlying
- **Usually means:** The linear delta-only estimate likely understates (for a long-convexity position) or misstates the true price change, since gamma effects grow with move size.
- **First question:** What move size is being considered, and has a gamma-adjusted (or full-revaluation) estimate been calculated alongside the delta-only figure?
- **Data to pull:** Position's delta and gamma, the specific move size under consideration.

### A backtest reports a strong Sharpe ratio or return figure with no mention of lookahead or survivorship bias controls
- **Usually means:** The reported performance may be inflated by using information not actually available at each historical decision point, or by excluding instruments/companies that failed or delisted.
- **First question:** Does the backtest logic use only data that would have actually been available at each decision point, and does the universe include delisted/failed instruments?
- **Data to pull:** Backtest methodology documentation, data universe construction rules.

### A backtest has no genuine out-of-sample validation period
- **Usually means:** The strategy's parameters may have been fit (explicitly or implicitly) to the entire available dataset, making the in-sample performance a poor predictor of future results.
- **First question:** Was any period held out entirely from parameter fitting, and how does performance on that period compare to the in-sample result?
- **Data to pull:** In-sample vs. out-of-sample performance metrics, parameter-fitting methodology.

### A trading model has a large number of free parameters relative to the size of its calibration dataset
- **Usually means:** A classic overfitting risk — the model may be fitting historical noise rather than a genuine, persistent pattern.
- **First question:** What is the ratio of free parameters to independent data points used in calibration, and has out-of-sample performance been checked?
- **Data to pull:** Model parameter count, dataset size, out-of-sample validation results.

### Implied volatility and historical volatility diverge sharply for a specific option/underlying
- **Usually means:** Often reflects a known upcoming event (earnings, regulatory decision, macro announcement) the market is pricing in, rather than a modeling error.
- **First question:** Is there a scheduled event before this option's expiry that would explain the market pricing in elevated (or depressed) forward-looking volatility?
- **Data to pull:** Upcoming event calendar for the underlying, implied volatility term structure around the event date.

### A Monte Carlo simulation result is reported to several decimal places with no convergence check shown
- **Usually means:** The apparent precision may not reflect actual numerical stability — an underpowered simulation can look precise while still being far from the converged value.
- **First question:** Has the simulation been re-run with a higher path count to confirm the estimate has stabilized within an acceptable tolerance?
- **Data to pull:** Path count used, price estimate at increasing path counts (convergence check).

### A derivative's Greeks are reported without stating the move-size range over which they remain a valid approximation
- **Usually means:** A reader might apply the Greek linearly across move sizes well beyond where the approximation holds, understating real exposure.
- **First question:** Over what move-size range is this Greek being presented as a valid approximation, and is a gamma-adjusted or full-revaluation figure available for larger moves?
- **Data to pull:** Gamma (or higher-order Greeks), the range of moves relevant to the current risk question.

### A strategy's backtest performance looks impressive on a visual equity-curve inspection alone
- **Usually means:** Visual inspection doesn't catch overfitting, lookahead bias, or survivorship bias — a smooth-looking curve can still be built on a flawed methodology.
- **First question:** Beyond the equity curve, has the strategy been checked against the specific bias controls (lookahead, survivorship) and out-of-sample validation?
- **Data to pull:** Full backtest methodology and validation results, not just the summary performance chart.
