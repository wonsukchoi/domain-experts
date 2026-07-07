# Aviation Inspector — Playbook

## Dual-threshold AD compliance check (filled example)

| Step | Value |
|---|---|
| AD interval, flight-hour leg | 800 hrs |
| AD interval, calendar leg | 24 months |
| Governing rule | Whichever occurs first |
| Total time at last compliance | 14,220.0 hrs |
| Current total time | 15,062.4 hrs |
| Hours elapsed since compliance | 15,062.4 − 14,220.0 = 842.4 hrs |
| Hour-leg status | 842.4 − 800 = 42.4 hrs over (842.4 / 800 = 105.3% of interval) |
| Calendar elapsed since compliance | 19 months |
| Calendar-leg status | 19 / 24 = 79.2% of interval — inside window |
| **Result** | Non-compliant. Hour leg crossed 42.4 hrs ago; calendar leg being inside its window does not offset a crossed hour leg under "whichever occurs first." |

**Use:** Evaluate both legs independently and take the worse of the two — never average them or let the more favorable leg substitute for the other. A record that looks fine on one column and doesn't get checked on the other is the single most common way a dual-threshold AD goes undetected.

## Fleet records-sampling stratification (filled example, 14-aircraft fleet)

| Stratum | Selection rule | Why this stratum | Aircraft selected (of 14) |
|---|---|---|---|
| Highest utilization | Top 2 tails by flight hours in the last 12 months | Fastest to cross an hour-based threshold | N601MA, N603MA |
| Recent records-custody change | Tails whose maintenance tracking moved to a new system/vendor within the surveillance cycle | Migrations are where hour/calendar logic gets dropped or miscoded | N612MA, N618MA |
| Prior discrepancy history | Tails with any open or recently closed discrepancy from the last 2 surveillance cycles | Repeat-offender aircraft are statistically likelier to recur | (none this cycle — none flagged) |
| Blind random | 1 tail chosen without regard to the above criteria | Tests whether the targeted strata are catching what a truly random pick would also catch, and prevents the sample from becoming predictable to the operator | N609MA |
| **Total sampled** | | | 5 of 14 (36%) |

**Use:** A sample built only from the "easy" or newest records systematically misses exactly the aircraft most likely to carry a defect — recent custody changes and high utilization are where dual-threshold tracking errors actually surface. The blind random pick exists so a certificate holder can't learn the sampling pattern and stage compliant records for the tails it can predict will be checked.

## Compliance-and-enforcement ladder (per FAA Order 2150.3 compliance philosophy)

| Rung | What it is | Criteria to land here | Example instrument |
|---|---|---|---|
| 1. Compliance action | Root-cause corrective action, no punitive record | First-time, inadvertent, operator's culture supports self-correction, no concealment | Corrective training, process fix verified by the inspector, no formal notice |
| 2. Administrative action | Formal record, non-punitive | Inadvertent but caught by FAA (not self-disclosed) with a documented isolated or systemic-but-correctable cause, no recurrence on this certificate | Warning Notice (lesser) or Letter of Correction (more substantive, requires verified corrective action) |
| 3. Legal enforcement action — civil penalty | Monetary penalty under 49 U.S.C. § 46301 | Reckless or intentional deviation, concealment, or recurrence after a prior Letter of Correction for the same or a closely related finding | Civil penalty order; statutory caps adjusted periodically for inflation — verify current figures before citing a specific dollar amount |
| 4. Legal enforcement action — certificate action | Suspension or revocation of the operating certificate or airman certificate | Egregious, repeated, or safety-critical violation where continued operation under the certificate presents an unacceptable risk | Notice of Proposed Certificate Action; suspension (time-limited) or revocation (permanent, new application required) |

**Use:** Movement up the ladder is driven by intent and recurrence, not by the size of the underlying paperwork or maintenance gap — a large but genuinely inadvertent first-time finding with a documented systemic cause still lands at rung 1 or 2; a small but repeated or concealed finding still escalates to rung 3 or 4. Recording a finding at the wrong rung either lets a real pattern go unenforced or punishes the transparent operator, both of which erode the incentive structure the ladder depends on.

## VDRP/ASAP disclosure eligibility check

| Question | If yes | If no |
|---|---|---|
| Was the deviation disclosed to the FAA before any FAA inspection, investigation, or enforcement action related to it began? | Continue eligibility review | **Ineligible** — proceed as an FAA-discovered finding regardless of subsequent disclosure |
| Is the disclosure complete (all known instances, not just the one FAA might already suspect)? | Continue eligibility review | Ineligible — partial disclosure does not qualify |
| Has the certificate holder implemented or committed to a corrective action addressing the root cause? | Eligible for VDRP treatment (typically no civil penalty) | Corrective action required before closing under VDRP |

**Use:** Timing relative to FAA discovery is the entire test on the first question — a certificate holder that discloses five minutes after an inspector opens a records review on the same item does not qualify, no matter how forthcoming the disclosure is once made.

## SMS audit — four-pillar scoring (illustrative, per 14 CFR Part 5 structure)

| Pillar | What's audited | Passing signal | Finding-severity trigger |
|---|---|---|---|
| Safety Policy | Documented safety objectives, accountable executive authority, non-punitive reporting policy | Policy exists, is current, and is demonstrably known by line staff (not just filed) | Policy exists on paper but line staff can't describe the non-punitive reporting commitment in their own words |
| Safety Risk Management (SRM) | Hazard identification and risk assessment process, applied to actual operational changes | Recent operational changes (new route, new aircraft type, vendor change) show a documented SRM assessment before implementation | A hazard report or operational change with no documented risk assessment, or one completed after the change was already implemented |
| Safety Assurance | Performance monitoring, internal audit, corrective action tracking, management review | Safety metrics are tracked, reviewed on a defined cadence, and corrective actions from audits are closed with evidence | A safety metric trending the wrong direction for 2 or more consecutive quarters with no documented management review or response |
| Safety Promotion | Training, communication of lessons learned, safety culture reinforcement | Training records current; hazard/incident lessons demonstrably communicated back to line staff | Training current on paper but staff interviews show no awareness of a recent safety-relevant incident or its lessons |

**Use:** A pillar audit that only checks whether the required document exists (policy on file, training records current) misses the actual test, which is whether the pillar is functioning as a detection mechanism. A hazard report closed without a risk assessment is not a documentation gap — it's evidence the Safety Risk Management pillar didn't do the one thing it exists to do.
