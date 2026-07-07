# Artifacts & templates

## Predicate comparison table

Filled example — OTC continuous glucose monitor, two predicate candidates:

| Attribute | New device | Predicate A (K210987) | Predicate B (K190456) |
|---|---|---|---|
| Intended use | General wellness glucose trend monitoring, adults 18+ | Same, OTC non-adjunctive | Adjunct to therapy, insulin dosing decisions |
| Risk category | Class II, special controls 21 CFR 862.1355 | Same | Higher — diagnostic use |
| Sensor chemistry | Enzymatic (glucose oxidase) | Same | Enzymatic, different membrane formulation |
| Read interval | 15 min | 15 min | 5 min |
| Cleared MARD | Target ≤9.2% | 9.2% | 7.8% (full range incl. hypoglycemic) |
| Clinical study size | 36 subjects, 2 sites (matches Predicate A track) | 36 subjects, 2 sites | 72 subjects, 4 sites |
| Verdict | — | **Selected** — matching intended use keeps evidence burden at the lighter track | Rejected — forces diagnostic-use evidence burden despite similar technology |

**Rule of thumb:** score every candidate on intended-use match first, technological-characteristics match second. A predicate that wins on technology but loses on intended use still forces the higher-risk evidence track.

## Regulatory strategy memo skeleton (filled)

```
TO: VP Product, VP Quality
FROM: Regulatory Affairs
RE: 510(k) Strategy — [Device Name]

RECOMMENDATION: File 510(k) against Predicate A (K210987), OTC non-adjunctive
CGM special-controls track (21 CFR 862.1355).

TESTING PLAN:
- Clinical: 36 subjects, 2 sites, per recognized consensus standard — $306,000
- Bench (ISO 10993 biocompatibility, EMC, wireless coexistence) — $180,000
- TOTAL: $486,000

TIMELINE: Submission month 0 → 1 AI cycle (typical for this track) →
clearance ~month 5.

CONDITION: Label and marketing claims must stay within "general wellness,
glucose trend monitoring." Any implied diagnostic or dosing claim moves
this device into Predicate B's risk category and voids this estimate.

OPEN GAPS (must close before RTA screen):
1. Wireless coexistence testing not yet scheduled — lab booked for
   submission minus 6 weeks.
2. Shelf-life stability data at 12 months pending — interim 6-month
   data supports filing; full data due before clearance decision point.

ALTERNATIVE CONSIDERED: Predicate B path — rejected. Diagnostic-use
evidence burden (72 subjects, 4 sites, + mandated PMS study) adds
$736,000 and 3-4 months with no label benefit for our target claim.
```

## RTA checklist excerpt (Class II 510(k), OTC device)

| # | Item | Status |
|---|---|---|
| 1 | Indications for use statement, FDA Form 3881 | Complete |
| 2 | 510(k) summary or statement | Complete |
| 3 | Truthful and accuracy statement | Complete |
| 4 | Class III summary and certification (if applicable) | N/A — Class II |
| 5 | Financial certification/disclosure (clinical study) | Complete |
| 6 | Declarations of conformity to recognized standards | **Missing — wireless coexistence standard not yet cited** |
| 7 | Substantial equivalence discussion (predicate comparison) | Complete |
| 8 | Performance testing summary (bench + clinical) | Complete |
| 9 | Labeling (draft) | Complete |
| 10 | Sterilization/shelf-life data (if applicable) | Interim data only — flag as risk |

**Rule:** one "Missing" row blocks submission. Run this screen internally before filing — an FDA RTA rejection resets the review clock to zero, unlike an AI request during substantive review, which only pauses it.

## AI-response tracker (filled example)

| AI Request # | Date issued | Question | Response due | Status |
|---|---|---|---|---|
| 1 | Day 60 | Provide bench data supporting wireless coexistence in 2.4GHz shared-spectrum environment | Day 180 (max) | Responded Day 45 with full test report — complete dataset, not partial |
| — | — | — | — | Clock resumed Day 46; no second AI cycle issued |

**Rule of thumb:** treat the response due date as a ceiling, not a target — respond with the complete literal dataset requested as soon as it's ready. A partial response "hoping they get the idea" is the most common cause of a second AI cycle, typically adding another 60-180 days.

## Change-control decision (letter to file vs. new submission)

Fallback order when a post-clearance device change occurs:

1. **Could the change significantly affect safety or effectiveness?** (per FDA's 2017 decision tree — check intended use, technological characteristics, performance specs, and labeling.) If yes → new submission.
2. **If no, does the change affect a previously cleared performance claim's supporting data?** If yes → new submission or a supplement, depending on region.
3. **If no to both, document as a letter to file** — includes the change description, the risk-assessment rationale, and sign-off from Quality and Regulatory Affairs jointly, not Regulatory Affairs alone.

Document the outcome every time, including "no new submission needed" — an inspector years later will ask why a specific change didn't trigger one, and "we didn't think about it" is not an answer that holds up.
