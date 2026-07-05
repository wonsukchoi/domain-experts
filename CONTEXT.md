# CONTEXT

## Current Task
Foundation complete (spec v2, lint CI, evals, parity harness, npm 0.2.0 published); role drafting continues via parallel LLM sessions following CONTRIBUTING.md's exact recipe.

## Key Decisions
- Trust = measured, not vouched: lint CI + counterfactual evals (13/15) + parity vs real practitioners (5/8) replace expert verification as the quality floor.
- New roles must be spec: 2 (SKILL.md + references/ trio); 42 legacy roles tracked in pinned issue #1.
- npm releases snapshot roles: bump version → npm publish (owner only, 2FA) → git tag.

## Next Steps
- Retrofit legacy roles (issue #1); spot-check Sonnet-drafted batches every ~10 roles.
- Grow parity question sets per role before quoting win rates publicly.
- Republish npm after next meaningful role batch; revoke the npm token pasted in chat (2026-07-05).
