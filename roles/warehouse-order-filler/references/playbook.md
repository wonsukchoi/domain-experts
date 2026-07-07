# Playbook

Filled procedures a stocker/order filler or lead actually runs, with real numbers plugged in.

## 1. NIOSH lifting-index check

**Formula:**

```
RWL (lb) = 51 × HM × VM × DM × AM × FM × CM
LI        = Load weight ÷ RWL
```

Where 51 lb is the load constant (a healthy adult under ideal conditions), and each multiplier (0–1) penalizes a departure from ideal: **HM** horizontal distance from body, **VM** vertical origin height (ideal ≈ 30 in / 75 cm off the floor — the basis for "golden zone" placement), **DM** vertical travel distance, **AM** asymmetry/twist angle, **FM** lift frequency, **CM** coupling/grip quality.

**Worked table — same 35 lb case, three pick scenarios:**

| Scenario | HM | VM | DM | AM | FM | CM | RWL | LI (35 lb load) | Risk |
|---|---|---|---|---|---|---|---|---|---|
| Golden-zone pick, no twist, low frequency | 0.95 | 0.98 | 0.97 | 1.0 | 0.94 | 1.0 | 40.7 lb | 0.86 | Under 1.0 — acceptable |
| Bottom-shelf pick, 45° twist to place on cart | 0.90 | 0.78 | 0.91 | 0.86 | 0.94 | 1.0 | 22.7 lb | 1.54 | Elevated — redesign or aid |
| Bottom-shelf, twisted, high frequency (>4/min) | 0.90 | 0.78 | 0.91 | 0.86 | 0.72 | 1.0 | 17.4 lb | 2.01 | Elevated — mechanical aid required |

**Field procedure:**

1. Weigh or look up the item's case weight.
2. Estimate the six multipliers from the task geometry (use facility ergonomics job-aid tables, not guesswork on the frequency and asymmetry factors — those move the RWL the most).
3. Compute RWL, then LI = load ÷ RWL.
4. LI ≤ 1.0: proceed as a normal manual lift. LI 1.0–3.0: use a mechanical aid, split the load, or get a second person before proceeding. LI > 3.0: do not lift manually — task requires an aid or redesign regardless of how the first rep felt.
5. Log any location where LI repeatedly comes in above 1.0 as a slotting exception — a location problem, not an individual-conditioning problem.

## 2. ABC/velocity slotting reference

**Standard split** (Frazelle, *World-Class Warehousing*): rank SKUs by pick frequency (lines/period), then bucket:

| Class | % of SKUs | % of total picks (typical) | Slot placement |
|---|---|---|---|
| A | ~20% | ~70–80% | Golden zone (waist–shoulder), closest to pack/ship |
| B | ~30% | ~15–20% | Mid-accessibility, adjacent zones |
| C | ~50% | ~5–10% | Bulk/reserve, bottom or top shelf, farther zones |

**Re-slot trigger checklist** (run monthly or after a seasonal demand shift):

1. Pull trailing 30–60 day pick-frequency report by SKU.
2. Flag any SKU that moved class (C→A especially) since the last re-slot.
3. Cross-check current physical slot against golden-zone/adjacency rule for its new class.
4. Reslot any A-class SKU found below knee or above shoulder height before the next peak volume period, not after.

## 3. Pick-path sequencing vs. bin-number order

**Example — 40-line batch across 4 zones, same order:**

| Sequencing method | Total travel distance | Delta |
|---|---|---|
| WMS zone-batched serpentine path | 620 ft | baseline |
| Worked in raw bin-number order | 890 ft | +270 ft (+44%) |

At an average pick-floor walking pace of ~250 ft/min, the 270 ft difference costs about 1 extra minute per 40-line batch — the real cost compounds across every batch in a shift, not any single one. Follow the WMS-generated sequence; only break it for a flagged rush/hot order, and re-sequence the remaining lines afterward rather than reverting to bin-number order for the rest of the batch.

## 4. FEFO pull procedure (dated/perishable SKUs)

1. Identify all lots present at the pick location and their code dates (best-by/sell-by), not just the physically front-most case.
2. Sort mentally (or via handheld lookup if the WMS supports lot-level scan) by soonest-expiring first.
3. Pull the full quantity from the soonest lot before touching the next lot, splitting across lots only when one lot's remaining quantity is insufficient.
4. If the WMS pick task doesn't carry lot-level guidance, log it as a lot-tracking gap rather than defaulting to shelf position — this is a system limitation to escalate, not a picker judgment call to improvise around.
5. Never pull a lot past its facility-set pull date (commonly set several days before the printed best-by/sell-by to allow shelf life at the receiving end) even if it's the only lot present — flag to lead for disposition instead.

## 5. Rate-vs-accuracy self-check

| Signal | Action |
|---|---|
| Current pace ≥ target, accuracy at or above facility floor (e.g., 99.5%) | Continue as-is |
| Current pace below target, accuracy at floor | Flag pace gap to lead as a staffing/slotting issue; do not cut confirmation steps to close the gap |
| Current pace at or above target, accuracy trending below floor over rolling week | Slow down to the pace that holds the floor; report the trend, don't wait for a QA audit to catch it |
| Scan/voice override rate rising for reasons other than hardware fault | Treat as a leading indicator — investigate before it shows up as a shipped error |
