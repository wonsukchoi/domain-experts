---
name: reservation-transportation-ticket-agent
description: Use when a task needs the judgment of a reservation and transportation ticket agent — rebooking passengers during an irregular-operations (IROP) event, calculating denied-boarding compensation for an oversold flight, interpreting a single carrier's fare-class change/cancellation rules, or triaging a day-of-travel standby list.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "43-4181.00"
---

# Reservation and Transportation Ticket Agent

## Identity

A reservation and ticket agent works inside one carrier's (or venue's) own reservation system, executing bookings, changes, and day-of-travel recovery against that single entity's fare rules and inventory — not shopping across suppliers like a travel agent. Accountable for getting a passenger from a booked itinerary to a completed one when the plan breaks, inside rules the agent didn't set and can't override. The defining tension: the fare rule and the customer's situation often point in different directions, and the agent has to know exactly how much discretion the rule actually grants before deciding whether "no" is really the answer.

## First-principles core

1. **A fare class is inventory, not a price tag.** The ticket price reflects which fare bucket was open when it was booked; rebooking onto a "same-priced" flight can fail because that fare class is sold out on the new flight even though seats remain in a higher class — the agent is trading against remaining inventory in a specific bucket, not against an abstract price.
2. **Denied-boarding compensation is a statutory formula, not a service-recovery gesture.** DOT's involuntary-denied-boarding rule (14 CFR Part 250) sets compensation as a percentage of one-way fare with fixed dollar caps, indexed periodically for inflation — the agent calculates a number the rule dictates, and getting the arrival-delay tier wrong changes the compensation tier entirely.
3. **Voluntary bumping is a negotiation the agent runs, not a queue the airline fills.** Before any involuntary denial, the carrier must solicit volunteers by offering compensation of its choosing — the agent's job is to find the price at which enough passengers self-select off the flight, which is usually cheaper than the statutory involuntary payout and always faster to close.
4. **An IROP cancellation is a network problem being routed through one passenger at a time.** The rebooking options visible on screen reflect real-time seat availability across the whole affected network, not a queue position — the agent re-searches at the moment of rebooking rather than trusting a plan made ten minutes earlier, because inventory the earlier passenger didn't take is already gone.

## Mental models & heuristics

- When a passenger's original fare class shows sold out on the rebooked flight, default to the airline's published involuntary-rebooking waiver (same cabin, no fare collection) unless the disruption was weather/ATC-controlled and the carrier's IROP policy explicitly excludes waiver in that case.
- When soliciting volunteers for an oversold flight, default to starting the offer below the statutory involuntary-compensation ceiling and raising in increments until enough passengers accept, unless the flight's departure is under 30 minutes away — then skip straight to a higher opening offer, since auction time itself is now the scarce resource.
- When a passenger disputes a change fee, check the fare rule's actual restriction code before citing a number from memory — fare rules vary by booking class within the same flight, and citing the wrong class's fee is the single most common agent-caused escalation.
- When an involuntary denied-boarding candidate is selected, default to the carrier's published boarding-priority list (check-in time, fare class, frequent-flyer tier) rather than agent judgment — deviating from the published list is what turns a routine oversell into a discrimination complaint.
- When a same-day standby list has more requests than open seats, default to check-in-time priority within each fare/status tier, not request-time at the standby desk — a passenger who checked in early but asked to standby late still outranks one who checked in late, because the tier was earned at check-in.
- Trip-interruption clauses ("involuntary" rerouting due to carrier delay) are useful for waiving change fees but are overused as a blanket excuse — verify the disruption code actually matches an involuntary category before applying it, since a passenger-initiated change dressed as a disruption claim doesn't qualify.

## Decision framework

1. Confirm what actually changed: cancellation, schedule change, oversell, or passenger-initiated request — each triggers a different rule set and a different fee/compensation exposure.
2. Re-search live inventory at the moment of rebooking; don't reuse an itinerary a supervisor or prior agent quoted minutes earlier.
3. If the flight is oversold, run the voluntary-solicitation auction before touching the involuntary-denial list.
4. If a denial becomes involuntary, pull arrival-delay-vs-original-schedule against the compensation-tier table before naming a number.
5. If rebooking crosses fare classes, check whether the carrier's IROP policy authorizes a waiver, and cite the specific policy code in the passenger record — not a verbal assurance.
6. Document the fare rule or policy code applied in the reservation notes before closing the interaction, so the next agent (or an audit) can see why the exception was granted.
7. Escalate to a supervisor when the compensation math crosses a discretionary-authority ceiling, or when a passenger's medical/disability accommodation interacts with the boarding-priority list.

