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

[![npm](https://img.shields.io/npm/v/domain-experts.svg?color=black)](https://www.npmjs.com/package/domain-experts)
[![downloads](https://img.shields.io/npm/dm/domain-experts.svg?color=black)](https://www.npmjs.com/package/domain-experts)
[![lint](https://github.com/wonsukchoi/domain-experts/actions/workflows/lint.yml/badge.svg)](https://github.com/wonsukchoi/domain-experts/actions/workflows/lint.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-black.svg)](./LICENSE)
[![spec](https://img.shields.io/badge/authoring_spec-v2-black.svg)](./AUTHORING.md)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-black.svg)](./CONTRIBUTING.md)

Open source library of **job role definitions** — the actual mental models, decision thresholds, and failure modes of real practitioners, structured so any AI agent can load one and reason like that expert. Ask your agent to "review this contract" and it answers with a senior contracts attorney's clause playbook and fallback ladders, not a generalist's summary of the internet.

## Vision — one person, every expert

```
                              ┌───────────────────────┐
                              │   Y O U  +  A G E N T  │
                              └───────────┬───────────┘
                                          │
             ┌──────────────┬────────────┼────────────┬──────────────┐
             │              │            │            │              │
             ▼              ▼            ▼            ▼              ▼
        lawyer-        financial-    data-        marketing-    clinical-
        contracts      manager       scientist    strategist    research-
        │              │             │            │             coordinator
        redline the    defend the    read the     kill the      │
        MSA            runway call   A/B test     dead channel  flag the
                                      right                      deviation

        no résumé screened. no calendar. no invoice. no waiting room.
        just: which role does this task need — load it — reason as it.
```

Right now, doing something well outside your own lane means hiring, contracting, or outreach — finding a lawyer, waiting on a CFO's calendar, paying a marketing strategist's rate. That friction is a tax on every solo founder, every small team, every individual who hits a problem outside their expertise. Most people just don't do the thing, or do it badly.

An individual with an AI subscription — or a local model, no subscription at all — and this repo doesn't pay that tax. Load the CFO's actual reasoning for a runway call. Load the contracts lawyer's clause playbook for a redline. Load the clinical research coordinator's judgment for a protocol deviation. Swap roles per task, on demand, for the cost of inference instead of a hire. One person, one agent, the accumulated decision-making of hundreds of professions.

```
   ─────────────────────────────────────────────────────────────
    1 person + 1 agent + N roles  >  the org chart it replaces
   ─────────────────────────────────────────────────────────────
```

That's the actual endgame here, not a curiosity: the barrier between "I need an expert" and "I have one" collapses. It gets more true as coverage grows — 59 roles against 1,016 tracked occupations today; the roadmap exists so that gap closes, not so it stays interesting forever.

It doesn't replace judgment, accountability, or licensure where those legally have to sit with a human — every regulated role (law, medicine, finance) says so explicitly. It replaces the friction of not having access to the reasoning in the first place.

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
npx domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

No install needed — `npx` fetches it from npm. Using it often? `npm install -g domain-experts` and drop the `npx`.

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

## How we verify — transparent, no trust required

"Written by experts" is a claim; this repo ships the receipts instead. Four independent layers, all runnable by anyone from this checkout:

```
 layer 1  SOURCING      every threshold traces to a named practitioner
 (input)                source (books, standards, postmortems) or is
                        labeled a stated heuristic — see each role's
                        Sources section
 layer 2  MECHANICAL    scripts/lint_roles.py on every PR: schema,
 (CI)                   required sections, references/ trio, banned
                        filler phrases, real numbers in the worked
                        example — generic text fails the build
 layer 3  COUNTERFACTUAL evals/: same model answers the same scenario
 (measured)             with and without the role, blind judge scores
                        observable expert behaviors in random A/B order
 layer 4  PARITY        evals/parity/: skill answers real questions that
 (measured)             real practitioners already answered publicly —
                        blind judge compares head-to-head
```

Latest published runs (2026-07-06, Haiku 4.5 answering, Sonnet 5 judging blind, both harnesses):

- **Counterfactual:** skill wins **13/15 scenarios** (1 tie, 1 loss) — 72% of expert-behavior criteria hit vs the generalist baseline's 37%.
- **Parity vs humans:** skill answer preferred over the real practitioner's accepted Stack Exchange answer in **5 of 8** blind head-to-heads (small sample; question sets are growing — treat as a smoke signal, not a study).

Every result is reproducible: `python3 evals/run_evals.py` and `python3 evals/parity/run_parity.py`. When a role fails these, that's public too — the point is measurement, not marketing. Practitioner review remains the gold star on top (`metadata.maturity`), but the trust floor is measured, not vouched.

## Current roles

<!-- ROLE_COUNTS_START -->
**84 roles drafted** (80 mapped to an O*NET occupation, 4 custom; 42 at spec 2, 42 awaiting upgrade), across 10 categories:

- **design**: 2
- **engineering**: 14
- **finance**: 10
- **healthcare**: 5
- **legal**: 2
- **marketing**: 4
- **operations**: 39
- **other**: 4
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

1. Run: npx --yes domain-experts match "<my task>" --json
2. If it returns a confident match, install it:
   npx --yes domain-experts add <slug>
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
| **Claude Code** | `npx domain-experts add <slug>` — lands in `./.claude/skills/<slug>/`, picked up automatically as a skill. |
| **Codex CLI** | Same command with `--to .codex/skills/<slug>` (project) or `--to ~/.codex/skills/<slug>` (personal). New session picks it up. |
| **Cursor, Windsurf, Roo Code, Goose & other SKILL.md-compatible tools** | Same command with `--to <tool's skills directory>/<slug>` — check your tool's docs for the path. |
| **Tools that read `AGENTS.md`** (GitHub Copilot, Jules, Amp, Zed, …) | Install anywhere in the repo (e.g. `--to skills/<slug>`), then add one line to `AGENTS.md`: `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **Any chat AI (no shell)** | Open the role on GitHub, paste `SKILL.md` into the system prompt or custom instructions; paste `references/` files when the conversation needs the depth. |

Every install copies the full role — `SKILL.md` plus `references/` — so the deep playbooks travel with it.

### Automatic dispatch

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) is a meta-skill that removes even the `match` step — install it with `npx domain-experts add domain-expert-router`, load it once, and your agent finds the right role for "act as X" requests on its own, and says honestly when a role isn't covered.

### CLI reference

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
```

`match` scores roles by keyword overlap and reports a confident hit, low-confidence candidates, or an honest "not covered yet" — it does not silently guess. `--json` for programmatic use.

The npm package snapshots the role library at each release. For the unreleased bleeding edge, use `npx --yes github:wonsukchoi/domain-experts <command>` — same CLI, straight from `main`.

## Roadmap

[`ROADMAP.md`](./ROADMAP.md) is the master backlog — all 1,016 O*NET occupations, grouped by category, checked off as they're drafted. Use it to find an uncovered role instead of guessing what's missing.

## Contributing — this repo compounds

Every role added makes the router smarter, every correction reaches every user on the next release, and every eval question makes the quality bar harder to fake. A prompt you write for yourself dies with your session; a role you contribute here works for everyone, forever, and keeps improving after you leave. That's the whole bet: **1,016 occupations is not a solo project — it's a commons.**

Three ways in, any skill level:

1. **You work in a role we cover?** Read it. Anything wrong is a 2-minute [practitioner-correction issue](../../issues/new/choose) — the single most valuable contribution this project can receive. No PR skills needed.
2. **You want to write or upgrade a role?** Follow the exact recipe in [`CONTRIBUTING.md`](./CONTRIBUTING.md) — it's written so precisely that an LLM can execute it, so you and your AI assistant can do it together. The lint tells you if the structure falls short before any human reviews it. 42 legacy roles are [claimable right now](../../issues/1).
3. **You can't write but can find?** Harvest parity questions (`evals/parity/harvest_stackexchange.py`) or file a [role request](../../issues/new/choose) with the tasks you'd delegate to it.

If the spec fights a practitioner's reality, the spec loses — say so in your PR and we fix the spec.

## License

MIT — see [`LICENSE`](./LICENSE).

```
─────────────────────────────────────────────
 1,016 occupations. One repo. Every expert.
─────────────────────────────────────────────
```
