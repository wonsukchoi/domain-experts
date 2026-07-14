# Red flags

### A solder joint judged acceptable by general appearance without checking against the specific workmanship standard's criteria
- **Usually means:** the joint may pass a personal visual impression while failing the objective standard (wetting angle, fillet coverage) that predicts long-term reliability.
- **First question:** has this joint been inspected under magnification against the specific standard's (IPC-A-610 or equivalent) numeric criteria, or judged by general appearance?
- **Data to pull:** the applicable workmanship standard and class, magnified inspection result if performed.

### A component handled without ESD precautions because the task "seemed" low-risk
- **Usually means:** invisible latent ESD damage could be present, undetectable until the component fails later in service.
- **First question:** was proper ESD grounding/handling procedure followed for this component, regardless of how routine the handling seemed?
- **Data to pull:** ESD control procedure compliance record, component ESD sensitivity classification.

### A crimped connection accepted based on visual appearance alone
- **Usually means:** pull-out force or wire strand damage hasn't actually been verified, and visual inspection doesn't reliably reveal either.
- **First question:** was a pull test or crimp height measurement performed per the sampling plan, or was the crimp accepted by appearance?
- **Data to pull:** crimp specification (height, pull force), test results if performed.

### A suspected cold solder joint or possible ESD exposure treated as a minor note rather than investigated
- **Usually means:** a single defect point that could be the sole cause of eventual complete failure is being treated as statistically diluted by surrounding correct work.
- **First question:** has the suspected joint/component been specifically re-inspected or tested, or was it noted and left as-is?
- **Data to pull:** the specific joint/component location, any follow-up inspection/test performed.

### A field failure traced to a specific solder joint, connector, or component with no root-cause classification (cold joint, ESD, crimp)
- **Usually means:** without classifying the specific failure mechanism, a systemic issue (a process or training gap) may go unaddressed.
- **First question:** does the failure investigation identify whether this was a cold joint, ESD damage, or a crimp/mechanical connection issue?
- **Data to pull:** failure analysis report, the specific defect mechanism identified.

### Multiple units from the same assembly line/shift showing a similar field failure pattern
- **Usually means:** a systematic process issue (a soldering technique problem, a lapsed ESD control point, a crimp tool calibration issue) rather than isolated unit variation.
- **First question:** do the failing units share a common assembly source, and does the failure mode point to a specific process step?
- **Data to pull:** failure traceability by assembly source/shift, common failure mode across units.

### A workmanship standard's criteria not clearly posted/available at the assembly workstation
- **Usually means:** assemblers may be relying on memory or personal judgment rather than the actual documented criteria.
- **First question:** is the applicable workmanship standard reference readily available and referenced during inspection, not just assumed known?
- **Data to pull:** workstation documentation availability, inspection method actually used.

### ESD-sensitive components stored or transported without proper static-safe packaging
- **Usually means:** damage risk exists even before the component reaches the assembly point.
- **First question:** were ESD-sensitive components maintained in static-safe packaging/handling from receipt through assembly?
- **Data to pull:** component handling chain-of-custody, packaging/ESD control at each transfer point.

### A crimping tool or soldering iron used without recent calibration/verification
- **Usually means:** the tool itself may not be producing connections within specification, regardless of operator technique.
- **First question:** when was this tool last calibrated/verified against its specification?
- **Data to pull:** tool calibration log.

### A rework performed on a suspected defective joint without re-verifying against the workmanship standard afterward
- **Usually means:** the rework may not have actually achieved compliance, only visual improvement.
- **First question:** was the reworked joint re-inspected against the standard's specific criteria, or just visually re-checked?
- **Data to pull:** post-rework inspection record.
