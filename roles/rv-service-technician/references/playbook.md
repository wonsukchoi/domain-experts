# Playbook

Filled walkthroughs for the four places this trade gets shortcut: LP-gas leak testing, roof-seal/moisture diagnosis, slide-out alignment, and winterization. Numbers are worked examples to adapt, not universal constants — always check the unit's own appliance connector spec, membrane manufacturer, and converter/battery documentation.

## 1. LP-gas manometer lock-up test

**Step 0 — pressure reference points (propane, typical RV system):**

| Test point | Target pressure | Notes |
|---|---|---|
| Regulator outlet / appliance manifold | 11 in. W.C. | Standard operating pressure for propane appliances on most RV systems (natural-gas installs run 10 in. W.C. — confirm before testing) |
| Cylinder-to-regulator (high side) | Per regulator/cylinder spec, not tested with a low-pressure manometer | Requires a 0–30 psi test gauge; not part of the routine appliance-side lock-up test |

**Lock-up test sequence:**

1. Turn off all appliance pilots and shut every appliance valve.
2. Connect the manometer at the test port nearest the regulator outlet (many ranges have a quick-connect test point; otherwise tee into the line ahead of the first appliance).
3. Open the supply valve, pressurize to **11 in. W.C.**, then close the supply valve to isolate the manometer and downstream piping from the source.
4. Start a 3-minute timer. **Any drop in reading over the 3 minutes is a fail** — a listed regulator and leak-free downstream piping hold pressure with no measurable loss.
5. On a fail, leave the system pressurized and soap-test every accessible connection (flare fittings, appliance connectors, shutoff valves) — bubbling identifies the leak point without depressurizing and losing the fault.
6. Repair the identified connection (re-torque to the fitting's spec, replace a damaged flare or gasket), then repeat steps 3–4. Only a full 3-minute hold with no drop clears the system for service.

**Common failure points, in descending frequency:** loose flare fittings behind appliances (vibration-loosened, not originally under-torqued), cracked or perished appliance connector hose, a shutoff valve that doesn't fully seat, and a regulator that has lost its lock-up capability with age (replace, don't re-test indefinitely).

## 2. Roof membrane and moisture diagnosis

**Membrane type and expected service characteristics:**

| Membrane | Typical service life | Recoat/inspect interval | Notes |
|---|---|---|---|
| EPDM (rubber) | ~10–15 years | Inspect every 6 months; recoat self-leveling lap sealant at penetrations roughly every 1–2 years | UV and ozone degrade the rubber and the lap sealant faster than the membrane itself fails outright |
| TPO | ~12–20 years | Inspect every 6 months; sealant recoat interval similar, but TPO tolerates UV better | Requires TPO-compatible sealant — EPDM lap sealant does not bond correctly to TPO |

**Moisture-meter reading thresholds (RV wood-substrate reference scale, pin or non-invasive):**

| Reading | Interpretation |
|---|---|
| < 15% | Normal ambient moisture — no action |
| 15–20% | Elevated — monitor, retest at next service interval, inspect nearest seal |
| > 20% | Active or recent intrusion — investigate source, do not just cosmetically repair |

**Diagnostic sequence:**

1. Visual sweep of every roof penetration (vents, AC shroud, antenna, edge trim) for cracked, chalking, or missing sealant — this is where nearly all roof leaks originate, not the flat field of the membrane.
2. Take a moisture-meter reading at the interior ceiling/wall seam below each suspect penetration.
3. Take a baseline reading at an unaffected location (a corner with no nearby penetration) for comparison — a single reading without a baseline can't distinguish elevated from normal for that unit's materials.
4. Probe (gently, non-destructively) any floor or wall area below a >20% reading for softness before scoping the repair — decking involvement changes the job from a sealant-and-panel repair to a structural one.
5. Reseal the source penetration regardless of whether interior damage is found — a dry substrate today with a cracked seal is next season's >20% reading.

**Cost-escalation pattern [stated heuristic, not a quoted industry figure]:** a caught-early reseal plus a contained interior panel repair runs in the low hundreds of dollars; the same leak left through one or more additional seasons commonly progresses to sidewall delamination or floor decking replacement, which is priced in the thousands. The exact dollar gap varies by unit and region — the pattern to act on is the timing, not a specific number.

## 3. Slide-out alignment

