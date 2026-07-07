# Playbook

Filled worksheets and sequences, not descriptions of them. Use these as the actual working documents on a job.

## 1. Device-spacing worksheet (smooth-ceiling baseline, then derate)

| Ceiling condition | Baseline smoke spacing (NFPA 72 Ch. 17, smooth flat ceiling) | Derate applied | Working spacing |
|---|---|---|---|
| Flat, ≤10 ft, no obstructions | 30 ft nominal (per detector listing; verify against manufacturer spacing table, which can be tighter) | none | 30 ft |
| Flat, 10–15 ft | 30 ft baseline | reduce per manufacturer's high-ceiling derate table (commonly ~10–20%) | ~24–27 ft |
| Flat, 15–20 ft | 30 ft baseline | reduce per manufacturer's high-ceiling derate table (commonly ~30–35%) | ~20–21 ft |
| Sloped/peaked (≥1 ft rise per 8 ft run) | 30 ft baseline | add a detector at the peak within 3 ft of the ridge, then apply flat-ceiling spacing from that point | site-specific, add ridge unit |
| Beam/joist depth >4 in., beam spacing >3 ft apart | 30 ft baseline | treat each beam pocket ≥1 ft deep as a partial ceiling; add detectors per pocket per NFPA 72 solid-joist/beam rules | site-specific, add per pocket |
| Within 3 ft of HVAC supply/return diffuser | 30 ft baseline | relocate device outside the 3 ft airflow disturbance zone rather than derate spacing | shift device, don't just shrink grid |

**Rule:** always cross-check the *manufacturer's listed* spacing table for the specific detector model against the NFPA 72 table — use whichever is more restrictive. The code sets a floor, not a ceiling, on conservatism.

## 2. Candela sizing worksheet (wall-mounted visual notification, NFPA 72 spacing-table logic)

| Room's largest single dimension | Minimum candela (illustrative, from NFPA 72's dimension-driven spacing table) | Common stocked rating to specify |
|---|---|---|
| 20 ft | 15 cd | 15 cd |
| 30 ft | 30 cd | 30 cd |
| 40 ft | 60 cd | 75 cd (95 cd sold out often; 75 cd covers with margin) |
| 50 ft | 95 cd | 95 cd |
| 60 ft+ or irregular/obstructed room | run manufacturer's room-specific calculation, don't extrapolate the table linearly | per calculation |

**Rule:** candela requirement scales with roughly the square of the governing room dimension, not with floor area — a 40×20 ft room (800 sq ft) sizes off the 40 ft dimension, not off an "800 sq ft" lookup. Long narrow rooms need less candela than a square room of equal area; wide-open square rooms need more.

## 3. NAC circuit load worksheet

| Step | Calculation |
|---|---|
| 1. List every notification appliance on the circuit with its rated alarm-current draw at system voltage (commonly 24V) | e.g., 9 appliances × 145 mA (60 cd horn/strobe) = 1,305 mA |
| 2. Compare to NAC circuit's rated output (check panel spec sheet, commonly 1.25A / 1,250 mA per circuit) | 1,305 mA > 1,250 mA rated → over budget |
| 3. Split appliances across two circuits to bring each under ~80% of rated output (leave headroom for future add-a-device) | 5 appliances (725 mA) + 4 appliances (580 mA) — both under 1,250 mA with margin |
| 4. Recalculate standby battery sizing: (standby current × 24 hr) + (alarm current × 5 min ÷ 60) = required Ah, per NFPA 72's 24-hour standby + 5-minute alarm minimum | e.g., 0.3A standby × 24h = 7.2Ah, plus 1.3A alarm × (5/60)h = 0.11Ah → ~7.3Ah minimum; specify next-size-up stocked battery (commonly jumps 7Ah → 12Ah → 18Ah) with margin for battery aging derate (commonly spec at 80% of rated capacity) |

## 4. AHJ acceptance-test prep checklist (run before scheduling the AHJ, not during)

1. **Record of Completion (NFPA 72 Chapter 7) complete and matches as-built** — system type, device count by type, circuit designations (pathway class per circuit), battery calculations, and installing contractor license number all filled in, not left as template placeholders.
2. **100% device functional pre-test performed and logged** — every initiating device alarmed (smoke test aerosol or heat gun as appropriate), every notification appliance verified audible/visible, every supervisory and trouble condition (open circuit, ground fault, low battery) induced and confirmed at the panel and at the monitoring station.
3. **As-built drawings reconciled against the Record of Completion** — device symbols, zone numbers, and circuit routing on the drawing match what's physically installed; common failure is a field change (moved detector, added device) that never made it back onto the drawing.
4. **Monitoring central station notified of test window** — so alarms during the AHJ walkthrough don't dispatch fire/police as a live event; confirm restoral of normal monitoring after the walkthrough closes.
5. **Egress/notification appliance audibility spot-checked in the loudest ambient-noise area of the building** (mechanical room, retail floor with music system) — NFPA 72 requires notification audible at 15 dB above average ambient or 5 dB above max ambient over 60 seconds, whichever is louder; a panel that "passes" in a quiet office can still fail in a loud retail space.
6. **Fire department connection, sprinkler flow/tamper switches, and elevator recall interfaces (if applicable) tested as part of the same walkthrough**, not deferred — AHJs frequently fail systems for an untested interface even when the core detection/notification passes cleanly.

## 5. False-alarm diagnostic sequence (existing system, repeated nuisance activations on one zone)

1. **Pull the panel's event history for the affected zone** — time-of-day pattern (every morning at a specific hour suggests HVAC startup or sun-driven thermal load; random suggests electrical/wiring); device type involved.
2. **Physically inspect the specific device** — dust/insect contamination in a photoelectric chamber, proximity to a shower/steam source for a smoke head, proximity to a kitchen or loading-dock exhaust for false thermal trips.
3. **Check wiring integrity at the device and at the nearest junction** before assuming the sensor itself is bad — a marginal ground fault or a loose splice produces intermittent false trips that read exactly like a "flaky detector."
4. **Compare against the manufacturer's sensitivity/contamination self-test log if the panel supports drift compensation reporting** — many addressable systems log sensitivity drift over time; a detector reporting near its contamination ceiling is a maintenance call (clean/replace), not a design flaw.
5. **Only after ruling out placement, contamination, and wiring, consider a device-type change** (e.g., photoelectric to a combination photoelectric/heat unit in a steam-prone bathroom, or a heat detector instead of smoke in a garage) — changing detection technology to chase a false-alarm pattern without diagnosing the cause first risks masking a real future event instead of just quieting a nuisance one.

## 6. Class A vs. Class B decision worksheet

| Factor | Favors Class B | Favors Class A |
|---|---|---|
| Occupancy | Single-tenant, low-rise, business/mercantile with sprinklers | High-rise, high-occupancy assembly, healthcare, any occupancy where continued operation past a single fault matters |
| Local code amendment | None on record specifying pathway class | Amendment mandates Class A above a stated story count or occupant load |
| Budget sensitivity | Tight rough-in budget, code allows Class B | Owner/GC has accepted the incremental four-wire cost |
| Risk of undetected single fault | Low (short runs, easy visual/periodic inspection) | High (long runs, concealed spaces, infrequent inspection access) |

**Rule:** default to whatever the local AHJ's adopted code edition and amendments require first; only apply the risk-based judgment above when the code is silent or offers a choice.
