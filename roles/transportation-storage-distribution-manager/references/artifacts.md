# Network diagnostic artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Order-flow breakdown (filled — see Worked example in SKILL.md for full narrative)

| Stage | 6 months ago | Current | Change |
|---|---|---|---|
| Order processing (warehouse pick/pack) | 14 hours | 38 hours | +24 hours |
| Last-mile delivery | 32 hours | 33 hours | +1 hour (flat) |
| **Total order-to-delivery** | **46 hours** | **71 hours** | **+25 hours** |
| Target | 48 hours | 48 hours | — |

**Reading it:** essentially all of the added delay (24 of 25 hours) is in warehouse processing, not delivery — the proposed truck-capacity fix would target the 1-hour-flat stage, not the 24-hour-growth stage.

## 2. Capacity gap sizing (filled example)

| Metric | Value |
|---|---|
| Current warehouse processing capacity | 2,400 orders/day |
| Current incoming order volume | 3,100 orders/day (45% growth over 6 months) |
| **Capacity gap** | **700 orders/day** |
| Full second shift (oversized fix) | +1,400 orders/day capacity, $340,000/year |
| Right-sized fix (4 additional pickers) | +700 orders/day capacity, $170,000/year |

**Rule applied:** the fix is sized to close the measured 700 orders/day gap exactly, not to whichever standard staffing increment (a full shift) happens to be administratively convenient.

## 3. Safety stock model (filled example)

| SKU | Avg. demand/week | Demand std. dev. | Lead time (days) | Lead time std. dev. | Calculated safety stock | Flat-rule (10%) safety stock |
|---|---|---|---|---|---|---|
| SKU A (high variability) | 1,200 units | 340 units | 12 | 4 | 890 units | 120 units — undersized |
| SKU B (stable demand) | 800 units | 60 units | 8 | 1 | 95 units | 80 units — reasonably close |

**Rule applied:** SKU A's flat-rule safety stock (120 units) would badly understate what its actual demand variability requires (890 units), risking frequent stockouts — this is exactly why safety stock is calculated per-SKU rather than applied as a uniform percentage.

## 4. Total landed cost comparison (filled example)

| Mode | Freight cost/unit | Transit time | Carrying cost during transit | Stockout risk cost (estimated) | Total landed cost/unit |
|---|---|---|---|---|---|
| Ocean freight | $2.10 | 28 days | $0.85 | $0.60 (higher variability, more stockout exposure) | $3.55 |
| Air freight | $6.40 | 3 days | $0.09 | $0.05 | $6.54 |
| Expedited ocean | $3.20 | 14 days | $0.42 | $0.20 | $3.82 |

**Rule applied:** the decision compares total landed cost, not freight quote alone — standard ocean freight looks cheapest on freight cost, but expedited ocean is close in total landed cost while meaningfully reducing stockout risk, making it the better choice for this product's actual risk profile.
