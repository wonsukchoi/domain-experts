# Playbook

## Scale-error projection worksheet

Fill to check whether a model-scale discrepancy is actually significant.

| Field | Value |
|---|---|
| Model scale | 1:50 |
| Model-scale error observed | 0.10" (example — cumulative chained-measurement drift) |
| Full-scale equivalent (error × scale ratio) | 0.10" × 50 = 5.0" |
| Is this significant at full scale? | Yes — 5" of window misalignment is visually/functionally significant |
| Bounded (non-chained) measurement error | ±0.005" per point |
| Full-scale equivalent of bounded error | 0.005" × 50 = 0.25" — acceptable |

**Rule:** always project a model-scale error to its full-scale equivalent before judging whether it's acceptable — a "tiny" model-scale number can represent a large, real-world discrepancy.

## Material representation testing guide

1. Identify the full-scale material and finish being represented.
2. Select 2-3 candidate model-scale materials that might visually represent it.
3. Create small sample swatches of each candidate.
4. View samples at the model's actual intended scale and typical viewing distance (not close-up under magnification).
5. Select the material that reads most convincingly as the intended full-scale material at that viewing distance — this may not be the "obvious" literal match.
6. Document the material choice and reasoning for future reference on similar projects.

## Model purpose-to-precision-priority table

| Model purpose | Precision priority | Finish priority |
|---|---|---|
| Design communication / concept review | Visual proportion, overall form | Material representation, presentation quality |
| Functional fit-check / engineering verification | Dimensional accuracy at critical interfaces | Low — finish only where needed for handling/protection |
| Client presentation / marketing | Visual proportion and material representation | High — presentation-grade finish |
| Long-term display / trade show | Visual proportion, material representation, AND construction durability | High, plus robust construction for repeated handling |

**Rule:** clarify which category (or combination) applies before starting, and allocate time/effort accordingly — building every model to the highest standard in every category wastes effort where it doesn't matter for that specific model's purpose.
