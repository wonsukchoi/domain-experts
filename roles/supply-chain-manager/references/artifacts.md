# Risk & network design artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Concentration risk map (filled example)

| Input | Sourcing concentration | Disruption cost estimate | Current mitigation | Priority |
|---|---|---|---|---|
| Critical semiconductor component | Single supplier, single region | $19.82M (90-day disruption) | None — flagged for diversification | High |
| Standard packaging material | Multiple suppliers, multiple regions | Low (~$150K, short substitution time) | Already diversified | Low |
| Specialized coating chemical | Single supplier, different region | $6.2M (60-day disruption) | Buffer stock (8 weeks), no secondary supplier | Medium |

**Rule applied:** priority is set by disruption cost and current mitigation gap, not by spend volume alone — the semiconductor component tops the list because it's both high-cost-if-disrupted and currently unmitigated.

## 2. Efficiency-resilience tradeoff model (filled — see Worked example in SKILL.md for full narrative)

| Option | Annual cost | Expected disruption cost (25% probability) | Total expected cost (year 1) |
|---|---|---|---|
| Stay single-sourced | $24,000,000 (current spend) | $4,955,000 | $28,955,000 |
| Diversify (30% to alternate supplier) | $24,000,000 + $2,100,000 premium + $850,000 one-time = $26,950,000 | Near-zero (risk substantially mitigated) | $26,950,000 |

**Reading it:** diversification's total expected cost is lower than staying single-sourced once the expected disruption cost is properly counted — this isn't a "pay more for safety" tradeoff, it's a lower total-expected-cost option once risk is priced in.

## 3. Bullwhip mitigation plan (filled example)

| Stage | Current forecasting input | Issue | Fix |
|---|---|---|---|
| Retailer | Point-of-sale end-customer demand | None — accurate real signal | N/A |
| Distributor | Retailer's order pattern (not POS data) | Amplifies retailer's order-batching variability | Connect distributor forecasting to shared POS data feed |
| Manufacturer | Distributor's order pattern | Further amplified variability, driving excess safety stock | Same shared-data connection via S&OP |
| Raw material supplier | Manufacturer's order pattern | Largest amplification, causing supplier capacity whiplash | Full S&OP integration with real end-demand visibility |

**Rule applied:** the fix at every stage is the same structural one (shared real-demand data via S&OP), not individual forecasting-improvement projects at each link, since the root cause is structural amplification, not any single stage's forecasting skill.

## 4. Disruption scope assessment template (filled example)

> **Event:** Regional geopolitical escalation affecting primary semiconductor supplier's manufacturing region.
> **Initial assessment (within 4 hours):** Confirmed via supplier contact and control-tower data — production continuing at 100% capacity currently, but export/logistics corridor at elevated risk over the next 4-8 weeks.
> **Scope:** Not yet a production stoppage; a logistics-corridor risk with an estimated 25% chance of escalating to a 90+ day supply interruption.
> **Response calibration:** Given the assessed scope (elevated risk, not active stoppage), response is proactive diversification (qualify alternate supplier, shift 30% volume) rather than emergency stockpiling or full supply-line rerouting, which would be a disproportionate reaction to the currently assessed risk level.
