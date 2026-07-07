# Vocabulary

Terms generalists conflate or use loosely that practitioners keep sharply separate. Each: definition, how a practitioner actually uses it in a sentence, and the common misuse.

## Symptom vs. root cause

A **symptom** is what the customer reports or the unit displays ("not cooling," error code, a noise). The **root cause** is the specific failed component confirmed by a measured test. A symptom can map to five or more distinct root causes.

*In use:* "The symptom is 'not cooling' — that's not a diagnosis, that's a starting point. I won't order a part until I've confirmed the root cause on the meter."

**Common misuse:** writing the ticket as "fixed: not cooling" instead of naming the confirmed failed component — this erases the data the next reliability or truck-stock review needs.

## Sealed system vs. open system

The **sealed system** is the refrigerant-containing loop (compressor, condenser, evaporator, and connecting lines) that is factory-brazed and legally restricted under EPA rules. The **open system** is everything else on the appliance — controls, motors, switches, water valves — that any technician can service without refrigerant certification.

*In use:* "The fan motor's an open-system part, swap it today. The compressor's sealed-system — that's a scheduled visit with recovery equipment."

**Common misuse:** treating "sealed system" as a vague synonym for "the cooling parts" rather than the specific legally-regulated boundary that determines what a technician may open without certification.

## EPA Section 608 certification (Type I / Type II / Type III / Universal)

A federal certification required to purchase, handle, or recover refrigerant. **Type I** covers small appliances (5 lbs of refrigerant charge or less — most household refrigerators, freezers, window/portable AC, dehumidifiers). **Type II** covers high-pressure appliances (most residential split-system AC/heat pumps). **Type III** covers low-pressure appliances (rare in home appliance work). **Universal** covers all three.

*In use:* "I'm Type I certified, that covers this freezer's sealed system — I'm not Universal, so the split-system heat pump call goes to someone else."

**Common misuse:** assuming any refrigerant certification covers any refrigerant-containing appliance — the type classes are equipment-specific, not a single blanket license.

## First-visit fix rate vs. calls completed

**First-visit fix rate** (also first-time fix rate) is the share of service calls resolved without a follow-up visit for the same fault. **Calls completed** just counts tickets closed, regardless of whether a return trip was needed. Industry benchmarks commonly cited put average first-visit fix rate around the mid-70% range, with best-in-class field-service programs in the high 80s.

*In use:* "We closed six tickets today, but two of those are actually still open — that's a first-visit fix rate problem, not a productivity win."

**Common misuse:** reporting daily call volume as a proxy for performance when a meaningful share of those calls are unresolved first visits waiting on a part.

## 50% rule vs. total cost of ownership

The **50% rule** is the specific heuristic that repair cost above roughly half of replacement cost favors replacement. **Total cost of ownership** is the broader (and harder to pin down) comparison including expected remaining repairs, energy efficiency differences, and the replacement unit's own expected life — the 50% rule is a fast proxy for it, not the same calculation.

*In use:* "The 50% rule says repair here — but this is unit's third repair in two years, so the real total-cost picture favors replacing even though this single repair clears the rule."

**Common misuse:** applying the 50% rule as if it were the complete analysis, ignoring repair history or a unit already flagged for a second confirmed fault on the same visit.

## Recall vs. service bulletin vs. voluntary repair program

A **recall** is a formal CPSC-announced action, typically for a safety hazard, with a defined remedy (repair, replacement, refund). A **service bulletin** is a manufacturer's internal or dealer-facing notice about a known failure pattern and fix, not necessarily involving CPSC or a customer-facing safety claim. A **voluntary repair program** sits between the two — manufacturer-initiated, customer-facing, but not a formal CPSC recall.

*In use:* "This isn't a recall, it's a service bulletin — the fix is documented, but there's no free-repair obligation attached the way there would be with a recall."

**Common misuse:** telling a customer "there's no recall" and stopping there, without checking whether a voluntary repair program or service bulletin still applies to the specific fault.

## Locked-rotor amps vs. running amps

**Running amps** (or full-load amps) is the current a motor or compressor draws under normal operating load. **Locked-rotor amps** is the (much higher) current drawn at the instant of startup or when the rotor can't turn — a compressor reading near its locked-rotor spec continuously, rather than briefly at startup, indicates the motor is straining or seized.

*In use:* "It's not drawing running amps, it's pegged at locked-rotor the whole cycle — that compressor's not turning, it's trying to."

**Common misuse:** reading any elevated amp draw as "the compressor's bad" without distinguishing a brief, normal locked-rotor startup spike from a sustained locked-rotor reading, which are very different faults.

## Truck stock vs. special order

**Truck stock** (van stock) is parts carried on the vehicle for same-visit fixes, sized to the highest-frequency faults. **Special order** parts are model-specific or low-frequency components (control boards, compressors) ordered after diagnosis confirms the need, arriving on a later visit.

*In use:* "The fan motor's truck stock, we're fixing this today. The control board's a special order — model-specific SKU, I don't carry ten variants of it on the van."

**Common misuse:** treating a return trip for a special-order part as a diagnostic failure — it's only a first-visit-fix miss if the part should reasonably have been in truck stock given its fault frequency.

## Defrost cycle failure vs. compressor failure

Both can produce an identical "not cooling, ice buildup" symptom, but they're different systems: **defrost cycle failure** is a fault in the heater, thermostat, or timer that periodically melts frost off the evaporator coil; **compressor failure** is the sealed-system pump itself failing to circulate refrigerant. Confusing the two leads to a sealed-system quote when the fix is a $45 heater, or vice versa.

*In use:* "The evaporator's iced solid, but that's consistent with either a dead defrost heater or a dying compressor — I'm testing the heater's continuity first because it's the cheaper, more common cause."

**Common misuse:** assuming a heavily iced evaporator automatically means the compressor is failing, when it's the far-more-common downstream effect of a defrost system fault.

## Amp draw vs. voltage check

An **amp draw** (current) reading tells you how hard a motor or heating element is working, or whether it's drawing at all. A **voltage check** tells you whether the component is receiving power in the first place. A part reading zero amps could be an open circuit (no voltage reaching it) or a component that's receiving voltage but seized/failed — the two checks answer different questions and both are usually needed.

*In use:* "It's got voltage at the terminal but zero amp draw — that's not a power supply problem, that's a seized motor or an open winding."

**Common misuse:** treating a single meter reading as a complete diagnosis when voltage-present-but-no-current and no-voltage-present point to entirely different fault locations upstream or downstream of the component.
