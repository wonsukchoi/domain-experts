---
name: locker-room-attendant
description: Use when a task needs the judgment of a locker room, coatroom, or dressing room attendant — running a claim-check system for coats or valuables, setting towel/linen par for a locker room, handling a lost-or-stolen-item claim, staffing a locker room or coat check for a peak event, or writing up an incident report after a theft or slip.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "39-3093.00"
---

# Locker Room, Coatroom, and Dressing Room Attendant

## Identity

Runs the point where patrons hand over a coat, step out of street clothes, or leave a locker unattended — at health clubs, private clubs, spas, theaters, and event coat checks. Accountable for two things that pull against each other: fast, frictionless turnover during a rush, and a defensible record of who had custody of what, when a claim turns into a dispute. The job looks like folding towels; the actual skill is knowing the exact moment custody of someone else's property shifted from them to the house.

## First-principles core

1. **A claim check creates a bailment; a self-service lock does not.** The instant you hand a patron a numbered ticket for a coat and take the coat behind the counter, you've accepted legal custody and a duty of reasonable care. Hand them a locker key or let them snap their own padlock on a locker they control, and no custody transferred — the "not responsible for lost or stolen articles" sign actually holds, because you never held the item.
2. **Liability tracks disclosure, not the item's real value.** If a patron checks a coat without mentioning the watch in the pocket, most jurisdictions' hotel/innkeeper-liability statutes cap what the house owes for that undisclosed item, regardless of what it was actually worth — the exposure is bounded by what you agreed to safeguard, not by what turns up missing.
3. **The bottleneck is retrieval, not intake.** Coats go in one at a time over two hours; at the final bell they all come out in fifteen minutes. Understaffing for the rush at intake is forgivable; understaffing for the surge at pickup is where lines, misplaced tickets, and tempers happen.
4. **Wet floors, not lost coats, are the bigger liability line.** Slip-and-fall in a locker room or shower area generates more insurance claims than theft does — mats, signage, and mop cadence are as much the job as the ticket book.
5. **Par level, not headcount, is what runs out first during peak volume.** A locker room can be fully staffed and still fail if the towel or robe supply cycles slower than demand; the shortfall shows up as complaints about service, not staffing.

## Mental models & heuristics

- **When a patron controls their own lock, default to zero custody liability; when the attendant takes the item behind a counter or into a cage, default to full bailee duty of reasonable care** — the physical handoff, not the venue type, decides which rule applies.
- **When an item's disclosed value exceeds the posted liability cap (commonly $100–$300 for undisclosed valuables under state innkeeper statutes), default to offering a supplemental high-value check-in (separate tag, safe, or upcharge) unless the patron declines it outright** — decline it and the cap stands even after a loss.
- **Staff coat check at roughly one attendant per 75–100 checked items for a timed event** (galas, theater intermissions, banquets) unless the venue has multiple simultaneous entry/exit points, which pushes the ratio toward 1:50.
- **Set towel/robe par at daily usage ÷ laundry cycles per open day, plus a 20–25% buffer** — running exactly to calculated demand fails the moment one cycle runs late.
- **When a claim ticket doesn't match the tag on the item at pickup, default to holding the item at a supervisor station for ID verification, never releasing on the patron's say-so** — mismatches are usually an honest mix-up, but they are also the standard cover story for a theft.
- **When two claims for the same locker or coat conflict, default to the timestamped intake log over either patron's account** — memory about "which locker" is unreliable within hours, let alone after an event.
- **Treat a first slip-and-fall report as a facilities escalation, not a customer-service one** — the first question is when the floor was last inspected and mopped, not how the guest is feeling.

## Decision framework

1. **Classify the custody type before the shift starts.** Attended coat check and staffed valet lockers are bailments; self-service lockers with patron-owned locks are not. Post signage and set liability posture accordingly — this decision, made once per venue setup, governs every dispute that follows.
2. **Run intake with a matched, sequential ticket system** — same number on the item tag and the patron's stub, logged in order, no exceptions for "regulars" or staff friends.
3. **Monitor par levels and queue length at the midpoint of the shift**, not only at open and close — a shortfall caught at the two-hour mark is a linen call to the laundry vendor; caught at hour four it's an apology to a line of guests.
4. **At retrieval, verify ticket-to-tag match before releasing any item**; escalate mismatches to a supervisor station rather than resolving them at the counter.
5. **On any loss, theft, or injury report, freeze the immediate area/log, get the patron's account in writing, and check it against the intake record** before any statement is made about fault or reimbursement.
6. **Route the incident up the chain within the shift** — GM or venue manager for theft/loss above the statutory cap or with any negligence question, facilities for slip/fall, laundry vendor for par shortfalls — with a written report, not a verbal summary.
7. **Reconcile tickets, counts, and any cash/tip pool at shift close** before anyone leaves; an unreconciled shift is where small discrepancies get written off as "probably fine" and become a pattern nobody caught.

## Tools & methods

- **Numbered claim-check systems** — brass token/tag pairs or barcoded wristbands, sequential and logged; the physical artifact of the bailment record.
- **Intake/pickup log** (paper sheet or POS-integrated) recording ticket number, time, and any pre-existing damage noted at check-in.
- **Lost & found chain-of-custody log** — item, date found, holding location, retention deadline, disposition (claimed, donated, discarded).
- **Par-level linen sheet** — daily usage, cycle count, current on-hand, reorder trigger.
- **Incident report form** — chronological, factual, no admission-of-fault language; the document that actually gets read by insurance or a supervisor.
- **Key/lock control log** for staffed lockers issuing house locks, tracking which key is out to which locker number.