**Diagnostic sequence — run before adjusting any cable, gearmotor, or roller:**

1. With the slide fully extended, measure the gap between the slide box and the opening frame at the top and at the bottom (and side-to-side if the mechanism is a cable/rack system on both edges).
2. Compare the difference between top and bottom (or side to side) against the manufacturer's tolerance — commonly **⅛–³⁄₁₆ in. (0.125–0.1875 in.)**; a difference beyond that is racking, not normal mechanical slop.
3. If racking is present, check tire pressure at every position against the placard spec before touching the slide mechanism — an imbalance of 15–20+ psi axle-to-axle or side-to-side is enough to twist the frame and rack a slide opening.
4. Check the leveling setup (jacks or blocks) for the same reason — an unlevel park produces the identical symptom to a tire-pressure imbalance.
5. If tire pressure and level are both within spec and racking persists, check the floor structure near the slide opening with a moisture meter — a water-softened floor section can rack a slide opening the same way an underinflated tire does.
6. Only after structural causes are ruled out or corrected does a persistent bind or gap point at the mechanism itself (cable tension, worn rollers, misaligned gearmotor) — adjust or replace at that point, and remeasure against the same tolerance to confirm the fix held.

## 4. 12V/120V converter and inverter diagnostic reference

**Multi-stage converter/charger voltage profile (lead-acid, typical):**

| Stage | Voltage (DC) | Purpose |
|---|---|---|
| Bulk | 14.4–14.8V | Fast charge to ~80% capacity |
| Absorption | 14.2–14.4V | Tapering current to top off remaining capacity |
| Float | 13.2–13.6V | Maintenance charge, indefinite hold |

**Lithium (LiFePO4) profile differs materially:** bulk/absorption commonly around 14.2–14.6V with no equalization stage, and float is often unnecessary or set lower (~13.6V) since LiFePO4 doesn't require a maintenance float the way lead-acid does. **Feeding a LiFePO4 bank a lead-acid equalization cycle is a battery-damage condition, not a charging variation** — confirm the charger's profile setting matches the installed chemistry before troubleshooting anything else on the DC side.

**Diagnostic sequence for a "batteries won't hold charge" or "dim lights" complaint:**

1. Identify battery chemistry and charger model/profile setting first — this determines what "correct" voltage even means for this unit.
2. Measure battery voltage under a real load (lights and a fan running), not open-circuit — open-circuit voltage recovers quickly and masks a weak battery or an undersized charger.
3. If voltage sits below ~13.2V (lead-acid) at idle-ish load with the charger connected and shore/generator power confirmed present, the fault is upstream of the battery (charger stage stuck, wiring/fuse loss) — check the charger output directly, not just at the battery terminal.
4. Separately verify AC-side power quality (shore polarity, generator output voltage/frequency) is actually reaching the converter — a converter with no correct AC input reads as a "dead battery" symptom.
5. Only after the DC-side chain (source → converter → battery → load) is confirmed correct does an inverter or transfer-switch fault become the next hypothesis for an AC-symptom complaint on battery power.

## 5. Winterization sequence

1. Drain the fresh water tank and all low-point drains; confirm flow has actually stopped at each drain, not just "opened the valve."
2. Bypass the water heater (turn the bypass kit valves) and fully drain the tank via its drain plug — skip this and antifreeze either doesn't protect the tank or is wasted filling a tank being drained anyway.
3. Open all faucets (hot and cold, including any outdoor shower or exterior kitchen) and flush the toilet until air, not water, comes through, confirming the system is blown down before adding antifreeze.
4. Connect a hand pump or 12V transfer pump to a jug of RV-rated (non-toxic propylene glycol) antifreeze at the fresh-water pump inlet, or use the pump's built-in winterizing valve if equipped.
5. Run antifreeze through each fixture (hot and cold sides separately) until pink discharge is consistent, typically **2–3 gallons for a single-axle travel trailer**, more for larger units with more fixture runs — confirm every fixture individually, including any washer hookup or ice-maker line.
6. Pour a cup of antifreeze down each drain (sinks, shower, tub) to protect the P-traps, and add antifreeze per the manufacturer's spec to the black and gray tanks if not treated by the flush above.
7. Document gallons used and confirm bypass valve position on the work order — the next tech (or the same one in spring) needs the record to know the system was actually protected, not just that antifreeze was purchased.
