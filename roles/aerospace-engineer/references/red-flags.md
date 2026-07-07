# Red flags

### Margin of safety reported as exactly 0.00 with no load-case citation
- **Usually means:** the analyst hit the target and stopped, or copied a prior iteration's number without re-running it against the current load update.
- **First question:** "Which load case and which knockdown factors produced this number, and when was it last re-run?"
- **Data to pull:** the FEM run log and load-case revision history for the component.

### Subsystem weight contingency at 0 lb before Critical Design Review
- **Usually means:** the subsystem is absorbing growth from a requirements change or a late design decision without escalating it.
- **First question:** "Is this growth traced to a specific decision, or is it undifferentiated creep?"
- **Data to pull:** the subsystem weight-budget tracker with delta history by review milestone.

### A requirement verified "by analysis" that the certification basis lists as needing test
- **Usually means:** schedule pressure substituted a cheaper verification method without DER concurrence.
- **First question:** "Has the DER or certification authority concurred with analysis-only verification for this requirement?"
- **Data to pull:** the means-of-compliance matrix and DER correspondence log.

### Weight-saving claims summed as percentages across multiple knockdown factors
- **Usually means:** the analyst added knockdown reductions instead of multiplying them, overstating effective allowable.
- **First question:** "Walk me through the knockdown stack — is each factor applied multiplicatively to the running allowable?"
- **Data to pull:** the margin-of-safety calculation sheet showing each knockdown step.

### A special condition or novel-system requirement with no negotiated means of compliance past 50% program schedule
- **Usually means:** a novel technology (electric propulsion, autonomy, new material) was assumed certifiable without early regulator engagement.
- **First question:** "When was this last discussed with the certification authority, and is there a means-of-compliance proposal on file?"
- **Data to pull:** the certification basis document and correspondence log with the authority.

### Static test article margin quoted to answer a fatigue or flutter question
- **Usually means:** a static-test-cleared margin is being treated as if it also clears a life-cycle or dynamic-stability requirement it wasn't tested for.
- **First question:** "Was this margin from the static test article, or from the fatigue/flutter test program?"
- **Data to pull:** the test program matrix mapping each test article to the requirements it verifies.

### Program-level fuel-burn guarantee margin consumed >70% before flight test begins
- **Usually means:** empty-weight growth is on the historical trajectory that continues through flight test, and the guarantee is now at risk.
- **First question:** "What's the remaining margin, and what's this program class's historical flight-test-phase growth rate?"
- **Data to pull:** the weight-and-balance tracker trend and the customer guarantee contract terms.

### A DER sign-off requested with less than 2 weeks before a hardware freeze milestone
- **Usually means:** the finding of compliance was treated as a formality rather than a review that can generate rework.
- **First question:** "What's the DER's typical turnaround for a finding of this complexity, and is there schedule float if it comes back with findings?"
- **Data to pull:** the DER review request log and program schedule float on the affected milestone.

### A component redesigned to fix one margin shortfall without rechecking adjacent load paths
- **Usually means:** local reinforcement changed load distribution into neighboring structure that hasn't been re-analyzed.
- **First question:** "Has the load redistribution from this change been re-run through the adjacent stations' FEM?"
- **Data to pull:** the FEM model revision and the list of stations downstream of the change in the load path.