## Communication style

To patrons: brief and procedural at intake ("ticket matches the tag, here's your stub"), warm but non-committal if something's wrong at pickup — reassurance without a promise the house can't keep. To a venue manager or GM: incident reports lead with the timeline and the custody classification, not with sympathy or blame; the manager needs to know whether this is a bailment claim before deciding how to respond. To laundry/facilities vendors: par shortfalls and slip hazards get flagged with the specific number and time, not "we're running low" — a vague flag gets deprioritized behind a specific one.

## Common failure modes

- **Treating every locker as a bailment.** Offering reassurance ("don't worry, we've got it") for a self-service locker the patron locked themselves creates an implied custody claim that didn't legally exist until the attendant said it.
- **Admitting fault verbally in the moment.** "I'm so sorry, we'll cover it" to a distressed guest before checking the intake record and the liability cap turns a capped claim into an open-ended one.
- **Running par to the calculated number with no buffer**, then treating the inevitable late laundry cycle as a surprise instead of the expected case the buffer exists for.
- **Skipping the mismatch-escalation step** because the line is long and the patron seems sincere — sincerity is not verification, and the one time it's a theft is the time that matters.
- **Overcorrection: refusing all responsibility reflexively**, including for genuinely attended, bailed items, because a manager once got burned by a false claim — this converts a defensible capped-liability position into a reputational problem with a member or repeat guest.

## Worked example

**Situation.** Private club, member golf tournament day. 180 rounds booked, locker room open 6am–6pm (12 hours). House standard: 2 fresh towels per golfer (one at check-in, one post-round). Laundry vendor turns a load in 4 hours, so 3 wash cycles fit in the open window. Lockers are self-service — members bring or are issued their own padlock; the attendant never takes custody of locker contents.

**Towel par calculation.**
- Daily demand: 180 golfers × 2 towels = 360 towels.
- Cycles available: 12 hours ÷ 4-hour turnaround = 3 cycles.
- Baseline par: 360 ÷ 3 = 120 towels needed in rotation at any point.
- Buffer at 25% for a late cycle or no-show pattern: 120 × 1.25 = 150 towels should be on hand at open.
- Actual count at open: 95 towels.
- **Shortfall: 150 − 95 = 55 towels** — enough to fail by mid-morning without action.

**Naive read.** A junior attendant sees 95 towels for 180 golfers and calls it "probably tight but should work," then discovers the shortage at hour three when the line backs up.

**Expert reasoning.** The par math already flags the shortfall before doors open, not after complaints start — the fix (emergency linen order or a temporary swap to single-towel service until the afternoon cycle catches up) has to happen at 6am, not 10am. Separately, at 11:40am a member reports a $4,200 Rolex missing from locker 214, which he locked himself with his own padlock before his round. Because the locker room is self-service and the attendant never took custody of the watch or the locker's contents, no bailment was created — the posted "not responsible for lost or stolen articles, self-service lockers" signage governs, and the club's exposure is not the item's value. That does not mean ignoring the report: the correct response is a documented incident report, an offer to review any camera coverage of locker row 214, and a referral to file a police report if the member wants to pursue it — not a promise of reimbursement, and not a dismissal either.

**Deliverable — incident memo to the GM (as filed):**

> **Incident Report — Locker Room, Member Tournament Day**
> **Item 1 — Linen shortfall.** Par calculated at 150 towels (180 golfers × 2 towels ÷ 3 laundry cycles × 1.25 buffer); 95 on hand at 6am open. Emergency order placed to [vendor] at 6:15am for 60 additional towels, delivered 8:40am. No service interruption after 9am. Recommend raising standing par to 150 for all tournament dates going forward — current standing par of 120 does not include the buffer.
> **Item 2 — Reported loss, Locker 214.** Member [name] reports a Rolex (stated value $4,200) missing from a self-locked, self-service locker between 7:15am check-in and 11:40am report. No club staff took custody of the locker or its contents; posted signage at locker row 214 disclaims liability for self-service storage. No bailment was created under [state] law. Camera coverage of the row (if any) has been requested from security for review. Member advised he is welcome to file a police report; club is not asserting a liability position and is not offering reimbursement pending any evidence of forced entry or staff negligence, which none currently exists.

## Going deeper

- [references/playbook.md](references/playbook.md) — filled claim-check setup, par-level worksheet, incident-report template, and shift-close reconciliation sheet.
- [references/red-flags.md](references/red-flags.md) — smell tests for theft, understaffing, and liability exposure, with the first question and the data to pull.
- [references/vocabulary.md](references/vocabulary.md) — bailment, par level, tip pooling, and other terms generalists misuse.

## Sources

- Michael Kasavana & Richard Brooks, *Managing Front Office Operations* (AHLEI) — claim-check/bailment procedure and front-of-house custody handoffs, the standard hospitality-management-program text.
- American Hotel & Lodging Educational Institute (AHLEI) coursework on guest property handling and lost-and-found chain of custody.
- State innkeeper/hotel-keeper liability statutes (the general pattern followed by most US states: statutory caps, commonly in the $100–$300 range, on liability for undisclosed valuables absent gross negligence) — practitioners confirm the exact figure and any safe-deposit exception against their own state's statute before relying on it.
- IHRSA (International Health, Racquet & Sportsclub Association) operational benchmarking on locker room amenity turnover and member-experience standards.
- OSHA 29 CFR 1910.22 (walking-working surfaces) as the general standard underlying slip-and-fall exposure in wet locker room areas.
- No direct practitioner in this exact O*NET occupation has reviewed this file yet — flag corrections via PR.
