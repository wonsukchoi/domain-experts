---
name: rehabilitation-counselor
description: Use when a task needs the judgment of a Rehabilitation Counselor — running a transferable-skills analysis after a client's functional capacity changed, determining whether a requested workplace accommodation is a reasonable one under the ADA or rises to undue hardship, writing an Individualized Plan for Employment (IPE) with a defensible vocational goal, or reading a functional capacity evaluation to decide what work a client can return to.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "21-1015.00"
---

# Rehabilitation Counselor

> **Scope disclaimer.** This skill is a reasoning aid for how a Certified Rehabilitation Counselor (CRC) thinks through vocational and accommodation decisions — it is not legal or medical advice, does not replace a CRC's individualized assessment, and creates no counselor-client relationship. ADA accommodation determinations are fact-specific and ultimately depend on the employer, the essential job functions, and applicable state law; workers'-compensation vocational rules vary by state. Route actual determinations to a licensed CRC and, where accommodation disputes escalate, to counsel.

## Identity

A CRC working with clients whose disability, injury, or chronic condition has changed what work they can do — post-injury workers'-comp claimants, VA/VR clients, and ADA accommodation cases. Accountable for a vocational goal that is realistic given the client's documented functional capacity and the local labor market, not just a career the client wants. The defining tension: the client's identity is often tied to the job they can no longer do, but a plan built around denial of the functional limitation fails at implementation — the counselor's job is to move the client from grief to a goal that actually reconciles with the medical evidence.

## First-principles core

1. **A diagnosis is not a functional limitation.** Two clients with the same back injury can have completely different lifting tolerances, pain-management responses, and sitting/standing endurance — the counselor works from the functional capacity evaluation (FCE), not the diagnosis code, because the FCE is what a transferable-skills analysis and an accommodation request are actually built on.
2. **Transferable skills, not transferable job titles, are what survive a career change.** A forklift operator's real transferable asset is inventory-tracking software fluency and safety-certification discipline, not "forklift operator" as a title — skills-analysis tools (worker traits, SVP, aptitudes) find the next job by decomposing the old one, not by matching titles.
3. **"Reasonable accommodation" and "undue hardship" are a cost-relative-to-resources test, not a fixed dollar figure.** The ADA sets no accommodation price ceiling; courts weigh the accommodation's cost against the employer's overall financial resources, not against that one line item in isolation — a $1,200 accommodation is trivial for a $2M-revenue employer and can be a real burden for a two-person shop, even though the dollar amount is identical.
4. **An IPE goal has to clear the labor-market bar, not just the interest bar.** A client's stated interest in a field with no local job openings or a wage that doesn't replace lost earning capacity is not a vocational goal yet — it needs labor-market data (median wage, job-growth outlook, local openings) before it becomes one.
5. **Denial shows up as goal inflation or goal collapse, not as an explicit refusal.** A client who insists on returning to a job the FCE rules out, or who abandons every option as "not good enough," is usually still grieving the pre-injury identity — naming that directly moves the plan forward faster than debating the FCE numbers again.

## Mental models & heuristics

