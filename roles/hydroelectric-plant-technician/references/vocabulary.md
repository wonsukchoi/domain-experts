# Vocabulary

### Cavitation (hydro turbine)
A hydraulic phenomenon where local pressure inside a turbine drops below vapor pressure, forming vapor bubbles that then collapse violently against the runner surface, progressively eroding it over time.
**In use:** "Running at that flow rate for this head puts us in the cavitation zone — damage that won't show up until the next inspection."
**Common misuse:** Assuming a unit is fine because it's running normally and producing power — cavitation damage accumulates progressively and invisibly during operation, only becoming apparent at a physical inspection of the runner, not through real-time performance monitoring.

### Hydraulic head
The effective water pressure/elevation difference driving a hydro turbine, which changes as reservoir level fluctuates and directly determines both achievable power output and the turbine's safe operating range.
**In use:** "Head's dropped fifteen percent with the reservoir drawdown — that changes what flow rate is actually safe here, not just how much power we can make."
**Common misuse:** Treating head as a fixed design parameter rather than a variable operating condition — reservoir level fluctuation changes head meaningfully over time, and the turbine's safe/efficient operating range shifts correspondingly.

### Cavitation-safe operating range (head-and-flow dependent)
The combination of head and flow rate within which a specific turbine can operate without significant cavitation risk, which shifts (typically narrowing and moving to lower flow) as head decreases.
**In use:** "Safe range at a hundred feet is eight hundred to twelve hundred cfs, but at eighty-five feet that narrows to six hundred to nine hundred — completely different range for the lower head."
**Common misuse:** Treating a turbine's safe operating range as a fixed flow-rate band independent of head — the actual safe range is defined by the combination of head and flow together, and a flow rate safe at one head can be unsafe at a different head.

### Environmental/fish-passage flow requirement
A regulatory-mandated minimum water flow release from a hydro facility, required for downstream ecological or fish migration purposes, functioning as a hard compliance constraint on generation scheduling.
**In use:** "Minimum flow requirement's four hundred cfs — that's satisfied first, then we optimize generation within whatever's left."
**Common misuse:** Treating the mandated minimum flow as one factor to balance against generation revenue rather than a hard constraint that must be satisfied regardless of its effect on power output — it's a regulatory requirement, not a negotiable operational trade-off.

### Governor (hydro turbine)
The control system managing a turbine's response to grid frequency deviations, adjusting wicket gate position or flow to help stabilize grid frequency, with tuning parameters (response speed, deadband) requiring specific verification.
**In use:** "Governor's tuned for a moderate response speed with a small deadband — verifying that's still accurate with an actual frequency response test, not just assuming from normal operation."
**Common misuse:** Assuming governor tuning is correct because the unit generates power normally under steady-state conditions — steady-state operation doesn't reveal how the governor actually responds to a frequency deviation, which requires a specific test to verify.

### Deadband (governor tuning)
The range of frequency deviation within which a governor doesn't initiate a response, a tuning parameter that (if set incorrectly) can cause a unit to either over-respond to normal fluctuations or fail to respond to deviations it should address.
**In use:** "Deadband's too narrow — the unit's chasing every minor frequency fluctuation instead of only responding to real deviations."
**Common misuse:** Treating deadband as a minor technical detail rather than a parameter directly affecting grid stability contribution — too narrow a deadband causes unnecessary hunting/oscillation, too wide fails to provide expected frequency support.

### Runner (turbine)
The rotating component of a hydro turbine that converts water flow energy into mechanical rotation, the primary component subject to progressive cavitation erosion damage.
**In use:** "Runner inspection found erosion consistent with cavitation — checking the operating log for when flow/head combinations fell outside the safe range."
**Common misuse:** Assuming runner condition can be inferred from operational performance alone — cavitation erosion doesn't necessarily affect generation output or efficiency noticeably until it becomes severe, making physical inspection the actual way to assess accumulated damage.

### Wicket gates
Adjustable vanes controlling water flow into a hydro turbine, whose position (controlled by the governor) determines both power output and the turbine's actual operating point relative to its safe/efficient range.
**In use:** "Adjusting wicket gate position to bring flow down into the safe range for this head."
**Common misuse:** Treating wicket gate position purely as a power-output control without considering its effect on the turbine's operating point relative to cavitation risk — the same gate position that's safe at one head can push the unit into a cavitation-risk zone at a different head.

### Head-dependent operating point recalculation
The practice of re-determining a turbine's target flow rate/operating point whenever reservoir head changes meaningfully, rather than holding a fixed setpoint regardless of head.
**In use:** "Recalculating operating point for the new head before we just carry over yesterday's setpoint."
**Common misuse:** Holding a flow rate setpoint constant across changing head conditions because "it worked before" — the turbine's safe and efficient operating point is head-dependent, and a setpoint that was appropriate at one head needs re-evaluation whenever head changes meaningfully.
