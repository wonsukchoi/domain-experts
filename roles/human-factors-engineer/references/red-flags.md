# Red flags

Smell tests a human factors engineer catches on a first pass over a workstation design, a manual-handling task, or a usability-test report.

### Lifting Index above 3.0 on a task logged as "moderate exertion" in the incident report

- **Usually means:** the task was never run through the NIOSH equation — someone estimated severity from the box weight alone, missing that horizontal reach or asymmetry can de-rate the RWL more than the load itself does.
- **First question:** what are the measured H, V, D, A, frequency, and coupling values this task's LI was computed from — or has it not been computed at all?
- **Data to pull:** task geometry measurements, the six-multiplier RWL calculation sheet, injury/near-miss log for the station.

### Workstation dimension set at the 50th-percentile ("average") value with no stated rationale

- **Usually means:** a single "average user" figure was used across every dimension, when clearance and reach dimensions need opposite percentile targets and no single percentile fits every requirement.
- **First question:** which specific requirement drove this dimension — clearance (needs 95th-percentile fit) or reach (needs 5th-percentile fit) — and does the chosen percentile match?
- **Data to pull:** ANSI/HFES 100 percentile table used, the specific requirement (clearance vs. reach) the dimension serves.

### RULA score of 7+ or REBA score of 8+ logged, with the corrective action listed as "increased break frequency"

- **Usually means:** the score's action-level band calls for redesign, and an administrative control (breaks, rotation) was substituted because it's faster to implement, not because it addresses the posture/force combination the score flagged.
- **First question:** what is the specific posture or force element driving the score into the top band, and can it be engineered out rather than paced around?
- **Data to pull:** the RULA/REBA scoring worksheet (Group A/B breakdown), the proposed corrective action record.

### Posture or lifting score was scored once at task design and never rescored after a process change

- **Usually means:** a tooling, packaging, or layout change since the original score altered horizontal reach, load, or posture, and nobody re-ran the instrument against the new geometry.
- **First question:** what changed in the task's geometry, weight, or frequency since the last score, and does the current setup still match the assumptions the original score used?
- **Data to pull:** original scoring worksheet with date, most recent process/tooling change record.

### SUS score reported as the sole usability finding, with no task completion rate or error count alongside it

- **Usually means:** the usability test measured perception but not performance — a design can score well on SUS while failing on the metric that actually matters for the task.
- **First question:** what were the task completion rate, time-on-task, and error count for the same session the SUS score came from?
- **Data to pull:** raw task-performance logs from the usability session, not just the aggregated SUS score.

### Heuristic evaluation report with no task-based usability test behind it

- **Usually means:** screens were checked against a heuristics checklist in isolation, which catches per-screen violations but misses flow-level failures that only appear when a real user tries to complete the actual task end-to-end.
- **First question:** has a representative user completed the full task flow, not just individual screens, and were completion and errors measured?
- **Data to pull:** heuristic evaluation findings list, usability test protocol (or its absence).

### UI target sizing change justified by "Fitts's Law says bigger is better" with no index-of-difficulty calculation shown

- **Usually means:** the law was cited as a slogan rather than applied — a distance reduction often achieves the same or better ID improvement at lower real-estate cost than a width increase, and the tradeoff wasn't computed.
- **First question:** what is the ID before and after the proposed change, and was a distance-reduction alternative considered?
- **Data to pull:** current and proposed D/W values, the ID calculation for each option.

### Monitoring or inspection task designed with signal intervals of 30+ minutes and no automation or pacing aid

- **Usually means:** the task relies on sustained human vigilance past the point where detection rate reliably degrades, and the design assumes attentiveness will hold rather than engineering around the known decrement.
- **First question:** what is the actual mean interval between required detections, and is there any forcing function (automated alert, paced sampling prompt) in place?
- **Data to pull:** task signal-rate log, any automation/alerting currently specified for the task.

### Root-cause of a use error logged as "operator error" with no system or interface factor investigated

- **Usually means:** the investigation stopped at the human action instead of asking what interface, procedure, or workload condition made that action likely — the Reason/Rasmussen framing that error is a predictable output of task demands wasn't applied.
- **First question:** what about the interface, procedure sequence, or concurrent workload made this specific error a likely outcome, not just a possible one?
- **Data to pull:** incident/error report, the task or interface sequence at the point of the error, concurrent workload conditions at that time.

### Composite Lifting Index for a multi-task job calculated by averaging single-task LIs

- **Usually means:** the assessor treated CLI as a simple mean instead of the NIOSH composite procedure, which weights by frequency and adds incremental contributions in descending LI order — averaging understates risk when one task dominates.
- **First question:** was the Composite Lifting Index computed per the NIOSH composite procedure, or averaged from individual task LIs?
- **Data to pull:** individual task LI values, frequency for each task, the composite calculation worksheet.
