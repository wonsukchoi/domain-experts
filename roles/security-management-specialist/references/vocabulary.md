# Working Vocabulary

### CARVER
A criticality/vulnerability scoring methodology (Criticality, Accessibility, Recoverability, Vulnerability, Effect, Recognizability) adapted from military targeting for corporate asset prioritization.
**In use:** "The data center scored 21 on CARVER — that's above our action threshold, it needs a dedicated control plan, not the standard building package."
**Common misuse:** Treated as a one-time exercise instead of a living reassessment; generalists score every asset a 4-5 across the board because nothing feels "unimportant," which flattens the ranking and defeats the point.

### Tailgating
Unauthorized entry by following an authorized badge-holder through a secured door without independently badging in.
**In use:** "Two tailgating events this quarter — both at the same corridor, both a held-door pattern, not a badge failure."
**Common misuse:** Confused with badge cloning or credential theft; tailgating is a human-behavior/door-discipline failure, not a technical one, so the fix is usually a mantrap or delayed-egress alarm, not better badges.

### Delayed egress alarm
A door-hardware control that sounds an alarm and delays release for a set interval (commonly 15-30 seconds) when someone attempts to exit through a secured door, deterring propping and unauthorized egress-assisted entry.
**In use:** "The mantrap alone won't stop a held-door pattern on exit — pair it with a delayed-egress alarm on that door."
**Common misuse:** Assumed to control entry; it's an exit-side control, and conflating the two leaves the entry vulnerability unaddressed.

### Insider threat
Risk originating from someone with authorized access (employee, contractor, vendor) misusing that access, as distinct from an external actor breaching perimeter controls.
**In use:** "Our insider-threat exposure is mostly in offboarding lag, not malicious intent — badges staying active past termination."
**Common misuse:** Assumed to mean malicious intent only; most insider-threat exposure in practice is negligent or process-driven (stale credentials, oversharing access), not deliberate.

### Threat-assessment team
A standing multidisciplinary group (typically security, HR, legal, EAP) that reviews reported behavioral-threat signals through a documented intake and tiering process, distinct from an ad hoc security response.
**In use:** "This gets routed to the threat-assessment team within 48 hours — security doesn't harden access unilaterally on a personnel case."
**Common misuse:** Conflated with a purely security-led response; the team's value is specifically the cross-functional check, and skipping HR/legal/EAP input creates both a missed intervention point and legal exposure.

### Executive protection tiering
A documented, exposure-based scoring system that determines the level of protective coverage assigned to an executive, ranging from standard awareness training to a full-time detail.
**In use:** "She moved from Tier 1 to Tier 2 the day the layoff announcement went out under her name."
**Common misuse:** Assigned by org-chart seniority instead of documented exposure, which both over-protects low-risk executives and under-protects high-exposure ones who don't hold the top title.

### Post order
A written, site-specific instruction set for a guard post covering duties, response protocols, and escalation contacts for that exact location.
**In use:** "Pull the loading-dock post order — does it actually specify a response time for a Tier-1 alarm, or just 'monitor the area'?"
**Common misuse:** Treated as generic boilerplate copied across posts; a post order that doesn't name specific response times and escalation contacts for its exact location isn't executable under pressure.

### Response time (Tier-1 / Tier-2)
The target elapsed time between an alarm or incident trigger and a guard physically arriving on scene, tiered by asset criticality.
**In use:** "We budget patrol density off the 4-minute Tier-1 target, not off a flat headcount number."
**Common misuse:** Confused with coverage hours (is someone on shift) rather than actual arrival speed — a post can be staffed 24/7 and still fail a response-time target if patrol routing is inefficient.

### Badge tiering by consequence
An access-control design principle assigning security level to a space based on the worst credible outcome if the control fails, not by convenience or organizational seniority.
**In use:** "The server room and the supply closet are on the same badge tier right now — that's a consequence-mapping failure, not a coincidence."
**Common misuse:** Designed instead around who's "important enough" to have broad access, which widens the blast radius of any single compromised credential.

### Residual risk
The risk that remains after a control is implemented, which should be explicitly stated rather than implied as "solved."
**In use:** "The mantrap closes the data-center gap; residual risk is tailgating at other entrances, which we'll re-score next quarter."
**Common misuse:** Omitted entirely from recommendations, leaving the reader to assume a control eliminates risk rather than reduces it to a stated, monitored level.

### Threat/exposure score
A documented, factor-based rating (public profile, controversy involvement, travel pattern, prior threats) used to size protective coverage, as distinct from an intuitive or title-based judgment.
**In use:** "His threat/exposure score didn't change, but hers did the moment the litigation named her personally."
**Common misuse:** Calculated once at hire or promotion and never revisited, even after events (public controversy, threats received) that should trigger a recalculation.
