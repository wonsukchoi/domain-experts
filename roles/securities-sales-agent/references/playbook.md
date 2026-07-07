# Securities Sales Agent — Playbook

## Share-class comparator (filled example)

Client horizon: 10 years. Gross expected return: 6.00%/yr, both classes, same underlying fund.

| Share class | Load | Ongoing fee | Net annual return | Initial invested | 10-yr projected value |
|---|---|---|---|---|---|
| A | 5.75% front | 0.25%/yr | 5.75% | $188,500 | $328,801 |
| C | none | 1.00%/yr | 5.00% | $200,000 | $325,779 |
| B | none (5-yr CDSC) | 1.00%/yr, converts to A at yr 8 | 5.00% until conversion, then 5.75% | $200,000 | ~$329,600 (converts before horizon ends) |

**Breakeven rule:** Class A recovers its front load against Class C's ongoing-fee drag at roughly year 7 for a 75bp fee spread. Below that horizon, recommend C or B; at or above it, recommend A unless a liquidity need falls inside the horizon.

**Liquidity check:** if the client may need funds inside a B-share's contingent deferred sales charge (CDSC) schedule (typically declining from 5% in year 1 to 0% by year 6), B is disqualified regardless of the breakeven math — the CDSC on early withdrawal can exceed the fee savings.

## Annuity rider cost breakdown (filled example)

Client: age 60, $300,000 premium, wants guaranteed lifetime income starting at 70.

| Component | Cost | What it insures |
|---|---|---|
| Base variable annuity, M&E fee | 1.25%/yr | Mortality/expense risk pooling, death benefit floor |
| Guaranteed lifetime withdrawal benefit (GLWB) rider | 0.95%/yr | Locks a 5% withdrawal rate on the "benefit base" for life, even if the account value hits zero |
| Fund-level expense ratios (underlying subaccounts) | 0.65%/yr avg | Investment management inside the annuity wrapper |
| **Total annual drag** | **2.85%/yr** | — |

**Reasoning check:** at a 5% guaranteed withdrawal rate on a $300,000 benefit base ($15,000/yr for life), compare against simply holding $300,000 unwrapped and running a 4% self-managed withdrawal rate ($12,000/yr, no longevity guarantee, no 2.85% annual drag). The rider is worth its cost only if the client's specific longevity risk (family history, no pension, small pool of other guaranteed income) justifies paying ~2.85%/yr more than an unwrapped portfolio to remove the risk of outliving the money. State this tradeoff explicitly in the file — never as "the annuity guarantees income," which is true but not the whole cost.

## Prospecting funnel tracker (filled example, quarterly)

| Source | Meetings booked | Qualified | Closed | Close rate (of qualified) | Avg new account size |
|---|---|---|---|---|---|
| Client referral | 12 | 11 | 6 | 54.5% | $145,000 |
| COI referral (CPA/attorney) | 8 | 8 | 5 | 62.5% | $210,000 |
| Seminar/cold outreach | 22 | 9 | 2 | 22.2% | $68,000 |
| **Total** | 42 | 28 | 13 | 46.4% | $138,150 avg |

**Diagnosis:** the seminar channel's qualification rate (9/22 = 41%) and close rate (22.2%) are both well below the referral channels — this is a pipeline-quality problem, not a volume problem. Adding more seminar meetings at the same 22.2% close rate produces proportionally more wasted time; the fix is tightening the qualification screen before the meeting, not running more seminars.

## Suitability file template (filled example)

- **Client objective:** stated in the client's own words, plus the advisor's restatement for confirmation.
- **Time horizon:** specific, in years, not "long-term."
- **Alternatives considered:** minimum two, named, with the specific reason each was rejected.
- **Cost comparison:** dollar terms at the client's actual horizon, not expense-ratio percentages alone.
- **Compensation disclosure:** whether the recommended option pays the rep more, less, or the same as the rejected alternatives, and confirmation the recommendation direction is unaffected by that difference.
- **Client acknowledgment:** signature/date confirming the objective, horizon, and cost comparison were reviewed before the transaction.
