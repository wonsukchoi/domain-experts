# Insurance Claims and Policy Processing Clerk — Playbook

## Intake completeness checklist (homeowners property claim)

| Field | Required? | Status | Action if missing |
|---|---|---|---|
| Policy number | Yes | ✅ Complete | — |
| Named insured matches policy | Yes | ✅ Complete | — |
| Date of loss within policy period | Yes | ✅ Complete | — |
| Loss location | Yes | ✅ Complete | — |
| Cause-of-loss code | Yes | ✅ Complete | — |
| Loss description narrative | Yes | ✅ Complete | — |
| Photos (minimum 4) | Yes | ⚠️ 2 of 4 | Request remaining 2, same-day |
| Contractor/mitigation estimate | Yes | ❌ Missing | Request, same-day, 5-business-day window |
| Prior-claims history on address | System-pulled | ✅ Complete | — |
| Contact preference | Yes | ✅ Complete | — |
| Correspondence mailing address | Yes | ✅ Complete | — |
| Signed proof-of-loss statement | Yes, state-mandated window | ❌ Missing | Request immediately — flag filing-window deadline |

**Rule:** any field tied to a statutory or policy deadline (proof-of-loss, notice-of-loss timing) gets flagged even if the rest of the file looks routine — the deadline runs from date of loss, not from when the file is reviewed.

## Endorsement-processing worksheet

| Step | Check | Example |
|---|---|---|
| 1. Confirm request source | Policyholder, agent, or underwriter-initiated | Policyholder requesting coverage-limit increase |
| 2. Confirm policy is active | Effective dates bracket the request date | Policy active 2024-01-01 to 2025-01-01; request dated 2024-06-15 ✅ |
| 3. Cross-check open claims | Any claim open on this policy? | Query claims system for policy number |
| 4. If open claim exists | Confirm endorsement effective date is AFTER the claim's date of loss, unless the endorsement is explicitly retroactive and approved as such | Open claim, date of loss 2024-06-10; endorsement requested effective 2024-06-15 — endorsement effective date is after date of loss, proceeds without conflict |
| 5. Process and confirm | Written confirmation to policyholder with new effective date and changed terms | "Your coverage limit for [peril] has been increased from $X to $Y, effective [date]." |

**The trap:** an endorsement effective *before* an open claim's date of loss, if processed without catching this, can appear to retroactively grant coverage that wasn't in force at the time of loss — this is a coverage dispute waiting to happen, not a processing formality.

## Code-validation reference table (cause-of-loss vs. narrative consistency)

| Cause-of-loss code | Narrative should mention | Mismatch example | Action |
|---|---|---|---|
| Burst pipe / plumbing failure | Water source inside structure, pipe/fixture failure | Narrative describes storm/roof leak instead | Clarifying question: "Please confirm the water source — the narrative describes a roof/storm-related leak, but the code submitted is for internal plumbing failure." |
| Wind/hail | Weather event, exterior damage (roof, siding, windows) | Narrative describes interior water damage only, no exterior mention | Clarifying question: confirm cause and request exterior damage documentation |
| Theft | Forced entry or unauthorized access, missing property list | Narrative describes property "misplaced," no forced-entry mention | Clarifying question: confirm whether this is a theft claim or a different loss type |
| Fire | Combustion event, smoke/heat damage | Narrative describes water damage only | Clarifying question: confirm cause-of-loss code matches the described event |

**Rule:** a mismatch is a routing signal, not a denial recommendation — this role documents the inconsistency and asks the clarifying question; the adjuster decides what it means.
