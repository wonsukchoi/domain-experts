### A risk report states VaR without expected shortfall
- **Usually means:** The report tells you how often losses exceed the threshold but nothing about how severe the loss gets beyond it — a real gap for tail-risk decision-making.
- **First question:** What is the expected shortfall (conditional VaR) at the same confidence level, and has it been calculated alongside the VaR figure?
- **Data to pull:** Portfolio return distribution or model output needed to calculate expected shortfall.

### A portfolio risk estimate uses correlation assumptions that haven't been stress-tested
- **Usually means:** The estimate may significantly understate risk in a crisis, since correlations between exposures commonly move toward 1 under stress, eroding assumed diversification benefit.
- **First question:** What would the risk estimate look like if correlations between the portfolio's components were stressed toward historical crisis-period levels?
- **Data to pull:** Current correlation assumptions used in the model, historical correlation behavior during past stress periods.

### A risk limit was set based on an industry-typical figure with no derivation from this organization's capital or risk appetite
- **Usually means:** The limit may not actually reflect what this organization can absorb, making a breach either meaningless (too loose) or unnecessarily restrictive (too tight).
- **First question:** What capital base and stated risk-appetite percentage was used to derive this specific limit?
- **Data to pull:** Capital base figure, board-approved risk appetite statement.

### A position is described as "fully hedged" with no quantified residual basis risk
- **Usually means:** Some exposure almost certainly remains — differences in timing, instrument, or underlying between the hedge and the original exposure rarely net to exactly zero.
- **First question:** What specific instrument is being used to hedge, and how does it differ from the underlying exposure (maturity, underlying asset, notional match)?
- **Data to pull:** Hedge instrument terms, underlying exposure terms, historical basis behavior between the two.

### Stress testing relies only on historical scenarios (replaying past crises)
- **Usually means:** Novel stress paths that haven't occurred historically could be missed entirely, since historical replay only tests scenarios that have already happened.
- **First question:** Has a reverse stress test (working backward from an unacceptable loss level) been run to find conditions not captured by historical scenarios?
- **Data to pull:** List of stress scenarios currently used, unacceptable loss threshold for reverse stress test design.

### A normal-condition VaR is within limit but hasn't been checked under a stressed-correlation scenario
- **Usually means:** The apparent comfort margin may not hold under actual crisis conditions, and the true risk profile is understated.
- **First question:** What does the VaR calculation show under a stressed correlation assumption, and does it still clear the limit?
- **Data to pull:** Stressed correlation assumption, recalculated VaR under that assumption.

### A hedge's net risk reduction is reported using gross notional hedged rather than a basis-risk-adjusted figure
- **Usually means:** The reported risk reduction may overstate the hedge's actual effectiveness.
- **First question:** What is the net exposure after accounting for basis risk, not just the gross notional amount hedged?
- **Data to pull:** Gross notional hedged, historical basis risk data for this hedge/exposure pairing.

### A limit breach under a stress scenario is not escalated because the normal-condition figure is within limit
- **Usually means:** The stressed finding — often the more informative one — is being effectively ignored in favor of the more comfortable normal-condition number.
- **First question:** Has the stressed-scenario breach been reported to the risk committee alongside the normal-condition figure, or only the normal-condition figure?
- **Data to pull:** Risk committee reporting log, both normal and stressed VaR figures for the period in question.
