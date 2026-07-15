# Red flags — what a UX designer notices instantly

Smell tests with thresholds. Any single one can be innocent; two or three together are a pattern.

### A flow shipped based on the designer's own fluent, hesitation-free walkthrough with no test against someone unfamiliar with it
- **Usually means:** the designer's fluency after weeks of exposure is worthless evidence about a first-time user's experience — the real signal only comes from watching someone who hasn't seen it before.
- **First question:** "Has anyone who's never seen this flow actually tried to complete it, unprompted?"
- **Data to pull:** usability testing history for this flow, participant familiarity level (first-time vs. team member).

### A disagreement about interface behavior resolved by adding a configurable setting rather than picking a default
- **Usually means:** feature creep via "just add a setting" quietly burdens every other user with a decision, in exchange for satisfying a small vocal minority.
- **First question:** "What problem does this setting actually solve, and can a well-designed default serve both cases without a permanent fork?"
- **Data to pull:** the specific request driving the ask, how many users are affected versus how many would be burdened by the added option.

### An optional form field with no visual distinction from required fields
- **Usually means:** users default to treating ambiguous fields as required, causing decision friction or invalid-data entry — a specific, well-documented usability failure mode.
- **First question:** "Is it visually unambiguous which fields are required versus optional, at a glance?"
- **Data to pull:** field labeling/styling convention used, abandonment or error-rate data at the specific field in question.

### A design critique framed as personal aesthetic preference ("I don't like this") rather than a specific predicted user impact
- **Usually means:** subjective taste is being presented as usability evidence, which can't be validated or acted on the same way a specific, falsifiable user-impact claim can.
- **First question:** "What specifically will a real user do differently because of this, not just how does it look to us?"
- **Data to pull:** the specific critique as stated, whether it's grounded in a testable user behavior claim.

### A competitor's UI pattern copied without understanding the specific user need it was solving for them
- **Usually means:** surface-level pattern matching can import a solution that doesn't fit this product's actual context, missing the underlying need or introducing an unnecessary complexity.
- **First question:** "What specific user problem was this pattern solving for the competitor, and does that same problem exist here?"
- **Data to pull:** the competitor pattern in question, the actual user need/context it addresses, whether an equivalent need exists in this product.

### A usability test conducted under ideal conditions (full attention, no time pressure) for a flow real users will encounter distracted or in a hurry
- **Usually means:** the test conditions don't match real usage conditions, producing an overly optimistic read on how the flow will actually perform.
- **First question:** "Do the test conditions reflect how real users will actually encounter this — attention level, device, time pressure?"
- **Data to pull:** the test protocol's conditions, comparison against actual real-world usage context for this flow.

### A business-goal-driven design change (e.g., a dark pattern boosting a conversion metric) implemented without naming the user-trust tradeoff explicitly to stakeholders
- **Usually means:** a real conflict between business and user goals is being resolved silently rather than as a knowing, named decision stakeholders should own.
- **First question:** "Has this tradeoff been named explicitly to stakeholders, or was it decided quietly as a design detail?"
- **Data to pull:** the specific design change and its user-trust implications, whether stakeholders were presented the tradeoff explicitly.

### A usability finding reported with no severity rating, treated with the same urgency as every other issue
- **Usually means:** without a severity scale (cosmetic/minor/major/catastrophic), prioritization may be driven by which issue is easiest to fix or most recently reported rather than actual user impact.
- **First question:** "What's this issue's actual severity — does it block task completion, or is it a cosmetic/minor annoyance?"
- **Data to pull:** the finding's effect on task completion, whether a workaround exists.
