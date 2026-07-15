# Red flags — what a security manager notices instantly

Smell tests with thresholds. Any single one can be innocent; two or three together are a pattern.

### A security incident response proposing a control on a different layer than the one that actually failed
- **Usually means:** the fix (e.g., more cameras for detection) may not address the actual failure mode (e.g., an access-control gap), leaving the real vulnerability open while spending on the visible, easy-to-approve option.
- **First question:** "What specifically failed — access control, detection, delay, or response — and does the proposed fix address that specific layer?"
- **Data to pull:** the incident's actual entry/access method, which layer (perimeter, access, monitoring, response) the failure traces to.

### Access rights review overdue against stated policy (e.g., quarterly review not conducted in 12+ months)
- **Usually means:** stale access (departed employees, expired contractor badges) is likely accumulating, a common and avoidable vulnerability that isn't caught until an incident or an audit.
- **First question:** "When was the last full access-rights review, and how many stale/unjustified access grants does a current audit find?"
- **Data to pull:** last access review date, current audit of active access grants against current legitimate need.

### A security control that's visibly present but routinely bypassed or worked around by staff
- **Usually means:** security theater — a control providing false confidence while its actual protective value has eroded because people don't comply with it under normal operating pressure.
- **First question:** "Is this control actually followed under normal conditions, or is it routinely propped open, shared, or worked around?"
- **Data to pull:** compliance observation data for the specific control, any documented workaround patterns.

### A generic security checklist applied without a threat model specific to this facility/organization
- **Usually means:** investment may be misallocated — over-invested in irrelevant controls, under-invested in the actual relevant threats for this specific context.
- **First question:** "What are the specific, plausible adversaries and scenarios for this facility, and does the control set map to them?"
- **Data to pull:** the facility/organization's documented threat model (or its absence), the controls currently deployed and their stated rationale.

### An incident response plan that has never been drilled or tested under realistic conditions
- **Usually means:** the plan's actual effectiveness under real time pressure is unknown, and gaps are likely to surface for the first time during an actual incident, when it's too late to fix them calmly.
- **First question:** "When was this plan last tested via a drill or tabletop exercise, and what did that test reveal?"
- **Data to pull:** drill/tabletop exercise history and findings, date of the plan's last update following a test.

### Security investment concentrated entirely on perimeter/access controls with no attention to insider threat or behavioral risk
- **Usually means:** the risk from people who already have legitimate access — often a significant share of real incidents — may be systematically underweighted relative to external-threat-focused controls.
- **First question:** "What controls address risk from people who already have legitimate access, separate from perimeter and access controls?"
- **Data to pull:** background screening and access-review processes, any behavioral risk indicators or insider-threat program in place.

### A single strong control relied upon for the highest-consequence risk with no redundant layer
- **Usually means:** a single point of failure exists for the scenario that matters most — a determined adversary only has to defeat that one control.
- **First question:** "For our highest-consequence risk scenario, is there more than one independent layer of protection, or does everything depend on one control?"
- **Data to pull:** the specific high-consequence scenario, the full list of independent controls protecting against it.

### A proposed control evaluated only on cost and visibility, with no check against deterrence/detection/delay/response contribution
- **Usually means:** the control's actual security value hasn't been assessed against its real function, risking investment in something that looks reassuring but doesn't meaningfully raise attacker cost or improve detection.
- **First question:** "Which of deterrence, detection, delay, or response does this control actually contribute to, and how much?"
- **Data to pull:** the proposed control's stated purpose and mechanism, an honest assessment against the four functions.
