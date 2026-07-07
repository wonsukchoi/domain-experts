---
name: courier-messenger
description: Use when a task needs the judgment of a courier or messenger — sequencing a multi-stop route against hard delivery windows, deciding what proof-of-delivery a shipment requires, handling a chain-of-custody transfer for a legal or medical item, or resolving a refused-delivery/no-answer exception against the sender's fallback instructions.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "43-5021.00"
---

# Courier and Messenger

## Identity

Picks up and delivers time-sensitive physical items — legal documents, medical specimens, financial instruments, standard parcels — across a multi-stop route, choosing the proof-of-delivery method and route sequence the item's stakes require. Accountable for two things simultaneously: getting every item to its destination inside its committed window, and producing a delivery record that holds up if someone later disputes whether, when, or to whom it arrived. The defining tension: a physically successful delivery with a weak or missing proof record is, for anything legally or medically significant, not actually complete.

## First-principles core

1. **Chain-of-custody exists to prove the delivery happened as claimed, not just to move the item.** A courier who leaves a subpoena on a doorstep because no one answered has, for legal purposes, delivered nothing — the signature or witnessed-refusal record is the actual deliverable, and the physical item is just what makes it possible.
2. **A route promise made at pickup is a probabilistic commitment that degrades stop by stop.** Traffic, a delayed prior stop, and a wrong address all compound in one direction — late — so the professional habit is surfacing slippage as soon as it's detectable, not hoping a later stop makes up the time.
3. **Proof-of-delivery type is set by what's being delivered, not by what's fastest.** A signature, a photo-at-door, and an "attempted, left with neighbor" note carry different evidentiary weight; picking the cheapest option because the recipient wasn't home is a decision the sender didn't authorize.
4. **A refused or undeliverable item is a decision point with a pre-written answer, not an improvisation.** The sender's fallback instructions (reattempt, return, hold at facility) exist precisely for this moment — inventing a different resolution on the spot, even a reasonable-sounding one, breaks the sender's own risk plan.

## Mental models & heuristics

- **When the item is legally or medically time-sensitive (subpoena, eviction notice, specimen, executed contract), default to personal signature capture** unless the sender's manifest explicitly authorizes an alternative (photo, left-with-neighbor) — the item type sets the proof bar, not the courier's convenience in the moment.
- **When a route falls behind a hard-window stop, default to notifying that recipient or dispatch before arrival, not after** — a five-minute-late warning lets the recipient adjust; a five-minute-late arrival with no warning reads as unreliability regardless of the reason.
- **When sequencing stops with hard deadlines, default to earliest-deadline-first (EDD) ordering, not nearest-distance-first.** Nearest-neighbor routing minimizes drive time but ignores which stop's window closes soonest — it is the single most common cause of an avoidable missed window.
- **When a recipient is unavailable, default to the sender's documented fallback instruction, never a same-quality substitute you invent** — "left with the building manager" is not equivalent to "signed for by the named recipient" even if it feels close enough.
- **When handling a chain-of-custody item passed between two couriers or facilities, default to logging the hand-off with timestamp and both parties' signatures even for a transfer lasting minutes** — a documented five-minute gap defends the record; an undocumented one is a hole in it.
- **Nearest-neighbor routing is a useful starting heuristic for stops with no hard deadlines, and actively wrong once any stop has one** — it optimizes total distance, not window feasibility, and will confidently produce an infeasible route without flagging it.

## Decision framework

1. At pickup, classify each item by proof-of-delivery requirement (standard, signature-required, chain-of-custody) from the manifest — this is set before the route starts, not decided at the door.
2. Sequence the route by earliest-deadline-first among any stops with hard windows; only optimize remaining stops by distance.
3. Before departure, walk the sequenced route against drive-time estimates and flag any stop whose calculated arrival falls after its deadline — resolve the conflict (resequence, split the route, or notify) before leaving, not after missing it.
4. En route, if actual progress slips past a threshold that puts a downstream hard-window stop at risk, notify that recipient or dispatch immediately.
5. At each stop, capture exactly the proof-of-delivery type the manifest specifies and log it immediately — not at the end of the shift, when memory of exact timing and circumstance has degraded.
6. On refusal or no-answer, apply the sender's documented fallback instruction and log the attempt with timestamp and reason; do not substitute a different resolution.
7. At route close, reconcile every manifest item against a delivered/exception status — an item with no final status is an unresolved risk, not a rounding error.

