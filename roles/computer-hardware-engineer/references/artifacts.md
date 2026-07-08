# Filled worksheets — SI, PDN, thermal, timing closure

Real table structures and formulas with plausible example numbers, ready to populate with a specific design's data.

## Signal integrity budget worksheet

**Interface:** DDR4-2400 (data rate 2400 MT/s, UI = 1/2400×10⁶ = 416.7 ps, rise/fall time Tr = 150 ps per JEDEC JESD79-4 typical driver spec).

| Step | Formula | Value |
|---|---|---|
| Knee frequency | Fknee = 0.35 / Tr | 0.35 / 150 ps = **2.33 GHz** |
| Per-inch stripline delay (FR4, εr≈4.0) | Tpd ≈ 1.017 × √εr ns/ft ≈ 170 ps/in | 170 ps/in |
| Transmission-line threshold length | Tr / 6 ÷ Tpd | 150 ps / 6 = 25 ps → 25 ps / 170 ps/in = **0.15 in** |
| Verdict | Any trace over 0.15 in one-way is electrically long | Route as controlled-impedance transmission line |
| Target Z0 (single-ended, DDR4 CK/CMD/ADDR) | Per JEDEC JESD79-4 | **40 Ω ±10%** (4.5 mil trace, 4.5 mil dielectric, typical microstrip stack-up hitting 40 Ω) |
| Target Zdiff (DQS differential pair) | Per JEDEC JESD79-4 | **80 Ω ±10%** |
| Byte-lane length-match tolerance | Per JEDEC JESD79-4, DQ to DQS within a byte lane | **±10 mils** |
| Via stub resonant notch check | f = c / (4L√εeff), εeff ≈ 3.2, c = 1.18×10¹⁰ in/s | For L = 60 mil (0.06 in) stub: f = 1.18×10¹⁰ / (4×0.06×1.79) = **2.75 GHz** — inside the 2.33 GHz knee-frequency band of interest → **back-drill required** |

## PDN target-impedance and decoupling-bank worksheet

| Step | Formula | Value |
|---|---|---|
| Rail | — | 0.9 V core |
| Transient current step | Idle → active | 2 A → 10 A, ΔI = **8 A** |
| Current-edge rise time | Vendor power-delivery guideline | **500 ps** |
| Ripple budget | 3% of Vrail | 0.03 × 0.9 = **27 mV** |
| Ztarget | ΔVallowed / ΔI | 0.027 / 8 = **3.375 mΩ** |
| Fknee | 0.35 / Tr | 0.35 / 500 ps = **700 MHz** |
| Board decoupling coverage band | DC to on-die-effective frequency | **DC – 100 MHz** (on-die caps cover above, per vendor spec) |
| Cap ESL (0402 X7R 100 nF, mounted) | Datasheet + via/pad inductance | **0.5 nH** |
| Cap SRF | 1 / (2π√(L·C)) | 1 / (2π√(0.5nH × 100nF)) ≈ **22.5 MHz** |
| Required effective ESL at 100 MHz | Ztarget / (2πf) | 0.003375 / (2π×100×10⁶) = **5.37 pH** |
| Cap count | Cap ESL / required effective ESL | 0.5nH / 5.37pH ≈ **93 caps** (+10 spare pads = 103 total) |
| Bulk cap coverage (below ceramic bank's low-frequency limit) | VRM loop bandwidth ~500 kHz–1 MHz | 4× 100 µF polymer bulk caps at the VR output, ESR-checked against Ztarget at 1 MHz |

## Thermal design worksheet

| Package | Pdiss (W) | θJA (°C/W, JEDEC 2s2p test board) | Tambient (°C, worst-case enclosure) | Tj = Tambient + Pdiss×θJA | Tj,max spec | Margin |
|---|---|---|---|---|---|---|
| BGA SoC (fanless enclosure) | 12 | 18.5 (no airflow) | 55 | 55 + 12×18.5 = **277°C** | 105°C | **FAILS by 172°C — heatsink or airflow required, not optional** |
| Same SoC + heatsink (θJC 0.4, θCS 0.2, θSA 6.5 with 200 LFM forced air) | 12 | θJA' = θJC+θCS+θSA = 0.4+0.2+6.5 = 7.1 | 55 | 55 + 12×7.1 = **140.2°C** | 105°C | **Still fails — need lower θSA heatsink or more airflow** |
| Same SoC + larger heatsink (θSA 3.0 at 200 LFM) | 12 | θJA' = 0.4+0.2+3.0 = 3.6 | 55 | 55 + 12×3.6 = **98.2°C** | 105°C | **Passes, 6.8°C margin — flag as tight, recommend design review if ambient spec ever revises upward** |

## Timing closure worksheet (board-level DDR4 write leveling example)

| Parameter | Value |
|---|---|
| UI (2400 MT/s) | 416.7 ps |
| Setup requirement (controller spec, tSU) | 250 ps |
| Hold requirement (controller spec, tH) | 150 ps |
| Typical-corner propagation skew (DQ vs DQS, matched to ±10 mil = ±1.7 ps) | 1.7 ps |
| Worst-case PVT additional skew (vendor-published, slow-slow/min-V/max-T) | 45 ps |
| Clock/data jitter (RMS × 6σ, vendor-published) | 28 ps |
| **Total worst-case skew+jitter** | 1.7 + 45 + 28 = **74.7 ps** |
| Setup slack at worst-case corner | UI − tSU − total skew/jitter = 416.7 − 250 − 74.7 = **92.0 ps (passes)** |
| Setup slack at typical corner only (naive check) | UI − tSU − typical skew = 416.7 − 250 − 1.7 = **165.0 ps (looks comfortable — misleading if reported alone)** |
| Verdict | Worst-case slack (92.0 ps) is the number that governs sign-off; typical-corner slack (165.0 ps) is not sufficient evidence of closure on its own. |
