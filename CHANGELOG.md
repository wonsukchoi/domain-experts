# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html): role batches bump minor, fixes bump patch.

npm releases are snapshots — `npx domain-experts` users get the role library as of the last publish, not `main`. Role counts below are what each tag ships.

## [Unreleased]

### Added
- 10 new spec-2 roles (79 total), including mental-health-counselor, high-school-teacher, graphic-designer, electrician, mechanical-engineer
- `SECURITY.md` — vulnerability reporting process and threat model (prompt injection in role content, CLI, npm supply chain)
- Repo `CLAUDE.md` session bootstrap and `CONTEXT.md` session-resume notes

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

[Unreleased]: https://github.com/wonsukchoi/domain-experts/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/wonsukchoi/domain-experts/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/wonsukchoi/domain-experts/releases/tag/v0.1.0
