# Contributing

The full quality bar, per-section spec, and LLM drafting pipeline live in [`AUTHORING.md`](./AUTHORING.md). Read it before writing — PRs are reviewed against it.

Common questions (lint failures, push conflicts, release process) are answered in [`docs/FAQ.md`](./docs/FAQ.md).

## Adding a new role

1. Check [`ROADMAP.md`](./ROADMAP.md) for an uncovered occupation — it's the master checklist so effort doesn't collide or guess at gaps.
2. Copy the structure in [`TEMPLATE.md`](./TEMPLATE.md) to `roles/<role-slug>/` — `SKILL.md` plus the `references/` trio (deep-dive, `red-flags.md`, `vocabulary.md`).
3. Write to the [`AUTHORING.md`](./AUTHORING.md) spec. Substance bar: an actual practitioner reading it should nod, not shrug. Generic job-description text ("responsible for stakeholder alignment") gets rejected — first-principles reasoning ("stakeholders disagree because they're optimizing different metrics; find the metric conflict before the personality conflict") gets accepted.
4. Set `metadata.maturity: draft` if you're not a practitioner in this role, `reviewed-by-practitioner` if you are one or had one review it. If the role matches an O*NET occupation in `ROADMAP.md`, set `metadata.onet_soc_code` to its code.
5. Set `metadata.spec: 2` (required for new roles — CI rejects legacy format) and run `python3 scripts/lint_roles.py <role-slug>` until clean. CI runs the same lint on every PR.
6. Run `python3 scripts/generate_roadmap.py` to refresh `ROADMAP.md`'s checklist and the README role-count summary — don't hand-edit either.
7. Open a PR. Title format: `role: add <role name>` or `role: improve <role name> — <what changed>`.

### PR checklist

- [ ] Self-scored against the `AUTHORING.md` rubric; score in PR description (`rubric: N/18`, ship bar is ≥14 with no zeros)
- [ ] Worked example has real numbers that reconcile, and quotes the actual deliverable
- [ ] No idea stated twice (the dedup rule)
- [ ] No banned patterns (see `AUTHORING.md` lint list)
- [ ] `references/` links in "Going deeper" resolve
- [ ] Regulated role → disclaimer blockquote present
- [ ] `python3 scripts/lint_roles.py <slug>` passes
- [ ] `generate_roadmap.py` re-run


## Exact recipe for adding a role (follow verbatim)

Written so precisely that an AI assistant can execute it without judgment calls. Replace `<slug>` with the kebab-case role name everywhere (e.g. `actuary`).

**Step 0 — pick and verify the role is uncovered:**
```sh
npx domain-experts search <keyword>        # must return no existing match
grep -i "<role name>" ROADMAP.md           # note the O*NET-SOC code if listed
```

