# CONTEXT

## Current Task
163 roles total (121 spec-2, 42 legacy queued for upgrade), lint 0 errors, all pushed to main. 2026-07-07 (later) session: added 6 O*NET Computer/Math roles via /generate-role — computer-information-research-scientist (18/18), network-support-specialist (leaf of network-architect, 17/18), computer-user-support-specialist (18/18), network-systems-administrator (18/18), mathematician (18/18), operations-research-analyst (18/18). Computer Programmers (15-1251.00) resolved use_existing → software-engineer already covers it (coding/debug/test judgment same, only design-authorship scope differs). All 6 PRs (#9-#14) merged to main; each needed manual rebase + regenerate_roadmap.py to resolve generated-file conflicts (workflow branches were cut before prior PRs merged). Added `.dual-graph/` to .gitignore (MCP tool state was recurring as untracked noise).
Prior (2026-07-07 morning): fixed physician-clinical-reasoning missing regulated-role disclaimer (rule 5). Parity grown to 7/157 roles: financial-analyst 5→8, paralegal new (5), actuary new (5) — 15W-0T-3L combined (83%). mediator↔law tried and dropped (wrong-perspective). Eval spot-check across three 7-role batches: 44W-5T-14L of 63 (70%), losses mostly judge preference not skill-file gaps. 21 of 157 roles had eval scenarios (pre-batch count).

## Key Decisions
- Trust = measured, not vouched: lint + counterfactual evals + parity-vs-practitioners are the quality floor; practitioner review is bonus.
- Growth levers: proof (grow parity sets) > coverage (Sonnet grinds roadmap). Distribution (posting to practitioner communities) dropped — not doing that.
- npm releases snapshot roles: bump version → owner runs npm publish (2FA) → git tag v<version>.
- Parity harvest quality bar includes perspective-fit, not just topic-fit: prune consumer/personal-finance or bystander-legal-trouble questions that don't match the role's professional vantage point (same reasoning that killed hr-people-manager parity).

## Next Steps
- More O*NET coverage: Computer/Math group has blanks left (Web Administrators 15-1299.01, Statisticians 15-2041, Biostatisticians 15-2041.01, Business Intelligence Analysts 15-2051.01, etc).
- Parity coverage still only 7 of 163 roles — grow more pairings (candidates: compliance-officer↔law, credit-analyst↔money; avoid general-legal-trivia SE sites for process-facilitation roles).
- Eval scenarios still missing for ~142 of 163 roles; keep batching 7 at a time, chronological order.
- Confirm dead ~/.npmrc token revoked on npmjs.com (flagged 2026-07-06, still not confirmed).
