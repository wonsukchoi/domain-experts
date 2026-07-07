# Hotel/Motel Desk Clerk — Red Flags

### Arrivals-vs-availability report shows a shortfall of 2+ rooms before 4pm
- **Usually means:** Standard oversell ratio didn't hold against tonight's actual no-show rate, or a stayover extended unexpectedly.
- **First question:** How many of tonight's expected no-shows have actually materialized so far, compared to the historical rate assumed this morning?
- **Data to pull:** Real-time arrivals-vs-availability report, historical no-show rate for this day-of-week.

### A guest disputes their rate and cites a screenshot or confirmation email different from the PMS
- **Usually means:** A channel-mapping error (OTA promo code, corporate code, or package rate didn't load correctly), not guest error.
- **First question:** What booking channel and rate code does the PMS show for this reservation?
- **Data to pull:** PMS confirmation record, original booking-channel confirmation.

### Housekeeping status shows "in progress" on a room already promised to an arriving guest
- **Usually means:** Turnover is running behind schedule, or the room was pulled for maintenance without the front desk being notified.
- **First question:** What's the actual estimated-ready time from housekeeping, not the scheduled one?
- **Data to pull:** Live housekeeping-status board, maintenance-ticket log for that room.

### A guest requests compensation above standing authority and is already visibly frustrated
- **Usually means:** A prior service failure (not just this interaction) has accumulated, or the guest has status/history that raises the stakes of getting this wrong.
- **First question:** Is this the guest's first contact about this issue, or has it already been raised and not resolved?
- **Data to pull:** Guest profile (loyalty tier, stay history, any prior complaint notes on this stay).

### Two or more walk-eligible guests check in within the same 15-minute window during a confirmed oversell
- **Usually means:** The walk-priority list needs to be applied now, not decided live at the desk under guest pressure.
- **First question:** Has the priority order already been run against tonight's arrival list, or is this the first time it's being applied?
- **Data to pull:** Walk-priority list output, remaining room-shortfall count.

### A guest's stated room request (view, floor, connecting rooms) wasn't noted as "confirmed" at booking
- **Usually means:** It was recorded as a preference, not a guarantee — but the guest may believe it was promised.
- **First question:** Does the reservation record show the request as "confirmed" or just "noted"?
- **Data to pull:** Reservation record's request-confirmation field.

### A walked guest's alternate accommodation is lower-tier or farther away than the original booking
- **Usually means:** The available partner-property inventory at the time of the walk was limited, or the walk wasn't planned ahead of the live situation.
- **First question:** Was a comparable-or-better alternative secured before the walk was disclosed to the guest, or after?
- **Data to pull:** Partner-property availability at time of walk decision, timestamp of alternative-arrangement confirmation.

### The same rate-discrepancy channel-mapping error recurs across multiple reservations in one week
- **Usually means:** A systemic PMS/channel-integration issue, not a one-off booking error.
- **First question:** Do the affected reservations share a common channel or rate-code pattern?
- **Data to pull:** Rate-discrepancy log across the week, channel/rate-code breakdown.

### A guest checks in early (well before standard check-in time) and becomes agitated when no room is ready
- **Usually means:** The gap between "early arrival" and "room ready" wasn't disclosed with a specific time window.
- **First question:** Was a specific ready-by time communicated at check-in, or just "we'll let you know"?
- **Data to pull:** Check-in timestamp, room-ready timestamp, whether luggage-hold was offered.
