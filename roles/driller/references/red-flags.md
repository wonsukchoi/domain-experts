# Driller red flags

### Pit gain >2–5 bbl (rig-specific alarm threshold) with pump rate unchanged
- **Usually means:** kick — formation fluid entering the wellbore faster than mud is being displaced; second most likely is an operational addition (mud added to the pits, a pill mixed in) that wasn't logged in real time.
- **First question:** was anything added to or removed from the pits in the last observation window, and is it logged?
- **Data to pull:** pit volume totalizer trend for the last 30 minutes, mud plant addition log, flow-out sensor trace.

### ROP step-change (rule of thumb: >2x recent average) with no WOB/RPM change
- **Usually means:** a drilling break — entering a softer or more permeable/porous zone; second most likely is a genuine lithology change already known from an offset well.
- **First question:** does an offset well in the field show a formation top at this depth?
- **Data to pull:** offset well correlation log, current WOB/RPM/torque trend, flow-check result.

### Standpipe pressure drops at constant pump rate and stroke count
- **Usually means:** washout in the drillstring (worn tool joint, cracked pipe body) reducing flow resistance; second most likely is a nozzle erosion or lost jet in the bit.
- **First question:** did torque or rotating hours on the current BHA change at the same time as the pressure drop?
- **Data to pull:** standpipe pressure trend, torque trend, BHA rotating-hours log since last trip.

### Standpipe pressure rises with no rate, depth, or mud-property change
- **Usually means:** bit balling (clay/cuttings packing the bit face) or a plugged nozzle; second most likely is a restriction building in the string (junk, swelling shale).
- **First question:** has mud rheology (plastic viscosity, yield point) drifted, or is the formation a known balling risk (reactive shale)?
- **Data to pull:** mud property log, cuttings return description, pump pressure vs. depth trend.

### Flow-out continues after pumps are shut down
- **Usually means:** confirmed kick — the well is flowing under its own pressure; there is no credible second cause once pumps are verified off.
- **First question:** are the pumps actually off (not just at idle stroke rate)?
- **Data to pull:** pump stroke counter reading at zero, flow-line visual/sensor confirmation, time stamp for shut-in decision.

### High differential pressure (mud weight well above pore pressure) combined with extended static time in a permeable zone
- **Usually means:** differential sticking risk building — the pipe is being pressed into the wellbore wall by the pressure differential across an exposed permeable interval; second most likely (if pipe is already stuck) is that it has already occurred.
- **First question:** how long has the string been static (not rotating or reciprocating) across this interval, and what's the calculated differential pressure there?
- **Data to pull:** mud weight vs. pore-pressure estimate at the interval, static-time log, hookload trend if a stuck-pipe attempt is already underway.

### Torque trending up over several stands with no BHA or hole-angle change
- **Usually means:** hole cleaning problem (cuttings accumulating, increasing friction) or building tortuosity/dogleg; second most likely is bit or stabilizer wear changing the cutting geometry.
- **First question:** has ROP or flow rate changed recently in a way that would reduce cuttings transport?
- **Data to pull:** torque and hookload trend, flow rate and ROP history, cuttings return volume vs. calculated cuttings generated.

### Gas reading (connection gas or background gas) trending up over several connections then a sharp spike
- **Usually means:** approaching a gas-bearing zone with the current mud weight margin thinning; second most likely is a mud-system contamination unrelated to formation gas (e.g., diesel-based additive).
- **First question:** is the trend gradual (formation approach) or a single spike (localized pocket or contamination)?
- **Data to pull:** gas trend log by connection, mud weight vs. pore-pressure trend at current depth, additive log for the relevant time window.

### Trip tank volume doesn't match calculated pipe displacement while tripping
- **Usually means:** the well is either taking fluid (losses) or giving fluid back (kick) during the trip, not that the trip tank reading is simply imprecise; second most likely is swab/surge effect large enough to matter, if margin is thin.
- **First question:** is the mismatch consistent in one direction across multiple stands, or a single-stand reading error?
- **Data to pull:** trip tank fill/bleed volume per stand vs. calculated steel displacement, pipe speed log for the trip.

### Mechanical specific energy rising while ROP flattens or drops at increasing WOB
- **Usually means:** past the founder point — added weight is going into bit damage, whirl, or balling, not additional rock removal; second most likely is a genuinely harder formation, in which case MSE rises with ROP holding, not dropping.
- **First question:** did ROP actually decline, or just fail to increase proportionally with WOB?
- **Data to pull:** real-time MSE trend, WOB/RPM/ROP trend over the same interval, bit dull-grade history for this bit type in this formation.
