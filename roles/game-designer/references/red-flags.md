# Red Flags

Smell tests for level, economy, and live-ops data. Each one names the exact number that should trigger a look, what it usually means, the first question to ask before touching anything, and the report that answers it.

### Tutorial-to-level-3 drop-off above 30% of new installs
- **Usually means:** the first mechanic introduction is unclear or too slow, not that the game itself is unappealing — install-to-tutorial-complete and tutorial-complete-to-level-3 are usually two separate failure points bundled into one number.
- **First question:** at which exact step (mechanic-intro screen, first fail, first ad/paywall) does the funnel actually drop, not just that it drops?
- **Data to pull:** first-session funnel report broken out by onboarding step, segmented by platform (iOS and Android funnels commonly diverge by 5-10 points at the same step).

### D1 retention under 25% for a mid-core-loop puzzle title
- **Usually means:** the core loop's first-session hook (first meaningful reward, first difficulty spike) isn't landing — distinct from a D7/D30 problem, which is usually content pacing or fatigue rather than onboarding.
- **First question:** is the drop concentrated in players who never complete a first win, or spread evenly across skill cohorts?
- **Data to pull:** D1 retention segmented by first-session outcome (won level 1, failed level 1, quit before finishing level 1).

### Top 1% of paying users generating more than 50% of IAP revenue
- **Usually means:** the economy is whale-dependent, by design or by drift — not automatically broken, but a single high-value player's churn now moves the revenue line more than a batch of level retunes can.
- **First question:** is this ratio stable release over release, or moving — increasing (economy calcifying around fewer payers) or decreasing (broadening, but possibly diluting average revenue per paying user)?
- **Data to pull:** payer-concentration report (revenue by percentile of paying users), trended over the last 6 batches.

### Median session length down more than 25% over two consecutive builds
- **Usually means:** an interstitial ad frequency increase, a load-time regression, or a level-length change shipped in one of those builds — rarely a sudden shift in player taste.
- **First question:** did either build touch ad cadence, load times, or average level length, before assuming a content or difficulty problem?
- **Data to pull:** session-length trend with build-version overlay, plus ad impressions per session for the same window.

### Booster usage on a single level more than 2x the batch average
- **Usually means:** players are spending boosters to survive a spike rather than using them as an intended progression aid — a proxy for hidden difficulty that pass rate alone hides, since a boosted clear still counts as a clear.
- **First question:** does the booster spike land in the near-fail band right before the win threshold, or earlier in the attempt — which points to an upfront spike rather than an end-of-level one?
- **Data to pull:** booster-activation log per level, joined to attempt outcome (cleared with booster vs. cleared without).

### Voluntary mid-level exit rate above 15% of attempts
- **Usually means:** boredom or a comprehension breakdown, not difficulty — a fail is a data point about the mechanic, a quit-without-failing is a data point about whether the player wanted to keep playing at all.
- **First question:** does the exit cluster early in the attempt (comprehension problem) or late (fatigue), by elapsed time or moves used?
- **Data to pull:** mid-level-exit timestamp distribution relative to attempt start, per level.

### Average days-to-first-purchase up, with the first-purchase level number moving 2+ levels later release over release
- **Usually means:** the early-game want-chain isn't surfacing a monetization hook soon enough, or an earlier offer's position got cut or deprioritized in a recent batch.
- **First question:** did the level number or trigger condition of the first purchase-eligible offer move later in the sequence in a recent release?
- **Data to pull:** first-purchase-event level-number distribution, trended by release.

### Soft-currency balance per active user growing more than 10% week over week
- **Usually means:** a sink/faucet imbalance — a new faucet (event reward, login bonus) shipped without a matching sink, or an existing sink got harder to trigger as completion rates shifted.
- **First question:** which specific faucet or sink line item changed in the last two batches?
- **Data to pull:** currency-economy report broken into faucets and sinks by source, not just the net balance.

### Store rating drop of more than 0.3 stars within a week of a specific release
- **Usually means:** a build-specific regression — a crash, a broken level, a monetization change players read as predatory — not a slow drift in general sentiment.
- **First question:** do the 1- and 2-star reviews in that window cluster on one complaint (a crash, a named level, a pricing change), or are they generic?
- **Data to pull:** store review text filtered to the release window, plus crash-free-session rate for the same build.

### Crash-free session rate under 99% on a build already in production
- **Usually means:** an engineering regression masquerading as a difficulty or churn complaint in the level data — a player who crashes mid-level often registers as an unexplained abandon or fail.
- **First question:** does the churn or fail spike correlate by device/OS version with the crash cluster, rather than by level or skill cohort?
- **Data to pull:** crash-free-session rate by device/OS, cross-referenced against the level(s) showing the anomalous data.

### An A/B test run past 4x the level's median time-to-cohort-completion with no significant result
- **Usually means:** the test is underpowered for the metric being read — D7 or conversion needs a much larger N and longer window than first-attempt clear rate — not that the two variants are truly equivalent.
- **First question:** was the sample-size calculation done against the actual reported metric, or against a proxy metric that reaches significance faster?
- **Data to pull:** the test's power/sample-size worksheet for the metric being reported, plus current N and elapsed cohort-days.
