# Artifacts & templates

Filled examples an agent can populate or execute against. Load this when producing an actual variance analysis, theo/comp calculation, or compliance flag — not for general reasoning (that's `SKILL.md`).

## Hold variance worksheet

```
Table/Game: [ID]              Shift: [date/shift]              Hands/spins dealt: [N]

Theoretical hold %: [house edge for this game/rules variant]
Average bet: $[X]
Theoretical win = Hands × Avg bet × Theoretical hold % = $[Y]
Actual win/(loss): $[Z]
Variance: $[Z - Y]

Standard deviation estimate (per-hand SD factor × avg bet × sqrt(hands)):
  SD ≈ [1.1-1.2 for blackjack, game-specific factor] × $[avg bet] × sqrt([N hands])
  = $[SD estimate]

Variance in SD units = [Z-Y] / SD estimate = [N] SD

Threshold: investigate if |variance| > ~2 SD (roughly 95% confidence outside normal range)
Result: [within normal range / outside normal range — investigate]

If investigating, check in order:
  1. Dealer procedure (surveillance review): [finding]
  2. Equipment/game integrity: [finding]
  3. Single-session concentration (one player driving the variance?): [finding]
  4. Bet-spread pattern if concentrated player identified: [ratio, correlation with count-favorable positions]
  5. Conclusion: [mundane cause identified / escalate to security for suspected cheating]
```

## Theoretical loss (theo) and comp calculation

```
Player: [ID]
Average bet: $[X]
Hands/decisions per hour (game-specific): [N] (e.g., ~60-80 for blackjack, ~500-600 for slots)
Hours played: [H]
House edge for game/bet type: [%]

Theo = Avg bet × Decisions/hour × Hours played × House edge %
     = $[X] × [N] × [H] × [edge%]
     = $[theo result]

Comp guideline (typical range, house-specific policy governs actual %):
  Comp budget = Theo × [house comp % policy, commonly 20-40% of theo for typical tier]

Do NOT price comp off: actual win/loss that session, how insistent the request is, or subjective
player value — theo is the number, session outcome is not.
```

## CTR / structuring flag checklist

```
Patron: [ID]                    Gaming day: [date]

Total cash-in transactions today: $[sum across all cage/table interactions]
Total cash-out transactions today: $[sum]

CTR threshold check: aggregate cash-in OR cash-out >= $10,000 in a single gaming day (US, verify
current threshold and jurisdiction-specific rules) -> [FILE CTR: yes/no]

Structuring check:
  - Multiple transactions each under threshold, same patron, same day: [count, amounts]
  - Transactions split across different cage stations/times to avoid single large transaction: [Y/N]
  - Pattern consistent with intentional threshold avoidance: [Y/N] -> if Y, file SAR regardless of
    whether CTR threshold was technically avoided

This is a mechanical compliance check, not a discretionary judgment call about the patron.
```
