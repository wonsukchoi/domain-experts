# Playbook

Filled sequences, tables, and thresholds for the room-attendant workflow. Load this when executing a shift, training a new attendant, or building a productivity/QA program.

## 1. Room-clean sequence by type (full-service property benchmark)

| Room type | Target time | Sequence |
|---|---|---|
| Checkout | 28 min | (1) Open windows/curtains, strip bed and trash first — air the room while you work. (2) Bathroom: toilet → tub/shower → sink → floor, in that order (dirtiest-to-cleanest surface logic, never reverse). (3) Dust and wipe all hard surfaces, high to low. (4) Vacuum, door to window. (5) Remake bed, restock amenities and linens to par. (6) Final visual sweep: check under bed, behind curtains, closet, mini-fridge. |
| Stay-over | 15 min | (1) Trash and used linens/towels only if guest has signaled (towel on floor = replace; towel on rack = reuse, per standard guest-signal convention). (2) Make bed. (3) Quick bathroom refresh: wipe sink/counter, replace used towels, restock amenities. (4) Light dust of visible surfaces. (5) Empty trash. No full vacuum unless visibly needed. |
| Deep-clean / project room | 90–120 min | Full checkout sequence plus: mattress flip/rotate, drapery spot-check, AC/heater vent dusting, wall spot-cleaning, furniture pulled from walls for behind-and-under cleaning, grout/tile detail in bathroom. Scheduled on a rotation (commonly quarterly per room), not triggered by a single guest complaint alone. |
| Suite / VIP turn | 45–60 min (1.5–2.0 credits) | Full checkout sequence across each room of the suite, plus amenity upgrade placement (turndown items, welcome amenity) per the property's VIP standard — always double-checked against the VIP arrival list, since a missed VIP amenity escalates faster than a missed standard one. |

## 2. Cart par-stocking table (16-room floor cart, full-service benchmark)

| Item | Par per cart | Notes |
|---|---|---|
| Sheet sets (flat + fitted) | 3 par per bed on the floor (≈48 for a 16-room, 1-king-avg cart) | 3 par = one on the bed, one in linen closet reserve, one in laundry cycle at any time. |
| Bath towels / hand towels / washcloths | 3 par per room occupancy | Matches the sheet-par logic; a 2-par cart runs out mid-morning on a heavy checkout day. |
| Amenity sets (shampoo/soap/etc.) | 1.25× room count | The 25% buffer covers stay-over top-offs and suite double-sets. |
| Trash liners | 2× room count | One for the room bin, one for the bathroom bin. |
| Color-coded cloths | Minimum 4 per cart, kept in separate cart pockets/bins | Red or designated color = toilet/bathroom floor only. Blue = mirrors/glass. Yellow = general surfaces (desks, dressers, TV). Green = kitchen/wet bar where present. Cloths never cross zones mid-shift; a soiled cloth goes to the laundry bag, not a rinse-and-reuse. |
| Sharps container + PPE kit | 1 per cart | Nitrile gloves, puncture-resistant sharps container, red biohazard bags. Restocked at shift end regardless of whether it was used, so the next shift starts full. |

## 3. Bloodborne pathogen / sharps containment steps (OSHA 29 CFR 1910.1030-aligned)

1. **Stop the cleaning sequence immediately.** Do not continue tidying around the item.
2. **Do not touch the sharp or fluid bare-handed.** Glove up before any contact, even to move a syringe two inches.
3. **Contain the sharp** directly into the cart's puncture-resistant sharps container — never recap a needle, never place it in a regular trash bag.
4. **Bag affected linens separately** in a labeled biohazard bag if visibly soiled with blood or bodily fluid; do not add them to the standard linen bag.
5. **Radio or call the supervisor before resuming service** in that room — this is a stop-and-report step, not a stop-and-continue-solo step.
6. **Log the incident**: room number, time, description, whether any skin contact occurred, attendant name. If any contact occurred, this triggers the property's exposure-incident procedure (medical evaluation offer), not just a housekeeping note.
7. **Resume the room only after containment and the report call are complete.**

## 4. Lost-and-found chain-of-custody log (filled example)

| Field | Entry 1 | Entry 2 |
|---|---|---|
| Date/time found | 2026-03-14, 1:15pm | 2026-03-14, 3:40pm |
| Room | 322 (checkout) | 410 (stay-over) |
| Finder | M. Reyes | M. Reyes |
| Description | Gold hoop earring, bathroom counter | iPhone charger cable, white, nightstand |
| Photographed in place? | Yes | No (low-value, not required) |
| Value tier | High (jewelry) — two-person verification required | Low — single-attendant log sufficient |
| Storage | Locked safe, tagged bag #3B | Floor supervisor lost-and-found bin |
| Hold period | 90 days (high-value tier) | 30 days (low-value tier) |
| Release condition | Guest ID + reservation match required | Guest description match sufficient |

Two-person verification means a supervisor or second attendant witnesses the item being bagged and both initial the log — this is what protects the finder from a later theft accusation, not a formality to skip when busy.

## 5. Inspection scorecard deduction table (property QA benchmark)

| Defect category | Deduction | Notes |
|---|---|---|
| Bathroom: hair, soap scum, missing amenity | −5 pts each | Highest-weighted category; guest-facing and sensory-immediate. |
| Bed: wrinkled linens, missing pillow, stain | −5 pts each | |
| Dust/surface: visible dust on hard surfaces | −3 pts each | |
| Trash/amenity restock miss | −3 pts each | |
| Vacuum lines/visible debris on floor | −2 pts each | |
| Cosmetic (drapery not aligned, TV remote misplaced) | −1 pt each | Lowest-weighted; first category to sacrifice when genuinely out of time, never the bathroom or bed categories. |

Pass threshold: 90/100 typical for full-service brand standards; two consecutive scores below threshold on the same attendant triggers a sequence retraining session, not a written warning — the deduction pattern (which category, not just the score) tells the supervisor whether it's a speed problem or a specific skill gap.

## 6. Bed bug suspicion protocol (NPMA-aligned)

1. **First suspicion** (live insect, shed skin, or fecal spotting on mattress seams) — stop servicing that room immediately, do not strip linens further or move items to another room.
2. **Do not move the cart's linens or cloths that touched the room into other rooms** until the room is confirmed and treated — cross-room transfer is the primary spread vector.
3. **Report to supervisor with room number and location of the finding** (which side of the bed, headboard, baseboard).
4. **Room goes on maintenance hold** pending pest control inspection — do not return it to the sellable inventory based on a visual "looks fine now" check.
