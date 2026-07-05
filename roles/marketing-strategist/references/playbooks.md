# Playbooks

Operational playbooks a strategist actually runs, with structure and example numbers. These are starting points to adapt, not scripts.

## 1. Positioning exercise (Dunford-style)

Run as a 2×3-hour workshop with sales, product, CS, and a founder/exec. Never solo — positioning written alone in a doc gets politely ignored.

**Steps, with a filled example (B2B expense-management SaaS):**

1. **List true competitive alternatives** — what customers would actually do, not your competitor slide. *Example: spreadsheets + email receipts (60% of lost deals), Expensify (25%), "do nothing, finance suffers" (15%).* If "spreadsheets" or "nothing" dominates, you're competing with inertia, and messaging must sell the problem before the product.
2. **Isolate unique attributes** — what you have that the alternatives don't. Be literal. *Example: real-time card feeds, auto-matching receipts to transactions, closes books 5 days faster.*
3. **Map attributes to value** — so what does each attribute buy the customer? *Example: "closes books 5 days faster" → controller stops working month-end weekends.*
4. **Identify who cares most** — the segment for whom that value is a hair-on-fire problem. *Example: 50–500-employee companies with one controller and no FP&A team. Not enterprise (they have staff), not 10-person startups (no month-end close pain yet).*
5. **Choose the market category** that makes the value obvious by default. *Example: "expense management" (crowded, price-compared) vs. "continuous close software" (new, needs explaining) — chose expense management, differentiated on close speed, because category creation was unaffordable at their stage.*
6. **Layer on trend only if genuinely relevant** — don't bolt on AI/whatever to look current.

**Output artifact:** a one-page positioning doc — the filled statement, the ranked alternatives list, the "who cares most" segment definition, and 3 proof points. Everything downstream (messaging hierarchy, briefs, site copy) cites this doc or gets sent back.

**Cadence:** revisit when a serious new alternative appears, when win/loss language shifts, or every 12 months — whichever comes first.

## 2. Channel portfolio review

Quarterly, 90 minutes, decisions required at the end. Inputs prepared beforehand; the meeting is for calls, not for reading dashboards together.

**The core table (example, $150k/mo budget):**

| Channel | Spend | Attributed CAC | Est. incremental CAC | Payback (mo) | Marginal CAC trend | Verdict |
|---|---|---|---|---|---|---|
| Meta prospecting | $80k | $185 | ~$200 | 11 | rising fast | cut & rebuild |
| Google branded | $25k | $45 | ~$64 (0.7x) | 3 | flat | holdout test |
| Google non-brand | $25k | $152 | ~$150 | 9 | stable | hold |
| TikTok | $10k | $98 | unknown | 5 | flat | scale w/ cap |
| Podcasts | $10k | ~$170 | unknown | 12+ | n/a | restructure |

Payback = CAC ÷ contribution margin per customer per month. Use contribution margin, never revenue.

**Saturation signals (any two together = treat as saturating):**
- CPM/CPC rising faster than the platform average for your vertical
- Frequency climbing with flat or falling reach
- CTR down 20%+ on refreshed creative (rules out creative fatigue as the sole cause)
- Marginal CAC ≥ 1.5× that channel's average CAC
- Audience overlap reports showing you're re-buying the same users

**Incrementality testing options, cheapest first:**
1. **Pause test** (~free, crude): turn a channel off for 2–4 weeks, watch blended conversions. Confounded by seasonality; acceptable for small channels only.
2. **Geo holdout** (low cost, weeks): pause or reduce in matched geos, compare. The workhorse. Needs enough conversion volume per geo — under ~30 conversions/geo/week, results are noise.
3. **Platform conversion-lift study** (free from the platform, but the platform grades its own homework — use as directional input, not verdict).
4. **Audience-split holdout / ghost ads** (moderate cost, cleanest for one platform).
5. **Full MMM calibrated with geo tests** (Meridian/Robyn or vendor; months of effort, justified above roughly $500k/mo spend or 6+ material channels).

**Rule:** any channel over ~15% of budget that has never had an incrementality test gets one scheduled before it gets more money.

