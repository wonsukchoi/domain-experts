# Cargo and Freight Agent — Playbook

## Dimensional weight calculation (filled example)

| Field | Value |
|---|---|
| Shipment dimensions | 48in × 40in × 60in |
| Volume (in³) | 48 × 40 × 60 = 115,200 in³ |
| Volume (ft³) | 115,200 ÷ 1,728 = 66.67 ft³ |
| DIM divisor — domestic air/parcel | 166 in³/lb |
| DIM divisor — international air | 139 in³/lb |
| DIM weight (domestic air) | 115,200 ÷ 166 = 694.0 lbs |
| DIM weight (international air) | 115,200 ÷ 139 = 828.8 lbs |
| Actual (scale) weight | 380 lbs |
| **Billed weight** | greater of actual and DIM = **694 lbs (domestic air)** |

Rule: always bill the greater of actual weight and DIM weight. A shipment with actual weight far below its DIM weight ("light and bulky") bills on DIM; a shipment where actual weight exceeds DIM ("dense and heavy") bills on actual.

## Density-based freight class lookup (filled example, LTL)

| Density (lbs/ft³) | Typical NMFC class range | Rate multiplier vs. baseline |
|---|---|---|
| < 1 | 400-500 (very low density) | 3.0-4.0x |
| 1-2 | 300-400 | 2.2-3.0x |
| 2-4 | 175-250 | 1.5-2.0x |
| 4-6 | 125-175 | 1.2-1.5x |
| 6-8 | 100-125 | 1.0-1.2x |
| 8-12 | 85-100 | 0.85-1.0x (baseline) |
| 12-15 | 70-85 | 0.75-0.85x |
| > 15 | 50-70 (dense, palletized) | 0.55-0.75x |

Table values are illustrative for teaching the density-to-class relationship; always confirm exact class against the current NMFC guide or classification tool for billing purposes. Foam-insert example: 5.70 lbs/ft³ falls in the 4-6 range → class ~175.

## Mode-comparison worksheet (filled example)

| Mode | Billed weight | Rate | Total cost | Transit time |
|---|---|---|---|---|
| Ground LTL (class 175) | 380 lbs (actual, LTL bills actual × class rate) | $1.35/lb | $513.00 | 4-5 business days |
| Domestic air | 694 lbs (DIM) | $2.10/lb | $1,457.40 | 1-2 business days |
| Cost delta | — | — | $944.40 (184% more) | 3+ days faster |

Decision rule: recommend the cheaper mode unless the shipper has stated a deadline the cheaper mode can't meet, or the cost of delay (stockout, contractual penalty, spoilage) exceeds the mode-cost delta.

## Bill of lading — required fields checklist

- [ ] Shipper and consignee name/address (exact legal entity, not "same as invoice")
- [ ] Piece count and packaging type (e.g., "1 pallet, shrink-wrapped")
- [ ] Weight (verified actual, not shipper-estimated)
- [ ] NMFC class (verified via density calculation, not commodity guess)
- [ ] Commodity description (specific enough to support the claimed class)
- [ ] Special-handling instructions (fragile, do-not-stack, temperature-controlled, hazmat placarding if applicable)
- [ ] Declared value (confirmed with shipper — this caps carrier liability on a claim)
- [ ] Freight charge terms (prepaid vs. collect, and who's billed)

## Cargo-claim documentation checklist (filled example scenario)

Scenario: consignee reports 2 of 10 cartons crushed on a ground LTL delivery.

| Documentation item | Status | Why it matters |
|---|---|---|
| Delivery receipt exception noted at time of delivery ("2 ctns crushed") | Present — driver and consignee both signed | Establishes damage was discovered at delivery, not later mishandling by consignee |
| Photos of damaged cartons, taken before unpacking | Present, 6 photos | Visual proof of damage extent and packaging condition |
| Photos of original packaging/bracing | Missing | Weakens argument that damage occurred in transit vs. inadequate packaging — request from shipper's records if available |
| Bill of lading matching declared value | Present, $4,200 declared | Caps recoverable amount at $4,200 regardless of actual replacement cost |
| Claim filed within carrier's claim window (typically 9 months under Carmack for domestic) | Filed day 3 | Well within window — no timing issue |

Outcome: claim proceeds with 4 of 5 documentation items present; missing packaging photos noted explicitly in the claim narrative rather than omitted, so the adjuster sees the gap was disclosed, not hidden.
