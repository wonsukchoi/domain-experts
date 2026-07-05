```
██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
███████╗██╗  ██╗██████╗ ███████╗██████╗ ████████╗███████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝
█████╗   ╚███╔╝ ██████╔╝█████╗  ██████╔╝   ██║   ███████╗
██╔══╝   ██╔██╗ ██╔═══╝ ██╔══╝  ██╔══██╗   ██║   ╚════██║
███████╗██╔╝ ██╗██║     ███████╗██║  ██║   ██║   ███████║
╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝

            a l l   h u m a n   e x p e r t s
              i n t o   A I   a g e n t s
```

[![lint](https://github.com/wonsukchoi/domain-experts/actions/workflows/lint.yml/badge.svg)](https://github.com/wonsukchoi/domain-experts/actions/workflows/lint.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-black.svg)](./LICENSE)
[![spec](https://img.shields.io/badge/authoring_spec-v2-black.svg)](./AUTHORING.md)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-black.svg)](./CONTRIBUTING.md)

Open source library of **job role definitions** — the actual mental models, decision thresholds, and failure modes of real practitioners, structured so any AI agent can load one and reason like that expert. Ask your agent to "review this contract" and it answers with a senior contracts attorney's clause playbook and fallback ladders, not a generalist's summary of the internet.

```
you ─── "review this vendor contract"
              │
              ▼
   ┌──────────────────────┐        ┌─ roles/lawyer-contracts/ ──────────────┐
   │  domain-expert       │        │                                        │
   │  router              │───────▶│  SKILL.md      the reasoning core      │
   │  (finds the expert   │        │  references/                           │
   │   your task needs)   │        │   ├─ clause-playbook.md  fallbacks     │
   └──────────────────────┘        │   ├─ red-flags.md        smell tests   │
                                   │   └─ vocabulary.md       terms of art  │
                                   └────────────────────┬───────────────────┘
                                                        │
                                                        ▼
                                     agent reasons like a senior
                                     contracts attorney — thresholds,
                                     market positions, redline language
```

## Quick start

```sh
npx --yes github:wonsukchoi/domain-experts match "review this vendor contract like a lawyer"
npx --yes github:wonsukchoi/domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

Or skip the manual step entirely: load [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) once, and your agent detects which expert a task needs, pulls the role's full context automatically, and tells you honestly when a role isn't covered yet instead of improvising. You keep working; the right expertise shows up by itself.

## "Can't I just tell Claude to act like a CFO?"

You can — and you'll get a shallow imitation: the average of every job description on the internet, regenerated from scratch each session, different every time, verified by no one.

```
 ── prompt: "act as a CFO" ───────────┬── role: financial-manager ───────────
                                      │
  "I'd start by monitoring cash       │  "DSO went 48 → 56 days with no
   flow and key financial metrics,    │   billing-terms change. Show me the
   ensuring alignment between…"       │   five largest invoices past 60 days
                                      │   — and reconcile bookings to the
                                      │   change in deferred revenue, because
                                      │   flat deferred + 'record bookings'
                                      │   don't coexist."
 ─────────────────────────────────────┴───────────────────────────────────────
```

The difference, concretely:

- **Non-derivable content.** Every role must pass a non-derivability test: nothing that can be regenerated from the job title alone. What's left is the stuff prompting can't produce on demand — numeric red-flag thresholds, market-standard negotiation ranges, worked examples with arithmetic that reconciles, fallback positions in preference order.
- **A quality gate, not a single generation.** Roles are built through a multi-pass pipeline ([`AUTHORING.md`](./AUTHORING.md)) — see the diagram below. A one-line prompt gets none of that.
- **CI-enforced structure.** Every PR runs [`scripts/lint_roles.py`](./scripts/lint_roles.py): schema, required sections, resolving links, banned filler phrases, red-flag completeness, real numbers in the worked example. Generic job-description text fails the build.
- **It compounds.** Your ad-hoc prompt disappears when the session ends. These files accumulate practitioner corrections, carry a maturity ladder (`draft` → `reviewed-by-practitioner` → `mature`) and a versioned spec (`spec: 2` marks roles at the current bar), and get better with every PR. Fixes reach everyone.
- **Token-efficient by design.** Each role is a compact reasoning core (`SKILL.md`) plus on-demand depth (`references/`). The agent pays for depth only when the task needs it:

```
roles/financial-manager/
├─ SKILL.md            ◀ always loaded · identity, first principles,
│                        heuristics, worked example with real numbers
└─ references/         ◀ loaded on demand
   ├─ artifacts.md       filled 13-week cash forecast, board slide, scenarios
   ├─ red-flags.md       DSO +15% QoQ · GM −200bps · headroom <20% …
   └─ vocabulary.md      bookings vs billings vs revenue vs ARR …
```

## How roles are built

```
  named sources        draft to        adversarial         revise        score vs
  books · standards ─▶ AUTHORING ──▶  critique by a  ──▶  or contest ─▶  9-criterion ──▶ ship
  practitioners        spec           separate model      each defect    rubric
                                                                            │
                            below 14/18, or any zero:  ◀────────────────────┘
                            loop (max 2) — or the role does not ship
```

Every role follows the same contract, enforced by spec and CI:

1. **Three ship tests** — a practitioner reading it nods rather than shrugs; an agent with the role makes measurably different decisions than without; nothing in it is derivable from the job title alone.
2. **Fixed anatomy** — identity, first-principles core, conditional heuristics ("when X, default to Y unless Z"), an executable decision framework, common failure modes, and a worked example with real, reconciling numbers ending in the actual deliverable (the memo, the redline, the readout).
3. **References trio** — a deep-dive playbook/artifacts file with filled templates, `red-flags.md` (signal → what it means → first question → data to pull), and `vocabulary.md` (terms of art with the common misuse spelled out).
4. **Provenance** — sources are named; specific numbers trace to them or are labeled as stated heuristics. Regulated roles (law, medicine, finance) carry explicit disclaimers.
5. **O*NET backbone** — coverage tracks the U.S. Department of Labor's occupation taxonomy (1,016 occupations), so growth is systematic, not whatever seemed interesting that week.

Full spec, rubric, and the LLM drafting pipeline: [`AUTHORING.md`](./AUTHORING.md).

## Current roles

<!-- ROLE_COUNTS_START -->
**59 roles drafted** (55 mapped to an O*NET occupation, 4 custom), across 9 categories:

- **design**: 1
- **engineering**: 8
- **finance**: 5
- **healthcare**: 3
- **legal**: 1
- **marketing**: 4
- **operations**: 33
- **product**: 1
- **sales**: 3

Browse all roles in [`roles/`](./roles/), or see [`ROADMAP.md`](./ROADMAP.md) for the full O*NET-backed checklist of what's covered and what's not.
<!-- ROLE_COUNTS_END -->

This block is auto-generated — run `python3 scripts/generate_roadmap.py` after adding/removing/re-mapping a role, don't hand-edit it.

## Use it with your AI tool

`SKILL.md` is a cross-tool format — the same role file works in Claude Code, Codex CLI, Cursor, and 30+ other agents. Only the install directory differs.

### Zero setup: paste this into your agent

Copy this into Claude Code, Codex, Cursor, or any agent with shell access, describe your task at the bottom, and it installs the right expert on its own:

```text
Install a domain expert for my task from the open-source library
https://github.com/wonsukchoi/domain-experts :

1. Run: npx --yes github:wonsukchoi/domain-experts match "<my task>" --json
2. If it returns a confident match, install it:
   npx --yes github:wonsukchoi/domain-experts add <slug>
   (default target is ./.claude/skills/<slug>; if you are not Claude Code,
   pass --to <your skills directory>/<slug>, e.g. --to .codex/skills/<slug>)
3. Read the installed SKILL.md fully. Open files under references/ whenever
   the task needs the depth they cover. Then do my task reasoning as that
   expert — apply its thresholds, red flags, and decision framework.
4. If there is no confident match, tell me which roles came closest and
   continue as a generalist — do not pretend to be an expert the library
   does not have.

My task: <describe your task here>
```

### Per-tool install

| Tool | How |
|---|---|
| **Claude Code** | `npx --yes github:wonsukchoi/domain-experts add <slug>` — lands in `./.claude/skills/<slug>/`, picked up automatically as a skill. |
| **Codex CLI** | Same command with `--to .codex/skills/<slug>` (project) or `--to ~/.codex/skills/<slug>` (personal). New session picks it up. |
| **Cursor, Windsurf, Roo Code, Goose & other SKILL.md-compatible tools** | Same command with `--to <tool's skills directory>/<slug>` — check your tool's docs for the path. |
| **Tools that read `AGENTS.md`** (GitHub Copilot, Jules, Amp, Zed, …) | Install anywhere in the repo (e.g. `--to skills/<slug>`), then add one line to `AGENTS.md`: `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **Any chat AI (no shell)** | Open the role on GitHub, paste `SKILL.md` into the system prompt or custom instructions; paste `references/` files when the conversation needs the depth. |

Every install copies the full role — `SKILL.md` plus `references/` — so the deep playbooks travel with it.

### Automatic dispatch

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) is a meta-skill that removes even the `match` step — install it with `npx --yes github:wonsukchoi/domain-experts add domain-expert-router`, load it once, and your agent finds the right role for "act as X" requests on its own, and says honestly when a role isn't covered.

### CLI reference

```sh
npx --yes github:wonsukchoi/domain-experts list          # browse all roles
npx --yes github:wonsukchoi/domain-experts search lawyer # substring search
npx --yes github:wonsukchoi/domain-experts match "review this like our CFO" [--json]
npx --yes github:wonsukchoi/domain-experts add <slug> [--to dir]
```

`match` scores roles by keyword overlap and reports a confident hit, low-confidence candidates, or an honest "not covered yet" — it does not silently guess. `--json` for programmatic use.

## Roadmap

[`ROADMAP.md`](./ROADMAP.md) is the master backlog — all 1,016 O*NET occupations, grouped by category, checked off as they're drafted. Use it to find an uncovered role instead of guessing what's missing.

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md). Short version: pick a role (new or existing), write it to the [`AUTHORING.md`](./AUTHORING.md) spec, open a PR — the lint tells you if the structure falls short before a human ever reviews it. Practitioners with real experience in a role are the most valuable contributors this project can have: if the content fights your reality, your correction wins.

## License

MIT — see [`LICENSE`](./LICENSE).

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
