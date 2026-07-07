# Vocabulary

Terms generalists conflate or use loosely that practitioners keep sharply separate. Each: definition, how a practitioner actually uses it, and the common misuse.

### Freeze-frame data vs. active fault code

The **active fault code** just names which circuit/parameter tripped a threshold. **Freeze-frame data** is the snapshot of live sensor values (voltage, pressure, rpm, temperature) captured at the moment the fault triggered — it shows *how* the signal behaved, which is what actually distinguishes a bad component from a bad harness.

**In use:** "Code says pressure sensor circuit, voltage above normal — but the freeze frame shows it pegged flat at 5V the whole time. That's a short, not a sensor reading a real high pressure."

**Common misuse:** treating the fault code's plain-English description as the diagnosis and ordering the named part without ever pulling the freeze-frame data that would confirm or rule it out.

### SPN/FMI vs. proprietary DTC

**SPN/FMI** (Suspicious Parameter Number / Failure Mode Identifier) is the SAE J1939 standard structure most modern ag ECUs use — SPN identifies the parameter, FMI identifies how it failed (above normal, below normal, erratic, etc.). A **proprietary DTC** is a manufacturer-specific code outside that structure, readable only with that manufacturer's software or a licensed aftermarket tool with the proprietary code list loaded.

**In use:** "That's a standard SPN/FMI code, any J1939-capable tool will read it — but the implement-pairing fault is a proprietary DTC, we need the OEM software or a Jaltest license with that manufacturer's database."

**Common misuse:** assuming any generic code reader will pull every fault on the machine, then being surprised when a proprietary fault shows up as an unreadable or generic "manufacturer-specific" placeholder.

### Main relief (or standby) pressure vs. charge pressure

**Main relief/standby pressure** is the working pressure available to an implement circuit or remote (open-center relief setting, or closed-center standby pressure). **Charge pressure** is the lower supply pressure that feeds a hydrostatic drive's main loop — a separate, smaller circuit whose job is keeping the main loop full, not doing the work itself.

**In use:** "Feeder house is sluggish — before we condemn the hydrostatic motor, check charge pressure. If that's low, the main loop's starved and nothing downstream will look right."

**Common misuse:** running a single "system pressure" check and treating it as covering both circuits, missing a charge-pressure problem because the main relief setting still tests correctly in isolation.

### Case-drain flow/temperature vs. system (working) pressure

**System pressure** tells you what the circuit is commanded to deliver. **Case-drain flow and temperature** measure internal leakage past worn seals or components inside a pump or motor — a wear indicator that shows up before the machine's actual output symptom does.

**In use:** "Working pressure's still in spec, but case-drain temp is climbing fast under load — that pump's wearing internally, it just hasn't failed enough to drop pressure yet."

**Common misuse:** clearing a hydraulic component because system pressure tests fine, without checking case-drain data that would have caught developing internal wear earlier.

### 540 vs. 1000 rpm PTO (and 540E)

**540 rpm** (6-spline) and **1000 rpm** (20/21-spline) are the two standard PTO output speeds; **540E** is an economy variant delivering the same 540 rpm output at reduced engine rpm for fuel savings. The ratings are not interchangeable — they're matched to different implement torque and power designs, not just a dial setting.

**In use:** "That baler's 1000-rated — running it off the tractor's 540 output will starve it, not just slow it down."

**Common misuse:** assuming PTO speed is a simple dial choice rather than a spec that must match the implement, and running a mismatched pairing until a shear pin or driveline component fails.

### ISOBUS vs. proprietary CAN implementation

**ISOBUS** (ISO 11783) is the standardized tractor-implement communication protocol most modern displays and implements support for cross-brand compatibility. A **proprietary CAN implementation** is a manufacturer's own bus protocol layered on the same physical CAN hardware but not interoperable with another brand's ISOBUS-only equipment without a compatible interface.

**In use:** "The implement's ISOBUS-certified, so it'll talk to any Class 3 display — but the tractor's own internal CAN bus is proprietary, don't go probing that expecting ISOBUS message structure."