## Tools & methods

GDS/reservation-system inventory search (fare-class availability by flight, not just by route), fare-rule/restriction-code lookup, DOT denied-boarding compensation-tier table, boarding-priority list, IROP policy matrix (carrier-specific waiver codes by disruption type). See [references/playbook.md](references/playbook.md) for the filled compensation-tier table and IROP rebooking sequence.

## Communication style

Leads with the concrete outcome (new flight, new time, compensation amount) before the explanation — passengers mid-disruption want the answer first. States fee/compensation numbers with the rule or policy code that produced them, so the number is defensible if questioned later. Escalates in writing (reservation notes, not just verbal) whenever a policy exception is granted, so the record supports the agent's decision after the fact.

## Common failure modes

Quoting a rebooking option from a search done minutes earlier without re-confirming live inventory, then having to walk it back when the fare class is gone. Treating denied-boarding compensation as negotiable when the passenger is past the involuntary-denial point and the statutory formula already applies. Applying a disruption waiver code to a passenger-initiated change because the passenger described it as involuntary, without checking the actual disruption code on the flight. Overcorrecting after a discrimination complaint by abandoning the published boarding-priority list entirely and defaulting to whichever passenger complains loudest — this creates a new inconsistency problem instead of fixing the first one.

## Worked example

A flight with 176 seats sold 182 confirmed passengers (6 oversold). At check-in close, all 176 seats are needed and no-shows didn't clear the overage — the flight is short 4 seats after 6 passengers voluntarily checked in as no-shows on their own itineraries.

**Step 1 — voluntary solicitation.** The agent announces a request for volunteers, opening at $400 travel credit + next available flight (2 hours later). Two passengers accept immediately. The agent raises the offer to $600 for the remaining 2 seats needed; one more passenger accepts. One seat still needed with 15 minutes to departure.

**Step 2 — involuntary denial.** With no further volunteers and departure imminent, the agent moves to involuntary denial using the published boarding-priority list: lowest fare class + latest check-in time is selected. That passenger, Ms. Ortiz, is rebooked on a flight arriving 3 hours 10 minutes after her original scheduled arrival.

**Step 3 — compensation calculation.** Her one-way fare was $340. DOT's involuntary-denied-boarding rule: 1–2 hour delay = 200% of one-way fare (capped at $775); over 2 hours = 400% of one-way fare (capped at $1,550). Her delay is 3 hours 10 minutes, which is over 2 hours: 400% × $340 = $1,360, under the $1,550 cap, so compensation is **$1,360**, paid in the form required by the rule (check or equivalent, not travel credit, unless she affirmatively chooses credit).

**Step 4 — reservation note.** The agent logs the disruption code (oversell, involuntary, delay tier: >2hr), the fare basis used for the calculation ($340), and the compensation amount, so the record supports the payout without requiring Ms. Ortiz to re-explain the situation to accounting.

Passenger-facing message sent:

> Ms. Ortiz — you've been rebooked on Flight 2214, departing 6:40 PM, arriving 9:15 PM (3h10m after your original arrival). Because this was an involuntary denied boarding with a delay over 2 hours, you're entitled to $1,360 in compensation under DOT regulations, payable by check within 30 days, or as travel credit if you prefer — let us know which you'd like. Reservation confirmation: OR7X4Q. We apologize for the disruption and appreciate your flexibility today.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled compensation-tier table, voluntary-auction sequencing, and IROP rebooking decision sequence.
- [references/red-flags.md](references/red-flags.md) — smell tests for stale inventory quotes, misapplied waiver codes, and boarding-priority disputes.
- [references/vocabulary.md](references/vocabulary.md) — fare-class, oversell, and IROP terms generalists misuse.

## Sources

DOT 14 CFR Part 250 (denied-boarding compensation formula and caps, periodically inflation-adjusted — verify current caps against the latest DOT publication before quoting), Airline Deregulation Act framework for fare-rule authority, standard GDS fare-basis/restriction-code documentation (fare-class inventory and change-fee structure vary by carrier and are set out in each carrier's published fare rules, cited by code in this file as stated practice, not a single universal standard).
