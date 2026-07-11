# Veterinary Technician Playbook

Filled procedures and reference tables for the technical work of the role. Numbers are illustrative reference values calibrated to typical small-animal practice — verify against the specific protocol, drug label, or equipment manual before use.

## 1. Anesthesia monitoring flowsheet (filled example)

Patient: 32 kg canine, ASA II, dental prophylaxis with extractions, isoflurane. Protocol: reassess and log every 5 minutes; escalate to the veterinarian if two or more parameters move adverse across two consecutive checks.

| Time | Jaw tone | Palpebral | HR (bpm) | RR (/min) | SpO2 (%) | ETCO2 (mmHg) | Iso (%) | Action |
|---|---|---|---|---|---|---|---|---|
| T+0 (post-induction) | Loose | Absent | 96 | 14 | 99 | 38 | 1.8 | Positioned, radiographs taken |
| T+10 | Loose | Absent | 90 | 12 | 99 | 39 | 1.6 | Prophy started |
| T+20 | Loose | Absent | 88 | 12 | 98 | 40 | 1.4 | Scaling in progress |
| T+25 | Moderate | Sluggish/present | 92 | 12 | 98 | 40 | 1.4 | Extraction started, fentanyl CRI running |
| T+35 | Moderate | Sluggish/present | 118 | 18 | 97 | 44 | 1.4 | HR/RR rising with probe stimulus on extraction site — reassess plane, do not increase vaporizer yet |
| T+40 | Tight | Present, brisk | 128 | 20 | 97 | 46 | 1.4→1.8 | Composite confirms light plane (jaw + palpebral + HR + RR together) — vaporizer increased |
| T+45 | Loose | Absent | 96 | 13 | 98 | 40 | 1.8 | Plane re-established, extraction resumed |

Rule shown: at T+35, HR and RR alone moved, but jaw tone and palpebral were unchanged — one data point, not a composite trend, so the correct move was reassessment, not an immediate vaporizer increase. At T+40, three parameters had moved together (jaw tone tightened, palpebral returned, HR/RR still elevated) — that's the composite trigger, and the vaporizer was increased.

## 2. CRI / dose calculation method (worked, two cases)

**Formula:** mL/hr = (dose in mcg/kg/hr × body weight in kg) ÷ concentration in mcg/mL.

**Case A — dilution required.** Fentanyl, ordered 3 mcg/kg/hr, 32 kg patient, stock 50 mcg/mL.
- Undiluted: 3 × 32 ÷ 50 = 1.92 mL/hr → below the ~2 mL/hr accuracy floor on a standard syringe pump.
- Dilute 1:9 with saline → working concentration 5 mcg/mL.
- Recalculate: 3 × 32 = 96 mcg/hr; 96 ÷ 5 = **19.2 mL/hr**.

**Case B — no dilution needed.** Lidocaine, ordered 50 mcg/kg/min (= 3,000 mcg/kg/hr), 20 kg patient, stock 2% (20,000 mcg/mL).
- 3,000 × 20 = 60,000 mcg/hr; 60,000 ÷ 20,000 = **3 mL/hr** — already inside the pump's accurate range, no dilution step needed.

**Check before programming any pump:** re-derive the rate from the concentration printed on the vial/bag actually in hand — not from the number that "usually" gets used for that drug.

## 3. Periodontal staging and probing-depth decision (AVDC-referenced)

| Stage | Finding | Probing depth (dog / cat) | Typical action |
|---|---|---|---|
| 0 | Clinically normal | ≤3 mm / ≤1 mm, no attachment loss | No treatment |
| 1 | Gingivitis only | ≤3 mm / ≤1 mm, no attachment loss, gingival inflammation | Prophylaxis, home care |
| 2 | Early periodontitis | <25% attachment loss | Prophylaxis + root planing, recheck interval |
| 3 | Moderate periodontitis | 25–50% attachment loss | Root planing or extraction per veterinarian, dental radiograph first |
| 4 | Advanced periodontitis | >50% attachment loss / mobility | Extraction, dental radiograph to confirm extent |

Probing exceeding 3 mm (dog) or 1 mm (cat) at any single site — even in an otherwise Stage 0–1 mouth — gets flagged for a dental radiograph before deciding scale-only vs. extraction; visible calculus above the gumline does not predict subgingival attachment loss.

## 4. Radiographic technique selection (illustrative chart, abdomen, 40 kVp fixed-mAs-style chart)

| Measured thickness at collimated site (cm) | kVp | mAs |
|---|---|---|
| 10 | 70 | 6 |
| 15 | 76 | 6 |
| 20 | 82 | 8 |
| 25 | 88 | 10 |

Measure with calipers at the actual collimated site immediately before exposure — not from a breed/weight lookup. If an image comes back washed out or too dark on the charted setting, the first move is remeasuring thickness at the site, not nudging kVp/mAs by feel; a chart built for average thickness does not hold for a barrel-chested or emaciated individual, and repeat exposures are exactly the dose-creep ALARA principles exist to avoid.

## 5. Pre-anesthetic minimum screen (PCV/TP)

| Species | Normal PCV | Normal TP |
|---|---|---|
| Canine | 37–55% | 5.4–7.7 g/dL |
| Feline | 24–45% | 5.7–7.8 g/dL |

PCV/TP via microhematocrit centrifuge and refractometer is the fastest pre-anesthetic screen available chairside; a PCV/TP outside range on the morning of a procedure gets flagged to the veterinarian before drugs are drawn up, regardless of how the patient looks clinically.
