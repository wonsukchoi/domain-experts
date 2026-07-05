# Parity tests — skill vs real practitioners

The strongest verification this repo can get without recruiting experts: real questions that real practitioners already answered publicly, answered fresh by the skill-loaded model, blind-judged head-to-head against the practitioner's accepted answer.

- **Win** — blind judge picks the skill's answer over the practitioner's.
- **Parity rate** — (wins + ties) / total. ≥50% wins means the skill writes answers a blind senior grader prefers to real practitioners' answers.

The judge never knows which answer is the human's, grades substance over length, and is asked to flag confident factual errors in both.

## Run

```sh
python3 evals/parity/run_parity.py                         # all roles with question files
python3 evals/parity/run_parity.py lawyer-contracts --model claude-haiku-4-5-20251001 --judge-model claude-sonnet-5
```

Results land in `evals/parity/results/` (gitignored, point-in-time).

## Harvesting more questions

```sh
python3 evals/parity/harvest_stackexchange.py <role-slug> <se-site> <tag> [n]
python3 evals/parity/harvest_stackexchange.py lawyer-contracts law contract-law 3
```

Quality bar (enforced by the script): question score ≥10, accepted answer with score ≥10, substantial self-contained bodies. Merge is additive; re-runs skip already-harvested IDs.

Good sites per role: `law` (lawyer-contracts), `stats` (data-scientist), `pm` (product-manager), `workplace` (hr-people-manager), `money` (financial roles — screen carefully, mostly consumer finance). Other sources (practitioner forums, published analyses) can be added by hand in the same JSON shape.

## Licensing

Stack Exchange content is **CC BY-SA 4.0**. Harvested files keep the source URL, author display name, and license tag — that attribution must stay with the data. Question files are therefore CC BY-SA, not MIT.

## Honest caveats

- SE answerers are high-rep, not credential-verified; accepted ≠ infallible. Wins mean "preferred by a blind senior grader," not "objectively correct."
- A handful of questions per role is a smoke signal, not a study. Grow the question sets before quoting numbers loudly.
- The skill arm loads SKILL.md only — if a role keeps its depth in references/, parity understates it.
