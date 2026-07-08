# Playbook

Filled formulas, thresholds, and workflows a manufacturing engineer runs against. Verify against the specific customer's PPAP/control-plan requirements and the governing ASME/AIAG edition in force — these are commonly applied industry conventions, not a substitute for a contract-specific requirement.

## 1. Process capability — Cpk and Ppk

**Cpk = min[(USL − X̄)/3σ_within, (X̄ − LSL)/3σ_within]** — uses within-subgroup variation (σ_within = R̄/d2), assumes the process is in statistical control.

**Ppk = min[(USL − X̄)/3σ_overall, (X̄ − LSL)/3σ_overall]** — uses overall (total) sample standard deviation, no in-control assumption; the correct index for an initial/short-run study (PPAP) before long-term control data exists.

| Study type | Index | Commonly cited threshold |
|---|---|---|
| Initial process study (PPAP submission) | Ppk | ≥ 1.67 |
| Ongoing production capability | Cpk | ≥ 1.33 |
| Ongoing, non-critical characteristic | Cpk | ≥ 1.00 (site/customer-specific) |

*Example: USL = 1.253 in, LSL = 1.250 in, X̄ = 1.2515 in, σ_within = 0.0006 in → Cpk = min[(1.253−1.2515)/0.0018, (1.2515−1.250)/0.0018] = min[0.833, 0.833] = **0.833**. After a fixturing fix drops σ_within to 0.0003 in with the same centered mean → Cpk = 0.0015/0.0009 = **1.667**.*

**Rule:** never compute Cpk from a control chart showing an out-of-control point, a run of 7+ points on one side of center, or a trend — stabilize the process first (root-cause and re-chart), then compute the index. A capability index from an unstable process is not diagnostic of anything.

## 2. GD&T — MMC, virtual condition, bonus tolerance

For a hole with a position tolerance called out **at MMC**:

**Virtual condition (VC) = MMC size − position tolerance** (hole feature; MMC of a hole is its smallest permitted diameter).
**Bonus tolerance available = actual produced size − MMC size** (grows as the hole departs from MMC toward LMC).
**Total position tolerance at a given produced size = basic position tolerance + bonus tolerance.**

| Term | Value in worked example (Ø0.375 hole, ⌀0.008 position at MMC) |
|---|---|
| MMC (smallest permitted hole) | 0.375 |
| Position tolerance (basic) | 0.008 |
| Virtual condition | 0.375 − 0.008 = **0.367** |
| Functional locator clearance (stated shop heuristic) | 0.0005 |
| Locating pin diameter | 0.367 − 0.0005 = 0.3665 → **Ø0.366** (standard undersize dowel) |
| If produced hole measures Ø0.3765 (0.0015 over MMC) | Bonus tolerance = 0.0015; total position tolerance available = 0.008 + 0.0015 = **0.0095** |

**Rule:** a locating pin is sized to virtual condition minus running clearance, never to the hole's nominal or basic dimension — sizing to nominal either jams on a worst-case part or under-locates a part that's using its full bonus tolerance, reintroducing the position error the fixture exists to remove.

## 3. Fixture locating — 3-2-1 principle

| Datum | Degrees of freedom removed | Locator type (typical) |
|---|---|---|
| Primary (A) | 3 (one translation + two rotations) | 3 locating buttons/pads on the largest functional flat |
| Secondary (B) | 2 (one translation + one rotation) | 1 pin sized to virtual condition in a functional hole |
| Tertiary (C) | 1 (remaining translation) | 1 edge or diamond-pin locator |

**Rule:** the locating scheme follows the print's datum reference frame in its stated precedence (A, then B, then C) — locating on a non-datum surface because it clamps more conveniently produces a part that reads in tolerance on the fixture but doesn't locate correctly against the datums the assembly or downstream process actually uses.

## 4. Tolerance stack-up — worst-case vs. RSS

**Worst-case: T_stack = Σ|T_i|** (sum of all contributor tolerances — guarantees fit at 100% of the population, no assumption about distribution).

