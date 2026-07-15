# Industrial production working vocabulary

Terms a production manager uses precisely. Format: definition → how a practitioner says it → common misuse.

**Bottleneck (constraint)** — The single station or step in a process with the lowest capacity, which determines the entire line's total output regardless of how fast any other station runs.
In use: "Station 3's 976 units/day capacity is the bottleneck — it's what our 980 units/day actual output is capped by, not final assembly."
Misuse: identifying the "most visible" or "most recently problematic" station as the bottleneck without checking actual per-station capacity and WIP data — the true constraint is often not the most obviously troubled step.

**WIP (work-in-progress)** — Partially completed units sitting between process steps, whose accumulation pattern is one of the clearest diagnostic signals for locating the actual bottleneck (WIP piles up immediately upstream of the true constraint).
In use: "340 units of WIP sitting in front of Station 3 and growing — that's the bottleneck signature, not a general inventory problem."
Misuse: treating WIP accumulation as a generic inventory management issue to be reduced everywhere uniformly, rather than reading it as a specific diagnostic pointing at the actual constraint's location.

**OEE (Overall Equipment Effectiveness)** — A composite metric combining availability (uptime), performance (speed relative to ideal), and quality (good units produced), used to evaluate true equipment/line performance rather than any single dimension in isolation.
In use: "Running the machine 20% faster raised performance but OEE only moved 3% once the resulting defect-rate increase was factored into the quality component."
Misuse: evaluating equipment or line changes on speed alone, missing a tradeoff on availability or quality that OEE's composite structure is specifically designed to catch.

**Poka-yoke (error-proofing)** — Designing a process or fixture so a specific mistake is physically difficult or impossible to make, as opposed to relying on inspection or worker vigilance to catch the error after it happens.
In use: "We added a poka-yoke fixture that only accepts the part in the correct orientation — the misassembly defect dropped to zero, not just 'caught more often.'"
Misuse: relying on end-of-line inspection or training/reminders to catch a recurring error, when a physical or process design change could prevent the error from being possible in the first place.

**Standard work** — A documented, consistent baseline process for a given production step, which makes it possible to distinguish real drift or genuine improvement from normal variation.
In use: "We can't tell if this change actually helped without comparing it against the documented standard work baseline, not just yesterday's output."
Misuse: attempting continuous improvement (kaizen) on a process with no documented standard, making any before/after comparison closer to guessing than measurement.

**Cost of quality (by detection point)** — The principle that the cost of correcting a defect rises steeply the further it travels from its point of creation before being caught — cheapest at the originating station, more expensive at final inspection, most expensive after reaching the customer.
In use: "This defect cost us a $200 rework at the station — the same defect caught after shipment last quarter cost us a $40,000 recall."
Misuse: weighting quality control investment evenly across the process or concentrated only at final inspection, missing that the same detection effort is disproportionately more valuable the earlier it's placed.

**Theory of constraints** — The operations management principle that a system's total throughput is capped by its single limiting step, and that improving any non-constraint step doesn't increase overall output.
In use: "Per theory of constraints, speeding up final assembly does nothing for total output while Station 3 remains the actual limiting step."
Misuse: distributing improvement investment evenly across all stations rather than concentrating it specifically on the identified bottleneck first.

**Statistical process control (SPC)** — Using control charts and statistical thresholds to distinguish a genuine process shift from normal, expected variation, catching drift before it produces an actual defect or failure.
In use: "The control chart flagged this measurement trending outside normal variation three cycles before it would have produced an out-of-spec part."
Misuse: reacting to every individual data point as if it signals a real process change, rather than using control limits to distinguish genuine shifts from expected noise.

**Changeover time** — The time required to reconfigure equipment or a line from producing one product/variant to another, a real capacity consumer that should be included in realistic capacity planning rather than assumed away.
In use: "Our realistic daily capacity accounts for the 45-minute changeover between product runs — the idealized capacity number doesn't."
Misuse: planning capacity or scheduling based on an idealized, fully-available line with no changeover, maintenance, or downtime built in, producing a plan that looks achievable on paper but isn't in practice.

**Fatigue-driven defect/incident lag** — The pattern where sustained overtime or understaffing doesn't immediately show up as a quality or safety problem, but produces a measurable rise in defect and incident rates after a delay, making short-term output stability a misleading signal of workforce capacity health.
In use: "Output held steady through the overtime stretch, but defect rate rose 40% starting in week 5 — that's the fatigue lag we should have been watching for."
Misuse: treating stable near-term output during a period of sustained overtime as evidence the staffing level is sustainable, missing that the negative effects typically show up with a delay rather than immediately.
