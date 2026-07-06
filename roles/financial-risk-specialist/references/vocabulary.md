### Value at Risk (VaR)
A statistical estimate of the maximum loss a portfolio is expected to experience over a given time period, at a specified confidence level — e.g., a 95% one-day VaR of $840,000 means a 5% chance of losing more than that in a day.
**In use:** "1-day VaR at 95% confidence is $840,300 under normal market conditions."
**Common misuse:** Treating VaR as the maximum possible loss, when it's actually a probability threshold — real losses can and do exceed it in the tail scenarios VaR itself doesn't quantify.

### Expected shortfall (conditional VaR)
The average loss expected in the scenarios where losses exceed the VaR threshold — a measure of tail severity that VaR alone doesn't provide.
**In use:** "Expected shortfall of $1,050,375 tells us how bad the average loss gets in that worst 5% of days, not just the threshold itself."
**Common misuse:** Reporting VaR alone and treating it as a complete risk picture, without also reporting expected shortfall for tail severity.

### Correlation breakdown
The phenomenon where correlations between asset classes or exposures, typically low or moderate in normal markets, move toward 1 during a crisis, eroding the diversification benefit a risk model assumed.
**In use:** "Correlation moved from 0.3 to 0.9 in the stress scenario, which is what drove the VaR increase."
**Common misuse:** Building a risk estimate on normal-market correlation assumptions without stress-testing how those correlations would behave in a crisis.

### Risk limit
A maximum acceptable loss threshold (often expressed as a VaR figure) set against an organization's actual capital base and stated risk appetite.
**In use:** "The daily VaR limit is $900,000, derived from 0.45% of our $200M capital base."
**Common misuse:** Adopting an industry-typical limit figure without deriving it from the specific organization's own capital and risk appetite.

### Basis risk
The residual risk that remains after a hedge is put in place, arising from differences between the hedge instrument and the underlying exposure it's meant to offset.
**In use:** "Even with the hedge in place, basis risk from the maturity mismatch means some exposure remains."
**Common misuse:** Describing a position as fully "hedged" without quantifying the basis risk that remains, implying zero residual exposure when that's rarely accurate.

### Reverse stress test
A stress-testing method that works backward from a specified unacceptable loss level to identify what combination of market conditions would produce it, rather than testing a pre-selected historical scenario forward.
**In use:** "Reverse stress testing found a plausible combination of a rate shock and liquidity squeeze that would breach our capital threshold — something our historical scenarios never surfaced."
**Common misuse:** Relying solely on historical scenario replay for stress testing, missing novel stress paths a reverse stress test is specifically designed to find.

### Parametric VaR (variance-covariance method)
A VaR calculation method assuming returns follow a known distribution (typically normal), using volatility and correlation estimates to compute the risk figure analytically.
**In use:** "Parametric VaR assumes normal returns — for a portfolio with fat tails, historical simulation might give a more realistic figure."
**Common misuse:** Using parametric VaR for portfolios with known non-normal return distributions (e.g., options-heavy portfolios) without checking whether the normality assumption materially understates risk.

### Historical simulation VaR
A VaR calculation method that applies actual historical returns to the current portfolio to generate a distribution of potential outcomes, without assuming a specific statistical distribution.
**In use:** "Historical simulation VaR captured the fat-tail risk this options position carries better than the parametric method did."
**Common misuse:** Relying exclusively on the historical dataset's observed range, which by definition can't capture a loss more severe than anything that's happened before.

### Hedge effectiveness
A measure of how much a hedge actually offsets changes in the value of the exposure it's meant to protect, as opposed to the hedge's gross notional size.
**In use:** "Hedge effectiveness testing shows this hedge offsets about 85% of the exposure's price movement — the remaining 15% is basis risk."
**Common misuse:** Assuming hedge effectiveness is 100% simply because a hedge exists, rather than testing and quantifying the actual offset percentage.

### Risk appetite
The level of risk (expressed as a specific, quantified threshold — e.g., a percentage of capital) an organization's board or leadership has explicitly approved as acceptable.
**In use:** "The 0.45%-of-capital daily VaR limit reflects the board's stated risk appetite, not just an industry benchmark."
**Common misuse:** Treating "risk appetite" as an informal, unquantified attitude rather than a specific, board-approved figure that risk limits should be explicitly derived from.
