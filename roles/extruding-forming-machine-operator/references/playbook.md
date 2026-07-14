# Playbook

## Draw-down/wall-thickness worksheet

Fill whenever takeoff speed or extrusion rate is adjusted.

| Field | Before change | After change |
|---|---|---|
| Extrusion (screw) rate | baseline | record actual |
| Takeoff speed | baseline | +8% (example) |
| Draw-down ratio | baseline (matched) | if only takeoff changed: ratio increases |
| OD measured | 4.000" | 3.995" (in spec — sizing compensated) |
| Wall thickness measured | 0.237" nominal | 0.220" (NOT compensated by sizing — check separately) |
| Wall thickness in spec? | Y | N — requires correction |
| Correction | — | Increase extrusion rate proportionally with takeoff speed to restore original draw-down ratio |
| Post-correction wall thickness | — | 0.236" (in spec) |
| Post-correction OD | — | 4.002" (in spec) |

**Rule:** any takeoff speed change requires a corresponding wall thickness check — OD staying in spec does not confirm wall thickness stayed in spec.

## Die swell compensation reference (illustrative — always use actual process characterization data)

| Material | Typical swell range (die opening vs. final dimension) |
|---|---|
| Rigid PVC | 3-5% smaller die opening than target final dimension, adjusted per specific formulation |
| Polyethylene (HDPE) | 5-10%, higher swell than rigid PVC |
| Polypropylene | 5-8%, varies by grade |

**Rule:** these figures are illustrative starting points only — actual die dimension must be established through process characterization (trial runs with dimensional verification) for the specific material, die, and process combination in use, not assumed from a generic table.

## Melt temperature/residence-time monitoring checklist

1. Confirm material's recommended processing temperature range from its technical data sheet.
2. Set melt temperature at the lowest point within that range that achieves adequate melt homogeneity — not the highest "for safety margin."
3. Calculate/monitor residence time based on current line speed and barrel/die volume.
4. If line speed decreases for any reason (a rate change, a downstream slowdown), recheck whether resulting residence time at current temperature still stays within the material's degradation-safe window.
5. Periodically sample and test for degradation indicators (color, mechanical properties) especially after any process speed or temperature change, not just at job start.
6. Document actual melt temperature and estimated residence time (not just setpoints) in the process log.
