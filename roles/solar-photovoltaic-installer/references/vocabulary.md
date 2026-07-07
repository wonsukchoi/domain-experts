# Vocabulary

Terms generalists conflate that PV installers keep sharply separate. Each: definition, a sentence a practitioner would actually say using it, and the common misuse.

## Voc vs. Vmp

**Voc** (open-circuit voltage) is a module's output voltage with no load connected — the highest voltage the module produces, and the figure that matters for string-sizing against an inverter's max input voltage. **Vmp** (voltage at maximum power point) is the operating voltage under load, always lower than Voc, and the figure the inverter's MPPT tracks during normal operation.

*Practitioner usage:* "Don't size the string off Vmp — the inverter has to survive Voc on a cold, no-load morning before it ever gets to track Vmp."

*Common misuse:* using Vmp in the max-voltage check because it's the "normal operating" number, missing that Voc governs the worst-case overvoltage risk.

## Temperature coefficient of Voc

The percentage change in a module's Voc per degree Celsius away from STC (25°C), always negative for crystalline silicon — Voc rises as temperature falls below 25°C and falls as temperature rises above it.

*Practitioner usage:* "This module's coefficient is −0.29% per degree — at our −18°C design low that's a 12% Voc bump, not a rounding error."

*Common misuse:* applying a coefficient from a different module's datasheet, or skipping the calculation entirely because "it's close enough at STC."

## Array boundary (rapid shutdown)

The zone within 1 ft in all directions of a PV array's modules and conductors, as defined for NEC 690.12 rapid-shutdown purposes — conductors outside this boundary must reach ≤30 V within 30 seconds of initiation, and current code requires the same limit *inside* the boundary as well, at module or sub-array level.

*Practitioner usage:* "The array boundary isn't just 'the array' — it's a 1-foot buffer around it, and conductors inside that buffer need their own rapid-shutdown control now, not just the output at the combiner."

*Common misuse:* treating "rapid shutdown" as satisfied once the array's single output point is controlled, without checking the inside-boundary requirement.

## MLPE (module-level power electronics) vs. central inverter RSD

**MLPE** — power optimizers or microinverters — perform power conversion or voltage limiting at each individual module. A **central inverter's array-boundary RSD (rapid shutdown device)** is a single relay or combiner-level device that controls the array's output as a whole. MLPE inherently satisfies the inside-array-boundary rapid-shutdown requirement; a central-only RSD device does not.

*Practitioner usage:* "We went with optimizers on this one specifically because it handles rapid shutdown at module level without adding a separate RSD box."

*Common misuse:* assuming any listed "rapid shutdown device" satisfies both zones regardless of where it sits in the circuit.

## 120% rule vs. 125% continuous-current rule

The **120% rule** (NEC 705.12(B)(3)(c)) caps the backfed breaker a busbar can carry, calculated from the busbar and main breaker ratings. The **125% continuous-current rule** (NEC 690.8(A)) sizes the minimum breaker or conductor ampacity from the inverter's actual continuous output current. They're two separate calculations that happen to both apply to the same breaker — passing one doesn't mean the other is satisfied.

*Practitioner usage:* "The 40-amp breaker clears the 120% busbar ceiling, but the inverter's actual output only calls for 30 amps under the 125% rule — we're sizing to the smaller, correct number, not just whatever the busbar allows."

*Common misuse:* citing the 120% rule alone as justification for a breaker size, without checking it against the inverter's actual required ampacity.

## Supply-side connection vs. load-side (breaker) tap

A **supply-side connection** taps into the service conductors ahead of the main breaker, entirely outside the 120% busbar rule, but requires its own disconnect and utility coordination. A **load-side tap** is a breaker added to the existing busbar downstream of the main breaker, and is the connection type the 120% rule constrains.

*Practitioner usage:* "This panel has no busbar headroom left — we're going supply-side instead of fighting the 120% rule on a load-side tap."

*Common misuse:* assuming a supply-side connection needs the same 120%-rule check as a load-side tap — it doesn't, because it isn't sharing the busbar at all.

## Flashed mount vs. surface mount

A **flashed mount** integrates the racking attachment's flashing into the roofing material's water-shedding order — under the course above, over the course below — the same lap logic used for any other roof penetration. A **surface mount** (sealant-over-lag, no flashing) relies on the sealant bead alone as the water barrier.

*Practitioner usage:* "This is a flashed mount, not surface-mounted — the flashing goes under the next course up before it goes back down, sealant's the backup, not the seal."

*Common misuse:* calling any sealed-looking attachment "flashed" when no flashing piece was actually integrated into the course order.

## Pull-out value vs. "looks solid"

**Pull-out value** (or withdrawal capacity) is a tested or engineered load rating for a specific fastener/embedment/rafter-species combination — the number that actually governs how many attachment points a racking run needs against wind uplift. "Looks solid" is a visual judgment with no verified number behind it.

*Practitioner usage:* "I don't care that the lag looks tight — what's its pull-out rating for this rafter species, and does the spacing clear our uplift number?"

*Common misuse:* treating fastener size or a snug fit as a substitute for a documented pull-out rating when setting attachment spacing.

## UL 1741 vs. UL 3741

**UL 1741** is the listing standard for inverters, converters, and interconnection equipment generally (grid-support functions, anti-islanding, etc.). **UL 3741** is a specific standard for outdoor rapid-shutdown PV systems, covering array-boundary voltage-limiting equipment. They cover overlapping but distinct equipment scopes and aren't interchangeable citations.

*Practitioner usage:* "The inverter's UL 1741-listed for interconnection, but the rapid-shutdown compliance claim needs to point at the UL 3741 listing for the array-boundary equipment specifically."

*Common misuse:* citing UL 1741 as evidence of rapid-shutdown compliance when the relevant listing for array-boundary behavior is UL 3741.

## Net metering agreement vs. interconnection agreement

The **interconnection agreement** is the utility's technical approval to physically connect the system to the grid (equipment specs, protection settings, inspection sign-off). The **net metering agreement** is the billing arrangement for how exported energy is credited — a separate document, sometimes with a different approval timeline and sometimes not offered at all depending on the utility's tariff.

*Practitioner usage:* "Interconnection's approved, we can energize — the net metering paperwork with the utility's billing department is still a separate step and can lag behind it."

*Common misuse:* treating interconnection approval as automatically including net-metering billing terms, and promising a homeowner bill credits before that separate agreement is actually in place.

## Trigger height vs. array boundary

**Trigger height** (a fall-protection term, 6 ft under OSHA 1926.501(b)(13) for most construction work) governs when a PFAS or guardrail is required for the crew. **Array boundary** (a rapid-shutdown term, NEC 690.12, 1 ft around the array) governs where voltage-limiting requirements apply for firefighter safety. Both are fixed distances in the trade but govern entirely different hazards and don't substitute for each other in a safety plan.

*Practitioner usage:* "Fall protection's a trigger-height question, rapid shutdown's an array-boundary question — don't conflate the two just because they're both 'the roof safety stuff.'"

*Common misuse:* treating a single safety walkthrough that covers fall protection as having also covered rapid-shutdown/array-boundary compliance, when they're unrelated checks.
