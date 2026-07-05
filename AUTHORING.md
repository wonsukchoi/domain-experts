# Authoring Spec — how a role gets written

This is the canonical spec for producing a role, whether the author is a human contributor or an LLM pipeline. `TEMPLATE.md` is the skeleton; this file is the quality bar and the process. Every new role and every improvement PR is judged against this document.

Gold-standard examples (read one before writing anything): [`financial-manager`](./roles/financial-manager/), [`lawyer-contracts`](./roles/lawyer-contracts/), [`product-manager`](./roles/product-manager/), [`data-scientist`](./roles/data-scientist/), [`marketing-strategist`](./roles/marketing-strategist/).

## What "matches or beyond human expert" means

Three operational tests. A role ships only if it passes all three:

1. **Practitioner nod test** — a real practitioner reading it nods ("yes, that's the actual job") rather than shrugs ("this is a job posting"). Every claim should be something a 10+ year practitioner would say, including the uncomfortable ones.
2. **Counterfactual test** — an agent loaded with this skill makes *different, better decisions* than the same agent without it. If a section wouldn't change any decision, it's filler.
3. **Non-derivability test** — the content could not be regenerated from the role title alone. "Purchasing managers evaluate suppliers" is derivable; "single-sourcing is a risk-allocation decision made by default when nobody prices the disruption scenario" is not. Numbers, thresholds, named clause positions, and worked arithmetic are the strongest non-derivable content.

Where a role can go *beyond* a single human expert: breadth of synthesis. One practitioner knows their industry and their decade; the role file can merge the consensus of many named sources across industries. That's the edge — use it, and cite it.

## File layout

```
roles/<role-slug>/
  SKILL.md                 # always loaded — the reasoning core, token-budgeted
  references/
    <deep-dive>.md         # playbook.md OR artifacts.md (see naming rule)
    red-flags.md           # smell tests with thresholds
    vocabulary.md          # terms of art, misuse-aware
```

**Progressive disclosure is the design principle.** `SKILL.md` is loaded into the agent's context whenever the role activates — every token costs. `references/` files load only when the task needs depth. Reasoning and judgment go in `SKILL.md`; templates, tables, checklists, and glossaries go in `references/`.

**Deep-dive naming rule:** `artifacts.md` when the role's output is documents/models (CFO forecasts, PM PRDs, legal clauses → `clause-playbook.md` is a valid specialization). `playbook.md` when the role's output is executed processes (marketing campaigns, data analyses → `analysis-playbook.md`). One or two deep-dive files max; a third needs justification in the PR.

