# Playbook

Filled calculations and templates a stucco crew actually runs, not descriptions of them.

## 1. Control-joint layout (worked, 45 ft × 20 ft wall, wood-frame three-coat)

**Rule set (ASTM C1063):** no panel exceeds ~150 sq ft; no single dimension exceeds 18 ft; length-to-width aspect ratio does not exceed 2.5:1.

**Step 1 — check overall wall against the 18-ft dimension cap.** Wall is 45 ft × 20 ft. Height (20 ft) exceeds 18 ft, so a horizontal control joint is required regardless of area math. Split at 10 ft (often set at a floor line, which also breaks framing shrinkage differences between stories).

**Step 2 — set panel length from the 150-sq-ft cap at the chosen row height.** Row height = 10 ft. Max panel length = 150 sq ft ÷ 10 ft = 15 ft (also inside the 18-ft cap).

**Step 3 — panel count.** 45 ft ÷ 15 ft = 3 panels per row. 2 rows × 3 panels = 6 panels total.

**Step 4 — reconcile to total wall area.** 6 panels × (15 ft × 10 ft = 150 sq ft) = 900 sq ft. Matches 45 ft × 20 ft = 900 sq ft exactly — no leftover sliver panel forcing an oversized edge panel.

**Step 5 — aspect ratio check.** Each panel is 15 ft × 10 ft → ratio 1.5:1, inside the 2.5:1 maximum.

**Common layout mistake to check for:** dividing a wall's length evenly without re-checking the area/aspect-ratio math at the chosen row height — a wall divided into 20-ft-wide panels at a 10-ft row height gives 200 sq ft panels, which clears the 18-ft single-dimension cap but blows past the 150-sq-ft area cap. Both caps have to clear at once, not just the one that's easiest to eyeball.

## 2. Coat cure-time schedule (ASTM C926, worked)

| Step | Minimum elapsed time | Adjustment |
|---|---|---|
| Scratch coat → brown coat | 48 hours, moist-cured | Extend if daytime temps are below ~50°F (hydration slows) |
| Brown coat → finish coat | 7 days | Extend further if RH < 30%, wind > 10 mph, or direct sun exposure is drying the coat faster than normal — add supplemental fogging 2×/day rather than shortening the calendar days |
| Finish coat → paint/sealer | 28 days (paint-manufacturer guidance, not an ASTM minimum — stated heuristic) | Longer in cool/damp climates; verify with the specific coating manufacturer's data sheet |

**Worked schedule (hot, dry, windy week — mid-70s°F, 25% RH, 12 mph afternoon wind):**

```
Day 1:      Scratch coat applied. Moist-cure (damp burlap or light misting) for first 24 hrs.
Day 3:      Brown coat applied (48-hr minimum met). Begin supplemental fog-misting
            2x/day given low RH/wind — normal humidity would not need this step.
Day 9:      Finish coat applied (7-day minimum off brown coat met; not compressed
            despite drying conditions, because those conditions argue for MORE
            cure attention, not less).
Day 37:     Earliest recommended paint/sealer date (28 days after finish coat).
```

**Reconciliation against a compressed ask:** if a GC requests scratch/brown/finish inside 3 total days, that schedule is short of the code-minimum brown-to-finish step by 7 − 3 = 4 days minimum, and by 6 days once the wind/humidity adjustment above is applied (finish coat pushed to day 9 instead of day 7). State the gap in days, not in general terms ("it needs more time").

## 3. WRB and lath detail checklist (wood-frame substrate)

| Item | Requirement | Fails if |
|---|---|---|
| Water-resistive barrier | Two full layers of approved WRB (or one layer plus a separate approved drainage layer) over wood-based sheathing | Single layer, or two layers installed without the intended drainage gap/lap sequence between them |
| Flashing at openings and penetrations | Continuous, lapped shingle-fashion (upper layers over lower) into the WRB plane before lath | Any penetration flashed after lath/scratch coat instead of integrated into the WRB sequence |
| Lath type | Expanded metal (diamond mesh) self-furring or woven wire, per spec | Flat (non-furred) lath used where self-furring was specified, leaving no key gap for scratch coat to grip |
| Lath fastener spacing | Fasteners at intervals not exceeding 6 in along each framing member, penetrating into solid framing (per ASTM C1063) | Fasteners only into sheathing, missed framing, or spaced wider than 6 in |
| Lath laps | Minimum 1 in side lap, 1 in end lap (2 in at butt joints per manufacturer spec) | Butted lath with no overlap, leaving an unreinforced seam |
| Weep screed | Minimum 4 in above earth / 2 in above paved surfaces, continuous around the base | Screed buried by finish grade or paving added after install without re-checking clearance |

## 4. Weep-screed clearance table

| Adjacent surface | Minimum clearance from screed to surface | Worked check |
|---|---|---|
| Bare earth/soil | 4 in | Grade at 0 in, screed set at 4 in above — passes |
| Paved surface (patio, walkway, driveway) | 2 in | Patio poured to within 1 in of screed — **fails**, needs 1 additional in of clearance or a supplemental flashing/drip detail added before scratch coat |

**Fix sequence when clearance fails after lath is already installed:** do not simply plaster over the shortfall. Add a secondary counter-flashing or drip detail at the base that re-establishes a drainage gap above the paved surface, photograph the correction, and note it in the job file before scratch coat proceeds — the alternative is a hidden moisture path that surfaces as staining or rot years after the crew has left the site.
