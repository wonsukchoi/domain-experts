# Operations Research Analyst — Playbook

## Safety-stock / staffing sizing (filled example)

| Step | Calculation | Value |
|---|---|---|
| Mean weekly demand (D) | | 1,200 units |
| Demand std dev (σ_D) | | 220 units |
| Replenishment lead time (L) | | 4 weeks |
| Stockout severity check | contractual penalty clause, not discretionary retail | escalate service level |
| Baseline safety stock (95%, Z = 1.65) | SS = 1.65 × 220 × 2.0 | 726 units |
| Service level chosen | 99% (Z = 2.33), justified above | |
| **Safety stock** | SS = Z × σ_D × √L = 2.33 × 220 × 2.0 | **1,025 units** |
| Unit cost | | $18 |
| Holding cost rate | | 22%/year |
| **Incremental annual holding cost vs. 95% baseline** | (1,025 − 726) × $18 × 0.22 | **$1,184/year** |

**Escalation checklist — when to move off the 95% default:**
1. Is the stockout consequence contractual, safety-related, or single point of failure? If yes → escalate toward 99% (Z = 2.33) or higher; if no → hold at 95% (Z = 1.65).
2. Quantify the incremental holding cost of the escalation (never state the escalation without this number).
3. Pull 12+ months of stockout-event history at the current policy; multiply event count by known cost-per-event (expedite fee, penalty, lost throughput).
4. Compare incremental holding cost against averted stockout cost — only escalate the SKUs/lanes where the net is positive.
5. Write the decision as a targeted exception, named by SKU or lane, not a blanket policy change.

## LP/MIP formulation checklist (before handing to solver)

1. State the decision variables in the units the sponsor will recognize (units shipped, hours staffed, lots produced) — not abstract indices only.
2. State the objective function and confirm it is the sponsor's actual cost/profit driver, not a proxy that's merely correlated with it.
3. List every constraint with its right-hand-side value and units; flag any constraint whose RHS was guessed rather than pulled from a system of record.
4. For every binary/integer "on-off" constraint requiring a Big-M term, size M from the tightest valid bound in the data:
   - Pull the max value the constrained variable can actually take in this problem instance.
   - Set M to that bound plus a small buffer (e.g., 10%), never a round "safe" number like 10,000 or 10^6.
   - Document the M value and its derivation next to the constraint — a reviewer must be able to check it without re-deriving it.
5. Solve the LP relaxation first; if the relaxation gap to the best-known integer solution is already tight (<2%), a fast heuristic may suffice without full MIP.
6. Run the full MIP; record optimality gap, node count, and wall-clock time — not just the objective value.

## Solver triage table (filled example)

| Symptom | Likely cause (ranked) | First check |
|---|---|---|
| Gap stuck >5% after 10x expected runtime | (1) Big-M too large, (2) weak formulation lacking valid cuts, (3) genuinely hard instance | Recompute M from tightest data bound; rerun |
| Solver returns "feasible" but a constraint is visibly violated on inspection | (1) Floating-point tolerance masking violation, (2) Big-M sized near numerical precision limit (e.g. M > 10^9) | Rerun with tolerance tightened by 10x; check M magnitude |
| Node count grows near-exponentially past a known problem size | (1) Missing symmetry-breaking constraints, (2) formulation branches on a variable with too many near-equal-value options | Add symmetry-breaking constraint; re-profile branching variable choice |
| Objective value swings >3% between reruns with identical input | (1) Solver using a non-deterministic parallel search, (2) tie-breaking on a near-degenerate optimum | Fix random seed / thread count; report the tie explicitly rather than treat one run as canonical |

**Escalation rule:** if gap is still >5% after checking all four rows, decompose the problem (see below) before adding more solver time — more compute on the wrong formulation is a sunk-cost trap.

## Decomposition checklist (when one model is intractable)

1. List the natural subproblems (e.g., allocation, timing, recovery) and whether each has its own well-understood solution method.
2. Check whether subproblems share only a small number of linking variables/constraints — if the linkage is thin, decomposition is likely to pay off; if every constraint links every subproblem, decomposition won't help.
3. Solve each subproblem independently with its fitted method (e.g., overbooking model, discount-allocation LP, traffic-management heuristic).
4. Reconcile: pass each subproblem's output as an input/bound to the others and iterate until the linking variables stop changing materially (e.g., <1% shift) between passes.
5. Report the reconciled joint solution's total objective alongside each subproblem's individual objective, so a reviewer can see where the value came from.

## Disruption recovery decision (filled example)

| Disruption scale | Recovery approach | Rationale |
|---|---|---|
| Single resource down, <10% of affected units | Patch by hand on the affected subset | Full re-solve too slow to matter; manual patch is fast and feasibility-checkable at this scale |
| Multi-resource disruption, 10–40% of affected units | Re-solve the affected subproblem only (not the full schedule) | Mirrors CrewSolver-style recovery — bounded re-solve keeps runtime inside the same-day clock while respecting downstream feasibility |
| System-wide disruption, >40% of affected units or safety-critical | Re-solve from scratch, escalate immediately | At this scale a partial re-solve risks missing global infeasibilities; full re-optimization is worth the runtime cost |

**Use:** Decide the recovery tier before the disruption happens, not during it — name who owns the call and what percentage threshold triggers each tier in the model's operating runbook.

## Recommendation memo — filled example

Uses the safety-stock sizing table above (D = 1,200, σ = 220, L = 4 weeks, $18/unit, 22%/year holding), for a component covered by a customer contract with a per-stockout penalty clause rather than a discretionary late-shipment cost.

> **Recommendation: Component X safety stock — 95% → 99% service level (this lane only)**
> Current policy: 726 units (95%, Z=1.65). Proposed: 1,025 units (99%, Z=2.33).
> Incremental holding cost: $1,184/year. Contractual-penalty history at 95% service: ~5 stockout events/year × $2,100/event ≈ $10,500/year. At 99% service, expected stockouts fall to ~1/year: ~$2,100/year in penalty exposure.
> **Net saving: ~$7,216/year** ($10,500 − $2,100 = $8,400 avoided penalty, less the $1,184 incremental holding cost), before counting the customer-relationship cost of a breach, which the penalty clause alone does not price.
> This is a targeted exception for this lane, not a policy-wide change — applying 99% broadly would add holding cost across lanes where the stockout consequence is an internal reshuffle, not a contractual penalty.
