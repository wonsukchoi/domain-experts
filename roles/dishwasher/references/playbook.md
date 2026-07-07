# Playbook

Filled operational sequences a dishwasher/steward actually runs — starting points to adapt to a specific kitchen's equipment and menu, not scripts to follow blind.

## 1. Pre-shift equipment verification

Run before the first dirty rack goes in. The rest of the shift's food-safety record depends on this baseline being right.

**Filled example — Friday dinner setup, high-temp machine + 3-comp sink:**

| Check | Spec | Reading | Action |
|---|---|---|---|
| Machine final rinse temp | ≥165°F (single-temp stationary rack) or ≥180°F (2-tank) | 179°F | Pass |
| Machine wash temp | ≥150°F | 156°F | Pass |
| Plate surface, heat-tape sample rack | Tape changes color at ≥160°F held 30 sec | Changed | Pass |
| 3-comp sink 1 (wash) | ≥110°F, detergent visibly sudsing | 112°F | Pass |
| 3-comp sink 2 (rinse) | Clean, no visible suds carried from sink 1 | Clear | Pass |
| 3-comp sink 3 (sanitize) — quat | 200–400ppm per test strip | 250ppm | Pass |
| Dosing pump calibration (if auto-dispensed) | Matches manual strip reading within one band | 250ppm strip vs. dispenser set 300ppm | Pass, within tolerance |

A failed reading at any row stops that path from opening for service until corrected — the machine or the sink, not both, may need to carry the full load until fixed.

## 2. Rack-loading reference

**Machine racks (16-plate standard rack):**

| Item | Position | Why |
|---|---|---|
| Dinner plates | Vertical, sorted by size before loading | Mixed sizes leave gaps that waste rack capacity and can shield lower plates from spray |
| Flatware | Perforated cylinder, handle down / utensil up | Food-contact surface (tines, bowl of spoon) faces the spray; handles blocking spray defeats sanitization on the part that touches the mouth |
| Glassware | Inverted, spaced — never nested/stacked | Nested glasses trap water and soil between them, defeating both wash and rinse |
| Bowls/cups | Inverted | Same reason as glassware |

**Sink-only items (never racked in the machine during a rush):** stockpots, sauté pans, sheet pans, hotel pans, cutting boards, anything exceeding the rack's clearance — running one of these through the machine occupies a full 16-plate slot for a single item and can also block spray arms for the rest of the load.

## 3. Rush triage — call script

**Floor bus tub backing up past holding capacity (2 tubs deep at the bus station):**
> Dishwasher to expo: "Clean plates are five out — pull the spare tens from the dry rack if the floor needs them now."
> Expo: "Heard, using spares."

**Kitchen pot rail backing up (cook reaching for a pan that isn't there):**
> Cook: "Need my 10-inch sauté back, I've got two more tickets on it."
> Dishwasher: "It's in the sink queue, two minutes — grab the spare hotel pan off the rack if you need it now."

**Routing decision announced at rush start:**
> Dishwasher to kitchen manager: "Machine's on plates and glass only tonight — pots and sheet pans go to the sink. Sink's got two people, should hold."

**Escalation (shortage will cost ticket time):**
> Dishwasher: "We're going to run short on 10-inch plates in about ten minutes if this pace holds — need a hand on the sink or we start re-plating onto whatever's clean."

Every call gets a response repeating the content back — a call that goes unanswered is treated as unheard.

## 4. Sanitizer/temperature check log — filled example, Friday dinner

| Time | Check | Reading | Spec | Action |
|---|---|---|---|---|
| 4:45pm (pre-shift) | Machine final rinse | 179°F | ≥165°F | Pass |
| 4:45pm | Sink 3, quat strip | 250ppm | 200–400ppm | Pass |
| 6:30pm | Machine final rinse | 175°F | ≥165°F | Pass |
| 7:40pm | Sink 3, quat strip | 150ppm | 200–400ppm | Fail — drained, refilled, re-dosed |
| 7:42pm | Sink 3, quat strip (recheck) | 210ppm | 200–400ppm | Pass, next load released |
| 9:00pm | Machine final rinse | 177°F | ≥165°F | Pass |
| 9:15pm | Sink 3, quat strip | 220ppm | 200–400ppm | Pass |

A failed reading stops the next load on that path until corrected and re-tested — the log documents the catch, it doesn't substitute for acting on it before the next rack runs.

## 5. Machine-down contingency

1. The instant the machine faults (no heat, error code, or a rinse-temp reading below spec that doesn't recover after one cycle) — stop routing new loads to it and switch entirely to the three-compartment sink.
2. Sink throughput runs at roughly a fifth of the machine's rated capacity — prioritize front-of-house small ware (glass, flatware, plates) since the floor cannot function without them; let pots stack in a holding soak rather than competing for sink time.
3. Notify the kitchen manager immediately with the specific fault (error code, temp reading, time observed) — not "the machine's acting up."
4. If the outage runs past 20–30 minutes, escalate to disposable service ware for the floor as a stopgap, per house policy, rather than letting the sink's slower throughput silently create a backlog that surfaces as a 9pm crisis.
5. Once the machine is restored, re-run the pre-shift verification sequence (section 1) before routing anything back through it — a repair doesn't certify itself.

## 6. Shift-end reset

1. Restock clean ware to opening par counts; shortfall or surplus noted for the kitchen manager, not silently carried into tomorrow.
2. Break down and sanitize the three-compartment sink; drain and flag the machine's chemical or rinse-water reservoirs per manufacturer schedule, not left to run stale into the next shift.
3. Log breakage (count and item) against the trailing weekly baseline — a spike gets flagged, not filed silently.
4. Any temperature or concentration excursion caught and corrected during the shift gets written into the shift log with the reading and the action taken, so the record exists independent of whether anyone asks.
