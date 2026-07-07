# Playbook

Filled reference material: DVC/SVC wiring-configuration tables, the gain-setting worksheet, the parasitic-draw isolation sequence, and the ADAS calibration-trigger checklist.

## 1. Subwoofer wiring-configuration tables (final impedance seen by the amp)

**Two identical subs, single voice coil (SVC), each rated 4-ohm:**

| Wiring | Final load |
|---|---|
| Both subs in series | 8-ohm |
| Both subs in parallel | 2-ohm |

**Two identical subs, dual voice coil (DVC), each coil rated 4-ohm (4 coils total):**

| Wiring | Final load |
|---|---|
| All 4 coils in series | 16-ohm |
| Each sub's coils in series (8-ohm/sub), subs in parallel | 4-ohm |
| Each sub's coils in parallel (2-ohm/sub), subs in series | 4-ohm |
| All 4 coils in parallel | 1-ohm |

Note the gap: with a DVC 4-ohm pair, there is no wiring path to 2-ohm final load. An amp whose rated-power sweet spot is 2-ohm will only ever see 1-, 4-, or 16-ohm from this specific sub pairing — 1-ohm is the one to reject if the amp's stable floor is 2-ohm.

**One SVC 2-ohm sub + one SVC 4-ohm sub (mismatched pair — generally avoid, included for the arithmetic):**

| Wiring | Final load |
|---|---|
| Series | 6-ohm |
| Parallel | 1.33-ohm (2×4 ÷ (2+4)) |

Mismatched-impedance pairs also split power unevenly between the two subs at any given final load — a further reason to spec a matched pair before wiring, not after.

## 2. Amplifier power-at-load reference (Ohm's-law-derived, for setting expectations before quoting)

For an amp rated at **P₁ watts at R₁ ohms**, rated power at a different stable load R₂ follows roughly P₂ ≈ P₁ × (R₁ / R₂) for a well-regulated Class D design (manufacturer's own multi-load spec table is authoritative — this is a planning estimate, not a substitute for the datasheet).

| Rated spec | Estimated at 4-ohm | Estimated at 2-ohm | Note |
|---|---|---|---|
| 300W @ 4-ohm / 500W @ 2-ohm (stable ≥2-ohm) | 300W | 500W | Worked-example amp; do not wire below 2-ohm. |
| 75W @ 4-ohm ×4ch / 150W ×2ch bridged @ 4-ohm | 75W/ch stereo | 150W/ch bridged | Bridged-mono minimum is commonly double the per-channel stereo minimum on 4-channel amps — check the specific datasheet. |

## 3. Gain-setting worksheet (calculated AC-voltage method)

1. Confirm the amp's rated power at the **actual wired final impedance** (not the amp's best-case spec), from step 1's wiring table and the manufacturer's load-specific power rating.
2. Compute target speaker-output voltage: **V = √(P × R)**.
3. Set all EQ/bass-boost/subsonic controls to their flat/neutral or manufacturer-recommended starting position before setting gain — these interact with gain and must be set first.
4. Play a reference test tone (commonly 40–50Hz for a sub channel) at a fixed, moderate head-unit volume (a common convention is ~75% of the source's maximum clean output, verified with the distortion detector on the head unit's own pre-out first).
5. With a DMM in AC-voltage mode across the speaker output leads, adjust the amp's gain control until the reading reaches the target V from step 2.
6. Confirm with a distortion detector or oscilloscope that the output is a clean sine wave (no flat-topping) at that setting; if clipping shows before reaching target V, the upstream signal (head-unit pre-out or LOC) is clipping first — fix that stage, don't compensate by leaving gain low.
7. Record the target voltage and the achieved reading on the work order.

**Worked-example figures:** 300W @ 4-ohm → V = √(300 × 4) = √1200 ≈ **34.6V AC**, achieved with the distortion-detector clip indicator dark.

## 4. Parasitic-draw diagnostic sequence

| Step | Action | What it isolates |
|---|---|---|
| 1. Baseline | Measure resting draw before any install work, after a full 20–40 min sleep cycle (all doors closed, no key nearby to avoid fob wake-up). | Establishes this vehicle's own normal, before any variable is added. |
| 2. Install | Complete the install per the decision framework. | — |
| 3. Post-install measurement | Re-measure resting draw after the same 20–40 min sleep cycle, doors closed. | Confirms whether the install added draw at all. |
| 4. Compute delta | Post-install draw − baseline draw. | Quantifies what the install itself added, independent of the vehicle's own baseline variability. |
| 5. Compare to expectation | Delta in the low teens of mA or less for most standby remote-start/alarm modules is expected; higher warrants isolation. | Distinguishes "normal for this module" from "something's wired wrong." |
| 6. Isolate (if delta is high) | Pull the new accessory's fuse (or use a clamp meter/fused jumper at each new circuit) one at a time, re-measuring after each pull. | Identifies which specific new circuit is causing the excess draw. |
| 7. Inspect the identified circuit | Check the isolated wire against the harness/bypass-module pinout diagram — confirm switched vs. constant routing. | Finds the specific mis-wire (commonly a trigger wire on the wrong circuit). |
| 8. Correct and re-verify | Re-wire per the harness diagram; repeat steps 1–5's post-install measurement. | Confirms the fix before delivery, not just after it "should" work. |

**Reserve-capacity-to-days-before-drain estimate:** usable capacity (Ah, to the shop's practical depth-of-discharge floor) ÷ draw (A) = hours until that floor is reached.

| Battery usable capacity | Draw | Hours to DoD floor | Days |
|---|---|---|---|
| 35Ah | 0.288A (288 mA — faulty) | ≈121.5 hr | ≈5.1 days |
| 35Ah | 0.053A (53 mA — corrected) | ≈660 hr | ≈27.5 days |
| 35Ah | 0.042A (42 mA — factory baseline alone) | ≈833 hr | ≈34.7 days |

## 5. ADAS recalibration-trigger checklist

Check after any job that involves removal or reinstallation of a windshield, front bumper cover, grille, side mirror housing, or rear hatch/glass panel — even when the accessory work itself targeted something else nearby.

- [ ] Identify every camera/radar/ultrasonic sensor mounted at or behind the panel that was removed (forward camera behind windshield, radar behind front bumper/grille badge, ultrasonic park sensors in bumper cover, blind-spot radar in rear bumper).
- [ ] Confirm whether the OEM specifies **static** calibration (target boards, level floor, fixed distance), **dynamic** calibration (drive cycle at specified speed on lane-marked roads), or both for this platform and sensor.
- [ ] If in-house equipment covers the platform, perform calibration and record the result (pass/fail, target values if the tool reports them).
- [ ] If in-house equipment does not cover the platform, refer to a calibration-equipped shop by name on the work order — do not release the vehicle with an unresolved calibration need undocumented.
- [ ] Run a post-calibration (or post-referral) scan confirming no ADAS-related DTCs before delivery.
- [ ] If no panel in any sensor's mounting or optical path was disturbed, note "ADAS calibration not applicable — no sensor path disturbed" on the work order, rather than leaving the topic unaddressed.
