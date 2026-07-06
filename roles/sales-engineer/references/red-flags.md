# Red Flags — Smell Tests a Senior SE Catches Instantly

Each entry: the signal with a threshold, what it usually means, the first question a veteran asks, and the specific data to pull. None are automatic verdicts — they're triggers for a check that takes minutes and routinely changes the deal read.

---

### POC scope has grown past 5 success criteria, or criteria were never signed
**Usually means:** no economic buyer sign-off happened before kickoff, or the champion is trying to satisfy multiple internal factions by adding criteria instead of saying no to side requests.
**First question:** "Which of these criteria did the economic buyer actually sign, and on what date?"
**Data to pull:** the signed success-criteria document itself — not the Slack thread or verbal recap. No document, no signed criteria.

### Champion is the only technical contact reached after 3+ weeks in an active cycle
**Usually means:** single-threading — the deal has exactly one internal advocate, and that person's departure, reassignment, or being overruled kills the deal with no warning.
**First question:** "Who else on your team will be in the room for the technical evaluation?"
**Data to pull:** meeting attendee lists across the last 3 calls; if the same one name appears every time, the deal is single-threaded regardless of what the CRM stage says.

### Economic buyer still unnamed on a deal marked "commit" in forecast
**Usually means:** the AE is forecasting on champion enthusiasm, not on a confirmed buying process — a strong technical win with no named budget owner has no path to a signature.
**First question:** "Who signs the check, and have we met them?"
**Data to pull:** MEDDPICC scorecard's Economic Buyer field; if it's blank or says "assumed to be VP X," that's the finding.

### Prospect requests 8-10 features demoed in the first call
**Usually means:** discovery was skipped, or the AE promised a broad show to avoid a harder qualifying conversation — a wide, shallow demo produces enthusiasm that doesn't survive the first technical objection.
**First question:** "Of these ten, which one is blocking something they're trying to ship this quarter?"
**Data to pull:** the discovery notes (if any exist); their absence is itself the finding.

### RFP text uses feature-naming language that matches one competitor's spec sheet almost verbatim
**Usually means:** the incumbent or a preferred vendor co-authored the RFP, and the evaluation is a formality — win rates on RFPs authored with a competitor's fingerprints are materially lower than on RFPs shaped through open discovery `[heuristic — stated SE-community consensus]`.
**First question:** "Did the customer share this spec with any vendor before publishing it?"
**Data to pull:** line-by-line comparison against the suspected competitor's public feature-naming; a go/no-go score recompute with this factor weighted in.

### Security questionnaire or SOC 2 request never arrives despite a "hot" deal
**Usually means:** procurement isn't genuinely engaged yet, or the deal is earlier in reality than the forecast stage suggests — security review is one of the few steps that can't be faked by enthusiasm.
**First question:** "Has procurement been looped in, and when do they expect to send the security packet?"
**Data to pull:** the decision-process map from MEDDPICC; confirm whether a security/procurement step even exists in their stated process or was assumed.

### Technical stakeholder goes quiet for 2+ weeks after an enthusiastic first demo
**Usually means:** an internal objection surfaced that wasn't raised to the SE directly — budget freeze, a competing internal build, or a stakeholder who wasn't in the room raising a blocker after the fact.
**First question:** "What changed since our last call?" asked directly to the champion, not routed through the AE.
**Data to pull:** whether any new attendee appeared on the internal customer side (a CISO, a new VP) between the demo and the silence — new stakeholders reset the clock.

### The same technical objection recurs across 3+ opportunities in a quarter
**Usually means:** a real product gap, not a coaching problem — reps keep re-arguing the same point deal by deal instead of it being escalated once with aggregate impact.
**First question:** "How many deals this quarter have hit this exact objection, and what did we say each time?"
**Data to pull:** CRM objection-tagging (if it exists) or a manual tally across the SE team's deal notes; the count itself is the business case for a product-management escalation.

### SE unilaterally wrote the bake-off rubric without the champion's input
**Usually means:** the evaluation will read as self-serving the moment the champion or a competitor's SE notices the weighting favors one vendor's known strengths — this burns credibility with the evaluator even if the underlying comparison was fair.
**First question:** "Did the champion review and agree to these weights before we shared any results?"
**Data to pull:** the rubric's version history / send date versus the date results were first shared.

### A "phase 2" feature gets demoed as though it already ships
**Usually means:** pressure to win the room overrode the disclosure norm — the gap between what was shown and what's actually in production becomes the implementation team's problem at go-live, and the champion's problem with their own leadership.
**First question:** "Is this feature in the current GA release, or on the committed roadmap for a named quarter?"
**Data to pull:** the release notes or roadmap commitment doc; if the feature isn't in either, it was vaporware in the demo.

### Integration-effort estimate comes only from the SE, never validated by the customer's own engineer
**Usually means:** the "2 engineer-weeks" number is a sales estimate, not an engineering one, and gaps like custom serialization layers or auth integrations routinely add 50%+ to the real figure.
**First question:** "Has anyone on your engineering team actually reviewed our integration guide against your existing service?"
**Data to pull:** whether a customer engineer (not just the champion) has signed off on the estimate before it's written into the success criteria.
