# Production Planning and Expediting Clerk — Playbook

## Shortage-triage worksheet (filled example)

| Component | On-hand | Needed | Shortfall | Open PO qty | Vendor-promised date | Shop needed-by date | Gap (days) | Priority |
|---|---|---|---|---|---|---|---|---|
| CTL-220 (PCB) | 18 | 50 | 32 | 60 | Day 9 | Day 8 | -1 | High — negative gap |
| BRK-045 (bracket) | 210 | 50 | 0 | — | — | Day 8 | +9999 (covered) | None |
| FAN-112 (cooling fan) | 40 | 50 | 10 | 25 | Day 6 | Day 8 | +2 | Low — buffer intact |
| CBL-330 (harness) | 0 | 50 | 50 | 0 | Not yet ordered | Day 8 | Unordered | Critical — no PO exists |

Gap = vendor-promised (or expected) date minus shop needed-by date. Negative gap means the promised date is later than the plan can absorb; that is the priority column regardless of shortfall size — a small shortfall with a large negative gap is worse than a large shortfall with a positive gap.

## Expedite-request template (filled)

**To:** Vendor purchasing contact
**Subject:** Expedite request — PO #4482-B, CTL-220, split shipment needed

We have an open PO (#4482-B, 60 units of CTL-220) with a promised ship date of day 9. Our production need-by date for a partial quantity is day 7. Requesting:

- Split shipment: first 35 units by day 7 (tracking number required, not just a promise)
- Remaining 25 units on the original day-9 date

If day 7 isn't achievable for any quantity, please confirm the earliest date you can ship at least 32 units, and we'll assess alternate coverage. This is a customer-committed ship date on our end (day 10); a further slip on your side has direct downstream cost to us.

## Vendor-confirmation-tracking log (filled example)

| Vendor | PO # | Original lead time | Promised date | Confirmation type | Tracking # | Status |
|---|---|---|---|---|---|---|
| Acme PCB Co. | 4482-B | 12 business days | Day 9 (rush) | Verbal/email, unconfirmed by carrier | — | Escalated day 3, split-ship requested |
| Acme PCB Co. | 4482-B (split) | — | Day 7 | Confirmed, carrier scan received | 1Z9A4...7X | On track |
| Meridian Fasteners | 4471-A | 5 business days | Day 6 | Confirmed, carrier scan received | 7Q2C...9K | On track |

Confirmation type matters more than the date itself: "verbal/email, unconfirmed" carries the vendor's historical on-time-delivery rate as its real confidence level, not 100%. Only a carrier scan / tracking number moves a date from "promised" to "confirmed" for planning purposes.

## Escalation-threshold table

| Slip size | Ship-date-facing? | Action |
|---|---|---|
| < 1 day | No | Absorb in existing float, no notification |
| < 1 day | Yes, within buffer | Log internally, no external notification |
| 1-2 days | No | Internal notification to supervisor only |
| 1-2 days | Yes | Notify account/customer-facing team same day |
| > 2 days | Either | Escalate immediately with cause and revised date; do not wait for end-of-shift report |

## Days-of-supply calculation

Days-of-supply = on-hand quantity ÷ average daily consumption rate.
Reorder/expedite trigger = days-of-supply < remaining lead time to replenish.

Example: on-hand 40 units, average daily consumption 8 units/day → 5 days of supply. If replenishment lead time is 6 business days, the component is already inside the expedite-trigger zone — the order should have gone out, or should go out today, not when the shelf visibly empties.
