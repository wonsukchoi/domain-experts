# CONTEXT

## Current Task
169 roles total, lint 0 errors, all pushed to main. 2026-07-07 (latest) session: drafted+shipped 4 roles closing the O*NET Computer/Math group blanks — web-administrator, statistician, biostatistician, business-intelligence-analyst (all spec-2, PR merged directly since drafted/linted in-session, not via /generate-role workflow). Then grew parity: statistician↔stats.stackexchange (good fit, 3W-0T-1L, 75%). compliance-officer↔law and credit-analyst↔money both failed again on SE (wrong professional vantage — general legal trivia / consumer personal-finance), so sourced from public-domain interagency regulatory FAQs instead (FinCEN joint SAR guidance; Fed/FDIC/OCC leveraged-lending + ALLL guidance) — compliance-officer 3W-0T-0L (100%), credit-analyst 1W-0T-2L (33%, losses show role file lacks worked-example specificity vs. real regulator answers).
Prior (2026-07-07 morning): fixed physician-clinical-reasoning missing regulated-role disclaimer. Parity was 7/163: financial-analyst 5→8, paralegal new (5), actuary new (5) — 15W-0T-3L (83%). mediator↔law dropped (wrong-perspective). Eval spot-check: 44W-5T-14L of 63 (70%).

## Key Decisions
- Trust = measured, not vouched: lint + counterfactual evals + parity-vs-practitioners are the quality floor.
- Confirmed pattern: generic SE sites (law, money) return wrong-perspective Q&A for institutional/regulatory-vantage roles (compliance-officer, credit-analyst, earlier mediator) — for these, public-domain regulator FAQs (FinCEN, Fed, FDIC, OCC) are a better parity source than harvest_stackexchange.py.
- Parity harvest quality bar includes perspective-fit, not just topic-fit — same rule that killed hr-people-manager/mediator parity.

## Next Steps
- Parity coverage now 10/169 — grow more pairings; credit-analyst's 33% result flags a real gap (worked-example depth) worth a role revision, not just more questions.
- Eval scenarios still missing for ~148 of 169 roles; keep batching 7 at a time, chronological order.
- Confirm dead ~/.npmrc token revoked on npmjs.com (flagged 2026-07-06, still not confirmed).
