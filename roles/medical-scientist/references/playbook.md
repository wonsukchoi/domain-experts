# Medical Scientist — Playbook

## Study-design checklist (filled example, in vivo efficacy study)

| Item | Specification | Status |
|---|---|---|
| Hypothesis | Compound X reduces tumor volume by >=40% vs. vehicle at 21 days in [model] | Set |
| Primary endpoint | Tumor volume (mm³) at day 21, tumor growth inhibition (TGI) % | Set |
| Model | [Xenograft/syngeneic/PDX], cell line, implantation route | Confirm passage number logged |
| Group size (power) | n=10/arm (see power table below) | Confirmed vs. historical SD |
| Randomization | Block randomization by baseline tumor volume before first dose | Protocol step, not post-hoc |
| Blinding | Caliper measurement by scorer blinded to group assignment | Confirm blinding maintained through endpoint |
| Positive control | [Known active comparator at established dose] | Included every run |
| Vehicle/negative control | Matched vehicle, same dosing route/schedule | Included every run |
| Exposure check | Satellite PK cohort or terminal plasma sampling | Scheduled, not assumed from prior study |
| GLP status | Exploratory (non-GLP) — this study does not feed a regulatory submission | Stated before study start |

## Sample-size / power table (by model type, stated heuristics — confirm against actual historical variance)

| Model type | Typical effect size sought | Historical CV | Suggested n/arm | Note |
|---|---|---|---|---|
| Cell viability assay (in vitro) | 3 technical reps/plate | 5-10% | 3 biological reps minimum | Technical reps qualify the plate, not the biology |
| Mouse xenograft (tumor volume) | >=40% TGI | 25-35% | 8-10/arm | Below 8/arm, only large effects (>50% TGI) are reliably detectable |
| Mouse survival study | Hazard ratio 0.5 | — (event-based) | 15-20/arm | Powered on expected event rate, not group size alone |
| GLP tox study (rodent) | Per regulatory guidance (ICH M3) | — | Per guidance, typically 10/sex/dose group | Not a discovery-stage decision — set by regulatory requirement |

## Assay-qualification worksheet (filled example, HTS screen)

| Metric | Formula | This run | Threshold | Pass? |
|---|---|---|---|---|
| Z'-factor | 1 − (3×(SD_pos + SD_neg)) / \|Mean_pos − Mean_neg\| | 0.71 | >=0.5 | Yes |
| Signal window | Mean_pos − Mean_neg | 68 units | Assay-specific | Yes (established at 40+) |
| Hit rate | Hits / total compounds screened | 1.8% | 0.1-3% typical | Yes (within expected range; >5% suggests plate artifact) |
| Edge effect | Compare edge-well vs. interior-well controls | <5% deviation | <10% | Yes |

## Go/no-go memo skeleton

```
Program: [name/compound ID]
Decision: [Advance to X / Hold / Terminate]

Basis:
- [Primary endpoint result, with replicate count and confidence interval — not a single-run point estimate]
- [Assay/model qualification status: Z'-factor, control performance]
- [Dose-response shape confirmation, if applicable]

Not yet shown:
- [Explicitly name what this study did NOT establish — e.g., in vivo relevance, mechanism confirmation]

Risk flagged:
- [Any orthogonal confirmation still pending before the next resource commitment]
```
