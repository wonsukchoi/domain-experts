# Role template

Copy this structure to `roles/<role-slug>/`. The quality bar and per-section spec live in [`AUTHORING.md`](./AUTHORING.md) — read it first; this file is only the skeleton.

```
roles/<role-slug>/
  SKILL.md
  references/
    playbook.md        # or artifacts.md — see AUTHORING.md naming rule
    red-flags.md
    vocabulary.md
```

## SKILL.md skeleton

```markdown
---
name: role-slug-here
description: Use when a task needs the judgment of a <Role> — <3-5 concrete task types this role handles, comma-separated>. This is what harnesses match against; name tasks, not capabilities.
metadata:
  category: engineering | product | design | finance | legal | marketing | sales | operations | healthcare | other
  maturity: draft | reviewed-by-practitioner | mature
  spec: 2 # authoring-spec version — always 2 for new roles
  onet_soc_code: "XX-XXXX.XX" # optional — matching O*NET-SOC code from ROADMAP.md
---

# <Role Name>

<!-- Regulated role (law/medicine/financial advice/safety/tax)? Add the disclaimer blockquote here — see lawyer-contracts for the pattern. -->

## Identity

2–4 sentences: seniority, org context, what they're accountable for, and the one tension that defines the job.

## First-principles core

3–5 internalized truths a generalist gets wrong. Bolded truth + the why. This is the only section where "why" lives.

1. **...** ...
2. **...** ...

## Mental models & heuristics

5–8 bullets, conditional form: "when X, default to Y unless Z". Named frameworks include when they're overused. Numeric rules of thumb welcome.

- ...

## Decision framework

4–7 executable process steps for a novel situation. No restating principles.

1. ...

## Tools & methods

Named tools, artifact types, rituals. Skip generic ones. Filled templates go in references/, not here.

## Communication style

How this role talks to peers vs leadership vs other functions — what they lead with, omit, and in what format.

## Common failure modes

Where agents/juniors playing this role go wrong — including overcorrections.

## Worked example

One scenario end-to-end with real, internally consistent numbers: the naive read, the expert reasoning that overturns it, and the actual deliverable output quoted (memo/redline/readout).

## Going deeper

- [references/playbook.md](references/playbook.md) — load when <...>
- [references/red-flags.md](references/red-flags.md) — load when <...>
- [references/vocabulary.md](references/vocabulary.md) — load when <...>

## Sources

Named books, standards, practitioners, postmortems. Specific numbers trace to a source or are labeled as stated heuristics.
```

## references/ skeletons

**red-flags.md** — 7–14 flags, each exactly:

```markdown
### <Signal, with numeric threshold where one exists>
- **Usually means:** <likeliest cause, then second>
- **First question:** <the one question a veteran asks>
- **Data to pull:** <specific report/query/document>
```

**vocabulary.md** — 8–17 terms generalists *misuse*:

```markdown
### <Term>
<1–2 sentence definition.>
**In use:** "<sentence a practitioner would actually say>"
**Common misuse:** <what generalists get wrong>
```

**playbook.md / artifacts.md** — filled examples, never descriptions of examples: real table structures with plausible numbers, step sequences with thresholds, fallback positions in preference order.
