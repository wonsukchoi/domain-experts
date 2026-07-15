# Red flags — what an analyst notices instantly

Smell tests with thresholds. Any single one can be innocent; two or three together are a pattern.

### GAAP net income positive while operating cash flow is negative for 2+ consecutive quarters
- **Usually means:** revenue recognition timing, receivables growth outpacing revenue, or capitalized costs (commissions, implementation) are masking a real cash problem the P&L doesn't show.
- **First question:** "What's driving the gap — is it AR growth, deferred cost capitalization, or something else specific in the cash flow statement?"
- **Data to pull:** cash flow statement (operating section), AR aging and DSO trend, capitalized cost schedule.

### A single-point forecast presented to two or more decimal places with no stated range or sensitivity
- **Usually means:** the output's precision is fake relative to the uncertainty in its input assumptions — false confidence dressed up as rigor.
- **First question:** "What are the 2-3 assumptions this number is most sensitive to, and what's the range if each is off by 20%?"
- **Data to pull:** the model's key driver assumptions, a quick sensitivity table varying each by a plausible range.

### A DCF or intrinsic valuation diverging significantly (commonly 30%+) from comparable trading multiples or precedent transactions with no stated reason
- **Usually means:** an assumption in the DCF (growth rate, discount rate, terminal value) is likely miscalibrated, or there's a genuine, explainable reason the comp set doesn't apply — but the gap needs an explicit explanation either way.
- **First question:** "What specifically explains the gap between the DCF and the comps — is it a real difference in the business, or an assumption problem?"
- **Data to pull:** the DCF's key assumptions (discount rate, terminal growth), the comp set and multiples used, any qualitative differences that might justify a premium/discount.

### A payback/ROI projection built on assumptions (CAC, close rate, deal size) that haven't been checked against the company's own existing comparable data
- **Usually means:** the pitch's numbers may be more optimistic than what the company's actual historical performance in a comparable channel/segment supports.
- **First question:** "What does our existing comparable data (current channel CAC, historical close rates) say versus the numbers used in this projection?"
- **Data to pull:** actual historical CAC/close rate/deal size for the most comparable existing channel or segment, the projection's stated assumptions.

### A "downside case" built by applying an arbitrary uniform haircut (e.g., "-20% across the board") rather than derived from actual worst-historical-case data
- **Usually means:** the downside scenario isn't grounded in real variability and may understate genuine tail risk.
- **First question:** "What's the worst actual historical performance seen in a comparable situation, and does the stated downside case reflect that or just an arbitrary percentage?"
- **Data to pull:** historical performance range for the comparable metric/channel, the stated downside case's derivation.

### A budget variance reported as a dollar amount with no breakdown into volume, price, mix, or one-time components
- **Usually means:** the variance is flagged but not actually explained — the same total variance can require completely different corrective action depending on its underlying driver.
- **First question:** "Is this variance driven by volume, price, mix, or a one-time item, and does the corrective action differ by cause?"
- **Data to pull:** variance decomposition (volume/price/mix/one-time), comparable prior-period breakdown.

### A margin or ratio change discussed without checking whether the numerator or the denominator moved
- **Usually means:** the interpretation of the ratio's change may be wrong if the actual driver (numerator vs. denominator) isn't identified first.
- **First question:** "Did this ratio move because the numerator changed, the denominator changed, or both — and in which direction each?"
- **Data to pull:** the numerator and denominator values for the periods being compared, not just the resulting ratio.

### A capital allocation decision justified partly by reference to money already spent
- **Usually means:** sunk cost is influencing a decision that should be evaluated purely on forward-looking incremental cost and benefit.
- **First question:** "Setting aside what's already been spent, does the remaining incremental investment still clear the bar against the next-best alternative use of that capital?"
- **Data to pull:** remaining required investment (excluding sunk cost), projected incremental return, next-best alternative use of the same capital.

### A model's critical assumption embedded several tabs deep in a cell reference with no summary stating it explicitly
- **Usually means:** the judgment call that actually drives the conclusion is invisible to anyone reviewing the model's output, risking it being overlooked or silently changed later.
- **First question:** "What are this model's 2-3 most consequential assumptions, and are they stated explicitly on a summary tab, not just buried in a formula?"
- **Data to pull:** the model's assumption/driver summary (or lack of one), the specific cell references the key outputs actually depend on.
