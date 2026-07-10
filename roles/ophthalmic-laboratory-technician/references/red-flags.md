# Red flags

### Finished lens accepted based on sphere/cylinder power match alone without checking axis against the job ticket
- **Usually means:** an axis error large enough to matter, especially at higher cylinder powers where tolerance is tighter.
- **First question:** what's the axis tolerance appropriate to this specific cylinder power?
- **Data to pull:** measured axis versus ticket axis versus the tolerance table for this cylinder power.

### Prescribed prism not detected on lensometer check at the intended optical center point
- **Usually means:** either the prism wasn't ground in, or the optical center is mispositioned relative to where it should be measured.
- **First question:** does the lensometer reading at the intended check point actually show the ticket-specified prism?
- **Data to pull:** lensometer prism reading compared against the ticket-specified prism and check point.

### Lens decentered to the frame's geometric center rather than the wearer's measured PD
- **Usually means:** unintended induced prism for that specific wearer, even though the lens's own power specifications check out fine.
- **First question:** what decentration point was actually used versus the wearer's measured monocular PD?
- **Data to pull:** the decentration point used compared against the wearer's measured PD.

### Lens is edged before a lensometer check is performed and passed
- **Usually means:** any grinding error — power, axis, or prism — becomes unrecoverable from that blank, requiring an expensive new-blank redo.
- **First question:** what does the operation sequence log show — lensometer check timestamp versus edging timestamp?
- **Data to pull:** the sequence-of-operations log for that job.

### Base curve selected without reference to the prescription's power range
- **Usually means:** avoidable off-axis optical aberration for higher-power prescriptions where base curve selection actually matters.
- **First question:** what base curve was used versus what the lab's selection chart specifies for this power range?
- **Data to pull:** the base curve used compared against the lab's base curve selection chart for this power range.

### A specific job type or power range shows a recurring pattern of axis/prism rejections at lensometer check
- **Usually means:** a systemic surfacing or grinding calibration issue for that specific parameter range, not isolated operator errors.
- **First question:** does the rejection log show a concentration in one power range or parameter?
- **Data to pull:** the rejection log broken out by power range and parameter over a defined period.

### Wearer-reported symptoms (eyestrain, distortion) after dispensing trace back to a lens that passed lensometer check but at the edge of the acceptable tolerance range
- **Usually means:** the tolerance being applied is a manufacturing standard, not a guarantee of zero perceptible effect for every wearer, especially for prism-sensitive individuals.
- **First question:** where in the acceptable range did this specific lens's measured values actually fall?
- **Data to pull:** lensometer check values compared against the tolerance range and the wearer's complaint details.
