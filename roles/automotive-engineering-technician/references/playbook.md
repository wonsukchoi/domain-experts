# Playbook

Filled templates for the three recurring instrumentation/data-reduction jobs: shunt-calibration verification, sample-rate/CFC channel setup, and rainflow/Miner's-rule damage reduction.

## 1. Shunt-calibration worksheet

Run immediately before every test session on a strain-gauge bridge — not just at initial bonding.

**Inputs to record before shunting:**

| Field | Value |
|---|---|
| Bridge configuration | Full bridge |
| Gauge factor (GF) | 2.06 |
| Excitation voltage (Vex) | 10.000 V |
| Target simulated strain (ε_sim) | 3,000 µε |
| Shunt resistor value | 59,880 Ω (sized for 3,000 µε at this GF/bridge config per gauge vendor table) |

**Predicted output:**

```
V_predicted = GF × ε_sim × Vex
            = 2.06 × 0.003000 × 10.000 V
            = 61.80 mV
```

**Measured output (from DAQ, shunt engaged):** record to 2 decimal places, e.g. 61.42 mV.

**Acceptance check:**

```
Error % = (V_predicted − V_measured) / V_predicted × 100
        = (61.80 − 61.42) / 61.80 × 100
        = 0.61%
```

| Error % | Disposition |
|---|---|
| ≤ 1% | Pass — signal chain verified, proceed to test |
| 1%–2% | Flag — recheck connectors/excitation before proceeding; log the value |
| > 2% | Fail — do not run; re-terminate bridge, re-verify excitation, repeat shunt-cal |

[1% pass threshold — practitioner-stated program convention; confirm against the specific test plan's stated shunt-cal tolerance before treating it as universal.]

**Record on the test log:** date, technician, bridge ID, GF, Vex, shunt resistor value, predicted mV, measured mV, error %, disposition. A shunt-cal entry older than the current test session does not cover today's run — re-run it even if the bridge was checked yesterday.

## 2. Sample-rate / CFC channel-setup matrix

Use when a test plan doesn't already specify sample rate and filter corner for a channel.

**Step 1 — estimate highest frequency of interest (f_max)** from prior test data on the same/similar component, or the engineer's stated bandwidth of concern.

**Step 2 — sample rate:**

```
f_sample = f_max × 5   (minimum field-practice multiplier)
   through
f_sample = f_max × 10  (preferred when disk/DAQ bandwidth allows)
```

**Step 3 — anti-alias filter corner:**

```
f_filter = f_sample ÷ 4   (upper bound)
   through
f_filter = f_sample ÷ 10  (lower bound, preferred)
```

**Step 4 — map to nearest SAE J211 CFC class** (corner frequency ≈ CFC ÷ 0.6):

| CFC class | Corner frequency | Typical use |
|---|---|---|
| CFC 60 | 100 Hz | Structural/durability-rate loads (suspension links, control arms, chassis mounts) |
| CFC 180 | 300 Hz | General dynamic/vibration channels |
| CFC 600 | 1,000 Hz | Impact/crash-adjacent transients |
| CFC 1000 | 1,667 Hz | High-rate impact channels |

**Worked selection — suspension control-arm strain channel, f_max ≈ 50 Hz:**

| Step | Calculation | Result |
|---|---|---|
| Sample rate | 50 Hz × 10 | 500 Hz |
| Filter corner | 500 Hz ÷ 5 | 100 Hz |
| CFC match | CFC = corner × 0.6 = 100 × 0.6 = 60; check: 60 ÷ 0.6 = 100 Hz | **CFC 60** |

Record the chosen sample rate, filter corner, and CFC class on the test plan so the next technician re-using the channel doesn't have to re-derive it. When no precedent exists and the channel content is genuinely uncertain, default to CFC 60 for structural/durability loads and escalate only if the engineer flags higher-frequency transient content of interest.

## 3. Rainflow-counting / Miner's-rule damage reduction

**Step 1 — collect the raw stress/strain time history** from the reduced strain-gauge channel over the test interval (e.g., 500 test-hours).

**Step 2 — rainflow-count into discrete stress-amplitude bins**, each with a cycle count `n`.

**Step 3 — look up cycles-to-failure `N` at each bin's stress amplitude** from the component's S-N (stress-life) curve.

**Step 4 — compute damage fraction per bin and sum (Miner's rule):**

```
D = Σ (n_i / N_i)
```

**Worked table (500 test-hours, front lower control arm):**

| Bin | Stress amplitude Sa | Cycles counted, n | Cycles to failure, N | n/N |
|---|---|---|---|---|
| A | 180 MPa | 1,200 | 50,000 | 0.02400 |
| B | 120 MPa | 8,500 | 400,000 | 0.02125 |
| C | 80 MPa | 45,000 | 2,000,000 | 0.02250 |
| **Total D** | | | | **0.06775** |

**Step 5 — extrapolate to a central life estimate** (linear damage accumulation to D = 1.0):

```
Life_central = test_hours / D
             = 500 / 0.06775
             = 7,380 test-hours
```

**Step 6 — bracket with the documented correlation error band (2.7%–31%)** rather than reporting the central estimate alone:

```
Life_low  = 7,380 × (1 − 0.31) = 5,092 test-hours
Life_high = 7,380 × (1 + 0.31) = 9,668 test-hours
```

**Step 7 — disposition rule:**

| Situation | Action |
|---|---|
| Range brackets or exceeds the target life with margin | Recommend inspection interval at the low end of the range; note as sufficient for now |
| Range straddles the target life | Route to engineer of record — recommend a second independent S-N reference to narrow the band before a hard interval is set |
| Low end of range is below the target life | Escalate immediately — do not close out; recommend design review |

Never file a bare point-estimate life number without the bracketed range and the disposition line — the point estimate alone hides the method's known uncertainty from the engineer signing the release decision.
