# Nanofabrication Playbook

Filled templates for technique selection, ALD/CVD process specs, MEMS/NEMS release sequencing, and metrology calibration tracking. Populate with the run's actual numbers — the structures below are the artifact, not a description of one.

## 1. Lithography technique-selection table

Score each candidate 1–5 per axis for the target run, then apply the volume gate. Do not average the scores into a single number — the triangle is a tradeoff, not an optimization.

| Technique | Resolution floor | Throughput | Cost/die at target volume | Volume gate |
|---|---|---|---|---|
| E-beam direct-write | ~5 nm | ~0.5–2 mm²/hr (serial) | $$$$ | <1,000 units/yr, or R&D/mask-making |
| DUV/optical (193i) | ~38 nm half-pitch | >100 wafers/hr | $ at volume, $$$$$ NRE | >100,000 units/yr |
| Nanoimprint (NIL) | ~10 nm features, ~10 nm 3σ overlay | ~10–60 wafers/hr | $$ | 1,000–100,000 units/yr, overlay budget ≥10 nm 3σ |

**Worked selection example.** Target: 40,000 sensor die/yr, feature CD 25 nm, overlay budget 15 nm 3σ.
- E-beam: resolution fine, throughput fails the gate — at the table's low end (0.5 mm²/hr), writing the ~4 mm² patterned area per die takes 8 hr/die; 40,000 die/yr × 8 hr = 320,000 tool-hours needed against one tool's realistic ~8,000 tool-hours/yr (2 shifts, ~90% uptime) — a ~40x shortfall — reject.
- DUV: resolution fine (38 nm floor is below what's needed only if CD target ≥38 nm; here CD target is 25 nm — DUV alone cannot hit it without a resolution-enhancement pitch-split, which adds $$$$ NRE not justified at 40,000/yr) — reject.
- NIL: resolution (10 nm) and overlay (10 nm 3σ) both clear the 25 nm CD / 15 nm overlay budget with margin; volume (40,000) sits inside the 1,000–100,000 gate — **select NIL**.

Document the rejected options and why in the process selection memo — a later reviewer re-litigating the choice should be able to see the gate math, not just the conclusion.

## 2. ALD process parameter template

Fill every field before a recipe goes to pilot. Growth-rate arithmetic must reconcile: `cycles × nm/cycle = target thickness`.

```
Material:                 Al2O3 (trimethylaluminum + H2O)
Precursor growth rate:     0.11 nm/cycle  [source: qualified on prior lot, recheck quarterly]
Target thickness:          4.4 nm
Cycles required:           40   (40 × 0.11 = 4.4 nm — reconciles)
Substrate temp:             150–300 °C  (process window; report actual set point)
Feature aspect ratio:       100:1
Pulse time (precursor):     0.5 s  →  revise to 0.625 s (+25%) if bottom-of-feature
                                       conformality <95% of top measurement
Purge time:                 3 s   →  add 2 s purge step if precursor starvation suspected
Target step coverage:       >95% (top vs. bottom CD ratio ≥0.95)
Accept/reject threshold:    bottom/top CD ratio <0.95 → hold lot, open deviation memo
Thickness uniformity spec:  ±1%  (wafer-to-wafer and within-wafer)
```

**Escalation ladder when conformality misses spec:**
1. First miss (ratio 0.90–0.95): extend pulse time +25%, add 2 s purge, requalify — do not release the failing lot.
2. Second miss after the pulse/purge fix (ratio still <0.95): suspect precursor delivery line temperature or aspect ratio underestimated at feature design — pull SEM cross-section before touching recipe again.
3. Third consecutive miss: stop the line. This is no longer a tuning problem — escalate to process engineering review with full lot history.

## 3. CVD/PVD parameter template (lower-aspect-ratio, cost-sensitive coating)

```
Deposition method:          PECVD (SiN barrier layer)
Target thickness:           50 nm
Deposition rate:            25 nm/min  →  process time 2 min
Feature aspect ratio ceiling: use only below 10:1 — above that, switch to ALD template
Line-of-sight coverage loss: expect 15–30% sidewall thinning at 5:1 aspect ratio;
                             reject if measured sidewall <70% of top-surface thickness
Chamber pressure:            600–900 mTorr
Substrate temp:              250–400 °C
```

## 4. MEMS/NEMS wet-release sequence

Execute in this order. Each step has a stop condition — do not proceed past a stop condition without documenting why.

1. **Sacrificial layer etch** (e.g., HF vapor or wet BOE release of oxide). Stop condition: etch time exceeds 120% of the qualified time for this geometry → pull and inspect under SEM before continuing; over-etch undercuts anchors.
2. **Rinse cascade** (DI water, minimum 3 cycles). Stop condition: resistivity <17 MΩ·cm on final rinse → add a cycle; ionic residue seeds later stiction nucleation sites.
3. **Transition to intermediate fluid** (IPA or acetone, per process qualification). Stop condition: none — this step exists to avoid a direct water→air interface, not to meet a spec.
4. **Drying — default path: supercritical CO2 critical-point drying.**
   - Chamber pressure: bring to supercritical (>1,071 psi, >31.1 °C) before venting.
   - Vent rate: slow bleed, avoid pressure gradient that reintroduces a liquid-vapor interface.
   - Accept condition: zero visible interface transition during vent — if a visible meniscus reappears, the batch is at stiction risk; re-run the supercritical transition rather than accepting the lot.
5. **Fallback drying — if supercritical CO2 equipment unavailable: SAM coating before ambient-air drying**, in this preference order (trading hydrophobicity against process compatibility):
   1. OTS (octadecyltrichlorosilane) — best hydrophobicity, most moisture-sensitive during application; use in <30% RH environment only.
   2. FDTS (perfluorodecyltrichlorosilane) — vapor-phase compatible, more process-tolerant than OTS, slightly lower hydrophobic contact angle.
   3. DDMS (dichlorodimethylsilane) — most process-compatible and easiest to apply, weakest hydrophobicity; use only when the structure's restoring force is high enough that marginal stiction resistance is sufficient (check spring constant vs. capillary force estimate before selecting).
6. **Post-release inspection**: optical or SEM survey for collapsed/stuck structures. Stiction failure rate >2% of die on a qualified process → stop, do not ship, open deviation memo citing which release step is suspect.

## 5. Metrology calibration checklist (CD-AFM / CD-SEM)

Run before accepting any measurement as process-representative rather than instrument artifact.

- [ ] Tip identity logged (serial number) and cross-referenced against tip-wear history.
- [ ] Tip radius last verified: within 30 measurement-days or 500 scans, whichever is sooner. Re-verify if either threshold is exceeded before trusting a new reading.
- [ ] Calibration standard measured same-session, reading within stated uncertainty (<1 nm for CD-AFM at 10 nm tip radius).
- [ ] If a process reading falls outside expected 3σ band: re-measure with a second, independently-calibrated tip before opening a process deviation — this separates instrument drift from real process shift.
- [ ] Tip wear flag: after 500 scans on a single tip, treat radius as suspect (+1–2 nm growth typical) even if last calibration passed — schedule re-verification rather than waiting for the next scheduled interval.
- [ ] Record top, mid, and bottom-of-feature measurements for any conformality-sensitive process (ALD, high-aspect-ratio etch) — a top-only reading cannot detect the starvation failure mode in Section 2.

## 6. Cleanroom class assignment (ISO 14644-1)

Assign per process step, not one blanket class for the whole line — over-classifying a low-sensitivity step wastes cost, under-classifying a lithography step introduces defects that show up as the nonlinear yield collapse described in the SKILL.md core.

| Process step | Typical ISO class | Rationale |
|---|---|---|
| Photolithography / e-beam exposure | ISO 3–5 | Particle-to-CD ratio is worst here; a single >0.1 µm particle can kill a sub-30 nm feature |
| ALD/CVD deposition | ISO 5–6 | Chamber is largely sealed during process; particle risk concentrated at load/unload |
| Wet etch / release | ISO 6–7 | Lower particle sensitivity than exposure steps; fluid handling dominates contamination risk instead |
| Packaging / dicing | ISO 7–8 | Downstream of critical-dimension-defining steps; particle tolerance loosens accordingly |
