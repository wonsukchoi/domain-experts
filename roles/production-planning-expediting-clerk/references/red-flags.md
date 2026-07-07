# Production Planning and Expediting Clerk — Red Flags

### Vendor-promised date has no tracking number 2+ days before it's due
- **Usually means:** the "promise" was a verbal or email assurance from sales, not a confirmed production/ship commitment from the vendor's operations side.
- **First question:** has this vendor's operations team (not sales) confirmed the ship date in writing?
- **Data to pull:** vendor order-confirmation email or portal status, vendor's historical on-time-delivery rate for rush orders specifically.

### Days-of-supply for a component is below its own replenishment lead time
- **Usually means:** an expedite trigger has already been crossed, whether or not the work order shows "late" yet.
- **First question:** is there already an open PO covering the gap, and is its promised date confirmed or just stated?
- **Data to pull:** MRP exception report, open PO status, current on-hand and consumption rate.

### A work order's system status says "on track" but the clerk has verbal knowledge of a delay
- **Usually means:** the system hasn't been updated with the real date, and every downstream planner relying on the system is working from stale information.
- **First question:** has the master schedule been formally updated with the new date, or only discussed informally?
- **Data to pull:** work-order revision history/timestamp of last schedule update vs. when the delay was first known.

### An expedite request doesn't name what capacity is being reallocated
- **Usually means:** the requester wants speed without acknowledging the tradeoff, and the receiving team (vendor or internal shop) has no basis to act cleanly.
- **First question:** what specifically is being deprioritized to make room for this?
- **Data to pull:** current queue/schedule for the resource being asked to expedite, and who has authority to approve bumping another order.

### A shortage shows up for a component that historically never runs short
- **Usually means:** either a genuine demand spike, or a bill-of-materials quantity error, or a data-entry mistake in a recent transaction — not automatically a real supply problem.
- **First question:** does the BOM quantity-per-unit match the engineering spec, and has anything changed recently (BOM revision, unit-of-measure conversion)?
- **Data to pull:** BOM revision history, recent inventory transaction log for the component.

### A single vendor supplies a component with no qualified second source
- **Usually means:** any delay from that vendor has no fallback, and the buffer stock (if any) is the only protection.
- **First question:** what is the current buffer quantity, and how many days of coverage does it represent at current consumption?
- **Data to pull:** safety-stock policy for the part, current on-hand vs. that policy.

### A customer-facing ship date has less than the standard staging buffer remaining and any open shortage exists
- **Usually means:** the standard internal cushion (time between parts-in-hand and ship date, for staging/assembly/test) has already been consumed by the shortage risk.
- **First question:** does the account/customer-facing team know yet, or is this still an internal-only concern?
- **Data to pull:** shop's standard staging-buffer policy (days between parts-complete and ship), current gap calculation.

### An expedite request has been sent to the same vendor three or more times in a quarter
- **Usually means:** either the vendor's baseline lead time is understated in the system, or the buying pattern (order timing/quantity) is structurally causing shortages, not the vendor's fault each time.
- **First question:** is the system's stated lead time for this vendor still accurate, or has it drifted longer without an update?
- **Data to pull:** vendor's actual delivered lead time over the last 6-12 orders vs. the system's stated lead time.

### A schedule slip is being absorbed silently for the second consecutive reporting period
- **Usually means:** float that was meant to be a one-time buffer is being treated as permanent slack, and the real completion date is drifting without anyone officially re-baselining it.
- **First question:** has the master schedule's committed date changed, or is the team just quietly working later each time?
- **Data to pull:** original committed date vs. current actual-completion trend over the last several cycles.