## 3. Budget allocation: brand vs. performance

Heuristics by stage — with the caveats that make them honest:

| Stage | Brand : Performance | Reasoning |
|---|---|---|
| Pre-PMF / <$5M rev | ~10:90 | You don't know the message yet; performance spend is also research. "Brand" here = consistent identity, not media dollars. |
| $5–50M, growing | 20–30 : 70–80 | Demand capture still cheap; start brand investment before capture saturates, because brand takes 6–12+ months to show up. |
| $50M+, category known | 40–60 : 60–40 | Binet & Field's ~60/40 territory. Performance-only at this stage means renting demand competitors' brands created. |
| Category leader | 60:40 or higher | Defending mental availability is the job; performance mops up. |

**The honest caveats:**
- These splits come mostly from consumer-category IPA data; B2B with 3 buyers a quarter and $200k ACVs does not obey a FMCG curve. Direct sales motion shifts the real "brand" budget into content, community, and events that don't sit in the media line.
- Runway overrides ratio. With <12 months of cash, brand spend you can't survive long enough to harvest is theater. Say so.
- The split is an output of the portfolio review, not an input. Set it by marginal returns and demand-pool depth, then sanity-check against the table — not the other way around.
- Whatever the split, brand spend gets a measurement plan too (share of search, aided/unaided awareness tracking, branded search volume trend, geo-level lift). "It's brand, you can't measure it" is a resignation letter in slide form.

## 4. Messaging hierarchy doc

One page. Everything customer-facing derives from it; nothing customer-facing contradicts it.

```
1. Positioning statement          (from the positioning doc — verbatim)
2. Core narrative                 (2–3 sentences: the change in the world,
                                   why old ways fail, what winners do now)
3. Value pillars (max 3)
   Pillar → claim → proof point → customer quote
   e.g. "Close faster" → "Books closed in 3 days, not 8"
        → benchmark data across 400 customers → controller quote
4. Segment overlays               (per key segment: which pillar leads,
                                   what vocabulary changes, what objection
                                   to pre-empt — economic buyer leads with
                                   cost pillar, technical buyer with
                                   integration pillar)
5. Banned phrases                 (claims legal/product won't stand behind,
                                   and competitor framings we refuse to adopt)
```

Review trigger: same as positioning. If sales decks stop matching this doc, the doc is dead — fix it or enforce it, don't let both drift.

## 5. Launch / campaign brief template (filled)

A brief that can't fill these fields isn't ready for creative.

```
CAMPAIGN: "Close the Books, Open the Weekend" — Q4 launch, auto-close feature
OWNER: Marketing strategist (S. Park)   BUDGET: $60k over 8 weeks

AUDIENCE: Controllers/VPs Finance, 50–500-employee cos, currently on
  Expensify or spreadsheets. NOT enterprise, NOT pre-close startups.
INSIGHT: Win/loss calls: 7 of 10 champions mentioned month-end weekends
  unprompted. The emotional job is reclaiming personal time, not "efficiency."
SINGLE MESSAGE: Your close should take 3 days, not 8.
  (Pillar 1 of messaging hierarchy; proof: 400-customer benchmark.)
CHANNELS & WHY: LinkedIn ($35k — where this title researches vendors),
  finance-community newsletter sponsorships ($15k — trusted voices),
  webinar with a customer controller ($10k — bottom-funnel proof).
SUCCESS METRIC: 250 qualified demo requests at ≤$240 each.
MINIMUM VIABLE SIGNAL: ≥60 demo requests by week 3 at ≤$300 each,
  else pause and re-cut creative/audience before spending the back half.
MEASUREMENT: UTM + CRM source, holdout = no-touch lookalike geo set for
  branded-search lift; post-demo "how did you hear about us" field.
WHAT WE ARE NOT DOING: no discount offer (position is value, not price);
  no broad awareness video — constraint this quarter is consideration.
```

The two fields most often missing from weak briefs: **minimum viable signal** (the pre-committed kill/adjust threshold) and **what we are not doing** (the scope fence that stops mid-flight additions).
