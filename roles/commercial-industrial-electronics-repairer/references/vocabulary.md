# Vocabulary

Terms generalists conflate that industrial controls/electronics practitioners keep sharply separate.

## Fault code vs. fault category vs. root cause

A **fault code** is the specific alarm the drive or PLC displays (e.g., "F5," "GF001"). A **fault category** groups codes by which physical side of the system they implicate — input/line, output/motor, drive-internal, or regenerative. **Root cause** is the actual failed part or condition confirmed by a test.

*In use:* "F5 is the code, overvoltage-during-decel is the category, and the confirmed root cause is an open DB resistor — not 'the drive.'"

*Common misuse:* treating the fault code itself as the diagnosis and jumping straight to a drive swap, skipping the category-narrowing step that would have pointed at a $180 part instead of a $4,200 one.

## Ladder logic vs. function block diagram vs. structured text

All three are IEC 61131-3 programming languages for PLCs. **Ladder logic** represents logic as rungs resembling relay circuits — the most common for discrete I/O. **Function block diagram** represents logic as interconnected functional blocks, common for process/analog control. **Structured text** is a text-based, higher-level language, common for math-heavy or complex sequencing.

*In use:* "The discrete interlocks are all ladder, but the PID loop on the oven zone is written in structured text — don't go hunting for it in the rungs."

*Common misuse:* assuming every PLC program is ladder logic; a program built primarily in function blocks or structured text won't show the fault condition as a rung at all.

## Forcing (I/O force) vs. actual value

A **forced** bit is manually pinned to a fixed value in the PLC, overriding whatever the physical input or program logic would otherwise produce, usually left over from a prior test. The **actual value** is what the input or logic would produce without any override.

*In use:* "The bit reads true, but check the force table first — someone forced it on last shift and never cleared it."

*Common misuse:* diagnosing a "stuck true" or "stuck false" condition as a hardware or logic fault without first checking whether it's simply a forgotten force — the single fastest wrong turn in PLC troubleshooting.

## Arc-flash boundary vs. restricted approach boundary vs. limited approach boundary

These are three distinct NFPA 70E-defined distances from an energized conductor, not interchangeable safety zones. **Limited approach boundary** is the outermost, where only qualified persons may cross. **Restricted approach boundary** is closer, requiring a documented shock-risk assessment and PPE. **Arc-flash boundary** is the distance at which incident energy drops to 1.2 cal/cm² (the second-degree-burn threshold) and is calculated independently of the other two.

*In use:* "We're inside the arc-flash boundary the moment the door's open, even if we're still outside the restricted approach boundary for shock."

*Common misuse:* treating all three boundaries as one line and assuming clearing "the boundary" satisfies every requirement — shock and arc-flash risk are assessed and mitigated separately.

## Incident energy vs. PPE category

**Incident energy** is the calculated or measured heat energy (cal/cm²) a worker at a given working distance would receive in an arc-flash event. **PPE category** is the discrete tier of protective clothing/equipment that NFPA 70E's tables map onto incident-energy bands.

*In use:* "The label says 6.2 cal/cm² at 18 inches — that's Category 2, not Category 1, so the lighter coverall doesn't cut it."

*Common misuse:* selecting PPE by category number from memory or habit instead of reading the panel's actual labeled incident energy, which is specific to that equipment's fault-current and clearing-time characteristics.

## Energized Electrical Work Permit (EEWP) vs. the testing/troubleshooting exception

An **EEWP** is the written, signed authorization NFPA 70E requires before most energized work. Testing, troubleshooting, and voltage measurement are on the standard's short exception list — permitted without a written EEWP in most site programs, but not without the shock/arc-flash risk assessment and matching PPE.

*In use:* "No permit needed for this — it's a diagnostic voltage check — but the Category 2 suit and insulated gloves still go on."

*Common misuse:* treating "no permit required" as "no PPE required" — the exception removes a paperwork step, not the underlying hazard assessment.

## Dynamic braking (DB) resistor vs. line regeneration

A **DB resistor** dissipates a motor's regenerative energy as heat during deceleration, switched in by a chopper transistor when the DC bus voltage rises. **Line regeneration** (a regenerative drive/front-end) instead feeds that energy back into the incoming line. Most single-drive installations use DB resistors, not line regen, unless specifically engineered for energy recovery.

*In use:* "This is a standard DB-resistor setup, not a regen front end — the OV trip on decel means look at the resistor and chopper, not the line side."

*Common misuse:* assuming any deceleration-related overvoltage trip is a line-side power-quality issue, which sends the diagnosis toward the utility or facility power instead of the drive's own braking circuit.

## Megger (insulation-resistance test) vs. continuity test

A **megger test** applies a high DC test voltage to measure insulation resistance between a conductor and ground/frame, catching insulation breakdown that a simple continuity check would miss. A **continuity test** confirms a conductor is unbroken end-to-end at low voltage — it says nothing about insulation condition.

*In use:* "Continuity's fine on the motor leads, but the megger reading is 0.4 MΩ against a 100 MΩ minimum — that's insulation breakdown, not a broken wire."

*Common misuse:* running only a continuity check on a suspected motor/cable fault and clearing it as good, missing an insulation-to-ground fault that continuity testing cannot detect.

## Fault-tolerant vs. safety-rated I/O

**Fault-tolerant** describes redundant or self-checking I/O built to keep operating (or fail to a known state) through a single component failure — a reliability property. **Safety-rated I/O** (e.g., a safety PLC input, a dual-channel E-stop circuit) is certified to a specific safety-integrity level and stop-time, a compliance property with its own re-validation requirement after any change.

*In use:* "That's fault-tolerant analog I/O for process uptime — it's not the safety circuit, and it doesn't need a safety re-validation after this edit."

*Common misuse:* assuming any redundant-looking circuit is "the safety circuit" and either over-applying re-validation paperwork to standard I/O or, worse, under-applying it to an actual safety-rated circuit.

## Board-swap vs. component-level repair (drive/PLC context)

**Board-swap** (or drive/module swap) replaces the entire failed assembly as a unit. **Component-level repair** replaces the specific failed part within that assembly — a resistor, a fan, a gate-driver chip — typically bench work requiring a confirmed root cause first.

*In use:* "It's one open resistor in the braking circuit — component repair at $180 beats a $4,200 drive swap, and the part's on the truck."

*Common misuse:* defaulting to a full swap because it's faster, without pricing the swap's parameter-reload and auto-tune time against the bench-repair alternative — the swap is often not actually faster once reconfiguration is included.
