### Delta
The sensitivity of an option's price to a small change in the underlying asset's price — the first-order (linear) Greek.
**In use:** "Delta of 0.41 means the option's price moves roughly $0.41 for a $1 move in the underlying, for a small move."
**Common misuse:** Using delta alone to estimate P&L for a large move in the underlying, ignoring the second-order gamma effect that becomes significant as move size grows.

### Gamma
The rate of change of an option's delta with respect to the underlying price — the second-order Greek, capturing convexity.
**In use:** "Gamma of 0.031 means delta itself shifts meaningfully once the underlying moves several dollars, which is why the linear delta estimate breaks down for a $5 move."
**Common misuse:** Ignoring gamma when estimating P&L for anything beyond a small move, leading to a systematically understated (for long-convexity positions) price-change estimate.

### Vega
The sensitivity of an option's price to a change in implied volatility.
**In use:** "Vega tells us how much the option's value would change if implied volatility shifted by one percentage point."
**Common misuse:** Confusing vega's sensitivity to implied volatility with sensitivity to historical/realized volatility, which is a different, backward-looking quantity.

### Theta
The sensitivity of an option's price to the passage of time (time decay), typically expressed as value lost per day holding other factors constant.
**In use:** "Theta shows this option loses about $0.05 in value per day, all else equal, as expiry approaches."
**Common misuse:** Treating theta as constant over the option's life, when time decay typically accelerates as expiry approaches, especially for at-the-money options.

### Implied volatility
The volatility level, when input into an option pricing model, that produces the option's current observed market price — the market's forward-looking volatility estimate.
**In use:** "Implied volatility is elevated ahead of earnings, reflecting the market's expectation of a large post-announcement move."
**Common misuse:** Treating a gap between implied and historical volatility as a pricing error to reconcile, rather than investigating for a known upcoming event that would explain it.

### Historical (realized) volatility
A backward-looking measure of how much an asset's price has actually moved over a specified past period.
**In use:** "Historical volatility over the past 30 days has been much lower than the current implied volatility, which is pricing in the upcoming FDA decision."
**Common misuse:** Using historical volatility as an input when pricing an option for a period that includes a known event materially different from the recent past — implied volatility (or an event-adjusted estimate) is usually more appropriate for that scenario.

### Lookahead bias
A backtesting error where the strategy's logic uses information that would not have actually been available at the historical point in time being simulated.
**In use:** "Using the full-year earnings figure to make a trading decision in March is lookahead bias — that data wasn't available yet."
**Common misuse:** Failing to check whether every data input used in a backtest's decision logic was genuinely available (in real time, without revision) at each simulated decision point.

### Survivorship bias
A backtesting error where the analysis universe excludes instruments or companies that failed, delisted, or were removed from an index, inflating the apparent historical performance.
**In use:** "This backtest only used companies currently in the index — that excludes every company that went bankrupt or was delisted, which is survivorship bias."
**Common misuse:** Constructing a backtest universe from a current index membership list rather than the actual historical membership at each point in time, silently excluding failures.

### Overfitting
A model calibration error where a model with too many free parameters relative to its data fits historical noise rather than a genuine, persistent pattern, producing impressive in-sample results that don't hold out-of-sample.
**In use:** "With this many parameters relative to our data points, we need strong out-of-sample validation before trusting this backtest."
**Common misuse:** Judging a model's quality by in-sample fit alone, without checking the parameter-to-data ratio or requiring genuine out-of-sample performance.

### Out-of-sample validation
Testing a model or strategy on data that was not used in any part of its parameter fitting or calibration process, to check whether its performance holds outside the data it was built on.
**In use:** "Out-of-sample performance dropped sharply compared to in-sample — that's a strong overfitting signal."
**Common misuse:** Treating a validation period as "out-of-sample" when it was actually used, even indirectly, in tuning the model's parameters.

### Monte Carlo simulation (convergence)
A numerical method estimating a value (e.g., an option price) by simulating many random paths and averaging the results — convergence refers to the estimate stabilizing as the number of simulated paths increases.
**In use:** "We re-ran the simulation at 10x the path count and the price barely moved — that confirms convergence."
**Common misuse:** Accepting a Monte Carlo result from a single, fixed path count without checking whether increasing the path count would materially change the estimate.
