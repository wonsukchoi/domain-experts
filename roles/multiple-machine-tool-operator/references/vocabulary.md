# Vocabulary

### Consequence-based triage
Prioritizing which of several simultaneously needy machines to address first based on the actual cost of further delay, rather than by arrival order, alarm sequence, or physical proximity.
**In use:** "C's been stopped six minutes losing pure output — that's higher consequence than B, which still has slack before its check is due. C goes first."
**Common misuse:** Defaulting to "first alarm, first served" or "closest machine first" — those orderings feel systematic but don't account for which situation actually costs more the longer it waits.

### Machine-minute analysis
An industrial engineering method for calculating how many machines one operator can effectively tend, based on each machine's cycle time and the time required for loading/servicing tasks.
**In use:** "Machine-minute analysis is what determines whether adding a fourth machine to this operator's assignment is actually feasible, not just intuition."
**Common misuse:** Assuming any number of machines can be added to a tending assignment as long as their combined "busy" time seems to fit — the analysis has to account for the timing overlap risk (multiple machines needing attention in the same window), not just total time budgeted.

### Unattended interval
The period a machine runs without direct operator observation between visits, during which any developing issue (tool wear, a misfeed, a jam) goes undetected until the next check.
**In use:** "We tightened B's unattended interval to five minutes because of the known tool wear issue on this job — A and C stay at their normal ten."
**Common misuse:** Applying the same unattended interval across every machine in a tending group regardless of differing risk profiles — a machine with a known wear-prone tool or tight tolerance needs a shorter interval than a stable, low-risk one.

### Cycle completion timing
The point at which a specific machine will finish its current operation and become ready for unload/reload or the next step, used as one basis for sequencing visits.
**In use:** "B's not done for another three minutes — visiting it now would just be a wasted trip."
**Common misuse:** Visiting a machine on a fixed rotation schedule regardless of whether it's actually near cycle completion — an early visit to a machine mid-cycle accomplishes nothing and delays attention to a machine that's actually ready.

### Setup exposure window
The period during a setup or changeover on one machine when the other machines in the same tending assignment go unattended for the setup's full duration.
**In use:** "We're doing the changeover on A now, while B and C both just started long, stable cycles — minimal exposure window for them during this setup."
**Common misuse:** Scheduling a setup purely around the convenience of the machine being changed over, without considering whether the other tended machines have enough slack to tolerate being unattended for that duration.

### Slack (remaining safe unattended time)
The amount of time a specific machine can continue running without operator attention before risk (a check becoming overdue, a cycle completing and sitting idle) meaningfully increases.
**In use:** "B's got two minutes of slack before its check is due — plenty to handle C's stoppage first."
**Common misuse:** Treating all machines as having equal slack at any given moment — slack is specific to each machine's current cycle position and check interval, and changes continuously as time passes.

### Round-robin rotation
A fixed, repeating visiting order (e.g., always A, then B, then C, then back to A) applied regardless of each machine's actual current status or need.
**In use:** "We stopped using strict round-robin once B's tool wear issue started — now the sequence follows actual need, not a fixed loop."
**Common misuse:** Treating round-robin as inherently fair or systematic — it's only appropriate when machines have genuinely identical, stable cycle times and risk profiles; otherwise it systematically over- or under-services different machines in the group.

### Dynamic visiting sequence
A machine-tending order that's recalculated based on current cycle status and risk, rather than fixed in advance, adjusting as conditions change through a shift.
**In use:** "Sequence isn't fixed — it's dynamic, recalculated every time a machine's status changes or a new one gets added to the group."
**Common misuse:** Building a visiting sequence once at shift start and treating it as valid for the rest of the shift — cycle times, tool wear, and workload can all shift mid-shift, and the sequence needs to be recalculated when they do, not just followed from the original plan.

### Tending group
The specific set of machines assigned to one operator to run and service simultaneously.
**In use:** "My tending group's three lathes right now — adding a fourth would need the sequence recalculated from scratch, not just squeezed into the existing rotation."
**Common misuse:** Treating a tending group's composition as fixed once assigned, rather than something whose visiting logic needs updating whenever the group's membership or any member's cycle time changes.

### Output loss vs. quality risk
The distinction between a stopped/idle machine (a pure throughput cost, straightforward to quantify) and a running machine approaching an undetected quality issue (a less visible but potentially more consequential risk).
**In use:** "The idle machine's losing us output every minute, sure — but the one drifting toward an undetected tolerance issue could cost us a whole batch if we don't catch it in time."
**Common misuse:** Automatically treating a visibly stopped machine as higher priority than a running one that's quietly approaching a quality problem — the correct triage weighs actual consequence of delay, which sometimes favors the less visually urgent situation.
