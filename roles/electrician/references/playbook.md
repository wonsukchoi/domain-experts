# Playbook — load calculation, ampacity/voltage-drop check, and troubleshooting sequence

Filled processes, not descriptions. Use the load-calc worksheet for any new circuit, subpanel, or service-capacity question; use the troubleshooting sequence for any dead-circuit or tripping-breaker callback.

## 1. NEC standard-method dwelling load calculation (Art. 220 Parts III–IV)

Worksheet, filled for a 2,200 ft² dwelling with one range, one dryer, a heat pump, and a new EV charger circuit (same job as the SKILL.md worked example):

| Step | Item | Formula / source | Value |
|---|---|---|---|
| 1 | General lighting | 3 VA/ft² × 2,200 ft² | 6,600 VA |
| 2 | Small-appliance circuits (min. 2) | 1,500 VA × 2 | 3,000 VA |
| 3 | Laundry circuit | 1,500 VA × 1 | 1,500 VA |
| 4 | Subtotal general load | sum of 1–3 | 11,100 VA |
| 5 | Demand factor (Table 220.42) | first 3,000 VA @ 100%, remainder @ 35% | 3,000 + (8,100 × 0.35) = **5,835 VA** |
| 6 | Fixed appliances (dishwasher, disposal, built-in microwave) | full nameplate — 220.53's 75% factor needs 4+ units, this job has 3 | **3,600 VA** |
| 7 | Range (12 kW, one unit) | Table 220.55 Column C | **8,000 VA** |
| 8 | Dryer (5 kW nameplate, one unit) | Table 220.54, 100% for 1 unit | **5,000 VA** |
| 9 | HVAC (heat pump, non-coincident 220.60) | larger of compressor (4,200 VA) or strip heat (10,000 VA) | **10,000 VA** |
| 10 | EV charger (50A breaker, continuous load, Art. 625) | 50A × 0.8 × 240V | **9,600 VA** |
| 11 | **Total demand** | sum of 5–10 | **42,035 VA** |
| 12 | **Service amps** | 42,035 ÷ 240V | **175.1 A** |

**Decision rule:** if total service amps (step 12) exceeds the existing main breaker rating, the service must be upgraded before new circuits are energized — do not stage the new circuits "for now" and revisit later; a load calc that already exceeds the main on paper doesn't get safer by being ignored. Target the next standard size (100/125/150/200/400A) that clears calculated demand by ≥10–15% headroom for one future addition.

**Optional method (220.82)** applies only to an *existing* dwelling with an existing service, not new construction, and skips the appliance-by-appliance demand factors: general loads (lighting + small appliance + laundry + all appliances at nameplate, excluding HVAC) get 100% of the first 10,000 VA and 40% of the remainder, then HVAC is added at 100% of the largest of four listed categories (heating vs. cooling, whichever governs). Use it as a faster second check on a remodel job; if it produces a lower number than the standard method, the standard method still governs unless the AHJ has explicitly accepted the optional method for that permit.

## 2. Ampacity and voltage-drop check for a new run

Sequence, applied to a 60A feeder run to a detached addition subpanel, 80 ft one-way, copper THWN-2 in PVC conduit:

1. **Count current-carrying conductors (CCC).** Two hots + one neutral carrying unbalanced return current = 3 CCC. Equipment ground doesn't count. 3 CCC is below the 4-conductor threshold in Table 310.15(C)(1) — no conduit-fill derating applies.
2. **Pick the ampacity column by termination rating**, not conductor insulation rating: OCPD and lugs on a 60A/100A-class breaker are typically 75°C-rated for this size — use the 75°C column of Table 310.16. 6 AWG copper = 65A at 75°C, which clears the 60A OCPD.
3. **Check ambient temperature.** If the run passes through an attic or other space regularly above 86°F (30°C), apply the Table 310.15(B)(1) correction factor to the 65A rating before confirming it still clears 60A; skip this step only for runs entirely in conditioned space or buried underground at normal soil temperature.
4. **Compute voltage drop.** VD = (2 × K × I × D) ⁄ CM, single-phase, K = 12.9 (copper). At estimated 48A (80% of the 60A OCPD, treating it as a continuous-capable load): VD = (2 × 12.9 × 48 × 80) ⁄ 26,240 = 3.78V = **1.57%** of 240V.
5. **Compare against the 3%/5% guideline** (branch/total, informational, not code-mandatory in most jurisdictions unless locally amended): 1.57% is well clear — no upsizing. If the same run were 150 ft instead of 80 ft, VD scales linearly to ~2.95% — flag it as borderline and consider one size up (4 AWG) even though it's not a code violation, because "passes today" and "passes with margin" are different recommendations to a client.

