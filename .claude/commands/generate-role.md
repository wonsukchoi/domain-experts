---
description: Resolve a need to a domain-expert role (existing, new leaf, or new parent) and draft it via the AUTHORING.md pipeline, opening a PR.
argument-hint: <free-text need, e.g. "agent for 2D mobile puzzle game dev">
---

Run the `generate-role` workflow (`.claude/workflows/generate-role.js`) via the Workflow tool, with `args` set to the literal task text: "$ARGUMENTS". Report the resulting status (use_existing / abandoned / shipped) and, if shipped, the PR URL.
