# Electromechanical Technician — Playbook

Filled diagnostic sequences and threshold tables. Run these as written; the thresholds are the acceptance criteria, not starting points for judgment calls.

## 1. Megger + polarization index procedure

**Equipment:** Megohmmeter, test voltage set per motor rated voltage:

| Motor rated voltage | Test voltage (DC) |
|---|---|
| < 1000 V | 500 V |
| 1000–2500 V | 1000 V |
| 2501–5000 V | 2500 V |
| 5001–12000 V | 5000 V |

**Sequence:**
1. De-energize, LOTO, discharge windings to ground (residual charge can read false-high).
2. Connect megger leads: line lead to each phase in turn (or all three shorted together), ground lead to frame.
3. Apply test voltage, start timer at 0:00.
4. Record reading at **60 seconds** (1-min IR).
5. Continue the same test uninterrupted; record reading at **600 seconds** (10-min IR).
6. Compute **PI = 10-min reading ÷ 1-min reading**.
7. Discharge windings to ground for at least 4× the electrification time before disconnecting leads.

**Acceptance:**
- 1-min IR minimum (IEEE 43): **rated kV + 1 MΩ**. Example: 460 V motor → 0.46 + 1 = **1.46 MΩ minimum**.
- PI interpretation (Class B/F/H windings):

| PI | Condition |
|---|---|
| < 1.0 | Dangerous — do not energize |
| 1.0 – 1.9 | Questionable / contaminated |
| 2.0 – 3.9 | Good |
| ≥ 4.0 | Excellent (verify not over-drying/embrittlement on older insulation) |

- If 1-min IR passes but PI < 2.0: log as **contamination fail**, not electrical clear. Schedule dry-out (heat gun or motor-dryer ramp, typically 4–8 hr at controlled rise ≤ 5°C/hr to target winding temp 80–105°C depending on insulation class) and re-test PI before return to service.

## 2. ISO 10816/20816 vibration zone tables

Overall RMS velocity (mm/s), by machine class. Use the class matching the equipment, not a single generic table.

**Class I** (small machines, up to 15 kW, integrally connected):

| Zone | Range (mm/s RMS) |
|---|---|
| A | 0 – 0.71 |
| B | 0.71 – 1.80 |
| C | 1.80 – 4.50 |
| D | > 4.50 |

**Class II** (medium machines, 15–75 kW, no special foundation; up to 300 kW on rigid mount):

| Zone | Range (mm/s RMS) |
|---|---|
| A | 0 – 1.40 |
| B | 1.40 – 2.80 |
| C | 2.80 – 7.10 |
| D | > 7.10 |

**Class III** (large rigid-mounted machines):

| Zone | Range (mm/s RMS) |
|---|---|
| A | 0 – 2.30 |
| B | 2.30 – 4.50 |
| C | 4.50 – 11.20 |
| D | > 11.20 |

**Zone meaning:** A = new-machine condition, B = acceptable for unrestricted long-term operation, C = unsatisfactory for continuous operation — plan corrective action, D = damage-risk, stop and repair.

**Procedure:**
1. Take overall RMS velocity at drive-end and non-drive-end bearing housings, horizontal + vertical + axial.
2. Classify against the correct machine class table above.
3. If Zone A/B: log as "no broadband problem" — this does **not** clear bearing/gear-mesh faults. Run FFT spectral analysis if a specific fault (bearing, gear mesh) is suspected regardless of zone.
4. If Zone C/D: schedule corrective action before Zone D; stop machine if Zone D.

## 3. MCSA sideband math

**Rotor bar defect sidebands:** appear at `f₁(1 ± 2s)` around line frequency, where f₁ = line frequency (Hz), s = per-unit slip = (n_sync − n_actual) / n_sync.

Example: 4-pole motor, 60 Hz line, nameplate speed 1755 RPM.
- n_sync = 120 × 60 / 4 = 1800 RPM.
- s = (1800 − 1755) / 1800 = 0.025.
- Sidebands at 60 × (1 ± 0.05) = **57 Hz and 63 Hz**.
- Sideband amplitude −45 dB to −40 dB below fundamental: early-stage rotor bar defect, monitor and trend. −35 dB or higher (closer to fundamental): broken/cracked bar, schedule replacement.

