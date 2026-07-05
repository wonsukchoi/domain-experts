# Artifacts & templates

Filled examples an agent can populate or execute against. Load this when producing an actual portfolio review, go/no-go assessment, or replication log — not for general reasoning (that's `SKILL.md`).

## Research portfolio scoring worksheet

```
Project           | Budget YTD | Expected info value (1-5) | Trend           | Go/no-go status
------------------|------------|----------------------------|-----------------|------------------
Coating process   | $1.2M      | 2 (below threshold)        | Diminishing     | Below interim gate — see decision memo
Catalyst screen   | $340K      | 4 (clear fork ahead)       | Accelerating    | Continue, increase allocation
Legacy assay      | $180K/yr   | 1 (result wouldn't change any decision) | Flat | Candidate for sunset — confirm no hidden dependency
New biomarker     | $95K       | 5 (binary go/no-go for a product line) | Early | Fund fully pending 90-day checkpoint

Scoring guide: expected info value = how much would a positive AND a negative result each change
a real downstream decision. A project scoring low on BOTH directions (result doesn't change
anything either way) is a candidate to defund regardless of scientific interest.
```

## Go/no-go criteria template (set BEFORE data collection)

```
Program: [name]                         Checkpoint: [e.g., 18 months / $X spent]

Interim success criterion (must be met to continue past this checkpoint):
  [Specific, measurable threshold, e.g., "≥25% improvement over baseline"]
  Rationale for this specific threshold: [why this number, tied to a downstream decision]

Final target: [e.g., 40% improvement]

Decision rule:
  IF interim result >= criterion: continue to next phase, budget $[X]
  IF interim result < criterion: STOP in current form; evaluate scoped pivot options: [list]
  Exception process: [who can override, and what evidence is required — set this now, not later]
```

## Replication/verification tracking log

```
Result: [claim, e.g., "novel compound shows 3x binding affinity vs. control"]
Original experiment: [date, conditions, N, statistical result]
Stakes if acted on without replication: [e.g., "would drive $2M follow-on program"]

Replication required before action: [Yes/No, and by whom - same lab, independent lab]
Replication 1: [date, result, matches original? Y/N]
Replication 2 (if stakes warrant): [date, result, matches? Y/N]

Status: [confirmed / not confirmed / mixed - do not act on original claim alone until this
section shows independent confirmation appropriate to the stakes]
```
