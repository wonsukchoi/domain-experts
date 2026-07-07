# Special Effects Artist/Animator — Vocabulary

### Previz (previsualization)
A rough, low-fidelity pass establishing camera, staging, and blocking before any polished animation work begins.
**In use:** "We're not touching secondary animation until previz is locked — I don't want to build on staging that's still going to change."
**Common misuse:** treated as optional or skippable on tight schedules, when skipping it is exactly what causes expensive structural notes after full animation is underway.

### Blocking
The stage establishing key poses and rough timing for a shot, without polish or secondary motion.
**In use:** "The blocking pass nails the timing of the landing — don't add follow-through yet, get this approved first."
**Common misuse:** confused with a rough draft that doesn't need formal approval, when it's actually the gate that protects downstream polish work from being wasted.

### Rig
The underlying skeletal/control structure that lets an animator pose and move a character or object.
**In use:** "This rig has too many controls for a background shot — we're paying for iteration speed we don't need."
**Common misuse:** assumed that a more complex rig is always better, when rig complexity trades directly against animator iteration speed with no benefit if the shot never shows the detail.

### AOV (arbitrary output variable)
A separate rendered data pass (e.g. diffuse, specular, shadow, depth) that comp combines rather than working from one flattened image.
**In use:** "Comp is missing the shadow AOV — lighting needs to re-render with the full pass list."
**Common misuse:** treated as an optional convenience, when missing AOVs force comp to work from a flattened image that can't be color/light-adjusted without a full re-render.

### Wedge / test render
A low-resolution or reduced-setting render used to test a technical or artistic decision before committing full render-farm time.
**In use:** "Run a wedge at the reduced fur substep count before we commit the farm to the full-resolution version."
**Common misuse:** skipped under schedule pressure, when skipping it is exactly what leads to discovering a costly problem only after the full render has already run.

### Playblast
A fast, low-fidelity preview render used for reviewing motion and timing without waiting for a full render.
**In use:** "Send the director a playblast of both cut options — don't wait for the final render to get a read on which one lands."
**Common misuse:** used as if it shows final quality, when its low fidelity means lighting/texture problems won't be visible in it — it's for timing and staging review only.

### Farm-hours
The total render-farm compute time consumed by a shot, calculated as frames × per-frame render time, independent of how many nodes render it in parallel.
**In use:** "This shot is at 307 farm-hours — on 8 nodes that's 38 wall-clock hours, which blows the deadline."
**Common misuse:** confused with wall-clock time; a shot's farm-hours cost doesn't change when you add nodes, only how fast that fixed cost gets paid off.

### Simulation cache
Precomputed simulation data (fur, cloth, fluid) stored so it doesn't need to be recalculated every time the shot is rendered or reviewed.
**In use:** "The fur cache is stale — it was baked against last week's geometry, before the creature's silhouette changed."
**Common misuse:** assumed to auto-update when upstream geometry changes, when in most pipelines a stale cache silently renders against outdated collision geometry until manually rebaked.

### Lock (picture/shot lock)
The formal point at which a shot's animation or edit is finalized and downstream departments (lighting, comp) begin work assuming it won't change.
**In use:** "The shot is locked — if the director wants a change now, that's a formal reopen, not a quick fix."
**Common misuse:** treated informally, where a "small" post-lock change is requested without acknowledging that lighting and comp are already built against the locked version and now need to redo work.

### The 12 principles of animation
A foundational diagnostic framework (squash/stretch, anticipation, timing, follow-through, arcs, etc.) originating from traditional animation, used to diagnose why a shot's motion doesn't read as believable.
**In use:** "The landing doesn't feel heavy because there's no anticipation — that's a timing problem, not a rig problem."
**Common misuse:** treated as a style guide for a specific look, when it's actually a diagnostic checklist applicable to any motion, stylized or realistic.

### TD (technical director)
A pipeline specialist who solves technical problems (rigging, simulation setup, render configuration) supporting the artists doing creative work.
**In use:** "Route the sim-blowup investigation to the TD — this is a solver-configuration issue, not an animation-quality issue."
**Common misuse:** conflated with the animator role; a TD solves how the tools work, not what the shot should look like.

### Substep (simulation)
The number of sub-calculations a simulation solver performs per frame; higher substep counts increase accuracy and render cost.
**In use:** "Dropping the fur substep count from full to reduced cut render time nearly in half with no visible difference at delivery resolution."
**Common misuse:** assumed that maximum substep count is always required for a "correct" simulation, when the actual requirement is whatever substep count is visually indistinguishable at the shot's delivery viewing distance.

### Reopen
Formally resuming work on a locked shot, with the cost recalculated against every downstream department already building on the locked version.
**In use:** "This isn't a tweak, it's a reopen — lighting and comp both need to redo work that assumed the old version."
**Common misuse:** described informally as a "small fix," obscuring that it triggers a real, calculable cost cascade through every stage after the one being changed.

### Node (render farm)
A single compute unit in a render farm; wall-clock render time for a shot is its total farm-hours divided by the number of nodes allocated to it.
**In use:** "We're on an 8-node allocation for this shot — borrowing nodes from another shot buys us time here at their expense."
**Common misuse:** assumed to be free/interchangeable capacity, when reallocating nodes from one shot to another directly delays whatever that shot was queued to do.