**Step 1 — create exactly these four files** (no more, no fewer, unless AUTHORING.md's naming rule says `artifacts.md` fits better than `playbook.md`):
```
roles/<slug>/SKILL.md
roles/<slug>/references/playbook.md      # OR artifacts.md — playbook if the role executes processes, artifacts if it produces documents/models
roles/<slug>/references/red-flags.md
roles/<slug>/references/vocabulary.md
```

**Step 2 — SKILL.md frontmatter, exactly this shape** (every field required except `onet_soc_code`):
```yaml
---
name: <slug>                  # MUST equal the directory name exactly
description: Use when a task needs the judgment of a <Role Title> — <task 1>, <task 2>, <task 3>, or <task 4>.
metadata:
  category: engineering | product | design | finance | legal | marketing | sales | operations | healthcare | other   # pick ONE
  maturity: draft             # unless a practitioner wrote/reviewed it
  spec: 2                     # always 2 for new roles — CI rejects anything else
  onet_soc_code: "XX-XXXX.XX" # only if it maps to a ROADMAP.md row; otherwise omit the line
---
```

**Step 3 — SKILL.md body**: all ten `## ` sections from TEMPLATE.md, in order: Identity, First-principles core, Mental models & heuristics, Decision framework, Tools & methods, Communication style, Common failure modes, Worked example, Going deeper, Sources. Hard rules the lint and reviewers enforce:
- Each idea appears exactly ONCE in the whole file (the dedup rule — never restate a principle as a heuristic and again as a framework step).
- Heuristics use the form "when X, default to Y unless Z".
- The Worked example contains real numbers that arithmetically reconcile and ends with the actual deliverable quoted (the memo/redline/readout itself, not a description of it).
- Going deeper links each references/ file with a relative link: `[references/red-flags.md](references/red-flags.md)`.
- Banned everywhere: "responsible for", "stakeholders" (unqualified), "leverage" (verb), "utilize", "it's important to", "best practices" (unqualified), "ensure alignment", "drive value", "various", "effectively", "holistic", adjectives where numbers belong.
- Regulated role (law/medicine/financial advice/tax/safety)? Add the disclaimer blockquote right after the H1 — copy the pattern from `roles/lawyer-contracts/SKILL.md`.

**Step 4 — references/ files, exact per-entry formats:**

`red-flags.md` — 7 to 14 entries, each exactly:
```markdown
### <Signal, with a numeric threshold where one exists>
- **Usually means:** <likeliest cause, then second most likely>
- **First question:** <the one question a veteran asks first>
- **Data to pull:** <specific report / query / document>
```

`vocabulary.md` — 8 to 17 terms a generalist misuses, each exactly:
```markdown
### <Term>
<1-2 sentence definition.>
**In use:** "<a sentence a practitioner would actually say>"
**Common misuse:** <what generalists get wrong>
```

`playbook.md` / `artifacts.md` — filled examples only, never descriptions of examples: real table structures with plausible numbers, step sequences with thresholds, fallback positions in preference order. Test: could an agent execute or populate it as-is?

**Step 5 — validate and register, in THIS order** (order matters — the roadmap script only counts git-tracked roles):
```sh
git add roles/<slug>
python3 scripts/lint_roles.py <slug>       # repeat until "0 errors"
python3 scripts/generate_roadmap.py        # regenerates ROADMAP.md, README counts, data/roles.json
git add -A
```

**Step 6 — self-score** against AUTHORING.md's 9-criterion rubric. Ship bar: **>=14/18 with no zeros**. Below bar: fix or don't submit — an unfilled slot is recoverable, a generic role poisons trust.

**Step 7 — PR** titled `role: add <role name>`, with the rubric score (`rubric: N/18`) and named sources in the description. The PR template walks the rest.

**Definition of done:** lint 0 errors · roadmap regenerated · rubric >=14 declared · sources named · (regulated only) disclaimer present.

## Exact recipe for upgrading a legacy role to spec 2 (follow verbatim)

Roles drafted before spec 2 lack the `references/` trio (including `vocabulary.md`) and the ten-section SKILL.md structure. The standing TODO is the **"Spec-2 upgrade queue"** section of `ROADMAP.md` (auto-generated — never hand-edit). Written so an AI assistant can execute it without judgment calls.

**Step 0 — pick and verify:**
```sh
grep -A2 'Spec-2 upgrade queue' ROADMAP.md    # pick the top entry, or any slug from the queue table
grep 'spec:' roles/<slug>/SKILL.md            # must be missing or 1 — if 2, it's already done, pick another
```

**Step 1 — read the existing `roles/<slug>/SKILL.md` in full.** It is source material, not the deliverable. Keep every correct heuristic, number, and framework; the upgrade is a restructure-and-deepen, not a from-scratch rewrite. Where the old content is generic ("responsible for…"), replace it per the AUTHORING.md pipeline (research → draft → adversarial critique → revise → score) — don't carry generic text forward.

**Step 2 — create the `references/` trio** using the exact per-entry formats from Step 4 of the add recipe above: `red-flags.md` (7-14 entries), `vocabulary.md` (8-17 misuse-aware terms), and `playbook.md` OR `artifacts.md`. Deep detail currently bloating SKILL.md moves here.

**Step 3 — restructure SKILL.md** to the ten `## ` sections in TEMPLATE.md order, per Steps 2-3 of the add recipe: update frontmatter to `spec: 2` (keep existing `onet_soc_code` and `category`), enforce the dedup rule, banned-word list, and heuristic form. Add the Going deeper section with relative links to each references/ file. Keep `maturity` as-is unless a practitioner reviewed the upgrade.

**Step 4 — validate and register, in THIS order:**
```sh
git add roles/<slug>
python3 scripts/lint_roles.py <slug>       # repeat until "0 errors"
python3 scripts/generate_roadmap.py        # role drops off the upgrade queue automatically
git add -A
```

**Step 5 — self-score** against the AUTHORING.md rubric; same ship bar as new roles (>=14/18, no zeros).

**Step 6 — commit** as `role: upgrade <role name> to spec 2`, then `git pull --rebase --autostash` before pushing (parallel sessions may be writing to `main`).

**Definition of done:** lint 0 errors · role gone from the upgrade queue after regeneration · rubric >=14 declared · no correct legacy content lost.

## Improving an existing role

Same spec. Highest-value improvements, in order: practitioner corrections to wrong/outdated heuristics, deepening a worked example with real numbers, adding missing red-flag thresholds, upgrading legacy roles to spec 2 (see the upgrade recipe above — the queue lives in `ROADMAP.md`).

## Practitioner review

If you actually work in a role and can confirm or correct its content, say so in your PR description (no verification required, just good faith) and bump `metadata.maturity` accordingly. If the spec fights your reality, the spec loses — say so and we'll fix the spec.

## LLM-assisted contributions

Welcome — but run the full pipeline in `AUTHORING.md` (research → draft → adversarial critique → revise → score), not a single generation pass. Single-pass LLM output is exactly the generic content this repo exists to replace, and it's easy to spot. State in the PR that the pipeline was used and include the rubric score.

## Style rules

- Frontmatter `description` must name concrete task types an agent harness can match — not "helps with X in general."
- Prefer bullet heuristics and named frameworks over paragraphs of prose.
- Cite sources where you can. "General knowledge" is fine for widely-known frameworks; specific claims (numbers, named methodologies) need a source.
- One role = one directory. If `SKILL.md` keeps growing past budget even with depth pushed to `references/`, the role is probably two roles — split it (e.g. `product-manager` vs `product-manager-technical`).

## Adding a whole new category

If your role doesn't fit an existing `metadata.category`, propose a new one in your PR description.
