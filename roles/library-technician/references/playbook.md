# Playbook

Filled templates for the three recurring end-to-end processes: copy-cataloging match decisions, the interlibrary loan (ILL) lifecycle, and serials claiming.

## Copy-cataloging match decision

Run this against every candidate OCLC/WorldCat record before attaching local holdings.

| Field checked | MARC tag | Match required? | If mismatched |
|---|---|---|---|
| ISBN | 020 | Yes, exact | Wrong edition/printing — reject, keep searching |
| Pagination | 300 | Within ±2 pp. | >2 pp. off with no edition statement (250) — treat as unresolved, don't guess |
| Edition statement | 250 | Yes, if present on either record | Conflicting edition statements — pick the one matching the item's title page, not the shorter record |
| Publisher/date | 264/260 | Same publisher, same or adjacent year | Different publisher — almost certainly a different edition, reject |
| Encoding level | Leader/17 | Accept blank, 1, 4 | 3, 5, 7, 8 (abbreviated/partial/prepublication/minimal) acceptable only if 020+300+250 all match cleanly |
| Subject headings | 6xx | At least one present | None present — flag for librarian even if all other fields match |

**Decision order:** ISBN exact match is the gate — no ISBN match, no further checks matter, keep searching or escalate. Given ISBN match, pagination and edition statement decide between duplicate records. Given a single clean survivor, encoding level and subject-heading presence decide accept-as-is vs. accept-with-local-edit vs. escalate.

**Escalate to librarian when:** no OCLC record exists at all (self-published, very small press, non-English rare item), or two+ records survive the pagination/edition check with no tiebreaker field to use.

## Interlibrary loan (ILL) lifecycle

**Borrowing (patron needs an item this library doesn't hold):**

| Stage | Target turnaround | Action if missed |
|---|---|---|
| Request submitted → routed to lending partners | Same day | — |
| First lending library responds | 1–2 business days | If no response in 3 days, route to next partner in rotation |
| Item ships | 3–5 business days from acceptance | If a rush need was flagged, check for an express/reciprocal partner before day 3 |
| Item received, checked in, patron notified | Same day as receipt | — |
| Standard loan period | 4–6 weeks, renewable once unless recalled | Recall from lending library takes priority over local renewal |

**Rush escalation rule:** if remaining time before the patron's stated need date is less than half of the realistic turnaround above, don't wait out the standard rotation — check a rush/express partner or a reciprocal-consortium option in parallel with the first request, not after it stalls.

**Lending (another library needs an item this library holds):**

| Stage | Target turnaround | Action if missed |
|---|---|---|
| Request received, item pulled from shelf | Same day | If not on shelf (checked out/missing), decline within 24 hrs, don't let it sit |
| Item shipped | 1–2 business days | — |
| Fee reconciliation (OCLC IFM) | Monthly batch | Reconcile transaction count against IFM statement before it posts to accounting; a mismatch of even 2–3 transactions in a 40-transaction month is worth a line-by-line check, not a shrug |

**Example month-end IFM reconciliation:** local ILL log shows 42 completed lends for the month. OCLC IFM statement bills 39 transactions. Difference of 3: check for (a) reciprocal/no-charge partners not billed under IFM — accounts for 2 of the 3 — and (b) one transaction logged locally as "completed" but still marked "in transit" on OCLC's side, meaning it hasn't triggered billing yet. Net: statement is correct; local log needed one status correction, not a dispute with OCLC.

## Serials claim schedule

| Days past expected arrival | Status | Action |
|---|---|---|
| 0–14 | Normal mail/processing variance | No action |
| 15–44 | Late but pre-claim window | Log as "watching"; no claim filed yet |
| 45–60 | Claim-eligible | File first claim this week — don't wait for a second missed date to "confirm" |
| 60–90 | Claim outstanding | Follow up with vendor if no response to first claim within 30 days |
| 90–120 | Free-replacement window closing | Escalate to acquisitions librarian for a paid backfill decision before the window shuts |
| 120+ | Window closed at most vendors | Backfill (if wanted) is now a paid reorder, not a claim |

**Rule of thumb:** treat day 45 as the trigger, not day 60 — a claim filed early costs nothing if the issue turns up in the mail the next day; a claim filed late can cost the replacement entirely.