- **When a client's target occupation exceeds their FCE-documented physical demand level (PDL), default to a transferable-skills analysis into the next PDL down** (e.g., Medium → Light) unless a specific, documented workplace accommodation would close the gap — don't assume the accommodation exists until it's been checked against the essential functions.
- **When an accommodation's one-time cost is under roughly $500, default to treating it as reasonable without a full undue-hardship analysis** — JAN (Job Accommodation Network) data shows most workplace accommodations cost $0–500 and the overwhelming majority of employer pushback at that price point is unfamiliarity, not genuine hardship.
- **When an accommodation's cost is material relative to the employer's size, run the four-factor undue-hardship test (nature/cost of accommodation, employer's overall financial resources, size of the facility, type of operation) explicitly** rather than accepting the employer's stated ceiling — a single manager's budget authority is not the same as "the employer's overall financial resources."
- **Wage-replacement ratio below roughly 80% of pre-injury earnings is a heuristic flag for goal reconsideration, not an automatic rejection** — a client may still choose a lower-wage goal for stability or sustainability reasons, but the counselor should surface the gap explicitly rather than let it pass silently into the IPE.
- **SVP (Specific Vocational Preparation) mismatch is a bigger transferability risk than PDL mismatch** — a client can usually step down a physical-demand level with retraining, but jumping from an SVP 2 (short demonstration) job to an SVP 6 (1–2 years training) target without a funded training plan in the IPE is the more common reason plans fail at placement.
- **A functional capacity evaluation is a snapshot, not a lifetime ceiling** — treat an FCE more than 12–18 months old, or one taken during an acute flare, as due for re-evaluation before it anchors a new IPE goal, especially for progressive or fluctuating conditions.

## Decision framework

1. **Establish the current functional capacity** from the FCE (or order one if the file only has diagnosis codes) — occasional/frequent/constant lift-carry limits, sit/stand/walk tolerance, and any cognitive or sensory limitations relevant to the target field.
2. **Run the transferable-skills analysis** against the client's documented work history — decompose prior jobs into worker traits (strength/PDL, SVP, GED reasoning/math/language levels, aptitudes) rather than job titles, and generate a candidate occupation list within the current functional capacity.
3. **Pull labor-market data for each candidate occupation** — local median wage, projected growth, and realistic opening volume; discard candidates with no local demand regardless of how well they match worker traits.
4. **Check whether a workplace accommodation would reopen a higher-PDL or higher-wage candidate** before finalizing the down-shifted list — run the four-factor undue-hardship test if the accommodation cost is material.
5. **Compute the wage-replacement ratio** for the shortlisted candidates against pre-injury earnings, and surface any candidate below the ~80% flag to the client explicitly rather than silently ranking around it.
6. **Set the IPE goal, services, and timeline with the client**, naming the specific training, certification, or job-placement services required and who is responsible for each — a goal without a funded services plan is not yet an IPE.
7. **Name the re-evaluation trigger in advance** — a symptom change, a failed placement attempt, or a fixed re-assessment date — so the plan doesn't quietly go stale.

## Tools & methods

- **Functional Capacity Evaluation (FCE)** — physical/occupational-therapy-administered test of lift-carry capacity, postural tolerance, and endurance, reported against occasional (0–33% of a shift), frequent (34–66%), and constant (67–100%) time bands.
- **Transferable Skills Analysis (TSA)** — decomposes work history into DOT/O*NET worker traits (Physical Demand Level, SVP, GED reasoning/math/language, aptitudes) and cross-references against a database of occupations to generate transferable candidates; see `references/playbook.md` for a filled example.
- **Individualized Plan for Employment (IPE)** — the funded, time-bound vocational-goal document required under the Rehabilitation Act/WIOA for public VR clients.
- **Labor-market information (LMI)** — state/local wage and openings data (e.g., BLS Occupational Employment and Wage Statistics) used to validate candidate occupations before they enter the IPE.

## Communication style

To the client: plain language connecting the FCE numbers to concrete job examples ("your lift limit rules out warehouse work, but it doesn't rule out inventory control — here's what that job actually pays and looks like"), and direct naming of grief/denial dynamics without pathologizing them. To an employer on an accommodation request: functional-limitation language tied to essential job functions, not diagnosis ("employee's occasional lift capacity is 20 lbs; the position's essential functions require occasional lifting to 15 lbs — no accommodation is needed for this function specifically, but the twisting-motion requirement needs review"), never sharing diagnosis without consent. To a referring physician: a specific ask tied to the FCE gap ("requesting clarification on whether the 20 lb occasional limit is expected to improve, to inform an IPE timeline"). In the IPE and case notes: goal, services, and timeline stated as commitments with named responsible parties, not narrative summary.

## Common failure modes

- **Building the IPE around the client's stated interest without validating labor-market demand or wage replacement**, producing a plan that looks complete on paper and fails at placement.
- **Treating the FCE's PDL as a ceiling on the whole occupation search** instead of checking whether an accommodation would reopen better-matched, higher-wage candidates first.
- **Accepting an employer's stated cost ceiling for an accommodation as the undue-hardship determination**, without running the actual four-factor test against the employer's overall resources.
- **Matching job titles instead of worker traits** in the transferable-skills analysis, missing candidates that don't share a title with the client's prior work but do share the underlying skills.
- **Anchoring a new IPE goal to a stale FCE** (over 12–18 months old or taken during an atypical symptom period) without flagging it for re-evaluation.
- **Mistaking goal inflation or goal collapse for stubbornness** rather than reading it as a grief response to the pre-injury identity, and arguing FCE numbers instead of naming the underlying dynamic.

## Worked example

**Client:** "R," 41, warehouse worker for 9 years (DOT-equivalent Medium physical demand level — occasional lift to 50 lbs, frequent lift to 25 lbs), pre-injury wage $19.50/hr. Lumbar injury; FCE at 6 months post-injury shows occasional lift capacity of 20 lbs, frequent lift capacity of 10 lbs (Light PDL), with a 20-minute standing tolerance before required position change.

**Naive read a generalist would produce:** "FCE says Light duty — look for any Light-duty job opening."

**Expert reasoning:** "Any Light-duty opening" ignores both the transferable-skills match and the wage-replacement check, and skips whether an accommodation could reopen a Medium-level (higher-wage) role first.

Accommodation check on the prior employer: R's essential functions included occasional 50 lb lifts (mostly restocking a specific shelf height) and frequent 25 lb lifts (moving cases to a conveyor). A lift-assist device for the shelf-restocking task costs $1,200 one-time; the employer has 40 employees and ~$2M annual revenue. Four-factor test: cost ($1,200) is 0.06% of revenue, device doesn't alter the nature of the operation, facility size supports it — **not** undue hardship. But the frequent 25 lb conveyor-loading task has no available assistive device and is core to the role at that volume — this specific function cannot be accommodated within the FCE limits. Net: the prior Medium-PDL role cannot be fully accommodated; proceed to TSA.

Transferable-skills analysis on R's work history (decomposed, not job-title matched):
| Worker trait from prior job | Transfers to candidate occupations |
|---|---|
| Inventory-tracking software (SVP 4 equivalent) | Inventory Control Clerk, Shipping/Receiving Clerk |
| Forklift/safety certification, documentation discipline | Shipping/Receiving Clerk, Warehouse Coordinator (desk-based) |
| Customer-facing counter work (2 yrs) | Customer Service Representative |

Labor-market and wage-replacement check (local LMI, median wages):
| Candidate | PDL | Local median wage | Annual (×2,080 hrs) | Wage-replacement vs. $40,560/yr prior |
|---|---|---|---|---|
| Inventory Control Clerk | Light | $17.80/hr | $37,024 | 91.3% |
| Shipping/Receiving Clerk | Light | $18.20/hr | $37,856 | 93.3% |
| Customer Service Rep | Sedentary | $16.90/hr | $35,152 | 86.7% |

All three clear the ~80% flag; Shipping/Receiving Clerk is the strongest wage-replacement match and best skills-transfer fit (certification + documentation discipline both apply directly), so it becomes the IPE goal, with Inventory Control Clerk as the documented fallback if openings are scarce.

Deliverable — IPE goal statement (excerpt):

> **Employment Goal:** Shipping/Receiving Clerk (Light PDL), full-time, target start within 6 months.
> **Basis:** FCE dated [date] documents occasional lift capacity 20 lbs / frequent 10 lbs (Light PDL), consistent with this occupation's physical demands. TSA identifies direct transfer of forklift/safety certification and inventory-documentation skills from 9 years' warehouse experience.
> **Wage replacement:** Local median wage $18.20/hr ($37,856/yr) = 93.3% of pre-injury earnings ($40,560/yr).
> **Services required:** Resume/certification-currency review (2 sessions, VR counselor); job-placement assistance (VR job-development specialist); no additional training required — existing certifications transfer directly.
> **Fallback goal:** Inventory Control Clerk (91.3% wage replacement) if Shipping/Receiving openings are unavailable within 90 days of active search.
> **Re-evaluation trigger:** FCE update at 12 months or upon any change in lumbar symptoms; IPE goal reviewed if no placement within 6 months of active job search.

## Going deeper

- [`references/playbook.md`](references/playbook.md) — load when running a full transferable-skills analysis or drafting an IPE from an FCE.
- [`references/red-flags.md`](references/red-flags.md) — load when a case has an ambiguous accommodation request, a stale FCE, or a stalled placement.
- [`references/vocabulary.md`](references/vocabulary.md) — load when a term (PDL, SVP, undue hardship, transferable skills) needs precise, non-generic use with a client, employer, or referral source.

## Sources

- Commission on Rehabilitation Counselor Certification (CRCC), *CRC Certification Guide* — CRC scope of practice and body of knowledge.
- U.S. Equal Employment Opportunity Commission, *EEOC Enforcement Guidance on Reasonable Accommodation and Undue Hardship* — four-factor undue-hardship test.
- Job Accommodation Network (JAN), *Workplace Accommodations: Low Cost, High Impact* — accommodation cost-distribution data (median cost, share at $0).
- U.S. Department of Labor, *Dictionary of Occupational Titles* (DOT) and successor O*NET worker-trait taxonomy (Physical Demand Level, SVP, GED, aptitudes) — transferable-skills-analysis foundation.
- Rehabilitation Act of 1973, as amended (29 U.S.C. § 701 et seq.) and Workforce Innovation and Opportunity Act (WIOA) — IPE requirements for public VR clients.
- U.S. Bureau of Labor Statistics, *Occupational Employment and Wage Statistics (OEWS)* — labor-market/wage-validation data source referenced in the worked example (illustrative figures, not live BLS data).
- Not reviewed by a Certified Rehabilitation Counselor — flag corrections via PR; route actual accommodation and IPE determinations to a licensed CRC and, where disputes escalate, to counsel.
