# Working Vocabulary — Terms Generalists Misuse

Format per term: definition, a sentence the way a practitioner actually uses it, and the common misuse to avoid.

---

**Outcome vs. output**
An output is a thing shipped (feature, release, doc). An outcome is a measurable change in user or business behavior the output was supposed to cause.
*Usage:* "The output was the templates gallery; the outcome we're accountable for is second-workflow creation going from 34% to 50%."
*Misuse:* status updates that report outputs as if they were outcomes — "we delivered the integration" answers "what did you ship," not "did it work."

**Activation vs. adoption vs. retention**
Activation: a *new* user reaches first value (the setup moment — e.g., creates their first workflow within 7 days). Adoption: an existing user incorporates a capability into how they work (repeat use of a feature, not first touch). Retention: users/accounts keep coming back over time, usually measured in cohorts.
*Usage:* "Activation is fine at 58%; the problem is adoption of anything beyond the first workflow — which is why week-12 retention sags."
*Misuse:* using the three interchangeably, or calling a single page-view "adoption." Each stage has a different owner, a different fix, and a different time window; conflating them hides where the funnel actually leaks.

**North-star metric vs. guardrail**
North star: the single metric that best proxies value delivered, which the whole team optimizes (e.g., weekly workflows completed). Guardrail: a metric you must *not* degrade while chasing the north star (support ticket rate, page load time, unsubscribe rate).
*Usage:* "The experiment moved the north star 4% but tripped the notification-opt-out guardrail, so we're not shipping it as-is."
*Misuse:* five "north stars" (then you have none), or running experiments with no guardrails — which quietly rewards cannibalizing long-term trust for short-term metric wins.

**Discovery vs. delivery**
Discovery: the work of figuring out what's worth building — interviews, prototypes, data analysis, spikes. Delivery: the work of building and shipping it reliably. Healthy teams run both continuously, in parallel.
*Usage:* "That's still in discovery — we have interview signal but no behavioral evidence, so it doesn't get an engineering slot yet."
*Misuse:* treating discovery as a phase that ends ("we did research in January"), or as a gate to skip when an exec is confident. Discovery is a weekly habit, not a project stage.

**MVP vs. v1**
An MVP is an *experiment* — the smallest thing that tests the riskiest assumption, and it may be a concierge service, a landing page, or a spreadsheet rather than software. A v1 is a *product* — the first version real customers rely on, which must meet a quality bar.
*Usage:* "The MVP is a manual CSV we email weekly to five design partners; if they open it three weeks running, we build the v1."
*Misuse:* the most abused term in the field — "MVP" as a euphemism for a v1 with the quality cut out. If customers are paying for it and depending on it, it's a v1 and owed v1 quality, whatever the roadmap slide calls it.

**Opportunity cost of a roadmap slot**
The value of the best alternative not built because this item took the capacity. The true cost of any feature is not its engineering weeks — it's the next-best feature those weeks would have funded.
*Usage:* "The report builder isn't expensive because it's 12 weeks; it's expensive because those 12 weeks are Slack notifications plus bulk-edit."
*Misuse:* evaluating a feature in isolation ("it's only three weeks, why not?"). "Why not" is never the bar; "instead of what" is.

**Counter-metric**
A metric watched specifically because it would reveal your primary metric being gamed or achieved harmfully. Close cousin of a guardrail, chosen adversarially: ask "how could this number go up while things get worse?"
*Usage:* "If we push notification volume to drive DAU, the counter-metric is opt-out rate — that's how we'd catch ourselves juicing the number."
*Misuse:* omitting one entirely, which turns "the metric went up" into unfalsifiable good news.

**Leading vs. lagging indicator**
Lagging: confirms results after they've happened (revenue, churn, NPS) — trustworthy but too late to act on. Leading: earlier signals that predict the lagging ones (activation rate, time-to-first-value, workflow #2 creation) — actionable but noisier.
*Usage:* "Churn is a lagging read on decisions we made two quarters ago; the leading indicator we can still do something about is week-3 second-workflow rate."
*Misuse:* managing the quarter by lagging metrics (steering by the rearview mirror), or the inverse — celebrating a leading indicator without ever validating that it actually predicts the lagging one.

**JTBD (jobs-to-be-done)**
The framing that customers "hire" a product to make progress in a specific circumstance — the job is stable even as solutions change, and the competition is whatever else gets hired for the job, including spreadsheets and doing nothing.
*Usage:* "The job isn't 'use our reporting feature' — it's 'prove to my boss monthly that the team is on track,' and today Excel is hired for it."
*Misuse:* relabeling a feature list as "jobs" ("the job is to use filters"). A real job statement contains a circumstance and a progress goal, and never mentions your product.

**Problem statement**
A falsifiable description of who has what pain, how often, with what evidence — deliberately containing no solution.
*Usage:* "Come back with a problem statement: which segment, what they can't do today, how we know, and what it costs them."
*Misuse:* solution-shaped problems — "the problem is we don't have dark mode." That's a feature request wearing a problem costume; the tell is that only one solution could possibly "solve" it.

**Two-way vs. one-way door**
Decision taxonomy by reversibility (Bezos's framing). Two-way doors can be walked back cheaply — decide fast, on thin evidence, low in the org. One-way doors can't — decide slowly, with a written doc and senior eyes.
*Usage:* "Defaulting the toggle on is a two-way door; deprecating the v1 API is a one-way door — those get different processes on purpose."
*Misuse:* applying one process to everything: heavyweight review for reversible calls (paralysis) or moving fast on irreversible ones (the expensive kind of scar tissue). Also, mislabeling doors — shipping "reversibly" to customers who build dependencies makes it a one-way door in practice.

**Product-market fit (PMF)**
Sustained, organic demand pull — retention curves that flatten instead of decaying to zero, and growth that doesn't stop when the paid spend does.
*Usage:* "The retention curve flattens at 38% after month 3 — that's fit in the mid-market segment; enterprise is still a hypothesis."
*Misuse:* declaring PMF from revenue that's actually founder-led sales heroics, or treating it as company-wide and permanent. Fit is per-segment and can be lost.

**Roadmap**
A prioritized statement of current belief about the most valuable problems to solve next, ordered by evidence — typically communicated as now/next/later themes.
*Usage:* "The roadmap changed because the evidence changed; here's what we learned and what moved."
*Misuse:* treating it as a dated delivery contract. Once "later" items have committed ship dates attached, the team has traded the ability to learn for the appearance of predictability — and will usually be forced to ship the wrong thing on time.
