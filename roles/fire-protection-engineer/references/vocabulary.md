# Vocabulary

Terms generalists flatten together that a fire protection engineer keeps sharply separate — the value is in the misuse, not the definition.

## Hydraulically most remote area

The design area within the sprinkler system that requires the highest supply pressure at the riser to achieve the required density — not necessarily the area farthest by distance, since elevation and pipe routing also drive friction/elevation loss.

**In use:** "We ran three candidate remote areas and the one at the far corner on the top floor governs — that's the hydraulically most remote area, not the one closest to the door."

**Common misuse:** assuming "most remote" means geometrically farthest from the riser by floor-plan distance alone, ignoring elevation and pipe-run friction.

## K-factor

A sprinkler's discharge coefficient (gpm/psi^0.5), stamped on the sprinkler, relating flow to pressure via Q=K√P — a physical property of that specific sprinkler orifice, not a design choice made independently of the sprinkler selected.

**In use:** "This is a K=8.0 head, not K=5.6 — recompute the branch flows, the discharge at the same pressure is different."

**Common misuse:** treating K-factor as interchangeable across sprinkler types or assuming a system-wide "standard" K-factor without checking the specific heads specified.

## Density/area method

NFPA 13's design methodology setting a minimum water application rate (density, gpm/ft²) over a minimum design area (ft²), with the two figures trading off along a curve for a given hazard classification — distinct from a fixed per-head flow requirement.

**In use:** "At this hazard classification we can trade a higher density for a smaller design area, or vice versa — pull the actual curve point, don't just use the table extremes."

**Common misuse:** treating density and area as independently fixed numbers rather than reading the actual curve for the combination the design will use.

## Residual pressure vs. static pressure

**Static pressure** is the pressure in a water system with no flow occurring. **Residual pressure** is the pressure remaining at a point while water is flowing (elsewhere, during a flow test, or under design demand) — always lower than static, and the figure that matters for whether a system can actually deliver water under fire conditions.

**In use:** "Static is 72 psi, but residual at our demand flow only holds at 68 — design against the residual number, not the static one."

**Common misuse:** citing static pressure as if it represents available fire-flow capacity, when only residual pressure under load reflects real system performance.

## Hose stream allowance

An additional flow (gpm) added to the sprinkler system's water supply demand — but not routed through the sprinkler pipe network itself — to account for manual hose streams used alongside automatic suppression; added at the point of connection to the water supply per NFPA 13's table for the hazard classification.

**In use:** "Add the 250 gpm hose stream allowance at the PIV, not into the sprinkler branch calc — it's a supply-side addition, not a pipe-network flow."

**Common misuse:** adding the hose stream allowance into the internal pipe network hydraulic calc instead of only at the water-supply connection point.

## Standpipe Class I / II / III

**Class I** standpipes serve fire department 2½" hose connections only, minimum 100 psi residual at the topmost outlet. **Class II** serve 1½" hose stations for trained occupant/first-aid use. **Class III** combine both — full fire department connections plus occupant hose stations on the same system.

**In use:** "This is a Class I standpipe for fire department use only — don't spec 1½" occupant hose stations on it, that's a Class II or III scope."

**Common misuse:** treating standpipe class as a size designation rather than an intended-user and connection-type designation with distinct minimum pressure requirements.

## Elevation head

The pressure change attributable purely to height difference in a water system — 0.433 psi per foot of elevation, added going up and subtracted going down — computed separately from friction loss, which depends on flow and pipe characteristics, not height.

**In use:** "The riser climbs 45 ft — that's 19.5 psi of elevation head on top of whatever the friction loss comes out to."

**Common misuse:** folding elevation change into a generic "safety margin" instead of computing it explicitly per foot of actual height difference.

## Hazen-Williams C-factor

An empirical pipe roughness coefficient used in the Hazen-Williams friction loss formula — higher C means smoother pipe and lower friction loss for the same flow. Varies by material and is fixed by NFPA 13 for design purposes regardless of a specific pipe's actual measured roughness.

**In use:** "It's CPVC, so C=150 in the calc, not the 120 we'd use for black steel — that changes every friction loss number in the branch."

