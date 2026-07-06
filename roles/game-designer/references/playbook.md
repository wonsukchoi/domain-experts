# Playbook

Filled operational patterns for the level-batch pipeline, monetization-architecture pass, and the near-fail IAP offer. Adapt the numbers to the studio's actual cadence and player base; the structure and thresholds are the reusable part.

## 1. Level-batch pipeline (biweekly cadence, 60 levels/batch)

Standing pipeline for a live-ops match-3/puzzle title shipping levels 141–200 as one batch, days 1–14 of a two-week sprint. Slippage past day 12 (live-ops-lead sign-off) means the batch ships without the polish pass, not late — the ship date doesn't move.

| Day | Stage | Owner | Gate to advance |
|---|---|---|---|
| 1–2 | Spec: written design doc per level (win threshold, move/time cap, mechanic mix, target attempts-to-clear for the mid-skill cohort) | Designer | Every level has a numeric target before anyone opens the editor |
| 3–8 | Build in level editor against the spec | Designer + tools | Level loads, is completable in QA's manual playthrough, matches the spec's mechanic list |
| 9–10 | Internal playtest (min. 8 players, mixed skill) | Design + QA | Median attempts-to-clear within ±30% of spec target, or the level is flagged for retune before the live-ops-lead review, not after |
| 11–12 | Live-ops-lead review & polish pass (live-ops lead, art, audio) | Designer | Sign-off logged per level; unresolved flags block that level only, not the batch |
| 13 | Cert / submission QA (store compliance: odds disclosure present on any randomized offer, age-rating text matches content) | QA | 0 open compliance flags |
| 14 | Ship to production | Live-ops | — |
| 14+ (next cycle) | Post-launch statistical review: 14-day cohort pull per level (attempts-to-clear, D7 by pass/fail segment, offer conversion) | Designer | Any level >2 points below batch-average D7 gets a tuning memo (see Worked example in SKILL.md) before the next batch ships |

**Fallback positions, in order, when day 12 sign-off is missed for a level:**
1. Ship with the polish pass deferred to a hotfix inside the same 14-day window — preferred; players see the level on schedule.
2. Pull the level from this batch, ship the batch at 59 levels, slot it first in the next batch — used when the flag is a data/compliance issue, not cosmetic.
3. Ship as-is with the flag logged — only for cosmetic-only flags (VFX polish, audio mix), never for an open compliance or completability flag.

## 2. Want-chain / pressure-mapping exercise

Run once per core-loop or economy design pass (new game, new season system, major monetization rework) — not per level. Output feeds the level-batch spec (stage 1 above) so IAP hooks are built into the loop rather than patched onto a finished one.

**Format:** for each core player want, chain it to the underlying need, tag the pressure type, then map to the mechanic and monetization hook it justifies.

| Want ("I want X") | So that (Y) | Underlying need (Z) | Pressure tag | Mechanic serving it | Monetization hook |
|---|---|---|---|---|---|
| Keep my daily streak alive | I don't lose the multiplier I've built up | Loss aversion | Time-pressure | Lives system, 30-min regen | Life refill, $1.99 or 50 soft currency |
| Beat my friend's weekly score | I feel skilled relative to someone who matters to me | Social status | Social-pressure | Friends leaderboard, weekly reset | Score-boosting booster, $2.99 |
| Clear this level before my train ride ends | I don't want an unfinished task nagging at me | Closure / time-pressure | Time-pressure | Session-length-aware near-fail offer (below) | "+5 moves," $0.99 |
| Unlock the next chapter's story beat | I'm invested in the narrative, not just the mechanic | Narrative curiosity | None (no pressure tag — flag as non-monetizable) | Star-gate progression | None — this want justifies content pacing, not a purchase; forcing an IAP here reads as narrative ransom and tests badly |
| Show off my board to teammates in the group chat | I get social validation off-platform | Social status | Social-pressure | Shareable end-of-level card | Cosmetic board skin, $3.99 |

**Reading the table:** a want with no pressure tag (row 4) is a signal to leave it alone — it's real player motivation but not a monetization lever, and bolting a paywall onto it (e.g., paying to skip a story beat) converts a retention driver into a churn driver. Only time-pressure and social-pressure rows are candidates for a paid mechanic; ego/status wants without an audience (nobody to show off to) don't sustain a monetization loop either.

**Step sequence:**
1. List 8–15 wants from player research (win/loss interviews, support tickets, review mining) — not brainstormed from the design team's assumptions.
2. Chain each to its underlying need; discard duplicates (two wants chaining to the same need get merged).
3. Tag pressure type. No tag = park it; don't force a hook.
4. For each tagged want, name the specific mechanic and the specific monetization hook — "a booster" is not specific enough; "score-boosting booster, shown post-fail, $2.99" is.
5. Before finalizing the core loop, check that every planned IAP traces to a row in this table. An IAP with no want-chain row is the "bolted on after" failure mode from SKILL.md's first-principles core.

## 3. Near-fail IAP offer — filled design pattern

The "buy more moves" (or "buy more time") offer, the genre's most reliable purchase-intent moment, built correctly.

**Trigger condition:** board state ends with the score gap to the win threshold ≤ 12% of that threshold, or ≤ 2 moves remaining on a move-capped level (whichever the level type uses). Below this band the offer reads as a genuine near-miss; above it, as a paywall on a level the player was never going to clear, which converts near 0% and reads as predatory.

**Offer parameters (filled example, 42,000-point threshold level):**

| Parameter | Value |
|---|---|
| Trigger band | Final score ≥ 36,960 (88% of 42,000) and < 42,000 |
| Offer | +5 moves |
| Price | $0.99 (or 100 soft currency, whichever the player has used more of in the last 7 days) |
| Frequency cap | Once per attempt; if declined, next offer on this level waits 2 attempts |
| Odds disclosure | N/A for this offer type (fixed reward, not randomized) — required only if the offer bundles a randomized booster |

**Target conversion band:** 1.8%–2.4% of players who enter the trigger band (studio average 2.1%, per SKILL.md's worked example). Outside this band, diagnose before touching price:

- **Conversion <1.5%:** check the trigger band isn't catching boards that are actually unclearable (audit board-completion logs for the failing cohort — if median gap-to-threshold among "near-fail" flags is >20%, the band is mis-calibrated, not the price). If the band is correct, the read is frustration, not purchase intent — the fix is retuning the level (narrow the trigger band or lower the win threshold), not discounting the offer.
- **Conversion >3%:** the level may be intentionally engineered as a "paywall level" — confirm this is a deliberate monetization design (common past level ~120 in many live-ops titles) rather than an accidental difficulty spike; if unintentional, it will show up as elevated post-fail abandonment despite the high conversion, and both numbers need to move together.

**Fallback positions, in preference order, when a near-fail offer underperforms its 1.8%–2.4% band with the trigger condition confirmed correct:**
1. Add a one-time bonus-tile trigger for players who land in the band but decline the offer — converts a subset of the abandonment into retention without touching price (this is the fix used in SKILL.md's Level 162 memo).
2. Narrow the win threshold by 5–10% for the specific cohort generating the near-fail cluster, re-measure at the next 14-day cohort pull.
3. Only as a last resort, adjust price — price is the least diagnostic lever and the last one to move, because it changes revenue-per-conversion without addressing whether the trigger band or the level itself is miscalibrated.
