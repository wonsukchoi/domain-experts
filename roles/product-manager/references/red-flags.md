# Red Flags — Smell Tests a Senior PM Catches Instantly

Each entry: what the smell usually means, the first question to ask, and what to actually look at. None of these are automatic verdicts — they're triggers for a specific check that takes minutes and routinely changes the decision.

---

## 1. Roadmap item with no problem statement

The ticket says "Build workspace templates" and the description is a feature spec, or empty.

**Usually means:** the item entered the roadmap through authority (an exec said so), momentum ("it's been on the list for three quarters"), or competitor anxiety — not through evidence. Features without problem statements can't fail, because nobody defined what they were supposed to fix; they also can't succeed.

**First question:** "What breaks for which user if we never build this?"

**Look at:** whether anyone can name the metric this is supposed to move; whether any discovery notes, support tickets, or usage data are linked. If the honest answer to the question is "nothing breaks, but it'd be nice" — it's a candidate for deletion, not scoping.

---

## 2. "We'll measure engagement" as the success metric

Or its cousins: "usage," "adoption," "activity" — any noun without a number, a denominator, and a deadline.

**Usually means:** nobody wants to be accountable for a specific outcome, so the metric was left vague enough that any result can be narrated as success. Post-launch, whatever went up gets promoted to "the metric we cared about."

**First question:** "What number, measured how, by what date, would make us call this a failure?"

**Look at:** whether the team can state the current baseline. If they don't know today's value, they haven't looked at the data, and the metric is decoration. A real version reads: "weekly workflow-edit rate among team leads, 22% → 30% within 60 days of GA."

---

## 3. Sales-driven feature with n=1 customer

"Acme needs multi-region data residency or the renewal is at risk." One account, one champion, one escalation.

**Usually means:** one of three things — (a) a real emerging segment need where Acme is just first, (b) an account-management problem being laundered through the roadmap because a discount or exec call is harder to ask for, or (c) a champion inside Acme who wants the feature more than Acme does. (b) is most common.

**First question:** "Which other accounts have this job — not this request, this *job* — and what do they do today?"

**Look at:** CRM and support for the same underlying need in other accounts (search the problem, not the feature name); the account's actual usage depth (an account barely using the product won't be saved by a new feature); whether the ask survives being offered a services/workaround alternative. If it evaporates when a cheaper path appears, it was (b).

---

## 4. Adoption metrics counting logins, not value events

The dashboard says "feature adoption: 61%" and the definition turns out to be "opened the page at least once."

**Usually means:** the metric was defined by what was easy to instrument, not by what indicates value delivered — or was defined generously because a launch narrative needed it. Page-opens include every curiosity click from the announcement banner.

**First question:** "What's the user action that means they actually got the value — and what's the number for *that*?"

**Look at:** the funnel from open → meaningful action → repeat within 30 days. Typical shape: 61% opened, 24% completed the core action once, 9% did it twice. The 9% is the adoption number. If repeat usage isn't instrumented at all, that's the finding.

---

## 5. A/B test peeked at day 2

"Early results look great — treatment is up 18%, can we ship?" Test was planned for two weeks.

**Usually means:** the team doesn't understand sequential peeking (checking repeatedly until significance appears inflates the false-positive rate several-fold — a "significant" day-2 result is frequently noise that regresses by day 10), or someone with a stake in the outcome is shopping for permission to stop early.

**First question:** "What sample size and duration did we pre-register, and what was the basis?"

**Look at:** whether a power calculation exists at all. If none does, the test can't be rescued by running longer — the minimum detectable effect was never defined. Also check for a novelty-effect window (metrics that spike week 1 and fade) and whether the metric being celebrated was the pre-registered primary or a flattering secondary found after the fact.

---

## 6. Velocity theater

Sprint review celebrates 47 points shipped, six releases this quarter, roadmap 94% on-time. Nobody mentions a customer or a metric.

**Usually means:** the team is being measured on output because outcomes are slower, noisier, and someone might look bad. Often it's a symptom of the layer above: leadership asks "is it on track?" and never "did the last one work?" — so the team optimizes for the question actually being asked.

**First question:** "Of the last five things we shipped, which ones moved their target metric — and which ones had a target metric?"

**Look at:** post-launch reviews (do any exist?); the ratio of roadmap items with pre-registered success criteria to those without; whether anything shipped in the past year was subsequently killed or rolled back. A team that has never killed a shipped feature isn't batting 1.000 — it's not keeping score.

---

## 7. Bonus: the feature that "just needs better onboarding"

8% adoption after two quarters, and the plan is a tooltip tour and an email campaign.

**Usually means:** the team is treating a demand problem as an awareness problem, because awareness is fixable with two weeks of work and demand isn't. Occasionally discoverability genuinely is the issue — but if users who *did* find the feature don't retain in it, more traffic into a leaky funnel changes nothing.

**First question:** "Of the users who found it, how many came back a second time?"

**Look at:** retention *within* the feature among users who tried it. Tried-once-never-returned above ~70% is a value problem; kill or rethink. Strong repeat usage among a tiny discoverer pool is the one case where the onboarding plan deserves its shot — with a pre-registered adoption target and a kill date attached.
