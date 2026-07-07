# Vocabulary

Terms generalists blur together that a compressor station operator keeps sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse.

## MAOP vs. relief valve set point

**MAOP** (maximum allowable operating pressure) is the PHMSA 49 CFR 192.619 regulatory ceiling for a pipeline segment, fixed by the weakest determining factor. The **relief valve set point** is the pressure at which a specific mechanical device lifts — it's set to act as a backstop under MAOP, not to define it.

*Practitioner usage:* "The relief valve is set at MAOP, but that doesn't mean MAOP moved — the relief valve is protecting the ceiling, not setting it."

*Common misuse:* treating the relief valve's set point as if it were the definition of MAOP, so that re-setting a relief valve is mistaken for a way to change the pipeline's operating limit.

## Isentropic vs. polytropic compression

**Isentropic** (ideal, no-loss) compression is the theoretical minimum temperature rise for a given pressure ratio. **Polytropic** compression accounts for real inefficiencies (friction, heat transfer, valve losses in a reciprocating unit), producing a higher actual discharge temperature than the isentropic calculation alone predicts.

*Practitioner usage:* "The isentropic number says 110°F rise, but with an 82% polytropic efficiency the actual discharge is running closer to 134°F rise — use the polytropic figure for the coating-limit check, not the ideal one."

*Common misuse:* using the isentropic (ideal) discharge temperature as the number to check against real equipment limits, which understates the actual temperature and misses a real excursion.

## Odorant concentration vs. LEL

The **lower explosive limit (LEL)** is the minimum gas-in-air concentration that can ignite (≈5% by volume for natural gas). **Odorant concentration** is a separate, lower threshold — §192.625 requires gas to be detectable by smell at no more than 1/5 of the LEL (≈1% gas-in-air) — so a leak is smelled well before it's anywhere near ignitable.

*Practitioner usage:* "We're not testing whether it's explosive at the test point — we're testing whether a person would smell it at one-fifth of that concentration, which is a much lower bar and the one that actually matters here."

*Common misuse:* treating "not at the LEL" as equivalent to "properly odorized," when the odorization requirement is a fraction of the LEL specifically so detection happens long before an explosive concentration is reached.

## ESD trip vs. relief valve

The **ESD (emergency shutdown) trip** is an active, instrumented response — sensors and logic that isolate and shut down the unit or station before a limit is reached. The **relief valve** is a passive mechanical backstop that only acts if pressure physically reaches its set point. They're independent protection layers, not redundant descriptions of the same protection.

*Practitioner usage:* "The ESD should trip and shut this down well before the relief valve ever has to lift — if the relief valve is doing the work, the ESD layer already failed."

*Common misuse:* citing a properly rated relief valve as sufficient overpressure protection on its own, without confirming the ESD trip is set to act first and actually functions.

## Blowdown vs. venting

**Blowdown** is the deliberate, sequenced depressurization of station piping through dedicated blowdown valves and stacks, following a documented rate and order to avoid secondary hazards (liquid slugging, uncontrolled vent-stack exposure). **Venting** is a broader, looser term sometimes used for any release to atmosphere, including unplanned ones.

*Practitioner usage:* "Follow the blowdown sequence in the O&M plan — don't just start venting from whatever valve is closest, the order and rate are there for a reason."

*Common misuse:* treating blowdown as interchangeable with "open a vent valve," skipping the documented sequence and rate that the procedure is built around.

## Aftercooler vs. intercooler

An **intercooler** cools gas between compression stages, before it enters the next stage's suction. An **aftercooler** cools gas after the final stage, before it enters the pipeline or downstream process. Losing one doesn't have the same failure signature as losing the other.

*Practitioner usage:* "It's the aftercooler fan that's down, not an intercooler — so stage-to-stage compression is unaffected, but final delivery temperature into the pipeline is what's at risk."

*Common misuse:* referring to any cooler on the unit generically as "the cooler," which obscures whether the affected stage is interstage or final discharge — the two have different downstream consequences.

## Reciprocating vs. centrifugal compressor

A **reciprocating** compressor moves gas via piston strokes in cylinders, well suited to high compression ratios per stage and variable/lower flow rates. A **centrifugal** compressor moves gas via a rotating impeller, well suited to high continuous flow at lower compression ratios per stage, and is subject to a distinct failure mode (surge) that reciprocating units don't have.

*Practitioner usage:* "This station's centrifugal unit needs a surge check on any load reduction — the recip skid across the yard doesn't have that failure mode at all."

*Common misuse:* applying reciprocating-specific troubleshooting (valve/rod-load focus) to a centrifugal trip, or vice versa, when the two machine types fail in fundamentally different ways.

## Surge (centrifugal compressors)

A flow-reversal instability that occurs when a centrifugal compressor's flow drops below its stable minimum for the current pressure ratio — the compressor briefly reverses flow, which repeats as a violent, damaging oscillation if not corrected immediately.

*Practitioner usage:* "We're getting close to the surge line on this reduction — open the recycle valve before we go any further, not after we hear it."

*Common misuse:* treating a single surge event as a minor operational hiccup rather than a mechanically damaging event that warrants inspection, and continuing to operate near the surge line without adjusting the anti-surge control.

## Class location vs. MAOP build-up allowance

**Class location** (PHMSA 49 CFR 192, Subpart K) is a population-density-based classification of a pipeline segment that drives design and testing requirements. The **build-up allowance** is the limited, short-duration pressure excursion above MAOP that regulations permit under specific conditions — it's not a general license to run over MAOP, and how much (if any) build-up is allowed depends on the segment's class location.

*Practitioner usage:* "Whatever build-up we might be allowed on this segment depends on its class location — check that before assuming any excursion above MAOP is automatically within tolerance."

*Common misuse:* assuming a fixed build-up percentage applies everywhere, when the actual allowance (if any) is tied to the specific segment's class location and operating history.

## Rod load (reciprocating compressors)

The combined mechanical force on a reciprocating compressor's piston rod from gas pressure differential across the piston, expressed as a percentage of the rod's rated capacity in each direction (compression and tension). Running near or over rated rod load risks rod, crosshead, or bearing damage independent of any temperature or pressure limit elsewhere in the system.

*Practitioner usage:* "Before we push this unit to the new discharge target, check rod load in both directions — the coating temperature limit isn't the only ceiling here."

*Common misuse:* checking only discharge pressure and temperature against pipeline limits while overlooking that a higher compression ratio can push rod load past the machine's own mechanical rating.
