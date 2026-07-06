### Business impact analysis (BIA)
The process of quantifying the operational and financial consequences of a disruption to a business process, typically expressed as a cost-of-downtime curve over increasing outage duration.
**In use:** "The BIA shows losses jump from $15,000/hour to $40,000/hour once we pass the 4-hour mark."
**Common misuse:** Reducing a BIA to a single severity label (critical/high/medium/low) instead of a cost curve that can actually drive a specific RTO/RPO target.

### Recovery time objective (RTO)
The target maximum duration within which a business process must be restored after a disruption, derived from the BIA's cost curve and set with margin below the process's MTD.
**In use:** "RTO for order processing is set at 6 hours — 2 hours of margin below our 8-hour MTD."
**Common misuse:** Setting RTO equal to MTD, leaving no buffer for the recovery process itself to run long.

### Recovery point objective (RPO)
The maximum acceptable amount of data loss, measured in time, that a process can tolerate — determining how frequently data must be backed up or replicated.
**In use:** "An RPO of 15 minutes means we can't tolerate losing more than the last 15 minutes of transactions."
**Common misuse:** Confusing RPO (data loss tolerance) with RTO (downtime tolerance) — they answer different questions and drive different technical requirements (backup frequency vs. failover speed).

### Maximum tolerable downtime (MTD)
The absolute ceiling on how long a process can be unavailable before causing unacceptable contractual, legal, safety, or survival-level consequences.
**In use:** "MTD here is 8 hours — beyond that, our contract lets the customer terminate."
**Common misuse:** Treating MTD as a soft target similar to RTO, rather than the hard external ceiling that RTO must be set meaningfully below.

### Single point of failure (SPOF)
A system, vendor, or individual whose failure would disrupt one or more critical processes, with no redundancy or alternative in place.
**In use:** "This vendor is a SPOF for three different critical processes — that's the real priority, not any one of those processes individually."
**Common misuse:** Assessing dependency risk process by process without checking whether the same underlying dependency shows up across multiple processes, missing the concentration risk.

### Dependency mapping
The process of documenting the systems, vendors, personnel, and facilities that a critical business process relies on to function.
**In use:** "Dependency mapping revealed this process relies on a single approval from one person with no designated backup."
**Common misuse:** Mapping dependencies only at the systems/IT level, missing vendor, personnel, or facility dependencies that are equally capable of causing a disruption.

### Tabletop exercise
A discussion-based simulation of a disruption scenario, walking participants through their planned response without actually executing technical recovery steps.
**In use:** "The tabletop exercise found that nobody knew who had authority to declare a disaster after hours."
**Common misuse:** Treating a tabletop exercise with no findings as evidence the plan is solid, rather than as a signal the scenario wasn't rigorous enough.

### Full failover test
A live test that actually executes the recovery process — failing systems or operations over to a backup site or configuration — to verify recovery capability under real conditions.
**In use:** "The full failover test showed actual recovery took 10 hours, well above our 6-hour target."
**Common misuse:** Relying only on tabletop exercises to validate a plan, without ever conducting a full failover test that can reveal technical execution problems tabletop discussion can't surface.

### Disaster recovery (DR) plan
The technical component of a continuity plan, focused specifically on restoring IT systems and infrastructure after a disruption.
**In use:** "The DR plan covers system failover; the broader continuity plan also covers facilities and personnel continuity."
**Common misuse:** Treating "DR plan" and "business continuity plan" as interchangeable — DR is the IT/infrastructure-focused subset of the broader continuity plan, which also covers people, facilities, and vendor dependencies.

### Cost-of-downtime curve
A quantified model of financial and operational loss as a function of outage duration, typically built in intervals (e.g., hour 1-2, hour 3-4, hour 5-8) rather than as a single flat figure.
**In use:** "The cost-of-downtime curve shows losses accelerate sharply after hour 4 as customers start diverting to competitors."
**Common misuse:** Using a single average cost-per-hour figure instead of a curve, which misses how impact often accelerates non-linearly as an outage extends.