**Size budgets** (targets, not hard caps — but overshooting means you're probably repeating yourself):

| File | Lines |
|---|---|
| `SKILL.md` | 80–120 |
| deep-dive file | 60–190 |
| `red-flags.md` | 45–90 |
| `vocabulary.md` | 50–80 |

## Frontmatter schema (exact)

```yaml
---
name: <role-slug>            # must equal the directory name
description: Use when a task needs the judgment of a <Role> — <3-5 concrete task types, comma-separated>.
metadata:
  category: engineering | product | design | finance | legal | marketing | sales | operations | healthcare | other
  maturity: draft | reviewed-by-practitioner | mature
  spec: 2                       # authoring-spec version — 2 is current; absent means legacy (pre-references format)
  onet_soc_code: "XX-XXXX.XX"   # if it maps to ROADMAP.md; omit otherwise
---
```

**Spec versioning:** `spec: 2` marks a role written to this document (references/ trio, worked example with numbers, dedup rule). Roles without the field are legacy format, grandfathered but slated for upgrade. New roles must be `spec: 2` — CI rejects legacy-format additions. `python3 scripts/lint_roles.py` runs the mechanical checks locally; CI runs the same script on every PR.

The `description` is what agent harnesses match against. It must name concrete task types ("negotiating a supplier contract, evaluating single- vs multi-source"), never capabilities in general ("helps with procurement").

## SKILL.md section spec

Every section from `TEMPLATE.md`, in order. Per-section bar:

### Identity (2–4 sentences)
Seniority, org context, what they're accountable for — plus the one tension that defines the job (e.g. "accountable for cost, but the harder job is the cost/continuity tradeoff"). No adjectives about being "experienced" or "skilled."

### First-principles core (3–5 numbered items)
The internalized truths a generalist gets wrong. Each item: bolded one-sentence truth + 1–2 sentences of *why*. These are the only place "why" lives — later sections apply these, they don't restate them.

- ❌ "Total cost matters, not just unit price." (derivable, no why)
- ✅ "**The lowest price and the lowest total cost are frequently different numbers.** Quality costs, delivery reliability, and switching costs are invisible in a quote and dominate in a disruption — the cheap supplier is often the expensive one, priced honestly."

### Mental models & heuristics (5–8 bullets)
Conditional form only: **"when X, default to Y unless Z"**, named frameworks with *when they're overused* ("RICE — useful tiebreaker, garbage-in when reach estimates are invented"), and numeric rules of thumb. No abstract advice.

### Decision framework (4–7 steps)
Pure process — the actual order of operations when facing a novel situation in the role. Steps reference the principles; they never re-explain them. Test: could an agent execute each step as written?

### Tools & methods
Named tools, artifact types, rituals of the trade. Skip generic ones (email, spreadsheets-in-general). Point to `references/` for the filled templates.

### Communication style
How the role talks to peers vs leadership vs other functions — what they lead with, what they omit, what format (memo, one-pager, redline).

### Common failure modes
Where agents and juniors pretending to be this role go wrong. Include the *overcorrections* (e.g. "having learned TCO, treats every commodity buy like a strategic sourcing event").

### Worked example (required, the hardest section)
One scenario, end-to-end, with **real numbers that are internally consistent** (they will be arithmetic-checked in review), a naive read that a generalist would produce, the expert reasoning that overturns or refines it, and **the actual deliverable output** (the memo, the redline, the readout — quoted, not described). This section is the single strongest signal of role quality. If you can't produce a numbered worked example, you don't understand the role well enough to write it.

### Going deeper
Relative links to each `references/` file with a one-line description of when to load each.

### Sources
Named books, standards, named practitioners/handles, postmortems. "General knowledge" allowed only for universally known frameworks. Every specific number or threshold traces to a source or is labeled as a stated heuristic.

## The dedup rule

**Each idea appears exactly once, in the section where it does the most work.** The single most common LLM failure is restating one principle as a principle, again as a heuristic, and again as a framework step. Test per sentence: delete it — is the idea still present elsewhere in the file? Then keep the deletion.

## references/ file specs

### red-flags.md (7–14 flags)
Per flag, four fields, exactly this shape:

```markdown
### <Signal, with a numeric threshold where one exists>
- **Usually means:** <most likely cause, then second most likely>
- **First question:** <the one question a veteran asks>
- **Data to pull:** <specific report/query/document>
```

- ❌ "Watch out for declining margins."
- ✅ "### Gross margin down >200bps over two quarters with no pricing change — Usually means: infrastructure cost creep or support headcount misclassified into COGS…"

### vocabulary.md (8–17 terms)
Per term: definition (1–2 sentences) + **a sentence a practitioner would actually say using it** + the common misuse. Pick terms generalists *misuse*, not terms they can look up — the value is the misuse column.

### Deep-dive file (playbook/artifacts)
Filled examples, never descriptions of examples. A template an agent can execute or populate: real table structures with plausible example numbers, step sequences with thresholds, fallback positions in preference order. If a section says "include things like X and Y," rewrite it to *be* X and Y.

## Regulated roles

Roles whose human counterpart is licensed (law, medicine, financial advice, structural/safety engineering, tax) must carry a blockquote disclaimer at the top of the SKILL.md body: reasoning aid, not professional advice; jurisdiction/context matters; licensed professional signs off. See `lawyer-contracts/SKILL.md` for the pattern.

## Banned patterns (lint list)

Phrases — presence of any is a review flag:
`responsible for` · `stakeholders` (unqualified) · `leverage` (as verb) · `utilize` · `it's important to` · `best practices` (unqualified) · `ensure alignment` · `drive value` · `various` · `effectively` · `holistic` · `robust` (about anything but statistics) · `in today's fast-paced`

Structural bans:
- An adjective where a number belongs ("significant increase" → give the % or delete)
- A bullet that restates another bullet in different words
- A "framework" that is a list of considerations rather than a decision procedure
- A worked example without arithmetic, or whose numbers don't reconcile

## LLM drafting pipeline

For maintainers generating roles with LLMs (any tier). The passes are separate LLM calls — **the drafter never grades its own work in the same context.**

**Pass 0 — Research.** Collect 5+ named sources: practitioner-written books, standards docs, postmortems, well-regarded forum/community threads, O*NET task lists (as a coverage skeleton only — O*NET text is exactly the generic content this repo rejects). Output: source notes with harvested *numbers, thresholds, named positions, and war stories*. If research yields no concrete numbers, stop — the draft will be generic.

**Pass 1 — Draft.** One file per call. Context: this spec + `TEMPLATE.md` + one gold-standard role of the same shape (document-producing vs process-executing) + the Pass 0 source notes. Instruction: write to spec; every claim traceable to source notes or flagged `[heuristic — needs practitioner check]`.

**Pass 2 — Critique.** Fresh call, adversarial. Instructions: (a) quote every sentence that could appear in a job description or be derived from the role title alone; (b) find every idea stated more than once; (c) recompute all worked-example arithmetic; (d) check every red flag has all four fields; (e) apply the banned-pattern list. Output: numbered defect list.

**Pass 3 — Revise.** Drafter context + defect list. Fix everything or explicitly contest a defect with a reason.

**Pass 4 — Score.** Fresh call, rubric below. Ship at **≥14/18 with no zero on any criterion**. Below threshold: loop to Pass 2 (max 2 loops), else *skip the role* — an unfilled roadmap slot is recoverable, a shipped-generic role poisons trust in the whole library.

### Scoring rubric (0 = fails, 1 = partial, 2 = meets bar)

| # | Criterion |
|---|---|
| 1 | Specificity — numbers/thresholds/named positions present throughout |
| 2 | Dedup — no idea appears twice |
| 3 | Worked example — real, reconciling numbers + quoted deliverable |
| 4 | Heuristics — conditional "when X, default Y unless Z" form |
| 5 | Red flags — thresholds + all four fields each |
| 6 | Vocabulary — misuse column carries real weight |
| 7 | Sources — named, and specific claims trace to them |
| 8 | Non-derivability — couldn't be regenerated from the title alone |
| 9 | Harness match — description names concrete task types |

Record the score in the PR description (`rubric: 16/18`).

## Human contributors

Same spec, lighter process: skip the pass structure, self-check against the rubric, open the PR. Practitioners get the strongest presumption — if you do the job and the spec fights your reality, the spec loses; say so in the PR and we'll fix the spec.
