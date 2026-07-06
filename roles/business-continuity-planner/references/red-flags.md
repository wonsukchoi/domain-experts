### A process's RTO is set equal to (not below) its MTD
- **Usually means:** No margin exists for the recovery process itself to run long, which it commonly does in a real incident — the process will breach MTD if recovery execution takes any longer than the plan assumes.
- **First question:** What margin exists between this process's RTO and its MTD, and is it enough to absorb realistic execution slippage?
- **Data to pull:** BIA-derived MTD, current RTO target, historical variance between planned and actual recovery time in past tests/incidents.

### A continuity plan hasn't been tested within its defined review cycle
- **Usually means:** The plan's actual recovery capability is unverified, regardless of how complete or current the document looks.
- **First question:** When was this plan last tested (tabletop, simulation, or full failover), and has anything material changed (systems, vendors, personnel) since then?
- **Data to pull:** Test history log, plan's last-updated date, list of material changes since the last test.

### A tabletop exercise or DR test produces zero findings
- **Usually means:** More often indicates an insufficiently rigorous or unrealistic scenario than a flawless plan.
- **First question:** How difficult/realistic was the scenario compared to the range of disruptions this process could actually face?
- **Data to pull:** Scenario design documentation, comparison to prior exercises' scenario difficulty and findings count.

### A single vendor, system, or person supports multiple processes labeled "critical"
- **Usually means:** A concentration risk (single point of failure) that's a higher priority than addressing any one dependent process's plan individually.
- **First question:** How many critical processes depend on this single point, and is there a remediation plan for it specifically, separate from the individual process plans?
- **Data to pull:** Dependency map showing all processes relying on this vendor/system/person.

### Current tested recovery capability exceeds a process's MTD
- **Usually means:** A critical, high-priority continuity gap exists regardless of how the process ranks on a general importance scale — this is the specific, actionable metric that should drive prioritization.
- **First question:** What is the size of the gap (tested recovery time minus MTD), and what would it cost, historically or estimated, if that gap isn't closed?
- **Data to pull:** Last test's actual recovery time, MTD, cost-of-downtime curve beyond MTD.

### RTO/RPO targets were set before a business impact analysis was conducted
- **Usually means:** The targets may be arbitrary IT defaults rather than derived from actual business cost-of-downtime data, and may not hold up when tested against real financial or operational impact.
- **First question:** What BIA data (cost-of-downtime curve, MTD) supports the currently stated RTO/RPO for this process?
- **Data to pull:** BIA documentation (or its absence) supporting the stated RTO/RPO.

### A continuity investment proposal doesn't quantify historical or projected exposure from the gap it addresses
- **Usually means:** The cost-benefit case is incomplete — an investment cost without a quantified exposure comparison can't be evaluated on its merits.
- **First question:** What is the quantified historical or projected annual cost of not making this investment (contractual penalties, escalated losses)?
- **Data to pull:** Historical incident/outage records with associated financial impact, BIA cost curve for the affected process.

### A BIA assigns a single severity label (critical/high/medium/low) rather than a cost-by-duration curve
- **Usually means:** The BIA doesn't yet provide enough data to derive a specific, defensible RTO — a label doesn't translate into a recovery time target the way a cost curve does.
- **First question:** Has a cost-of-downtime curve (cost at successive duration intervals) been built for this process, or only a categorical severity rating?
- **Data to pull:** BIA documentation for this process, underlying financial/operational data if available.
