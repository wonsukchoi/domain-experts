# Red flags

### Hole diameter measuring outside the drawing's tolerance band
- **Usually means:** drill wander from a worn or missing guide bushing, or a drill bit run past its service life; second most likely is a measurement error from an uncalibrated or misread gauge.
- **First question:** was a guide bushing used, and is the measuring gauge within its calibration date?
- **Data to pull:** the drawing's exact tolerance callout, the gauge's calibration record, the drill bushing's condition/service log.

### Fastener not reaching full seat or specified torque within a normal number of turns
- **Usually means:** hole elongation or debris preventing proper seating, or a mismatched fastener/hole size.
- **First question:** does the hole measure within tolerance when checked with a go/no-go gauge?
- **Data to pull:** hole diameter measurement, fastener part number against the drawing callout, torque wrench reading history for that joint.

### Torque wrench calibration sticker past its due date
- **Usually means:** the tool was overlooked in the recalibration cycle, or it was pulled back into service after a repair without recertification.
- **First question:** how many fasteners were torqued with this tool since its last valid calibration?
- **Data to pull:** tool calibration log, list of work orders/serial numbers where this tool was used since the last valid date.

### Dropped hardware (rivet, washer, drill shaving) inside a structure not yet closed out
- **Usually means:** normal handling loss during the operation — the concern isn't the cause, it's confirming the item's location before the structure closes.
- **First question:** has the item been physically recovered, or does a tool/hardware count confirm it's accounted for?
- **Data to pull:** tool and hardware accountability count for the operation, area search log.

### Work instruction revision not matching the engineering drawing's current revision block
- **Usually means:** a drawing change was released without the derived work instruction being updated, or the workstation is running from a cached/printed copy.
- **First question:** what does the drawing's revision block show right now versus what the work instruction cites?
- **Data to pull:** drawing revision history, work instruction revision date, engineering change order (ECO) log for the affected drawing.

### Sealant or bonding operation performed outside its certified cure temperature/humidity range
- **Usually means:** ambient shop conditions drifted outside spec during cure, or the operation was scheduled without checking the environmental log.
- **First question:** what were the actual recorded temperature and humidity during the cure window?
- **Data to pull:** shop environmental monitoring log for the cure period, sealant manufacturer's certified cure range.

### A matched-drilled part being substituted from stock after final drilling has already occurred elsewhere on the assembly
- **Usually means:** a part was pulled from general stock without recognizing it carries a unique final-drilled hole pattern tied to a specific mating assembly.
- **First question:** does this part's serial/traceability tag confirm it was final-drilled as part of this specific assembly?
- **Data to pull:** part traceability tag/serial number, matched-drilling record for the assembly.

### An oversize fastener installed without a documented nonconformance report
- **Usually means:** a field decision was made to "fit" the joint without routing the deviation through MRB.
- **First question:** does a nonconformance report exist for this hole, and does it match the fastener actually installed?
- **Data to pull:** nonconformance report log for the part/serial number, the installed fastener's part number against the drawing's approved repair options.

### A close-out inspection buy-off missing or signed out of sequence
- **Usually means:** the structure was closed before the required in-process inspection was completed, or the paperwork was backfilled after the fact.
- **First question:** does the timestamp on the buy-off precede or follow the structure's physical close-out?
- **Data to pull:** traveler/work order sign-off timestamps, inspection stamp records.

### Two consecutive nonconformances on the same drawing feature across different assemblies
- **Usually means:** a tooling or fixture problem (worn bushing, miscalibrated drill jig) affecting every unit run through it, not an isolated operator error.
- **First question:** were both nonconformances produced using the same tool, fixture, or bushing?
- **Data to pull:** tooling/fixture usage log for both units, nonconformance report details for both events.
