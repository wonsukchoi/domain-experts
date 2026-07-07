# Red flags

Smell tests an operator or a reviewer catches before signing off a shift, dismissing a door-fault log, or letting a headway trend ride. Each entry: what it usually means, the first question a veteran asks, and the data to pull before proceeding.

### Door recycled 3+ times at one stop with no visual/CCTV check of the pocket

**Usually means:** the sensor has already failed once or twice to reopen against whatever is caught (a soft or narrow object below the force threshold), and a third blind cycle is repeating the same test rather than adding safety margin.
**First question:** "Has anyone actually looked at that door pocket, or are we just recycling and hoping?"
**Data to pull:** the door-fault event log for that door and stop, and the CCTV/mirror record (or its absence) for the recycle window.

### A door closes clean with no fault logged, but a rider or bystander reports something caught

**Usually means:** the sensor is working exactly as designed against a soft/thin object below its reopen-force threshold — a clean log is not evidence nothing happened.
**First question:** "What was reported caught, and could its resistance plausibly be under this door's reopen threshold?"
**Data to pull:** the reported description of the object, the door system's certified reopen-force spec, and the recorder/CCTV trace at the moment of closure.

### Gap to the train ahead already at or below the line's ATP minimum separation, and dwell is being shortened anyway

**Usually means:** the operator believes shortening dwell recovers schedule, when forward speed is already capped by the separation floor regardless of dwell length — the shortened dwell buys nothing and adds door-force risk.
**First question:** "What's the actual gap to the train ahead right now, against the minimum separation — not against the scheduled headway?"
**Data to pull:** current headway/gap telemetry to the lead and following train, and the line's published ATP minimum separation value.

### Headway gap to the following train trending toward the minimum-separation floor with no control-center notification

**Usually means:** the operator is treating the delay as a personal schedule problem instead of a system one — the following train will be ATP-limited regardless, and a late notification forces a rolling brake application instead of a controlled upstream hold.
**First question:** "Does control know about this gap yet, and is there still time for them to hold the train behind me upstream instead of braking it in motion?"
**Data to pull:** the current and trending gap to the following train, and the timestamp of any notification sent to the control center.

### ATC/CBTC fault or mode-drop alarm acknowledged with no change in operating speed

**Usually means:** the operator is carrying over the prior ATO/ATP-authorized speed instead of confirming the new mode's restriction — the alarm is being treated as informational rather than as the actual safety-relevant event.
**First question:** "What mode are we in right now, and what's the speed restriction for that mode — not what we were doing thirty seconds ago?"
**Data to pull:** the mode-change timestamp from the onboard log, the recorded speed before and after the alarm, and the agency rulebook's speed table for that mode.

### Curved-platform stop with doors opened and no confirmation the gap filler deployed

**Usually means:** the mechanism's usual reliability is being treated as a guarantee — a gap filler that fails to deploy silently reverts the platform edge to its uncorrected curve geometry.
**First question:** "Was the gap-filler indicator actually checked, or assumed because it usually works?"
**Data to pull:** the gap-filler deployment indicator log for that stop and the platform's documented uncorrected gap dimension.

### Train stopped unscheduled in a tunnel for more than 2–3 minutes with no passenger announcement logged

**Usually means:** the operator is waiting for a definitive update before saying anything, while the silence itself is what pushes passengers toward uncontrolled self-evacuation.
**First question:** "When was the last announcement made, and does the interval since then exceed the standard window?"
**Data to pull:** the PA/intercom announcement log with timestamps and the elapsed time since the stop began.

### Wheel slip/slide event on approach to a platform, with the next stop worked to the same memorized berthing point

**Usually means:** a rail-adhesion condition (moisture, leaves, contamination) at that location hasn't been accounted for before reusing a stopping mark sized for normal adhesion.
**First question:** "What caused the slip/slide, and is today's approach accounting for it or identical to the one that slid?"
**Data to pull:** the wheel slip/slide event log, sanding activation record if equipped, and any track/rail condition reports for that location.

### Short-turn or service adjustment made with no notification to the following crew or control center

**Usually means:** a local decision that changes headway for everyone downstream is being treated as this operator's call alone, instead of a system-level change that the next crew and control need to plan around.
**First question:** "Does the crew behind me and control know this is happening, and when did they find out?"
**Data to pull:** the timestamp of the short-turn/adjustment decision against the timestamp of the notification to control and the following crew.

### Door-force complaint pattern recurring at the same station across multiple shifts

**Usually means:** a station-specific factor (dwell too short for actual ridership volume, a platform pinch point concentrating boarding at one door) is being treated as isolated operator incidents rather than a location pattern needing a schedule or platform-management fix.
**First question:** "How many door-force events have logged at this specific station in the past month, and is the scheduled dwell there realistic for its ridership?"
**Data to pull:** the door-fault log filtered by station, and the scheduled versus actual dwell time at that station over the same period.
