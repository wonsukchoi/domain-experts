# Playbook

Filled templates a territory rep actually runs, with structure and plausible numbers. Starting points to adapt, not scripts.

## 1. Account tiering table

Rebuilt quarterly; drives call cadence and how much negotiating flexibility a rep pre-clears for each tier before a conversation happens.

| Tier | Definition (example territory, $11.1M total) | Count | % of territory revenue | Call cadence | Pre-cleared discount authority |
|---|---|---|---|---|---|
| A — Strategic | >$1M/year or >10% of territory | 2 accounts | 34% | Weekly + quarterly business review | 0%, escalate any ask |
| B — Core | $250k–$1M/year | 9 accounts | 44% | Biweekly | Up to 2% off list |
| C — Standing | $50k–$250k/year | 22 accounts | 18% | Monthly | Up to 4% off list |
| D — Transactional | <$50k/year | ~40 accounts | 4% | Quarterly / reactive | Up to 5% off list |

**Rule of thumb:** the more an account can hurt you if it leaves, the less unilateral pricing authority a rep should have on it — Tier A concessions go to a sales manager or pricing committee by default, not because the rep isn't trusted, but because a bad Tier A concession sets the floor for the whole distributor group behind it.

## 2. Pricing / rebate proposal structure

Use when a buyer opens a price, terms, or line-review conversation. Fill every row before the meeting, not during it.

```
ACCOUNT: [name]                          TIER: [A/B/C/D]
CURRENT: [units/yr] @ [$/unit list] = [$ revenue/yr]
CURRENT LANDED COST: [$/unit]            CURRENT MARGIN: [$/unit, %]
BUYER'S ASK: [price cut / terms / service — decompose all three]
COMPETITIVE CLAIM: [quote produced? Y/N — if N, treat as opener]

COST PRESSURE THIS CYCLE: freight [+/-X%], material [+/-X%]
  → new landed cost: [$/unit] ([+/-X%] vs. current)
  → full pass-through price to hold current margin %: [$/unit]

OPTION A — Straight cut to buyer's ask:
  [units] x [$/unit] = [$ revenue], margin [$/unit] = [$ total margin]
OPTION B — Flat price despite cost inflation:
  [units] x [$/unit] = [$ revenue], margin [$/unit] = [$ total margin]
OPTION C — Negotiated: list [$/unit] + volume tier(s) + rebate:
  Tier 1: [units] ([+X%]) → [X%] rebate → effective net [$/unit]
  Tier 2: [units] ([+X%]) → [X%] rebate → effective net [$/unit]
  [units] x [$/unit] = [$ revenue], margin [$/unit] = [$ total margin]

RECOMMENDATION: [Option], because [$ margin delta vs. both alternatives]
COMMITMENT REQUIRED IN EXCHANGE: [volume floor / term length / exclusivity]
AUTHORITY NEEDED: [within rep's band / escalate to manager / pricing committee]
EXPIRATION: this offer holds through [date]; re-quote required after.
```

**Rule:** never walk into the room with only Option A modeled. If the only structure prepared is the buyer's own ask, the negotiation is already lost before it starts.

## 3. Chargeback / deduction dispute log

Reconciled monthly against remittances, not at year-end. A rep who only checks this in December has already absorbed months of unrecovered margin.

| Date | Account | Invoice # | Deduction reason | Amount | Valid? | Action | Status |
|---|---|---|---|---|---|---|---|
| 3/4 | Heartland | 88213 | EDI ASN mismatch | $412 | No — ASN sent on time, buyer's WMS logged late | Disputed w/ documentation | Recovered 3/22 |
| 3/11 | Heartland | 88240 | Short-ship claim, 6 cases | $168 | Yes — picking error confirmed by 3PL | Accepted, root-caused with 3PL | Closed |
| 3/18 | Regional Supply | 88301 | Co-op ad fund overspend true-up | $1,050 | Pending — awaiting spend backup from buyer's marketing | Requested itemized spend report | Open |

**Threshold:** if deductions on an account exceed roughly 3% of invoiced revenue in a rolling quarter, escalate the account for a full audit before the next pricing conversation — a buyer running deductions above that level is either genuinely mismanaging compliance or using chargebacks as an informal price reduction, and the two require different responses.

## 4. Line-review defense prep checklist

Line reviews are scheduled events (usually annual or biennial for large accounts) — prep starts 60–90 days out, not the week of.

1. **Pull the account's own scorecard data** (OTIF %, fill rate, deduction rate, GMROI on your SKUs) — know your grade before the meeting; a rep who is surprised by their own scorecard has already lost credibility.
2. **Model GMROI for every SKU under review** against the account's stated hurdle rate. Anything below hurdle needs either a margin fix (price, cost, terms) or a planned graceful exit — don't defend a SKU that's genuinely underwater on their numbers.
3. **Bring a volume/margin history**, not just a relationship pitch — buyers on a line review are grading vendors against each other on data, not tenure.
4. **Prepare one concrete forward commitment** (a promotional calendar, a new-item pipeline, a rebate structure) — showing up only to defend the status quo reads as having nothing new to offer.
5. **Know your walk-away SKUs before the meeting.** Offering to sunset a genuinely low-performing item preemptively often buys credibility on the SKUs worth defending.

## 5. Trade show follow-up cadence

Trade show leads decay fast; the difference between a rep who converts and one who doesn't is almost entirely follow-up discipline, not the pitch at the booth.

| Day | Action |
|---|---|
| Day 0–1 (at show) | Log every conversation with account name, need stated, and next step — not just a business card scan |
| Day 2–3 | Personalized follow-up referencing the specific conversation, not a generic "great meeting you" blast |
| Day 7 | Send the specific material promised (price sheet, sample, spec) — never promise and not deliver within a week |
| Day 14 | Call to confirm receipt and ask the one open question from the show |
| Day 30 | If no traction, move to standard territory cadence for that account's tier; don't keep "special" follow-up going indefinitely for a cold lead |
