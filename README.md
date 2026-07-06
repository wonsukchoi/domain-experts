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

**[English](./README.md) | [한국어](./README.ko.md) | [日本語](./README.ja.md) | [简体中文](./README.zh-CN.md) | [Español](./README.es.md) | [Português](./README.pt-BR.md) | [हिन्दी](./README.hi.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Tiếng Việt](./README.vi.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | [Bahasa Indonesia](./README.id.md)**

Open source library of **job role definitions** — the actual mental models, decision thresholds, and failure modes of real practitioners, structured so any AI agent can load one and reason like that expert. Ask your agent to "review this contract" and it answers with a senior contracts attorney's clause playbook and fallback ladders, not a generalist's summary of the internet.

**Jump to:** [Quick start](#quick-start) · ["Why not just prompt it?"](#cant-i-just-tell-claude-to-act-like-a-cfo) · [Vision](#vision--one-person-every-expert) · [How roles are built](#how-roles-are-built) · [How we verify](#how-we-verify--transparent-no-trust-required) · [Current roles](#current-roles) · [Use with your tool](#use-it-with-your-ai-tool) · [Roadmap](#roadmap) · [Contributing](#contributing--this-repo-compounds)

## Quick start

```sh
npx domain-experts match "review this vendor contract like a lawyer"
npx domain-experts add lawyer-contracts   # installs into ./.claude/skills/
```

No install needed — `npx` fetches it from npm. Using it often? `npm install -g domain-experts` and drop the `npx`.

**Using Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code, or Amp?** `npx domain-experts command --tool <id>` installs a `/domain-expert` slash command for it — restart your session and run `/domain-expert review this vendor contract`. It matches, loads, and reasons as the right role in one step, no manual `match`/`add` dance.

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

### So what's the actual moat?

Fair pushback: none of the above stops someone from `git clone`-ing this exact repo and shipping it as their own product — MIT license, zero content lock-in. Honest answer: the file set is not the moat. What's hard to fork is the machine that keeps producing and correcting it:

- **The pipeline, not the output.** Copying 97 files takes one command. Copying the adversarial-critique → 9-criterion-rubric → lint-gated authoring loop ([`AUTHORING.md`](./AUTHORING.md)) that keeps producing and correcting them does not — a fork inherits today's snapshot, not tomorrow's fixes.
- **A standard, not a database.** `SKILL.md` already runs in 30+ agent tools. Being the largest library in a portable open format is a distribution position, not a content position — the value is in being the default answer people find, not in the bytes themselves.
- **Verified, not claimed.** Every competitor can say "written by experts." Few can run `python3 evals/run_evals.py` in front of you and show 13/15 counterfactual wins. Trust here is measured and reproducible, not asserted.
- **Freshness beats parametric recall.** Even if a future model trains on this repo's public text, that knowledge freezes at the training cutoff. This repo's corrections ship the day a practitioner files them — no retrain cycle, versioned, traced to a source.
- **Coverage discipline.** O*NET's 1,016-occupation backbone forces systematic long-tail coverage (funeral-home-manager, wind-energy-operations-manager) that an opportunistic competitor curating only trending roles won't bother matching.
- **Free and portable beats subscription-locked.** This doesn't compete with your LLM bill — you still pay for inference either way. It competes with closed vertical SaaS ("AI Legal Advisor," $99/mo): those can't match free, forkable, and runnable on a local model with zero recurring cost.

None of this is a moat yet at 97 roles and a small contributor base — it's a trajectory. The bet: the commons compounds faster than any single fork can keep pace with, once enough practitioners are filing corrections instead of writing prompts from scratch each session.

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

That's the actual endgame here, not a curiosity: the barrier between "I need an expert" and "I have one" collapses. It gets more true as coverage grows — 92 roles against 1,016 tracked occupations today; the roadmap exists so that gap closes, not so it stays interesting forever.

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

Full spec, rubric, and the LLM drafting pipeline: [`AUTHORING.md`](./AUTHORING.md). In a Claude Code checkout, this whole pipeline runs as `/generate-role "<need>"` — see [Maintainer automation](#maintainer-automation-claude-code) below.

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
**161 roles drafted** (151 mapped to an O*NET occupation, 10 custom; 119 at spec 2, 42 awaiting upgrade), across 10 categories:

**O\*NET coverage:** `███░░░░░░░░░░░░░░░░░` 14.9% (151 / 1,016 occupations)

- **design**: 3
- **engineering**: 33
- **finance**: 21
- **healthcare**: 10
- **legal**: 18
- **marketing**: 5
- **operations**: 58
- **other**: 7
- **product**: 1
- **sales**: 5

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

**Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Roo Code, and Amp users:** skip the paste — `npx domain-experts command --tool <id>` installs `/domain-expert` once, then just run `/domain-expert <task>` each time (see [`/domain-expert` slash command](#domain-expert-slash-command) below).

### Per-tool install

| Tool | How |
|---|---|
| **Claude Code** | `npx domain-experts add <slug>` — lands in `./.claude/skills/<slug>/`, picked up automatically as a skill. |
| **Codex CLI** | Same command with `--to .codex/skills/<slug>` (project) or `--to ~/.codex/skills/<slug>` (personal). New session picks it up. |
| **Cursor** | Same command with `--to .cursor/skills/<slug>` — Cursor reads the same `SKILL.md` format natively. |
| **Windsurf, Roo Code, Goose & other SKILL.md-compatible tools** | Same command with `--to <tool's skills directory>/<slug>` — check your tool's docs for the path. |
| **Tools that read `AGENTS.md`** (GitHub Copilot, Jules, Amp, Zed, …) | Install anywhere in the repo (e.g. `--to skills/<slug>`), then add one line to `AGENTS.md`: `When a task needs <role> judgment, read skills/<slug>/SKILL.md first.` |
| **Any chat AI (no shell)** | Open the role on GitHub, paste `SKILL.md` into the system prompt or custom instructions; paste `references/` files when the conversation needs the depth. |

Every install copies the full role — `SKILL.md` plus `references/` — so the deep playbooks travel with it.

### Automatic dispatch

[`skills/domain-expert-router/SKILL.md`](./skills/domain-expert-router/SKILL.md) is a meta-skill that removes even the `match` step — install it with `npx domain-experts add domain-expert-router`, load it once, and your agent finds the right role for "act as X" requests on its own, and says honestly when a role isn't covered.

### `/domain-expert` slash command

```sh
npx domain-experts command --tool <id>   # claude (default), codex, gemini, cursor, windsurf, roo, amp
```

Restart your session, then use `/domain-expert <task>` directly — e.g. `/domain-expert review this vendor contract`. It runs `match`, loads the winning role's `SKILL.md` (and `references/` as needed), and answers as that expert, or tells you honestly when nothing matches yet. Same idea as the router skill above, packaged as a one-shot command instead of an always-loaded skill.

| `--tool` | Installs to | Notes |
|---|---|---|
| `claude` (default) | `.claude/commands/domain-expert.md` | |
| `codex` | `~/.codex/prompts/domain-expert.md` | Codex only reads prompts from the user-level dir, no project-local option; OpenAI's docs mark this mechanism deprecated in favor of "skills" but it still works |
| `gemini` | `.gemini/commands/domain-expert.toml` | TOML format |
| `cursor` | `.cursor/commands/domain-expert.md` | |
| `windsurf` | `.windsurf/workflows/domain-expert.md` | Windsurf calls these "workflows" |
| `roo` | `.roo/commands/domain-expert.md` | |
| `amp` | `.agents/commands/domain-expert.md` | Amp's location is fixed at the repo root, no separate global directory |

Add `--global` to install to the tool's user-level directory (e.g. `~/.claude/commands/`, `~/.cursor/commands/`) instead of the project directory, or `--to <path>` for a fully custom location.

### CLI reference

```sh
npx domain-experts list          # browse all roles
npx domain-experts search lawyer # substring search
npx domain-experts match "review this like our CFO" [--json]
npx domain-experts add <slug> [--to dir]
npx domain-experts command [--tool <id>] [--global] [--to path]  # install the /domain-expert command
```

`match` scores roles by keyword overlap and reports a confident hit, low-confidence candidates, or an honest "not covered yet" — it does not silently guess. `--json` for programmatic use.

The npm package snapshots the role library at each release. For the unreleased bleeding edge, use `npx --yes github:wonsukchoi/domain-experts <command>` — same CLI, straight from `main`.

### Maintainer automation (Claude Code)

Working in a Claude Code checkout of this repo adds three slash commands that automate the pipeline above rather than replace it — every one is human-PR-gated, none commits to `main` or publishes on its own:

- `/generate-role "<need>"` — resolves a free-text need to an existing role, a new specialization leaf, or a new parent role, then runs the AUTHORING.md Pass 0-4 pipeline (research → draft → adversarial critique → score, capped at 2 revision loops) and opens a PR.
- `/audit-roles [batchSize]` — batched re-score of shipped roles against the rubric and source currency; stamps `last_audited`/`audit_score`, flags `status: needs-refresh`, deprecates (moves to `roles/_deprecated/`) after a second consecutive failure.
- `/scan-project <path>` — read-only scan of an external project (stack, README, structure, recent commits), proposes candidate needs cross-checked against existing coverage, and hands the ones you pick to `/generate-role`. Nothing about the scanned project is written anywhere.

Non-confident `match` queries are logged to `data/gap-log.jsonl` and surfaced, ranked by frequency, in [`ROADMAP.md`](./ROADMAP.md)'s "Requested but missing" section — a concrete signal for what to draft next.

## Roadmap

[`ROADMAP.md`](./ROADMAP.md) is the master backlog — all 1,016 O*NET occupations, grouped by category, checked off as they're drafted. Use it to find an uncovered role instead of guessing what's missing.

## Contributing — this repo compounds

Every role added makes the router smarter, every correction reaches every user on the next release, and every eval question makes the quality bar harder to fake. A prompt you write for yourself dies with your session; a role you contribute here works for everyone, forever, and keeps improving after you leave. That's the whole bet: **1,016 occupations is not a solo project — it's a commons.**

Common questions (lint failures, push conflicts, release process) → [`docs/FAQ.md`](./docs/FAQ.md).

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
