# Contributing

## Adding a new role

1. Check [`ROADMAP.md`](./ROADMAP.md) for an uncovered occupation — it's the master checklist so effort doesn't collide or guess at gaps.
2. Copy [`TEMPLATE.md`](./TEMPLATE.md) to `roles/<role-slug>/SKILL.md`.
3. Fill in every section. Substance bar: an actual practitioner reading it should nod, not shrug. Generic job-description text ("responsible for stakeholder alignment") gets rejected — first-principles reasoning ("stakeholders disagree because they're optimizing different metrics; find the metric conflict before the personality conflict") gets accepted.
4. Set `metadata.maturity: draft` if you're not a practitioner in this role, `reviewed-by-practitioner` if you are one or had one review it. If the role matches an O*NET occupation in `ROADMAP.md`, set `metadata.onet_soc_code` to its code.
5. Run `python3 scripts/generate_roadmap.py` to refresh `ROADMAP.md`'s checklist and the README role-count summary — don't hand-edit either.
6. Open a PR. Title format: `role: add <role name>` or `role: improve <role name> — <what changed>`.

## Improving an existing role

Same file, same schema. PRs that add missing first-principles depth, correct outdated/wrong heuristics, or add a practitioner-reviewed worked example are the highest-value contributions.

## Practitioner review

If you actually work in a role and can confirm or correct its content, say so in your PR description (no verification required, just good faith) and bump `metadata.maturity` accordingly.

## Style rules

- Frontmatter `description` must be specific enough for an agent harness to match a task to this role — not "helps with X in general."
- Prefer bullet heuristics and named frameworks over paragraphs of prose.
- Cite sources where you can. "General knowledge" is fine for widely-known frameworks; specific claims (numbers, named methodologies) need a source.
- Keep a role to one `SKILL.md`. If it's getting too long, the role is probably two roles — split it (e.g. `product-manager` vs `product-manager-technical`).

## Adding a whole new category

If your role doesn't fit an existing `metadata.category`, propose a new one in your PR description.
