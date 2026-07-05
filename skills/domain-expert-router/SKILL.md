---
name: domain-expert-router
description: Use whenever the user asks you to act as, consult, or reason like a specific job role/domain expert (e.g. "review this like a CFO," "what would a UX designer say," "act as a contracts lawyer") and this repo's roles/ directory is available. Finds the best-matching role SKILL.md and adopts it, or honestly reports the gap if none exists.
metadata:
  category: other
  maturity: draft
---

# Domain Expert Router

## What this does

This repo (`domain-experts`) is a growing library of job-role `SKILL.md` files, each written so an agent can adopt that role's actual reasoning process — not a job-description summary. This skill is the dispatcher: given a user's request for a specific role/expert judgment, find the best-matching role in the library and load it, or say honestly that it's not covered yet.

Only 24 of the ~1,016 O*NET occupations tracked in `ROADMAP.md` are drafted so far — a no-match result is the common case, not an edge case. Handle it as a first-class outcome, not an afterthought.

## Procedure

1. **Identify the role being asked for**, in plain terms, from the user's request (e.g. "review this contract like a lawyer" → role: contracts lawyer).

2. **Find the best match.** Run:
   ```sh
   npx domain-experts match "<the role/task in plain language>" --json
   ```
   (or, if the CLI isn't available, grep `roles/*/SKILL.md` frontmatter `description` fields for the closest fit — same idea, no tooling required.)

3. **If `confident: true`:**
   - Read the matched file in full (`best.file` from the JSON, or the path the CLI printed).
   - Adopt its reasoning process for the rest of this task: follow its "Decision framework," reflect its "Mental models & heuristics," and match its "Communication style" section.
   - Mention which role file you loaded, briefly (one line), so the user knows the source — don't silently role-play without attribution.
   - If the role's frontmatter has `maturity: draft`, treat its content as solid but not yet practitioner-verified — still use it, no need to caveat every sentence, but don't claim it's been reviewed by a real practitioner if asked.

4. **If `confident: false` (no strong match) — this is a hybrid response, not a dead end:**
   - **State the gap honestly first:** "No role for `<X>` in the repo yet." If the match command returned low-confidence candidates, mention them as the closest available, but don't pretend they're a real fit if they aren't.
   - **Point at how to close the gap:** check `ROADMAP.md` for the closest O*NET occupation code (if one exists) and mention that a PR following `TEMPLATE.md`/`CONTRIBUTING.md` would add it.
   - **Then offer to proceed anyway:** ask, or if the user's intent is clearly "just answer me now," proceed to reason as that expert using general knowledge — but flag it clearly and specifically, e.g. "Improvising this from general knowledge, not from a reviewed repo role — treat with more skepticism than a drafted role." Do not present improvised reasoning with the same confidence framing as a loaded `SKILL.md`.
   - Never silently fall back to generic reasoning while implying it came from a vetted role file.

## Why the honest-gap step matters

The whole point of this repo is that a loaded `SKILL.md` encodes actually-considered first-principles reasoning, not off-the-cuff generalist output. Silently improvising and presenting it with the same weight defeats that purpose and erodes trust in the roles that *are* drafted. Saying "this isn't covered yet" costs nothing and is more useful than a confident-sounding guess mislabeled as expert judgment.

## Example

> User: "Review this vendor contract like our in-house counsel would."

1. Role identified: contracts/commercial lawyer.
2. `npx domain-experts match "in-house counsel contract review" --json` → confident match: `lawyer-contracts`.
3. Read `roles/lawyer-contracts/SKILL.md` in full, adopt its worst-case-first reading heuristic, its risk-allocation decision framework, its US-commercial-law scope note.
4. Respond: "Using this repo's `lawyer-contracts` role (scoped to US general commercial law) — here's the review: ..."

> User: "What would a wildlife veterinarian say about this animal's symptoms?"

1. Role identified: wildlife veterinarian — not in `roles/`.
2. Match returns no confident hit.
3. Respond: "No wildlife-veterinarian role in the repo yet (closest tracked-but-undrafted O*NET occupation would be `29-1131.00` Veterinarians — check `ROADMAP.md`). Want me to reason through this from general knowledge anyway? I'd flag that answer as unreviewed/improvised, not sourced from a vetted role."
