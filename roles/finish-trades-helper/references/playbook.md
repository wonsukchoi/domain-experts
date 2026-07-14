# Finish Trades Helper Playbook

Filled templates for batching, containment, and coverage across paint, wallcovering, and plaster/stucco days. Populate with the day's real numbers — don't work from the blank column headers.

## Plaster/stucco base-coat mix and coverage

| Coat | Thickness | Cement:sand ratio (by volume) | Coverage per bag of cement (94 lb) |
|---|---|---|---|
| Scratch coat | 3/8" | 1:4 | ~80 sq ft at 3/8" |
| Brown coat | 3/8" | 1:4 to 1:5 | ~80 sq ft at 3/8" |
| Finish coat (trowel/float) | 1/8" | Manufacturer premix (no field cement:sand ratio) | Per bag — check product data sheet |

**Take-off formula:** wall area (sq ft) × thickness (ft) = mud volume (cu ft). Split volume by ratio parts (e.g., 1:4 = 5 parts total) to get cement and sand volumes. 1 bag portland cement ≈ 1 cu ft; sand is ordered by cu yd (27 cu ft/yd) or by weight (~2,700 lb/yd).

Example: 600 sq ft × 0.03125 ft (3/8") = 18.75 cu ft → cement 3.75 cu ft (4 bags), sand 15 cu ft (0.56 → order 0.75 cu yd).

## Weather-adjusted batch-scheduling template (cement plaster, no retemper)

1. Get the plasterer's trowel/scratch rate (sq ft/hr) for today's coat.
2. Check ambient temperature, RH, and wind against normal-condition assumptions (roughly 70-80°F, RH >40%, wind <10 mph).
3. Set today's working-life window: ~90 min normal conditions; ~60 min if temp >85°F or wind >10 mph or RH <20%; shorter still if two or more of those stack.
4. Batch size (sq ft) = trowel rate × working-life window (hours).
5. Mix each new batch when the current one has about 15-20% of its area remaining, not when it runs out.
6. Log actual mix time per batch — no retemper past initial stiffening; a batch that stiffens before it's placed is a discard, not a fix.

| Batch | Area (sq ft) | Mix start (min) | Placement time (min) | Done (min) | Condition |
|---|---|---|---|---|---|
| 1 | 100 | 60 | 60 | 120 | Normal-adjusted (60-min window) |
| 2 | 100 | 110 | 60 | 170 | |
| 3 | 100 | 160 | 60 | 220 | |
| 4 | 100 | 210 | 60 | 270 | Stoppage +10 min this batch |
| 5 | 100 | 310 | 60 | 370 | Shifted +10 min |
| 6 | 100 | 370 | 60 | 430 | Shifted +10 min |

## Cure-time reference (portland cement plaster, ASTM C926 / IRC §R703.6.2.1)

| Between coats | Minimum cure |
|---|---|
| Scratch → brown | 48 hours |
| Brown → finish | 7 days |

Extend both minimums, don't shorten them, when RH is trending low or wind is elevated during the cure window — the code number is a floor for normal conditions, not a target for adverse ones.

## RRP (lead-safe) containment sizing (40 CFR 745.85)

| Structure | Triggers RRP practices when prep disturbs |
|---|---|
| Interior room, pre-1978 | > 6 sq ft of painted surface |
| Exterior, pre-1978 | > 20 sq ft of painted surface, or any work within 10 ft of the foundation |

**Containment checklist when triggered:**
1. Poly sheeting on floor/ground extending at least 10 ft from the work area (exterior) or covering the full room (interior).
2. No dry-scraping without HEPA-shrouded tools; no open-flame paint removal; no uncontained power-sanding.
3. Warning signs posted at containment boundary.
4. HEPA vacuum + wet-wipe cleanup before containment comes down.
5. Verification (visual + optional dust-wipe clearance) logged before the area is turned back over.

## Paint boxing and spread-rate reference

| Job size (same color, continuous surface) | Boxing practice |
|---|---|
| 1 can | No boxing needed |
| 2+ cans, same batch/lot number | Boxing optional but recommended for large sprayed areas |
| 2+ cans, different batch/lot numbers | Box into one container before loading sprayer or cutting in — mandatory to avoid flash lines |

Typical spread rate: ~350-400 sq ft/gallon per coat on primed drywall or siding (check the product's technical data sheet — this varies by product and substrate porosity).

## Wallcovering paste/book-time reference

| Material | Open/tack time after pasting | Book time before hanging |
|---|---|---|
| Pre-pasted vinyl (light-medium weight) | Skins in ~10-15 min in normal humidity | 3-5 min |
| Pre-pasted heavier vinyl/non-woven | Skins in ~10-15 min | 5-10 min |
| Clear premixed paste (non-pre-pasted stock) | ~10-15 min before edges start to skin | N/A — hang promptly after pasting |

Default to a 5-minute book when the manufacturer instruction sheet is missing or unclear; check the actual instruction sheet first — book times vary by material weight.

## Painter's tape removal window

| Condition | Removal window |
|---|---|
| Interior, out of direct sun | Same day to 24 hours |
| Exterior or direct sun exposure | Same day |
| Product technical data sheet states otherwise | Follow the data sheet — some low-tack products are rated for multi-day exposure |
