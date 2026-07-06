# CONTEXT

## Current Task
Foundation done (spec v2, lint CI, npm 0.3.0 published+tagged, CLAUDE.md bootstrap); Sonnet sessions add roles unattended via CONTRIBUTING.md's exact recipe. `/domain-expert` slash command shipped (7 tools), `scripts/check_links.py` in CI. 97 roles total; 7-role batch spot-checked with evals (10W-1T-3L vs baseline, losses = judge tiebreaks/harness limitation, not gaps). Parity sets grown: lawyer-contracts 5→12, data-scientist 8→11, product-manager 8→11, personal-financial-advisor new (3, via money.SE). 31W-2T-4L of 37 (89%) vs practitioners as of 2026-07-06; all 4 losses diagnosed as genuine depth-variance (2 repeat known cases: SIR modeling, ASA p-value controversy; 2 new: k-means SSE mechanics, standup-diagnosis depth) — left unchanged. hr-people-manager parity attempted earlier, dropped — workplace.SE skews employee-grievance questions, wrong perspective for a manager-facing role.

## Key Decisions
- Trust = measured, not vouched: lint + counterfactual evals + parity-vs-practitioners are the quality floor; practitioner review is bonus.
- Growth levers: proof (grow parity sets) > coverage (Sonnet grinds roadmap). Distribution (posting to practitioner communities) dropped — not doing that.
- npm releases snapshot roles: bump version → owner runs npm publish (2FA) → git tag v<version>.

## Next Steps
- Parity coverage still only 4 of 97 roles — grow more role/SE-site pairings (candidates: financial-analyst↔money, mediator/paralegal↔law) or add non-SE sources.
- Next eval spot-check due after ~10 more roles land.
- Confirm dead ~/.npmrc token revoked on npmjs.com (flagged 2026-07-06, not yet confirmed).
