# Animal Scientist — Playbook

## Least-cost ration worksheet (filled example: growing beef steer, 550 lb, ADG 2.5 lb/day)

| Ingredient | % of mix (DM) | CP contribution | TDN contribution | Cost/ton | Cost contribution ($/ton mix) |
|---|---|---|---|---|---|
| Corn | 31.6% | 2.84% | 27.81% | $220 | $69.52 |
| Soybean meal | 10.7% | 5.14% | 8.99% | $420 | $44.94 |
| Grass hay | 56.7% | 4.54% | 31.19% | $150 | $85.05 |
| Mineral supplement | 1.0% | — | — | $600 | $6.00 |
| **Total** | **100.0%** | **12.5%** | **68.0%** | — | **$205.51** |

Requirement check: CP target 12.5% — met exactly (binding). TDN target 68% — met exactly (binding). Both nutrients are binding constraints; a price change on corn or soybean meal (the two ingredients carrying most of the CP/TDN load) forces a full reformulation, not a substitution.

Reformulation trigger table:

| Trigger | Action |
|---|---|
| Corn price moves >10% | Re-run full LP formulation — corn is the primary energy-cost driver |
| Soybean meal price moves >10% | Re-run full LP formulation — soybean meal is the primary protein-cost driver |
| Hay price moves >10% with no CP/TDN change | Re-run for cost only; hay is not a binding-nutrient ingredient here |
| New feed-tag analysis received | Re-run against actual analyzed values, not book values |

## EPD selection-index weighting table (filled example: terminal-sire selection)

| Trait | EPD value | Herd average | Economic weight ($/unit) | Weighted contribution |
|---|---|---|---|---|
| Birth weight | +2.1 lb | +3.0 lb | -$4.50/lb (calving-ease risk) | +$4.05 |
| Weaning weight | +58 lb | +45 lb | +$1.20/lb | +$15.60 |
| Yearling weight | +95 lb | +78 lb | +$0.95/lb | +$16.15 |
| Calving ease direct | +8.5% | +5.0% | +$2.80/% | +$9.80 |
| Milk | +18 lb | +22 lb | +$0.60/lb | -$2.40 |
| **Terminal index total** | — | — | — | **+$43.20/calf vs. herd average** |

Reading rule: a bull with an outstanding single-trait EPD (here, weaning weight +58 lb) but a below-average calving-ease EPD would score lower on the index once the calving-ease-risk weight is applied — the index total, not any single EPD, is the selection decision.

## Feed-conversion-ratio troubleshooting sequence

1. Verify dry-matter-intake measurement — check scale calibration and refusal/orts weighback; intake-measurement error is the single most common false FCR alarm.
2. Check for subclinical illness (parasite load, subclinical acidosis, respiratory disease) via pen observation and, if available, recent treatment records — illness suppresses intake and gain before visible symptoms appear.
3. Confirm the FCR benchmark used matches the animal's current growth stage — a benchmark for early-growth FCR will always look "bad" applied to a late-finishing group, which converts less efficiently by design.
4. Re-verify the ration was mixed and delivered as formulated (batch records, bunk-reading consistency) — mixing or delivery error is more common and cheaper to fix than a formulation defect.
5. Only after 1-4 are ruled out, re-run the least-cost formulation against a fresh feed-tag analysis to check for a genuine nutrient shortfall.
