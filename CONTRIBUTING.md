# Contributing

The full quality bar, per-section spec, and LLM drafting pipeline live in [`AUTHORING.md`](./AUTHORING.md). Read it before writing — PRs are reviewed against it.

## Adding a new role

1. Check [`ROADMAP.md`](./ROADMAP.md) for an uncovered occupation — it's the master checklist so effort doesn't collide or guess at gaps.
2. Copy the structure in [`TEMPLATE.md`](./TEMPLATE.md) to `roles/<role-slug>/` — `SKILL.md` plus the `references/` trio (deep-dive, `red-flags.md`, `vocabulary.md`).
3. Write to the [`AUTHORING.md`](./AUTHORING.md) spec. Substance bar: an actual practitioner reading it should nod, not shrug. Generic job-description text ("responsible for stakeholder alignment") gets rejected — first-principles reasoning ("stakeholders disagree because they're optimizing different metrics; find the metric conflict before the personality conflict") gets accepted.
4. Set `metadata.maturity: draft` if you're not a practitioner in this role, `reviewed-by-practitioner` if you are one or had one review it. If the role matches an O*NET occupation in `ROADMAP.md`, set `metadata.onet_soc_code` to its code.
5. Set `metadata.spec: 2` (required for new roles — CI rejects legacy format) and run `python3 scripts/lint_roles.py <role-slug>` until clean. CI runs the same lint on every PR.
6. Run `python3 scripts/generate_roadmap.py` to refresh `ROADMAP.md`'s checklist and the README role-count summary — don't hand-edit either.
6. Open a PR. Title format: `role: add <role name>` or `role: improve <role name> — <what changed>`.

### PR checklist

- [ ] Self-scored against the `AUTHORING.md` rubric; score in PR description (`rubric: N/18`, ship bar is ≥14 with no zeros)
- [ ] Worked example has real numbers that reconcile, and quotes the actual deliverable
- [ ] No idea stated twice (the dedup rule)
- [ ] No banned patterns (see `AUTHORING.md` lint list)
- [ ] `references/` links in "Going deeper" resolve
- [ ] Regulated role → disclaimer blockquote present
- [ ] `generate_roadmap.py` re-run

## Improving an existing role

Same spec. Highest-value improvements, in order: practitioner corrections to wrong/outdated heuristics, deepening a worked example with real numbers, adding missing red-flag thresholds, upgrading pre-`references/` roles to the current layout.

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