## 3. Half-split troubleshooting sequence — tripping breaker or dead circuit callback

Applied to: a 20A kitchen small-appliance circuit that trips within 2–3 seconds of the breaker being reset, with no obvious burned device.

1. **Classify the trip type before touching anything.** Instant trip on close, before any load is drawing (or even with all loads unplugged) = magnetic trip = short or ground fault in the wiring itself, a device, or the breaker. A trip after the circuit has carried load for minutes = thermal trip = overload, a different repair entirely (load reduction or a dedicated circuit, not a wiring fault hunt).
2. **De-energize and verify dead** — lock out/tag out the breaker, then test-known-live-test the meter (test on a known live source, test the target circuit, retest the known live source) before opening any device or splice. Never proceed on the assumption "that's the right breaker" from memory.
3. **Disconnect all loads/devices from the circuit** and reset the breaker with nothing connected. If it holds, the fault is in a downstream device (add loads back one at a time until it trips again — that device or its wiring segment is the fault). If it trips with everything disconnected, the fault is in the wiring or a fixture hard-wired to the circuit itself.
4. **Half-split the run.** Identify the electrical midpoint of the circuit (usually the most accessible junction box roughly halfway between the panel and the last device) and open it. Megohmmeter or continuity-test hot-to-neutral, hot-to-ground, and neutral-to-ground on each half separately with the panel breaker off and both ends isolated.
5. **Read the result and recurse.** A near-zero-ohm reading on one half narrows the fault to that half; repeat the midpoint split within that half until the fault is isolated to a single device, splice, or staple-through-cable point (a common cause: a fastener driven through a cable during finish work, shorting hot to ground or neutral).
6. **Repair and re-verify in stages** — fix the isolated fault, reconnect one section at a time, and reset the breaker after each addition rather than reconnecting the whole circuit at once; this catches a second, coincidental fault instead of assuming one fault explains everything.
7. **Document the root cause and the fix** on the service ticket, including which half-split step isolated it — this is what turns a one-off repair into a pattern the next callback (on a different circuit, same house) can be checked against.

## 4. Quick-reference ampacity table (copper, common residential/light-commercial sizes)

| AWG | 60°C column | 75°C column | Typical use |
|---|---|---|---|
| 14 | 15A | 15A | Lighting circuits (15A breaker) |
| 12 | 20A | 20A | General receptacle/small-appliance circuits (20A breaker) |
| 10 | 30A | 30A | Water heaters, small dedicated 240V loads |
| 8 | 40A | 50A | Dryers, cooktops, subpanel feeders ≤40A |
| 6 | 55A | 65A | Ranges, subpanel feeders 50–60A, EV chargers ≤50A |
| 4 | 70A | 85A | Larger subpanel feeders, 70–80A loads |
| 2 | 95A | 115A | 100A subpanel feeders |
| 1/0 | 125A | 150A | 150A service/feeder conductors |
| 2/0 | 145A | 175A | 175–200A feeder conductors |

**Column selection rule:** use the 60°C column unless every termination in the circuit (breaker, lugs, device) is listed for 75°C — most panel and breaker hardware ≤100A is 60°C-rated unless the equipment label states otherwise. This table assumes no more than 3 current-carrying conductors in the raceway and an ambient temperature ≤86°F (30°C); apply Table 310.15(C)(1) fill derating at 4+ CCC and Table 310.15(B)(1) correction above that ambient before finalizing a size.
