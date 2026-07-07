# Courier and Messenger — Playbook

## Route sequencing: earliest-deadline-first (EDD)

Given a set of stops, some with hard delivery windows:

1. Separate stops into hard-window (has a deadline) and flexible (no deadline).
2. Order hard-window stops by deadline, earliest first.
3. Insert flexible stops into the gaps between hard-window stops where drive time allows, preferring to minimize total added distance.
4. Walk the full sequence with drive-time estimates; compute arrival time at each stop.
5. Any stop where computed arrival > deadline is a conflict — resolve before departure:
   - Resequence if a different order closes the gap.
   - Split the route across two couriers if resequencing can't close it.
   - Notify the recipient/sender of an unavoidable delay and get authorization to proceed late, or to reschedule.

**Filled example — 4 stops, 9:00 AM start:**

| Stop | Deadline | Drive time from prior stop | EDD arrival | Margin |
|---|---|---|---|---|
| Depot → A | 9:20 | 18 min | 9:18 | +2 min |
| A → B | 9:50 | 15 min | 9:33 | +17 min |
| B → C | 10:30 | 18 min | 9:51 | +39 min |
| C → D | 11:00 | 22 min | 10:13 | +47 min |

Nearest-neighbor (distance-first) on the same stops would have sequenced B before A (B is 12 min from depot vs A's 18 min), producing a 9:27 arrival at A against its 9:20 deadline — a 7-minute miss. EDD sequencing avoids this because it protects the tightest deadline first regardless of distance.

## Proof-of-delivery selection by item type

| Item type | Required proof | Fallback if recipient unavailable |
|---|---|---|
| Subpoena / legal process | Personal signature or witnessed refusal, per jurisdiction's process-service rules | Follow the specific statute's substituted-service procedure — do not improvise |
| Medical specimen | Chain-of-custody log: timestamp + signature at every hand-off | Cold-chain items: do not leave unattended: return to depot or transfer to another courier with a logged hand-off |
| Signature-required parcel | Named-recipient signature | Sender's documented fallback (redeliver, hold at facility, return) — check manifest before defaulting to "leave with neighbor" |
| Standard parcel | Delivery confirmation (photo or scan) | Leave per standard delivery instructions; log as delivered-unattended |

## Delivery-exception handling

1. Attempt delivery per the manifest's specified method.
2. If unsuccessful, classify the exception: refused, no-answer, wrong-address, damaged-in-transit, access-denied (locked building/gate).
3. Check the manifest for a sender-specified fallback for that exception type.
4. If no fallback is specified, do not improvise — hold the item and flag to dispatch for sender instruction before proceeding.
5. Log the attempt: timestamp, exception type, any evidence (photo of locked gate, note left).
6. If a reattempt is authorized, note the new attempt window and resequence remaining stops around it.

**Filled exception log entry:**

> Stop D (Item #8842, signature-required parcel): Attempted 10:05 AM, no answer. No fallback specified on manifest. Held per default policy — not left unattended. Flagged to dispatch for sender instruction. Photo of door taken as attempt evidence.

## End-of-route reconciliation

Every item on the manifest must close with one of: delivered (with proof type logged), exception (with type and evidence logged), or returned-to-depot. An item with no closing status at end of route is treated as a possible loss-in-transit and escalated immediately, not carried over silently to the next shift.
