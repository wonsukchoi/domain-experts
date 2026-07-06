# CONTEXT

## Current Task
157 roles total (115 spec-2, 42 legacy queued for upgrade), lint 0 errors, all pushed to main. 2026-07-07 session: fixed physician-clinical-reasoning missing regulated-role disclaimer (rule 5). Parity grown to 7/157 roles: financial-analyst 5→8, paralegal new (5), actuary new (5) — 15W-0T-3L combined (83%), all losses genuine depth-variance. mediator↔law tried and dropped (wrong-perspective, same failure as hr-people-manager). Eval spot-check: wrote scenarios + ran for two 7-role engineering batches — frontend/mobile/platform/appsec/embedded-firmware/data/ml-engineer (16W-1T-4L, 76%), then software-qa-analyst/health-informatics-specialist/gis-technologist/network-architect/database-architect/digital-forensics-analyst/logistics-engineer (14W-1T-6L, 67%). Combined 30W-2T-10L of 42; every loss had tied or near-tied criteria hits (judge holistic preference, not a content gap) — left unchanged. 14 of 157 roles now have eval scenarios.

## Key Decisions
- Trust = measured, not vouched: lint + counterfactual evals + parity-vs-practitioners are the quality floor; practitioner review is bonus.
- Growth levers: proof (grow parity sets) > coverage (Sonnet grinds roadmap). Distribution (posting to practitioner communities) dropped — not doing that.
- npm releases snapshot roles: bump version → owner runs npm publish (2FA) → git tag v<version>.
- Parity harvest quality bar includes perspective-fit, not just topic-fit: prune consumer/personal-finance or bystander-legal-trouble questions that don't match the role's professional vantage point (same reasoning that killed hr-people-manager parity).

## Next Steps
- Parity coverage still only 7 of 157 roles — grow more pairings (candidates: compliance-officer↔law, credit-analyst↔money; avoid general-legal-trivia SE sites for process-facilitation roles).
- Eval scenarios still missing for 143 of 157 roles; keep batching 7 at a time, oldest/most-used roles first.
- Confirm dead ~/.npmrc token revoked on npmjs.com (flagged 2026-07-06, still not confirmed).
