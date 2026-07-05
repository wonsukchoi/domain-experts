# Underwriting artifacts — filled templates

Working templates an agent can populate. Numbers continue the Meridian Fabricating Co. renewal from `SKILL.md` (structural steel fabricator, TIV $18.4M, GL rated on revenue, $9.2M → $11.4M) so the arithmetic stays internally consistent across documents.

## 1. Renewal underwriting worksheet

**Loss experience triangle (basic-limit capped at $250K, $000s):**

| Policy year | Earned premium | Raw incurred | Large loss (capped) | Attritional | Capped incurred | Capped LR |
|---|---|---|---|---|---|---|
| Yr 1 (3 yrs ago) | 395 | 612 | 480 → 250 | 132 | 382 | 96.7% |
| Yr 2 | 415 | 158 | — | 158 | 158 | 38.1% |
| Yr 3 (expiring) | 438 | 402 | 275 → 250 | 127 | 377 | 86.1% |
| **3-yr total** | **1,248** | **1,172** | | | **917** | **73.5%** |

Trended (×1.10 development/trend factor): 917 × 1.10 = 1,009 → trended LR 80.8%. Credibility Z = √(14 claims / 1,082 full-credibility standard) = 11.4%. Manual expected LR = 58.0%. Credibility-weighted LR = 0.114(80.8) + 0.886(58.0) = **60.6%** → experience mod **1.045**.

**GL rating worksheet (exposure = revenue, per $1,000):**

| Factor | Value | Running rate |
|---|---|---|
| Bureau loss cost | $4.85 | — |
| × Company loss-cost multiplier | 1.35 | $6.55 |
| × ILF ($1M/$1M → $2M/$2M) | 1.16 | $7.598 |
| × Schedule credit (safety program) | 0.93 | $7.066 |
| × Experience mod | 1.045 | **$7.384** |

Premium = $11,400 (revenue in $000s) × $7.384 = **$84,178**, vs. prior $65,007 at mod 1.00 on $9,200 revenue (+29.5% = 23.9 pts exposure growth × 1.045 mod).

## 2. Cat model PML table (property, by return period)

| Return period | Modeled loss (% of TIV) | Modeled loss ($) | vs. treaty automatic capacity ($10M) |
|---|---|---|---|
| 10-year | 8% | $1.47M | within |
| 50-year | 28% | $5.15M | within |
| 100-year | 45% | $8.28M | within |
| **250-year** | **62%** | **$11.4M** | **exceeds by $1.4M** |
| 500-year | 74% | $13.6M | exceeds by $3.6M |

Post-reinforcement 250-year PML (35% reduction to structural loss component): $11.4M × 0.65 = **$7.4M** — back within automatic capacity. Facultative quote for the current $1.4M excess: $1.4M × 7.5% ROL = **$105,000**/yr, vs. one-time insured cost of ~$140,000 to reinforce.

## 3. Deductible / SIR comparison (primary GL, current $10K deductible)

| Option | Retention type | Loss elimination ratio | Premium credit | Collateral required | Net effect |
|---|---|---|---|---|---|
| Hold at $10K | Deductible | — (baseline) | — | No | Status quo |
| $25,000 | Deductible | 18% | ~7% off primary GL premium | No (under $25K trigger) | Recommended |
| $50,000 | SIR | 35% | ~13% off primary GL premium | Yes — ~$175K (3.5× expected retained losses) | Broker's ask; collateral cost likely exceeds the savings for a mid-market insured |

**Underwriter note (quotable):** "35% LER on the $50K SIR looks like the better economics until you price the $175K collateral post — for an account this size that's a bigger balance-sheet ask than the premium credit is worth. Counter at $25,000 deductible: no collateral trigger, 18% LER, and the broker still gets a credit to bring back to the insured."

## 4. Referral memo template (filled)

```
TO: UW Committee
FROM: [Underwriter], Commercial P&C
RE: Meridian Fabricating Co. — renewal referral (three independent triggers)
DUE: [date] — quote must go to broker within 5 business days

TRIGGERS:
1. Raw 3-yr loss ratio 93.9% (> 70% mandatory-referral threshold)
2. Modeled 250-yr PML ($11.4M) exceeds treaty automatic capacity ($10M)
3. Facultative reinsurance required for the $1.4M excess

ANALYSIS:
- Capped/trended/credibility-weighted LR is 80.8% account-specific, 60.6%
  blended; experience mod 1.045 (4.5% debit) — NOT the 44.5% the raw
  number implies. Cause: one large fire loss (Yr1, roof collapse, snow
  load) and one open liability claim (Yr3, $275K reserve) drove the raw
  number; both capped at basic limit for pricing purposes.
- Roof collapse cause has NOT been remediated — this is the one place the
  credibility-weighted number understates real hazard. Recommend an
  engineering condition, not just a rate.
- GL premium moves +29.5% (23.9 pts exposure growth on $9.2M->$11.4M
  revenue, 4.5 pts new experience mod) — broker needs this decomposition
  before the quote lands or the increase reads as punitive.

RECOMMENDATION:
Bind, conditioned on ONE of:
  (a) signed roof-reinforcement commitment (engineer's letter in hand,
      completion verified within 6 months) — models to $7.4M PML, removes
      facultative requirement entirely, or
  (b) facultative cession of the $1.4M excess at $105K/yr, cost passed
      through as a property premium surcharge.
Hold umbrella ROL flat at 0.76% given class severity tail. Recommend
$25,000 GL deductible (not the requested $50K SIR) to avoid triggering
collateral for no net insured benefit.
```

## 5. Quote / conditions-of-renewal letter (filled excerpt)

```
Re: Meridian Fabricating Co. — Renewal Terms

We are pleased to offer renewal terms subject to the following:

1. Property (TIV $18.4M): terms bound subject to EITHER (a) a signed
   commitment to complete roof structural reinforcement per the attached
   engineering scope within 6 months of binding, with a mid-term
   inspection contingency, OR (b) acceptance of a $0.105M facultative
   reinsurance surcharge on the property premium. Wind/hail deductible
   remains 5% of TIV ($920,000 minimum).

2. General Liability: $1M/$2M limits, revenue-rated at $11.4M reported
   revenue - premium $84,178 (see enclosed rating detail: 23.9 points of
   this change is exposure growth on your reported revenue increase,
   4.5 points is an experience modification). Deductible option: we can
   offer $25,000 per-occurrence at no collateral requirement; a $50,000
   self-insured retention is available but requires ~$175,000 posted
   collateral per our retention program.

3. Umbrella: $5M xs $1M, premium $38,000, terms unchanged.

This quote is valid for 15 business days. Please confirm which property
condition you're electing so we can bind on schedule.
```
