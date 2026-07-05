# Artifacts & templates

Filled examples an agent can populate or execute against. Load this when producing an actual stage-gate memo, TEA comparison, or balance tracker — not for general reasoning (that's `SKILL.md`).

## Stage-gate template with TRL criteria

```
GATE REVIEW: [Process name] — Gate [N]: [Bench → Pilot / Pilot → Demonstration / Demo → Commercial]

Current TRL claimed: [N]
Data supporting this TRL claim:
  - Throughput demonstrated: [X kg or tons/day] for [Y] consecutive days
  - Mass balance closure: [Z]% (threshold: within 5%)
  - Energy balance closure: [Z]% (threshold: within 10%)
  - Yield stability: [mean ± std dev] over the run
  - Feedstock variability tested: [single lot / N lots spanning typical composition range]

Next tier requirements (must be satisfied before capital release):
  - Throughput target: [10x current, or as scoped]
  - Duration: [minimum continuous run, e.g. 60-90 days]
  - Balance closure threshold: [5%]
  - Go/no-go criteria: [explicit — e.g. "yield must not degrade >5% relative from bench baseline"]

Capital at risk if this gate is skipped: $[estimate]
Estimated cost of a failed attempt at next tier if this gate's data gap isn't closed: $[range], based on [comparable industry cases if available]

Recommendation: [Proceed to next tier / Hold for more data / Do not proceed]
```

## Techno-economic comparison table (credit-adjusted revenue per unit feedstock)

```
Process           | Yield  | Fuel price | CI score      | Credit value    | Revenue/ton feedstock
                   |        | ($/gal)    | (gCO2e/MJ)    | ($/ton CO2e)    | (fuel + credit)
-------------------|--------|------------|---------------|-----------------|----------------------
Process A (soy)    | 88%    | $3.20      | 55            | $75             | $612/ton
Process B (UCO)    | 82%    | $3.20      | 25            | $75             | $698/ton
Process C (tallow) | 85%    | $3.20      | 40            | $75             | $651/ton

Calculation basis (Process B example):
  Fuel revenue = 0.82 yield × [gal/ton feedstock conversion factor] × $3.20/gal
  Credit revenue = (100.45 baseline CI − 25 CI) × [MJ/gal] × [gal/ton] ÷ 1,000,000 × $75/tonCO2e
  Total = fuel revenue + credit revenue, per ton of feedstock consumed

NOTE: baseline diesel CI (~100.45 gCO2e/MJ), credit values, and conversion factors are program- and
year-specific — pull current published values (e.g., CARB LCFS quarterly report) before using this
table for an actual decision; the structure of the calculation is the reusable part, not these numbers.
```

## Mass/energy balance closure tracker (per pilot run)

```
Run ID: [date/batch]           Duration: [N days]           Throughput: [X kg/day]

INPUTS (mass):                          OUTPUTS (mass):
Feedstock: [X] kg                       Product (fuel): [Y] kg
Hydrogen/reagent: [X] kg                Byproduct stream 1: [Y] kg
Catalyst (net consumed): [X] kg         Byproduct stream 2: [Y] kg
                                         Waste/loss (measured): [Y] kg
Total in: [sum]                         Total out: [sum]

Closure = Total out / Total in × 100% = [Z]%
Threshold: 95-105% (within 5%) to proceed to next scale tier
Unaccounted gap: [Total in − Total out], investigate if closure outside threshold before any further capital commitment
```
