# Red flags

Smell tests worth catching before they show up as a contamination event, a missed pushback, or a GSE-safety incident.

### An adapter or improvised fitting is found connecting a lavatory hose to a potable-water port (or the reverse)
- **Usually means:** worn/damaged dedicated equipment being worked around under time pressure rather than swapped for a spare cart; second most likely, mislabeled or unlabeled equipment after a cart reassignment.
- **First question:** "Why does this connection need an adapter — what's actually preventing the correct coupling from seating?"
- **Data to pull:** GSE inventory/labeling log for the cart in question, maintenance record on coupling wear for that cart, turn-time log for the shift (was the crew behind schedule).

### A periodic water-quality sample comes back total-coliform-positive, especially a repeat positive on the same tail
- **Usually means:** a disinfection/flush cycle was missed or a cross-connection occurred upstream of the sample point; second most likely, sampling technique contamination.
- **First question:** "When was this tail's last documented disinfection flush under the ADWR schedule, and was it on time?"
- **Data to pull:** Aircraft Drinking Water Rule sampling/disinfection log for the tail, servicing log for recent turns, cart assignment history for that gate.

### Potable water service is completed before lavatory/waste service in the same door area on a recurring basis
- **Usually means:** crews defaulting to whichever cart is physically closer rather than the waste-first sequence, most often at gates with tight cart-staging space.
- **First question:** "What determines which cart goes first at this gate — the checklist order, or whichever truck is already in position?"
- **Data to pull:** service-order timestamps from the turn log, gate layout/staging diagram, crew training record on service sequence.

### The same aircraft type or gate slot runs over its lavatory/potable service budget on a recurring basis
- **Usually means:** the budgeted minutes don't match that aircraft's actual panel count or tank capacity, not that the crew is slow; second most likely, a chronic equipment issue (worn couplings, low cart pressure) at that gate.
- **First question:** "Pull the last eight service times for this aircraft type at this gate — clustered around one cause, or spread evenly?"
- **Data to pull:** per-turn service time log, equipment maintenance record for that gate's carts, aircraft-type servicing checklist vs. actual elapsed time.

### GSE is staged or moving within the published clearance distance while the aircraft's anti-collision beacon is on
- **Usually means:** the driver is going by a visual read of engine rotation instead of the beacon signal, or ramp discipline on beacon-status checks has lapsed.
- **First question:** "Was the beacon confirmed off before this equipment approached, and by whom?"
- **Data to pull:** ramp safety audit/observation log, GSE telemetry or dash-cam timestamp if available, beacon-status callout record for that turn.

### A servicing crew is still working near the fuselage/wing when deicing trucks stage or begin application
- **Usually means:** the servicing task ran long and wasn't cleared in time, or the deice crew wasn't told servicing was still in progress.
- **First question:** "Who called clear on this aircraft before deicing started, and what was actually still in progress at that time?"
- **Data to pull:** deicing start-time log, servicing completion timestamp for that tail, ramp coordination radio log.

### An aircraft pushes back with the deicing holdover-time window closing before the ramp's own queue-to-rotation estimate
- **Usually means:** the holdover math wasn't communicated to the flight crew/ramp coordinator before pushback, or the queue-length estimate wasn't checked against the holdover clock at all.
- **First question:** "What was the holdover time posted for this aircraft, and when was it last compared against the queue estimate before pushback?"
- **Data to pull:** deicing application start-time record, HOT table used and fluid type, ramp queue/taxi-time estimate at time of pushback, any pre-takeoff contamination check called.

### Type I fluid alone is used ahead of an extended ground delay rather than as a first-step deicer followed by an anti-icing fluid
- **Usually means:** the two-step deice/anti-ice distinction wasn't applied, most often because the delay wasn't anticipated at the time of treatment.
- **First question:** "Was this treated as a one-step or two-step application, and what was the ground-delay estimate at the time?"
- **Data to pull:** deicing work order/fluid-type log, ATC/ramp delay estimate issued around treatment time, any subsequent re-treatment record.

### Lost or unlogged service-panel closure is found during a post-turn inspection
- **Usually means:** the closure/verification step was skipped under time pressure at the end of a rushed service.
- **First question:** "Walk me through the closure step on this panel — was it checked, or assumed closed because the hose was already disconnected?"
- **Data to pull:** service completion log/checklist for that turn, panel inspection finding, turn-time log for the shift.
