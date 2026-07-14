# Playbook

## Tooling wear inspection worksheet

Fill before starting any production run.

| Field | Value |
|---|---|
| Last ID | Size 9, Style ATH-2291 |
| Spec max wear tolerance | 0.020" |
| Measured deviation (toe-box profile) | 0.040" |
| Within tolerance? | N — replace/refinish before starting |
| Action | Last replaced, new last first-article checked |
| First-article result | Within spec — cleared for production |

**Rule:** never start a production run on tooling with unverified or known-excessive wear — a worn last produces a systematic defect across every unit, not an isolated issue.

## In-process sampling containment table

| Sample point | Bond pull strength (lbf) | Spec (min 25 lbf) | Pass/Fail |
|---|---|---|---|
| Pair 50 | 27 | ✓ | Pass |
| Pair 100 | 26 | ✓ | Pass |
| Pair 150 | 27 | ✓ | Pass |
| Pair 200 | 26 | ✓ | Pass (last good sample) |
| Pair 250 | 18 | ✗ | **FAIL** |

**Containment scope:** pairs 201-250 (50 pairs, produced since last good sample) — NOT the full batch.

**Rule:** containment scope is defined by the interval between the last good sample and the failing sample, not the entire batch — narrower, targeted containment based on actual sampling data is both more accurate and more efficient than a blanket full-batch hold.

## Material-specific parameter reference guide (illustrative — always use the actual material/style specification)

| Material | Lasting tension consideration | Molding/bonding temperature consideration |
|---|---|---|
| Full-grain leather | Standard tension range, moderate stretch | Standard cure temperature per compound |
| Synthetic/PU upper | Often requires different tension (less natural stretch) | May require adjusted temperature for proper adhesion |
| Mesh/textile upper | Lower tension typically needed (less structural stretch resistance) | Standard, but verify compatibility with mesh backing |

**Rule:** always confirm the specific material's parameter requirements against the process specification — never assume a previous material's settings transfer directly to a new material.
