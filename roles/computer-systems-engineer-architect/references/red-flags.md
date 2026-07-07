# Red flags

### An interface agreed "in the meeting" with no ICD revision issued within 5 business days
- **Usually means:** the two teams have different mental models of the same agreement and won't discover it until integration.
- **First question:** "Which ICD revision number captures this, and who signed it?"
- **Data to pull:** ICD change log; if no entry exists, the agreement isn't real yet.

### A requirement with no verification method entered in the VCRM
- **Usually means:** the requirement is aspirational language that was never operationalized, or ownership of writing the test was dropped between teams.
- **First question:** "How will we know, with a specific test or analysis, that this is met?"
- **Data to pull:** VCRM row for that requirement ID.

### TPM margin below 10% of allocated budget with more than 6 months of design work remaining
- **Usually means:** the subsystem is trending toward a requirements failure that will surface late, when it's expensive to fix.
- **First question:** "What's the trend over the last 3 reviews, not just this one data point?"
- **Data to pull:** TPM tracking chart, last 3 review cycles.

### A build-vs-buy decision documented with only unit cost, no adapter or EOL-risk line item
- **Usually means:** the tradeoff analysis undercounts the COTS option's true integration cost.
- **First question:** "What does the vendor's data sheet say about EOL support, and does that land inside or outside the program's operational life?"
- **Data to pull:** vendor data sheet EOL clause; program operational-life requirement.

### A subsystem team requests a requirements change after their design is >80% complete
- **Usually means:** the original requirement was under-specified, or the team discovered a constraint late — either way, the change is far more likely than an earlier one to break another subsystem's interface.
- **First question:** "Does this change any interface in the N² matrix that another team has already built against?"
- **Data to pull:** current N² diagram; affected ICDs.

### Two subsystems built by different vendors, no single ICD document, only email threads
- **Usually means:** the interface exists only as tribal knowledge distributed across two organizations, guaranteed to diverge at the next personnel change on either side.
- **First question:** "If both engineers who wrote these emails left tomorrow, could a new engineer reconstruct this interface?"
- **Data to pull:** the email thread itself — if it can't be converted into a controlled document in under a day, the interface was never actually agreed, only discussed.

### Integration testing scheduled to start before all interfacing ICDs are frozen
- **Usually means:** schedule pressure pushed integration ahead of design closure; expect integration-phase rework that looks like "bugs" but are actually late-discovered interface disagreements.
- **First question:** "Which ICDs are still in draft, and which subsystems built against the draft version?"
- **Data to pull:** ICD baseline status list vs. integration test schedule.

### A verification test passes against the as-built implementation but no one re-checked it against the original requirement wording
- **Usually means:** the test was written by the subsystem team to prove their own implementation, not derived independently from the requirement — a common way a defect survives verification.
- **First question:** "Read the requirement text and the test procedure side by side — do they say the same thing?"
- **Data to pull:** requirement text (baselined version) and the test procedure document.

### A single subsystem has more than 4 interfaces in the N² matrix and no dedicated interface owner
- **Usually means:** the subsystem has become a de facto integration hub without the staffing to manage it, and interface drift there will cascade to the most other subsystems.
- **First question:** "Who is the one person accountable for every interface this subsystem touches?"
- **Data to pull:** N² matrix row/column count for that subsystem; staffing assignment.

### Program risk register has no entry for vendor end-of-life dates on any COTS component
- **Usually means:** long-life programs (5+ years) haven't cross-checked vendor support commitments against operational life, deferring a real cost to a future program phase where it will look like a surprise.
- **First question:** "For each COTS line item, does its EOL date fall before or after our last planned operational year?"
- **Data to pull:** vendor data sheets; program operational-life requirement.
