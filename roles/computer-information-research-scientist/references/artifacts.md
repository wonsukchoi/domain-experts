# Artifacts Playbook

Filled templates for the three deliverables this role actually produces and defends: a funding proposal built to a funder's mechanical caps, a reproducibility checklist and artifact-badge submission, and an ablation table that survives a reviewer's own re-derivation.

## NSF CISE proposal structure and caps

Use these as pass/fail gates — a program officer's administrative screen checks page count and required labeled sections before anyone reads for substance. Numbers below are current PAPPG (Proposal & Award Policies & Procedures Guide) caps for a standard CISE research proposal; verify against the live solicitation before submitting, since core/CAREER/collaborative mechanisms shift specifics.

| Section | Cap | Notes |
|---|---|---|
| Project Summary | 1 page | Must contain **two separately labeled** statements: Overview, Intellectual Merit, Broader Impacts — blended prose fails the check. |
| Project Description | 15 pages | Includes figures, tables, references-in-text; a Results from Prior NSF Support subsection is required if any team member had NSF funding in the last 5 years. |
| References Cited | No cap | Full citations for every claim; missing DOI/URL is a minor flag, not a rejection. |
| Biographical Sketches | 3 pages per senior person | NSF-approved format (SciENcv) only as of 2023 — a CV in the old 2-page format is an auto-return. |
| Budget Justification | 3 pages per budget-year page-equivalent, ~5 pages typical for a 3-year budget | Must itemize: personnel (months × rate), equipment >$5k individually, travel (conference vs. fieldwork), participant support (non-fungible line), indirect costs at the negotiated rate. |
| Current & Pending / Other Support | No page cap, exact NSF-approved format | Every source of support for every senior person, including in-review proposals elsewhere — omission found later can trigger a research-integrity inquiry, not just a returned proposal. |
| Data Management & Sharing Plan | 2 pages | Must specify: what data/code will be shared, repository (e.g., Zenodo, an institutional repo), license, and embargo period if any. |
| Postdoctoral Mentoring Plan | 1 page | Required only if the budget includes postdoc salary. |

**Administrative-return checklist (run before submission, not after a decline):**

- [ ] Project Summary has Overview / Intellectual Merit / Broader Impacts as three separately labeled paragraphs.
- [ ] Project Description ≤ 15 pages including all figures and in-text citations.
- [ ] Every biosketch uses the current SciENcv-generated format.
- [ ] Current & Pending list includes proposals currently under review at other agencies, not just funded awards.
- [ ] Budget Justification itemizes every equipment line >$5,000 separately.
- [ ] Data Management & Sharing Plan names a specific repository, not "data will be made available."
- [ ] Font ≥ 10pt, margins ≥ 1 inch, single-spaced — mechanical formatting checks that trigger auto-return.

## Reproducibility checklist (submission-time, not camera-ready afterthought)

Fill this in at the point of writing the Methods section, not after a reviewer asks. Each row needs a concrete answer, not a checkbox.

| Item | Answer required | Example |
|---|---|---|
| Code released | Repository URL + commit hash | `github.com/lab/sparse-attn`, commit `a91f3c2` |
| Environment pinned | Docker image digest or lockfile | `Dockerfile` pinned to `pytorch/pytorch:2.3.0-cuda12.1`, `requirements.txt` with exact versions |
| Data availability | Public dataset name+version, or synthetic/proprietary with access path stated | ImageNet-1k (2012 val split), or "proprietary; contact for access under NDA" |
| Compute budget disclosed | GPU-type × count × wall-clock hours | 8× A100-80GB, 62 hours per run, 4 runs |
| Hyperparameters | Full table, including ones held fixed | Learning rate 3e-4, warmup 10k steps, batch 512, seed {0,1,2} |
| Number of seeds / runs per result | Integer, plus variance reported | 3 seeds; mean ± std reported in Table 2 |
| Checkpoints released | Which ones, at what training step | Final + best-val checkpoint for all 4 ablation rows |
| Evaluation script | Exact script name/path in repo | `eval/topk_accuracy.py --split val` |

**ACM Artifact Review and Badging — target tier decided at project-planning time, not after the paper is written:**

| Badge | Requirement | Typical gate that blocks it |
|---|---|---|
| Artifacts Available | Artifact placed in an archival repo (not a personal webpage) with a permanent identifier (DOI) | Author defaults to "code on my GitHub," no DOI — fails |
| Artifacts Evaluated – Functional | Documented, consistent, complete, exercisable by a reviewer | Missing a README with exact run command, or a hardcoded absolute path — fails |
| Artifacts Evaluated – Reusable | Functional bar + carefully documented enough to be repurposed | No API/CLI abstraction, everything inlined in one script — fails |
| Results Reproduced | Independent team, same experimental setup, obtains consistent results | Author's own re-run doesn't count — must be a different team |
| Results Replicated | Independent team, different experimental setup, obtains consistent results | Rare; typically a follow-up paper's contribution, not the original submission's |

Default target for a standard empirical paper: **Artifacts Evaluated – Functional.** Anything less and a reproducibility claim in the abstract is unsupported; anything more (Reusable) is a real scope increase — budget an extra week for documentation and interface cleanup, don't promise it under submission-deadline pressure.

## Ablation table template

One factor changed per row, same seed and eval set as the row above it, deltas must arithmetically reconcile to the headline claim.

| Configuration | Metric | Δ vs. previous row |
|---|---|---|
| Baseline | *(baseline value)* | — |
| + *(confound 1, e.g. LR schedule change)* | *(value)* | *(delta)* |
| + *(confound 2, e.g. batch size change)* | *(value)* | *(delta)* |
| + *(proposed contribution)* | *(value = headline number)* | *(delta)* |

Reconciliation check: sum of all row deltas must equal (headline value − baseline value) exactly, to the reported precision. If it doesn't, a row is missing or an interaction effect exists — state the interaction explicitly rather than silently absorbing the discrepancy into the last row.

**Worked instance** (same numbers as the SKILL.md example, for direct reuse):

| Configuration | Top-1 accuracy | Δ vs. previous row |
|---|---|---|
| Baseline | 80.1% | — |
| + LR schedule (cosine, warmup 5k→10k) | 82.7% | +2.6pp |
| + batch size (256→512) | 83.2% | +0.5pp |
| + proposed sparse-attention module | 84.3% | +1.1pp |

2.6 + 0.5 + 1.1 = 4.2pp = 84.3% − 80.1%. Reconciles. Report the module's isolated contribution (+1.1pp, ~26% of the total gain) in the abstract, not the unattributed 4.2pp.

## Fallback positions when the ideal isn't available

In preference order, when the full checklist can't be met:

1. **Full artifact release + Reproducibility-Functional badge** — always attempt first; the marginal cost is a few days of cleanup, the credibility cost of skipping it is the paper's central claim.
2. **Partial release (code, no data)** when data is proprietary or subject to a data-use agreement — state exactly what's withheld and why, and release a synthetic-data harness that exercises the same code path if feasible.
3. **Release on request** only when data-use or export-control restrictions make public hosting genuinely infeasible — must name a concrete request process (an email address, an IRB-approved data-sharing agreement template) rather than an unspecified "contact the authors," and must be disclosed as the weaker tier in the paper text itself, not left implicit.
4. **No release** — acceptable only for work explicitly scoped as position/theory papers with no empirical artifact to release; if the paper reports an experiment, this tier should trigger a second look at whether the paper should claim reproducibility at all.
