# Playbook

## Xenon transient timing check (filled example)

Power reduction 100% → 50%, planned hold 4 hours, typical xenon peak 6–10 hours post-reduction for this reactor type.

| Time since reduction | Xenon transient phase | Reactivity implication |
|---|---|---|
| 0–2 hours | Rising, early phase | Xenon burden growing, but still relatively small |
| 4 hours (planned return) | Rising, approaching mid-transient | Xenon burden meaningfully higher than at 0–2 hours, still climbing |
| 6–10 hours | Near peak | Xenon burden at or near maximum — hardest point to overcome via rod withdrawal |
| 10+ hours | Decaying | Xenon burden falling — easier point to return to power |

**Options at the 4-hour decision point:**

| Option | Reactivity implication |
|---|---|
| Return to 100% at 4 hours (as originally planned) | Must overcome a still-rising xenon burden — verify available reactivity/shutdown margin covers this specifically |
| Extend hold to 8+ hours | Passes through the peak; return to power happens on the declining side of the transient, generally easier |
| Return to 100% at 4 hours with explicit margin verification | Acceptable if the shutdown margin/reactivity calculation is confirmed to cover the projected 4-hour xenon burden specifically, not just a general "should be fine" |

## Shutdown margin verification worksheet (filled example)

| Check | Naive approach | Correct approach |
|---|---|---|
| Rod configuration | 47 of 48 control rods fully inserted, 1 rod at 10% withdrawn for power shaping | Same physical configuration |
| Margin assessment (naive) | "47 of 48 rods in — plenty of margin" | Not a valid basis for the shutdown margin determination |
| Margin assessment (correct) | — | Calculate shutdown margin assuming the single most reactive rod (identified by the core's reactivity worth map, not necessarily the one currently withdrawn) fails to insert — compare the resulting negative reactivity against the required minimum margin for this reactor's technical specifications |

**Result:** The naive "most rods are in" observation says nothing about whether the calculated worst-case margin — which specifically assumes the single most reactive rod does NOT insert — actually meets the required minimum. Only the calculation, not the rod-position headcount, answers that question.

## Rod worth curve reference (filled example)

Illustrative single control rod, full travel range 0% (fully in) to 100% (fully out).

| Rod position | Approximate relative worth per unit withdrawal |
|---|---|
| 0–20% (near fully in) | Low — near the bottom of the worth curve |
| 40–60% (mid-range) | High — peak worth region |
| 80–100% (near fully out) | Low — near the top of the worth curve, most worth already extracted |

**Applied check:** Withdrawing a rod by 10% near the 0–20% range and withdrawing the same rod by 10% near the 40–60% mid-range produce meaningfully different reactivity additions — planning a rod move by physical distance alone, without checking the current position against the worth curve, risks under- or over-predicting the resulting reactivity change.
