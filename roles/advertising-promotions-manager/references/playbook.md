# Campaign playbook

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Media plan (built backward from objective)

**Objective:** Trial signups for new subscription tier among 600,000 existing non-subscribed users, 21-day flight before intro-price window closes.
**Effective frequency target:** 4 exposures/person (range for category: 3-7).
**Required impressions:** 600,000 × 4 = 2,400,000.

| Channel | % of impressions | Impressions | CPM | Cost | Rationale |
|---|---|---|---|---|---|
| CTV | 35% | 840,000 | $65 | $54,600 | Audience over-indexes on streaming per media-consumption data |
| Paid social (Meta/TikTok) | 45% | 1,080,000 | $18 | $19,440 | Highest reach efficiency for this audience segment |
| Programmatic display | 20% | 480,000 | $11 | $5,280 | Retargeting layer for users who saw CTV/social but didn't act |
| **Total** | 100% | **2,400,000** | — | **$79,320** | Against $96,000 approved budget |
| Reserved for creative test | — | — | — | $16,680 | 10% of CTV impressions held for A/B test before full delivery |

**Budget check:** $79,320 + $16,680 = $96,000 — matches approved budget exactly. If the backward-built plan exceeds budget, narrow audience or shorten flight before lowering the frequency target silently.

## 2. Creative brief

| Field | Content |
|---|---|
| Audience | 600,000 existing app users, active in last 90 days, never subscribed to paid tier |
| Objective | Drive trial signup before intro-price window closes (day 21) |
| Core message (one only) | "Try [tier] free for 14 days — price goes up after [date]" |
| Desired action | Tap-through to in-app trial signup flow |
| Mandatory constraints | Legal disclosure of intro-price end date must appear on-screen for 2+ seconds (CTV) or in first 3 lines of copy (social); brand color/logo lockup per brand guidelines v4 |
| What this brief does NOT specify | Visual style, talent, shot list, exact copy — creative team's call within the above |
| Success metric this creative is judged against | CTR uplift in A/B test vs. control concept, then conversion rate post-launch |

## 3. Creative test plan

| Step | Detail |
|---|---|
| Budget | $16,680 (10% of CTV allocation), 5 days before full flight |
| Variants | Cut A (product-demo led), Cut B (urgency/price-led) |
| Sample size | ~130,000 impressions per variant (sufficient to detect a 15%+ CTR difference at 90% confidence given category baseline CTR ~0.9%) |
| Decision rule | Winner = higher CTR at test's end, unless the gap is under 10% relative (in which case default to the lower-CPM variant) |
| Result (example) | Cut B: 1.34% CTR vs. Cut A: 1.10% CTR — 22% relative lift, exceeds the 10% decision threshold. Cut B becomes the default. |

## 4. Post-campaign debrief template (filled)

**Flight:** 21 days. **Budget:** $96,000 approved, $95,940 spent (99.9% of budget).

**Delivery:**
- Impressions: 2,393,000 / 2,400,000 planned (99.7%)
- Average frequency: 3.8 / 4.0 target
- Channel concentration: no channel exceeded 45% of delivered spend — no concentration flag
- Viewability (CTV/display, third-party verified): 74%

**Response:**
- Platform-reported (last-click) conversions: 16,900
- Holdout-adjusted conversions: 14,200 (5% holdout group converted at 1.9% organically; the gap is subtracted from the raw platform number)
- Conversion rate on holdout-adjusted number: 2.37% vs. 2.00% pre-set threshold — **threshold met**

**Attribution sanity check:** Platform-reported number overstated true lift by ~19% (16,900 vs. 14,200) — consistent with known last-click over-crediting; the holdout-adjusted figure is the one carried into the reported result.

**Recommendation for next flight:** Cut B (urgency/price-led) becomes default creative. Hold a 10%+ test-budget allocation for any flight of 14+ days. CTV CPM rose 8% from the prior comparable flight — worth a rate conversation with the vendor before the next quarter's buy.

## 5. Frequency-capping quick reference

| Signal | Action |
|---|---|
| CTR flat or rising, frequency under upper bound of effective range | Continue delivery as planned |
| CTR declining 20%+ week over week, frequency at or above upper bound | Cap frequency or rotate creative |
| CTR declining but frequency still under lower bound of effective range | Investigate creative/targeting fit, not frequency — the audience hasn't seen it enough for fatigue to be the cause |
| Reach plateauing (new-impression share dropping below ~15% of daily delivery) mid-flight | Signal of audience saturation on current channel mix — consider adding a channel rather than raising frequency further on the same one |
