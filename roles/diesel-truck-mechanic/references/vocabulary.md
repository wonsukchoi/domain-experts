# Diesel Truck Mechanic — Vocabulary

### Derate
An ECM-commanded staged reduction in engine torque and/or road speed triggered by an unresolved emissions or safety fault, escalating in steps (e.g., torque limited, then speed capped at 5 mph) rather than a sudden shutdown.
**In use:** "It's in the second-stage derate already — 5 mph — so we're towing it, not driving it in."
**Common misuse:** Treating derate as a single on/off failure state rather than a graduated sequence, which leads to driving a truck further than the derate stage allows and turning a sensor issue into a catalyst or turbo replacement.

### Regen (regeneration)
The process of burning off accumulated soot in the diesel particulate filter (DPF), occurring passively during normal high-exhaust-temperature operation, actively via ECM-commanded fuel dosing, or manually via a parked forced regen.
**In use:** "This truck never gets hot enough on its route to passive-regen, so it's forcing an active regen every other day."
**Common misuse:** Assuming every DPF warning lamp calls for an immediate forced regen, without checking whether the underlying cause (short-trip duty cycle, failing injector) will just reload the filter within days.

### SCR (Selective Catalytic Reduction)
The aftertreatment system that injects DEF into the exhaust stream to convert NOx into nitrogen and water across a catalyst, separate from the DPF's job of trapping particulate soot.
**In use:** "The code's on the SCR side, not the DPF — don't pull the filter, check the NOx sensor delta first."
**Common misuse:** Conflating SCR faults with DPF/soot faults because both live in the exhaust aftertreatment system; they have different sensors, different failure modes, and different fixes.

### DEF quality fault (SPN 3364)
A J1939 fault code reporting that the reductant-quality sensor is reading DEF concentration outside the normal operating range — it reports what the sensor measures, not that the sensor itself is defective.
**In use:** "Before we order a new DEF quality sensor, pull a refractometer sample — half these codes are bad fluid, not a bad sensor."
**Common misuse:** Replacing the DEF quality sensor as the first response to the code, without independently testing the fluid concentration.

### Pushrod stroke
The linear travel of the brake chamber's pushrod when the brakes are applied, measured against a maximum allowable distance that varies by chamber type and size under CVSA criteria.
**In use:** "Type 30 on the drive axle is reading 2¼ inches of stroke — that's past the 2-inch limit, it's out of service."
**Common misuse:** Eyeballing chamber travel instead of measuring it with a stroke gauge against the specific chamber-type limit, or applying one stroke limit across all chamber sizes.

### Out-of-service (OOS)
A specific, published defect from the CVSA North American Standard Out-of-Service Criteria that legally bars a vehicle from operating until repaired — a defined checklist item, not a general judgment that something is "bad."
**In use:** "That's not just a repair item, that's an OOS item — the driver can't leave the yard until it's fixed."
**Common misuse:** Using "out of service" loosely to mean "needs repair soon," when it specifically means the vehicle cannot legally be driven until the cited defect is corrected.

### PM-A / PM-B
Tiered preventive maintenance intervals: PM-A covers lube, filters, and a safety walk-around; PM-B adds the full chassis, brake, and driveline inspection scope, typically at a longer mileage interval than PM-A.
**In use:** "This is due for a PM-B, not just a PM-A — get the stroke gauge out on all the chambers while it's up."
**Common misuse:** Treating PM-B as "a bigger oil change" instead of the point where brake, steering, and driveline items that don't get checked at PM-A actually get inspected.

### SPN/FMI
The SAE J1939 fault code format: Suspect Parameter Number identifies the system or component, Failure Mode Identifier describes how it's failing (e.g., "below normal range," "abnormal rate of change").
**In use:** "Same SPN as last time but a different FMI — it's not the same failure, don't reuse the last repair order."
**Common misuse:** Reading only the SPN and assuming it names a specific failed part, when the FMI is what actually narrows down the failure mode.

### Limp-home mode
The reduced-performance operating state (torque and/or speed limited) that lets a truck reach a destination under its own power after certain fault conditions, distinct from a full shutdown.
**In use:** "It's in limp-home at 5 mph — that's meant to get it to the yard, not to finish the route."
**Common misuse:** Continuing to dispatch or route a truck normally while it's in limp-home mode instead of treating it as a tow-or-terminal-only condition.

### Glad-hand
The coupling that connects the tractor's air lines (service and emergency) to the trailer's air brake system.
**In use:** "Air loss is at the glad-hand seal, not the trailer valve — swap the rubber seal before condemning anything downstream."
**Common misuse:** Assuming an air-loss complaint is a trailer brake system fault before checking the glad-hand connection and seals, which are a far more common and cheaper failure point.

### Deadhead miles
Miles driven with an empty trailer or no load, generating cost but no freight revenue — relevant to downtime and repair-location decisions because it changes what "getting the truck back in revenue service" actually means.
**In use:** "If we tow it to the shop 60 miles out, that's deadhead both ways before it's earning again — factor that into the total cost, not just the tow bill."
**Common misuse:** Comparing repair options on parts and labor cost alone without factoring in the deadhead or out-of-route miles a tow or reposition adds.

### Blow-by
Combustion gases escaping past the piston rings into the crankcase, visible as excessive crankcase pressure or smoke from the breather tube.
**In use:** "Crankcase pressure's up and there's visible blow-by at idle — that's ring or liner wear, not a turbo seal."
**Common misuse:** Attributing any smoke from the engine compartment to a turbo failure without checking crankcase pressure and breather tube discharge first.

### CSA BASIC (Vehicle Maintenance)
One of FMCSA's Compliance, Safety, Accountability behavior analysis categories; a fleet's score here is driven by roadside inspection defects, including out-of-service violations, and affects how often its trucks get selected for inspection.
**In use:** "Two OOS brake write-ups this quarter and our Vehicle Maintenance BASIC score is going to put every truck in this fleet under more roadside scrutiny."
**Common misuse:** Treating CSA BASIC scores as an abstract compliance metric disconnected from real inspection frequency, when a poor score measurably increases how often the fleet's trucks get pulled for inspection.
