# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html): role batches bump minor, fixes bump patch.

npm releases are snapshots — `npx domain-experts` users get the role library as of the last publish, not `main`. Role counts below are what each tag ships.

## [Unreleased]

### Added
- `domain-experts init [slug...]` CLI subcommand — one-shot setup: installs the router skill, the `/domain-expert` command, and any named roles
- `domain-experts update [--to dir]` CLI subcommand — re-fetches every role installed under a skills directory from the library and reports updated/unchanged/skipped, so `add` no longer leaves a permanently static snapshot
- `domain-experts preview <slug>` CLI subcommand — prints a role's Identity + Worked example sections without installing it
- `evals/run_evals.py --backend openai|ollama|cli` — evals no longer locked to the `claude` CLI; run the same scenarios/judge against OpenAI-compatible APIs or local Ollama models
- `scripts/suggest_role_requests.py` + weekly `.github/workflows/role-requests.yml` — auto-opens `role-request` issues for uncovered O*NET occupations, ranked by `data/gap-log.jsonl` signal when present, deduped against already-open issues
- `scripts/lint_roles.py` now resolves every `../<slug>/...` cross-role link anywhere in a SKILL.md body (not just Going deeper), catching references to renamed or nonexistent roles

## [0.3.0] — 2026-07-06

### Added
- `domain-experts command --tool <id>` CLI subcommand — installs a `/domain-expert <task>` slash command/custom prompt across 7 tools (Claude Code, Codex CLI, Gemini CLI, Cursor, Windsurf, Roo Code, Amp) that runs `match`, loads the winning role, and reasons as that expert in one step; `--global` targets the tool's user-level directory instead of the project
- 23 new spec-2 roles (97 total): mental-health-counselor, high-school-teacher, graphic-designer, electrician, mechanical-engineer, actuary, database-administrator, penetration-tester, personal-financial-advisor, budget-analyst, mediator, paralegal, paramedic, real-estate-broker, sales-engineer, compliance-manager, regulatory-affairs-manager, loss-prevention-manager, funeral-home-manager, spa-manager, wind-energy-operations-manager, wind-energy-development-manager
- `SECURITY.md` — vulnerability reporting process and threat model (prompt injection in role content, CLI, npm supply chain)
- `scripts/check_links.py` — CI check for dead relative links across README/AGENTS/CONTRIBUTING/docs
- Repo `CLAUDE.md` session bootstrap and `CONTEXT.md` session-resume notes

### Fixed
- `match` command ranking: added IDF weighting (rare query words outweigh common ones) and plural/singular stemming so real-world phrasing (e.g. "review this vendor contract") reliably surfaces the right role instead of a coincidentally keyword-heavy wrong one

## [0.2.0] — 2026-07-06

### Added
- 15 new spec-2 roles (74 total)
- `references/` directories now included in npm installs
- Router skill (`skills/domain-expert-router/`) installable — dispatches "act as X" requests to a role
- `data/roles.json` machine-readable role index
- Parity harness: skill answers scored against real practitioners' published answers

### Changed
- Eval criteria sharpened to specificity-demanding form with strict judge
- CONTRIBUTING.md gained the verbatim-executable role recipe

## [0.1.0] — 2026-07-06

### Added
- First npm release: `domain-experts` CLI (`list` / `search` / `match` / `add`) and 59-role library
- Spec v2 authoring format (`AUTHORING.md`): SKILL.md + references trio, worked examples with reconciling numbers, dedup rule
- Lint CI (`scripts/lint_roles.py`) and roadmap generator (`scripts/generate_roadmap.py`)

[Unreleased]: https://github.com/wonsukchoi/domain-experts/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/wonsukchoi/domain-experts/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/wonsukchoi/domain-experts/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/wonsukchoi/domain-experts/releases/tag/v0.1.0
