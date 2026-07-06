# Farm Products Buyer — Playbook

## Basis history table (corn, this elevator, cents relative to nearby board)

| Month | Sep (harvest) | Oct | Nov | Dec | Jan | Feb |
|---|---|---|---|---|---|---|
| 2021 | -42 | -38 | -30 | -25 | -20 | -18 |
| 2022 | -40 | -35 | -28 | -22 | -18 | -15 |
| 2023 | -45 | -40 | -32 | -24 | -20 | -16 |
| 2024 | -38 | -33 | -26 | -20 | -16 | -12 |
| 2025 | -35 | -30 | -24 | -18 | -14 | -10 |
| **5-yr avg** | **-40** | **-35.2** | **-28** | **-21.8** | **-17.6** | **-14.2** |

**Use:** Compare today's posted basis against the 5-year average for the same month. If today's September basis is quoted at -55 against a -40 average with no local cause (no plant outage, no rail congestion reported), treat it as a pricing error to flag, not a market signal.

## Moisture shrink and drying-charge schedule (corn, baseline 15.0%)

| Points over baseline | Shrink % (per point, cumulative) | Drying charge ($/bu, per point, cumulative) |
|---|---|---|
| 0.1 – 1.0 | 1.2% / point | $0.03 / point |
| 1.1 – 3.0 | 1.4% / point | $0.04 / point |
| 3.1 – 5.0 | 1.6% / point | $0.05 / point |
| >5.0 | Refer to merchandising manager — may require rejection or re-drying at grower's cost | Refer to merchandising manager |

**Worked calculation, 2.2 points over baseline:**
- Shrink: 2.2 × 1.4% = 3.08% → multiply net scale bushels by (1 − 0.0308).
- Drying charge: 2.2 × $0.04 = $0.088/bu → subtract from the futures+basis price per bushel.

## Foreign material (FM) and test weight tolerance (US #2 Yellow Corn)

| Factor | Standard / no-discount threshold | Discount trigger |
|---|---|---|
| Foreign material | ≤ 3.0% | Each 1% over 3.0% → additional 1.0% shrink |
| Test weight | ≥ 54 lb/bu (No. 2 min); 56 lb/bu common elevator baseline | Below baseline: refer to posted per-lb discount table; above baseline: no premium unless contract states one |
| Damaged kernels (total) | ≤ 5.0% | Each 1% over 5.0% → additional 0.5% shrink |

## Contract type selection table

| Grower wants to lock... | Instrument | What's still open |
|---|---|---|
| Nothing yet, selling at delivery | Spot/cash sale at delivery | Full price risk (futures + basis) until delivery |
| Futures price now, basis later | Hedge-to-arrive (HTA) | Basis — must be set before contract's stated pricing deadline |
| Basis now, futures later | Basis contract | Futures — must be set before contract's stated pricing deadline |
| Full flat price now | Cash forward contract | Nothing — both legs locked; grower is obligated to deliver at this price regardless of market moves |

## Daily position/hedge report (example, corn, by contract month)

| Contract month | Forward-purchased (bu) | Hedged (futures sold, bu) | Net open position (bu) | Action |
|---|---|---|---|---|
| Dec | 185,000 | 185,000 | 0 | None — fully hedged |
| Mar | 62,000 | 40,000 | 22,000 long-cash / short-futures needed | Sell 22,000 bu Mar futures today |
| May | 15,000 | 0 | 15,000 | Sell 15,000 bu May futures — below house limit (25,000 bu), monitor |

**Use:** Any contract month showing a net open position above the house limit (here, 25,000 bu) requires same-day hedge execution, not carry-over to the next trading day.

## Settlement statement — filled example

> **Elevator Grain Co. — Settlement Statement #4471**
> Grower: J. Alvarez Farms | Date: September 14 | Commodity: Yellow Corn | Contract ref: CF-2025-0912
>
> Gross weight: 76,540 lbs | Tare weight: 28,220 lbs | Net weight: 48,320 lbs
> Bushels (56 lb/bu): 863.9 bu gross
>
> Grade: US #2 Yellow Corn
> - Moisture: 17.2% (baseline 15.0%, 2.2 pts over)
> - Foreign material: 1.8% (within 3.0% tolerance — no discount)
> - Test weight: 57 lb/bu (above baseline — no discount)
>
> Shrink: 2.2 pts × 1.4%/pt = 3.08% → Net bushels: 837.5 bu
> Drying charge: 2.2 pts × $0.04/pt = $0.088/bu
>
> Pricing: Dec futures $4.320 + basis ($0.350) = $3.970/bu gross, less drying charge $0.088/bu = **$3.882/bu net**
>
> **Bushels paid: 837.5 bu × $3.882/bu = $3,251.18**
> **Amount due grower: $3,251.18**

## Fallback positions when elevator storage nears capacity (in preference order)

1. Widen posted basis by 5-10 cents to slow voluntary intake before turning any trucks away.
2. Offer growers a deferred-price ticket (grain accepted and weighed, price set later) to keep intake moving without committing to today's cash price.
3. Arrange overflow storage (ground piles, rented off-site bins) for grain already committed under existing forward contracts.
4. Only as a last resort, restrict intake by appointment/schedule — this is the option most likely to damage grower relationships and should be a short-term, communicated measure, not a silent cutoff.
