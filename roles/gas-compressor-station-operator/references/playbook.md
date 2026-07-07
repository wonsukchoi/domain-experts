# Playbook

Filled worksheets an operator actually runs, not descriptions of them — adapt the numbers to the unit and station in front of you.

## 1. Discharge-temperature worksheet (polytropic compression)

Formula: T2 = T1 · r^((k−1)/k), where T1/T2 are absolute temperature (°R), r is the stage pressure ratio (P2/P1, absolute), k is the ratio of specific heats (≈1.27 for typical pipeline-quality natural gas). Actual temperature rise = ideal (isentropic) rise ÷ polytropic efficiency (typically 0.78–0.85 for a reciprocating unit in reasonable mechanical condition).

Example — single stage, suction 250 psig/90°F, discharge 665 psig (r = 2.35), efficiency 0.82:
T1 = 550°R. r^((k−1)/k) = 2.35^0.2126 ≈ 1.199. Ideal T2 = 550 × 1.199 ≈ 660°R (ideal ΔT ≈ 110°R).
Actual ΔT = 110 / 0.82 ≈ 134°R. Actual T2 ≈ 550 + 134 = 684°R ≈ 224°F.

**Check:** compare actual T2 against (a) the compressor manufacturer's maximum discharge temperature rating and (b) the downstream pipe coating/tariff limit (commonly ~140°F/60°C at the pipeline tie-in, after final aftercooling — not at the raw compressor discharge, which runs hotter before cooling).

**Cooling-capacity-loss adjustment:** if a cooler bank is running at reduced fan capacity, approximate the achievable temperature drop as scaling roughly with remaining fan capacity (e.g., 1 of 2 fans down ≈ half the normal temperature reduction), then re-run the check — do not assume a partial fan loss produces a proportionally small effect on the final delivered temperature.

## 2. MAOP / relief-margin worksheet

1. Confirm MAOP for the segment per §192.619 (lowest of design pressure of the weakest component, prior test pressure basis, or historical operating pressure).
2. Confirm relief valve set point — should be at or below MAOP, per §192.199/§192.201 capacity requirements.
3. Confirm ESD high-pressure trip point — should be set below the relief valve set point, so the ESD acts first.
4. Confirm normal operating (control) setpoint — should carry a working margin below the ESD trip point, not just below MAOP, so ordinary control variation doesn't itself force a trip.

Example: MAOP = 1,440 psig → relief valve set at 1,440 psig → ESD high-pressure trip set at 1,400 psig (≈97% of MAOP) → normal control setpoint held at 1,370–1,390 psig, leaving roughly 10–30 psig of control-variation headroom before the ESD trip engages.

## 3. Odorant-concentration verification worksheet

1. Establish LEL for the gas in service (typical pipeline-quality natural gas ≈ 5% by volume).
2. Compute the detectability threshold: 1/5 of LEL (per §192.625) = LEL × 0.20.
   Example: 5% × 0.20 = 1.0% gas-in-air must be reliably detectable by smell.
3. Sample at the system's farthest, most dilute test point from the odorant injection point — not adjacent to the injector, where odorant concentration is highest and least representative of end-of-line detectability.
4. Compare the sample result (by instrument reading or trained-panel sniff test) against the 1.0% threshold. A result at or below detectability at that concentration passes; a result requiring a higher concentration to detect fails and triggers an injection-rate/pump-function investigation.
5. Log sample location, date, gas LEL basis, computed threshold, and pass/fail result on the compliance worksheet — a "smells fine" note without the concentration basis does not satisfy the requirement.

## 4. PHMSA Part 192 interval-tracking worksheet (compressor station specific)

| Requirement | Section | Interval | Last completed | Deadline |
|---|---|---|---|---|
| Pressure-limiting/regulating station test | §192.739 | ≤15 months, ≥1×/calendar year | 2025-11-02 | 2027-02-02 |
| Overpressure-protective device test | §192.743 | ≤15 months, ≥1×/calendar year | 2025-09-18 | 2026-12-18 |
| Odorant sampling (far-point) | §192.625(f) | Per O&M plan (commonly quarterly) | 2026-04-01 | 2026-07-01 |
| ESD/blowdown functional test | O&M plan | Per O&M plan (commonly annual) | 2025-08-14 | 2026-08-14 |

Internal scheduling target: back the deadline off by 2–3 months for any device test, so a failed test still leaves time to repair and retest before the regulatory deadline — the same discipline applies to odorant sampling and ESD functional tests even where the interval is set by the operator's own O&M plan rather than a fixed CFR clock.

## 5. ESD/blowdown functional-test worksheet

1. Confirm isolation valve sequence: which valves close (unit isolation) before blowdown valves open, per the station's documented ESD sequence — never open blowdown ahead of confirmed isolation.
2. Trigger the ESD (functional test mode) and time the isolation valve closure against its rated stroke time.
3. Open the blowdown path and log depressurization rate (psig/min) against the documented design rate for the piping volume being blown down — a rate significantly slower than design points to a partially plugged blowdown line or an undersized vent orifice; a much faster rate raises concern about liquid slugging or free-jet noise/ignition exposure at the vent stack.
   Example: 1,200 psig station volume designed to blow down to 50 psig within roughly 10 minutes; actual test shows 50 psig reached in 9.5 minutes — within tolerance.
4. Confirm vent stack condition (no obstruction, drain/knockout functioning) before and after the test.
5. Log start pressure, end pressure, elapsed time, and any deviation from the last functional test's timing — a trend of slowing depressurization across tests is itself a finding, even if each individual test technically passes a pass/fail threshold.
