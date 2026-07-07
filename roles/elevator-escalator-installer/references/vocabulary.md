# Vocabulary

Terms generalists conflate or use loosely that a licensed mechanic keeps sharply separate, because the code and the maintenance record depend on the distinction.

### Rated speed vs. contract speed vs. governor tripping speed

**Rated speed** is the nameplate/code reference speed the unit is certified to operate at. **Contract speed** is the speed specified in the original purchase/installation contract, which is usually but not always identical to rated speed. **Governor tripping speed** is the actual measured speed at which the overspeed governor releases the car/counterweight safety — a separate, empirically-read number that must fall inside a code-specified percentage band above rated speed.

**In use:** "Contract speed was 350 fpm, that's also what's on the nameplate as rated speed — but the governor actually tripped at 372, so we report the trip as a percentage of rated, not contract."

**Common misuse:** treating "rated speed" and "governor tripping speed" as the same number, or reporting a governor test as pass/fail without stating the actual measured trip speed the pass/fail was computed from.

### Interlock vs. restrictor

**Interlock** is the electrical device verifying a hoistway or car door is fully closed and locked before permitting car movement. **Restrictor** is the mechanical device limiting how far a door can be manually forced open when the car is stopped outside the unlocking zone at a landing. They protect against different failure sequences — the interlock is the primary safeguard against moving with a door open; the restrictor is the backup for when someone (or something) has already defeated or is trying to defeat the interlock.

**In use:** "The interlock circuit tests fine, but the restrictor let the door open past spec — that's still a fail, and it's the more dangerous one because it's the backup device."

**Common misuse:** treating a passing interlock test as verification that the door circuit is safe overall, without separately testing the restrictor.

### Category 1 vs. Category 5 periodic test

**Category 1** is the annual, no-load functional test of the safety circuit and its components. **Category 5** is the 5-year, full-load mechanical test that physically loads the car (and counterweight) and runs the safety and buffer under that load. A no-load pass does not substitute for a full-load pass; they test different failure conditions.

**In use:** "The Category 1 is current, but the Category 5 full-load counterweight test is what's actually due this cycle — don't file this visit as complete until that's run."

**Common misuse:** assuming a recently passed Category 1 means the unit is generally "up to date" on testing, when the Category 5 clock runs independently and covers conditions Category 1 never tests.

### QEI vs. AHJ

**QEI (Qualified Elevator Inspector)** is an individual certified (commonly through NAESA International or an equivalent body) to witness and sign off periodic tests and inspections. **AHJ (Authority Having Jurisdiction)** is the government body (state, city, or provincial elevator safety office) that adopts a code edition and enforces compliance — the QEI works within rules the AHJ sets, and can be employed by the AHJ, a third-party inspection firm, or in some jurisdictions the maintenance contractor.

**In use:** "The QEI witnessed the buffer strike test, but it's the AHJ's adopted code edition that determines what percentage load the buffer test actually requires."

**Common misuse:** treating "QEI-approved" as equivalent to "code-compliant" without checking which code edition the AHJ has adopted at that address — a QEI applies the rules that are in force, and those rules differ by jurisdiction and adoption date.

### Type A vs. Type B safety

**Type A (instantaneous)** safety devices stop the car abruptly once engaged, generally used only at lower rated speeds because the deceleration at higher speed would exceed safe limits. **Type B (progressive)** safety devices apply a controlled, ramping braking force, used at higher rated speeds specifically to keep deceleration within the code's retardation limits.

**In use:** "This is a Type B progressive safety — expect a controlled ramp-down on the strike test, not a hard stop, and check the retardation curve, not just whether it stopped."

**Common misuse:** assuming any car safety is instantaneous-type, and diagnosing a "soft" progressive-safety stop as a partial failure when a ramping deceleration is the correct behavior for that device type.

### Traction vs. positive drive

**Traction** elevators move the car by friction between hoist ropes and a drive sheave grooved to grip the rope — traction loss (rope slip at the sheave) is a real failure mode distinct from a governor or safety-circuit fault. **Positive drive** systems (e.g., screw or hydraulic-plunger types) move the car by direct mechanical or fluid coupling with no slip possible in the same sense.

**In use:** "Independent tach and controller display disagree — check for traction loss at the sheave before assuming it's an encoder fault, since this is a traction unit."

**Common misuse:** applying traction-specific diagnostic logic (checking for rope slip) to a positive-drive or hydraulic unit where that failure mode doesn't apply, or vice versa.

### Buffer (spring) vs. buffer (oil)

**Spring buffers** absorb impact through mechanical compression and are typically used on lower-speed cars; they release stored energy back into the car unless designed to dissipate it, so retardation characteristics differ from oil buffers. **Oil buffers** dissipate impact energy hydraulically and are required at higher rated speeds because they can deliver a more controlled, non-rebounding retardation curve across a wider speed range.

**In use:** "At 350 fpm we're within spring buffer territory for this class, but the modernization spec bumped rated speed high enough that the buffer needs to go to oil — the spring buffer's stroke and rebound characteristics don't cover the new speed."

**Common misuse:** treating "the buffer test passed" as buffer-type-agnostic, when the correct type for a given rated speed is itself a threshold to check before the strike test even runs.

### Releveling vs. anticreep

**Releveling** is the controller automatically correcting car position after it has settled off-floor (from rope stretch, load change, or hydraulic oil compression) while doors may be open. **Anticreep** is a specific hydraulic-elevator control function preventing gradual downward drift while stopped and loaded, functioning even without triggering a full relevel cycle. They address related but distinct symptoms and are diagnosed differently.

**In use:** "It's not releveling too often — it's failing to anticreep between releveling events, which points at the hydraulic valve, not the door-zone sensor."

**Common misuse:** using "releveling" to describe any position drift, which misdirects troubleshooting toward the door-zone/leveling sensor when the actual fault is the anticreep function or the hydraulic system itself.

### Firefighters' Service Phase I vs. Phase II

**Phase I** is building-lobby-level recall of elevators to a designated floor upon fire alarm activation, overriding normal hall calls. **Phase II** is in-car firefighter control, engaged once the car has recalled, allowing manual operation by fire personnel with normal safety interlocks modified for that purpose. They are sequential, not interchangeable states, and each has its own functional test requirement.

**In use:** "Phase I recall tested clean, but Phase II in-car operation needs its own separate functional test — passing recall doesn't verify in-car control."

**Common misuse:** testing or reporting Phase I and Phase II as a single combined pass/fail, or leaving a Phase II key switch engaged after a drill because "Phase I already reset."

### Step-chain elongation vs. comb-clearance

**Step-chain elongation** is the cumulative stretch of an escalator's step-drive chain over its service life, taken up by a tensioning device with finite remaining travel. **Comb-clearance** is the gap between the fixed comb plate at a landing and the moving step tread, a completely separate measurement governing entrapment risk at the landings. Both are gauge-measured, not visually estimated, and neither predicts the other.

**In use:** "Elongation's within tolerance, but comb clearance at the lower landing is the one that's drifted — gauge both every visit, don't assume one is fine because the other is."

**Common misuse:** using a single "escalator looks tight and rides smooth" impression to sign off on both measurements instead of gauging each independently.
