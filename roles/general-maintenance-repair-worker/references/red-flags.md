# Red flags

Signals a veteran maintenance tech treats as a stop-and-escalate trigger rather than "try it once more."

### Breaker trips a second time on reset, same visit

**Usually means:** a genuine load fault or a short downstream of the panel, not a nuisance trip — the first trip can be transient, the second confirms the circuit is protecting itself correctly.

**First question:** "What's plugged in or running on this circuit right now, and did anything change on it recently?"

**Data to pull:** circuit map/panel schedule for that breaker, any recent work orders touching devices on the same circuit, breaker amperage rating vs. the load it's carrying.

### GFCI outlet trips more than twice in a week in a wet location

**Usually means:** either normal protective behavior against moisture ingress (fine, replace/reseal) or a ground fault further along the circuit that a device swap won't fix.

**First question:** "Does it trip with nothing plugged in, or only under load from a specific appliance?"

**Data to pull:** which outlets share the circuit, whether the trip correlates with a specific appliance, whether the device has ever been swapped for this same complaint before.

### Water heater TPR valve discharging, or visible bulging/rust weep at the tank seam

**Usually means:** TPR discharge alone can be a simple valve replacement; bulging or seam weep means the tank itself is failing and replacement (not repair) is coming.

**First question:** "Is the water coming from the valve itself or from the tank body?"

**Data to pull:** tank age/install date, last flush date, water pressure reading (high static pressure without an expansion tank is a common root cause of repeated TPR discharge).

### Same symptom on the same unit/asset a third time within 90 days

**Usually means:** the prior two visits patched a symptom without finding root cause — repeating the same fix a third time is choosing to pay for the repair again instead of diagnosing it.

**First question:** "What did the last two work orders on this ticket actually replace or adjust?"

**Data to pull:** full work-order history for the unit/asset, parts used on each prior visit, whether the same tech closed all three.

### PM completion rate below ~85% for two consecutive months

**Usually means:** reactive tickets are consuming the hours budgeted for preventive work, which predicts a rise in emergency-tier tickets roughly one to two quarters out.

**First question:** "Which PM tasks got skipped, and were they skipped for the same reason both months?"

**Data to pull:** CMMS PM-vs-reactive hour split by month, list of specific PM tasks marked incomplete, staffing hours available vs. scheduled.

### Open work-order backlog exceeds roughly 4 weeks of tech-hours

**Usually means:** either understaffing relative to ticket volume or a triage failure letting low-tier tickets sit uncleared while capacity gets consumed by higher-tier work — either way it's a leading indicator, not paperwork debt.

**First question:** "Break the backlog down by hazard tier — is it cosmetic tickets aging, or are safety/compliance tickets actually stuck?"

**Data to pull:** backlog count and age by tier, tech-hours available per week vs. average new-ticket hours per week over the last quarter.

### Tenant reports a gas smell

**Usually means:** an actual gas leak until ruled out — this is never a "check it when you get a chance" ticket regardless of how many false alarms have occurred before.

**First question:** "Is anyone in the unit right now, and has anyone touched a light switch or turned anything on?"

**Data to pull:** none before life-safety response — evacuate, ventilate, do not operate electrical devices, call the gas utility/fire department, then document afterward.

### No-heat ticket open past 24 hours in cold-weather season

**Usually means:** the ticket has already crossed most local habitability-code windows, converting it from a routine repair into a compliance exposure for the property.

**First question:** "How old is this ticket, and has the tenant been offered temporary heat in the meantime?"

**Data to pull:** ticket timestamp vs. local habitability statute's stated response window, outdoor temperature during the open period, whether a temporary heater was offered/logged.

### Structural crack visibly wider than a prior inspection photo (roughly 1/8" growth or more)

**Usually means:** active movement, not a cosmetic settling crack — this is outside general-maintenance scope regardless of how small it looks.

**First question:** "Do we have a dated photo of this crack from the last inspection to compare width against?"

**Data to pull:** prior inspection photos with a scale reference (coin, tape measure), location relative to load-bearing walls or foundation, any recent nearby excavation or water intrusion.

### A job's estimated cost lands right at or just under the state handyman exemption threshold

**Usually means:** either a legitimate small job, or scope creep being mentally sized down to stay "under the line" — the second pattern is how unlicensed work above the real threshold happens.

**First question:** "If this took one more hour or one more part, would it cross the line — and does that change what we're allowed to do?"

**Data to pull:** itemized labor + material estimate, whether the job requires a permit independent of price, the property's state licensing board threshold (not a threshold remembered from a different state).

### Breaker or fuse has been replaced with a higher-amperage unit than the panel schedule specifies

**Usually means:** someone upsized the protection to stop nuisance trips instead of fixing the load — this is a fire-risk finding, not a maintenance convenience.

**First question:** "What's the panel schedule's rated amperage for this breaker, and what's actually installed?"

**Data to pull:** panel schedule/labeling, wire gauge feeding the circuit, date of the last panel service or breaker swap.
