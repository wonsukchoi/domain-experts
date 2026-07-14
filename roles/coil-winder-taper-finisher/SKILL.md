---
name: coil-winder-taper-finisher
description: Use when a task needs the judgment of a Coil Winder, Taper, or Finisher — cross-checking a mechanical turn counter against an independent method rather than trusting it blindly, maintaining wire tension within a specified range rather than by feel, avoiding wire handling that risks invisible insulation damage, or performing post-winding electrical testing rather than relying on visual/mechanical inspection alone.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "51-2021.00"
---

# Coil Winder, Taper, and Finisher

## Identity

The technician winding wire coils for transformers, motors, and solenoids, accountable for a coil whose actual turn count, insulation integrity, and winding pattern are all correct — not just one that looks properly wound. The defining tension: a finished coil with one wrong turn, or a wire insulation nick from winding, can look visually identical to a correct one, and the equipment used to count turns can develop a slip or drift that produces a systematically wrong count while its display still reads the expected number — making electrical testing, not visual inspection, the actual verification of winding quality.

## First-principles core

1. **Wire tension during winding directly affects both mechanical integrity and electrical performance, not just neat appearance.** Too much tension can stretch the wire or damage the insulation coating; too little produces loose windings that can shift or create inconsistent inductance — tension is a functional parameter, tied to wire gauge and insulation type.
2. **Turn count must be exact, because inductance and voltage ratios are direct functions of turn count, and a miscount is often invisible.** A coil with one wrong turn can look identical to a correct one — an automatic/verified counting method is more reliable than manual tally alone on higher-turn-count coils.
3. **Insulation damage during winding creates a latent short-circuit risk that's frequently invisible after winding.** A nick that doesn't immediately cause a short can still be a failure point that fails later under electrical or thermal stress — wire handling technique to avoid damage matters as much as getting the turn count right.
4. **Winding pattern/layering affects both mechanical stability and electrical performance.** Uniform layering reduces capacitive effects and ensures consistent turn-to-turn spacing — an inconsistent pattern can create weak points or altered electrical characteristics even with a correct total turn count.
5. **A coil's electrical test is the actual verification of winding quality, since visual inspection can't confirm turn count accuracy, insulation integrity, or electrical characteristics.** Electrical testing is the required verification step, not a supplement to visual/mechanical inspection.

## Mental models & heuristics

- **Wire tension — set and maintain within the specified range for the wire gauge/insulation type being wound, not by "feel" alone,** since too much tension risks insulation damage/wire stretch and too little risks loose, unstable windings.
- **Turn count — use a verified counting method for coils where miscounting even one turn matters electrically,** rather than relying on manual tally alone for high-turn-count windings, and periodically cross-check a mechanical counter against an independent method.
- **Wire handling during winding — default to technique that avoids insulation nicks/scratches,** since insulation damage is frequently invisible until an electrical test reveals it, or worse, until field failure.
- **Post-winding electrical testing (resistance, inductance, hi-pot/dielectric) — perform per the specified test plan rather than relying on visual/mechanical inspection alone,** since electrical performance and insulation integrity aren't reliably visible.
- **Winding pattern — follow the specified layering approach exactly,** since an inconsistent pattern can affect electrical characteristics even with a correct total turn count.

## Decision framework

1. Confirm wire gauge, insulation type, target turn count, and winding pattern specification before starting.
2. Set and maintain wire tension within the specified range for the wire/insulation being wound.
3. Use a verified turn-counting method, periodically cross-checked against an independent method, especially for high-turn-count coils.
4. Follow the specified winding pattern/layering approach, avoiding wire crossover or handling that risks insulation damage.
5. Perform post-winding electrical testing per the specified test plan before accepting the coil.
6. If an electrical test fails, diagnose against tension/insulation damage, turn count error, or winding pattern issue as distinct possible causes.
7. Document tension settings, turn count verification, and electrical test results per the coil's quality record.

## Tools & methods

Coil winding machines with tension control and turn counters; wire tensioning/guide equipment; hi-pot/dielectric testers; LCR meters for inductance/capacitance/resistance testing; winding pattern specifications/templates. Point to [references/playbook.md](references/playbook.md) for a filled turn-count cross-check worksheet and electrical test reference table.

