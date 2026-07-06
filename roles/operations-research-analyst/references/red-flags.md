# Operations Research Analyst — Red Flags

### Big-M constant set to a round "safe" number (10,000, 10^6, 10^9) instead of derived from the tightest data bound
- **Usually means:** the modeler never computed the actual max value the constrained variable can take, and defaulted to a number that "feels big enough."
- **First question:** "What is the largest value this variable can actually take in this instance, and does M exceed it by more than a small buffer?"
- **Data to pull:** the constraint's variable-bound derivation and the solver's reported optimality gap/node count for the run.

### Optimality gap still >5% after 10x the expected solve time
- **Usually means:** (1) an oversized Big-M loosening the relaxation, (2) a weak formulation missing valid cuts/symmetry-breaking constraints, (3) a genuinely hard instance being solved with the wrong method.
- **First question:** "Has anyone recomputed M from the data, or are we just letting the solver run longer?"
- **Data to pull:** solver log showing gap-vs-time trajectory and the current M values on every binary/integer constraint.

### Solver reports "feasible" but a constraint is visibly violated on manual inspection (often traced to Big-M > 10^9)
- **Usually means:** floating-point tolerance masking a real violation, often because a Big-M was sized near the solver's numerical precision limit (M > 10^9).
- **First question:** "What tolerance is the solver using, and how does it compare to the magnitude of the largest Big-M in the model?"
- **Data to pull:** solver tolerance settings and the magnitude of every Big-M constant in the formulation.

### Objective value swings more than 3% between reruns on identical input
- **Usually means:** a non-deterministic parallel search or tie-breaking on a near-degenerate optimum being reported as if one run were canonical.
- **First question:** "Is the random seed and thread count fixed, and if not, how many of these 'optimal' solutions are actually ties?"
- **Data to pull:** solver run logs across at least 3 reruns with the same input, plus seed/thread configuration.

### A single monolithic model covering an entire multi-stage process (allocation + timing + recovery) that has never converged in test runs
- **Usually means:** the problem naturally decomposes into subproblems with thin linkage, and forcing one model to solve all of it at once is why it's intractable.
- **First question:** "Do these subproblems share more than a handful of linking variables, or could each be solved separately and reconciled?"
- **Data to pull:** the constraint matrix's block structure (which constraints touch which variable groups) and node-count history on the joint model.

### Safety-stock or staffing target quoted as a fixed number (e.g., "95% service level" or "MAPE under 15%") with no stated cost-of-error or volatility behind it
- **Usually means:** the number was copied from a different SKU family, a prior project, or a textbook default rather than sized against this problem's stockout consequence.
- **First question:** "What is the stockout or forecast-error consequence here, and is it life-safety/contractual or a discretionary late shipment?"
- **Data to pull:** 12+ months of stockout/forecast-error event history with per-event cost, and the demand or lead-time volatility (σ) used in the calculation.

### Utilization reported as a single average (e.g., "we're at 82% busy") used to justify no staffing change
- **Usually means:** the average is masking a convex wait-time relationship that has already started compounding — utilization above roughly 85–90% degrades wait times sharply, not linearly.
- **First question:** "What does the queueing or simulation model say about wait time at this utilization, not just the average itself?"
- **Data to pull:** arrival-rate distribution and the queueing/simulation model's wait-time output at the reported utilization.

### A recommendation memo that states the optimized answer with no naive-baseline comparison
- **Usually means:** the sponsor has no legible reference point to judge the size of the improvement, which stalls adoption regardless of the model's quality.
- **First question:** "What would the current manual approach have produced on this same instance, in the same units?"
- **Data to pull:** the manual/status-quo policy's output on the identical scenario, expressed in the sponsor's units (cost, service level, headcount).

### A production model with no revalidation date on the calendar
- **Usually means:** the model was fit once at launch and nobody owns checking whether the world it assumed still holds; degradation is silent until the recommendation quietly stops matching reality.
- **First question:** "When is this model scheduled to be revalidated against current data, and who owns that trigger?"
- **Data to pull:** the model's original fitting-period data and the most recent 3 months of actuals, compared side by side.

### Every disruption, regardless of scale, triggers a full from-scratch re-solve (or, inversely, every disruption gets patched by hand)
- **Usually means:** there's no tiered recovery runbook — recovery approach is being chosen by habit or panic rather than by the disruption's actual scale (% of affected units, safety criticality).
- **First question:** "What percentage of the schedule does this disruption affect, and does that cross the threshold where a full re-solve is actually warranted?"
- **Data to pull:** the disruption's affected-unit count as a percentage of the total, and the recovery-tier runbook (if one exists).

### A forecast or model result reported without a sensitivity/what-if attached
- **Usually means:** the analyst treated the point estimate as the deliverable and skipped the "what if this assumption moves" question the sponsor will ask next, costing credibility in the room.
- **First question:** "Which single assumption is this recommendation most sensitive to, and what happens if it moves 10%?"
- **Data to pull:** a one-way sensitivity table on the top 2-3 input parameters against the recommended decision.
