# Physical/corporate security working vocabulary

Terms a security manager uses precisely. Format: definition → how a practitioner says it → common misuse.

**Defense in depth (layered security)** — Deploying multiple independent security layers (perimeter, access control, monitoring, response) so that a failure or bypass of any single layer doesn't collapse the whole system, as opposed to relying on one strong control.
In use: "Even though the badge system failed here, the monitoring layer and response plan are independent — that's defense in depth working as designed."
Misuse: relying on one strong control (a good lock, a single guard, one camera system) as if it were sufficient on its own, creating a single point of failure an adversary only has to defeat once.

**Deterrence, detection, delay, response** — The four functions any security control should be evaluated against; a control that contributes to none of them is not providing real security value regardless of its cost or visibility.
In use: "Cameras primarily contribute to detection and response, not delay or deterrence for a determined actor — that's why they weren't the right fix for an access-control failure."
Misuse: evaluating a control purely on cost or visible reassurance without checking which of the four functions it actually serves, risking investment in "security theater."

**Security theater** — A control that's visible and reassuring but doesn't meaningfully raise attacker cost or improve detection, or that's so burdensome it gets routinely bypassed — worse than no control because it creates false confidence.
In use: "The badge reader on that side door is security theater — it's propped open every day because it's the smoking-break exit."
Misuse: assuming any visible security measure is providing real protective value without checking whether it's actually complied with or whether it meaningfully affects an adversary's cost or detection risk.

**Threat model** — The specific, context-dependent set of plausible adversaries and scenarios relevant to a given facility or organization (opportunistic theft, insider threat, workplace violence, targeted intrusion), used to select controls rather than applying a generic security checklist.
In use: "Our threat model here is dominated by opportunistic theft and insider access misuse, not targeted intrusion — that shapes where we invest."
Misuse: deploying a generic, one-size-fits-all security package without threat-modeling the specific context, over-investing in irrelevant controls while under-investing in the actual relevant risks.

**Insider threat** — Security risk originating from people who already have legitimate access (current or recently departed employees, contractors), a category that perimeter-focused controls (cameras, badge readers at entry points) systematically underweight.
In use: "This incident traced to a stale contractor badge — that's an insider-threat/access-review gap, not a perimeter failure."
Misuse: building elaborate perimeter defenses (cameras, fencing, entry badges) while neglecting access review and behavioral risk monitoring for people who already have legitimate access, missing a major real-world incident category.

**Access review (least privilege)** — The periodic process of checking active access grants against current legitimate need, removing access that's outlived its justification (a departed employee's badge, an expired vendor's access), as distinct from a one-time provisioning check at onboarding.
In use: "The access review found 34 stale active badges from people who departed an average of 62 days ago — that's the gap this incident traces to."
Misuse: treating access provisioning as a one-time event at hire/contract start, with no periodic review that catches access that should have been revoked after a departure or role change.

**Tabletop exercise** — A structured, discussion-based drill simulating a security incident to test a response plan's actual effectiveness before relying on it in a real event, as distinct from a written plan that's never been exercised.
In use: "The tabletop exercise revealed the escalation contact list was three roles out of date — better to find that in a drill than during a real incident."
Misuse: treating a written, unrehearsed incident response plan as reliable without testing it, missing gaps that only surface under simulated (or worse, real) time pressure.

**Residual risk** — The risk that remains after security controls are applied, which is never zero — an honest security program frames decisions in terms of acceptable residual risk and cost-benefit, not a false promise of absolute protection.
In use: "Even with these controls, some residual risk remains — the question for leadership is whether this level is acceptable given the cost of further reduction."
Misuse: presenting a security investment as eliminating risk entirely, rather than honestly framing it as reducing risk to an acceptable, cost-justified residual level.

**Access-control failure vs. detection failure** — Distinguishing whether an incident occurred because someone gained access they shouldn't have had (access-control failure) versus because the incident wasn't caught in time despite being visible (detection failure) — different failure modes requiring different fixes.
In use: "This was an access-control failure — a valid but stale badge got someone in. A camera wouldn't have prevented that; it might have helped catch it faster, but that's a different layer."
Misuse: treating every incident as if it calls for the same category of fix (e.g., always adding more cameras) without diagnosing which specific layer actually failed.

**Adversarial risk (vs. accidental/operational risk)** — Risk arising from an actor deliberately trying to defeat controls (theft, intrusion, sabotage), which requires reasoning about adaptive, intentional behavior — a different discipline than managing accidental failure or operational risk.
In use: "This isn't like an equipment failure risk — we have to assume an adversary will actively look for the gap, including ones we haven't thought of yet."
Misuse: applying the same risk-assessment logic used for accidental/operational failures (which don't actively seek out control weaknesses) to adversarial risk, missing that a deliberate actor will specifically probe for and exploit gaps.