**Common misuse:** assuming "it's all CAN bus" means any tool or display can read any system on the machine, when ISOBUS compliance and a manufacturer's internal proprietary bus are separate networks with separate message formats.

### Dealer diagnostic-tool subscription vs. one-time purchase

Most OEM diagnostic software (Service ADVISOR, EST, EDT) is licensed on a **recurring subscription** tied to a dealer account, not sold as a one-time tool purchase to an independent shop or farm — a structural cost that recurs annually regardless of how many repairs it's used for.

**In use:** "We're not buying Service ADVISOR outright — it's a subscription, and letting it lapse mid-season means a simple calibration turns into a dealer appointment."

**Common misuse:** budgeting for OEM diagnostic access as a one-time capital cost rather than a recurring line item that has to stay current through the season it's needed.

### ECU reflash/calibration vs. parameter reset

A **reflash** rewrites the ECU's firmware/software; a **calibration** sets machine-specific values (injector trim codes, component matching data) after a part replacement. A **parameter reset** just returns user-adjustable settings (not firmware or calibration data) to default — a much smaller and usually field-serviceable operation.

**In use:** "Swapping that injector needs a calibration to code the new trim values in — that's not the same as the parameter reset we can do from the cab menu."

**Common misuse:** assuming any in-cab "reset" option covers a required calibration after a part swap, then finding the machine runs poorly because the trim/calibration data was never actually updated.

### Mobile service call vs. shop teardown

A **mobile service call** brings diagnostic and repair capability to the machine in the field — appropriate when the fault is likely field-repairable and the calendar cost of transport/queue time is high. A **shop teardown** is warranted when the repair genuinely requires shop equipment (press, lift, specialized tooling) regardless of season.

**In use:** "This is a harness repair — mobile call, we'll have them running in under two hours. The rotor bearing replacement is a shop job no matter what the calendar says."

**Common misuse:** defaulting to a shop appointment out of habit for a fault that a mobile visit could resolve same-day, adding transport and queue delay during a window where that delay has real cost.

### Parts cannon vs. confirmed diagnosis

The **parts cannon** approach replaces the component the fault code names, hoping it resolves the issue, without confirming root cause first. A **confirmed diagnosis** verifies the failure mode (with freeze-frame data, a pressure test, or a direct continuity/resistance check) before any part is ordered.

**In use:** "Let's not parts-cannon this — pull the freeze frame first, confirm it's actually the sensor and not the harness feeding it."

**Common misuse:** treating a fast parts swap as the time-saving move during a harvest-window breakdown, when an unconfirmed swap that doesn't fix the fault costs more total downtime than the ten minutes it would have taken to confirm first.

### Seed-tube/row-unit sensor fault vs. mechanical meter wear

A **row-unit sensor fault** is an electronic fault in the seed-sensing or population-reporting hardware itself. **Mechanical meter wear** (a worn seed disk, a degraded brush or belt in the metering mechanism) produces a similar-looking population or singulation error on the monitor without any electronic fault present at all — the monitor can't tell these apart, only a physical inspection can.

**In use:** "Monitor's flagging a population drop on row 6 — check the meter for disk wear before pulling the sensor, a worn disk throws the same symptom as a bad sensor."

**Common misuse:** replacing the row-unit sensor because the monitor flagged that row, without inspecting the metering mechanism itself for wear that would produce the identical monitor reading.

### Pre-season inspection vs. warranty/PDI inspection

A **pre-season inspection** is a recurring, owner-scheduled check run before each season regardless of machine age or warranty status. A **PDI (pre-delivery inspection)** is a one-time dealer check performed before a new or newly-serviced machine's first delivery to the customer — the two are sometimes confused as covering the same ground, but PDI doesn't repeat and doesn't catch a season's worth of accumulated wear.

**In use:** "PDI was two years ago when this combine was new — that's not a substitute for this fall's pre-season check on the hydraulics and harness wear points."

**Common misuse:** assuming a machine that had a thorough PDI at purchase doesn't need a recurring pre-season inspection, missing wear that's accumulated since delivery.
