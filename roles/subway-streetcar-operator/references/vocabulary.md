# Vocabulary

Terms generalists conflate that a subway/streetcar operator keeps sharply separate, because the difference changes what was actually protected, verified, or physically at risk.

## ATP (Automatic Train Protection) vs. ATO (Automatic Train Operation) vs. ATS (Automatic Train Supervision)

**ATP** enforces the safety envelope — maximum speed, safe braking, minimum separation — and will penalty-brake a violation regardless of who or what is driving. **ATO** is the system that drives to a speed/stopping target within whatever envelope ATP allows; it can be absent (manual driving) without ATP also being absent. **ATS** is the higher-level supervision layer that manages routing and headway across the whole line, not any individual train's braking. Losing ATO just changes who's driving; losing ATP changes what's protecting.

**In use:** "ATO dropped out on this train, but ATP's still enforcing the speed envelope — I'm driving it manually, but I'll still get a penalty brake if I overspeed."

**Common misuse:** treating "automation is off" as one fact, when ATP, ATO, and ATS can each be up or down independently, and only the ATP state actually changes the safety envelope.

## Fixed block vs. moving block (CBTC)

**Fixed block** signaling divides track into discrete sections and permits only one train per section, so minimum separation is set by block length. **Moving block**, used in CBTC (communications-based train control), continuously calculates each train's actual braking distance and allows a following train to close to that dynamic distance rather than waiting for a fixed section to clear — shorter, denser headways become possible without changing physical block boundaries.

**In use:** "We're on moving-block CBTC through here, so my actual separation to the train ahead is based on its real braking curve, not a fixed section boundary."

**Common misuse:** describing any short headway as "CBTC" without distinguishing whether the line is actually running moving-block logic or a fixed-block system with unusually short blocks.

## Sensitive edge / obstruction detection vs. presence detection

**Sensitive edge** obstruction detection triggers a door reopen when it meets resistance at or above a certified force threshold — it senses resistance, not the mere presence of an object. **Presence detection** (an infrared curtain or similar, where equipped) senses that something occupies the doorway regardless of the force it exerts. A sensitive-edge-only door system can close on a soft or narrow object that never generates enough resistance to trigger reopening.

**In use:** "This door's sensitive-edge only — no presence beam — so a strap or scarf caught in it might never trip the reopen."

**Common misuse:** assuming any door "sensor" would catch anything caught in the doorway, without knowing whether the specific system is force-based, presence-based, or both.

## Berthing point vs. brake point

**Berthing point** is the exact longitudinal position where the train should come to rest at a platform (door alignment with platform doors, gap filler, or markers). **Brake point** is the location where braking begins in order to reach the berthing point at the correct speed — the two are related but distinct, and a slip/slide event or a changed adhesion condition can move where braking should start without changing where the train needs to stop.

**In use:** "The berthing point hasn't moved, but I'm starting my brake application earlier today after that slide on the last approach."

**Common misuse:** treating "the stopping mark" as one fixed thing, when the brake point is the variable that should adjust for conditions while the berthing point stays fixed.

## Headway vs. schedule adherence

**Headway** is the time interval between consecutive trains as actually experienced by passengers on the platform. **Schedule adherence** is how closely a train's individual timestamps match a printed timetable. A line can have poor schedule adherence but even headway (acceptable to riders) or good schedule adherence but bunched, uneven headway (worse for riders) — the two are not the same metric and can move in opposite directions.

**In use:** "Forget the timetable for a minute — our headway's actually even right now, that's what matters more on a line this frequent."

**Common misuse:** managing purely to the printed schedule on a high-frequency line, when riders experience headway evenness and bunching, not minute-level schedule variance.

## Bunching vs. gapping

**Bunching** is two or more trains closing to an abnormally short following interval, usually because a delayed train picks up disproportionate boarding load, which slows it further while the train behind (now facing lighter boarding) catches up. **Gapping** is the mirror problem — an abnormally long interval opens ahead of a train, and it in turn picks up extra boarding load, reinforcing the gap. Both are self-reinforcing without an active hold/run intervention.

**In use:** "We're bunching with the train ahead — I'm going to hold an extra beat at the next couple stops so the gap behind me opens back up to normal."

**Common misuse:** treating a short gap as simply "running early" rather than recognizing the self-reinforcing boarding-load feedback loop that will make it worse without an active hold.

## Restricted manual vs. manual (ATP active)

**Manual (ATP active)** means the operator drives, but automatic train protection is still enforcing the speed envelope and will penalty-brake a violation. **Restricted manual** means ATP itself is degraded or unavailable, and the operator is relying on the agency rulebook's stated reduced speed cap and direct sighting instead of automatic enforcement. The two are both "the operator is driving," but only one has an automatic backstop.

**In use:** "We're in restricted manual through the interlocking, not just manual — there's no ATP catching an overspeed here, so I'm running to the rulebook cap and sighting every signal myself."

**Common misuse:** treating any non-ATO driving as one undifferentiated "manual mode," without checking whether ATP is still actively enforcing the envelope or genuinely absent.

## Gap filler vs. platform edge

**Gap filler** is a mechanical device at specific curved-platform stations that extends to close the horizontal gap between a curved platform edge and the train floor to within accessibility standards. **Platform edge** is the fixed physical structure itself, whose uncorrected gap at a curve can exceed accessible limits without the gap filler engaged. The gap filler is a deployed state, not a permanent property of the platform.

**In use:** "Confirm the gap filler's actually out before we open on the curve side — the platform edge alone doesn't meet the gap spec here."

**Common misuse:** referring to "the gap" as a fixed fact about the station, without distinguishing whether it's describing the platform's raw geometry or the corrected gap only present when the filler has deployed.

## Dwell time vs. door-cycle time

**Dwell time** is the total time a train is stopped at a platform, from arrival to departure, driven by how long boarding actually takes. **Door-cycle time** is the mechanical duration of one open-close sequence, largely fixed by the door system regardless of ridership. Compressing dwell time under schedule pressure doesn't shorten the door-cycle time — it shortens the boarding window before the door cycle runs, which is exactly where a rushed closure risks a force event.

**In use:** "I can't make the door cycle itself any faster — if I need to save time, it has to come from cutting the boarding window, and that's the part with the door-force risk."

**Common misuse:** talking about "speeding up the doors" when what's actually being shortened is the boarding window before a fixed-duration door cycle runs.

## Third rail vs. overhead catenary

**Third rail** delivers traction power via an energized rail alongside or between the running rails, typically on heavy-rail subway systems, and is the reason detraining in a tunnel is not a simple walk-away — the rail is a live hazard at track level. **Overhead catenary** delivers power from wires above the vehicle, common on streetcar/light-rail systems, and changes the hazard profile of a trackside evacuation (no live rail underfoot, but overhead clearance and any at-grade traffic become the relevant hazards instead).

**In use:** "This is third-rail territory — nobody steps onto that trackbed until traction power's confirmed cut, that's a different call than our overhead streetcar line."

**Common misuse:** applying one system's evacuation assumptions to the other, when the power-delivery method changes exactly what's dangerous about the trackside space.
