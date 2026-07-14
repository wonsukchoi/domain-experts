# Vocabulary

### Form, fit, and function
A three-way classification of what a prototype validates: form (shape/appearance), fit (whether it physically mates with other components), and function (whether it performs its intended mechanical/operational role) — a prototype can validate some of these without validating all.
**In use:** "This aluminum prototype confirms form and fit — function testing needs a prototype in the actual production resin, since aluminum behaves completely differently under load."
**Common misuse:** Treating successful testing on any one of form, fit, or function as confirming all three — a substitute-material prototype in particular can pass fit and even a basic function test while still not representing how the final production material will actually perform.

### Production feasibility (of a prototype feature)
Whether a design feature achievable by a prototype's one-off fabrication method (machining, hand-fitting) is also achievable by the intended mass-production process (injection molding, casting, stamping).
**In use:** "The prototype machined this undercut fine, but we're checking whether the actual mold tool can achieve it without an expensive side-action."
**Common misuse:** Assuming a feature's successful prototype fabrication confirms it's production-feasible — one-off fabrication methods are typically far more flexible than mass-production processes, and a feature achievable one way isn't automatically achievable the other.

### Side-action (tooling)
An additional mechanism in an injection mold or die that moves independently of the main opening/closing action, required to form an undercut or other feature that can't be released by a simple straight pull.
**In use:** "That undercut needs a side-action — that's a real cost and complexity addition the machined prototype didn't reveal."
**Common misuse:** Assuming any geometric feature achievable in a prototype translates to a simple, low-cost tooling solution — features requiring side-actions carry meaningful additional tooling cost and complexity that isn't apparent from the prototype's own fabrication ease.

### Flow length (injection molding)
The distance molten plastic must travel from the injection point to fill a mold cavity, which determines the minimum wall thickness needed for reliable, complete fill without short shots.
**In use:** "This part's flow length calls for a minimum sixty-thousandths wall — the spec's forty is going to risk short shots in actual production."
**Common misuse:** Specifying or validating a wall thickness based on structural or visual requirements alone without checking it against the resin's flow-length guideline for the part's actual size and geometry — a wall that's structurally fine can still be too thin to reliably fill during actual molding.

### One-off fabrication (no process capability data)
Manufacturing a single part or small quantity using flexible, general-purpose methods (machining, hand-fitting) rather than a repeatable, statistically characterized production process.
**In use:** "There's no process capability data for a one-off part like this — we're measuring every critical dimension directly, not trusting an assumed tolerance."
**Common misuse:** Assuming a one-off fabrication method's typical or nominal capability applies to a specific piece without direct verification — without a production run's worth of statistical data behind it, each critical dimension on a one-off part needs its own direct check.

### Tooling master
A precisely made model or part serving as the reference geometry from which production tooling (molds, dies, fixtures) is built or verified, requiring a tolerance discipline matched to that tooling process's actual requirements.
**In use:** "This isn't a design-review model — it's the tooling master, so it needs to hit the tolerance the moldmaker actually requires, not a general 'looks right' standard."
**Common misuse:** Building a tooling master to a generic model-quality standard rather than the specific tolerance the downstream tooling process requires — different tooling processes have different accuracy needs, and a mismatch here propagates into every part made from that tooling.

### Revision tracking (prototype/model)
Documentation identifying which specific design revision each feature or area of a physical model reflects, especially important for models reworked or updated multiple times.
**In use:** "This model's been through three revisions — the mounting boss is rev C, but the rest of the body is still rev B, and that's documented, not just assumed."
**Common misuse:** Treating a reworked model as uniformly reflecting its most recent revision without verifying and documenting which specific areas were actually updated — ad hoc rework can leave a model as an undocumented hybrid of different design states.

### Check fixture
A precision tool used to verify that production parts conform to their design specification, requiring its own accuracy standard distinct from a prototype or appearance model.
**In use:** "Check fixture needs to be more accurate than the tolerance it's verifying — that's a different standard than we'd use for a display model."
**Common misuse:** Building a check fixture to the same tolerance as the parts it's meant to verify, rather than a tighter tolerance appropriate for a measurement tool — a fixture's own accuracy needs headroom above what it's checking, or its measurements aren't trustworthy.

### Substitute material (prototyping)
A material used to fabricate a prototype that differs from the specified final production material, often chosen for prototyping convenience (machinability, cost, availability) rather than matching production mechanical properties.
**In use:** "We're prototyping in aluminum for machinability, but that's a substitute material — it doesn't tell us anything about how the actual production plastic will perform under load."
**Common misuse:** Treating a substitute-material prototype's successful testing as representative of final production material performance — mechanical properties (strength, flex, thermal behavior) can differ substantially between a substitute and the final material, limiting what the prototype can actually validate.
