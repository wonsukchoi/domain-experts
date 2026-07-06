# Real estate broker artifacts — templates with real structure

Filled examples an agent can populate directly. Numbers throughout follow the 142 Birchwood Lane scenario in SKILL.md's worked example ($649,900 list, 1,850 sqft, 1998-built, 2-car garage) unless noted.

## 1. Comparative market analysis (CMA)

Comps: sold within the trailing 3–6 months, within ~0.5 miles (wider in low-inventory rural markets), similar gross living area (±15–20%). Adjustments move the *comp's* price toward what it would have sold for with the subject's features — add value the comp lacks, subtract value the comp has that the subject doesn't.

| Comp | Sqft | Sold price | Sold date | Feature diff. vs. subject | Adjustment | Adjusted price | Adjusted $/sqft |
|---|---|---|---|---|---|---|---|
| A — 118 Birchwood Ln | 1,780 | $645,000 | 62 days ago | None material | $0 | $645,000 | $362 |
| B — 205 Maple Ct | 1,920 | $675,000 | 47 days ago | Updated kitchen (2023) | −$15,000 | $660,000 | $344 |
| C — 90 Elmwood Dr | 1,830 | $615,000 | 91 days ago | No garage (subject: 2-car) | +$8,000 | $623,000 | $340 |

**Adjustment increments used (stated heuristics for this market, not universal constants):** finished garage bay ≈ $4,000 each; updated kitchen (within 3 years) ≈ $12,000–$18,000; extra full bathroom ≈ $8,000–$10,000; each 100 sqft of GLA difference ≈ 1× the market's average adjusted $/sqft (here ≈ $349) applied only if the raw comps aren't already sqft-matched within 10%.

**Reconciliation:** average adjusted $/sqft = ($362+$344+$340)/3 ≈ $349. Applied to subject's 1,850 sqft: $645,650 point estimate. CMA range: $623,000 (low comp, C) to $660,000 (high comp, B). **List-price recommendation:** $649,900 — just above the point estimate, comfortably under the range ceiling, to generate multiple-offer velocity rather than a single post-DOM-stall lowball. State this reasoning to the seller in writing before they see a lower number than they expected.

## 2. Listing agreement (exclusive right-to-sell) — key terms block

| Term | Filled value |
|---|---|
| Type | Exclusive right-to-sell (broker earns commission regardless of who procures the buyer — the standard MLS-eligible form; exclusive agency and open listings exist but forfeit MLS cooperation incentives) |
| Term | 120 days (typical range 90–180; shorter in hot markets, longer for unique/rural properties) |
| List price | $649,900 |
| Commission | 5.0% of sale price, split per cooperating-broker agreement stated separately (post-2024 settlement: buyer-broker compensation is negotiated in the buyer-representation agreement, not published in the MLS) |
| Protection period | 90 days after expiration — commission still owed if a buyer who toured during the listing term buys within this window |
| Seller disclosures required | State transfer disclosure statement, lead-based paint disclosure (pre-1978 construction only), any known material defects |

## 3. Buyer-representation agreement — key terms block

Required, signed, in writing before touring property in any market subject to the August 2024 NAR settlement changes.

| Term | Filled value |
|---|---|
| Type | Exclusive buyer representation |
| Term | 60 days (typical range 30–90; matched to the buyer's active search intensity, not a default) |
| Compensation | 2.5% of purchase price, or $8,000 minimum, whichever is greater — paid by seller/listing broker if offered as a concession, otherwise buyer pays the difference directly at closing |
| Scope | Single property vs. area-wide search — stated explicitly; a single-property agreement lets the buyer work with other agents on other properties |

## 4. Offer structure with escalation clause

Standalone addendum, not folded into the main purchase agreement body, so it can be negotiated independently of price and contingencies.

```
ESCALATION ADDENDUM — 142 Birchwood Lane

Base offer price: $650,000
Escalation increment: $3,000 above any bona fide, verifiable competing offer
Escalation cap: $685,000 (offer will not exceed this price under any circumstance)
Verification: Seller's agent must provide a copy of the competing offer's signature
  page and price term (redacted of buyer-identifying information) before this
  clause activates.
If no competing offer is presented, Base offer price stands.
```

**Appraisal-gap coverage addendum (separate clause — do not merge with escalation):**

```
APPRAISAL GAP ADDENDUM

If the property appraises below the final contract price, Buyer agrees to pay,
in addition to the down payment, the difference between the appraised value
and the contract price, up to a maximum of $10,000. Any gap beyond $10,000
reopens price negotiation or permits either party to terminate under the
appraisal contingency, at Buyer's election.
```

## 5. Multiple-offer comparison worksheet

Rank on realized-price expectation, not headline price. Row order: price → financing strength → EMD as a % of price (signals commitment) → contingencies retained → appraisal-gap coverage → expected close date.

| | Offer A | Offer B | Offer C |
|---|---|---|---|
| Price | $655,000 | $675,000 | $678,000 (escalated) |
| Financing | Conventional, 20% down | Conventional, 30% down | Conventional, 25% down |
| EMD | $9,825 (1.5%) | $20,250 (3.0%) | $13,000 (2.0% of the $650,000 base offer) |
| Inspection contingency | Standard (10 days) | Waived | Waived except major systems/structural |
| Financing contingency | Standard (21 days) | Standard (21 days) | Standard (21 days) |
| Appraisal-gap coverage | None | $15,000 | $10,000 |
| Est. appraised value (broker's CMA-based estimate) | $660,000 | $660,000 | $660,000 |
| Realized price if appraisal holds at $660,000 | $655,000 (no gap) | $675,000 (gap $15k, fully covered) | ~$670,000 (gap $18k, only $10k covered — renegotiates down) |
| Est. close timeline | 30 days | 21 days | 24 days |

**Recommendation line for the seller memo:** rank by the "realized price if appraisal holds" row, not the headline price row — see SKILL.md worked example for the full reasoning and the deliverable memo.

## 6. Seller estimated net proceeds sheet

Run before the seller counters or accepts, not after.

| Line | Amount |
|---|---|
| Accepted price | $675,000 |
| Less: listing commission (5.0%) | −$33,750 |
| Less: existing mortgage payoff | −$310,000 |
| Less: prorated property tax (seller's share, 4 months of $8,400/yr bill) | −$2,800 |
| Less: title/escrow fees (seller's customary share) | −$2,200 |
| Less: any negotiated seller concessions (e.g., buyer's closing costs) | $0 (none in this offer) |
| **Estimated net to seller** | **$326,250** |
