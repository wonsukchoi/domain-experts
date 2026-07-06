# CONTEXT

## Current Task
Foundation done (spec v2, lint CI, evals 13/15, npm 0.2.0, CLAUDE.md bootstrap); Sonnet sessions now add roles unattended via CONTRIBUTING.md's exact recipe. Growing parity sets: lawyer-contracts/data-scientist/product-manager at 5/8/8 questions, 16W-0T-4L (80%) vs practitioners as of 2026-07-06; all 4 losses diagnosed as genuine depth-variance on edge-case/meta questions, not content gaps — left unchanged. hr-people-manager attempted, dropped — workplace.SE skews employee-grievance questions, wrong perspective for a manager-facing role. Added `/domain-expert` slash command (7 tools: claude/codex/gemini/cursor/windsurf/roo/amp) and `scripts/check_links.py` in CI. 7-role batch (compliance-manager, regulatory-affairs-manager, loss-prevention-manager, funeral-home-manager, spa-manager, wind-energy-operations-manager, wind-energy-development-manager) spot-checked with 2 eval scenarios each (14 total): 10W-1T-3L vs baseline. All 3 losses were criteria ties resolved by judge overall-preference tiebreak (fhm-1, fhm-2, lpm-1) — one loss (fhm-1) traced to baseline knowing casket-price-list/CPL detail that's already in `references/playbook.md` but not loaded in the eval harness (SKILL.md only) — a harness limitation, not a role gap. Left roles unchanged.

## Key Decisions
- Trust = measured, not vouched: lint + counterfactual evals + parity-vs-practitioners are the quality floor; practitioner review is bonus.
- Growth levers: proof (grow parity sets) > coverage (Sonnet grinds roadmap). Distribution (posting to practitioner communities) dropped — not doing that.
- npm releases snapshot roles: bump version → owner runs npm publish (2FA) → git tag v<version>.

## Next Steps
- Republish npm (0.2.0 → next, includes /domain-expert command + 7 new roles); local ~/.npmrc dead token removed 2026-07-06, confirm revoked on npmjs.com too.
- Parity sets starved (3 questions/1 result vs 97 roles) — grow these before adding more roles.
- Next spot-check due after ~10 more roles land.
