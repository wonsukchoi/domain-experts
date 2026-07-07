# Red flags

Signals a pump station operator catches during a round, an alarm response, or a review of trend data. Format for each: what it usually means, the first question to ask, and the data to pull before deciding anything.

### NPSH margin ratio (NPSHa/NPSHr) below 1.2 at current operating flow

- **Usually means:** the pump is at or approaching cavitation risk — a dropped wet well/suction level, added suction friction, or a higher-flow duty point than the curve was checked against.
- **First question:** "Has suction-side geometry, level, or liquid temperature changed since this was last calculated, or is this the same pump running at a different flow?"
- **Data to pull:** current suction level/pressure, suction piping friction losses, NPSHr from the manufacturer curve at actual (not rated) flow, liquid temperature.

### Pump producing a rattling or "gravel/marbles" sound with stable discharge pressure

- **Usually means:** cavitation at the impeller eye — vapor bubbles forming and collapsing — occurring before it shows up as a measurable performance loss.
- **First question:** "What's the NPSH margin at this exact flow right now, not at rated flow?"
- **Data to pull:** current flow and suction pressure, NPSHr at that flow, recent impeller inspection or vibration history.

### Wet well level reaches the high-level alarm setpoint

- **Usually means:** inflow is exceeding pump capacity — a power issue, a clogged pump, a failed lead pump, or a genuine wet-weather inflow spike — with a defined freeboard window before overflow.
- **First question:** "How many minutes of freeboard remain at current inflow if no additional pump comes online right now?"
- **Data to pull:** current level, inflow rate estimate, standby pump/generator status, time-to-overflow calculation for this station's known geometry.

### Any discharge reaching a storm drain, ditch, or waterway from a wet well or manhole

- **Usually means:** a reportable sanitary sewer overflow (SSO) under the applicable state program and the Clean Water Act's discharge prohibition — the notification clock starts at discovery, not at confirmation of volume.
- **First question:** "What time was this discovered, and has the state/health-department notification clock already started?"
- **Data to pull:** discovery timestamp, estimated volume and duration, receiving water identification, the applicable state program's category and reporting-timeline requirements.

### Valve or pump actuator closure time shorter than the pipe's critical period (Tc = 2L/a)

- **Usually means:** the closure will produce close to the full Joukowsky surge regardless of how gradual the actuator appears — a factory default timing that was never checked against this pipe's length and wave speed.
- **First question:** "What's Tc for this specific run, and how does the current actuator setting compare to it?"
- **Data to pull:** pipe length and material (for wave speed), current actuator closure-time setting, downstream pipe/fitting pressure ratings.

### Check valve audibly slamming on pump shutdown

- **Usually means:** a water-hammer event at the moment of flow reversal — the same pressure-reversal mechanism a surge study is meant to prevent, happening in miniature every cycle.
- **First question:** "Is this a new sound for this pump/valve combination, or has it always done this?"
- **Data to pull:** pump shutdown sequence (VFD ramp-down vs. instant trip), check valve type and age, any recent change in system pressure or pipe configuration.

### Suction pressure dropping toward zero or a pump losing prime

- **Usually means:** a closed or obstructed suction valve, a dropped wet-well/source level below the suction bell, or a failed foot valve/priming system — and a seal-damage clock measured in seconds to low minutes.
- **First question:** "Has the automatic low-suction-pressure trip already fired, or is the pump still running dry right now?"
- **Data to pull:** current suction pressure reading, trip-point setpoint and whether it activated, seal-chamber temperature if instrumented.

### Duty point outside roughly 70–120% of the pump's best efficiency point (BEP)

- **Usually means:** the system curve has shifted (a throttled valve, a changed downstream demand, a new branch) more than the pump selection — running there wears bearings and seals faster even while flow and pressure look adequate.
- **First question:** "What changed on the system side — not the pump side — that moved the duty point off the curve's efficient range?"
- **Data to pull:** current flow and head at the duty point, pump's BEP flow from its curve, any recent valve position or downstream demand change.

### Bearing temperature or vibration trending upward over several consecutive readings

- **Usually means:** a lagging confirmation of an NPSH-margin or BEP problem that's been present for a while, more often than a bearing defect appearing on its own.
- **First question:** "Does this correlate with a duty-point or NPSH-margin change, or is it isolated to this pump regardless of operating point?"
- **Data to pull:** vibration/temperature trend over recent weeks, NPSH margin and BEP ratio at current operating flow, maintenance history on this pump.

### Force main or suction line air pocket suspected (uneven flow, pressure oscillation with no valve change)

- **Usually means:** trapped air at a high point altering effective pipe diameter and contributing to pressure oscillation or reduced surge protection at air/vacuum valve locations.
- **First question:** "Are the air/vacuum valves at the known high points functioning, and when were they last inspected?"
- **Data to pull:** pipeline profile (high-point locations), air valve inspection/maintenance log, pressure trend at the suspected location.
