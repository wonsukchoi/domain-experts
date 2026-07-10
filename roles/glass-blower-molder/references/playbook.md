# Playbook

## COE compatibility check (filled example)

Tube joint, piece A (labeled borosilicate) and piece B (labeling uncertain).

| Piece | Tested COE (×10⁻⁷/°C) | Glass family consistent with reading |
|---|---|---|
| A | 33 | Borosilicate |
| B | 51 | Soda-lime/soft glass |

| Calculation | Value |
|---|---|
| COE difference | 51 − 33 = 18 |
| Difference as % of piece A's COE | 18 / 33 = 54.5% |
| Compatibility assessment | **Incompatible — reject pairing, source matched stock** |

**Compatibility rule of thumb applied:** A COE difference under roughly 5–10% between two glasses is commonly workable for a stable joint depending on piece geometry and annealing care; a 54.5% difference is far outside any workable range regardless of annealing schedule.

## Annealing schedule worksheet, thickest-cross-section basis (filled example)

Blown vessel with wall thickness varying from 2mm (body) to 8mm (base), where the base is the thickest section.

| Basis for schedule | Approach | Result |
|---|---|---|
| Naive: average wall thickness | (2mm + 8mm) / 2 = 5mm | Schedule undersized for the 8mm base — soak time too short for that section to equalize |
| Naive: thinnest wall thickness | 2mm | Schedule severely undersized — base retains significant residual stress |
| Correct: thickest wall thickness | 8mm | Soak time and cooling rate calculated for the 8mm base, ensuring the thinner 2mm body (which equalizes faster) is also fully relieved by the time the thickest section is |

**Rule applied:** Annealing schedule duration and cooling rate scale with the square of the thickest cross-section's dimension for many practical estimation methods — meaning the 8mm base needs meaningfully more soak time than a schedule calculated off the 5mm average would provide, even though the average looks like a reasonable middle-ground figure.

## Working temperature reference by glass type (filled example)

| Glass type | Approximate working range | Approximate annealing point | Notes |
|---|---|---|---|
| Soda-lime (soft glass) | ~1350–1600°F | ~900°F | Lower COE tolerance for thermal shock than borosilicate |
| Borosilicate | ~1800–2200°F | ~1050°F | Higher working temperature, better thermal shock resistance |

**Rule applied:** Switching torch/kiln parameters from a soda-lime setup directly to borosilicate stock without adjustment risks failing to properly soften the borosilicate (parameters tuned too low) — verify glass type and reset parameters for the specific type in use every time stock changes.
