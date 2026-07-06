# Search Marketing Strategist — Playbook

## Keyword intent-to-strategy mapping

| Intent | Example query | Primary lever | Notes |
|---|---|---|---|
| Informational | "how does SEO work" | Organic content | Low paid commercial value; build authoritative content instead |
| Navigational | "[brand name] login" | Organic (ensure ranking #1) + light brand paid defense | Usually already ranks; paid defense against competitor bidding on brand |
| Commercial investigation | "best project management software" | Both — organic comparison content + paid non-brand bidding | High-value research-stage queries, strong candidate for both channels |
| Transactional | "buy [product] online" | Paid search (high-intent bidding) + optimized landing page | Highest commercial value; prioritize paid bidding and conversion-focused landing pages |

## Incrementality test design and calculation (filled example)

| Step | Value |
|---|---|
| Reported last-click ROAS | $180,000 revenue ÷ $20,000 spend = **9.0x** |
| Active-market conversion rate (ads on) | 3.4% |
| Holdout-market conversion rate (ads off) | 3.1% |
| Relative lift | (3.4% − 3.1%) ÷ 3.1% ≈ **9.7%** |
| True incremental revenue (9.7% × $180,000) | ≈ **$17,460** |
| **True incremental ROAS** | $17,460 ÷ $20,000 ≈ **0.87x** |

**Use:** Always run this calculation for brand paid search before trusting a reported ROAS — the gap between last-click ROAS (9.0x) and true incremental ROAS (0.87x) here shows how dramatically cannibalization can distort the apparent value of a campaign.

## Quality Score diagnostic checklist

1. Check expected CTR component — is the ad copy compelling and relevant to the specific keyword, not just the campaign theme?
2. Check ad relevance component — does the ad's headline and description closely match the specific keyword being bid on?
3. Check landing page experience component — page load speed, mobile usability, and content relevance to the ad and keyword.
4. Identify the lowest-scoring component and address it directly before considering a bid increase.

**Use:** Never raise a bid to compensate for a low Quality Score without first identifying and fixing the specific underlying component — the bid increase treats a symptom, not the cause, and keeps CPC elevated indefinitely.

## Marginal ROAS / saturation curve table (illustrative structure)

| Monthly spend tier | Incremental spend | Incremental revenue | Marginal ROAS |
|---|---|---|---|
| $0 - $10,000 | $10,000 | $60,000 | 6.0x |
| $10,000 - $20,000 | $10,000 | $45,000 | 4.5x |
| $20,000 - $30,000 | $10,000 | $22,000 | 2.2x |
| $30,000 - $40,000 | $10,000 | $9,000 | 0.9x |

**Use:** Read this table by marginal ROAS at each tier, not average ROAS across total spend — here, moving from $30K to $40K would be unprofitable (0.9x marginal ROAS) even though the average ROAS across all spend to date might still look acceptable.

## Attribution model comparison checklist

1. Pull channel-level performance under last-click attribution.
2. Pull the same channels' performance under a data-driven or multi-touch model.
3. Identify any channel where the two models diverge significantly (e.g., strong under multi-touch, weak under last-click).
4. Treat a large divergence as a signal that the channel plays an assisting role the last-click model doesn't capture — factor this into budget decisions rather than relying on last-click alone.

## Incrementality findings memo — filled example

> **Brand Paid Search Incrementality Analysis — [Month]**
> Last-click attributed ROAS: 9.0x ($180,000 revenue ÷ $20,000 spend).
> Geo holdout test: active-market conversion rate 3.4% vs. holdout (ads-off) conversion rate 3.1% — **9.7% relative lift**, indicating ~90% of attributed conversions are cannibalized organic.
> True incremental revenue: ≈$17,460. **True incremental ROAS: ≈0.87x — the campaign is running at a loss on a true-incrementality basis despite the 9.0x reported figure.**
> **Recommendation: Reduce or reallocate brand paid search spend toward non-brand/upper-funnel terms where incrementality is higher; re-test brand spend levels periodically as organic ranking strength changes.**
