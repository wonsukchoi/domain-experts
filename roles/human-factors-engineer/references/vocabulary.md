# Vocabulary

Terms generalists flatten together that a human factors engineer keeps sharply separate — the value is in the misuse, not the definition.

### Percentile (anthropometric)

The proportion of a reference population at or below a given value on one specific body dimension — not a rank of "how average a person is" overall. A person can be 5th-percentile on stature and 95th-percentile on hand length simultaneously; percentiles don't transfer across dimensions.

**In use:** "We're not designing to '5th percentile people' — we're designing this reach dimension to the 5th-percentile reach value and this clearance dimension to the 95th-percentile breadth value, on two different people."

**Common misuse:** treating percentile as a property of a person ("design for the 50th-percentile user") rather than a property of a single measured dimension, which produces a design that fits an imaginary composite person on no real dimension.

### Lifting Index (LI) vs. Recommended Weight Limit (RWL)

**RWL** is the maximum recommended weight for a specific lift's geometry, computed by de-rating the 23kg load constant with six multipliers. **LI** is the ratio of the actual load to that task-specific RWL — the risk metric used for prioritization. RWL changes per task; LI is what gets compared against action thresholds.

**In use:** "The carton weighs less than last quarter's task, but the RWL dropped further because the new pallet position increased horizontal reach — LI still went up."

**Common misuse:** comparing the raw lifted weight to a generic "50 lb limit" instead of computing the task-specific RWL first.

### RULA vs. REBA

**RULA** (Rapid Upper Limb Assessment) scores upper-body posture, force, and muscle use, built for seated desk/assembly tasks. **REBA** (Rapid Entire Body Assessment) extends the same logic to whole-body posture including trunk, neck, and legs, and adds an activity score — built for tasks with more dynamic, whole-body movement (lifting, carrying, non-seated work).

**In use:** "This is a seated inspection task, so RULA fits; the loading-dock task involves trunk bending and carrying, so score that one with REBA."

**Common misuse:** using RULA on a whole-body dynamic task, which under-weights trunk and leg loading that REBA's structure was built to capture.

### Action level (RULA/REBA)

The published band a total score falls into, mapping directly to an urgency of response — not a single pass/fail line. RULA and REBA each define four bands from "acceptable" to "investigate and change now."

**In use:** "A RULA score of 5 is action level 3 — investigate soon and change soon, not an emergency but not a low-priority backlog item either."

**Common misuse:** treating any score below the instrument's maximum as automatically "acceptable," ignoring the intermediate action-level bands that call for investigation before the top band is reached.

### Index of Difficulty (ID)

Fitts's Law's measure of a pointing task's inherent difficulty: ID = log2(2D/W), combining target distance and width into a single bits-of-information value that predicts movement time. Because it's logarithmic, distance and width contribute on an equal, substitutable footing.

**In use:** "Halving the distance drops the ID by the same amount as doubling the width — check which change is cheaper before speccing a bigger button."

**Common misuse:** treating target width as the only lever for improving pointing speed, ignoring that layout (distance) changes are frequently the cheaper way to reduce the same ID.

### System Usability Scale (SUS) score

A standardized 10-item questionnaire converted to a 0-100 score measuring perceived usability after a task session — a subjective-perception metric, not a direct measure of task success.

**In use:** "SUS came in at 75, above the ~68 average benchmark — but check the completion rate before calling the design done."

**Common misuse:** reporting SUS alone as "the usability result," when it answers "did they like it," not "could they do it."

### Vigilance decrement

A well-documented drop in signal-detection rate that occurs after roughly 20-35 minutes of a low-event-rate monitoring task, driven by the limits of sustained attention rather than by an individual's effort or character.

**In use:** "The console has been quiet for 25 minutes — that's inside the window where detection rate reliably starts to drop, which is why the pacing alert exists."

**Common misuse:** attributing a missed detection late in a monitoring shift to the operator "not paying attention," when the decrement is a predictable property of the task design at that signal rate.

### Skill-Rule-Knowledge (SRK) taxonomy

Rasmussen's classification of human performance into skill-based (automatic, low attention), rule-based (if-then procedures), and knowledge-based (novel problem-solving) behavior — each with a different characteristic error type (slip, mistake in rule selection, or reasoning failure under uncertainty).

**In use:** "This was a rule-based error — the operator applied the right procedure to a situation that looked like the trained case but wasn't, not a skill-based slip."

**Common misuse:** labeling every error a "human error" without identifying which behavior level it occurred at, which determines whether the fix is an interface cue, a procedure redesign, or better decision-support information.

### Coupling (NIOSH lifting equation)

The quality of the hand-to-load connection at the moment of lift — good (well-designed handles), fair (usable but non-optimal grip), or poor (no handle, awkward or sharp grip) — one of the six RWL multipliers, not a general comment on grip strength.

**In use:** "Coupling is fair, not good — the cutouts aren't molded handles, so CM is 0.95, not 1.00, at this vertical height."

**Common misuse:** rating coupling as "good" whenever a handle of any kind is present, without checking whether it meets the specific geometric criteria (size, shape, grip depth) the standard's "good" category requires.

### Composite Lifting Index (CLI)

The NIOSH-defined risk metric for a job with multiple distinct lifting tasks — computed by ordering tasks by descending individual LI and adding each subsequent task's frequency-weighted incremental contribution, not by averaging the individual task LIs.

**In use:** "Task 2 has the highest single-task LI, so it anchors the composite; Task 4's incremental contribution gets added on top of that, not blended into an average."

**Common misuse:** averaging or summing raw single-task LIs directly, which can understate the true composite risk when one task dominates and others are low-frequency.

### Heuristic evaluation

An expert-review method (Nielsen's 10 heuristics) where reviewers check an interface's screens against a fixed list of usability principles, rating severity of each violation found — a discount method, distinct from and complementary to a task-based usability test with real users.

**In use:** "Heuristic evaluation flagged three visibility-of-system-status violations — now we need a task-based test to see if any of them actually block task completion."

**Common misuse:** treating a clean heuristic evaluation as equivalent to a validated design, when it can miss flow-level and task-sequence problems that only surface when a real user attempts the whole task.

### Affordance

A perceivable property of an object or interface element that signals how it can be used (a button's raised edge suggesting "press," a handle's shape suggesting "pull") — distinct from a signifier, which is an explicit cue (a label, an icon) added because the affordance alone isn't perceivable.

**In use:** "The flat rectangle doesn't afford tapping on its own — it needs a signifier, like a drop shadow or an explicit 'Tap to continue' label."

**Common misuse:** using "affordance" to mean any visual design cue, when the term specifically refers to the perceived action possibility itself, separate from any added label or icon.
