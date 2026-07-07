# Interviewer — Playbook

## Quota-tracker table (filled example, day 7 of a 10-day field period)

| Cell | Definition | Target | Completes | Fill rate (per day) | Status | Projected final |
|---|---|---|---|---|---|---|
| 1 | Male, 18-34 | 25 | 25 | — | Closed | 25 |
| 2 | Female, 18-34 | 25 | 23 | 3.3/day | Open | 25 (day 8) |
| 3 | Male, 35+ | 25 | 25 | — | Closed | 25 |
| 4 | Female, 35+ | 25 | 11 | 1.6/day | Open — at risk | ~17 (shortfall) |

Fill rate = completes to date ÷ field days elapsed. Projected final = current completes + (remaining field days x fill rate), capped at target. A cell showing a projected final below target with more than 1 field day remaining gets flagged in the daily status report, not just the closing-day report — the earlier a shortfall is visible, the more field-period options (extension, incentive, reweighting) stay available.

## Refusal-disposition codes and re-approach rules

| Disposition | Meaning | Re-approach? |
|---|---|---|
| Soft refusal | "Not a good time," "too busy," no explicit "don't call again" | Yes — different day/time, restate purpose and time estimate |
| Privacy/trust concern | Respondent questions legitimacy or data use | Yes, once — offer verification (callback number, sponsor name); no further attempts if declined again |
| Hostile refusal | Explicit anger, hangs up abruptly | No — log and remove from further contact for this study |
| Explicit "do not call again" | Respondent states this directly | No — honor immediately, flag in system to suppress future studies per do-not-call list policy |
| Language barrier | Respondent doesn't speak an available interview language | No re-approach by this interviewer; route to language-matched interviewer if the study supports it, otherwise terminal non-response |

## Refusal-conversion callback script (filled example)

> "Hi, this is [interviewer name] calling back from [organization]. I know I reached you at a difficult time before — I wanted to check if now might work better, or if there's a time later today or this week that would. The survey takes about [X] minutes and is about [one-sentence neutral topic description]. If now still isn't good, I'm happy to try again another time — just let me know what works."

Note what this script does NOT do: it doesn't add pressure ("this will only take a second"), doesn't misstate the time estimate to sound shorter, and doesn't argue with the respondent's stated reason. Each of those would introduce a different kind of bias (rushed, low-quality responses; or a self-selected sample of people willing to be pressured) even if it raised the raw completion count.

## Break-off logging format

When a respondent starts but doesn't finish, log:

- **Break-off question number/section** (not just "incomplete") — e.g. "Broke off at Q14, start of the household-income battery."
- **Stated reason if given** — "said they had to go," "seemed uncomfortable with income questions," or blank if none given.
- **Elapsed time at break-off** vs. expected time to that point — a break-off well past the expected duration for that section is a different pattern than one at the exact expected pace.

Example log entry:

> Case #0847. Break-off at Q14 (household income battery start). Elapsed time: 11:20 vs. expected ~9:30 to this point. No reason given — respondent said "I have to go" and ended the call. Logged as break-off, not refusal (completed 13 of 22 questions). Not counted toward quota.

A cluster of break-offs at the same question (e.g. 6 of 40 incomplete interviews all breaking off at the same income question) is itself a finding to report — it may indicate the question is worded in a way that's triggering discomfort or confusion beyond what the researcher anticipated, independent of any individual respondent's reason.
