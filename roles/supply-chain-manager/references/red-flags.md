# Red flags — what a supply chain manager notices instantly

Smell tests with thresholds. Any single one can be innocent; two or three together are a pattern.

### A critical input single-sourced from one supplier/region with no documented concentration risk assessment
- **Usually means:** the exposure is invisible until a disruption forces discovery, at which point diversification is far more expensive and slower to arrange than it would have been proactively.
- **First question:** "What's the estimated disruption cost and probability for this specific input, and has diversification been priced against it?"
- **Data to pull:** current sourcing concentration by input, any existing risk mapping/assessment for critical inputs.

### A years-long track record with a single supplier cited as evidence the concentration risk doesn't need addressing
- **Usually means:** a clean history is evidence the risk hasn't materialized yet, not evidence it isn't real — the underlying exposure exists independent of whether it has caused a problem so far.
- **First question:** "Independent of this supplier's track record, what would a 90-day disruption from them actually cost us?"
- **Data to pull:** disruption cost estimate for this specific input, independent of historical supplier performance.

### A demand forecast at one stage of the chain built by reacting to the immediately downstream stage's orders rather than real end-customer demand signal
- **Usually means:** bullwhip effect amplification — each stage reacting to the stage below rather than shared real-demand data compounds variability upstream, a structural problem, not a forecasting skill issue at any single link.
- **First question:** "Is this forecast built from real end-demand signal, or from the immediately downstream stage's order pattern?"
- **Data to pull:** the forecasting inputs used at each stage, comparison between end-customer demand variability and the amplified variability seen further upstream.

### A supply chain optimized uniformly toward lean/just-in-time with no differentiation by input criticality
- **Usually means:** resilience investment may be under-allocated for genuinely critical, hard-to-substitute inputs while being wasted on low-stakes commodity ones, since a uniform approach doesn't match actual risk profile.
- **First question:** "Does resilience investment (buffer stock, multi-sourcing) differ by input criticality, or is the same lean approach applied everywhere?"
- **Data to pull:** input criticality/substitutability classification, current buffer stock and sourcing strategy by category.

### A functional decision (purchasing unit cost, production batch size, distribution routing) evaluated only on its own local metric
- **Usually means:** local optimization may be degrading total system performance even though it looks efficient on the function's own measure.
- **First question:** "Does this decision improve total chain cost and responsiveness, or just this function's own local metric?"
- **Data to pull:** the decision's effect on total system cost/inventory/responsiveness, not just the local function's reported efficiency.

### A disruption response launched immediately without first establishing the disruption's actual scope and duration
- **Usually means:** a fast but poorly calibrated response (over- or under-reacting relative to the real severity) can cause more damage than a brief, deliberate assessment followed by a proportionate response.
- **First question:** "Do we actually know the scope and expected duration of this disruption, or are we reacting before that's established?"
- **Data to pull:** current visibility/status data on the disruption, timeline of assessment versus response initiation.

### Supply chain visibility that relies on periodic reports rather than near-real-time status across supplier, production, and logistics stages
- **Usually means:** a disruption's true scope may be understood too late for an effective, proportionate response, with damage compounding during the detection lag.
- **First question:** "How quickly would we actually detect and understand a disruption at this stage of the chain, given our current visibility tooling?"
- **Data to pull:** current visibility/monitoring tooling and its actual latency, historical detection time for past disruptions.

### An S&OP (sales and operations planning) process that exists on paper but doesn't actually share demand data across purchasing, production, and distribution functions
- **Usually means:** the structural fix for bullwhip variability isn't actually functioning if the shared information base isn't real, regardless of whether a process nominally exists.
- **First question:** "Does the S&OP process actually give every function the same real demand data, or does each stage still plan off its own local signal?"
- **Data to pull:** the S&OP process's actual data inputs per function, whether demand information is genuinely shared or siloed.
