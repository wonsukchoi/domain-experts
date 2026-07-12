# Tour Director — Red Flags

### A vendor-chain delay exceeding 60 minutes with no downstream commitment yet re-checked
- **Usually means:** The TD is treating the delay as isolated to the current activity instead of mapping it against every remaining hotel, guide, and meal commitment for the rest of the day.
- **First question:** "Which of today's remaining bookings has a hard time constraint set by someone else — the guide's next job, the restaurant's table turn — and has that constraint actually been checked against the new arrival time?"
- **Data to pull:** Today's remaining vendor bookings with their stated hard constraints; actual versus planned arrival time at the current stop.

### A same-day change is about to cost more than the TD's contracted independent spending authority
- **Usually means:** The situation requires an operator decision (rebooking, comping, canceling a paid vendor), not a TD improvisation, and the ops desk hasn't been called yet.
- **First question:** "Is this decision within my contracted authority, or does it need the ops desk's sign-off before I commit the group to it?"
- **Data to pull:** The operator contract's stated spending-authority threshold; the estimated cost of the change under consideration.

### Per diem or gratuity envelope contents don't match the running log by more than a small, explainable amount
- **Usually means:** A collection or disbursement wasn't logged in real time, or cash was handled without a second person present.
- **First question:** "When was the last point the log and the physical cash matched, and what changed hands since then?"
- **Data to pull:** The per diem/gratuity log; the timestamp and amount of every collection and disbursement since the last confirmed match.

### Rooming list occupancy codes don't sum to the passenger manifest headcount
- **Usually means:** A late cancellation, a couple splitting into singles, or a new booking wasn't reflected in the rooming list before it was sent to the hotel.
- **First question:** "What's the most recent manifest change, and was the rooming list updated after it or before it?"
- **Data to pull:** Manifest change log with timestamps; the version/send-date of the rooming list on file with the hotel.

### A hotel has no matching room block despite a confirmed rooming list and confirmation number
- **Usually means:** A hotel-side overbooking or a block release that happened after confirmation — this is above TD spending authority to fix personally.
- **First question:** "Has the operator's ops desk been called yet, or is a personal card about to be used to guarantee alternate rooms?"
- **Data to pull:** The original confirmation number and date; the hotel's stated reason for the shortfall.

### A step-on or local guide doesn't appear at the confirmed meeting point past 15 minutes
- **Usually means:** A miscommunication on meeting point/time, or a genuine no-show — both need the same immediate fallback regardless of cause.
- **First question:** "Is there a callback number for this guide, and has the fallback content plan already been started while waiting?"
- **Data to pull:** The guide's confirmed contact number; the TD's prepared fallback content for this stop.

### A guest is repeatedly missing scheduled coach departures by more than a few minutes
- **Usually means:** A guest who hasn't internalized the group's schedule discipline, or a mobility/health issue not yet disclosed to the TD.
- **First question:** "Is this a communication gap about departure times, or is there something about this guest's pace or condition that needs a private conversation?"
- **Data to pull:** This guest's departure-lateness pattern across the trip so far; whether a private conversation has already happened.

### An optional excursion is being sold to a guest who has stated a mobility, budget, or interest mismatch with it
- **Usually means:** Commission pressure is overriding the fit judgment the TD would otherwise apply automatically.
- **First question:** "Would this recommendation be the same if there were no commission attached to it?"
- **Data to pull:** The guest's stated preferences or limitations on file; the excursion's physical-demand and pricing details.

### A guest's passport, visa, or required medical document is discovered missing or invalid at a border crossing or check-in
- **Usually means:** A pre-departure document check was skipped or incomplete, or the document expired mid-trip.
- **First question:** "Is a photocopy or digital copy on file, and has the operator's or consulate's stated procedure for this situation been pulled up yet?"
- **Data to pull:** The documents wallet's copy of this guest's travel documents; the operator's stated emergency-document procedure.

### The TD has made three or more unilateral vendor-cost decisions in a single trip without contacting the ops desk
- **Usually means:** Either the TD is exceeding contracted authority repeatedly, or the authority threshold itself is miscalibrated for this route and needs feedback to the operator.
- **First question:** "Were these decisions individually within authority, or is this a pattern worth flagging to the operator regardless?"
- **Data to pull:** A log of each decision's cost and the authority threshold it was measured against.

### A group's visible cohesion or mood drops sharply following a disruption announcement
- **Usually means:** The announcement led with apology or uncertainty instead of what happened and the new plan, or the group senses the TD is improvising rather than executing a plan.
- **First question:** "Did the announcement state the new plan clearly, and was it delivered with the same calm authority as a normal daily briefing?"
- **Data to pull:** What was actually said in the announcement, compared against the disruption-announcement template.
