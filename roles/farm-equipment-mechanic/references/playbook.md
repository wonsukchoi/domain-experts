# Playbook

Filled procedures and reference tables — run these directly, don't treat them as descriptions of what to do.

## 1. ECU fault-code diagnostic sequence

**Never skip step 2 to go straight to step 4.** Parts availability during harvest makes step 4 the slowest and least reversible step in the sequence.

1. **Read the active code and its SPN/FMI (or proprietary DTC).** Note whether it's active or stored/intermittent — an intermittent code that hasn't recurred in the current session changes the diagnostic priority (wiring/connection over component).
2. **Pull freeze-frame or live data for the parameter in question.** Compare the signal's behavior against a known-good pattern: pegged at a rail voltage (0V or 5V) usually means a short/open in the harness or connector, not component drift; a signal that tracks but reads consistently offset usually means a genuinely degraded sensor or a calibration issue.
3. **Confirm at the connector with a multimeter** (resistance, voltage, continuity as appropriate) before ordering any part. Check known wear/chafe points on the harness run for that circuit (pivot points, articulation joints, routing near heat sources) first.
4. **Only after steps 1–3 confirm the component itself, order the part.** If the fix requires OEM calibration or reflash after the part is installed, confirm dealer software access and lead time *before* removing the old part — not after the machine is already apart.
5. **Verify the fix under the same operating condition that triggered the original fault** (implement engaged, system under working load, PTO running) — a bench-clear code is not a confirmed repair.

**Common SPN/FMI patterns worth recognizing (illustrative, verify against the specific ECU's fault-code list):**

| Pattern | FMI meaning | Typical root cause |
|---|---|---|
| Signal pegged at 5V (rail-high) | 3 — voltage above normal | Short to reference/power in harness; less often a failed sensor |
| Signal pegged at 0V (rail-low) | 4 — voltage below normal | Open circuit or short to ground in harness/connector |
| Signal erratic/noisy, no clear rail | 2 — data erratic/intermittent | Loose or corroded connector, chafed wire making intermittent contact |
| Value out of expected range but stable | 0 or 1 — above/below normal operating range | Genuinely degraded or miscalibrated sensor, or a real mechanical fault upstream (e.g., a real low-pressure condition, not a sensor problem) |

## 2. Hydraulic pressure-test targets by system type

Always verify against the specific machine's OEM service manual — these are typical ranges for triage, not universal constants.

| System | What to test | Typical target range | Notes |
|---|---|---|---|
| Open-center remote/implement circuit (tractor, planter lift) | Main relief pressure | 2,600–3,300 psi | Set at the relief valve; low reading with good pump flow points to the relief valve itself or an internal leak downstream |
| Closed-center / load-sensing system | Standby (system) pressure | 2,900–3,300 psi | Standby pressure below spec with engine at rated rpm points to the pump's load-sensing/compensator control, not the implement |
| Hydrostatic propel/feeder-house drive (combine) | Charge pressure | 300–450 psi | Low charge pressure starves the main hydrostatic loop and shows up as sluggish or no propel/feeder-house response before any main-loop symptom appears |
| Any hydrostatic or gear-reduction drive | Case-drain flow/temperature | Flow within OEM spec; temperature climbing well above ambient+150°F under load | Rising case-drain temperature under sustained load is an early signature of internal pump or motor wear before an output symptom shows up |

**Isolation order:** test charge/standby pressure first (the supply side) before condemning a cylinder, motor, or valve on the demand side — a starved supply makes every downstream component look weak even when none of them are faulty.

## 3. PTO speed and torque reference

| Rating | Spline count | Typical engine/PTO rpm relationship | Shear-pin/slip-clutch torque |
|---|---|---|---|
| 540 rpm | 6-spline | Standard PTO output speed at rated engine rpm | Sized to the specific implement — verify against implement's OEM spec, not the tractor's |
| 540E (economy) | 6-spline | Same 540 output achieved at reduced engine rpm for fuel economy | Same torque rating as standard 540; the difference is engine rpm, not shaft speed |
| 1000 rpm | 20 or 21-spline | Standard PTO output speed at rated engine rpm | Higher-torque-capacity implements (large rotary cutters, big square balers) |

**Checklist:**

1. Confirm the implement's rated PTO speed against the tractor's selected PTO output *before* connecting — a 540-rated implement run at 1000 rpm overspeeds it; a 1000-rated implement run at 540 starves it of the power the design assumes.
2. Measure actual output speed with a handheld tachometer at the shaft, not just the dash indicator — a slipping clutch pack inside the tractor's PTO engagement can show correct dash selection with reduced actual output speed.
3. Inspect spline wear (visible rounding, play when engaged) and shear-pin/slip-clutch condition against the implement's torque spec — a shear pin substituted with the wrong-grade bolt defeats the entire protection design.
4. Check driveline guard condition (shield, shaft tunnel) at the same time — a PTO fault diagnosis is also the routine point to catch a missing or degraded shield before it becomes a safety incident.

## 4. Pre-season inspection checklist and cost comparison

**Checklist (run 4–6 weeks before the season's first field day):**

- Hydraulic system: main relief/standby pressure test, case-drain flow/temperature check, hose and fitting inspection for chafing or weeping.
- Electrical/CAN: harness inspection at known wear points (pivots, articulation joints), battery/charging system load test, ISOBUS termination resistor check.
- PTO/driveline: spline wear inspection, shear-pin/slip-clutch torque verification, shield/guard condition.
- ECU: pull stored (non-active) fault codes — a code that cleared itself but is stored often marks the same wear point that will fail mid-season.
- Precision-ag: row-unit sensor and connector inspection, auto-steer receiver mount and ground-strap check, display firmware version against current release.

**Cost comparison (illustrative, scale to the specific fleet):**

| | Pre-season inspection | In-season failure (harvest window) |
|---|---|---|
| Direct cost | 4–6 hours shop labor + minor parts (~$400–$800 typical) | Same repair cost, plus downtime |
| Downtime cost | None — off-season | Field-capacity-dependent; see SKILL.md worked example (single-incident exposure of $10,000+ is common on a mid-size operation during a weather-constrained window) |
| Decision | Run it unless the operation can show genuine schedule slack to absorb an in-season breakdown | — |

## 5. Right-to-repair tool-access decision table

| Repair type | Access needed | Typical cost/lead time | Route |
|---|---|---|---|
| Mechanical/hydraulic repair, no calibration required (harness splice, hose, cylinder seal, PTO clutch) | None — hand tools and test equipment | Same-day | Shop or mobile service, independent-capable |
| Code reading, live data, basic diagnostics | Aftermarket multi-brand tool (e.g., Jaltest AG, Diesel Laptops) | Tool cost is a fixed shop investment (subscription/license, typically renewed annually), no per-repair lead time | Independent-capable once the tool is owned |
| Component replacement requiring OEM calibration (injector coding, some sensor replacements) | OEM software (Service ADVISOR / EST / EDT) or dealer | Dealer appointment lead time — routinely multi-day during planting/harvest season | Confirm before teardown; may require dealer even for an otherwise simple swap |
| ECU reflash, security-locked parameter change, some precision-ag pairing/activation | OEM software, often dealer-only regardless of tool ownership | Dealer-only; lead time same as above | Route to dealer at intake, not after diagnosis |

Confirm which row a repair falls into during intake triage (SKILL.md decision framework, step 4) — discovering a dealer-only lockout after the machine is torn down converts a same-day fix into a multi-day one with the machine already down.
