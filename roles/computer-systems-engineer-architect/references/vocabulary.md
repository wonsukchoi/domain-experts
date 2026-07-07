# Vocabulary

### Baseline
A formally agreed, version-controlled set of requirements or design artifacts that can only be changed through a defined change-control process.
**In use:** "That interface isn't in the baseline yet — it's still a trade study, don't build against it."
**Common misuse:** Treating any written-down requirement as "baselined." A document isn't a baseline until it's gone through the formal review and sign-off that makes changing it require a process, not an edit.

### Allocation
The act of assigning a portion of a top-level requirement (mass, power, latency budget) down to a specific subsystem.
**In use:** "The 15ms end-to-end latency budget allocates as 8ms to the SDR front end, 4ms to the network, 3ms margin."
**Common misuse:** Allocating a budget without tracking the margin — allocation is only useful if someone is watching whether the subsystem is trending inside or outside its slice.

### Verification vs. validation
Verification proves the system was built to the requirements ("did we build it right"); validation proves the requirements were the right ones ("did we build the right thing").
**In use:** "This test verifies SYS-014; it doesn't validate that 40Mbps was ever the number the customer actually needed."
**Common misuse:** Using the two terms interchangeably. A system can pass every verification test and still fail validation if the requirements themselves were wrong.

### Interface control document (ICD)
The controlled document defining a boundary between two subsystems — physical, logical, and timing characteristics, plus fault behavior.
**In use:** "Freeze the ICD before either team starts detailed design, or we're building against a moving target."
**Common misuse:** Writing an ICD that only covers the happy path and omits fault behavior (what each side does on loss-of-signal or malformed data) — the fault-behavior section is usually where integration bugs live.

### N² diagram
A matrix representation of every subsystem-pair interface, used to make interface count and complexity visible rather than assumed.
**In use:** "We're at 6 subsystems now — pull up the N² diagram before anyone tells me integration is simple."
**Common misuse:** Building the diagram once at kickoff and never updating it as subsystems are added or interfaces change.

### Technical performance measure (TPM)
A small number of tracked parameters (mass, power, latency) whose margin erosion over time predicts a requirements failure before it happens.
**In use:** "Power draw's margin dropped to 6% this review — that's a TPM trend, not a data point, escalate it."
**Common misuse:** Tracking TPMs as a single snapshot rather than a trend across reviews — the trend is what predicts failure, not any one measurement.

### Trade study
A structured comparison of two or more design options against weighted criteria, producing a documented recommendation, not an informal preference.
**In use:** "The trade study came back $60K in favor of COTS on unit cost, but the program risk plan overrides it on schedule risk."
**Common misuse:** Running a trade study only on cost when the deciding factor is actually schedule or reliability risk — the criteria weighting should be set before the numbers come in, not after.

### Requirements traceability
The documented, bidirectional link from a top-level requirement down through allocation to a verification result.
**In use:** "Pull the traceability chain on SYS-031 — which subsystem requirement does it decompose to, and what's the test evidence?"
**Common misuse:** One-directional traceability (requirement to test) without the reverse link (test result back to the exact requirement wording), which makes it impossible to audit what a passing test actually proves.

### Build vs. buy (total cost of integration)
The decision to develop a subsystem in-house versus procure a commercial-off-the-shelf (COTS) component, evaluated on total integration cost, not unit price.
**In use:** "COTS wins on unit cost, but once you add the adapter layer and the vendor's EOL risk, in-house is only $60K more."
**Common misuse:** Comparing unit costs directly without pricing the adapter/wrapper engineering and vendor support-lifecycle risk that COTS options often carry.

### Margin
The gap between a TPM's current estimate and its allocated budget, expressed as a percentage of the budget.
**In use:** "8% margin on mass with 6 months left in design — that's inside the escalation threshold."
**Common misuse:** Reporting margin as an absolute number (kg, watts) instead of as a percentage of the allocated budget, which makes it impossible to compare urgency across TPMs with different units.

### End-of-life (EOL) risk
The risk that a vendor-supplied component will be discontinued before the program's operational life ends, forcing a redesign.
**In use:** "Vendor's EOL commitment is 3 years; our operational life is 8 — that's a real, deferred cost even though it's not in this year's budget."
**Common misuse:** Ignoring EOL risk entirely in a build-vs-buy comparison because it doesn't show up as a line item until years later, when it resurfaces as an unplanned redesign.

### Functional flow block diagram (FFBD)
A diagram showing the sequential and logical relationships of system functions, used before interface diagrams to establish what the system does, in what order.
**In use:** "Draw the FFBD before the N² diagram — you can't map interfaces between functions you haven't sequenced yet."
**Common misuse:** Skipping straight to interface diagrams without first establishing the functional sequence, which produces an interface map with no rationale for why those functions interact.