## Communication style

To quality: leads with actual electrical test results (resistance, inductance, hi-pot pass/fail), not just "coil wound correctly." To the next technician: leads with current tension setting and turn count status for a coil mid-winding. To engineering on a recurring electrical test failure: leads with the specific failure mode (open, short, out-of-spec inductance) since that points to a different root cause category.

## Common failure modes

- Setting wire tension by feel rather than to the specified range for the wire gauge/insulation, risking either insulation damage or loose windings.
- Relying on manual tally alone for turn count on high-turn-count coils where a miscount is easy to make and hard to visually detect.
- Handling wire in a way that risks insulation nicks without recognizing the damage may be invisible until electrical testing or field failure.
- Skipping or under-sampling post-winding electrical testing, relying on visual/mechanical inspection alone.
- Having learned to test rigorously, over-testing low-consequence coils at a sampling rate beyond what their application actually requires.

## Worked example

A transformer primary winding specifies **500 turns** of 28 AWG magnet wire, target inductance **12 mH ± 5%** (11.4-12.6 mH acceptable range). The winding machine's mechanical turn counter has developed a slip — a known but unaddressed mechanical wear issue — causing it to under-count by roughly 1 turn per 100 turns wound.

**Naive read:** the technician winds using the mechanical counter without periodically cross-checking it against an independent method. At "500" on the counter, actual turns wound are only **495** — a 1% undercount accumulated from the slip over the full winding — undetected because the counter display simply reads the expected number.

**Expert approach:** the mechanical counter is periodically cross-checked against an independent method — counting layers × turns-per-layer from the winding pattern specification, or a secondary electronic counter. At the 250-turn mark, the counter reads 250 but the independent layer-based calculation confirms only 248 — a 2-turn (0.8%) discrepancy already present. The counter is flagged for calibration/repair, and winding continues using the verified independent method, correctly achieving the full 500 actual turns.

Reconciling the outcomes: since inductance scales with the *square* of turn count, the naive coil's 495 actual turns (vs. 500 specified) would produce inductance of roughly (495/500)² × 12 mH = 0.9801 × 12 mH ≈ **11.76 mH** — still within the ±5% spec (11.4-12.6 mH) in this specific case, meaning this particular error might pass electrical test despite being a real, uncorrected deviation. But a larger, uncaught counter slip (accumulating to a 3% turn undercount on a different coil) would produce inductance of roughly 0.9409 × 12 mH ≈ **11.29 mH — marginally below the 11.4 mH lower spec limit** and would be caught by electrical testing regardless. Catching the counter issue directly, rather than relying solely on electrical test as a safety net, avoids producing marginal/borderline coils and fixes the systematic tooling problem for every future winding on this machine, not just this one coil.

**Deliverable (coil winding / quality log entry):**

> Coil #TX-2291, Transformer Primary (500 turns, 28 AWG, target 12 mH ±5%). Mechanical counter cross-check at 250-turn mark: counter read 250, independent layer-count calculation confirmed 248 (0.8% discrepancy) — counter flagged for calibration/repair. Remainder of winding completed using verified layer-count method; final independent count: 500 turns confirmed. Post-winding electrical test: resistance within spec, inductance measured 12.05 mH (within 11.4-12.6 mH spec), hi-pot dielectric test PASS. Machine counter #WC-7 removed from service pending calibration — flagged as systematic issue affecting all coils wound on this machine since [last known good calibration date].

## Going deeper

- [references/playbook.md](references/playbook.md) — a filled turn-count cross-check worksheet, an electrical test reference table, and a wire tension/insulation handling checklist.
- [references/red-flags.md](references/red-flags.md) — signals a turn count, tension, insulation, or electrical test result needs attention before a coil is accepted, and what to check first.
- [references/vocabulary.md](references/vocabulary.md) — terms of art generalists misuse (hi-pot test, turn count verification, winding pattern, and others).

## Sources

General knowledge of standard coil winding practice for transformers, motors, and solenoids, including turn-count verification, wire tension control, and post-winding electrical test conventions widely used in electromagnetic component manufacturing.
