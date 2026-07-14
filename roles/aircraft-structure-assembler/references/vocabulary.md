# Vocabulary

### Nonconformance report (NCR)
A documented record of a part or process deviating from its engineering drawing or specification, routed for engineering/MRB disposition rather than resolved in the field.
**In use:** "That hole's 0.003 over max allowable — I'm writing an NCR, not just grabbing a bigger bolt."
**Common misuse:** Treating an NCR as paperwork overhead for a problem already solved by a field fix — the report and the disposition have to happen *before* the fix is applied, not as a record of what was already done.

### Material Review Board (MRB)
The cross-functional authority (typically engineering, quality, and manufacturing) that dispositions a nonconformance — use-as-is, repair, rework, or scrap — with the authority to approve deviations from the drawing.
**In use:** "MRB dispositioned it as a bushing repair, not a straight oversize bolt — that's what we're installing."
**Common misuse:** Assuming any technician with enough experience can informally "MRB" a decision on the shop floor — disposition authority is a defined role in the quality system, not a function of seniority or confidence.

### Matched drilling
A process where mating structural parts are drilled to final hole size together, in place, so the resulting hole pattern is unique to that specific assembly's fit-up.
**In use:** "These two skins were matched-drilled together — you can't pull a replacement skin from stock and expect the holes to line up."
**Common misuse:** Assuming any two parts with the same part number are interchangeable — a matched-drilled part's holes are unique to the specific unit it was drilled with, regardless of part number.

### FOD (Foreign Object Debris)
Any object or material not intended to be part of the finished structure or system — a dropped fastener, a drill shaving, a tool — left inside an assembly.
**In use:** "We stop everything and do a FOD count before that panel gets closed up — no exceptions for size."
**Common misuse:** Treating small or "obviously harmless" debris as not worth a stop-work check — FOD risk is about what an object can do once the aircraft is in service (jam a mechanism, short a circuit), not its size at the time it's dropped.

### Fay-surface sealant
Sealant applied between two mating surfaces before they're joined, primarily for corrosion prevention and, on some structure, fuel-tank sealing — distinct from a fillet seal applied after joining.
**In use:** "This skin gets fay-sealed before the rivets go in, not sealed around the edge afterward."
**Common misuse:** Substituting a fillet seal (applied after assembly) for a fay-surface seal (applied before) because the visual result looks similar — the two serve different functions and one can't be substituted for the other on a drawing that specifies fay-surface application.

### Interference fit
A fastener or bushing installed with a slightly larger diameter than its mating hole, requiring press-fitting, which creates a controlled clamping stress distinct from a simple clearance fit.
**In use:** "The repair bushing needs 0.0005 to 0.0015 interference — too loose and it won't transfer load properly, too tight and you risk cracking the hole."
**Common misuse:** Treating "tight fit" and "interference fit" as the same thing — interference fit is a specified dimensional range with an engineering purpose (load transfer, fatigue performance), not just a qualitative sense that a part went in snugly.

### Edge distance
The minimum distance from the center of a fastener hole to the nearest edge of the material, specified to prevent the material from tearing out under load.
**In use:** "Going to the next oversize bolt changes our edge distance margin — we need to re-check it, not just assume it's still fine."
**Common misuse:** Assuming edge distance requirements scale automatically with fastener size changes without re-verification — a repair that changes fastener diameter can silently violate an edge distance requirement that was fine for the original size.

### Torque preload
The clamping force generated in a bolted joint by tightening a fastener to a specified torque value, which the joint's fatigue-life and load-transfer calculations assume.
**In use:** "That fastener's torqued to spec, so we know it's carrying the preload the stress analysis assumed — a fastener that just 'looks tight' tells us nothing."
**Common misuse:** Equating visual tightness or "feel" with correct preload — torque, tool calibration, and friction conditions all affect the actual preload achieved, and none of that is visible by inspection alone.

### Traveler
The document (paper or electronic) that accompanies a part or assembly through each manufacturing and inspection step, recording who performed and who verified each operation.
**In use:** "Check the traveler before you start — station 6's buy-off isn't signed yet, so this part isn't cleared to move to riveting."
**Common misuse:** Signing a traveler step out of sequence (backfilling a buy-off after the physical work has already moved on) — the traveler's value as a traceability record depends on the sign-off actually reflecting when the inspection occurred.

### Basis of design
The engineering drawing (and its current revision) that constitutes the certified, authoritative specification for a part — distinct from any derived document (work instruction, router) that translates it for shop-floor use.
**In use:** "The work instruction says one thing, but the drawing's basis of design is what's certified — we stop and get the work instruction corrected, not the other way around."
**Common misuse:** Treating a work instruction as equally authoritative to the drawing it was derived from — work instructions can lag behind a drawing revision, and when they conflict, the drawing governs.
