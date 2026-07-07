# Commercial/Industrial Designer — Red Flags

### Wall thickness below process minimum (e.g., <1.0mm in general-purpose ABS)
- **Usually means:** the geometry was modeled for aesthetics or a CAD-convenience reason without checking the target resin's flow-length-to-wall-thickness ratio; second most likely is a late feature squeeze (adding a snap-fit or rib) that thinned an adjacent wall without re-checking.
- **First question:** "What resin and process are we tooling for, and what's its minimum recommended wall thickness at this flow length?"
- **Data to pull:** the resin datasheet's flow-length/wall-thickness guidance and the current CAD wall-thickness analysis (most CAD packages have a built-in thickness-check tool).

### Draft angle at or near 0° on a vertical face
- **Usually means:** the part was modeled as a pure extrusion without applying draft, often because the designer modeled from a 2D profile and forgot the manufacturing step; less commonly, a genuine functional reason (a mating flat face) that needs a side-action to resolve.
- **First question:** "Is this face functional-flat, or can it take standard draft?"
- **Data to pull:** the DFM checklist's draft-angle line item and a mold-flow or ejection simulation if available.

### Single "recommended" material presented with no alternatives shown
- **Usually means:** the recommendation was reverse-engineered from a preferred aesthetic or a supplier relationship rather than from a load-case-driven index comparison; less commonly, time pressure skipped the shortlist step entirely.
- **First question:** "What's the dominant load case, and what index did we rank against?"
- **Data to pull:** the material-selection matrix (see artifacts.md) — if it doesn't exist, that's the finding.

### Full-fidelity prototype requested before any targeted mockup exists
- **Usually means:** stakeholder pressure wants "something to show" rather than an answer to a specific open question; less commonly, a genuinely single-question design where full fidelity is the fastest path.
- **First question:** "What's the one riskiest question this prototype needs to answer?"
- **Data to pull:** the list of open design questions and which ones a lower-fidelity mockup could answer for a fraction of the cost/time.

### Tooling quote requested before a DFM pass has been documented
- **Usually means:** schedule pressure is skipping the DFM gate to hit a tooling-order deadline; the cost of skipping shows up later as a first-shot mold correction, which is far more expensive than a design-stage fix.
- **First question:** "Has manufacturing engineering signed off on this geometry?"
- **Data to pull:** the DFM checklist disposition (see artifacts.md) and whether every flag has a resolution, not just an acknowledgment.

### Anthropometric fit range not stated anywhere in the design brief
- **Usually means:** the design defaulted to the designer's own body dimensions or a single "average" figure without an explicit percentile decision; this surfaces later as a usability complaint from users outside the unstated range.
- **First question:** "What percentile range are we designing to, and for which population dataset?"
- **Data to pull:** the design brief's stated fit range, or absence of one.

### Volume forecast used for the tooling decision has no downside case
- **Usually means:** the breakeven analysis was run only against the optimistic sales forecast; if the process choice flips at a realistic downside volume, that's a decision the client needs to see, not one made silently on their behalf.
- **First question:** "What does the breakeven recommendation look like at 50% of forecast?"
- **Data to pull:** the tooling cost-breakeven worksheet re-run at a downside volume.

### Client change request arrives after tooling is cut
- **Usually means:** either a genuine late-discovered functional issue, or scope drift that should have been caught in an earlier design-freeze gate; the cost consequence (tool rework vs. new tool) needs to be quoted before agreeing to the change, not after.
- **First question:** "Is this a functional necessity or a preference change, and what does it cost against the existing tool?"
- **Data to pull:** the tool-modification cost quote from the mold shop versus a new-tool quote, to bound the decision.

### Snap-fit or living-hinge feature specified without a deflection-force calculation
- **Usually means:** the geometry was sized by visual proportion rather than by calculating the actual deflection force against a human-actuation range; this either fails in the field (too weak) or frustrates users (too stiff).
- **First question:** "What's the calculated actuation force, and does it fall in the 20-40N one-handed range?"
- **Data to pull:** the beam-deflection calculation for the snap-fit geometry against the material's flexural modulus.
