<div align="center">

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

</div>

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
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts     # installs into ./.claude/skills/
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
**52 roles drafted** (48 mapped to an O*NET occupation, 4 custom), across 9 categories:

- **design**: 1
- **engineering**: 6
- **finance**: 5
- **healthcare**: 1
- **legal**: 1
- **marketing**: 4
- **operations**: 30
- **product**: 1
- **sales**: 3

Browse all roles in [`roles/`](./roles/), or see [`ROADMAP.md`](./ROADMAP.md) for the full O*NET-backed checklist of what's covered and what's not.
<!-- ROLE_COUNTS_END -->

This block is auto-generated — run `python3 scripts/generate_roadmap.py` after adding/removing/re-mapping a role, don't hand-edit it.

## Using a role with an agent

**CLI:**

```sh
npx domain-experts list                              # browse all roles
npx domain-experts search lawyer                     # substring search
npx domain-experts match "review this like our CFO"  # best-guess role match for a natural ask
npx domain-experts add lawyer-contracts              # copies the role into ./.claude/skills/lawyer-contracts/
npx domain-experts add lawyer-contracts --to some/other/dir
```

`match` scores roles by keyword overlap and reports a confident hit, low-confidence candidates, or an honest "not covered yet" — it does not silently guess. Use `--json` to consume the result programmatically.

**Automatic dispatch:** [`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) is a meta-skill that does this end to end — point an agent at it once (e.g. load it as a Claude Code skill) and it will find the right role for "act as X" requests on its own, running `match` under the hood.

**Manual:** point your agent (e.g. Claude Code's `Skill` tool, or any system prompt injection) at the relevant `roles/<slug>/SKILL.md` directly. The frontmatter (`name`, `description`) is written so agent harnesses can auto-match a role to a task; the body is the expert reasoning context, and `references/` holds the depth the agent loads when the task calls for it.

## Roadmap

[`ROADMAP.md`](./ROADMAP.md) is the master backlog — all 1,016 O*NET occupations, grouped by category, checked off as they're drafted. Use it to find an uncovered role instead of guessing what's missing.

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md). Short version: pick a role (new or existing), write it to the [`AUTHORING.md`](./AUTHORING.md) spec, open a PR — the lint tells you if the structure falls short before a human ever reviews it. Practitioners with real experience in a role are the most valuable contributors this project can have: if the content fights your reality, your correction wins.

## License

MIT — see [`LICENSE`](./LICENSE).

<div align="center">

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```

</div>
