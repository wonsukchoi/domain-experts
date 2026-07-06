---
description: Batch re-score shipped domain-expert roles against AUTHORING.md and flag/deprecate stale ones.
argument-hint: "[batch size, default 10]"
---

Run the `audit-roles` workflow (`.claude/workflows/audit-roles.js`) via the Workflow tool. If "$ARGUMENTS" is a positive integer, pass `args: {batchSize: $ARGUMENTS}`; otherwise call it with no args (default batch of 10). Report which roles were stamped active, flagged needs-refresh, or deprecated, and the PR URL.
