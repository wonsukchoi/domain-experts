# Playbook

## Scallop-height / stepover calculation (filled example)

Ball-nose tool, radius R = 0.250", target max scallop height h = 0.0002".

Formula: h = R − √(R² − (s/2)²), rearranged to solve for max stepover: s = 2√(R² − (R−h)²)

| Step | Value |
|---|---|
| R (tool radius) | 0.250" |
| h (target max scallop height) | 0.0002" |
| R − h | 0.2498" |
| (R−h)² | 0.06240004 |
| R² | 0.0625 |
| R² − (R−h)² | 0.00009996 |
| √(R² − (R−h)²) | 0.009998 |
| s (max stepover) | 2 × 0.009998 ≈ 0.020" |

**Verification at s = 0.020":** (s/2)² = 0.0001; R² − (s/2)² = 0.0624; √0.0624 = 0.249800; h = R − 0.249800 = 0.000200 — exactly matches the 0.0002" target.

**Comparison — naive s = 0.010":** (s/2)² = 0.000025; R² − (s/2)² = 0.062475; √0.062475 = 0.249950; h = 0.250 − 0.249950 = 0.00005" — four times tighter than required, at roughly double the pass count for the same surface width.

| Stepover | Resulting scallop height | Passes across 4" surface | Meets 0.0002" spec? |
|---|---|---|---|
| 0.010" (naive default) | 0.00005" | ~400 | Yes, but over-finished |
| 0.020" (calculated) | 0.00020" | ~200 | Yes, exactly on spec |

## Multi-setup datum verification (filled example)

Part requiring two setups: Setup A machines the top face and bore; Setup B (after flipping the part) machines the bottom face features.

| Setup | Datum used | Physical reference |
|---|---|---|
| A | Datum A (bottom face), Datum B (locating pin in bore) | Vise jaw + locating pin fixture |
| B (naive) | Top face (opposite of datum A) as the new zero reference | Different vise jaw contact — no shared reference to setup A |
| B (corrected) | Same locating pin (datum B) referenced through a through-hole in the fixture plate | Same physical pin location as setup A |

**Naive approach risk:** Setup B zeroing off the top face (rather than referencing back to datum B) means any parallelism or flatness error between the top and bottom faces transfers directly into a positional error between features cut in setup A and setup B — a stack-up invisible until final inspection.

**Corrected approach:** Both setups physically locate off the same pin (datum B), so features from both setups share one consistent reference regardless of any face-to-face parallelism error in the raw stock.

## Post-processor / dry-run validation checklist (filled example)

New 5-axis part, first time running on Machine 7's post-processor.

1. Confirm the post-processor version matches Machine 7's current control software version (check control's displayed version against the post-processor's documented compatible version).
2. Simulate the full program in CAM software with the actual fixture model imported, checking clearance at every tool orientation, not just the nominal starting position.
3. Load the program on Machine 7 and air-cut it fully, tool retracted to a safe clearance height, watching rotary axis direction and rapid move sequencing against the simulation.
4. Confirm feed-override dial is at 100% and spindle is not engaged during the air cut, so the observed motion matches the programmed feed exactly.
5. Only after a clean air cut, proceed to a single-part production cut with in-process measurement before releasing the full batch.
