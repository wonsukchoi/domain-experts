# Document Management Playbook

## Retention schedule matrix (filled example — general corporate)

| Record series | Retention trigger | Retention period | Authority | Disposal method |
|---|---|---|---|---|
| Signed customer contracts | Contract end date | 7 years post-expiration | State UCC statute of limitations (contracts) | Certificate of destruction |
| Employee personnel files | Termination date | 7 years post-termination | EEOC recordkeeping + state wage/hour statutes | Certificate of destruction |
| Tax filings & supporting docs | Filing date | 7 years | IRS record retention guidance | Certificate of destruction |
| Board minutes & corporate resolutions | Creation | Permanent | Corporate governance requirement | Never disposed |
| General business correspondence | Creation | 3 years | Business-need default (no statute) | Standard disposal |
| Accident/incident reports (workplace) | Incident date | 5 years | OSHA 29 CFR 1904.33 | Certificate of destruction |
| Marketing/promotional drafts | Superseded | 1 year post-supersession | Business-need default | Standard disposal |

## ROT audit worksheet (filled example)

Population: departmental file share, 42,000 files, no prior classification.

| Category | Definition | Sample finding | Count | % |
|---|---|---|---|---|
| Redundant | Duplicate of a record already classified elsewhere | Multiple copies of same contract in 6 folders | 6,300 | 15.0% |
| Obsolete | Superseded version, expired policy, deprecated template | Policy docs replaced ≥2 revisions ago | 8,820 | 21.0% |
| Trivial | Personal files, test uploads, no business record value | "test.docx", meeting-invite screenshots | 1,680 | 4.0% |
| **Total ROT** | | | **16,800** | **40.0%** |
| Retain (active/permanent) | | | 25,200 | 60.0% |

Sampling method: stratified random sample of 5% (2,100 files) manually reviewed by folder path; ROT rate applied to full population; full-population automated rule pass (filename/duplicate-hash matching) run before disposal to confirm sample rate holds outside the 5% (target: within ±3 points of sample estimate before proceeding to disposal sign-off).

## Migration wave reconciliation template

For each wave, before proceeding to the next:

```
Wave: [N]
Source count (this wave):        [X]
Migrated successfully:            [Y]
Exceptions logged:                [X - Y]
Exception rate:                   [(X-Y)/X %]
Exception root causes:
  - Checksum/corrupt source:      [count]
  - Metadata mapping failure:     [count]
  - Permission/ACL failure:       [count]
  - Other (specify):              [count]
Hash-sample validated (n, % of wave): [n / % ]
Remediation status:               [all remediated / N open, ETA]
GATE: proceed to next wave only if remediation status = "all remediated"
```

Fallback position if exception rate exceeds 2% on any wave: halt subsequent waves, escalate to platform vendor support, do not proceed until root cause identified — a rising exception rate across waves indicates a systemic crosswalk or source-corruption issue, not isolated noise.

## Legal hold vs. retention schedule conflict resolution

1. On hold notice receipt, identify custodians and content scope (date range, matter keywords, specific folders/repositories).
2. Flag all in-scope content with a hold marker in metadata — this must suppress any automated disposition rule regardless of the item's underlying retention classification.
3. Cross-reference the hold scope against any disposal queue already staged; pull matching items out before execution.
4. On hold release notice (from legal, in writing — never assume expiration), remove the hold marker and allow the item to resume its normal retention/disposition path.
5. Fallback if hold scope is ambiguous (e.g., "all contracts with Acme"): default to the broader interpretation and confirm with legal before narrowing — under-preservation risk outweighs the storage cost of over-preservation during an active hold.
