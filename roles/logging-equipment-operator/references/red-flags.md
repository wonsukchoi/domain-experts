# Red flags

Smell tests a senior mechanized-logging operator or foreman catches before a shift goes wrong. Format for each: what it usually means, the first question to ask, and the data to pull.

## 1. Slope classification unchanged since the harvest plan was drawn, despite recent rain

**Usually means:** the crew is trusting a dry-season LiDAR flyover number instead of ground-truthing bearing capacity, which is the actual limiting factor for wheeled equipment stability.

**First question:** "When was this zone last walked, and how much rain has it seen since?"

**Data to pull:** harvest-plan classification date vs. last-48-hour precipitation; most recent ground-walk notes for the zone in question; any operator reports of tire/track sinkage on the current shift.

## 2. Feller-buncher production outrunning skidder/forwarder extraction for more than one shift

**Usually means:** felling is being run at its own rated capacity without regard to the extraction system's throughput, building a standing-wood backlog that gets re-driven over (soil compaction) and burns machine-hours nobody can bill against delivered tons.

**First question:** "How many tons of felled wood are sitting un-extracted right now, and for how long?"

**Data to pull:** felling machine-hours and tons/hr vs. skidder/forwarder machine-hours and tons/hr for the same period; standing-inventory tons at shift end; re-drive passes over already-decked ground.

## 3. Boom/grapple routinely working at full reach on a slope near the machine's rated limit

**Usually means:** the operator (or the job layout) is treating the ROPS/FOPS rated grade as safe at any load geometry, when a fully extended, loaded boom shifts the center of gravity outward and lowers the effective tip-over threshold well below the spec-sheet number.

**First question:** "Is the boom working at full reach because the trail layout forces it, or is it habit?"

**Data to pull:** trail spacing plan for the zone; boom-reach telemetry or operator log if available; incident/near-miss log for lateral instability events on that slope class.

## 4. More than ~3 hang-ups per shift on the same block

**Usually means:** a felling-head cut pattern or lean-reading problem, not unusually difficult terrain — and each one is an exposure event if the crew starts improvising manual recovery out of frustration with the pace.

**First question:** "What's the cut pattern on the hung stems — are they clustered by a specific lean direction or stand density?"

**Data to pull:** hang-up log with tree lean, stand density, and felling-head cut angle per incident; whether any hang-up was cleared by a person on foot rather than mechanically.

## 5. Operator or crew reports a hang-up "handled" with no machine-hours logged against it

**Usually means:** someone went out on foot with a cant hook or peavey instead of using the grapple or winch — converting the mechanized system's core safety advantage back into faller-equivalent struck-by exposure, without a faller's training.

**First question:** "Walk me through exactly how that hang-up came down — which machine, which attachment, how long did it take?"

**Data to pull:** shift log entries around the hang-up; machine-hour meter readings for the relevant equipment during that window; any witness account of someone exiting the cab.

## 6. Forwarder or skidder payload consistently under ~70% of rated capacity per turn

**Usually means:** trail spacing or bunching pattern is forcing partial loads, not that the operator is driving conservatively — a layout problem that compounds into a much higher cost-per-ton than the rated machine capacity implies.

**First question:** "What's the actual average load weight per turn this week, and how does trail spacing compare to the machine's working radius?"

**Data to pull:** load-weight logs per turn (onboard scale or estimated); trail spacing map; average travel distance per turn vs. the bunching plan.

## 7. Blended cost-per-ton reported flat while the zone mix shifts toward steeper terrain

**Usually means:** a steep pocket's higher extraction cost (winch-assist rental, reduced cycle rate) is being absorbed into a tract-wide average instead of tracked separately, hiding a zone that may already be running at or below margin.

**First question:** "What's the cost-per-ton for the steep zone alone, not blended with the flat ground?"

**Data to pull:** zone-by-zone machine-hour cost and production rate (see `playbook.md` §4 worksheet); contracted delivered rate; margin by zone, not tract-wide.

## 8. Machine utilization (productive hours ÷ scheduled hours) below ~65% for more than a few days

**Usually means:** mechanical downtime, weather delays, or an extraction bottleneck are eating into billable production — and the rated production-rate number the job was bid on no longer reflects reality.

**First question:** "What's actually consuming the non-productive hours — breakdowns, weather, or waiting on another machine?"

**Data to pull:** machine-hour meter logs split into productive/idle/maintenance categories; maintenance ticket history for the period; weather log against scheduled shifts.

## 9. Winch-assist tether angle exceeding roughly 30° off the machine's line of travel

**Usually means:** the anchor point was set for convenience rather than path geometry, reducing effective pull and adding side-load the anchor may not be rated for.

**First question:** "Where's the anchor relative to where the machine actually needs to travel, not where it was easiest to set up?"

**Data to pull:** anchor placement vs. planned travel path; anchor rating documentation; cycle-time data (a bad angle usually shows up as cycle times well past the ~15–25% winch-assist penalty budget).
