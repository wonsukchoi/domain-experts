# Artifacts

## WPS/PQR form (filled example, condensed)

Joint: pressure-vessel nozzle-to-shell T-joint, A516 Gr 70, combined thickness 51 mm (2.0 in).

**WPS-204, Rev 1**

| Field | Qualified range |
|---|---|
| Process | SMAW, root and fill |
| Base metal | P-No. 1, Group 1 or 2 (A516 Gr 70 qualified) |
| Thickness qualified | 3/16 in – 4 in (from 2 in coupon, t/2t rule per QW-451) |
| Filler metal | E7018, F-No. 4, H4 or better (redried, verified) |
| Preheat/interpass | 150°F min / 300°F max (H8 path) or 70°F min / 300°F max (H4 verified path) |
| PWHT | 1100–1200°F, 1 hr/in hold, per UCS-56 |
| Position | 1G, 2G, 5G qualified (coupon welded 5G) |

**PQR-204 test results (coupon basis for the WPS above)**

| Test | Requirement | Result | Pass/fail |
|---|---|---|---|
| Tensile (2 specimens) | ≥ 70 ksi (base metal min) | 74.2, 73.8 ksi | Pass |
| Side bend (4 specimens) | No crack/tear-out > 1/8 in | 0 defects | Pass |
| Charpy V-notch (3 specimens, weld metal, at -20°F) | Avg ≥ 20 ft-lb, no single < 15 ft-lb | 24, 22, 19 ft-lb (avg 21.7) | Pass, low margin — flag for production monitoring |
| Hardness survey (HAZ) | ≤ 248 HV (if sour service applies) | 232 HV max reading | Pass |

## Preheat calculation worksheet (filled example)

Steel: A516 Gr 70. Cert chemistry: C 0.20, Mn 1.10, Si 0.25, Cr 0.10, Mo 0.05, Ni 0.15, Cu 0.15, V nil.

**Step 1 — CE(IIW):**
CE = C + Mn/6 + (Cr+Mo+V)/5 + (Ni+Cu)/15
CE = 0.20 + 1.10/6 + (0.10+0.05+0)/5 + (0.15+0.15)/15
CE = 0.20 + 0.1833 + 0.0300 + 0.0200 = **0.4333 ≈ 0.43**

**Step 2 — combined thickness:** shell 32 mm + nozzle 19 mm = **51 mm (2.0 in)**.

**Step 3 — lookup (AWS D1.1 Annex I, CE 0.35–0.45 group, thickness bracket >38–63 mm):**

| Diffusible hydrogen level | Minimum preheat/interpass |
|---|---|
| H16 (as-received, no drying) | 225°F (107°C) |
| H8 (field-exposed low-hydrogen) | 150°F (66°C) |
| H4 (verified redried) | 70°F (21°C) |

**Decision:** specify the H8/150°F path as the default (no special consumable handling procedure required beyond standard low-hydrogen practice), with the H4/70°F path as an approved alternate if the shop commits to a redry-and-log consumable control procedure for that job.

## PWHT time-temperature plan (filled example)

Vessel shell, 1.25 in thick, A516 Gr 70 (not quenched-and-tempered — no re-temper constraint on this grade).

| Phase | Rate/hold | Value |
|---|---|---|
| Heat-up rate above 600°F | Max per UCS-56 | 400°F/hr ÷ thickness(in) up to 400°F/hr cap → 320°F/hr for 1.25 in |
| Hold temperature | Per UCS-56, P-No. 1 | 1100–1200°F |
| Hold time | 1 hr per inch, 2 hr minimum | 1.25 hr (rounded to 1.5 hr for margin) |
| Cool-down rate above 600°F | Max per UCS-56 | 320°F/hr for 1.25 in |
| Thermocouple placement | Per code, near thickest section and weld | 2 TCs: one on shell OD 2 in from weld toe, one on nozzle OD 2 in from weld toe |

Rule applied: for a quenched-and-tempered grade (skip on this A516 job, apply on A517), add a check that hold temperature stays ≥50°F below the plate's certified tempering temperature before finalizing this chart — a straight UCS-56 lookup alone doesn't carry that constraint.

## Process selection tradeoff (filled example)

Job: 40 ft of field-erected structural seam welds, moderate wind exposure, carbon steel, AWS D1.1 governed.

| Process | Deposition rate | Field wind tolerance | Relative cost/ft | Verdict |
|---|---|---|---|---|
| GMAW (solid wire, spray transfer) | 4–8 lb/hr | Poor — porosity above ~5 mph without shielding | Lowest consumable cost | Rejected — site has no windbreak |
| Gas-shielded FCAW | 6–12 lb/hr | Poor–moderate, same shielding-gas exposure | Low–moderate | Rejected, same reason |
| Self-shielded FCAW (FCAW-S) | 5–10 lb/hr | Good — no external shielding gas to lose | Moderate | **Selected** |
| SMAW | 1–3 lb/hr | Excellent | Highest labor cost per ft (lowest deposition rate) | Backup for tie-in joints too tight for FCAW-S gun access |

Rule applied: wind tolerance eliminated the two gas-shielded candidates before deposition rate or cost were even compared — a screening constraint that removes a process outright takes priority over ranking the survivors on productivity.
