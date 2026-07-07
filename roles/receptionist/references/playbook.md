# Receptionist — Playbook

## Call-triage priority table

| Situation | Priority | Action |
|---|---|---|
| Physical visitor at desk, no call ringing | 1 (immediate) | Greet, run badge/sign-in procedure |
| Physical visitor at desk + phone ringing | 1 (visitor first) | Acknowledge visitor verbally ("I'll be right with you"), let call route to voicemail or answer briefly to place on hold |
| Line ringing, no visitor present, no other line holding | 1 | Answer within 2-3 rings |
| Two lines ringing simultaneously | FIFO unless flagged | Answer the one queued longer, unless the other is a flagged VIP/emergency extension |
| Line holding 60-90+ seconds | Check-in required | Return to the line: "Still with me — [name] is finishing another call, one more minute okay?" |
| Known emergency/security line rings | Always priority 1 | Interrupts any in-progress call or visitor greeting |

## Badge / sign-in exception log

Use this format any time procedure is bent for a legitimate reason — creates an audit trail and a pattern-detection record.

```
Date/time: 2026-03-14 09:14
Visitor: [name], claimed appointment with "James" (ambiguous — two James on staff)
Action taken: held visitor at desk, called both James extensions, confirmed James O. (Finance)
Badge issued: yes, 09:16, escorted status: no (self-directed to Finance suite per James O.)
Exception: none — procedure followed, just took an extra 90 seconds to disambiguate
```

```
Date/time: 2026-03-14 14:02
Visitor: [name], no appointment, said "I'm just dropping something off for Sarah"
Action taken: declined to badge in; offered to hold the item at the desk for pickup
Badge issued: no
Exception: none — visitor left item, no access granted
```

## Escalation scripts

**Angry caller, valid complaint, needs a specific person:**
"I can hear this has been frustrating — I want to get you to someone who can actually fix this instead of explaining it twice. Let me get you to [name], one moment." (Then give the receiving person the gist before transferring, not after.)

**Visitor without appointment, insists it's urgent, no one confirms:**
"I'm not able to confirm an appointment on our end, so I can't send you back without that. I can leave a message for [name] right now if you'd like to give me your contact info — they'll be able to reach you directly." (Firm, not apologetic — the badge control isn't a judgment call to soften.)

**Caller who won't state their reason for calling ("just put me through"):**
"I do need at least a general reason to route you to the right person — I don't need details, just whether this is about billing, support, or something else." (One redirect attempt; if they still refuse, route to a general line/voicemail rather than guessing.)

## Daily handoff note (shift change)

```
Handoff — 2026-03-14, 5:00 PM shift change

Open items:
- Visitor "James O." meeting ran long — guest badge #14 not yet returned, flag at front desk if seen
- Line 2 call from ~2:00 PM (invoice complaint, no callback number left) — voicemail forwarded to accounting, no further action needed
- Badge printer low on cardstock — reorder submitted, expect Thursday

Nothing else outstanding.
```