**Bearing fault frequencies** (modulate current sidebands at f₁ ± m·f_bearing, where f_bearing is BPFO, BPFI, or BSF from bearing geometry):
- BPFO (ball pass frequency, outer race) = (N_b/2) × f_r × (1 − (Bd/Pd) cos θ)
- BPFI (inner race) = (N_b/2) × f_r × (1 + (Bd/Pd) cos θ)
- N_b = number of rolling elements, f_r = shaft rotational frequency (Hz), Bd = ball diameter, Pd = pitch diameter, θ = contact angle (0° for a deep-groove ball bearing under pure radial load, cos θ = 1 — use the manufacturer's specified contact angle for angular-contact or tapered-roller bearings).
- Example: 6205 deep-groove ball bearing (θ = 0°), N_b = 9, Bd/Pd ≈ 0.213, f_r = 29.25 Hz (1755 RPM): BPFO ≈ 9/2 × 29.25 × (1 − 0.213 × 1) ≈ **103.6 Hz**. This modulates current at f₁ ± BPFO: the sum term is 60 + 103.6 = **163.6 Hz**, the difference term is |60 − 103.6| = **43.6 Hz** (a negative difference folds to its absolute value — there is no physical −43.6 Hz component). A sideband at either 163.6 Hz or 43.6 Hz, with amplitude within 45–50 dB of the fundamental, flags an outer-race defect 90–120 days ahead of a Zone C vibration reading.

## 4. Decay-test vs. ultrasonic leak decision table

| Symptom | Test to run first | Procedure | Pass/fail threshold |
|---|---|---|---|
| Cylinder "slow" or "soft," no audible hiss | Pressure decay | Pressurize to rated operating pressure, isolate supply, monitor drop over 60 s | < 5% pressure drop / 60 s = pass (internal seal OK); ≥ 5% = internal (piston seal) bypass, rebuild required |
| Audible hiss at fittings or rod seal | Ultrasonic leak detector | Scan fittings, rod seal, port connections at ~40 kHz with directional probe | Any localized signal > 6 dB above ambient = external leak, tighten/reseal at that point |
| Slow AND audible hiss | Run both, in that order | Decay test first isolates internal vs. external; ultrasonic then localizes the external component | Decay < 5% and no ultrasonic hit = false alarm, check downstream valve/flow control instead |

Do not skip the decay test because a hiss is audible — internal bypass can coexist with an unrelated external leak, and fixing only the audible one leaves the machine still failing.

## 5. Crimp pull-test minimums (IPC/WHMA-A-620)

Pull rate: **~25 mm/min (1 in/min)**, motorized wire grip + fixed terminal clamp, axial pull to break or to slip.

| AWG | Class 1 min (lbf) | Class 2 min (lbf) | Class 3 min (lbf) |
|---|---|---|---|
| 24 | 8 | 10 | 12 |
| 22 | 12 | 15 | 18 |
| 20 | 18 | 22 | 26 |
| 18 | 25 | 30 | 35 |
| 16 | 35 | 40 | 45 |

(Values are IPC/WHMA-A-620 practitioner-referenced minimums by class; verify against the current revision for the exact terminal/wire combination in use — some connector families publish tighter OEM minimums that supersede the generic table.)

**Sequence:**
1. Select sample crimps from the same batch/operator/machine setting as the production run (not a single cherry-picked good one).
2. Mount in pull-tester, zero the gauge, pull at 25 mm/min to failure or wire slip-out.
3. Record peak force. Compare to the class minimum for that AWG.
4. Failure mode matters: wire breaks before terminal slips = good crimp, marginal wire; terminal slips off wire = bad crimp, re-terminate and re-test full batch.
5. Log per-batch pass rate; < 100% pass on a sampled batch triggers 100% re-inspection of that batch, not just the failed sample.

## 6. NFPA 70E arc-flash PPE category table

Per Table 130.7(C)(15)(a), incident energy at 18-inch working distance:

| PPE Category | Minimum incident energy | Example minimum PPE |
|---|---|---|
| CAT 1 | ≥ 4 cal/cm² | Arc-rated shirt/pants or coverall, face shield or arc flash hood, hard hat, safety glasses, hearing protection, leather gloves |
| CAT 2 | ≥ 8 cal/cm² | Same as CAT 1 plus arc-rated arc flash hood or balaclava, higher-rated fabric |
| CAT 3 | ≥ 25 cal/cm² | Arc flash suit (jacket + pants or coverall), arc-rated hood, layered system |
| CAT 4 | ≥ 40 cal/cm² | Full arc flash suit, highest-rated hood, double-layer switching coat/pants |

**Sequence:**
1. Pull the equipment's arc-flash label if present — it states incident energy or PPE category and working distance directly. Use it.
2. If no label: use the category-based table method only if the equipment matches a listed task/equipment combination in Table 130.7(C)(15)(a) (e.g., "MCC, insulated case or molded case circuit breaker, 240 V and below, up to 25 kA fault current, 0.03 sec clearing time") — otherwise an incident-energy analysis is required, do not guess.
3. Don PPE at or above the determined category before LOTO on the enclosure — LOTO verification itself (voltage check) is inside the arc-flash boundary and requires PPE.
4. Re-verify PPE category if fault current or clearing time has changed since the label/analysis date (breaker settings changed, upstream protection modified) — a stale label is a red flag, not a clearance.
