# CONTEXT

## Current Task
169 roles total, lint 0 errors, all pushed to main. 2026-07-07 session: drafted+shipped 4 roles closing O*NET Computer/Math blanks (web-administrator, statistician, biostatistician, business-intelligence-analyst). Grew parity to 10/169 (statistician↔stats 75%; compliance-officer/credit-analyst via public-domain regulator FAQs since SE gave wrong-perspective results). Fixed credit-analyst's flagged 33%→100% via 2 targeted heuristic additions. Then ran 14 batches of eval-scenario writing (4 scenarios/role) — **eval scenario coverage is now complete: 169/169 roles.**

## Key Decisions
- Trust = measured, not vouched: lint + counterfactual evals + parity-vs-practitioners are the quality floor.
- Confirmed pattern: generic SE sites (law, money) return wrong-perspective Q&A for institutional/regulatory-vantage roles — for these, public-domain regulator FAQs (FinCEN, Fed, FDIC, OCC) are a better parity source than harvest_stackexchange.py.
- Parity harvest quality bar includes perspective-fit, not just topic-fit — same rule that killed hr-people-manager/mediator parity.
- Eval scenario criteria are drawn from each role's own Common Failure Modes / Mental Models sections and deliberately avoid restating the SKILL.md's own Worked Example — keeps the eval testing transfer, not memorization.

## Next Steps
- Eval scenario authoring is done (169/169) — next lever is actually *running* `evals/run_evals.py` across the full set and reading results, not writing more scenarios.
- Parity coverage still only 10/169 — the main remaining growth lever; grow more pairings, watching for the wrong-perspective trap on institutional/regulatory roles.
- Confirm dead ~/.npmrc token revoked on npmjs.com (flagged 2026-07-06, still not confirmed).
