# Red flags

Smell tests a fire protection engineer catches in the first pass over a hydraulic calc package, alarm design, or egress plan.

### Sprinkler head design pressure computed below 7 psi

- **Usually means:** the density-derived pressure was used without checking it against the code minimum operating pressure for that sprinkler type.
- **First question:** what does the sprinkler's listing state as its minimum operating pressure, and does the calc actually use the higher of that figure and the density-derived pressure?
- **Data to pull:** the sprinkler's listing/approval data sheet, the density/area calc worksheet showing both figures.

### Hydraulic calc's "most remote area" is the area closest to the riser, not the actual hydraulic worst case

- **Usually means:** the designer picked the geometrically simplest area to calculate rather than running multiple candidate areas and confirming which one actually requires the highest pressure at the riser.
- **First question:** were alternate candidate areas (farthest from riser, highest elevation, smallest pipe runs) checked and ruled out?
- **Data to pull:** the full set of candidate-area calcs considered, not just the one submitted.

### Storage height or commodity classification changed after the sprinkler system was designed, with no re-run hydraulic calc on file

- **Usually means:** a tenant or operational change (rack storage installed, high-piled combustibles introduced) pushed the actual hazard above what the system was designed for, and nobody flagged it to re-run the calc.
- **First question:** what is the current commodity classification and storage height, and does it still match the design-basis hazard classification on file?
- **Data to pull:** current warehouse racking layout/storage height survey, original design-basis hazard classification documentation.

### Hydrant flow test data on file is more than roughly 3-5 years old, or the municipal main has been altered since

- **Usually means:** the water supply the design relied on may no longer reflect actual available pressure/flow — main replacements, new large water users on the same main, or infrastructure degradation can shift the curve materially.
- **First question:** has the municipal water authority made any main changes on this line since the test date, and is a re-test warranted before relying on the old data?
- **Data to pull:** flow test date and source, municipal water authority main-improvement records for the service area.

### Fire pump acceptance/annual test shows churn pressure or 150% flow point outside the NFPA 20 curve requirements

- **Usually means:** pump wear, impeller degradation, or a driver/controller issue is reducing actual output below the rated curve — a pump that "runs" isn't the same as a pump that meets its rated performance envelope.
- **First question:** how does the current test curve compare point-by-point (churn, rated, 150%) to the original acceptance test and the NFPA 20 requirement bands?
- **Data to pull:** current and original acceptance test curves, maintenance/inspection log for the pump and driver.

### Egress width calc uses the sprinklered capacity factor while the sprinkler system has an open impairment, is unmonitored, or covers only part of the floor

- **Usually means:** the egress design assumed a suppression credit that isn't actually in force for the condition being evaluated.
- **First question:** is the sprinkler system fully in service, monitored, and NFPA 13-compliant for the specific area the egress calc covers?
- **Data to pull:** sprinkler system impairment log, monitoring status, as-built coverage drawing for the area in question.

### Common path of travel or dead-end corridor measurement is within roughly 5 ft of the code limit for that occupancy

- **Usually means:** the layout was designed to just clear the limit rather than with margin, and a minor as-built deviation (furniture, a relocated wall) could push it over.
- **First question:** what does the as-built field measurement actually show, versus the drawing dimension used in the code analysis?
- **Data to pull:** as-built field verification, the specific code table and occupancy classification used for the limit.

### Notification appliance candela rating doesn't match the room dimensions on the NFPA 72 spacing table

- **Usually means:** a stock appliance was specified without checking its rated coverage against the actual room size, or a room was resized after the alarm layout was finalized.
- **First question:** what room dimension does the spacing table require for this candela rating, and does the as-drawn room exceed it?
- **Data to pull:** NFPA 72 spacing table for the specific candela rating, current architectural floor plan.

### Standpipe residual pressure at the topmost outlet, per hydraulic calc, is at or below the 100 psi Class I minimum

- **Usually means:** the calc is marginal and any field variance (pipe roughness above design C-factor, an added fitting) could push actual performance below the code minimum.
- **First question:** what safety margin does the calc show above 100 psi, and is it enough to absorb realistic field variance?
- **Data to pull:** full standpipe hydraulic calc with margin stated explicitly, C-factor assumptions used.

### Positive alarm sequence total delay (alarm response + investigation) exceeds roughly 3 minutes

- **Usually means:** the investigation period, response period, or both are configured longer than NFPA 72 permits, delaying general alarm and occupant notification.
- **First question:** what are the configured alarm response and investigation period durations individually, and do they sum within the code-permitted total?
- **Data to pull:** fire alarm control panel programming documentation, the specific NFPA 72 edition's positive alarm sequence timing requirement.

### Fire-rated wall or floor penetration for a sprinkler pipe, conduit, or duct isn't firestopped to the wall's rated assembly

- **Usually means:** the trade that made the penetration didn't coordinate with the firestopping requirement, or firestopping was value-engineered out without re-checking the rated assembly requirement.
- **First question:** does the penetration have a listed firestop system matching the wall/floor's fire-resistance rating, or just field-packed insulation?
- **Data to pull:** UL/Intertek listed firestop system documentation for the specific penetration type and rating, field inspection photos.

### Smoke control system acceptance test shows a stairwell pressurization differential below roughly 0.05 in. w.c. at any tested door

- **Usually means:** fan capacity, leakage path assumptions, or door-opening dynamics differ from the design model — the as-built building doesn't match the modeled leakage.
- **First question:** which specific door/floor failed the differential test, and what does the fan/damper commissioning data show for that zone?
- **Data to pull:** commissioning test report by floor/door, fan and damper as-tested performance data, original smoke-control model assumptions.
