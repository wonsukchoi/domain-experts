# Domain Experts — session bootstrap

Before doing ANY work in this repo, read these three files in full, in this order:

1. `AGENTS.md` — what lives where, the rules, release checklist, known pitfalls
2. `CONTRIBUTING.md` — especially the "Exact recipe for adding a role (follow verbatim)" section
3. `docs/CONTEXT.md` — where the last session left off

## Non-negotiables when adding or editing roles

- New roles are `spec: 2` per `AUTHORING.md`: SKILL.md + `references/` trio, worked example with real reconciling numbers, each idea stated exactly once.
- Order of operations: write files → `git add roles/<slug>` → `python3 scripts/lint_roles.py <slug>` until 0 errors → `python3 scripts/generate_roadmap.py` → commit everything together → `git pull --rebase --autostash` → push.
- Never hand-edit generated content: README role-count block, ROADMAP checklist, `data/roles.json`.
- Another session may be pushing to `main` concurrently — always pull --rebase --autostash before push.
- Quality bar: a practitioner should nod, not shrug. If a role would ship generic, skip it and pick another — an empty slot is recoverable, a generic role poisons trust.
