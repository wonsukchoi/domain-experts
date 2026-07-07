# Playbook

Filled procedures and templates, not descriptions of them. Use these as the actual worksheet.

## Shift-open PAR checklist (18-seat bar top + service well, ~120 covers/night volume)

| Item | PAR (units) | Set to survive |
|---|---|---|
| Ice (well bin) | 180 lbs | 4-hour rush before restock run |
| Citrus wheels (lemon/lime/orange, cut) | 6 doz each | Full Friday shift |
| Olives/cherries (garnish bins) | 2 qt each | Full shift |
| Speed rail well spirits (per slot) | 2 backups behind pour bottle | ~90 min at rush pour rate |
| Mixers (soda gun lines + bottled) | Full bag-in-box + 1 spare | Full shift |
| Bar towels | 24 | Full shift, laundered mid-shift if slammed |

Heuristic: garnish and ice PAR set for the *slowest* restock window of the night (usually the 90 minutes after last call for barbacks), not the average — running out at 11pm is recoverable, running out at 1:30am during last call is not.

## Pour-cost reconciliation worksheet (fill per shift or per period)

| Category | Units sold (POS) | Standard pour (oz) | Theoretical oz | Actual oz depleted (bottle weight) | Variance oz | Variance % |
|---|---|---|---|---|---|---|
| Well | 260 | 1.5 | 390 | 449 | +59 | +15.1% |
| Call | 100 | 1.5 | 150 | 162 | +12 | +8.0% |
| Premium/craft | 50 | 2.0 | 100 | 128 | +28 | +28.0% |

Formula: `Theoretical oz = units sold × standard pour oz`. `Variance % = (Actual − Theoretical) / Theoretical`. Flag any category over +10% for a bottle-weight spot check before assuming staff behavior; check the POS recipe-costing template first if the overage concentrates in one specific drink rather than spreading evenly across a category.

## Bottle-weight spot check (confirms or rules out free-pour drift)

1. Weigh the bottle before service (or use a known full-bottle baseline weight, e.g., a 750ml well vodka bottle = 1,750g full, empty bottle = 500g, so 1,250g = liquid, and 1g ≈ 0.033oz at vodka's density).
2. Pour 10 timed, normal-service pours to the standard glass — no special care taken, this simulates real conditions.
3. Reweigh. Expected depletion at a clean 1.5oz standard = 15.0oz. Convert weight loss to oz and compare.
4. Example: weight loss = 516g → 516 × 0.033 ≈ 17.0oz depleted for 10 pours → average pour 1.70oz, a 13.3% overpour. Above the ±0.25oz (≈16.7%) tolerance band on the high side is borderline; above it consistently across two checks is a retrain trigger, not a one-off.

## Drink-tier pricing table (target pour cost 20%, house example)

| Tier | Pour (oz) | Unit spirit cost/oz | Cost per drink | Target cost % | Menu price |
|---|---|---|---|---|---|
| Well | 1.5 | $0.71 | $1.07 | 20% | $7.00 (round to venue's price ladder) |
| Call | 1.5 | $1.10 | $1.65 | 15% | $9.00 |
| Premium/craft | 2.0 | $1.60 | $3.20 | 18% | $16.00 (add ~$1.50 for modifiers/garnish) |

Heuristic: well is priced tight to the house-wide pour-cost target because it's the volume driver; call and premium are priced to a *lower* cost percentage (higher dollar margin) because the price ceiling is set by perceived value, not by cost-plus math — guests won't pay double for a well drink poured heavier, but will pay for a name-brand pour or a built cocktail.

## Cutoff / refusal script (escalating)

**Stage 1 — slow, don't refuse.** "Let me get you some water and check on food while I finish this round for the table." (No mention of cutting off — most guests self-correct with a pause.)

**Stage 2 — soft refusal.** Quietly, at the guest's seat, not announced: "I'm going to switch you to water for a bit — I want to make sure you get home okay tonight." Offer a non-alcoholic option immediately so the exchange isn't just a "no."

**Stage 3 — firm refusal, one time, no debate.** "I can't serve you any more tonight. I can call you a cab or a rideshare." State once; do not re-argue the reasoning if the guest pushes back — repeat the boundary and involve a manager or security immediately if it escalates.

**Documentation (same night, before end of shift):** time, specific observed behaviors (not "seemed drunk" — "slurred order twice, dropped keys reaching for phone, raised voice at 11:40pm"), what was offered (water/food/rideshare), who else witnessed it (manager, security, other staff), and outcome. This record is the first thing pulled if a dram shop claim is ever filed.

## Till/comp reconciliation at close

1. Pull the POS Z-report: total sales, total comps/voids, total tips, payment-type breakdown.
2. Count the drawer (cash) and reconcile against the POS cash-sales line, net of the starting bank.
3. Cross-check every comp/void against the comp log — each entry needs a reason code and, above the house threshold (commonly $20 or 2 drinks), a manager initial.
4. Variance beyond roughly 1% of net cash sales (e.g., $15 on a $1,500 cash night): recount once before logging it as a shortage/overage; log the number either way, don't round it away.
5. File the shift's pour-cost worksheet and the till reconciliation together — a variance in one changes how the other should be read (a short till plus a high pour-cost variance in the same category points at a different cause than either alone).
