# Red flags & diagnostics

Signals an experienced lodging manager notices instantly. Load this when triaging a revenue, overbooking, or service question — not for general reasoning (that's `SKILL.md`).

### A rate cut is proposed to boost occupancy without a RevPAR projection
- **Usually means:** the decision is being evaluated on occupancy alone, and the rate reduction may cost more in ADR than it gains in occupancy
- **First question:** "What's the projected occupancy response to this rate change, and does the resulting RevPAR beat the current RevPAR?"
- **Data to pull:** current ADR/occupancy/RevPAR, historical rate elasticity for comparable rate moves

### Overbooking level exceeds the historical no-show rate for that specific day-of-week/season
- **Usually means:** the policy is based on a flat/generic overbooking percentage rather than this date's actual expected no-show count
- **First question:** "What's the historical no-show rate specifically for this day-of-week and season, and does the overbooking amount match it or exceed it?"
- **Data to pull:** historical no-show/cancellation data segmented by day-of-week and season, current bookings-on-the-books

### Channel mix decisions are being reported/compared by gross ADR only
- **Usually means:** commission cost isn't being netted out, understating the relative value of lower-commission channels (direct, corporate/GDS)
- **First question:** "What's the net rate after commission for each channel, not just the gross ADR?"
- **Data to pull:** channel-by-channel gross rate, commission percentage, and calculated net rate

### Housekeeping/front-desk schedule was built from a template rather than current booking pace
- **Usually means:** staffing will likely mismatch actual occupancy on both slow and peak days within the scheduling period
- **First question:** "What's the current occupancy forecast for the days this schedule covers, and when was the schedule last checked against it?"
- **Data to pull:** rolling occupancy forecast (bookings + pickup curve) vs. the staffing schedule's assumed occupancy

### A group block request is being evaluated on group rate alone
- **Usually means:** displacement cost against forecast transient demand for the same dates hasn't been calculated
- **First question:** "What's the forecast transient ADR and demand for these specific dates, and how does the group rate compare after accounting for displaced transient room-nights?"
- **Data to pull:** booking pace and forecast transient ADR for the requested dates

### A walked guest's compensation was decided ad hoc rather than from a pre-defined protocol
- **Usually means:** the property doesn't have a walk-guest recovery protocol ready, or front-desk staff don't have clear authority to act without escalation delay
- **First question:** "Was there a pre-defined relocation and compensation plan in place before this walk happened, and did front desk have authority to execute it immediately?"
- **Data to pull:** the walk-guest protocol documentation and the actual timeline of the recovery response

### RevPAR is declining while occupancy is flat or rising
- **Usually means:** ADR is being eroded, often through discounting, channel mix shift toward higher-commission OTAs, or unauthorized rate overrides
- **First question:** "Is the RevPAR decline coming from rate erosion, channel mix shift, or something else — and where specifically?"
- **Data to pull:** ADR trend by channel, rate override log, channel mix trend over the same period
