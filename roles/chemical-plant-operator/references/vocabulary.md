# Vocabulary

### Mass balance
The accounting principle that material entering a process must equal material leaving plus any accumulation, reaction, or loss, used to verify a process is behaving as expected.
**In use:** "Mass balance is 30 kg short of what evaporation alone explains — that's not normal variance, escalate it."
**Common misuse:** Assuming individually normal-looking flow or level readings mean the process is fine, without actually reconciling total inputs against outputs and inventory change.

### Exotherm (reaction)
The heat released by a chemical reaction, which for many reactions accelerates as temperature rises, creating a self-reinforcing runaway risk if not controlled.
**In use:** "Exotherm's picking up faster than the cooling loop can track — cut feed rate now, not after it climbs further."
**Common misuse:** Treating a rising batch temperature as a linear, easily-correctable trend rather than recognizing that heat generation rate can outpace fixed cooling capacity if allowed to drift.

### Alarm priority
The classification of an alarm by the actual severity of consequence and time available to respond, distinct from how frequently it triggers.
**In use:** "That's a low-priority nuisance alarm — the high-priority pressure alarm gets addressed first regardless of which one fired first."
**Common misuse:** Responding to alarms in order of occurrence or familiarity rather than by their actual consequence severity and urgency.

### Reactant addition sequence
The specified order and rate at which chemicals are combined in a process, designed to ensure the intended reaction pathway occurs safely.
**In use:** "Sequence matters here — adding B before A fully disperses risks a different, faster reaction than what's intended."
**Common misuse:** Assuming a different addition order or rate is equivalent as long as the same total materials eventually combine, ignoring that sequence and rate can produce a different, sometimes hazardous reaction pathway.

### Safe operating envelope
The combination of process variable ranges — temperature, pressure, concentration, flow — within which a process is safe to run, considered jointly rather than as independent single-variable limits.
**In use:** "Every variable's individually in range, but together they're at the edge of the safe operating envelope — treat that as a caution condition."
**Common misuse:** Verifying each variable individually against its own limit without checking whether the combination of several near-limit values together represents an unsafe condition.

### Interlock
An automated safety control that prevents a process action — opening a valve, starting a pump — unless specified conditions are met, enforcing correct sequencing or preventing hazardous combinations.
**In use:** "Interlock won't let that valve open until the reactor's below the specified temperature — that's by design, not a bug to work around."
**Common misuse:** Treating an interlock as an obstacle to bypass for convenience rather than as the enforced version of a sequencing or safety requirement.

### Runaway reaction
A reaction where heat generation exceeds cooling capacity and accelerates uncontrollably, often preceded by a gradual, easily-missed temperature drift.
**In use:** "That gradual half-degree drift an hour ago was the early sign — by the time it's obviously a runaway, the window to act cheaply has passed."
**Common misuse:** Assuming a runaway reaction is always a sudden, unmistakable event, rather than recognizing the early, subtle temperature trend that precedes and enables it.

### Batch record
Documentation of the actual materials charged, process conditions, and any deviations for a specific batch, used for traceability and quality verification.
**In use:** "Batch record shows the exact charge weights and timing — that's what let us trace the shortfall back to this specific step."
**Common misuse:** Logging a batch as "processed per procedure" without recording actual measured quantities and conditions, which prevents reconciling a mass balance discrepancy after the fact.

### Distributed control system (DCS)
The integrated computer control system used to monitor and adjust chemical process variables from a control room.
**In use:** "DCS shows every individual variable in range — still need to run the mass balance separately, since it won't flag that on its own."
**Common misuse:** Treating the DCS's individual variable displays as sufficient monitoring without also checking cross-variable relationships like mass balance that the DCS may not automatically flag.

### Chemical compatibility
Whether two or more chemicals can be safely mixed, stored, or processed together without an unintended, potentially hazardous reaction.
**In use:** "Checked the compatibility reference before sharing that tank — these two aren't cleared for co-storage."
**Common misuse:** Assuming any chemicals used in the same overall process are compatible for direct mixing or shared containment, without checking the specific compatibility reference for that combination.
