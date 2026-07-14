# Playbook

## Embrittlement-relief timing worksheet

Fill for any embrittlement-susceptible material batch.

| Field | Value |
|---|---|
| Batch # | PK-2291 |
| Material | High-strength steel fasteners, embrittlement-susceptible grade |
| Pickling parameters | 10 min, 10% HCl, 70°F (spec: 8-12 min) — within spec |
| Pickling completion timestamp | record actual |
| Required bake-start window | Within 4 hours of pickling completion |
| Actual bake start timestamp | record actual |
| Elapsed time (pickling to bake start) | calculate |
| Within required window? | Y/N |
| Bake parameters (temp/duration) | 375°F / 4 hr (verify against spec) |
| If window missed: disposition | Hold for sustained-load embrittlement verification testing — do NOT release on bake-completion alone |
| If window met: disposition | Standard release per normal QA process |

## Bath concentration monitoring table

| Check interval | Action |
|---|---|
| Per facility schedule (e.g., every shift or per volume processed) | Titrate bath, record actual concentration |
| Concentration below spec minimum | Add acid per calculated makeup, re-verify before resuming production |
| Concentration significantly above expected (rare) | Investigate — may indicate an addition error; re-verify before use |
| Iron content trending upward over multiple checks | Plan for bath replacement/dump per facility's iron-buildup threshold, don't wait for a failure |

**Rule:** never assume concentration based on elapsed time or nominal makeup — always verify via titration or equivalent measurement at the specified interval.

## Rinse verification checklist

1. After pickling, process part through the specified rinse sequence (may include multiple rinse stages).
2. Check rinse water pH or conductivity per the facility's specified acceptance criteria — not visual appearance alone.
3. If reading indicates residual acid/contamination above acceptance threshold, re-rinse before proceeding.
4. Document rinse verification result for the batch before it proceeds to the next process step (coating, baking, shipping).
5. For embrittlement-susceptible material proceeding to baking: confirm rinse is complete and adequate before baking, since baking a part with acid residue can complicate both the baking process and part quality.
