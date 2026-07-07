# Playbook

Filled worksheets for the three recurring planning problems: grade-adjusted brake-point planning for a non-standard consist, slack-action sequencing at a throttle/brake transition, and Hours of Service scheduling. Numbers below are the cited regulatory thresholds and stated industry conventions, not a substitute for a carrier's approved train-handling instructions or a specific locomotive's braking curve — those always control over this worksheet.

## 1. Grade-adjusted brake-point recompute

**Method, in order:**
1. Compute bare stopping distance from the operating speed on level track using a stated deceleration rate for the equipment (v² ÷ 2a), then adjust for grade by subtracting (descending) or adding (ascending) g × grade-fraction from the deceleration term.
2. Compute the brake pipe propagation lag distance: (train length in feet ÷ ~900 ft/sec) × operating speed in ft/sec. This is the extra distance covered before the rear of the train is actually braking.
3. Apply the carrier's operating margin convention to (stopping distance + lag) — commonly a doubling, to leave room for a graduated second reduction and a partial recharge [heuristic — carrier-specific].
4. Compare the result against any fixed lineside brake-point landmark; if the landmark was sized for a shorter or lighter reference train, treat the difference as lost margin, not as slack to spend.

**Worked example — two consists against the same MP 203.9 card (1 mile / 5,280 ft before an absolute signal), 50 mph, 1% descending grade:**

| Quantity | Reference train (card basis) | Today's train |
|---|---|---|
| Length | 3,700 ft | 7,392 ft |
| Grade-adjusted stopping distance | 1,696 ft | 1,696 ft (same speed/grade) |
| Propagation lag distance | 301 ft | 602 ft |
| Required distance (2x margin convention) | 2 × 1,997 ≈ 3,994 ft | 2 × 2,298 ≈ 4,596 ft |
| Cushion at the 5,280 ft card location | 5,280 − 3,994 = 1,286 ft | 5,280 − 4,596 = 684 ft |

**Decision rule:** if the recomputed cushion at a fixed card location drops by more than roughly a third from the reference-train cushion, move the first minimum reduction earlier by the shortfall distance rather than accepting the card location as-is. Here, restoring the reference train's 1,286 ft cushion requires starting ~602 ft (about 0.11 mi) earlier than the card — in practice rounded to a clear landmark, e.g., a fifth of a mile.

## 2. Slack-action sequencing at a throttle/brake transition

**Free slack accumulation:** standard freight coupler free slack is commonly cited at roughly 3/4 inch per coupling. For a 140-car train (139 couplings between cars), total potential free slack the train can run in or run out is 139 × 0.75 in ≈ 104 in ≈ 8.7 ft.

**Why the distance matters more than it sounds:** 8.7 ft of accumulated slack closing over a couple of seconds during an abrupt throttle-to-brake transition on a sag represents a real relative-velocity change concentrated at each coupling — enough to produce buff (compression) or draft (tension) forces well beyond what the same net speed change would produce if the slack were kept extended throughout [heuristic — exact force magnitude depends on car weight distribution and is not asserted here; the qualitative risk and the distance figure are the actionable parts].

**Sequencing rule of thumb:**
- **Descending into a sag (grade flattens or reverses) with slack stretched:** maintain a light brake application or sustained throttle through the transition rather than releasing fully, so the train doesn't shift from stretched to bunched in one uncontrolled step.
- **Cresting a hill onto a descending grade under power:** begin the first minimum reduction before or at the crest, not after the train starts to accelerate on the downgrade, so the transition from throttle to brake happens while slack is still extended rather than after it has already begun to bunch.
- **After any application, before making a second reduction:** confirm brake pipe pressure has had time to stabilize (recharge is not instantaneous); stacking reductions before the pipe restabilizes reduces the reserve available for a subsequent adjustment.

## 3. Hours of Service scheduling

**Governing limits (49 U.S.C. § 21103):** 12-hour maximum on-duty period for a train employee; minimum 10 consecutive hours of undisturbed off-duty rest required afterward before returning to duty. An interim release at an away-from-home terminal that is interrupted or shorter than the carrier's qualifying threshold does not satisfy the rest requirement and the off-duty clock restarts from the actual, undisturbed release.

**Worked example.** An engineer reports for duty at 06:00. Under the 12-hour limit, the engineer must be relieved from duty no later than 18:00 regardless of how much of the trip remains. If relief and release occur exactly at 18:00 with no interim calls, the minimum 10-hour rest period runs 18:00–04:00, making 04:00 the earliest legal next on-duty time. If the engineer is called back at 02:00 for a "quick" assignment two hours before the 10-hour rest period would otherwise complete, that call interrupts the rest period — under the Act's undisturbed-rest requirement, the clock does not simply resume at the interruption; the carrier owes a fresh qualifying rest period before the engineer can be used again, not credit for the hours already elapsed.

**Decision rule:** raise a rest-period risk to the dispatcher as soon as the remaining trip distance and current speed profile suggest the 12-hour mark will be reached before the terminal, not when the mark is imminent — a relief point identified with hours of notice is a routine crew change; one identified with minutes of notice is a stopped train blocking a main track.
