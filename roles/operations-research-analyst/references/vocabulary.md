# Vocabulary

Terms of art an operations research analyst uses precisely, that generalists routinely
misuse — usually by borrowing the word's everyday meaning instead of its technical one.

- **Optimal**
  Definition: the provably best solution *given the constraints and objective as modeled* — not the best solution to the real-world problem.
  In use: "The routing model returns the optimal solution for this cost function, but it doesn't yet penalize driver overtime."
  Misuse: treating "optimal" as a synonym for "correct" or "good," when a model can be mathematically optimal against a wrong or incomplete formulation. An optimal answer to the wrong problem is still the wrong answer.

- **Feasible**
  Definition: a solution that satisfies every stated constraint, independent of whether it is any good.
  In use: "The schedule is feasible — it meets every crew-rest rule — but it's not close to the cost-minimizing one."
  Misuse: using "feasible" to mean "acceptable" or "reasonable." A feasible solution can still be wildly expensive; feasibility is a floor, not an endorsement.

- **Significant**
  Definition: outside the range explainable by random noise at a stated confidence level — a statistical claim with a threshold attached.
  In use: "The demand lift is significant at p < 0.05 against the holdout period."
  Misuse: using it as a synonym for "large" or "important." A tiny, practically meaningless effect can be statistically significant with enough data, and a large, real effect can fail to reach significance with too little.

- **Robust**
  Definition: a solution or model whose performance degrades gracefully as inputs move away from their assumed values — the opposite of a solution that is optimal at one point and collapses elsewhere.
  In use: "We chose the robust staffing plan, which costs 3% more at the base case but doesn't fall apart if arrivals spike 20%."
  Misuse: using "robust" as vague praise for "well-built" or "thorough." Technically it means a specific, checkable property (bounded performance loss under specified parameter variation), not general solidity.

- **Sensitivity analysis**
  Definition: a systematic check of how the optimal solution and objective value change as specific input parameters vary within a defined range — not a one-off "what if we tried a different number."
  In use: "The sensitivity analysis shows the plan stays optimal for lead times between 2.5 and 3.5 weeks, but the basis changes outside that band."
  Misuse: treating a single alternate-scenario rerun as sensitivity analysis. Real sensitivity analysis reports the range over which a conclusion holds, not just a second data point.

- **Big-M**
  Definition: a large constant used in a mixed-integer formulation to "switch off" a constraint when a binary variable is 0 — its correctness and solver performance both depend on it being sized from the problem's actual bounds, not chosen arbitrarily.
  In use: "We resized Big-M from the tightest valid bound in this instance's data, which cut branch-and-bound nodes by an order of magnitude."
  Misuse: picking an arbitrarily huge Big-M "to be safe." An oversized M loosens the LP relaxation, slows the solver, and at extreme magnitudes can produce a spuriously feasible or wrong answer from floating-point rounding — the opposite of safe.

- **Degenerate (solution/basis)**
  Definition: a basic feasible solution in which one or more basic variables equal zero, which can cause the simplex method to cycle or stall without technique-specific safeguards.
  In use: "The solver kept re-visiting the same objective value — that's a degenerate basis, not a bug in the model."
  Misuse: using "degenerate" loosely to mean "broken" or "bad." It's a specific structural property of a solution that has known causes and known fixes (e.g., Bland's rule), not a general insult.

- **Optimality gap**
  Definition: the certified percentage difference between the best solution found so far and a proven lower (for minimization) or upper (for maximization) bound on the true optimum — the number that tells you how far from provably optimal a solver's current answer is.
  In use: "We stopped the solver at a 0.8% optimality gap after four hours because further runtime bought negligible improvement."
  Misuse: quoting only the objective value and omitting the gap, which lets a merely "pretty good" answer masquerade as optimal. Without the gap, "the solver found X" is meaningless — X could be 1% or 40% off true optimum.

- **NP-hard**
  Definition: a formal complexity classification meaning no algorithm is known that solves every instance of the problem in polynomial time — not a claim that a specific instance is unsolvable or even hard in practice.
  In use: "Vehicle routing is NP-hard in general, but this instance's structure lets a good heuristic get within 2% of optimal in seconds."
  Misuse: using "NP-hard" to mean "impossible" or as an excuse to skip modeling effort. Most NP-hard problems encountered in practice are solved to a useful gap routinely — the classification describes worst-case scaling, not this Tuesday's instance.

- **Heuristic**
  Definition: a method that produces a good, fast solution with no guarantee of optimality (and often no bound on how far from optimal it can be), used when an exact method is too slow for the time budget.
  In use: "We use a greedy-insertion heuristic for the daily reroute since a same-day clock doesn't allow for an exact solve."
  Misuse: treating "heuristic" as a lesser or embarrassing fallback rather than a deliberate, often correct engineering choice — and conversely, presenting a heuristic's output with the same confidence as a solver's certified-optimal one without saying so.

- **Stochastic**
  Definition: involving genuine randomness in the model itself (demand, arrivals, service times drawn from a distribution) — distinct from a deterministic model merely being "uncertain" because its inputs were guessed.
  In use: "We moved from a deterministic EOQ model to a stochastic one because lead time itself varies, not just the point forecast of it."
  Misuse: calling any model with imprecise inputs "stochastic." A model with a single best-guess input is still deterministic; stochastic modeling means the variability is represented explicitly (a distribution), not just acknowledged in prose.

- **Service level**
  Definition: a specific, quantified target — most commonly cycle service level (probability of not stocking out in a replenishment cycle) or fill rate (fraction of demand met from stock) — that must be stated with which definition is meant, since the two produce different safety-stock numbers for the same target percentage.
  In use: "Confirm whether the 95% target is cycle service level or fill rate before I size safety stock — they're not interchangeable."
  Misuse: quoting a service-level percentage without specifying which metric, or treating a single company-wide number as universally correct rather than something to be set from the specific stockout-cost asymmetry of the SKU in question.

- **Utilization**
  Definition: the fraction of available capacity actually in use (ρ), meaningful only in the context of the queueing relationship it drives — wait time and queue length are convex, not linear, functions of ρ, and the system is only stable at all when ρ < 1.
  In use: "Utilization is at 82%, which on this arrival-variability profile already means wait times are past the knee of the curve."
  Misuse: reading utilization as a linear health indicator ("we're fine, we're under 100%"), missing that the wait-time cost of the last few points of utilization is far larger than the cost of the first few.

- **Decomposition**
  Definition: splitting one intractable joint optimization problem into multiple coupled subproblems that are each solved with a fitted method and reconciled, rather than solved as one monolithic model.
  In use: "Yield management here decomposes into overbooking, discount allocation, and traffic management — each solved separately, the way DINAMO did it."
  Misuse: assuming any problem with multiple components should be decomposed by default, or conversely never checking for a natural decomposition and stalling on a monolithic model that was never going to solve in time.
