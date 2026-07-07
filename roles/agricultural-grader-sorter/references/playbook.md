# Playbook

Filled reference tables and decision sequences for line-side grading and lot disposition. Load this when running an actual sample, sizing a sampling plan, or working the resort/downgrade/reject decision.

## 1. Nested defect-tolerance pattern (USDA 7 CFR 51 series)

USDA fresh-produce grade standards share a common nested-tolerance shape: the top grade allows the smallest total defect percentage, and only a fraction of that total can be the more serious sub-categories. Apples (7 CFR 51.300 et seq.) as the reference commodity:

| Grade | Total defect allowance | Of which, max "serious damage" | Of which, max decay |
|---|---|---|---|
| US Extra Fancy | 5% | 2.5% (half of total) | 0.5% (a tenth of total) |
| US Fancy | 10% | 5% (half of total) | 1% (a tenth of total) |
| US No. 1 | 10% | 6% | 1% |

Potatoes (7 CFR 51.1540 et seq.) follow the same nested shape at different absolute numbers — US No. 1 allows 5% total defects with 1% max for serious damage/soft rot/freeze injury; US No. 2 allows 10% total with 2% max serious damage. **The lesson that transfers across commodities: never grade against the total percentage alone — bucket every defect and check the sub-allowance separately, because a lot can be well within the total and still fail on decay or serious damage alone.**

Eggs (USDA AMS Egg-Grading Manual, AH-75) grade on different axes — Haugh unit (albumen quality) and air-cell depth (age/moisture loss), both read by candling:

| Grade | Haugh unit | Air cell depth |
|---|---|---|
| AA | ≥ 72 | ≤ 1/8 in (3.2 mm) |
| A | ≥ 60 | ≤ 3/16 in (4.8 mm) |
| B | < 60 | > 3/16 in |

## 2. ANSI/ASQ Z1.4 sampling excerpt (General Inspection Level II, AQL 2.5%)

Used to size the QC sample off the declared lot size — never a fixed headcount regardless of lot size.

| Lot size range (pieces) | Code letter | Sample size (n) | Accept (Ac) | Reject (Re) |
|---|---|---|---|---|
| 281–500 | H | 50 | 3 | 4 |
| 501–1,200 | J | 80 | 5 | 6 |
| 1,201–3,200 | K | 125 | 7 | 8 |
| 3,201–10,000 | L | 200 | 10 | 11 |
| 10,001–35,000 | M | 315 | 14 | 15 |

**Reading it:** find the row for the declared lot size, pull that many pieces at random across the full lot (not the top layer of a bin, not the first cartons off the truck), count defects, compare to Ac/Re. Defect count ≤ Ac → accept. Defect count ≥ Re → fails at that sample; do not creep the number back down by resampling the same lot with a different handful. A count strictly between Ac and Re doesn't occur in this table (Re = Ac + 1) — the plan is binary by design.

## 3. Resort vs. downgrade vs. reject decision sequence

Run this arithmetic explicitly every time a sample crosses Re — don't default to whichever action is fastest to execute.

1. **Compute blanket-downgrade loss:** (cartons in lot) × (price at current grade − price at next grade down).
2. **Compute re-sort recovery:** assume population defect rate ≈ sample defect rate. Culled pieces → weight → juice/processing revenue (typically $0.05–$0.10/lb, well below fresh-pack price but above $0). Remaining pieces → weight → cartons → revenue at the original grade.
3. **Compute re-sort labor cost:** (lot piece count ÷ grader throughput, typically 40–50 pieces/minute) × (fully loaded hourly labor rate).
4. **Net re-sort value = recovery − labor cost.** Compare directly to blanket-downgrade loss.
5. **If re-sort net > downgrade net, re-sort.** If labor cost would exceed the grade spread (small lot, low-value commodity, short-staffed shift), downgrade instead.
6. **If defect bucket includes decay** (not just cosmetic/serious-damage), reject the affected bin/pallet section outright regardless of the dollar math — decay risk (mycotoxin carryover, cross-contamination to adjacent fruit) isn't a yield-optimization decision.

**Worked instance** (2,700-piece apple bin, 8.8% sample defect rate, Fancy $28/carton vs. No.1 $19/carton, juice $0.08/lb, labor $19/hr, 45 pcs/min):
- Blanket downgrade: 22 cartons × $9 = $198.
- Re-sort: 238 culled pcs ÷ 3/lb ≈ 79 lb × $0.08 = $6.34 juice revenue; 2,462 remaining pcs ÷ 3/lb ≈ 821 lb ÷ 40 = 20 cartons × $28 = $560. Labor: 2,700 ÷ 45 = 60 min = 1 hr × $19 = $19.
- Re-sort net: $560 + $6.34 − $19 = $547.34 vs. downgrade net $198 → re-sort by ≈$349/bin.

## 4. Escalation thresholds

| Signal | Action |
|---|---|
| Single sample crosses Re, no prior history on this grower/field | Hold lot, run resort-vs-downgrade math, log disposition. No escalation yet. |
| Sample falls exactly at Ac or Re ± 1 (marginal) | Pull one confirmatory sample, same size, before declaring a hold. |
| Two consecutive samples (same lot or same grower/field within the shift) cross Re | Escalate to QA supervisor immediately — do not resolve at station level a second time. |
| Any decay defect found in sample | Flag entire bin/pallet as suspect regardless of aggregate rate; pull adjacent-bin samples before continuing to ship from that storage block. |
| Grower/field cull rate ≥ 2x that grower's trailing-30-day average, twice in a week | Escalate to QA supervisor and flag for grower conversation — likely a field-level issue (irrigation, pest, harvest timing), not a line problem. |

## 5. Optical sorter vs. hand grading — where each wins

| Attribute | Best tool | Why |
|---|---|---|
| Size/weight | Optical sizer | Consistent, no fatigue, sub-second per piece. |
| External color | Optical/camera sorter | Calibrated color bands, more repeatable than human color judgment across a shift. |
| Brix/internal sugar, some internal defects | NIR sorter | Reads through the skin; correlates well (roughly 85–90%) with manual refractometer/cut-test checks on mature, non-fresh-damaged fruit. |
| Fresh mechanical bruising (< 4 hrs old) | Human station, post-sizer | Bruising hasn't discolored enough yet for camera/NIR to flag; feel (firmness) catches it before sight can. |
| Incipient decay (not yet visibly soft/discolored) | Human, trained on smell/feel cues + spot penetrometer checks | Sensors read what's visible now; early decay is a same-day-developing condition. |
| Shape/stem-bowl defects, unusual cultivar variance | Human | Rule-based optical thresholds struggle with shape variance across natural product; humans generalize faster than retraining a sorter's model. |

**Line design consequence:** put the optical sorter first (size/color/gross culls), then a human station immediately after for same-day-harvest lots, then a final human check-weigh/spot-check before palletizing — not a single pass-through with humans spread thin across the whole line.
