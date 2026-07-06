# Online Merchant — Playbook

## Net contribution margin calculation (filled example)

| Component | Value |
|---|---|
| Retail price | $80.00 |
| Cost of goods sold (COGS) | −$32.00 |
| **Gross margin** | $48.00 (60%) |
| Payment processing fee (2.9% + $0.30) | −$2.62 |
| Outbound shipping cost (merchant-paid) | −$7.50 |
| Return rate | 25% |
| Return processing cost per returned unit | $18.00 |
| Expected return cost per unit sold (25% × $18) | −$4.50 |
| **Net contribution margin** | **$33.38 (41.7%)** |

**Use:** Always run the full cost stack past gross margin — the true net figure here (41.7%) is meaningfully lower than the headline gross margin (60%), and that gap is what actually determines whether the SKU is worth scaling.

## CAC vs. LTV calculation (filled example)

| Component | Value |
|---|---|
| First-order CAC (paid social channel) | $28.00 |
| Net contribution margin per order | $33.38 |
| Contribution after CAC (first order) | $33.38 − $28.00 = $5.38 |
| Reorder rate within 12 months | 35% |
| Average additional orders among reorderers | 1.4 |
| 12-month LTV contribution | $33.38 + (0.35 × 1.4 × $33.38) = $33.38 + $16.36 = **$49.74** |
| **CAC:LTV ratio** | $49.74 ÷ $28.00 ≈ **1.78x** |
| Healthy threshold (reference) | ~3:1 |
| **Result** | 1.78x < 3:1 → **marginal, flag for optimization before scaling** |

## Marketplace vs. owned-store comparison table (illustrative structure)

| Factor | Owned storefront | Marketplace |
|---|---|---|
| Referral/platform fee | 0% (payment processing only) | ~15% typical referral fee |
| Fulfillment fee (if using platform fulfillment) | N/A (self-fulfilled or 3PL cost) | Separate per-unit fulfillment fee |
| Customer data ownership | Full | Limited/none |
| Reach | Requires own acquisition spend | Built-in marketplace traffic |
| **Net margin impact** | Higher per-unit margin, but bears full acquisition cost | Lower per-unit margin, but lower acquisition cost due to built-in traffic |

**Use:** Fill in this table with the specific product's actual fee percentages and estimated acquisition costs on each channel before deciding — reach alone doesn't justify a channel choice without the margin and customer-data tradeoff quantified.

## Chargeback ratio monitoring checklist

1. Calculate monthly chargeback ratio (chargebacks ÷ total transactions) and track the trend over the past 6-12 months.
2. Compare against the relevant card network's monitoring/excessive-chargeback program threshold (commonly cited in the 0.65-1% range, varies by program and network).
3. If trending upward, break down chargeback reason codes to identify root cause (fraud, product dissatisfaction, friendly fraud, unauthorized transaction).
4. Address the specific root cause (fraud screening, clearer product descriptions/photos, improved customer service response time) rather than treating the ratio as an unavoidable cost.

## Inventory reorder point worksheet (illustrative structure)

| Factor | Value |
|---|---|
| Average daily demand | 12 units |
| Lead time (days) | 14 |
| Safety stock (based on demand variability) | 40 units |
| **Reorder point** (avg daily demand × lead time + safety stock) | 12×14 + 40 = **208 units** |
| Stockout cost estimate (lost sale + retention risk) | $50/unit-day of stockout |
| Holding cost estimate | $2/unit/month |

**Use:** Set safety stock by weighing the stockout cost estimate against the holding cost estimate explicitly — a safety stock level chosen only to minimize stockout risk, without checking the holding cost tradeoff, tends toward chronic overstocking.

## SKU and channel findings memo — filled example

> **SKU Profitability and Channel Analysis — Jacket SKU [ref]**
> Gross margin: 60% ($48 on $80 retail). **True net contribution margin after payment fees, shipping, and expected returns: 41.7% ($33.38/unit).**
> Paid social channel: CAC $28, 12-month LTV contribution $49.74 (including 35% reorder rate at 1.4 additional orders). **CAC:LTV ratio: 1.78x — below the ~3:1 healthy threshold.**
> **Recommendation: Do not scale paid social spend further on this SKU until CAC is reduced or retention is improved — current unit economics are marginal, not clearly profitable, despite an apparently strong 60% headline gross margin.**
