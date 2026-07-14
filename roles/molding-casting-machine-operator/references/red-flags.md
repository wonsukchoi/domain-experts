# Red flags

### Intermittent porosity or defect found despite machine-displayed parameters reading consistently within spec
- **Usually means:** a gap exists between machine-set and actual in-cavity conditions that the standard display doesn't reveal.
- **First question:** does cavity pressure sensor data (if available) show consistent fill pressure, or does it vary shot-to-shot despite constant machine settings?
- **Data to pull:** cavity pressure trend data, shot sleeve/barrel fill consistency data, recent X-ray or internal inspection results.

### A defect recurring in the same location on the part across many consecutive cycles
- **Usually means:** a tooling/gate design limitation rather than a process parameter issue.
- **First question:** does the defect location correlate with a specific gate, runner, or weld-line position on the tool?
- **Data to pull:** defect location mapping across recent parts, tool/gate design layout.

### A part passing visual and dimensional inspection but intended for a pressure-critical or structural application with no internal inspection performed
- **Usually means:** internal porosity risk hasn't been checked, and visual/dimensional passing doesn't rule it out.
- **First question:** does this application's criticality require X-ray or equivalent internal inspection, and has it been performed?
- **Data to pull:** the part's application/criticality classification, internal inspection sampling plan and results.

### Cooling time reduced to improve cycle time, verified only immediately after ejection
- **Usually means:** dimensional stability hasn't been confirmed at full room-temperature equilibrium, where warpage from insufficient cooling actually appears.
- **First question:** were parts measured immediately after ejection, or after reaching full room-temperature equilibrium?
- **Data to pull:** dimensional measurements at both immediate-post-ejection and full-cool-down timepoints.

### A parameter adjusted to fix a short shot with no check for flash, or vice versa
- **Usually means:** the fix may have traded one defect for its opposite without verification.
- **First question:** after this adjustment, has the part been checked for the opposite defect mode?
- **Data to pull:** before/after inspection results for both short-shot and flash indicators.

### A new or repaired mold/die put into production without a first-article inspection including required internal checks
- **Usually means:** an assumption that the tool performs identically to its prior validated state, unverified.
- **First question:** has a first-article part from this specific tool state been fully inspected, including internal inspection if the application requires it?
- **Data to pull:** first-article inspection report for this specific tool/repair state.

### Shot sleeve or barrel fill percentage running below its specified minimum
- **Usually means:** a metering or material-delivery inconsistency risking air entrapment during injection.
- **First question:** does current fill percentage meet the process spec's minimum, and is it consistent shot-to-shot?
- **Data to pull:** shot sleeve/barrel fill percentage data, metering/ladle process log.

### A weld line or knit line showing reduced strength at a consistent location, addressed repeatedly through process parameter changes without resolution
- **Usually means:** the weld line's location and severity are set by gate/runner design, which process parameters can only shift within tool-set limits.
- **First question:** has a tooling change (gate location/size) been considered, or has only process parameter adjustment been attempted?
- **Data to pull:** history of process parameter changes attempted for this defect, gate/runner design details.

### Machine cavity pressure sensor data available but not being reviewed as part of routine process monitoring
- **Usually means:** a data source that could catch a machine-set-vs-actual gap isn't being used proactively.
- **First question:** is cavity pressure trend data being reviewed regularly, or only pulled after a defect is already found?
- **Data to pull:** cavity pressure monitoring review frequency/process, recent trend data.

### A quality escape traced back to a process running within all logged machine setpoints
- **Usually means:** the setpoints themselves may not have been sufficient verification, since actual in-cavity/in-part conditions weren't independently confirmed.
- **First question:** was any in-cavity or internal part verification performed during the period the escape occurred, or only machine setpoint monitoring?
- **Data to pull:** the escape's defect type, whether cavity pressure or internal inspection data exists for the affected production window.
