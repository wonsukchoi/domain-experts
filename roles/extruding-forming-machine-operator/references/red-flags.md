# Red flags

### Outer diameter in spec but wall thickness not separately checked after a rate/speed change
- **Usually means:** a draw-down ratio change from a takeoff speed adjustment may have affected wall thickness even though sizing equipment held OD to spec.
- **First question:** was wall thickness measured directly, or only outer diameter?
- **Data to pull:** current wall thickness measurement, takeoff speed and extrusion rate before/after any recent change.

### Die dimensions set to match the target final part dimension directly
- **Usually means:** die swell and draw-down compensation may not have been accounted for, risking an incorrectly sized final part despite a "correctly sized" die.
- **First question:** does the die dimension include the appropriate swell/draw-down compensation for this material and process, or match the target dimension exactly?
- **Data to pull:** process characterization data for this material/die combination, actual die dimension vs. target part dimension.

### Melt temperature run at the higher end of the acceptable range "for safety margin" on flow
- **Usually means:** unnecessary degradation risk is being accepted for a flow margin that may not actually be needed.
- **First question:** does the material actually require this temperature for proper flow, or is it set higher than necessary?
- **Data to pull:** material's recommended processing temperature range, actual melt temperature and flow quality observed.

### A dimensional or quality issue that appeared partway through a run, not at start-up
- **Usually means:** a drifting process condition (barrel temperature, screw wear, feed consistency) rather than a fixed setup error.
- **First question:** did the run start in-spec, and if so, what could have changed since then?
- **Data to pull:** dimensional trend data across the run, process parameter trend (temperature, pressure) across the same period.

### A material degradation indicator (discoloration, off-gassing smell, reduced mechanical test result) discovered after a run that looked visually fine
- **Usually means:** excessive residence time or temperature degraded the material in a way not visible until later testing.
- **First question:** what was the actual melt temperature and residence time for this run relative to the material's degradation threshold?
- **Data to pull:** melt temperature/residence time log, any mechanical/quality test results from this run.

### Sizing/cooling calibration not re-verified after a process rate or die change
- **Usually means:** the die may have been adjusted, but sizing equipment — the actual final-dimension control — wasn't re-checked to match.
- **First question:** was sizing calibration verified against the new process conditions, or left at its prior setting?
- **Data to pull:** sizing equipment calibration record, process parameters at time of last calibration vs. current.

### An output rate increase implemented via takeoff speed alone, without a corresponding extrusion rate change
- **Usually means:** draw-down ratio has shifted, which affects wall thickness even if overall output volume increased as intended.
- **First question:** did extrusion (screw) rate increase proportionally with takeoff speed, or was takeoff speed changed alone?
- **Data to pull:** extrusion rate and takeoff speed before/after the change, resulting draw-down ratio.

### A new material or resin lot run without re-verifying process parameters (temperature, degradation threshold) for that specific material
- **Usually means:** parameters validated for a different material/lot may not be appropriate for the new one.
- **First question:** does the current material's processing specification match what's currently programmed, or is a prior material's settings being reused?
- **Data to pull:** current material's technical data sheet, actual programmed process parameters.

### A part failing a downstream mechanical/pressure test despite passing initial dimensional inspection
- **Usually means:** either a wall thickness issue not caught by OD-only inspection, or material degradation not visible at initial inspection.
- **First question:** was wall thickness specifically checked, and does the process log show melt temperature/residence time within spec for this run?
- **Data to pull:** wall thickness data for the affected parts, process log for the relevant production window.

### A shift handoff not specifying current draw-down ratio or sizing calibration status alongside rate settings
- **Usually means:** the incoming operator lacks the information needed to recognize whether current settings represent a validated, matched combination.
- **First question:** does the handoff specify the relationship between extrusion rate, takeoff speed, and sizing calibration, not just individual setpoints?
- **Data to pull:** the shift handoff record, current process parameter set.
