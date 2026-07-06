# CONTEXT

## Current Task
157 roles total (115 spec-2, 42 legacy queued for upgrade), lint 0 errors. Repo blindspot sweep 2026-07-07: fixed physician-clinical-reasoning missing regulated-role disclaimer blockquote (rule 5 violation). Parity sets grown: financial-analyst 5→8 (money.SE, pruned 3 wrong-perspective personal-finance Qs), paralegal new (5, law.SE, procedure/discovery/citation-fit only), actuary new (5, stats.SE survival-analysis/risk). Financial-analyst+paralegal batch: 10W-0T-3L of 13 (77%; losses = GME short-squeeze, Motorola corporate-action history, fake-precedent citation, all genuine depth-variance). Actuary: 5W-0T-0L (100%). mediator↔law attempted, dropped — law.SE is general legal-dispute trivia, no coverage of actual mediation process-design questions (BATNA/caucus/impasse), same wrong-perspective failure as hr-people-manager. Parity now covers 7 of 157 roles.

## Key Decisions
- Trust = measured, not vouched: lint + counterfactual evals + parity-vs-practitioners are the quality floor; practitioner review is bonus.
- Growth levers: proof (grow parity sets) > coverage (Sonnet grinds roadmap). Distribution (posting to practitioner communities) dropped — not doing that.
- npm releases snapshot roles: bump version → owner runs npm publish (2FA) → git tag v<version>.
- Parity harvest quality bar includes perspective-fit, not just topic-fit: prune consumer/personal-finance or bystander-legal-trouble questions that don't match the role's professional vantage point (same reasoning that killed hr-people-manager parity).

## Next Steps
- Parity coverage still only 7 of 157 roles — grow more pairings (candidates: compliance-officer↔law, credit-analyst↔money; avoid general-legal-trivia SE sites for process-facilitation roles).
- Next eval spot-check due after ~10 more roles land.
- Confirm dead ~/.npmrc token revoked on npmjs.com (flagged 2026-07-06, still not confirmed).
