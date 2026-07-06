# CONTEXT

## Current Task
157 roles total (115 spec-2, 42 legacy queued for upgrade), lint 0 errors. Repo blindspot sweep 2026-07-07: fixed physician-clinical-reasoning missing regulated-role disclaimer blockquote (rule 5 violation). Parity sets grown: financial-analyst 5→8 (money.SE, pruned 3 wrong-perspective personal-finance Qs), paralegal new (5, law.SE, procedure/discovery/citation-fit only). New batch 10W-0T-3L of 13 (77%); losses (GME short-squeeze, Motorola corporate-action history, fake-precedent citation) all genuine depth-variance, left unchanged. Parity now covers 6 of 157 roles.

## Key Decisions
- Trust = measured, not vouched: lint + counterfactual evals + parity-vs-practitioners are the quality floor; practitioner review is bonus.
- Growth levers: proof (grow parity sets) > coverage (Sonnet grinds roadmap). Distribution (posting to practitioner communities) dropped — not doing that.
- npm releases snapshot roles: bump version → owner runs npm publish (2FA) → git tag v<version>.
- Parity harvest quality bar includes perspective-fit, not just topic-fit: prune consumer/personal-finance or bystander-legal-trouble questions that don't match the role's professional vantage point (same reasoning that killed hr-people-manager parity).

## Next Steps
- Parity coverage still only 6 of 157 roles — grow more pairings (data-scientist, product-manager, lawyer-contracts already done; try mediator↔law, actuary↔stats/money).
- Next eval spot-check due after ~10 more roles land.
- Confirm dead ~/.npmrc token revoked on npmjs.com (flagged 2026-07-06, still not confirmed).
