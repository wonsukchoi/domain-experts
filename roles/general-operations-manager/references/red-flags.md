# Red flags — what an operations manager notices instantly

Smell tests with thresholds. Any single one can be invisible-until-obvious; two or three together are a pattern.

### Two departments each hitting their individual targets while a shared downstream metric (customer complaints, cycle time) is degrading
- **Usually means:** a coordination failure at the handoff between the two teams, not a competence problem in either — each team's own metric doesn't capture what's breaking at the interface.
- **First question:** "What's the actual handoff process between these two teams, and has it been mapped recently, not just assumed?"
- **Data to pull:** each team's individual metrics, the specific handoff/interface data (commitments made, capacity available) between them.

### An initiative or investment improving a step that isn't the actual bottleneck
- **Usually means:** visible effort and resources are being spent without moving overall throughput, since gains anywhere except the true constraint don't show up in total output.
- **First question:** "Is this the step that's actually limiting overall throughput, or does it just feel like the most fixable one?"
- **Data to pull:** throughput/cycle-time data at each step in the process, identification of which step has the least slack.

### A recurring process or approval step that no one can explain the specific failure mode it prevents
- **Usually means:** the process may be pure ceremony accumulated over time rather than a control mapped to an actual risk, adding drag without a corresponding benefit.
- **First question:** "What specific failure would happen if we removed this step, and has that failure actually occurred recently?"
- **Data to pull:** the process's stated purpose (if documented), any incident history it was meant to prevent.

### Status reports showing consistently green/on-track while direct observation of the actual work reveals workarounds or informal fixes
- **Usually means:** the gap between reported status and ground truth has grown, likely because reports are being filtered or optimistically summarized as they pass through layers.
- **First question:** "What does the work actually look like on the ground right now, independent of the last status report?"
- **Data to pull:** direct observation notes (gemba walks, spot checks), comparison against the corresponding status report language.

### A cross-functional initiative stalling with each team believing another team owns the next step
- **Usually means:** no RACI or explicit ownership was established before the initiative started — the classic ambiguous-ownership failure mode.
- **First question:** "Who is the single accountable owner for this initiative's next milestone, in writing?"
- **Data to pull:** the initiative's RACI or ownership documentation, if any exists; the specific stalled step and who each team assumed owned it.

### A metric a team appears to be "gaming," with no review of what the metric actually incentivizes
- **Usually means:** the behavior is very likely the predictable, rational response to how the metric is designed, not a discipline or character problem.
- **First question:** "If I were on this team, optimizing exactly for this metric as written, would this behavior be the rational thing to do?"
- **Data to pull:** the metric's exact definition and how it's calculated, the specific behavior being labeled as "gaming."

### A large, infrequent process overhaul being planned instead of a small, testable, reversible change
- **Usually means:** the change accumulates risk and will make it hard to isolate what worked or failed if something goes wrong, compared to an incremental, validated approach.
- **First question:** "Can this be tested at small scale first, and if not, why not?"
- **Data to pull:** the proposed change's scope and rollback plan, any smaller-scale test option that was considered or dismissed.

### Small operational workarounds or inefficiencies that have persisted for months with no one assigned to resolve them
- **Usually means:** unresolved friction is compounding into structural drag that will be much more expensive to unwind the longer it's tolerated as "how we've always done it."
- **First question:** "How long has this workaround existed, and what would it take to actually fix the underlying process instead of continuing to work around it?"
- **Data to pull:** duration and frequency of the workaround, any prior attempts or discussions about fixing the root cause.
