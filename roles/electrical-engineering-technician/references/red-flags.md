# Red flags

Smell tests a bench test/debug technologist catches on a first pass over a failure report, test log, or fault disposition.

### Rework note says "reflowed/reseated, unit passed" with no before/after resistance or voltage number attached

- **Usually means:** the rework was performed without confirming which specific joint or connection was defective — a reseated connector or a general reflow can mask the real fault without fixing it, and it will reappear on the next thermal cycle or vibration event.
- **First question:** what was the node-to-node resistance or voltage measured before the rework, and what was it measured at after, at the same load current?
- **Data to pull:** the before/after IR-drop or continuity measurements for the specific node reworked, not just the retest pass/fail.

### Scope screenshot in the test record has no bandwidth or probe attenuation setting recorded

- **Usually means:** the rise-time or amplitude reading on the screenshot can't be independently checked against the instrument's own contribution (SKILL.md First-principles core #2), and the measurement isn't reproducible by anyone else.
- **First question:** what scope model/bandwidth and probe attenuation (1x/10x) were used for this capture?
- **Data to pull:** the scope's channel setup screen or the test procedure's specified instrument configuration for this step.

### A returned or field-failed unit's ESD-handling log is missing or unfilled at intake

- **Usually means:** there's no way to rule ESD in or out as a contributor to an otherwise-unexplained intermittent or marginal failure, and a unit gets dispositioned as a simple part failure when it may be a latent ESD event.
- **First question:** was this unit's chain of custody from depackaging to intake entirely inside an ESD-protected area, and if not, for how long and under what conditions was it outside one?
- **Data to pull:** the handling/shipping log and the EPA (ESD-protected area) qualification record for any station the unit passed through.

### A suspect component is discarded without an out-of-circuit verification

- **Usually means:** the fix that actually resolved the symptom is unconfirmed — it could be the swapped part, or it could be an incidental disturbance (a reseated connector, a cleaned contact) during the same repair action.
- **First question:** was the removed component tested out-of-circuit (curve tracer, component tester) and found actually out of spec, or was it swapped on suspicion alone?
- **Data to pull:** the out-of-circuit test result for the removed part, if one exists.

### More than roughly 3 units fail the same test step within one shift, each dispositioned individually

- **Usually means:** a process escape (a solder profile drift, a connector lot change, a handling-procedure lapse) is producing correlated failures, not independent random defects, and treating each as an isolated unit repair misses the corrective-action opportunity.
- **First question:** do the failed units share a build date, lot, station, or operator in common?
- **Data to pull:** the traveler/build records for the failed units, cross-referenced by lot and station.

### A "cannot reproduce" or "no fault found" disposition used default trigger settings and a single capture attempt

- **Usually means:** the fault's actual trigger condition or duty cycle was never searched for — a narrow single-shot capture on a default edge trigger will miss anything that isn't a clean, frequent, single-polarity event.
- **First question:** was persistence/infinite-persistence mode or a widened trigger condition (pulse width, runt, window) tried before closing the ticket?
- **Data to pull:** the scope's trigger and acquisition mode settings used during the reproduction attempt.

### An IPC-A-610 finding is cited with no class number

- **Usually means:** the reviewer can't tell whether the condition cited is actually a defect for this build's contracted class, since Class 1/2/3 acceptance criteria for the same visual condition (e.g., solder fillet height, void percentage) differ materially.
- **First question:** what IPC-A-610 class does this build's contract or drawing specify, and does the cited condition fail at that class?
- **Data to pull:** the build's IPC class callout (drawing note or contract) and the specific criterion table for that class.

### A resistance in the tens-of-milliohms range is measured with a standard 2-wire DMM lead set

- **Usually means:** the reading includes lead and contact resistance that can itself be tens of milliohms, making the reported number unreliable at the resolution needed to confirm or rule out the suspected fault.
- **First question:** was this measurement taken 4-wire (Kelvin), and if not, what is this DMM/lead combination's known residual resistance?
- **Data to pull:** the measurement method noted in the test record and, if 2-wire, a null/short-lead-resistance check for that same lead set.

### A downstream IC is declared dead with no check of power-rail sequencing or ordering at power-up

- **Usually means:** some ICs (particularly those with separate core/IO rails) latch into a fault state or sustain damage if rails power up out of the datasheet-specified order or timing window, which looks identical on a post-mortem to a simple component failure.
- **First question:** does this IC's datasheet specify a rail power-up sequence or maximum skew between rails, and was that sequence verified on this board at the time of failure?
- **Data to pull:** the IC datasheet's power-sequencing requirement and a scope capture of the actual rail rise order on the failed unit (or an exemplar of the same design).

### A repaired unit is retested only at the specific step that originally failed

- **Usually means:** a shared root cause (an ESD event, a process escape affecting a whole lot) can produce a second latent fault elsewhere on the board that the single-step retest won't catch, shipping a unit with an undetected second defect.
- **First question:** was the full test procedure re-run after rework, or only the originally-failed step?
- **Data to pull:** the post-rework test log's step coverage versus the full procedure's step list.
