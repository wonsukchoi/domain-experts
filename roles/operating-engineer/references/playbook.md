# Operating Engineer — Playbook

Filled reference sequences: load-chart interpolation and rigging deductions, utility-locate color code and tolerance-zone workflow, grade-tolerance verification, and swing-radius exclusion-zone math.

## 1. Load chart interpolation and net-capacity check

Example chart shape for a 55-ton-class hydraulic truck crane, 105 ft main boom, on fully extended outriggers, 360° rotation (illustrative — always pull the actual OEM chart for the specific machine and boom length in use):

| Working radius | Gross capacity |
|---|---|
| 20 ft | 32,000 lb |
| 25 ft | 24,000 lb |
| 27 ft | 21,000 lb |
| 30 ft | 18,000 lb |
| 35 ft | 13,000 lb |
| 40 ft | 11,000 lb |

(Capacity does not decrease linearly with radius — boom moment is a physical, curved relationship, so a chart's decrements between listed radii are never assumed to be even. Always read the specific radius from the actual chart page rather than interpolating between two published lines.)

**Working steps:**

1. Confirm configuration (outriggers fully extended and crane leveled, vs. on-rubber) — pull the chart page that matches, never blend.
2. Identify every radius the load will pass through during the lift, not just the pick point: the pick radius, any radius reached while swinging clear of obstructions, and the set-down radius. Chart against the largest of these.
3. Sum rigging deductions below the hook — headache ball/hook block, slings, spreader bar or lifting beam, any below-the-hook attachment — and subtract from gross chart capacity to get net capacity.
4. Compare load weight to net capacity at the largest radius in the path. Target load at or under roughly 85% of net capacity for a routine lift as a standing margin beyond the chart's own built-in safety factor.
5. If load exceeds 85% of net capacity (or exceeds net capacity outright), the fix is a configuration change that reduces the required radius — reposition the crane pad closer, use a longer boom section with a steeper working angle, or add counterweight/increase outrigger spread if the OEM chart supports a higher-capacity configuration — not a decision to "ease into it."

**Rigging deduction reference (illustrative, confirm against the specific rigging in use):**

| Item | Typical weight |
|---|---|
| Headache ball / overhaul ball | 150–350 lb |
| Hook block (multi-part) | 300–800 lb |
| Slings (per leg, wire rope or synthetic) | 20–150 lb |
| Spreader bar / lifting beam | 200–1,500 lb depending on capacity rating |

## 2. Utility locate and tolerance-zone workflow

**APWA Uniform Color Code:**

| Color | Facility type |
|---|---|
| Red | Electric power lines, cables, conduit |
| Yellow | Gas, oil, steam, petroleum, gaseous materials |
| Orange | Communication, alarm, signal lines, cables, conduit |
| Blue | Potable water |
| Purple | Reclaimed water, irrigation, slurry |
| Green | Sewer, drain lines |
| Pink | Temporary survey markings |
| White | Proposed excavation limits/route |

**Workflow:**

1. Submit an 811/one-call locate ticket before any mechanized excavation; confirm all utility owners have responded (clear, marked, or "can't locate — needs manual verification") before digging.
2. Treat every paint mark or flag as the centerline of an approximate location, not a survey point — the tolerance zone is commonly 18–24 in. either side of the mark (confirm the exact figure against the responding utility owner and state one-call center rules, since the band varies by jurisdiction).
3. Anywhere mechanized excavation will cross the tolerance zone, hand-dig or vacuum-excavate (pothole) to expose the actual utility before bringing bucket, trencher, or auger equipment within the zone.
4. Track locate ticket validity — commonly good for a defined working-day window (frequently cited around 10–15 business days depending on jurisdiction) — and refresh the ticket if the job runs past that window or if marks have faded, been disturbed, or been paved/graded over.
5. Log any discrepancy between the locate mark and what's found during potholing (depth, offset, or an unmarked line) back to the one-call center and the utility owner immediately — a single unreported discrepancy is how the next crew on the same site hits the same line.

## 3. Grade-tolerance verification

| Grade type | Commonly cited tolerance | Notes |
|---|---|---|
| Rough grade / subgrade prep | ±0.1 ft (≈1.2 in) | Checked against a laser or GPS grade-control benchmark before starting cut/fill; the standard most earthwork specs cite for base preparation |
| Fine grade (base course, paving prep) | ±0.05 ft (≈0.6 in) | Tighter than rough grade; typically checked more frequently across the same run |
| Finish grade (under slab, flatwork) | ±0.25 in (commonly specified locally, verify against project spec) | The tightest tolerance in the sequence; a benchmark error here shows up as a visible slab high/low spot |

**Working steps:**

1. Before starting any cut or fill run, verify the grade-control laser or GPS system against a known benchmark or control point — do not trust the prior day's calibration without a spot-check.
2. If a spot-check reads outside the tolerance band for that grade type, stop and re-verify the benchmark itself before continuing — a shifted or bumped benchmark produces a plausible, consistent wrong reading across the whole run, which is why it isn't caught by a single spot-check partway through.
3. Re-check tolerance at defined intervals across a long run (not only at the start and end), since a benchmark or receiver drift accumulates gradually rather than announcing itself.
4. Record the actual measured deviation when logging a grade check, not "close enough" — the next trade (paving, slab, utility) is building on the number logged, not on a visual impression.

## 4. Swing-radius / exclusion-zone math

```
Exclusion zone radius = max working (boom/bucket) radius + counterweight swing radius + buffer
```

- OSHA 1926.1424(g) requires a barricade for any accessible area where clearance between the rotating superstructure (including counterweight) and a fixed object or a person is 2.5 ft or less — treat 2.5 ft as the minimum clearance, not a target.
- Counterweight swing radius on a mobile crane commonly extends several feet behind the machine's tracks/tires — confirm the specific machine's counterweight swing dimension from its spec sheet rather than estimating by eye.
- For excavators and other machines with a conventional (non-zero) tail swing, the rear of the house swings outside the track/undercarriage footprint on rotation — the exclusion zone has to account for this even when the bucket/boom side looks clear.
- Add a buffer beyond the calculated minimum (commonly a few feet) to absorb positioning error in the barricade placement itself, not just the machine's swing.
- Confirm a qualified signal person is stationed with a clear sightline to both the operator and any ground personnel before rotation or travel begins in a zone with foot traffic — the barricade and the signal person are independent controls, not substitutes for each other.
