# Red flags

Smell tests a journeyman or foreman catches before the first switch is thrown or the first ground is applied. Each entry: what it usually means, the first question a veteran asks, and the data to pull before proceeding.

### Switching order marks a circuit "open" but no voltage test has been logged at the work location

**Usually means:** the crew is treating dispatcher confirmation as proof of zero energy — the most common precursor to contact incidents on circuits with backfeed potential (customer generators, adjacent-circuit ties) or a misidentified device.
**First question:** "Who tested for absence of voltage at this exact work location, with what instrument, and is it in the job briefing record?"
**Data to pull:** the job briefing form's voltage-test entry, the tester's calibration/rating for this voltage class, and the switching order's device list cross-checked against what's physically at the work location.

### Grounds applied at only one point on a de-energized section longer than a single span

**Usually means:** the work position is not actually bracketed, leaving an unprotected span if an induced or backfed fault occurs between the ground point and the work location.
**First question:** "Where is the work position relative to every ground set on this section, and is it bracketed on both sides?"
**Data to pull:** the grounding plan diagram, span lengths between ground sets and the work position, and the circuit's induction-exposure history (parallel transmission, double-circuit structures).

### Ground set rating unknown or assumed "standard" for the circuit

**Usually means:** nobody has checked the ground set's rated fault-current capacity against this circuit's actual available fault current — an undersized set can fail before upstream protection clears.
**First question:** "What's this circuit's available fault current, and what's this ground set rated for?"
**Data to pull:** the circuit's fault-current study or protective-device coordination study; the ground set's ASTM F855 rating plate.

### PPE category selected from voltage class alone, with no incident-energy study cited

**Usually means:** someone is pattern-matching PPE to voltage the way MAD is keyed to voltage, but incident energy depends on fault current and clearing time, not voltage alone — the same voltage class can require different PPE categories at different points on the system.
**First question:** "What's the incident-energy value at this specific work position, and from what study or table?"
**Data to pull:** the position-specific incident-energy calculation or arc-flash study, upstream protective-device clearing time, and the date the study was last updated against current settings.

### Crew reports "we always do it this way" when asked about a grounding or switching step

**Usually means:** procedural drift has set in on a familiar circuit or job type — the step being skipped is usually the one that "never mattered" until the one time the circuit's actual state didn't match assumptions.
**First question:** "Walk me through this step as if it were a circuit you'd never worked before — what would you check?"
**Data to pull:** the crew's job briefing records for this circuit over the past several jobs, checking whether the same step is consistently abbreviated.

### Storm restoration crews dispatched in the order outage tickets arrived

**Usually means:** dispatch is optimizing for visible responsiveness to individual callers rather than total customer-hours of outage, which restores far fewer customers per crew-hour than topology-based sequencing.
**First question:** "Where does this ticket sit on the system relative to the substation and feeder — and is a higher-ratio segment still waiting?"
**Data to pull:** outage management system topology view, customers-affected-per-segment counts, and crew-hours-to-repair estimates for every open segment, not just the ticket in front of the dispatcher.

### Mutual-aid crew dispatched without a documented briefing on host-utility grounding/PPE procedure

**Usually means:** time pressure during a large event is skipping the step that reconciles a visiting crew's home procedures with the host system's — a documented pattern in multi-utility storm response incidents.
**First question:** "Has this crew been briefed on our grounding sequence and PPE standard, specifically, not just given a work order?"
**Data to pull:** the mutual-aid intake/briefing checklist, the visiting crew's home-utility procedure documentation, and confirmation of which set of procedures governs on this system.

### Crew has been on shift beyond roughly 16 hours and is assigned a new energized or grounding task

**Usually means:** fatigue-driven procedural shortcuts are statistically more likely from this point forward, regardless of the crew's stated confidence.
**First question:** "How long has this crew actually been working, including drive time and the prior shift, and who's next in rotation?"
**Data to pull:** shift logs including travel time, the crew rotation plan, and whether a fresh crew is available to take this specific task.

### Voltage class on system maps doesn't match visible construction standard (hardware, insulator count, structure type) at the work location

**Usually means:** either the maps are out of date or the crew is about to work the wrong MAD/PPE assumptions onto a conductor that isn't what the paperwork says it is.
**First question:** "Does what I'm looking at match a 46kV or a 69kV construction standard for this utility — and which does the map say?"
**Data to pull:** the utility's construction standards reference by voltage class, as-built records for this structure, and confirmation from the system operator before proceeding under either assumption.
