---
description: Scan a project and suggest domain-expert skills it would benefit from, then draft the ones the user picks.
argument-hint: <absolute path to the project to scan>
---

Target project: "$ARGUMENTS"

Tell the user up front, in one line, that this reads local project files (stack, README, directory structure, recent commit messages) to propose suggestions, and nothing about the project itself is written anywhere or leaves this conversation.

1. Run the `scan-project` workflow (`.claude/workflows/scan-project.js`) via the Workflow tool, with `args: {projectPath: "$ARGUMENTS"}`.
2. Present the returned `suggestions` via AskUserQuestion as a multi-select: each option's label is the `need`, description shows the `rationale` and `confidence`, and any suggestion with `cli_confident: true` must say so explicitly (e.g. "already likely covered by `<cli_best_slug>`") since picking it will probably resolve to `use_existing` rather than draft something new.
3. For every need the user selects, run the `generate-role` workflow (`.claude/workflows/generate-role.js`, unmodified) with that exact need text as `args`, one at a time — not in parallel, so PR branches/commits don't race each other.
4. Report each result (use_existing / abandoned / shipped + PR link) as it completes. If the user selects nothing, say so and stop — no files change.
