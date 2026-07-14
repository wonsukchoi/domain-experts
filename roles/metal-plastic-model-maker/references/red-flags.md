# Red flags

### A prototype successfully machined to a spec that would be difficult or impossible for the intended production process
- **Usually means:** the prototype's fabrication flexibility may be masking a real production feasibility problem.
- **First question:** has this specific feature/dimension been checked against the actual intended production process's constraints (molding, casting, stamping), not just confirmed achievable by the prototype's own method?
- **Data to pull:** the feature's specification, production process guidelines (e.g., resin flow-length data, minimum draft/wall thickness for the process).

### A design signed off based on a prototype's successful fit/function test without a production feasibility check
- **Usually means:** the sign-off may be based on validation the prototype's fabrication method provided, not validation of actual manufacturability.
- **First question:** has anyone confirmed the design's features are achievable by the intended production process, separate from the prototype's success?
- **Data to pull:** production feasibility review record if one exists, prototype fabrication method vs. production process.

### A critical dimension on a one-off prototype accepted without direct measurement
- **Usually means:** an assumption based on the fabrication method's typical capability, rather than actual verification on this specific piece.
- **First question:** was this dimension directly measured on the actual piece, or assumed based on the machine/process's general capability?
- **Data to pull:** dimensional verification record for this specific critical feature.

### A prototype built in a substitute material used to validate functional performance (strength, flex, thermal behavior)
- **Usually means:** the substitute material's different mechanical properties may not represent the final production material's actual behavior.
- **First question:** does the substitute material's relevant mechanical property (strength, flex modulus, thermal expansion) match the final production material closely enough for this specific test?
- **Data to pull:** substitute material properties vs. final production material properties, what specific validation was performed.

### A multi-revision model with no documentation of which areas reflect which revision
- **Usually means:** the physical model may be an undocumented hybrid of different design revisions.
- **First question:** does a revision map exist showing which specific features/areas were updated at which revision?
- **Data to pull:** the model's revision history/documentation, visual inspection of feature consistency.

### A tooling master or check fixture built to a generic "model quality" tolerance rather than the specific downstream tooling process's requirement
- **Usually means:** the model's accuracy may not actually match what the tooling process needs.
- **First question:** what tolerance does the specific downstream tooling process require, and does this model meet it?
- **Data to pull:** the downstream tooling process's tolerance requirement, the model's actual measured accuracy.

### A design feature validated by a prototype but rejected or requiring costly rework once actual production tooling is quoted/built
- **Usually means:** the prototype didn't adequately represent production process constraints before the design was locked.
- **First question:** could this issue have been caught by checking production process feasibility before or during prototype validation?
- **Data to pull:** the specific feature that caused the tooling issue, whether a feasibility check was performed on the prototype.

### A model or prototype delivered without specifying what it does and doesn't validate (form, fit, function, production feasibility)
- **Usually means:** the receiving team may misinterpret the model's scope, treating a form/fit validation as also confirming function or manufacturability.
- **First question:** does the delivery documentation clearly state the model's validated scope?
- **Data to pull:** delivery notes/documentation accompanying the model.

### A prototype's fabrication method achieving a geometry (undercut, thin wall, sharp internal corner) without checking if the intended production process can replicate it
- **Usually means:** a specific, checkable feasibility gap that a general "looks fine" review would miss.
- **First question:** has this specific geometric feature been checked against the production process's known limitations?
- **Data to pull:** the feature's geometry, the production process's documented limitations for that feature type.

### A rework/revision performed on a model without updating its documentation before it's used again for a design decision
- **Usually means:** the model's current physical state may not match its documented state, risking a decision made on outdated information.
- **First question:** does the model's documentation reflect the most recent rework, or is it lagging behind the physical part?
- **Data to pull:** documentation timestamp vs. last physical rework timestamp.
