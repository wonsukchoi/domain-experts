# Public Safety Telecommunicator — Playbook

## Determinant-code reference (illustrative — exact card content is protocol-specific)

| Tier | Example trigger | Response posture |
|---|---|---|
| Omega | Minor complaint, no acute distress described (e.g. finger laceration, controlled) | Non-emergency guidance, lowest-priority response or referral |
| Alpha | Stable but symptomatic (e.g. isolated vomiting, no other red flags) | Routine-priority unit response |
| Bravo | Moderate acuity, one concerning finding (e.g. persistent abdominal pain with a cardiac-risk history) | Elevated-priority response |
| Charlie | Serious, specific finding (e.g. chest pain in a patient over 35 with prior cardiac history) | ALS-level response |
| Delta | Serious and unstable-trending (e.g. difficulty breathing with visible distress) | ALS response, closest available unit |
| Echo | Immediately life-threatening (e.g. confirmed not breathing, active arrest) | Highest-priority response, concurrent pre-arrival instructions |

Card selection starts from the caller's Chief Complaint in their own words, then Key Questions narrow to a specific tier. When two tiers are plausible from the same complaint, take the higher one until a specific answer rules it out.

## Concurrent-dispatch timing checklist

1. **0:00–0:15** — Answer, capture callback number + rough location, get the one-line nature of the call.
2. **0:15–0:30** — Confirm or correct displayed location against caller's description.
3. **0:15–0:45** — Work Key Questions toward a determinant code; escalate the moment an answer reveals higher acuity.
4. **At determinant-code moment** — Transmit for dispatch immediately, regardless of how much of the script remains.
5. **After transmission** — Continue pre-arrival instructions and background questions (history, medications, bystander count) concurrently while units are en route.
6. **On call end** — Log dispatch timestamp, determinant code, and any deviation with a stated reason.

Do not treat step 3's remaining unanswered questions as a reason to delay step 4 once the determinant code is reachable.

## Location-verification script

When displayed location and caller description don't obviously match:

> "I want to make sure units go to the right place — can you confirm the address you're at right now, not where this phone is registered to?"

For a wireless call with no confirmed street address:

> "Can you see a street sign, a building number, or a nearby landmark you can describe?"

For a VoIP call with a registered location that seems stale (subscriber moved, or caller describes a different city):

> "The system shows [registered address] — is that where you are right now, or has this number moved since it was set up?"

Never dispatch to a displayed address the caller has not confirmed when any inconsistency is present, even if it costs 10-15 seconds to ask.

## Sample callback-attempt log (call dropped mid-interview)

> **Case #4488 — Call Dropped, Callback Attempted**
> Call answered 00:00:00. Caller reported "someone broke into my house, I think they're still—" — call disconnected 00:00:22, mid-sentence.
> Callback attempted 00:00:24: no answer, forwarded to voicemail.
> Callback attempted again 00:00:55: no answer.
> Escalated per policy: dispatched a welfare-check unit to last-known/confirmed location based on partial information captured before disconnect (address confirmed at 00:00:10, before drop). Case not closed until unit reports scene status.
