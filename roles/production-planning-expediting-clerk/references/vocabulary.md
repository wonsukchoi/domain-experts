# Production Planning and Expediting Clerk — Vocabulary

### Days-of-supply
On-hand quantity divided by average daily (or weekly) consumption rate, expressed in days of coverage remaining before stockout.
**In use:** "CTL-220 is down to 5 days of supply against a 6-day lead time — that's already past the trigger point."
**Common misuse:** treating days-of-supply as a simple countdown to a problem, rather than comparing it directly against replenishment lead time — the trigger isn't zero, it's the moment supply drops below lead time.

### Pegging
The MRP-system function that traces which specific demand (work order, sales order) a given inventory lot or open PO is allocated to satisfy.
**In use:** "Before I release this PO to another work order, let me check what it's pegged to — someone else might be counting on it."
**Common misuse:** assuming on-hand inventory is "available" without checking whether it's already pegged to a different, higher-priority order.

### Firm order vs. planned order
A firm order is a committed, system-locked purchase or work order that won't move without manual intervention; a planned order is a system-generated suggestion (from MRP logic) that can still shift automatically as inputs change.
**In use:** "That PO is still planned, not firm — don't quote a date off it until purchasing releases it."
**Common misuse:** treating a planned order's suggested date as a confirmed commitment, when the system can silently re-date it overnight based on changed demand.

### Split shipment
Delivering an order in more than one partial shipment rather than a single full-quantity delivery, usually to meet an earlier partial need date.
**In use:** "We can't get all 60 units by Thursday, but the vendor agreed to split-ship 35 by Thursday and the rest the following week."
**Common misuse:** assuming a vendor can split-ship on request — many vendors have minimum shipment quantities or per-shipment fees that make small splits impractical or costly.

### Safety stock / buffer stock
Inventory held above expected demand specifically to absorb variability in lead time or consumption, not part of the "working" quantity needed for normal operations.
**In use:** "We're eating into safety stock now, not just the working inventory — that's the signal to escalate, not wait."
**Common misuse:** treating buffer stock as available inventory for normal allocation, rather than as a reserve that, once tapped, needs replenishment planning of its own.

### Lead time (quoted vs. actual)
Quoted lead time is what a vendor states as standard; actual lead time is what they've historically delivered, which can differ meaningfully, especially under rush conditions.
**In use:** "Their quoted lead time is 12 days, but their actual average on rush orders has been running 15."
**Common misuse:** planning off the quoted lead time without checking the vendor's actual delivered performance, especially for expedited or rush orders where quoted times are often optimistic.

### Work-order traveler
The document (physical or digital) that accompanies a work order through production, recording status, quantities completed, and sign-offs at each stage.
**In use:** "Check the traveler — it should show where in the process this order actually is, not just what the system status field says."
**Common misuse:** relying solely on the system's summary status field instead of the traveler's stage-by-stage detail, missing partial completion or a stalled sub-step.

### Bill of materials (BOM)
The structured list of every component and quantity required to build one unit of a finished item.
**In use:** "Before I chase the vendor for a shortage, let me confirm the BOM quantity-per-unit is actually right — a lot of 'shortages' are BOM errors."
**Common misuse:** assuming a shortage calculated from the BOM is automatically a real supply problem, without first verifying the BOM itself is current and accurate.

### Expedite vs. escalate
Expediting is the operational act of trying to move a specific order faster (through a vendor or internal shop); escalating is the communication act of raising a risk to someone with authority to make a tradeoff decision.
**In use:** "I've already expedited the PO with the vendor — now I need to escalate to the account manager because it still might not make the customer date."
**Common misuse:** using the terms interchangeably, which obscures whether an action (expedite) or a decision (escalate) is actually what's needed next.

### Master production schedule (MPS)
The authoritative, system-of-record schedule of what will be produced, in what quantity, by when — the single source that all downstream planning (material requirements, capacity, shipping commitments) derives from.
**In use:** "Update the MPS the moment the new date is confirmed — every other plan in this building is built off that number."
**Common misuse:** allowing informal or verbal schedule changes to circulate without updating the MPS, so different teams end up planning against different, unofficial versions of the schedule.

### Priority override
A documented, authorized exception that changes the default sequencing rule (e.g., earliest-ship-date-first) for a specific order, made by someone with the authority to make that tradeoff.
**In use:** "Without a documented priority override, I have to release these in ship-date order — I can't just bump one because someone asked nicely."
**Common misuse:** treating an informal request from a persuasive or senior-sounding person as equivalent to an actual authorized override, without documentation.
