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

| Role | Path |
|---|---|
| Software Engineer (Backend) | [`roles/software-engineer/SKILL.md`](./roles/software-engineer/SKILL.md) |
| Product Manager | [`roles/product-manager/SKILL.md`](./roles/product-manager/SKILL.md) |
| Financial Analyst | [`roles/financial-analyst/SKILL.md`](./roles/financial-analyst/SKILL.md) |
| UX Designer | [`roles/ux-designer/SKILL.md`](./roles/ux-designer/SKILL.md) |
| Lawyer (Contracts / Commercial) | [`roles/lawyer-contracts/SKILL.md`](./roles/lawyer-contracts/SKILL.md) |
| Marketing Strategist | [`roles/marketing-strategist/SKILL.md`](./roles/marketing-strategist/SKILL.md) |
| Sales Account Executive (B2B) | [`roles/sales-account-executive/SKILL.md`](./roles/sales-account-executive/SKILL.md) |
| Data Scientist | [`roles/data-scientist/SKILL.md`](./roles/data-scientist/SKILL.md) |
| HR / People Manager | [`roles/hr-people-manager/SKILL.md`](./roles/hr-people-manager/SKILL.md) |
| DevOps / Site Reliability Engineer | [`roles/devops-sre/SKILL.md`](./roles/devops-sre/SKILL.md) |
| Customer Success Manager | [`roles/customer-success-manager/SKILL.md`](./roles/customer-success-manager/SKILL.md) |
| Accountant / Financial Controller | [`roles/accountant-controller/SKILL.md`](./roles/accountant-controller/SKILL.md) |
| Technical Recruiter | [`roles/technical-recruiter/SKILL.md`](./roles/technical-recruiter/SKILL.md) |
| Physician (Clinical Reasoning) | [`roles/physician-clinical-reasoning/SKILL.md`](./roles/physician-clinical-reasoning/SKILL.md) |

## Using a role with an agent

Point your agent (e.g. Claude Code's `Skill` tool, or any system prompt injection) at the relevant `SKILL.md`. The frontmatter (`name`, `description`) is written so agent harnesses can auto-match a role to a task; the body is the actual expert reasoning context.

## Roadmap

[`ROADMAP.md`](./ROADMAP.md) is the master backlog — all 1,016 O*NET occupations, grouped by category, checked off as they're drafted. Use it to find an uncovered role instead of guessing what's missing.

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md). Short version: pick a role (new or existing), fill in `TEMPLATE.md`'s sections with real first-principles substance, open a PR.

## License

MIT — see [`LICENSE`](./LICENSE).
