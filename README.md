# Domain Experts

*All human experts into AI agents.*

Open source, crowd-sourced library of **job role definitions** — written from first principles by (or with review from) real practitioners — structured so any AI agent can load one and act as that domain expert.

## Why

LLM agents are generalists. Ask one to "think like a CFO" or "review this like a senior backend engineer" and you get a shallow imitation. This repo is an attempt to fix that by crowdsourcing the actual mental models, decision frameworks, heuristics, and blind spots that real practitioners in a role use — not job-description fluff.

Each role is written as a self-contained **skill file** (`SKILL.md`) that an AI agent (Claude Code, or any agent framework that supports skill/tool-style context injection) can load to adopt that role's reasoning process.

## How it works

- Every role lives in `roles/<role-slug>/SKILL.md`.
- Roles follow the schema in [`TEMPLATE.md`](./TEMPLATE.md): identity, first-principles core, mental models, decision frameworks, tools/methods, communication style, common failure modes, and sources.
- Anyone can open a PR to add a new role, or improve an existing one. Practitioners with real experience in the role are especially welcome — call this out in your PR.
- Quality bar: prefer *how an expert actually thinks and decides* over generic responsibility lists you could get from a job posting.

## Current roles

<!-- ROLE_COUNTS_START -->
**29 roles drafted** (25 mapped to an O*NET occupation, 4 custom), across 9 categories:

- **design**: 1
- **engineering**: 4
- **finance**: 4
- **healthcare**: 1
- **legal**: 1
- **marketing**: 4
- **operations**: 10
- **product**: 1
- **sales**: 3

Browse all roles in [`roles/`](./roles/), or see [`ROADMAP.md`](./ROADMAP.md) for the full O*NET-backed checklist of what's covered and what's not.
<!-- ROLE_COUNTS_END -->

This block is auto-generated — run `python3 scripts/generate_roadmap.py` after adding/removing/re-mapping a role, don't hand-edit it.

## Using a role with an agent

**CLI (recommended):**

```sh
npx domain-experts list                              # browse all roles
npx domain-experts search lawyer                     # substring search
npx domain-experts match "review this like our CFO"  # best-guess role match for a natural ask
npx domain-experts add lawyer-contracts              # copies SKILL.md into ./.claude/skills/lawyer-contracts/
npx domain-experts add lawyer-contracts --to some/other/dir
```

`match` scores roles by keyword overlap and reports a confident hit, low-confidence candidates, or an honest "not covered yet" — it does not silently guess. Use `--json` to consume the result programmatically.

**Automatic dispatch:** [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) is a meta-skill that does this end to end — point an agent at it once (e.g. load it as a Claude Code skill) and it will find the right role for "act as X" requests on its own, running `match` under the hood, and will tell you honestly (rather than improvise silently) when a requested role isn't in the library yet.

**Manual:** point your agent (e.g. Claude Code's `Skill` tool, or any system prompt injection) at the relevant `roles/<slug>/SKILL.md` directly. The frontmatter (`name`, `description`) is written so agent harnesses can auto-match a role to a task; the body is the actual expert reasoning context.

## Roadmap

[`ROADMAP.md`](./ROADMAP.md) is the master backlog — all 1,016 O*NET occupations, grouped by category, checked off as they're drafted. Use it to find an uncovered role instead of guessing what's missing.

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md). Short version: pick a role (new or existing), fill in `TEMPLATE.md`'s sections with real first-principles substance, open a PR.

## License

MIT — see [`LICENSE`](./LICENSE).
