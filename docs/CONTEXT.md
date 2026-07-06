# CONTEXT

## Current Task
Foundation done (spec v2, lint CI, evals 13/15, parity 5/8, npm 0.2.0, CLAUDE.md bootstrap); Sonnet sessions now add roles unattended via CONTRIBUTING.md's exact recipe.

## Key Decisions
- Trust = measured, not vouched: lint + counterfactual evals + parity-vs-practitioners are the quality floor; practitioner review is bonus.
- Growth levers ranked: proof (grow parity sets) > distribution (post roles to practitioner communities) > coverage (Sonnet grinds roadmap).
- npm releases snapshot roles: bump version → owner runs npm publish (2FA) → git tag v<version>.

## Next Steps
- Spot-check Sonnet batches every ~10 roles; run evals on samples.
- Post 1-2 flagship roles to their profession's community for first practitioner corrections.
- Republish npm after next batch; revoke npm token pasted in chat 2026-07-05 if not done.
