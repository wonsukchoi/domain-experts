# Red flags — what a mechanical design engineer notices instantly

Smell tests with thresholds. Any one can be innocent; two or three together in the same stress report or CAD release is a pattern worth stopping the review for.

### FEA peak stress reported at an unfilleted sharp corner or re-entrant edge
- **Usually means:** the "peak stress" is a mathematical singularity — stress at a true sharp corner in a linear-elastic model is mesh-dependent and grows without bound as the mesh refines, so the number is an artifact, not a physical prediction.
- **First question:** "Does that corner have a fillet in the actual part, and did you re-run the mesh refined at that location to confirm the stress converges instead of climbing?"
- **Data to pull:** the mesh convergence study (2–3 refinement levels) at that specific node, and the CAD model to confirm whether the corner is truly sharp or just coarsely meshed as one.

### Static FEA shows FS > 3 on a part subjected to more than ~10³–10⁴ load cycles over its life, with no fatigue analysis attached
- **Usually means:** the review stopped at the yield check because the number looked comfortable, without running the notch-corrected fatigue check that governs cyclic loading — exactly the gap that let B-104's FS-3.57-on-paper part have an actual fatigue FS of 1.35.
- **First question:** "How many cycles does this part actually see over its service life, and where's the S-N/Goodman check?"
- **Data to pull:** the duty cycle / load spectrum, and the Kt/Kf and Goodman (or Soderberg) calculation at every fillet, hole, or section change in the load path.

### Stress concentration factor (Kt) applied to nominal stress but never converted to a fatigue notch factor (Kf) for a cyclic load case
- **Usually means:** the analyst pulled Kt from a chart and stopped, treating it as directly applicable to fatigue — for ductile, fatigue-loaded metals, using Kt instead of Kf (Kt discounted by notch sensitivity q) systematically overstates the fatigue penalty, which can mask that the analysis skipped the notch-sensitivity step rather than confirm conservatism.
- **First question:** "Is that Kt or Kf on the fatigue side, and where did the notch-sensitivity value come from?"
- **Data to pull:** the notch-sensitivity chart or source used for q, and the material/radius combination it was read at.

### A single factor of safety value quoted with no statement of which limit (yield, ultimate, fatigue-corrected endurance) it was computed against
- **Usually means:** FS is being treated as a single portable number, but FS on yield, FS on ultimate, and FS on fatigue-corrected endurance are different calculations with different denominators — an unqualified "FS = 2" could mean any of them and the reader can't tell if the design actually clears the governing failure mode.
- **First question:** "FS against what — yield, ultimate, or the Goodman-corrected fatigue limit — and is that the failure mode that actually governs this load case?"
- **Data to pull:** the calculation showing the denominator (Sy, Su, or Se-corrected value) used for the quoted FS.

### Provided fillet radius or hole edge condition doesn't match the radius/condition the FEA model (or hand Kt lookup) actually used
- **Usually means:** the analysis ran against an earlier or idealized geometry (often a CAD simplification with sharp corners suppressed to features that don't exist yet) and was never re-checked against the released drawing's actual dimensions.
- **First question:** "What radius did the model or the Kt lookup actually use, and does it match the dimension on the released drawing?"
- **Data to pull:** the CAD model's feature history/simplification log and the released drawing's toleranced radius callout.

### Tolerance on a dimension tighter than ±0.005 in with no stated functional reason
- **Usually means:** the drafter defaulted to a tight tolerance out of caution rather than deriving it from a fit, stack-up, or performance requirement — this forces process capability studies, 100% inspection, or scrap that the design doesn't actually need.
- **First question:** "What function fails if this dimension is a standard ±0.005 in instead — and if nothing does, why is it tighter?"
- **Data to pull:** the tolerance stack-up sheet or fit calculation that the tight tolerance is supposedly protecting.

### A feature (internal corner, undercut, deep blind thread) that requires a process change from the part's baseline manufacturing method, discovered at quote instead of at design review
- **Usually means:** the CAD design closed geometrically without anyone checking it against the target process's tool-access and feature limits — common when design and manufacturing reviews happen sequentially instead of concurrently.
- **First question:** "Was this feature checked against the target process's tool-access limits before the design was released, or is this the first time manufacturing has seen it?"
- **Data to pull:** the DFM review memo (or its absence) and the date of the first manufacturing-engineering touchpoint on this part.

### Worst-case tolerance stack-up run on a 6+ part chain of independently toleranced, high-volume components
- **Usually means:** applying worst-case (arithmetic sum) methodology to a long chain of independently manufactured parts produces a tolerance requirement far tighter than the actual statistical risk, driving unnecessary cost — RSS is the appropriate method once the part count and independence assumptions hold.
- **First question:** "Is this stack safety/interference-critical with a short chain, or a long chain of independent parts where RSS is the standard method?"
- **Data to pull:** the part count in the stack, the independence of each tolerance source, and whether the dimension is safety/function-critical enough to justify worst-case anyway.

### Material substitution proposed (cost or availability driven) with no re-check of the governing failure mode
- **Usually means:** a like-for-like strength comparison (Sy or Su) was used to justify the swap, but fatigue behavior, machinability, and corrosion resistance don't scale the same way between alloys — a substitute with equal or higher static strength can have a materially lower endurance limit or notch sensitivity.
- **First question:** "Does the substitute material's fatigue and machinability data support this swap, or just the static strength number?"
- **Data to pull:** the substitute material's S-N data (or Se′ estimate) and machinability rating, not just its yield/ultimate strength.

### Buckling not checked on a slender or thin-walled compression member with FS quoted only against yield
- **Usually means:** the analysis treated the member as a simple stress problem when its length-to-cross-section ratio puts it at risk of elastic instability (buckling) well below the material's yield stress — yield-only FS is the wrong check for this geometry.
- **First question:** "What's the slenderness ratio here, and has Euler/Johnson buckling been checked separately from the yield check?"
- **Data to pull:** the member's effective length, radius of gyration, and the buckling calculation (or its absence) alongside the yield FS.