**RSS (statistical): T_stack = √(Σ T_i²)** (root-sum-square — assumes each contributor is normally distributed and centered, and is only valid when every contributor has demonstrated capability, commonly Cpk ≥ 1.33).

*Example, 4-part stack with individual tolerances 0.002, 0.003, 0.0015, 0.002:*
*Worst-case: 0.002 + 0.003 + 0.0015 + 0.002 = **0.0085**.*
*RSS: √(0.002² + 0.003² + 0.0015² + 0.002²) = √(0.000004 + 0.000009 + 0.00000225 + 0.000004) = √0.00001925 = **0.00439**.*

**Rule:** RSS gives roughly half the stack-up of worst-case in this example — a real cost/tolerance win, but only defensible when every contributor's capability data supports it. Default to worst-case for safety-critical or low-volume assemblies where a single field failure isn't acceptable.

## 5. GR&R (Gauge Repeatability & Reproducibility) acceptance

| %Contribution (or %Study Variation, per AIAG MSA) | Acceptability |
|---|---|
| < 10% | Acceptable measurement system |
| 10–30% | Marginal — acceptable depending on application, cost, or criticality |
| > 30% | Unacceptable — requalify gauge/method before trusting capability data from it |

**Rule:** run GR&R before capability, not after a marginal Cpk shows up — a Cpk computed with a >30%-contribution gauge is measuring the gauge's noise, and process changes made in response to it will not move the number.

## 6. PFMEA — severity/occurrence/detection and action priority

| Severity | Occurrence | Detection |
|---|---|---|
| 9–10: hazard without/with warning (safety, regulatory) | 8–10: very high — failure almost inevitable | 8–10: very remote to remote chance of detection |
| 7–8: loss of primary function | 5–7: moderate — occasional failures | 5–7: low to moderate detection chance |
| 4–6: degraded function, customer dissatisfaction | 2–4: low — relatively few failures | 2–4: high detection chance |
| 1–3: minor, no noticeable effect | 1: failure unlikely | 1: almost certain detection |

**RPN = Severity × Occurrence × Detection** (1–1000). AIAG-VDA action priority (AP: High/Medium/Low) supersedes raw RPN ranking — a Severity 9–10 item is **High** action priority regardless of RPN.

*Example: Severity 9 (bore failure causes press-fit bushing to loosen in service), Occurrence 3, Detection 5 → RPN = 135 — a mid-range RPN that a pure RPN-threshold gate (commonly set around 100–120) might pass, but AIAG-VDA's severity-first AP table flags this **High** priority on severity alone and requires an action regardless.*

## 7. OEE — availability × performance × quality

**Availability = Run Time / Planned Production Time.**
**Performance = (Ideal Cycle Time × Total Count) / Run Time.**
**Quality = Good Count / Total Count.**
**OEE = Availability × Performance × Quality.**

| Loss category | Typical causes | Who typically fixes it |
|---|---|---|
| Availability | Changeover, breakdown, starved/blocked upstream/downstream | Maintenance, scheduling |
| Performance | Micro-stops, reduced speed, minor jams | Manufacturing engineering (fixturing, tooling, process) |
| Quality | Scrap, rework, startup rejects | Manufacturing engineering (process capability), quality |

*Example: Planned time 2,400 min, run time 2,040 min → Availability = 0.85. Ideal cycle 4.0 min, 450 parts in 2,040 min → Performance = (4.0×450)/2,040 = 0.882. 423 good of 450 → Quality = 0.940. OEE = 0.85×0.882×0.940 = **0.705** (70.5%).*

**Rule:** decompose before proposing a fix — a low Performance factor with healthy Availability means a speed/micro-stop problem that adding a second machine won't solve; a low Quality factor means a capability problem, not a capacity problem. World-class OEE benchmark commonly cited: 85%; this is a stated industry heuristic, not a universal requirement — compare against the site's own baseline and schedule need first.
