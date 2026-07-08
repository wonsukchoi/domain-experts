# Playbook

Filled formulas, tables, and scoring worksheets a human factors engineer runs against. Verify the current published edition of each standard before citing — these are the commonly cited formulas and tables, not a substitute for the standard's current text.

## 1. NIOSH Revised Lifting Equation — frequency and coupling multiplier tables

RWL = LC x HM x VM x DM x AM x FM x CM (see SKILL.md worked example for the full computation on one task). LC = 23 kg. The five geometry multipliers (HM, VM, DM, AM) come from measured task geometry; FM and CM come from published lookup tables:

**Frequency multiplier (FM)** — selected values, duration <=1 hour, vertical location V < 75 cm (Waters et al. 1994, Table 5):

| Lifts/min | FM |
|---|---|
| 0.2 | 1.00 |
| 1 | 0.94 |
| 2 | 0.91 |
| 3 | 0.88 |
| 4 | 0.84 |
| 6 | 0.75 |
| 9 | 0.52 |
| 12 | 0.37 |
| 15 | 0.00 (exceeds recommended max frequency at this duration) |

**Coupling multiplier (CM)** (Waters et al. 1994, Table 7):

| Coupling quality | V < 75 cm | V >= 75 cm |
|---|---|---|
| Good (well-fitted handles, or box < 25kg with grip < 40cm below front) | 1.00 | 1.00 |
| Fair (handles present but not optimal, e.g., cut-out or non-molded) | 0.95 | 1.00 |
| Poor (no handles, awkward grip, sharp edges) | 0.90 | 0.90 |

**Rule:** LI = actual weight / RWL. LI < 1.0 = no lifting-specific action; 1.0-3.0 = moderate-to-high risk, redesign priority; > 3.0 = high risk, immediate redesign. For a multi-task job, compute a Composite Lifting Index (CLI) — do not average single-task LIs; CLI weights by frequency and adds each task's incremental contribution in descending order of individual LI.

## 2. RULA (Rapid Upper Limb Assessment) — scoring worksheet

Score posture in two groups, add a muscle-use and force/load score, then look up the grand score in the action table.

| Group A (arm/wrist) | Score input | Group B (neck/trunk/legs) | Score input |
|---|---|---|---|
| Upper arm position | 20-45deg flexion = 2 | Neck position | 0-10deg flexion = 1 |
| Lower arm position | 60-100deg = 1 | Trunk position | 0deg (upright, supported) = 1 |
| Wrist position | 0-15deg deviation = 2 | Legs | bilateral weight-bearing = 1 |
| Wrist twist | mid-range = 1 | — | — |
| + Muscle use (static >1 min or repeated >4x/min) | +1 | + Muscle use | +1 |
| + Force/load (2-10kg intermittent) | +1 | + Force/load | +1 |

Example: Group A posture score 5, +1 muscle, +1 force = **7**. Group B posture score 3, +1 muscle, +1 force = **5**. Grand score from the RULA table (Group A x Group B lookup) = **6**.

**Action levels:** 1-2 acceptable · 3-4 investigate further, change may be needed soon · 5-6 investigate soon, change soon · 7+ investigate and change immediately.

## 3. REBA (Rapid Entire Body Assessment) — scoring worksheet

Same structure as RULA but covers whole-body posture including trunk, neck, legs (Group A) and arm/wrist (Group B), plus a separate coupling score and an activity score.

**Action levels (Hignett & McAtamney 2000):** 1 negligible, no action · 2-3 low risk, may be needed · 4-7 medium risk, further investigation, change soon · 8-10 high risk, investigate and implement change soon · 11-15 very high risk, implement change now.

**Rule:** a REBA score of 8+ or a RULA score of 7+ both land in the same operational band — redesign now, not at the next scheduled review.

## 4. ANSI/HFES 100-2007 workstation anthropometry — selected percentile values (US civilian adult population)

| Dimension | 5th %ile female | 50th %ile | 95th %ile male |
|---|---|---|---|
| Standing eye height | 142.8 cm | 158.8 cm | 179.1 cm |
| Sitting elbow height (seat to elbow) | 18.1 cm | 23.3 cm | 29.5 cm |
| Forward functional reach (seated) | 60.5 cm | 71.6 cm | 82.5 cm |
| Seated popliteal height | 35.0 cm | 41.0 cm | 47.5 cm |
| Hip breadth (seated) | 31.2 cm | 36.4 cm | 43.7 cm |

**Application rule:** size a clearance/knee-space/aisle-width dimension to the 95th-percentile-male value (fits the largest user); size a reach/control-distance dimension to the 5th-percentile-female value (fits the smallest user). A single workstation adjustable across this full range (e.g., seat height 35.0-47.5 cm) accommodates both without forcing a design compromise on either dimension.

## 5. Fitts's Law — index of difficulty worked example

ID = log2(2D/W), where D = distance to target center, W = target width along the movement axis. Movement time MT = a + b x ID (a, b fit empirically per device/study; typical mouse-pointing constants a ≈ 0.1s, b ≈ 0.1s/bit are commonly cited starting values, not universal).

| Scenario | D | W | ID = log2(2D/W) | Effect of the change |
|---|---|---|---|---|
| Baseline button | 400px | 40px | log2(800/40) = log2(20) = **4.32 bits** | — |
| Double the width | 400px | 80px | log2(800/80) = log2(10) = **3.32 bits** | ID drops 1.0 bit |
| Halve the distance | 200px | 40px | log2(400/40) = log2(10) = **3.32 bits** | ID drops 1.0 bit — same gain as doubling width |
| Halve distance AND keep width | 200px | 40px vs baseline 400px/40px | — | Reducing distance is free (layout change); doubling width costs 2x the screen area |

**Rule:** distance and width contribute equally inside the log — when both a layout change and a size change achieve the same ID reduction, the layout change is usually cheaper.

## 6. System Usability Scale (SUS) — scoring worksheet

10 items, alternating positive/negative phrasing, 5-point Likert (1=strongly disagree, 5=strongly agree). Score conversion: for odd items (positively worded), score = response - 1; for even items (negatively worded), score = 5 - response. Sum all 10 converted scores (range 0-40), multiply by 2.5 for a 0-100 SUS score.

Example: a participant scores items 1,3,5,7,9 (positive) at 4,4,3,5,4 -> converted 3,3,2,4,3 = 15. Items 2,4,6,8,10 (negative) at 2,2,3,1,2 -> converted 3,3,2,4,3 = 15. Sum = 30. SUS = 30 x 2.5 = **75**.

**Benchmark (Sauro 2011, aggregate industry norms):** mean SUS ~68; scores >80.3 grade "A" (top 10%); 68 is the average, not a pass threshold — pair with task completion rate and error count from the same session before concluding a design is fine.

## 7. NASA Task Load Index (TLX) — subjective workload

Six subscales (Mental Demand, Physical Demand, Temporal Demand, Performance, Effort, Frustration), each rated 0-100, combined via pairwise-comparison weighting (or unweighted "Raw TLX" average for a faster field version). A Raw TLX above ~55-60 on a 100-point scale is commonly treated as a flag for workload-reduction review on sustained-attention or multitasking tasks — a stated heuristic, not a NASA-published cutoff.
