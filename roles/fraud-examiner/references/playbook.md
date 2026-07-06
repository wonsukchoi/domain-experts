# Fraud Examiner — Playbook

## Predication documentation checklist

1. What specific fact, tip, or anomaly triggered the concern? (Document verbatim if from a tip line or complaint.)
2. Is there a second, independent corroborating factor (e.g., a control-bypass pattern, a separately surfaced pressure indicator)?
3. Does the combination of facts give a reasonable, professional basis to believe fraud may have occurred — not just a general sense that something seems off?
4. Has this predication been documented in writing before any formal investigative step (interviews, record requests) begins?

**Use:** Never skip this step — an investigation opened without documented predication creates real legal exposure for the organization regardless of what the investigation eventually finds.

## Benford's Law analysis (filled example)

| Leading digit | Expected frequency (Benford's Law) | Observed frequency (this vendor's invoices) |
|---|---|---|
| 1 | 30.1% | 12% |
| 2 | 17.6% | 9% |
| ... | ... | ... |
| 9 | 4.6% | **22%** |

**Finding:** Leading digit "9" appears nearly 5x more often than expected — consistent with invoices deliberately structured just under a $10,000 approval threshold.

**Use:** Treat this as a lead requiring corroboration, not a standalone finding — pull the actual invoices behind the anomaly and check them against the vendor's registration and business legitimacy before drawing a conclusion.

## Loss quantification worksheet (filled example)

| Component | Value |
|---|---|
| Number of flagged invoices | 47 |
| Total value | $438,600 |
| Average invoice amount | $9,332 |
| Time period | 18 months |
| **Confirmed fraudulent payment total** | **$438,600** |

## Vendor/entity verification checklist

1. Check the vendor's registered business address against employee addresses in the organization's HR/personnel records.
2. Check state business registry for the vendor's actual registration status, ownership, and incorporation date.
3. Check for other verifiable customers or business activity beyond transactions with this organization.
4. Check who has vendor-master edit access and whether any independent review occurred at onboarding.

## Interview sequencing plan (illustrative structure)

| Order | Interview subject | Type | Purpose |
|---|---|---|---|
| 1 | AP clerks / process staff | Non-accusatory, informational | Establish who has vendor-master access, confirm process facts |
| 2 | Employee's supervisor | Non-accusatory, informational | Confirm oversight (or lack thereof) at vendor onboarding |
| 3 | Primary suspect | Admission-seeking | Conducted last, after evidence is fully gathered and corroborated |

**Use:** Never move the primary suspect interview earlier in this sequence — doing so risks destroyed records or a coordinated cover story before the evidence trail is secured.

## Findings and recommendation memo — filled example

> **Fraud Investigation Findings — [Case Ref]**
> Predication: Specific tip (employee, vendor, timeframe) corroborated by independently surfaced financial pressure indicator.
> Control gap: No segregation between vendor-master maintenance and invoice approval under $10,000 threshold.
> Analytical finding: Benford's Law leading-digit "9" frequency of 22% vs. expected 4.6%, consistent with threshold-splitting. 47 invoices, **$438,600 total confirmed fraudulent payments.**
> Vendor verification: Registered address matches employee's personal residence — confirmed shell entity.
> Admission obtained in sequenced interview process, following documentary corroboration.
> **Recommendation: Terminate employment, pursue civil restitution for $438,600, refer to law enforcement for criminal prosecution given documentary and admission evidence. Remediate by segregating vendor-master maintenance from invoice approval duties, removing the informal sub-threshold approval gap, and implementing periodic Benford's Law screening as an ongoing detective control.**
