# Agent guide for this repo

This repo turns human job roles into agent-loadable skill files. If you're an AI agent working in this checkout, this is your map.

## What lives where

- `roles/<slug>/SKILL.md` — one role's reasoning core; `roles/<slug>/references/` — its deep-dive playbooks, red flags, vocabulary.
- `AUTHORING.md` — the canonical quality spec and LLM drafting pipeline. **Read it before writing or editing any role.** TEMPLATE.md is only the skeleton.
- `scripts/lint_roles.py` — mechanical checks; `scripts/generate_roadmap.py` — regenerates ROADMAP.md, the README role-count block, and `data/roles.json`.
- `bin/cli.js` — the `domain-experts` CLI (list/search/match/add).
- `skills/domain-expert-router/` — meta-skill that dispatches "act as X" requests to a role.

## Rules

1. New roles must be `spec: 2` per AUTHORING.md — SKILL.md + references/ trio, worked example with reconciling numbers, no idea stated twice. CI rejects legacy-format additions.
2. Order of operations when adding/renaming a role: write files → `git add roles/<slug>` → `python3 scripts/lint_roles.py <slug>` until clean → `python3 scripts/generate_roadmap.py` → commit everything together. The roadmap script counts only git-tracked roles; running it before `git add` skips your new role.
3. Never hand-edit the auto-generated blocks in ROADMAP.md or README.md (between START/END markers) or `data/roles.json`.
4. Don't invent numbers in role content. Specific thresholds trace to a named source or are labeled as stated heuristics.
5. Regulated roles (law, medicine, financial advice, tax, safety) carry the disclaimer blockquote — see `roles/lawyer-contracts/SKILL.md`.
6. Commit messages: `role: add <name>` / `role: improve <name> — <what>` for role work; plain imperative for infra.

## Release (npm)

The package `domain-experts` on npm ships the CLI **and the role library** — npm users are frozen at the last publish, so release after every meaningful role batch or CLI change:

1. Bump `version` in package.json (semver: role batches = minor, fixes = patch).
2. `npm publish` — **must be run by the maintainer**, not an agent: it triggers browser-based 2FA auth. Sanity-check the tarball listing npm prints (roles + references + data/roles.json + skills/ present).
3. `git tag v<version> && git push origin v<version>` and commit the version bump.
4. Keep README truthful: human commands are `npx domain-experts …`; commands inside the agent copy-paste prompt use `npx --yes …` (agents hang on npx's interactive confirm without it).

## Known pitfalls

- A parallel drafting session may be committing to `main` at any time — `git pull --rebase --autostash` before pushing; expect occasional races.
- `generate_roadmap.py` counts only git-tracked roles. Run it **after** `git add`, or your role is missing from the counts and CI fails.
- Branch protection requires the `lint` check on PRs; admin direct pushes bypass it (the "Bypassed rule violations" notice is expected).
- Don't wrap multi-line ASCII code blocks in `<div align="center">` — it centers each line independently and skews the art.

## Verify before you're done

```sh
python3 scripts/lint_roles.py          # 0 errors required
python3 scripts/generate_roadmap.py    # then confirm git diff is only your intended files
node bin/cli.js list >/dev/null        # CLI still parses every role
```
