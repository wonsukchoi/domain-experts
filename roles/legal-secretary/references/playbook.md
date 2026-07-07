# Legal Secretary — Playbook

## Conflicts-check workflow (filled)

**Step 1 — Extract every name from the intake form.**

| Role on new matter | Name |
|---|---|
| Prospective client | Meridian Fabrication LLC |
| Adverse party | Coastal Steel Supply |
| Key witness | Dana Reyes |
| Related entity (client's parent co.) | Meridian Holdings Inc. |

**Step 2 — Run each name against the firm-wide conflicts database (current clients, former clients, adverse parties on other matters, related entities).**

| Name | Search result | Conflict type | Action |
|---|---|---|---|
| Meridian Fabrication LLC | No match | — | None |
| Coastal Steel Supply | Match: former client of R. Nakamura, matter closed 14 mo ago | Rule 1.9 (former client) | Attorney determination: substantially related? If no — disclose to former counsel + document, then clear. If yes — matter is barred absent informed consent. |
| Dana Reyes | Match: current client of T. Okafor, unrelated matter | Informational only | Flag for awareness, no action |
| Meridian Holdings Inc. | No match | — | None |

**Step 3 — Log the result in the conflicts database regardless of outcome** (a "checked, clear" entry is as important as a "checked, flagged" entry for the firm's audit trail).

**Step 4 — Do not open the matter file until every flagged item has a documented resolution.**

## E-filing rejection troubleshooting (filled)

| Rejection reason | How it shows up | Fix |
|---|---|---|
| PDF/A non-compliance | System error: "document does not meet PDF/A-1b standard" | Re-export from the source application using the court's specified PDF/A profile — do not just "print to PDF," since many print-to-PDF outputs are not PDF/A-compliant by default |
| File size over limit | System error: "file exceeds maximum size of [X] MB" | Split into multiple filed documents per the court's multi-part filing convention, or reduce embedded-image resolution before re-export |
| Missing or malformed signature block | Clerk's office rejection notice after initial acceptance | Confirm the court's electronic-signature format (e.g., "/s/ Attorney Name") is present exactly as required, not just a scanned signature image where a typed format is required |
| Wrong event type selected | Filing accepted but flagged by clerk as miscategorized | Cross-check the event-type taxonomy against the document type before submission — when unsure, call the clerk's office rather than guess, since a miscategorized filing can be treated as not filed for deadline purposes in some jurisdictions |
| Missing required attachment (e.g., proposed order) | System rejects the filing as incomplete | Confirm the full required-attachment list for that motion type against the local rules before starting the submission, not after a rejection |

**Escalation trigger:** if a rejection occurs within 2 hours of a filing deadline and the fix isn't immediately clear, escalate to the supervising attorney immediately rather than continuing to troubleshoot alone — a missed deadline from unescalated troubleshooting is a worse outcome than an attorney being pulled in early.

## Multi-party deposition scheduling (filled)

**Constraint list, ordered hardest-to-easiest:**

1. Out-of-state expert witness — available only two specific weeks this quarter
2. Court reporter — booked 3+ weeks out in this market
3. Opposing counsel — generally available with 2 weeks' notice
4. Supervising attorney — most flexible, can rearrange around the above

**Sequence:** confirm the witness's two available weeks first → confirm court-reporter availability within those weeks → propose 2-3 specific dates to opposing counsel within that intersection → confirm attorney's calendar last, since it's the easiest to move.

**Anti-pattern to avoid:** proposing a date based on the attorney's open calendar slot first, then discovering the expert witness isn't available that week — this forces a full re-negotiation with every other party who already confirmed.
