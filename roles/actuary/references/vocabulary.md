# Actuary working vocabulary

Terms an actuary uses precisely. Format: definition → how a practitioner says it → common misuse.

**Ultimate (loss)** — The total amount a claim, accident year, or line will eventually cost once every claim is closed, including IBNR — a projection, not an observed number until decades later for the longest-tail lines.
In use: "AY2023 ultimate is $20.0M; only $12.0M of that has emerged so far."
Misuse: treating "ultimate" as if it were the current reported figure, or assuming a mature-sounding evaluation age (24, 36 months) means the ultimate is nearly known for a genuinely long-tail line.

**IBNR (incurred but not reported)** — The portion of ultimate losses not yet reflected in reported losses (paid + case reserves) — covers claims not yet reported to the carrier and future development on claims already reported ("IBNER").
In use: "IBNR is $8.0M this quarter, up from $0.3M — almost entirely a factor-selection change, not new claims."
Misuse: assuming IBNR only means "claims nobody has told us about yet." Most of a mature line's IBNR is IBNER — known claims that will develop further, not unknown ones.

**Chain-ladder method** — Projects ultimate losses by applying cumulative development factors, derived from historical age-to-age patterns, to current reported (or paid) losses.
In use: "Chain-ladder gives $19.27M on the revised factors — check it against BF before selecting."
Misuse: applying it mechanically to immature or thin accident years, where a small reported base multiplied by a large factor produces wild, unreliable swings.

**Bornhuetter-Ferguson (BF) method** — Blends an a priori expected loss estimate (from pricing) with the chain-ladder's implied percentage unreported, so early development doesn't get fully driven by (often noisy) actual emergence.
In use: "BF dampens the swing on this immature year — it's $20.75M versus chain-ladder's $19.27M, and BF is more trustworthy at this maturity."
Misuse: using BF as the default for every accident year including fully mature ones, where the a priori expected loss ratio is stale and chain-ladder's own signal should dominate.

**Credibility (classical / limited-fluctuation)** — The formal weight (Z, between 0 and 1) given to a data set's own indication versus a complement, based on volume relative to a full-credibility standard (1,082 claims for ±5% at 90% confidence, per the standard classical formula).
In use: "This segment is 79% credible — Z = 0.886 — so the filed change blends 88.6% own indication with 11.4% the countrywide number."
Misuse: treating "credible" colloquially (believable) rather than as the specific statistical weight it is, or applying full weight to any data set that merely "feels like enough" without checking it against the standard.

**Complement of credibility** — The alternative estimate (industry benchmark, prior approved rate trended forward, broader class-plan indication) blended in for the portion of the estimate not covered by own-data credibility.
In use: "Our complement is the countrywide indication, territory-adjusted — not just '0% change,' which is itself an unexamined assumption."
Misuse: defaulting to "no change" as the complement by default, which silently asserts a specific answer without justifying it.

**Development factor (age-to-age / link ratio)** — The ratio of cumulative losses at one evaluation age to the prior age, averaged across accident years (volume-weighted, simple, or medial) to produce a selected factor.
In use: "The 24-to-36 factor jumped to 1.35 on the last two diagonals — we didn't just take the 5-year average."
Misuse: averaging every available year with equal weight regardless of whether the most recent diagonals are diverging from the pattern — the average can hide exactly the signal that matters.

**CDF (cumulative development factor) / tail factor** — CDF is the product of all remaining age-to-age factors from a given age to ultimate. The tail factor is the (often judgmental) portion beyond the last age with credible triangle data.
In use: "CDF from 24 months is 1.606, including a 1.03 tail — the tail is benchmark-based since our own data only goes to 60 months."
Misuse: computing CDF correctly but selecting the tail factor by extrapolating the triangle's own thin late-development data instead of anchoring to industry benchmarks when own experience doesn't reach that far.

**Permissible (loss) ratio** — The maximum loss ratio a rate can sustain while still covering expenses and the target profit provision; permissible = 1 − expense ratio − profit provision.
In use: "Permissible is 58% this filing — 37% expense, 5% profit — so a 63% trended loss ratio supports a rate increase."
Misuse: comparing an actual loss ratio to an industry-average combined ratio instead of to the company's own permissible ratio, which depends on its own expense structure and target return.

**Combined ratio** — Loss ratio plus expense ratio; above 100% means an underwriting loss before investment income.
In use: "Combined ratio is 104% this year, but paid-to-incurred is also declining — check whether the ratio's improvement story next year is real or reserve-driven."
Misuse: treating combined ratio movement as automatically reflecting underwriting or claims performance without checking whether reserve releases or strengthening are driving the change.

**Loss trend (frequency vs. severity)** — Frequency trend = change in claim rate per exposure unit over time; severity trend = change in average cost per claim. Both are fit and applied separately before recombining into a net loss-cost trend.
In use: "Frequency is trending −1%, severity +7.5% — net loss cost is still up 6.4% even though claim counts are falling."
Misuse: quoting only a single blended trend figure, which can mask a frequency decline offsetting (and hiding) an accelerating severity problem.

**Social inflation** — The rise in claim severity driven by litigation dynamics — larger jury verdicts, third-party litigation funding, eroding tort reform, plaintiff-bar strategy shifts — rather than by economic inflation or claims volume.
In use: "The 24-to-36 factor jump is social inflation showing up in bodily-injury severity, not a data error."
Misuse: invoking it as a catch-all excuse for any adverse development without checking whether a more mundane cause (claims-handling change, one large claim, data error) explains it first.

**Statement of actuarial opinion (SAO)** — The signed opinion (governed by ASOP 36) stating whether booked reserves make a reasonable provision for unpaid claim obligations, filed with regulators.
In use: "The SAO this year carries a risk-of-material-adverse-deviation disclosure on AY2023 given the trend shift."
Misuse: treating the SAO as a formality to be copy-forwarded year to year rather than re-derived from the current year's actual risk factors.

**Risk-based capital (RBC) ratio** — A regulatory solvency measure comparing a company's total adjusted capital to its Authorized Control Level RBC; action levels trigger regulatory intervention well above outright insolvency.
In use: "We're at 240% of ACL — above the 200% Company Action Level, but trending toward it, so the capital plan is already being drafted."
Misuse: treating 100% (technical insolvency) as the relevant threshold to manage to, instead of the 200% Company Action Level that triggers a mandated response long before actual insolvency.
