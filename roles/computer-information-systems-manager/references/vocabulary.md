# IT management working vocabulary

Terms an IT manager uses precisely. Format: definition → how a practitioner says it → common misuse.

**Total cost of ownership (TCO)** — The full cost of a system or vendor decision over its useful life: acquisition/licensing, implementation, migration, integration, support, training, and eventual replacement/exit cost — as opposed to acquisition price alone.
In use: "The new platform's license is cheaper, but TCO including migration and retraining pushes the real payback past 4 years."
Misuse: comparing vendor options on license price or implementation quote alone, missing migration, training, and future exit costs that can dominate the real total.

**Vendor lock-in (switching cost / exit cost)** — The real cost of leaving a vendor or platform once adopted — data migration, retraining, integration rework, contractual penalties — that should be estimated at decision time, not discovered only when trying to leave.
In use: "This platform's proprietary export format means our exit cost in three years would look a lot like today's migration cost — that's part of the decision, not a future surprise."
Misuse: evaluating a platform decision without pricing what it would cost to leave it later, treating lock-in as an unforeseeable future problem rather than a quantifiable cost of the decision now.

**Technical debt** — The accumulated cost of deferred system upgrades, shortcuts, or unaddressed gaps, framed as debt because it accrues an ongoing cost (increased maintenance burden, risk, slower future work) the longer it's carried.
In use: "We're carrying about $400K of estimated technical debt in the legacy billing system — deferring the migration another year adds real interest, not just delay."
Misuse: treating technical debt as a vague, unquantified complaint ("the code is messy") rather than a specific, estimated backlog with remediation cost and business risk attached.

**Risk register (security risk register)** — A tracked list of identified risks (often security vulnerabilities) with likelihood, business impact, and an accountable owner for the accept/remediate/mitigate decision — translating technical findings into business-decision terms.
In use: "This CVE is on the risk register at medium likelihood, high impact — flagged for the CISO's risk-acceptance review this week."
Misuse: keeping vulnerabilities in a purely technical tracker (severity score only) with no business-impact translation or named decision-owner, which lets risk-acceptance happen by default inaction instead of deliberate choice.

**Recovery time objective (RTO) / Recovery point objective (RPO)** — RTO is the maximum acceptable time to restore a system after an outage; RPO is the maximum acceptable amount of data loss, measured in time (e.g., "last 15 minutes of data" for a 15-minute RPO). Both should be set per system based on actual business impact, not uniformly.
In use: "This system's RTO is 4 hours and RPO is 15 minutes — the payment system next to it has a 15-minute RTO and near-zero RPO because the cost of downtime is completely different."
Misuse: applying the same RTO/RPO targets across all systems regardless of their actual criticality, wasting investment on low-stakes systems while under-protecting genuinely critical ones.

**Build vs. buy** — The decision framework for whether to custom-develop a capability internally or purchase/use an existing commercial or open-source solution, ideally driven by whether the capability is core to competitive differentiation.
In use: "This workflow tool is undifferentiated for us — clear buy decision, saving engineering capacity for the parts of the product that are actually core."
Misuse: defaulting to "build" because it's more engaging for the team, or defaulting to "buy" reflexively, without checking whether the specific capability is actually core to the business's differentiation.

**ITIL (IT Infrastructure Library)** — A widely used framework of IT service management practices (incident management, change management, problem management) providing standardized processes for running IT as a service function.
In use: "We follow ITIL change-management practice — no production change without a documented, approved change record."
Misuse: adopting ITIL terminology without the underlying discipline (e.g., calling something a "change record" without an actual approval and rollback process behind it).

**Shadow IT** — Technology systems or tools adopted and used within the organization without formal IT oversight, approval, or security review — often arising because an official process was too slow or a business unit's need wasn't met by sanctioned tools.
In use: "We found a business unit running an unapproved cloud database with customer data — that's shadow IT, and it's now a security and compliance gap we have to remediate."
Misuse: treating shadow IT purely as a compliance violation to shut down, without investigating why the business unit went around the official process — often a signal that sanctioned tooling isn't meeting a real need.

**Change management (IT context)** — The formal process of proposing, reviewing, approving, and documenting changes to production systems, designed to reduce the risk of an unreviewed change causing an outage or security issue.
In use: "This deployment needs to go through change management — we need the rollback plan documented before it's approved for the production window."
Misuse: treating change management as a bureaucratic formality to route around under time pressure, rather than the actual control that catches a large share of preventable outages before they happen.

**Business continuity plan (BCP) vs. disaster recovery (DR) plan** — BCP covers how the whole business keeps operating during a disruption (people, processes, alternate locations); DR is the narrower technical plan for restoring IT systems and data specifically — DR is a component of BCP, not a synonym for it.
In use: "Our DR plan covers restoring the ERP system within its RTO; the broader BCP also covers how the finance team keeps processing payments manually in the meantime."
Misuse: using "DR plan" and "business continuity plan" interchangeably, which can leave non-IT operational continuity unplanned if only the technical restoration piece was addressed.
