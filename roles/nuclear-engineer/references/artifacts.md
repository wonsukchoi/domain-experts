# Nuclear Engineer — filled artifacts

## Shielding calculation worksheet (filled example)

| Field | Value |
|---|---|
| Source | Co-60, sealed source, primary sample station Room 114 |
| Average gamma energy | 1.25 MeV |
| HVL in lead at this energy | 1.2 cm |
| Unshielded dose rate at wall | 850 mrem/hr |
| Design target (ALARA objective, continuously occupied area) | 1.0 mrem/hr |
| Required attenuation factor | 850 |
| HVLs required (log₂ 850 = 9.73) | 10 (round up) |
| Shielding thickness | 10 × 1.2 cm = 12.0 cm lead-equivalent |
| Post-shield calculated dose rate | 850 / 2¹⁰ = 0.83 mrem/hr |
| Margin to target | 1.0 − 0.83 = 0.17 mrem/hr (17%) |

**Cost-benefit check on the next HVL (11th):**

| Item | Value |
|---|---|
| Marginal thickness | +1.2 cm |
| Estimated marginal material/install cost | ~$4,300 (36 ft² wall panel) |
| Occupancy | 10 workers × 250 hr/yr |
| Dose avoided by 11th HVL | ~0.3 person-rem/yr |
| Value at $2,000/person-rem | ~$600/yr |
| Decision | Cost exceeds benefit — stop at 10 HVLs |

Rule of thumb table for common shielding materials (HVL, MeV 1.0–1.33 gamma, i.e. Co-60 range):

| Material | HVL (cm) | Density (g/cm³) |
|---|---|---|
| Lead | 1.2 | 11.3 |
| Steel | 2.1 | 7.87 |
| Concrete | 6.2 | 2.35 |
| Water | 14.0 | 1.0 |

## 10 CFR 50.59 screening checklist (filled example)

**Proposed change:** relocate a temporary radiation monitor 3 ft from its Tech-Spec-required location during a planned outage, per a maintenance work order.

1. **Does the change affect a design function described in the FSAR?** Yes — the monitor's location is described in FSAR Section 11.4 as providing area coverage for Room 114.
2. **Does it decrease the reliability of a system that mitigates a design-basis accident?** No — the monitor is an area monitor, not a mitigating system; coverage is maintained at the new location per a re-verified line-of-sight calculation.
3. **Does it create the possibility of a new or different kind of accident?** No — the relocation doesn't change any plant system, process, or accident-initiating condition.
4. **Does it exceed or alter a Technical Specification limit?** No — Tech Spec 3.3.7 requires monitor coverage of the room, not a specific coordinate; coverage is preserved.
5. **Screening result:** does NOT require prior NRC approval (50.59(c)(2) criteria not met) — proceed under the facility's internal 50.59 evaluation and document per the site procedure.

*(A "yes" on any of items 1–4 without full mitigation routes the change to Licensing for a 50.59 evaluation and likely a license amendment request — this checklist is a first screen, not the full evaluation.)*

## PRA importance ranking table (filled example, for maintenance-rigor prioritization)

| System/component | CDF (Fussell-Vesely) | Risk Achievement Worth (RAW) | Maintenance rigor tier |
|---|---|---|---|
| Emergency diesel generator A | 0.18 | 12.4 | Tier 1 (highest — quarterly surveillance, dedicated spares) |
| Auxiliary feedwater pump 2 | 0.11 | 8.7 | Tier 1 |
| Component cooling water valve MOV-204 | 0.04 | 22.1 | Tier 1 (low FV, but high RAW — rarely fails, but its failure removes a key barrier) |
| Instrument air compressor 3 | 0.02 | 1.3 | Tier 3 (standard PM interval) |
| Corridor lighting panel | <0.001 | 1.05 | Tier 3 |

**Reading the table:** MOV-204 has a low Fussell-Vesely (doesn't contribute much to *baseline* CDF because it rarely fails) but a high RAW (if it *were* failed, CDF would jump 22x) — it gets Tier 1 rigor despite looking unimportant by failure-rate history alone. This is the concrete case for ranking by PRA importance, not by "how often has this broken."
