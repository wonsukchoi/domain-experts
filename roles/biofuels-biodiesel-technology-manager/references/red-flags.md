# Red flags & diagnostics

Signals an experienced biofuels technology manager notices instantly. Load this when triaging a scale-up or commercialization decision — not for general reasoning (that's `SKILL.md`).

### A scale-up proposal jumps more than one ~10x throughput tier at once
- **Usually means:** schedule or funding pressure is overriding the normal gating discipline; heat transfer, mixing, or residence-time effects that don't scale linearly haven't been tested
- **First question:** "What specifically was validated at the intermediate scale we're skipping, and why do we believe it's not needed?"
- **Data to pull:** the current tier's mass/energy balance closure data and run duration vs. the next tier's throughput target

### Mass balance closure outside 95-105% at a pilot run being used to justify the next capital commitment
- **Usually means:** an unidentified loss, side reaction, or measurement error exists that hasn't been characterized
- **First question:** "Where specifically is the unaccounted mass — which stream, and has it been sampled directly?"
- **Data to pull:** the full balance tracker for the run in question, broken out by input/output stream

### A technology ranking or investment decision uses yield or capital cost alone, with no mention of credit value
- **Usually means:** the economic comparison is missing the CI-score-driven credit revenue, which for renewable fuel pathways is frequently comparable to or larger than the fuel-sale margin itself
- **First question:** "What's this process's CI score, and what's the credit-adjusted revenue per unit feedstock compared to the alternative?"
- **Data to pull:** current techno-economic analysis (TEA) model; check whether it has a credit-value line item at all

### Regulatory pathway approval hasn't been initiated by the time a technology reaches pilot scale
- **Usually means:** pathway approval is being treated as a later administrative step rather than a parallel critical-path item, and its multi-year timeline hasn't been priced into the commercialization schedule
- **First question:** "What's the current status of the pathway petition, and when was it actually filed?"
- **Data to pull:** regulatory pathway tracking log with filing and expected decision dates

### A process is being locked to a single feedstock's exact composition without a stated rationale
- **Usually means:** the process was optimized for near-term yield/capital efficiency without pricing the feedstock-supply-concentration risk over the plant's actual operating life
- **First question:** "What happens to yield and economics if this specific feedstock's price rises 30% or supply drops by half?"
- **Data to pull:** feedstock supply agreement terms and historical price/availability volatility for the specific feedstock

### A novel process element is disclosed publicly (conference paper, permit filing, marketing material) before an IP filing decision is made
- **Usually means:** the patent option may be foreclosed by public disclosure, and the fallback (trade secret) only works if the element is genuinely unobservable post-deployment
- **First question:** "Is this specific innovation observable from the product stream or from equipment inspection once we're operating — and if so, has a patent application been filed?"
- **Data to pull:** IP disclosure review log and the specific disclosure's date relative to any filing

### A demonstration-scale or commercial-scale budget doesn't include a specific contingency line tied to unresolved scale-up risk
- **Usually means:** the budget was built assuming linear scale-up from smaller-tier data, without pricing the real probability of a scale-dependent effect (mixing, heat transfer) requiring redesign
- **First question:** "What's the contingency percentage, and is it based on this specific process's scale-up risk or a generic project-management default?"
- **Data to pull:** the capital budget's contingency line and its stated basis

### Yield or performance data is reported from a single run rather than a stated duration of continuous, stable operation
- **Usually means:** a single good result is being treated as proof of process stability, when process stability over time (not peak performance) is what commercial operation actually requires
- **First question:** "How many consecutive days of stable operation does this result represent, and what was the variability over that period?"
- **Data to pull:** the full run log, not just the summary result, including any excursions or manual interventions during the run
