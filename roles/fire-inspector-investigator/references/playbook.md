# Fire Inspector/Investigator — Playbook

## Occupant-load factors by occupancy type (NFPA 101 Table 7.3.1.2, selected)

| Occupancy | Factor | Basis |
|---|---|---|
| Assembly, concentrated (standing, no fixed seats) | 7 net sq ft/person | Net floor area |
| Assembly, less-concentrated (tables/chairs) | 15 net sq ft/person | Net floor area |
| Business | 100 gross sq ft/person | Gross floor area |
| Mercantile, street floor | 30 gross sq ft/person | Gross floor area |
| Mercantile, upper/basement floor | 60 gross sq ft/person | Gross floor area |
| Educational, classroom | 20 net sq ft/person | Net floor area |
| Storage | 300 gross sq ft/person | Gross floor area |

**Net vs. gross:** net excludes walls, columns, restrooms, and fixed equipment footprint; gross includes everything within the exterior walls. Using gross where net applies understates the occupant load — the single most common calc error in mercantile-to-assembly occupancy reclassifications (e.g., a retail space converted to an event venue without a re-inspection).

## Egress-width factors (NFPA 101 Table 7.3.3.1)

| Component | Unsprinklered | Sprinklered (NFPA 13) |
|---|---|---|
| Stairs | 0.3 in/person | 0.2 in/person |
| Level components (doors, corridors, ramps) | 0.2 in/person | 0.15 in/person |

Required width = occupant load × factor for the relevant component. Compare against **measured clear width** (door leaf width minus hardware/stop encroachment, typically 1.75–2 inches per side), not the nominal door-frame width.

## Scene-preservation timing checklist

| Phase | Action | Deadline |
|---|---|---|
| Active suppression | Note first-arriving-crew observations (smoke color, flame location, forcible-entry conditions) | Before overhaul begins |
| Immediately post-knockdown | Photograph/video scene before overhaul disturbs char patterns and debris | Before overhaul begins |
| Overhaul | If overhaul is operationally necessary before investigator arrival, document who performed it and what was moved | Same shift |
| Witness canvass | Collect statements from occupants/bystanders while memory is fresh | Within 24–48 hours |
| Origin mapping | Diagram char depth, V-patterns, low-burn indicators against a to-scale floor plan | Within first scene visit |
| Sample collection | Pull ILR samples (ASTM E1618) from origin-area debris before weather/cleanup exposure | Same visit as origin mapping |

## Origin-and-cause report outline (filled example)

```
1. SCOPE AND METHODOLOGY
   Investigation conducted per NFPA 921 (current edition). Scene examined
   [date]. Prior reports/documents reviewed: [list].

2. FACTUAL FINDINGS (observations only — no opinion)
   - Structure: [occupancy classification, construction type, sprinkler status]
   - Fire department response: [arrival time, initial conditions observed]
   - Fire patterns observed: [location, description — V-patterns, char depth
     measurements, low-burn indicators]
   - Witness statements: [summarized, attributed]
   - Laboratory results: [ILR sample results, lab report reference]

3. ANALYSIS
   3.1 Origin determination: [pattern/witness/dynamics correlation reasoning]
   3.2 Cause hypotheses tested:
       Hypothesis A — Electrical: [evidence for/against, eliminated/retained]
       Hypothesis B — Human/incendiary: [evidence for/against, eliminated/retained]
       Hypothesis C — [mechanical/natural/other]: [evidence for/against]

4. OPINION AND CONCLUSION
   Cause classification: [Accidental / Incendiary / Undetermined]
   Confidence level: [reasonable degree of professional certainty / insufficient
   evidence to reach a conclusion]
   Basis: [cross-reference to Section 3 findings]

5. CODE COMPLIANCE FINDINGS (independent of cause)
   [Egress, occupant load, fire-protection-system violations, cited separately
   from cause classification]
```
