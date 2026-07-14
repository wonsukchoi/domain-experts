# Derrick operator playbook

Filled procedures for the three recurring calculations: trip-tank displacement checks, barite weight-up, and setback-capacity tracking.

## 1. Trip-tank displacement check (per-stand kick/swab monitor)

**Setup.** Before pulling the first stand, record: pipe OD/weight in the hole, closed-end displacement (bbl/ft) from a displacement/capacity table, and stand length. Zero the trip tank.

| Pipe | Displacement (closed-end, bbl/ft) | Stand length | Calculated fill/stand |
|---|---|---|---|
| 5 in., 19.5 lb/ft DP | 0.0075 | 92 ft (triple) | 0.69 bbl |
| 4.5 in., 16.6 lb/ft DP | 0.0061 | 92 ft (triple) | 0.56 bbl |
| 6.625 in. drill collar | 0.0230 | 31 ft (single) | 0.71 bbl |

**Per-stand log (example, from the SKILL.md worked trip):**

| Stand # | Calculated fill (bbl) | Actual fill (bbl) | Cumulative deficit (bbl) | Deficit % |
|---|---|---|---|---|
| 47 | 0.69 | 0.51 | 0.18 | 26% |
| 48 | 0.69 | 0.50 | 0.37 | 27% |
| 49 | 0.69 | 0.53 | 0.53 | 26% |
| 50 | 0.69 | 0.50 | 0.72 | 26% |
| 51 | 0.69 | 0.51 | 0.90 | 26% |

**Trigger rule:** one stand outside ±15% of calculated fill — note it, keep pulling. Two or more consecutive stands outside that band, with the deficit compounding rather than alternating over/under — stop the trip and run a flow check before the next stand. A cumulative deficit that stays a roughly constant percentage stand over stand (as above) is the swab signature; a deficit that appears once and self-corrects the next stand is gauge noise.

**Flow check (once stopped):** pick up off bottom to a fixed reference point, shut down pumps, observe the flow line for continued flow with no pumps running. Flowing with pumps off confirms the well is unloading and the crew moves to a shut-in per the rig's well control procedure; static confirms the earlier deficit was volumetric (e.g., a hole-cleaning or ballooning effect) rather than an influx, and the trip resumes with tightened monitoring.

## 2. Barite weight-up (sacks required)

**Mass-balance derivation.** Barite specific gravity ≈ 4.2, i.e. ≈ 35 lb/gal. A 100-lb sack of barite added to mud volume V (bbl) at starting weight W1 (ppg) to reach target weight W2 (ppg) both adds mass and adds volume (mass ÷ 35 lb/gal ÷ 42 gal/bbl). Balancing mass before and after gives:

**Sacks required, n = 14.7 × V × (W2 − W1) / (35 − W2)**

(V in bbl, W1/W2 in ppg, 35 = assumed barite lb/gal at SG 4.2, 100-lb sacks.)

**Worked example.** Active system V = 500 bbl, current weight W1 = 9.6 ppg, program calls for W2 = 10.5 ppg:

n = 14.7 × 500 × (10.5 − 9.6) / (35 − 10.5) = 14.7 × 500 × 0.9 / 24.5 = 6,615 / 24.5 ≈ **270 sacks**

Check the result against the mud balance after mixing — target weight confirmed by measurement, not by sack count, since real barite density and system losses during mixing vary from the assumed 35 lb/gal.

**Sequencing fallback (in preference order):**
1. Add barite through the hopper at a controlled rate while circulating, checking weight every 15–20 minutes against the calculated curve toward W2.
2. If weight isn't tracking the calculation (e.g., running consistently light after the calculated sack count is in), suspect hopper losses or an inaccurate starting-volume figure before adding sacks beyond the calculated number — recount system volume first.
3. If time doesn't allow full circulation before the next trip, weight up the active pits only and flag the un-weighted volume explicitly to the incoming crew and mud engineer — never assume a partial treatment brought the whole system to program weight.

## 3. Setback capacity tracking

**Setup.** Confirm the derrick/substructure rated setback capacity (stands and/or total weight) from the rig's equipment documentation before the well is spudded — this is a structural rating, not a rule of thumb to re-derive on the fly.

**[Stated heuristic — figures below are illustrative rig-class ranges, not a substitute for the specific rig's rated documentation; verify against that document before applying the 90% trigger.]**

| Rig class | Typical rated setback (stands) | Action threshold |
|---|---|---|
| Triple, land rig, moderate depth | ~90 stands | Plan a short trip or bit change by stand 80 (≈90% of rating) |
| Triple, deep/high-spec land rig | ~120 stands | Plan by stand 105 (≈90% of rating) |

**Rule:** track racked-stand count against the rated number on the trip sheet in real time. At ~90% of rated capacity, flag to the driller that the next reasonable stopping point (bit trip, casing point, or connection) should be treated as the trip point — do not rack past the rated number to avoid an unplanned trip; the rating doesn't have margin built in for "it's held more before."
