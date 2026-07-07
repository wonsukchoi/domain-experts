# Reservation and Transportation Ticket Agent — Red Flags

### Rebooking option quoted more than 5 minutes ago, not re-searched
- **Usually means:** Fare-class inventory has changed — the quoted seat/fare may already be gone.
- **First question:** "Has this been re-searched right now, or is this from an earlier search?"
- **Data to pull:** Live GDS inventory query timestamp vs. current time.

### Change fee cited from memory rather than the ticket's actual fare-basis code
- **Usually means:** The agent is applying a general or remembered fee instead of the fare rule attached to this specific ticket.
- **First question:** "What is the fare-basis code on this exact ticket, and what does its rule say?"
- **Data to pull:** Fare-basis code and associated restriction/change-fee rule from the ticket record.

### Disruption waiver code applied to a passenger-initiated change
- **Usually means:** A passenger described a voluntary change as involuntary to avoid a fee, and the agent accepted the framing without checking the flight's actual disruption code.
- **First question:** "Does this flight actually carry a disruption code, or is this passenger requesting a voluntary change?"
- **Data to pull:** Flight status/disruption code from operations records.

### Involuntary denied-boarding compensation calculated without checking the arrival-delay tier
- **Usually means:** The agent used a flat percentage without confirming which delay bracket (1–2hr vs 2hr+) the passenger's actual rebooked arrival falls into.
- **First question:** "What is the exact scheduled arrival time of the original flight vs. the rebooked flight?"
- **Data to pull:** Original and rebooked arrival times, delay duration in hours/minutes.

### Boarding-priority list deviated from without a documented protected-tier reason
- **Usually means:** An agent selected an involuntary-denial candidate based on judgment rather than the published list, risking a discrimination complaint.
- **First question:** "Why was this passenger selected instead of the next name on the priority list?"
- **Data to pull:** Boarding-priority list order and the documented reason for any deviation.

### Voluntary-solicitation offer split evenly across multiple volunteers instead of honored per-acceptance
- **Usually means:** The agent misunderstands the auction mechanic — each volunteer is owed the offer live at the moment they accepted, not an averaged amount.
- **First question:** "What offer was live on the board when each volunteer accepted?"
- **Data to pull:** Time-stamped offer log during the solicitation.

### Compensation offered as travel credit without first stating the cash-equivalent amount
- **Usually means:** The agent skipped the required disclosure step — cash/check must be offered and its amount stated before credit can be offered as an alternative.
- **First question:** "Was the passenger told the cash amount before being offered credit?"
- **Data to pull:** Script/notes from the passenger interaction.

### No reservation note logged after a policy exception was granted
- **Usually means:** The next agent or an audit will have no record of why a waiver or exception was applied, risking inconsistent handling on follow-up contact.
- **First question:** "What disruption code, fare basis, or policy reference was cited when this exception was granted?"
- **Data to pull:** Reservation notes/audit trail for the transaction.

### Standby list prioritized by request time at the desk rather than check-in time and tier
- **Usually means:** The agent is running an ad hoc queue instead of the carrier's actual standby-priority rule.
- **First question:** "What check-in time and fare/status tier does each standby passenger have?"
- **Data to pull:** Standby list with check-in timestamps and tier data.
