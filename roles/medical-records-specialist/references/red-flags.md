# Red Flags

Smell tests for coding, CDI, ROI, and audit-response operations. Format per flag: what it usually means, the first question to ask, the data to pull.

### DNFB (Discharged Not Final Billed) exceeding 5 days facility average

- **Usually means:** either a documentation gap (missing signature, unresolved query) or a coder backlog, roughly in that order of frequency.
- **First question:** "Is this account waiting on a person (physician query, missing signature) or waiting on a queue (coder capacity)?"
- **Data to pull:** DNFB aging report broken out by hold reason (query pending, documentation incomplete, coder queue, edit failure).

### Facility Case Mix Index (CMI) up more than 5% month-over-month with flat volume and flat service mix

- **Usually means:** either a genuine documentation-improvement win or a query practice that has started leading — the two look identical on a CMI trend line.
- **First question:** "Pull the 10 highest-weight-change accounts this month — do the queries that drove them offer a closed option set, or do they name the diagnosis first?"
- **Data to pull:** query audit sample of the top CC/MCC-driving accounts, cross-referenced against the AHIMA/ACDIS compliant-query checklist.

### Coding accuracy below 95% on a 10-chart audit sample

- **Usually means:** training gap on a specific guideline area, or productivity-quota pressure pushing volume over accuracy.
- **First question:** "Are the errors clustered on one guideline (e.g., POA assignment, sequencing) or spread evenly across the sample?"
- **Data to pull:** the audit worksheet with error type tagged per chart, not just a pass/fail count.

### Query response rate under 80%, or queries aging past 2 business days unescalated

- **Usually means:** physician engagement gap, or the escalation path isn't actually being triggered.
- **First question:** "Which service line has the lowest response rate, and has anyone told that service chief the CMI/DNFB impact in dollars?"
- **Data to pull:** query response-rate report by attending/service line, plus the escalation log to check whether day-2 escalations are actually firing.

### ROI turnaround exceeding the state's statutory ceiling (often 15 business days, below HIPAA's 30-day outer limit)

- **Usually means:** ROI staffing backlog, or authorization-completeness rejections that aren't being caught until late in the queue.
- **First question:** "Is the delay in the intake/verification step or the actual pull-and-send step?"
- **Data to pull:** ROI request log with timestamps at each stage (received, authorization verified, pulled, sent).

### Master Patient Index (MPI) duplicate rate above 2%

- **Usually means:** registration isn't verifying identity consistently (no two-identifier check, no biometric/photo match), producing duplicate MRNs for the same patient.
- **First question:** "Are duplicates concentrated at one registration point (ED, one outpatient site) or system-wide?"
- **Data to pull:** MPI duplicate/overlay report by originating department, plus the registration identity-verification policy actually in force at that site.

### Modifier -59 (or -XE/-XS/-XP/-XU) usage rate spikes on a payer's post-payment review

- **Usually means:** unbundling — separately billing components of a bundled procedure — either a coding-software edit override pattern or a deliberate provider billing habit.
- **First question:** "Pull the NCCI edit pairs being overridden — is there a documented, medically necessary reason for each override, or is it a blanket modifier default?"
- **Data to pull:** claims report filtered to modifier -59 family usage, joined to the NCCI edit table it's overriding.

### RAC/payer ADR unaddressed past day 40 of the 45-day response window

- **Usually means:** the ADR tracking log isn't actually being monitored, or the requested records are harder to compile than expected (multi-facility chart, missing scan).
- **First question:** "What specifically is blocking compilation, and can it be escalated today rather than at day 45?"
- **Data to pull:** open ADR log sorted by days-remaining, with the blocking reason noted per account.

### Repeated amendment requests targeting the same provider's documentation

- **Usually means:** a documentation habit problem (vague templated notes, copy-forward errors) rather than a pattern of factual disputes — treating each as an isolated amendment misses the underlying fix.
- **First question:** "Across the last 5 amendment requests on this provider, is there a common note type or template involved?"
- **Data to pull:** amendment request log filtered by provider, with note type and template ID.

### A breach or disclosure involving 500 or more records

- **Usually means:** crosses the HITECH threshold requiring notification to HHS OCR within 60 days and, separately, notice to prominent media in the affected state/jurisdiction — smaller breaches have a longer, annual-aggregate reporting path instead.
- **First question:** "Has legal/compliance confirmed the exact count and the affected jurisdictions, before any notification clock is treated as started?"
- **Data to pull:** the breach risk assessment (the four-factor HIPAA analysis) and the confirmed affected-record count.

### A record on the destruction schedule also appears on the open litigation-hold list

- **Usually means:** the retention/destruction process and the legal-hold list aren't cross-checked before a destruction run — the single most common spoliation-risk failure in HIM operations.
- **First question:** "Has legal confirmed this record has no open hold before it goes into this destruction batch?"
- **Data to pull:** the litigation-hold list dated same-day as the destruction batch list, diffed against each other.
