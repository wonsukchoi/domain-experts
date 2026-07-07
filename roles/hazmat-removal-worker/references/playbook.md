# Containment sizing, respirator selection, and clearance playbook

Filled worksheets for the four recurring hazmat-removal decisions: negative air machine sizing, respirator-class selection by exposure multiple, clearance sampling parameters, and the decontamination sequence.

## 1. Negative air machine sizing / ACH calculator

```
Required CFM (derated) = enclosure volume (ft³) × required ACH ÷ 60
Required nominal (clean-filter) CFM = required derated CFM ÷ 0.5 (50% filter-loading derate)
Achieved ACH at nominal rating = (selected unit CFM × 60) ÷ enclosure volume
```

| Enclosure | Volume (ft³) | Required ACH | Required derated CFM | Required nominal CFM | Selected unit | Margin |
|---|---|---|---|---|---|---|
| Mechanical room, Class I TSI removal | 4,050 | 4 | 4,050×4÷60 = 270 | 270÷0.5 = 540 | 750 CFM | +39% over required nominal |
| Small bathroom, Condition 3 mold (S520) | 800 | 4 | 800×4÷60 = 53 | 53÷0.5 = 106 | 500 CFM | +372% — single smallest available unit still oversized; normal for small rooms |
| Basement, lead RRP interior demo | 2,400 | 4 | 2,400×4÷60 = 160 | 160÷0.5 = 320 | 750 CFM | +134% |

Rule: never size off the clean-filter rated CFM alone — the 50% derate accounts for filter loading over a shift; a unit that only clears the derated-CFM line at hour one will drop below 4 ACH before the filter change interval.

## 2. Respirator-class selection by exposure multiple

```
Effective exposure = measured or assumed 8-hr TWA ÷ Assigned Protection Factor (APF)
Pass condition: effective exposure < applicable PEL, with margin — not equality
```

| Task / contaminant | Measured or default exposure | PEL | Multiple of PEL | Respirator | APF | Effective exposure |
|---|---|---|---|---|---|---|
| Asbestos Class I, TSI removal, no negative exposure assessment on file | 0.9 f/cc | 0.1 f/cc | 9x | Full-facepiece PAPR (1926.1101 Class I default) | 1,000 | 0.0009 f/cc |
| Asbestos Class II, resilient floor tile removal, negative exposure assessment on file (<0.05 f/cc historically) | 0.04 f/cc | 0.1 f/cc | 0.4x | Half-face APR (documented NEA supports step-down) | 10 | 0.004 f/cc |
| Lead RRP interior demolition, no monitoring data (default assumption per RRP practice) | Assume ≥ action level | 50 µg/m³ (general industry PEL) | Assumed elevated | Half-face APR minimum, escalate on visible dust generation | 10 | Per-task; escalate if visible dust exceeds containment control |
| Mold Condition 3, visible growth >100 sq ft, no quantitative air data (standard for mold — no OSHA PEL exists) | N/A — S520 default | N/A | N/A | Full-facepiece APR with P100, minimum per S520 for Condition 3 | 50 | N/A — driven by containment level, not a PEL multiple |

Rule: a half-face APR (APF 10) run at any multiple above roughly 8-9x PEL leaves under 15% margin before a seal leak or underestimated task-disturbance level pushes effective exposure over the PEL — escalate the respirator class, not the assumption.

## 3. Clearance sampling parameters by contaminant

| Contaminant | Method | Sample parameters | Clearance criterion | Result if failed |
|---|---|---|---|---|
| Asbestos (school/AHERA-triggered project) | Aggressive air sampling, PCM (NIOSH 7400) | 5 stations minimum, 10 L/min × 130 min = 1,300 L/station | < 0.01 f/cc (AHERA clearance) | Re-clean/re-wet the specific failed station's area only; re-sample that area |
| Asbestos (non-AHERA, PCM ambiguous or elevated) | TEM analysis | Same air volumes, sent for TEM if PCM is inconclusive or above criterion | ≤ ~70 structures/mm² (lab/project-specific action level) | Re-clean and re-sample; do not release on a borderline PCM alone |
| Lead (RRP post-abatement) | Dust-wipe sampling, EPA-recognized lab | 1 sq ft wipe per surface type (floor, sill, trough), per room | Floor 10 µg/ft², interior sill 100 µg/ft², window trough 400 µg/ft² | Re-clean the specific surface/room that failed; re-wipe only that surface type |
| Mold (Condition 3, post-remediation per S520) | Visual + moisture-meter verification; third-party air/surface sampling by preference, not OSHA-mandated | Per remediation protocol's stated sampling plan (no single federal numeric standard) | Visual: no residual growth/debris; moisture: at or below material's dry-standard reading; sampling (if used): comparable to outdoor/reference sample | Re-clean and re-verify moisture source before re-testing — a passing wipe over an active moisture source is a temporary pass |

Rule: clearance samples are location-specific. A failed sample re-opens the specific area it represents, not the whole containment — re-cleaning stations that already passed wastes the shift without addressing the failure point.

## 4. Decontamination sequence checklist

```
1. Remove gross contamination (HEPA-vacuum or wet-wipe outer suit) while still inside containment/decon chamber.
2. Doff outer protective suit, inside the decon chamber, contaminated side folded inward.
3. Doff boot covers/gloves, inside the decon chamber.
4. Exit decon chamber into the clean-side airlock.
5. Doff respirator LAST, only once fully outside the contaminated-side chamber.
6. Respirator cleaned/disinfected or cartridges/filters changed per manufacturer schedule before reuse.
```

Rule: the respirator comes off last, never before the suit — reversing steps 2 and 5 is the single most common way a "clean" exit recontaminates the worker's face and airway.
