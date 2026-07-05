# Artifacts & templates

Filled examples an agent can populate or execute against. Load this when producing an actual funnel analysis, deviation report, or consent checklist — not for general reasoning (that's `SKILL.md`).

## Enrollment funnel worksheet

```
Study: [protocol #]              Target: 60 enrolled              Window: 6 months, month 4 status

Stage                    | Count | % of prior stage | Protocol assumption | Variance
--------------------------|-------|-------------------|----------------------|----------
Referrals received        | 340   | —                 | ~300 by month 4      | +13% (ahead)
Screened                  | 210   | 62%               | ~65%                 | -3pts (in line)
Found eligible             | 48    | 23%               | ~40%                 | -17pts (BOTTLENECK)
Consented & enrolled       | 22    | 46%               | ~85%                 | -39pts (also check)

Screen-fail reason breakdown (of 162 screened-ineligible):
  [Specific lab-value criterion]: 71 (44%) — vs. ~20% expected -> investigate criterion interpretation
  Other exclusion criteria: 91 (56%) — in line with expectation

Next step: escalate specific criterion question to PI/medical monitor, NOT generic outreach increase.
```

## Protocol deviation report (short form)

```
Study: [protocol #]              Participant ID: [ID]              Date of deviation: [date]

Deviation description: [what happened, specifically]
Protocol section deviated from: [reference]
Immediate safety impact: [none / assessed, describe]
Was this deviation preventable: [Y/N, brief reasoning]

Reported to:
  [ ] Principal Investigator — date: ______
  [ ] IRB — date: ______ (per study's reporting timeline requirement)
  [ ] Sponsor — date: ______

Corrective action taken: [describe]
Preventive action to avoid recurrence: [describe]

NOTE: report regardless of how minor this seems — the reporting system, not the coordinator's own
judgment in the moment, is what determines significance.
```

## Consent re-confirmation checklist (trigger-based, not just at enrollment)

```
Participant: [ID]                    Trigger event: [protocol amendment #X / new safety info / N months elapsed]

Re-confirmation conversation completed: [date]
Key points re-confirmed:
  [ ] Participant understands what has changed (if amendment) or new information (if safety update)
  [ ] Participant's willingness to continue re-confirmed, not assumed from prior consent
  [ ] Questions addressed: [note any raised]
  [ ] Updated consent form signed if required by amendment: [Y/N, date]

Documentation location: [note where this is filed in the study record — must be traceable]
```
