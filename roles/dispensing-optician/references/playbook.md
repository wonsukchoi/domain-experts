# Dispensing Optician — Playbook

Filled sequences and reference tables for the fitting process end-to-end. Numbers are stated heuristics unless a specific standard is named — treat as starting points, not universal constants.

## 1. Intake and measurement sequence

Order matters — measuring after frame selection locks in constraints the face may not support.

1. **Distance PD (monocular, each eye to nasal bridge center).** Record OD and OS separately, not just a binocular total — a 64mm binocular PD split 33/31 fits differently than 32/32.
2. **Near PD (if any add power)** — typically 3mm less per eye than distance PD as a starting estimate, confirmed with a near pupillometer read, not assumed from the distance number.
3. **Vertex distance** — measure and record whenever sphere ≥ ±4.00D anywhere in the Rx, or whenever the Rx explicitly states a vertex distance the refraction was performed at.
4. **Pantoscopic tilt target** — standard target ~8-12° from vertical; note if the Rx or the patient's habitual wear (e.g., low-riding frames) suggests a different target.
5. **Fitting height for the specific frame chosen**, measured with the patient in normal head posture, not on a frame board — record the millimeter distance from the lowest point of the lens shape to the pupil center.

## 2. Frame selection against Rx power (worked table)

| Rx sphere magnitude | Recommended eyewire size | Recommended index | Why |
|---|---|---|---|
| 0 to ±2.00D | Any (patient preference) | 1.50-1.56 | Edge thickness immaterial at this power |
| ±2.25 to ±4.00D | Mid-size, avoid large eyewires | 1.60 | Controls edge/center thickness and weight |
| ±4.25 to ±6.00D | Small-to-mid eyewire | 1.67 | Large eyewire at this power produces a visibly thick edge (minus) or heavy center (plus) |
| >±6.00D | Smallest eyewire the face/style allows | 1.74 or polycarbonate/Trivex if impact-resistance also needed | High-index alone doesn't fix a large eyewire choice; both matter |

## 3. Frame material adjustment reference

| Material | Heat response | Adjustment technique | Failure mode if mishandled |
|---|---|---|---|
| Cellulose acetate | Softens ~130-150°F, holds new shape on cooling | Frame warmer, then hand-shape, cool before releasing | Over-relaxed with too much heat, loses shape retention over time |
| Zyl / propionate | Similar to acetate but more solvent-sensitive | Light heat, avoid alcohol-based cleaners near adjustment points | Cracks if flexed cold without heat |
| Nylon / TR-90 | Flexible at room temp, minimal heat needed | Small, incremental adjustments; avoid overheating | Over-flexing without heat causes stress-whitening or crack |
| Monel / stainless metal | Some heat tolerance, mostly cold-adjustable | Standard pliers, solder joints for structural repair | Metal fatigue at solder points from repeated over-bending |
| Titanium / beta-titanium | Springs back near original shape; resists standard heat adjustment | Cold-forming with titanium-rated pliers, incremental small bends | Standard heat gun does nothing useful; forcing a large single bend causes permanent kink instead of smooth curve |

## 4. Lab order — fields that must be explicit, not defaulted

- Rx (sphere, cylinder, axis, add, prism if any) transcribed exactly from the written Rx, not from a prior pair's lensmeter reading.
- Monocular PD (distance and near), fitting height per eye.
- Vertex distance, whenever ≥ ±4.00D anywhere in the Rx.
- Lens material/index, coating requests (AR, photochromic, polarized), and frame material (affects edging bevel choice).
- Any prism or slab-off request, stated as diopters, base direction, and which eye.
- Progressive/bifocal design name — minimum fitting height differs by design and by add power; never assume a generic value.

## 5. Verification checklist before dispensing (every pair, no exceptions)

1. Sphere, cylinder, axis on lensmeter — both lenses — against the written Rx, not the lab's packing slip alone.
2. Add power, if applicable.
3. Prism, if prescribed, including base direction.
4. **Pair check**: with both lenses on the lensmeter reference or on the patient, confirm no unintended vertical or horizontal imbalance beyond ANSI Z80.1 tolerance (prism tolerance: greater of 0.33Δ or one-third of the prescribed amount).
5. Optical center / fitting cross position relative to the recorded PD and fitting height, visually confirmed on the patient's face, not just on the frame board.
6. Frame fit: level, appropriate pantoscopic tilt, temple length, nose pad contact — adjusted, then re-verified on lensmeter if the adjustment was material (see red-flags.md for what counts as material).

## 6. Vertical-imbalance calculation (Prentice's Rule) — step sequence

1. Convert each eye's Rx to spherical equivalent at the point in question (SE = sphere + cylinder/2).
2. Measure `c`, the distance in centimeters from the lens's optical center to the point the patient looks through (e.g., 0.8cm below OC for a typical progressive near zone).
3. Δ (prism diopters) = c × F, computed separately for each eye.
4. Subtract the smaller Δ from the larger — the difference is the induced vertical imbalance between the eyes.
5. If the differential exceeds ~1.5-2.0Δ for an adult (or any amount for a patient with known fusion problems), the fix is compensating prism (commonly a slab-off/reverse-slab ground into the higher-power lens), not a remake to the same design.

## 7. Return-visit triage sequence

1. Re-verify the dispensed pair on the lensmeter against the original Rx and fitting record — confirm sphere/cyl/axis/add/prism and PD/seg-height placement first, before discussing anything with the patient about adaptation.
2. If verification finds a discrepancy from the fitting record: remake, same visit if lab-cut, same-day if in-house edged.
3. If verification confirms everything is to spec: proceed to an adaptation conversation, timeline expectations (3-7 days typical for a first progressive, longer for a ≥1.00D sphere or ≥0.50D cylinder Rx change), and a scheduled recheck at 1-2 weeks if symptoms persist.
4. If the complaint is specifically diplopia (not blur, not "swimming" peripheral distortion) and verification is in spec, escalate to slab-off/prism-compensation review rather than treating it as ordinary adaptation — diplopia from an in-tolerance pair is the vertical-imbalance-stacking scenario, not adaptation.
