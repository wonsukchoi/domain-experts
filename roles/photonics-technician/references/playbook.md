# Playbook — splice, inspection, and test worksheets

Filled worksheets, not templates to describe. Copy the row structure and substitute real numbers.

## 1. Fiber end-face inspection worksheet (IEC 61300-3-35)

**Header block (record before scoring any zone):**

| Field | Value |
|---|---|
| Connector / traveler # | LC/UPC, traveler WO-4471 |
| Fiber type | Single-mode, 9/125 µm |
| Scope | 400x video probe, cal cert current |
| Grade applied | Grade 2 (multimode/single-mode general use — not Grade 1 high-power or Grade 3 UPC-tolerant) |

**Zone table — connector single-mode, Grade 2, PC/UPC:**

| Zone | Radius from core center | Scratches allowed | Defects (pits/chips) allowed |
|---|---|---|---|
| A — Core | 0–25 µm | None ≥3 µm | None ≥2 µm |
| B — Cladding | 25–120 µm | No limit if <3 µm width | 5 max, ≤10 µm each |
| C — Adhesive | 120–130 µm | No limit | No limit |
| D — Contact | 130–250 µm | No limit | No limit, unless defect chips into Zone B |

**Filled example — connector under test:**

| Item | Value | Zone limit | Verdict |
|---|---|---|---|
| Zone A scratch, longest | 2.1 µm wide | <3 µm allowed | PASS |
| Zone A pit | none observed | 0 allowed ≥2 µm | PASS |
| Zone B chip, largest | 31 µm | ≤10 µm each (5 max) | **FAIL** |
| Zone B chip count ≥ limit size | 1 | ≤5 | FAIL (single oversized defect fails independent of count) |
| Zone C/D | adhesive bead within zone, no debris in B | not scored pass/fail (3rd ed. 2022) | N/A |

