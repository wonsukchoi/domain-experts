# CONTEXT

## Current Task
169 roles total, lint 0 errors, all pushed to main. 2026-07-07 (latest) session: drafted+shipped 4 roles closing O*NET Computer/Math blanks (web-administrator, statistician, biostatistician, business-intelligence-analyst). Grew parity to 10/169 (statistician↔stats 75%; compliance-officer/credit-analyst via public-domain regulator FAQs since SE gave wrong-perspective results — see Key Decisions). Fixed credit-analyst's flagged 33%→100% via 2 targeted heuristic additions. Then ran 8 batches of eval-scenario writing (7 roles/batch, 4 scenarios each, chronological-by-add-date order): ux-designer through brownfield-redevelopment-specialist — 56 roles covered. Eval scenario coverage now 119/169; 50 roles remain (next batch starts after `brownfield-redevelopment-specialist` in `/tmp/missing_chrono.txt` — regenerate via `git log --diff-filter=A --name-only -- 'roles/*/SKILL.md'` reversed, minus existing `evals/scenarios/*.json`, if that scratch file is gone).

## Key Decisions
- Trust = measured, not vouched: lint + counterfactual evals + parity-vs-practitioners are the quality floor.
- Confirmed pattern: generic SE sites (law, money) return wrong-perspective Q&A for institutional/regulatory-vantage roles — for these, public-domain regulator FAQs (FinCEN, Fed, FDIC, OCC) are a better parity source than harvest_stackexchange.py.
- Parity harvest quality bar includes perspective-fit, not just topic-fit — same rule that killed hr-people-manager/mediator parity.
- Eval scenario criteria are drawn from each role's own Common Failure Modes / Mental Models sections and deliberately avoid restating the SKILL.md's own Worked Example — keeps the eval testing transfer, not memorization.

## Next Steps
- Continue eval-scenario batching (7 roles/batch, 4 scenarios each) until all 169 covered — 50 remain.
- Parity coverage 10/169 — still the other major growth lever; grow more pairings when eval-scenario batching pauses.
- Confirm dead ~/.npmrc token revoked on npmjs.com (flagged 2026-07-06, still not confirmed).
