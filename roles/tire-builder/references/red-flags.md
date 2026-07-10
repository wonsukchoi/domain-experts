# Red flags

### Measured splice overlap (ply or belt) falls outside the specified tolerance range for that tire design
- **Usually means:** a stress-concentration point weaker than the surrounding material, not visible after curing without destructive testing.
- **First question:** what's the actual measured overlap versus the specified tolerance range?
- **Data to pull:** the splice measurement compared against the tire's engineering specification.

### Component stock (calendered ply/belt material) is used past its documented tack/usability window
- **Usually means:** reduced adhesion risking ply separation that manifests only after the tire is already in service.
- **First question:** how long has this stock been sitting since calendering or mixing, versus its usability window?
- **Data to pull:** the stock batch timestamp compared against the tack-window specification.

### A visible air pocket or bubble is detected during ply/belt application, and the build proceeds without correcting it
- **Usually means:** a permanent internal defect that curing will not resolve, risking blistering or separation later.
- **First question:** was the section corrected before proceeding, or left as-is?
- **Data to pull:** build station inspection notes on whether a correction was made.

### Bead tension or position on the building drum is not verified against specification before proceeding
- **Usually means:** risk of improper rim seating or bead separation under inflation or load later.
- **First question:** what does the bead tension/position measurement actually show against spec?
- **Data to pull:** bead tension/position measurement compared against specification.

### A specific defect type recurs across multiple tires traced to the same build station or shift
- **Usually means:** a station-specific process or equipment issue, not a series of unrelated one-off build errors.
- **First question:** does the defect occurrence log show a concentration at one specific station or shift?
- **Data to pull:** the defect occurrence log broken out by build station and shift over a defined period.

### Green tire final inspection is skipped or abbreviated before sending to the curing press
- **Usually means:** a build-stage defect (splice, air pocket, bead issue) proceeds to curing undetected, becoming much harder or impossible to catch afterward.
- **First question:** was the full inspection checklist actually completed for this tire?
- **Data to pull:** the inspection checklist completion record compared against the standard requirement.

### A uniformity or balance defect is found in finished cured tires without tracing back to the specific build station or component batch that produced it
- **Usually means:** the root cause at the build stage goes uncorrected and continues producing similar defects.
- **First question:** what does the build traceability record show for this tire's station, stock batch, and shift?
- **Data to pull:** finished tire uniformity test results compared against build traceability records.
