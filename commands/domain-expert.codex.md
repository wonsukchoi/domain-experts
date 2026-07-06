---
description: Route a task to the best-matching domain-experts role and reason as that expert.
argument-hint: <task description>
---

Task: $ARGUMENTS

1. Run: `npx --yes domain-experts match "$ARGUMENTS" --json`
2. If `confident: true`:
   - Read the matched role's `SKILL.md` in full (path in `best.file`), and any `references/` files the task needs the depth of.
   - Mention which role you loaded, in one line, before answering.
   - Adopt its reasoning for the rest of this response: follow its Decision framework, apply its Mental models & heuristics, match its Communication style.
   - If `metadata.maturity` is `draft`, use it fully but don't claim practitioner review if asked.
3. If `confident: false`:
   - State plainly that no role covers this yet. Name the closest low-confidence candidates if any were returned.
   - Point at `ROADMAP.md` in the domain-experts repo for the nearest O*NET occupation, and mention a PR per `CONTRIBUTING.md` would add it.
   - Then answer the task as a generalist if that's clearly still wanted — flagged explicitly as improvised, not sourced from a vetted role.
4. Never blend step 2 and step 3 framing — a loaded role's answer and an improvised one must read as visibly different confidence levels.
