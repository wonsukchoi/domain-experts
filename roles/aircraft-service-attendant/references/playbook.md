# Playbook

Filled sequences and tables for the recurring decisions: turnaround servicing budgets by aircraft type, the dedicated potable/lavatory equipment sequence, GSE clearance distances, and a holdover-time reference excerpt.

## Turnaround servicing checklist by aircraft type

| Aircraft type | Typical scheduled ground time | Potable water service | Lavatory (waste) service | Notes |
|---|---|---|---|---|
| Regional jet (CRJ/E-jet, ~50–90 seats) | 25–30 min | ~5 min, 1 service panel, ~40–60 gal tank | ~6–8 min, 1–2 lav units | Tight turn — servicing often the pacing task |
| Narrow-body (A320/737 family) | 35–45 min | ~8 min, 1 service panel, ~150–200 gal tank | ~10–12 min, 2–4 lav units | Standard domestic short-haul turn |
| Widebody twin-aisle (767/777/A330) | 60–90 min | ~15 min, 2 service panels, ~300–400 gal tank | ~20–25 min, 4–8 lav units | Multiple access panels often serviced by a two-person crew in parallel |
| Large widebody (747/A380) | 90–150 min | ~20–25 min, 2–3 service panels, ~450+ gal tank | ~25–35 min, 8–12+ lav units | Servicing frequently runs concurrent with cargo/catering, not sequential |

Regional-jet and widebody per-task minutes above are presented as industry-typical figures scaled from narrow-body practice, not a single cited cross-operator standard — confirm against the specific airline's ground-ops manual for the tail in question [heuristic, flagged].

## Potable water / lavatory dedicated-equipment sequence

| Step | Action | Why this order |
|---|---|---|
| 1. Arrival check | Confirm which cart is assigned to which system by color-code/label before approaching the aircraft — never by memory of "the cart I used last time" | Carts get reassigned between shifts; the label is the control, not habit |
| 2. Lavatory (waste) service first | Drain waste tank, rinse per aircraft-type procedure, replenish precharge fluid, close and verify panel | Servicing waste before potable in the same door zone limits any splash/residue reaching the potable connection point |
| 3. Coupling verification | Confirm the lav hose seats without force or an adapter; if it doesn't seat cleanly, stop and swap equipment rather than adapt the fitting | A coupling that won't seat is very often the non-interchangeable-fitting control working as intended |
| 4. Potable water service, separate cart | Connect the dedicated potable coupling, fill to aircraft-specified level, verify no cross-flow indicator or shared valve was touched during lav service | Same non-interchangeability check applies in reverse |
| 5. Panel/access closure | Close and secure all service panels, log service completion (time, tail number, tech ID) | Feeds the maintenance/dispatch record and the periodic water-quality sampling schedule |
| 6. Periodic water-quality sampling | Per the aircraft's Aircraft Drinking Water Rule sampling interval (not every turn), pull a total-coliform sample using the airline's kit | Ongoing verification the potable system remains within EPA ADWR limits, independent of any single turn's servicing |

## GSE clearance distances around an active aircraft

| Zone | Condition | Minimum clearance / rule | Note |
|---|---|---|---|
| Jet engine intake | Engine running, any power | No GSE or personnel forward of the engine within the manufacturer's published intake-suction danger zone (commonly on the order of 10–15 ft at idle, more at higher power) | Suction risk increases sharply with power setting, not linearly with visible sound |
| Jet blast (behind engine) | Engine at higher power (e.g., taxi/takeoff thrust) | Hazard zone can extend 100+ ft directly aft of the engine at high power settings | Distance scales with thrust setting, not with how far away "feels safe" |
| Propeller arc | Engine running or about to start | No GSE or personnel within the propeller's rotation arc at any time engines could start | Beacon-on is the governing signal, not visible rotation |
| Wingtip / stabilizer staging | Aircraft stationary, servicing in progress | Commonly a minimum ~10 ft (3 m) staging clearance for GSE not actively coupled to the aircraft | Applies to carts/trucks queued or repositioning, not equipment actively connected for service |
| Approach for coupling | Any engine state | Confirm anti-collision (beacon) light is off before approaching with GSE, regardless of visual read on engine rotation | Beacon on = engines running or about to start, by convention across ground-ops manuals |

## Holdover-time (HOT) reference excerpt — Type IV fluid

| Precipitation / condition | OAT range | Published holdover time (illustrative) |
|---|---|---|
| Active snow, light | −3°C to 0°C | ~35–75 min |
| Active snow, moderate | −3°C to 0°C | ~20–45 min |
| Freezing drizzle | 0°C to −5°C | ~15–30 min |
| Frost only, no active precipitation | any | Longer, often 60+ min, but confirm against current table |

These ranges are illustrative of published SAE/Transport Canada HOT table structure, not a substitute for the current-season official table, which is reissued and must be checked per fluid brand, concentration, and conditions on the day of use [heuristic — verify against current official HOT table before use]. Convention: the holdover clock starts at the beginning of the final anti-icing fluid application, not at the end of application or at pushback. Under active or moderate-to-heavy precipitation, use the lower bound of the published range, not the midpoint.
