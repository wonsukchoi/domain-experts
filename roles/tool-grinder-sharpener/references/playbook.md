# Playbook

## Wear-pattern diagnostic table

| Wear pattern | Likely cause | Action |
|---|---|---|
| Uniform wear across all cutting edges | Normal abrasive wear | Standard regrind, no process flag needed |
| Chipping concentrated on some (not all) edges | Interrupted cut, excessive feed, or misalignment | Flag to process engineering; regrind clearing full chip depth + margin |
| Discoloration / heat tinting | Heat generation issue (insufficient coolant, excessive speed) in application | Flag to process engineering for cutting parameter review |
| Built-up edge (material adhered to cutting face) | Inadequate lubrication or wrong cutting speed for material | Flag to process engineering; clean thoroughly before regrinding |
| Cracking along a specific geometric feature (not random) | Possible original manufacturing defect or design stress concentration | Flag to tool engineering/supplier, not just a process issue |

## Regrind-depth calculation worksheet

| Field | Value |
|---|---|
| Tool | End Mill #EM-8842, 4-flute 0.500" carbide |
| Measured chip/damage depth | 0.008" |
| Clearance margin for subsurface damage | 0.004" |
| Total regrind depth | 0.012" |
| Spec relief angle | 10° |
| Spec rake angle | 5° |
| Post-regrind measured relief | 10.1° |
| Post-regrind measured rake | 4.9° |
| Within tolerance? | Y |
| Cumulative regrinds to date | record actual |
| Estimated remaining regrinds before retirement | record actual |

**Rule:** regrind depth = measured damage depth + clearance margin, never set by visual "looks clean" judgment alone.

## Heat management checklist for tool sharpening

1. Confirm coolant delivery is active and reaching the grinding contact point before starting.
2. Use light, incremental passes rather than aggressive single-pass material removal, especially on hardened/carbide tooling.
3. Monitor for any discoloration or visible heat signs during and after grinding.
4. If heat discoloration appears, treat the affected area as potentially reduced in hardness — consider additional inspection or a more conservative regrind approach for that tool.
5. Allow adequate cooling time between passes on tools sensitive to heat buildup.
6. Document grinding parameters (pass depth, coolant use) for tools where heat sensitivity is a known concern.