**Rule:** a single Zone A or Zone B defect exceeding its size limit fails the connector regardless of all other zones passing — do not average or "mostly clean" a verdict. Re-cleave and re-polish before re-inspection; do not attempt to re-clean a chip (chips are not contamination and don't clean out).

## 2. Splice-loss budget worksheet

**Header block:**

| Field | Value |
|---|---|
| Segment | Patch panel A → bench 12, OM4 multimode, 850 nm |
| Length | 150 m |
| Splice method authorized | Mechanical (fusion splicer unavailable, insufficient pull-through) |
| Acceptance ceiling (traveler) | ≤1.00 dB total |

**Budget build-up:**

| Line item | Basis | Value |
|---|---|---|
| Fiber attenuation | 150 m × 3.0 dB/km (OM4 @850nm, datasheet) | 0.45 dB |
| Splice loss | Mechanical splice ceiling per method | up to 0.50 dB |
| Connector loss (new far-end connector, typical) | 0.20–0.40 dB/mated connector *pair*; only one new connector is being terminated here, not a full pair, so half that range applies | ≤0.20 dB |
| **Budgeted total (worst case)** | sum | 1.15 dB — exceeds 1.00 dB ceiling on paper |
| **As-measured total (bidirectional OTDR + power-meter cutback)** | actual | 0.81 dB |
| Margin vs. ceiling | 1.00 − 0.81 | 0.19 dB |

**Rule:** always carry both the worst-case budgeted total (for go/no-go planning before work starts) and the as-measured total (for traveler close-out). A worst-case budget over ceiling is not a stop condition by itself — proceed and measure; a worst-case budget *under* ceiling with no splice yet made is not a pass either, since the actual splice can still land near its method ceiling.

**Method-ceiling reference table:**

| Splice method | Typical loss | Ceiling to budget against |
|---|---|---|
| Fusion, single-mode, good execution | 0.01–0.05 dB | 0.10 dB |
| Fusion, multimode | 0.05–0.10 dB | 0.15 dB |
| Mechanical, single-mode or multimode | up to 0.3 dB typical | 0.5 dB |

## 3. OTDR trace read — dead-zone check worksheet

**Header block:**

| Field | Value |
|---|---|
| Launch condition | Direct from patch panel A connector (no launch cord) |
| Pulse width | 30 ns (short-range setting for <5 km span) |
| Strong reflective event | 0 m, reflectance −25 dB (patch panel connector) |

**Dead-zone geometry table (typical, this OTDR/pulse-width class):**

| Zone type | Definition | Typical extent at −25 dB reflectance, 30 ns pulse |
|---|---|---|
| Event dead zone (EDZ) | Min. spacing to resolve two separate reflective events | ~1–3 m |
| Attenuation dead zone (ADZ) | Min. distance after an event before loss can be accurately measured | ~10–15 m (used: 12 m) |

**Filled example:**

| Item | Value |
|---|---|
| Reflective event position | 0 m |
| ADZ extent at this reflectance/pulse width | ~12 m |
| Splice under test, position | 62 m |
| Splice position minus event position | 62 − 0 = 62 m |
| Inside ADZ? | 62 m > 12 m → **No, outside dead zone** |
| Conclusion | Flat trace section reflects a real absence of excess loss at 62 m, not a masking artifact; the bidirectional splice-loss reading stands |

**Decision rule:**
1. Identify every reflective event upstream of the feature under test and its reflectance.
2. Look up (or bracket from vendor spec) the ADZ extent at that reflectance and the pulse width used.
3. If feature position − event position < ADZ extent → **re-run with a launch cord** long enough to push the reference plane past the ADZ, then re-read. Do not report the original trace's silence at that position as a result.
4. If feature position − event position ≥ ADZ extent → the trace read at that position is valid as-is.
5. Always confirm a splice or connector loss reading bidirectionally (A→B and B→A OTDR shots, averaged) — a unidirectional OTDR reading can differ by 0.1 dB or more from the true loss at a fiber mismatch, splice, or connector.

## 4. L-I-V sweep and burn-in worksheet

**Header block:**

| Field | Value |
|---|---|
| Part | Laser diode, 1550 nm DFB, datasheet threshold Ith ≤ 15 mA, slope efficiency ≥0.20 W/A |
| Test temp | 25.0 °C ± 0.5 °C (TEC-controlled) |
| Sweep range | 0–80 mA forward current, 0.5 mA step |

**L-I-V sweep results:**

| Current (mA) | Optical power (mW) | Forward voltage (V) |
|---|---|---|
| 5 | 0.02 (below threshold — spontaneous emission) | 1.02 |
| 15 | 0.15 (at/near threshold — kink check point) | 1.08 |
| 20 | 1.20 | 1.11 |
| 40 | 5.20 | 1.18 |
| 60 | 9.30 | 1.24 |

| Derived value | Calculation | Result | Datasheet limit | Verdict |
|---|---|---|---|---|
| Threshold current (Ith) | Linear extrapolation of above-threshold slope back to P=0 | 14.2 mA | ≤15 mA | PASS |
| Slope efficiency | ΔP/ΔI between 20–60 mA = (9.30−1.20)/(60−20) | 0.2025 W/A | ≥0.20 W/A | PASS |
| Kink check | Slope discontinuity between 15–25 mA band | None >5% deviation observed | none allowed | PASS |

**Burn-in worksheet:**

| Field | Value |
|---|---|
| Condition | 70 °C case temp, 1.2x rated drive current, per screening spec |
| Duration | 168 hours (7-day standard infant-mortality screen) |
| Monitored parameter | Optical power at fixed current, logged hourly |
| Degradation threshold | >5% power drop from 24-hour baseline → fail, remove from lot |
| Result, this unit | 24 hr baseline 9.30 mW → 168 hr reading 9.11 mW (−2.0%) | within 5% → **PASS** |

**Rule:** a part exhibiting a kink (slope discontinuity) anywhere in the sweep fails regardless of meeting Ith and slope-efficiency numbers at the tested points — a kink indicates a mode instability that a single-point Ith/slope check will not catch. Always sweep continuously through the region 50% below to 150% above expected threshold, not just spot-check three currents.

## 5. Hermeticity / ESD handling worksheet

**ESD pre-handling checklist (verify before touching any ESD-sensitive part, ANSI/ESD S20.20):**

| Check | Method | Threshold | Result |
|---|---|---|---|
| Wrist strap continuity | Wrist strap tester | <3.5 MΩ to ground | 1.2 MΩ — PASS |
| Mat resistance to ground | Mat tester | 1×10⁶–1×10⁹ Ω | 4.7×10⁷ Ω — PASS |
| Ionizer (if required for isolated-conductor parts) | Offset voltage check | <±35 V isolated-conductor limit | −8 V — PASS |
| Part HBM/CDM class | Datasheet lookup | 100 V HBM / 200 V CDM typical floor | Class 1B HBM (100V–250V) — full protocol required |

**Helium leak test worksheet (GR-468-CORE, per MIL-STD-883 TM 1014 Condition A):**

| Field | Value |
|---|---|
| Package internal volume | 0.05 cm³ |
| Required leak rate spec | ≤5×10⁻⁸ atm·cc/sec (He) |
| Detector sensitivity floor | 1×10⁻⁹ atm·cc/sec |
| Measured result | "No leak detected" (below 1×10⁻⁹ floor) |
| Is this a pass against spec, or a floor artifact? | Floor artifact — detector cannot distinguish "true zero leak" from "leak below 1×10⁻⁹," and spec ceiling (5×10⁻⁸) is above the floor, so **this result is a valid pass**, not ambiguous |
| Escalate to destructive IGA? | Only if the required spec threshold itself is below the detector floor (not the case here) — this lot closes out on the mass-spec result alone |

**Rule for the ambiguous case:** if the *required spec threshold* is numerically below the detector's stated sensitivity floor, "no leak detected" cannot be recorded as a pass on its own — route a sampling percentage (per the qualification plan, typically 3–5 units per lot) to destructive Internal Gas Analysis for moisture content, and record the IGA result, not the leak-check non-result, as the qualifying data point.
