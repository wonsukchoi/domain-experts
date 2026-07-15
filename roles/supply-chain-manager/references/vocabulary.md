# Supply chain management working vocabulary

Terms a supply chain manager uses precisely. Format: definition → how a practitioner says it → common misuse.

**Bullwhip effect** — The structural amplification of demand variability moving upstream through a supply chain, caused by each stage reacting to the immediately downstream stage's orders rather than real end-customer demand — a systemic property of information delay, not a forecasting skill failure at any single link.
In use: "The 40% swing our supplier sees isn't bad forecasting on their part — it's the bullwhip effect amplifying our own 8% actual demand variability."
Misuse: blaming a specific upstream stage's forecasting accuracy for variability that's actually a structural amplification effect requiring shared demand visibility to address, not better local forecasting.

**Efficiency-resilience tradeoff (efficient frontier)** — The tradeoff between lean, low-cost supply chain configurations (minimal buffer, single-sourcing) and more redundant, resilient ones (buffer stock, multi-sourcing), with the right position depending on the actual cost of disruption for a specific input, not a universal default.
In use: "This component's disruption cost is high enough to justify sitting further toward the resilient end of the frontier, even at a real price premium."
Misuse: defaulting an entire supply chain uniformly toward lean efficiency (or uniformly toward redundant buffering) without locating each critical input's actual position on the tradeoff based on its specific disruption cost.

**Concentration risk** — Exposure created by relying on a single supplier, single region, or single transportation corridor for a critical input, which is often invisible until a disruption event reveals it.
In use: "We mapped concentration risk across all critical inputs and found three single-source dependencies with no documented contingency plan."
Misuse: only discovering a concentration risk during an actual disruption, when diversification is far more expensive and slower to arrange than it would have been if mapped proactively.

**S&OP (Sales and Operations Planning)** — A cross-functional process aligning demand forecasting, production planning, and supply planning on a shared information base, the structural fix for bullwhip-effect variability.
In use: "S&OP gives purchasing, production, and distribution the same real demand signal — that's what actually dampens the bullwhip effect, not better forecasting at any one stage alone."
Misuse: having an S&OP process that exists on paper without actually sharing real demand data across functions, leaving each stage still planning off its own local, delayed signal.

**Expected cost of disruption** — The probability of a supply disruption multiplied by its estimated cost if it occurs, used as the basis for comparing a guaranteed diversification/resilience cost against the risk it's meant to address.
In use: "A 25% probability of a $19.82M disruption gives an expected cost of $4.955M — that's the number the diversification cost should be compared against."
Misuse: evaluating a resilience investment only against the worst-case disruption cost or ignoring probability entirely, rather than using expected value as the comparison basis for a rational cost/benefit decision.

**Total system cost (vs. local function optimization)** — Evaluating a decision by its effect on the whole supply chain's cost and responsiveness, as distinct from the metric any single function (purchasing, production, distribution) is individually measured on.
In use: "The larger batch size lowers production's per-unit cost, but it raises total system inventory carrying cost enough that it's a net loss chain-wide."
Misuse: approving a decision because it improves one function's local metric without checking whether it degrades total system performance once effects on other functions (inventory, responsiveness, cost) are included.

**Supply chain visibility (control tower)** — Near-real-time status information across supplier, production, and logistics stages, a prerequisite for fast, proportionate disruption detection and response.
In use: "Our control tower flagged the port delay within hours — that's what let us reroute before it became a multi-week problem."
Misuse: relying on periodic reports rather than near-real-time visibility, discovering a disruption's true scope too late for an effective response, with damage compounding during the detection lag.

**Category-based resilience investment** — Allocating multi-sourcing, buffer stock, or dual-routing investment differentially based on an input's criticality and substitutability, rather than applying uniform resilience strategy across all inputs regardless of stakes.
In use: "This component gets the full resilience treatment — dual-sourced, buffered — because it's both critical and hard to substitute; packaging materials don't get the same investment."
Misuse: applying the same sourcing/buffering strategy to a critical, hard-to-substitute input as to a low-stakes commodity one, wasting resilience investment in one direction while under-protecting in the other.

**Disruption scope assessment** — The deliberate, brief process of establishing a disruption's actual scope and expected duration before committing to a response, since a fast but miscalibrated reaction can cause more damage than a short, accurate assessment followed by a proportionate response.
In use: "We took 4 hours to confirm this was a 2-week regional issue, not a 6-month one — that assessment shaped a very different, better-calibrated response than an immediate reflexive scramble would have."
Misuse: launching an immediate, reflexive response (activating full contingency plans, panic-buying alternate supply) before establishing the disruption's actual scope, risking an over- or under-calibrated reaction relative to the real severity.

**Buffer stock** — Inventory held specifically to absorb supply or demand variability for a given input, sized to the input's criticality and disruption cost rather than a uniform safety-stock policy applied across all items.
In use: "We hold 6 weeks of buffer stock on this critical component, versus 1 week on lower-criticality commodity items — that's deliberate, not an oversight."
Misuse: applying a single, uniform buffer stock policy (e.g., "2 weeks of everything") without adjusting for the specific criticality and disruption cost of each input.
