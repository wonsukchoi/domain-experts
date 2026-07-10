# Food Science Technician — Playbook

Operational checklists with concrete thresholds. Defaults, not laws — deviate consciously and document why in the record.

## 1. Calibration-verification checklist, by instrument

Run at the start of every shift/run, not just on the scheduled calibration date:

| Instrument | Reference standard | Frequency | In-tolerance band | Action if out |
|---|---|---|---|---|
| Water-activity meter (chilled-mirror) | Saturated salt standard (e.g., NaCl, true aw 0.753) | Start of shift + every 4 hrs of continuous use | ±0.003 aw vs. reference | Stop use, run second standard; if still out, remove from service, tag, notify metrology |
| pH meter | NIST-traceable buffers, 2-point (4.01, 7.00) | Daily 2-point calibration; mid-run verify against 7.00 | ±0.02 pH vs. buffer | Recalibrate; if fails twice, replace electrode |
| Moisture balance | Certified moisture-free reference weight | Daily | ±0.1% of certified value | Recalibrate per manufacturer procedure; log drift trend even if it passes |
| Refractometer (Brix) | Distilled water (0.0 °Brix) + sucrose standard | Daily | ±0.1 °Brix | Zero and recheck; replace prism if scratched/pitted |

**Rule:** a verification failure discovered *after* a batch of samples has been run invalidates every result since the last passing check, not just the one that triggered the discovery — retest the full run from the last known-good verification point.

## 2. OOS / deviation decision tree

Applies to any analytical result outside spec or unexpectedly outside historical range.

1. **Is this a mandatory-hold category regardless of retest?** (Pathogen positive, allergen-swab positive, foreign material, metal-detector reject not cleared by re-pass.) → **Yes: quarantine immediately, file deviation, skip to step 5.** → No: continue.
2. **Sample identity check** — lot number and retain location match the batch record? No → correct the record or re-pull the correct sample; this alone resolves a meaningful share of apparent OOS events.
3. **Instrument verification check** — was the instrument in tolerance at or after the last verification before this test? No → flag as method deviation, re-verify instrument, retest.
4. **Method-execution check** — was every SOP step (equilibration/incubation time, replicate count, sample prep) followed as written? No → flag as method deviation, retest via full SOP.
5. **Retest from a fresh aliquot, triplicate where the SOP allows.** Retest confirms in-spec → release recommendation with full record (original result + root cause + retest data) to supervising scientist/QA. Retest confirms out-of-spec → quarantine, file deviation with raw data, escalate for disposition. **A technician never disposes or releases on their own signature — that's the scientist/QA manager's call.**
6. **File the complete chain** (original result, root cause found, retest data, control-chart context) in the LIMS/paper trail before closing the ticket.

## 3. Environmental monitoring — zones and corrective-action tiers

| Zone | Definition | Example locations | Routine swab frequency |
|---|---|---|---|
| 1 | Food-contact surfaces | Slicer blade, filling nozzle, conveyor belt | Every shift on RTE lines |
| 2 | Non-food-contact surfaces near product | Equipment frame, drip trays, switches near Zone 1 | Weekly |
| 3 | Surfaces further from product but in the processing room | Floor drains, walls, forklift wheels in the room | Weekly to monthly |
| 4 | Outside the processing room entirely | Locker rooms, hallways, receiving dock | Monthly |

**Corrective-action tiers on a Listeria spp. positive:**

- **Zone 1 positive:** immediate stop, clean/sanitize/re-swab before line restart, hold any product run since the last negative Zone 1 result, notify QA and food scientist same-shift.
- **Zone 2/3 positive:** intensified vector swabbing — 10–40 additional swabs radiating outward from the positive site (adjacent equipment, drains, floor) — to trace whether a harborage point exists, not a single re-clean-and-retest. Two consecutive clean rounds (typically 2–4 weeks apart) close the investigation; one clean swab does not.
- **Zone 4 positive:** log and monitor trend; investigate only if repeated or if it correlates with a Zone 2/3 finding nearby.

## 4. Control-chart rules (Xbar-R / individuals charts)

Signals that warrant investigation even when every individual point is inside spec (Western Electric–style rules, applied per monitored CCP/spec parameter):

- One point beyond 3σ from the centerline.
- Two of three consecutive points beyond 2σ on the same side.
- Seven (or more) consecutive points on the same side of the centerline.
- A clear trend of 6+ consecutive points steadily rising or falling.

**Rule:** any of the above triggers a documented look at the process (calibration, raw-material lot, environmental condition) *before* the chart produces an actual spec failure — the chart's value is catching the trend earlier than a pass/fail check can.

## 5. Sensory difference-test logistics checklist

For a triangle test requested by the scientist/QA to confirm or rule out a detectable difference (e.g., reformulation, shelf-life endpoint):

1. Confirm panelist pool meets the protocol's minimum screened count — commonly **n = 24–30** for a standard triangle test at α = 0.05; recruiting fewer produces a test that can only report "not significant," which is not the same as "no difference."
2. Screen panelists for relevant sensory acuity (not a general staff pull) and confirm no product allergen conflicts.
3. Code and randomize sample presentation order per the protocol sheet; never let the panelist see which cup is the "odd" sample or which product is "new."
4. Collect raw individual responses (correct/incorrect), not just the aggregate count, so the significance table lookup and any later reanalysis are auditable.
5. Report the raw correct-count against the significance table for that specific n and α — do not round the panel size or backfill missing responses.

**Worked check:** n = 30, guessing probability 1/3 (mean 10 correct by chance, SD ≈ 2.58). The published critical value at α = 0.05 is 15 correct out of 30. A result of 17/30 correct clears the threshold — report as a statistically significant detectable difference, not as "close to significant."