**Common misuse:** using a single C-factor across all pipe materials in a system instead of the material-specific value NFPA 13 specifies.

## Occupant load factor

A code-assigned area-per-person figure (ft²/occupant) used to compute the design occupant load of a space from its floor area — varies by occupancy type and by whether the area is gross or net floor area, and is not the same as an actual observed headcount.

**In use:** "Storage areas use 300 ft²/occupant, not the 30 ft²/occupant sales-floor factor — recompute the occupant load for that back-of-house zone separately."

**Common misuse:** applying one occupancy's load factor across an entire mixed-use floor plate instead of computing occupant load zone by zone against each area's actual use.

## Egress capacity factor

A code-assigned inches-of-width-per-occupant figure used to compute the minimum required egress width for a stair or level component — lower (more permissive) when the building is sprinklered and alarmed, because the suppression/detection system earns a code credit.

**In use:** "We can use the 0.2 in/occupant sprinklered factor on the stairs here, since the system covering this area is fully monitored and in service."

**Common misuse:** applying the sprinklered credit without confirming the specific area is actually covered by an in-service, code-compliant system for the condition being evaluated.

## Common path of travel vs. dead-end corridor

**Common path of travel** is the distance an occupant must travel before reaching a point where two separate paths to two different exits become available. A **dead-end corridor** is a corridor segment beyond which there is no exit access at all — travel down it dead-ends. Both are limited by code, but they measure different things and can both apply to the same layout independently.

**In use:** "The common path is fine at 60 ft, but check the dead-end separately — that back hallway doesn't connect to anything."

**Common misuse:** treating a passing common-path-of-travel check as if it also clears the dead-end-corridor limit, when the two are independent measurements against independent limits.

## Positive alarm sequence

An NFPA 72-permitted delay sequence where a single detector activation triggers an alarm response period followed by an investigation period before general occupant notification and full alarm — intended to reduce nuisance evacuations, with a strict total-time cap.

**In use:** "Positive alarm sequence is configured, but check the total delay against the cap — response plus investigation can't exceed what the code allows before general alarm."

**Common misuse:** configuring the response and investigation periods without checking that their sum stays within the code's total permitted delay.

## Notification appliance candela

The light intensity rating (candela) of a visual notification appliance (strobe), which the code ties to maximum room dimension via a spacing table — a higher-candela unit is required as room size increases, not a fixed rating usable in any room.

**In use:** "That's a 15 cd unit in a room that needs 30 cd per the spacing table for its dimensions — undersized."

**Common misuse:** specifying a single candela rating across an entire project regardless of individual room dimensions.

## Smoke compartment

A subdivision of a building enclosed by smoke barriers (rated for smoke resistance, not necessarily full fire resistance) intended to contain smoke movement and provide a refuge/relocation area — distinct from a fire compartment, which is bounded by fire-rated construction and sized to contain fire spread.

**In use:** "That's a smoke barrier, not a fire wall — it stops smoke migration for horizontal relocation, but don't count on it for the fire-resistance rating the egress plan needs elsewhere."

**Common misuse:** treating "smoke compartment" and "fire-rated compartment" as interchangeable, when their construction requirements and design purposes differ.

## Churn (shutoff) pressure

A fire pump's discharge pressure at zero flow — the maximum pressure the pump produces, used to check that downstream piping and devices aren't overpressured when the system is static and the pump is running against a closed system.

**In use:** "Churn pressure on this pump is 165 psi — check the sprinkler piping's rated working pressure before we commit to this pump, we may need a pressure-reducing valve downstream."

**Common misuse:** sizing a pump only against its rated-flow performance point and never checking the churn pressure against downstream piping's pressure rating.

## Water supply curve vs. demand point

The **water supply curve** plots available pressure against flow across a range (derived from flow test data). The **demand point** is the single flow/pressure pair the fire protection system actually requires. A system is adequate only if the demand point falls under the supply curve at that same flow — a single-number pressure comparison at the wrong flow can mislead.

**In use:** "Don't just compare our required 43 psi to their static 72 psi — plot the demand point against the actual supply curve at our design flow."

**Common misuse:** comparing required pressure to the water system's static pressure instead of to the available pressure at the actual demand flow.