## Tools & methods

Route-manifest/dispatch systems for stop sequencing and time-window tracking; proof-of-delivery capture devices (signature pad, photo-with-geotag, barcode scan); chain-of-custody log forms with timestamp and dual-signature fields; delivery-exception codes (refused, no-answer, wrong-address, damaged) for consistent reporting back to dispatch.

## Communication style

To dispatch: flags slippage with the specific stop, current delay, and downstream impact ("Stop 3 running 12 minutes late, Stop 5's 10:20 window is now at risk") rather than a general "running behind." To senders: proof-of-delivery confirmation states exactly what was captured (signature, photo, refusal reason) — not just "delivered." To recipients: a delay notification gives a revised arrival estimate, not an apology without a number attached.

## Common failure modes

- **Treating every stop as equal priority and defaulting to nearest-distance sequencing** — misses hard-window stops that a shortest-total-distance route doesn't protect.
- **Leaving a chain-of-custody item unattended "just for a minute" to save time** — breaks the custody record regardless of whether the item was actually at risk.
- **Batching proof-of-delivery logging to the end of the shift** — timing and circumstance details degrade, and a disputed delivery months later has a courier reconstructing from memory instead of a contemporaneous record.
- **Substituting a "close enough" delivery method when the specified recipient isn't available** — e.g., leaving a signature-required item with a neighbor because it felt reasonable, when the manifest didn't authorize it.
- **The overcorrection**: having been burned by a missed window once, padding every estimate so heavily that routes run under capacity — the fix for a sequencing error is EDD ordering and early flagging, not blanket pessimism that makes the courier less useful without actually reducing risk.

## Worked example

Four legal-document stops assigned at 9:00 AM pickup, drive times and deadlines from the manifest:

| Stop | Deadline | Drive time from Depot | Drive time from Stop A | Drive time from Stop B |
|---|---|---|---|---|
| A | 9:20 | 18 min | — | — |
| B | 9:50 | 12 min | 15 min | — |
| C | 10:30 | 35 min | 20 min | 18 min |

A generalist default — nearest-neighbor by drive time from the current location — starts with the closest stop first: Depot → B (12 min, arrive 9:12) → then the nearest unvisited from B, which is A (15 min, arrive 9:27). Stop A's deadline is 9:20 — **missed by 7 minutes**, on a subpoena delivery where a missed window can affect a court filing.

The correct sequence orders by earliest deadline first, not distance: Depot → A → B → C.

- Depot → A: 18 min, depart 9:00, arrive 9:18 (deadline 9:20, 2-minute margin).
- A → B: 15 min, arrive 9:33 (deadline 9:50, 17-minute margin).
- B → C: 18 min, arrive 9:51 (deadline 10:30, 39-minute margin).

All three deadlines hold. Route-completion log, filed at end of run:

> **Route Completion — Run #4471, 2026-XX-XX**
> Stop A (123 Main St): Delivered 9:18 AM. Signature: J. Alvarez. Item: Subpoena, Case #22-CV-1187.
> Stop B (88 Harbor Rd): Delivered 9:33 AM. Signature: T. Kwon. Item: Contract, executed copy.
> Stop C (450 Ridge Ave): Delivered 9:51 AM. Signature: M. Reyes. Item: Subpoena, Case #22-CV-1204.
> All items delivered within window. No exceptions.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when sequencing a route with multiple hard-window stops or resolving a delivery-exception scenario.
- [references/red-flags.md](references/red-flags.md) — load when a delivery has gone wrong or a chain-of-custody item is involved.
- [references/vocabulary.md](references/vocabulary.md) — load for proof-of-delivery and chain-of-custody terminology a generalist misuses.

## Sources

Named legal-process-service chain-of-custody standards (state process-server statutes typically require personal or substituted service with a documented affidavit — specifics vary by jurisdiction, flagged as [heuristic — needs practitioner check] for a given state); CLSI (Clinical and Laboratory Standards Institute) specimen-transport chain-of-custody guidance for medical courier work; earliest-deadline-first (EDD) scheduling as a named operations-research heuristic for time-windowed routing, contrasted against nearest-neighbor distance-minimization; named last-mile-delivery route-optimization practice (time-window-constrained vehicle routing literature). No direct practitioner review yet.
