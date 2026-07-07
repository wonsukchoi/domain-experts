# Playbook

Filled tables and worksheets for triaging across ATM, PC, and copier/MFP calls under contracted SLA time pressure.

## 1. SLA tier table (typical multi-vendor field-service contract)

| Tier | Equipment class | Response window | Resolution window | Coverage | Typical penalty for miss |
|---|---|---|---|---|---|
| Tier 1 — Critical | Branch/on-premise ATM, core banking PC | 2 hours | 4 hours | 24×7 | $500/incident + service-credit escalation past 3/month |
| Tier 2 — Standard | Off-premise/retail ATM, office copier/MFP | 4 hours | Next business day (NBD) | 8×5 (M–F) | Service credit, ~5% of monthly fee per breach |
| Tier 3 — Best-effort | Individual PC/workstation break-fix | Same or next business day | 3 business days | 8×5 (M–F) | Reputational only, no contractual credit |

Response clock stops at "technician on-site, ticket acknowledged in system." Resolution clock stops at "fault verified cleared, functional test passed, ticket closed." The two are scored independently — hitting response and missing resolution is still a full breach.

## 2. MTTR / MTBF targets by equipment class (fleet-review baseline)

| Equipment | Target MTTR | Typical MTBF (based on duty cycle) | PM interval |
|---|---|---|---|
| ATM cash dispenser (high-transaction branch) | ≤ 2.5 hrs | ~25,000 notes dispensed between reseat-worthy jams | 25,000 notes or 90 days, whichever first |
| ATM card reader / PIN pad | ≤ 2.0 hrs | ~18–24 months between failures | Annual firmware/cleaning cycle |
| Office copier/MFP (mid-volume, ~20k pages/mo) | ≤ 4 hrs on-site, NBD resolution | ~100,000–150,000 impressions between hardware-level failures | Every 100,000 impressions or 90 days |
| PC/workstation (business desktop) | ≤ 1 business day | ~3–5 years between hardware failures outside drive/battery wear | No fixed PM; imaging/patch cycle substitutes |

Availability = MTBF ÷ (MTBF + MTTR). A dispenser at 25,000-note MTBF and 2.5-hour MTTR sustains ~99.99% device availability at that transaction rate — the number that matters to the contract is availability, not either input alone. A fleet showing flat or improving MTTR alongside falling MTBF is not improving; it's absorbing more frequent failures with faster response, which is a maintenance-plan problem, not a dispatch-efficiency win.

## 3. Triage decision tree by machine class

**ATM (cash-handling):**
1. Pull error code + dispense-cycle counter + PM-interval position.
2. Code ambiguous between procedural and mechanical? → check counter position first.
   - Inside PM interval (< target notes/days) → default to procedural cause (bin full, jam clear, cassette misseat). Open under two-person integrity, reseal, test.
   - At or past PM interval → check go/no-go wear gauge on the implicated part.
     - Within OEM tolerance → clear jam, reseat, test; flag for early PM.
     - Past tolerance (e.g., > 30% wear) → go to swap-vs-repair worksheet (below).
3. Any action that opens a cash compartment → two-person integrity, count-in/count-out logged, regardless of which branch of the tree got here.

**Copier/MFP:**
1. Pull meter read, consumable life %, and last firmware version before dispatch.
2. Consumable at or past rated life, or firmware behind by ≥ 2 versions → resolve remotely or via a consumable-only visit; no board-level diagnosis needed.
3. Hardware error persists after consumable/firmware ruled out → on-site diagnostic, then swap-vs-repair worksheet if board-level.

**PC/workstation:**
1. Remote diagnostic first (event log, SMART drive status, memory test) — best-effort SLA gives room to rule out software/driver causes before a truck roll.
2. Confirmed hardware fault → swap-vs-repair worksheet; PCs skew toward swap by default because loaded bench-repair labor on commodity components (RAM, PSU, drive) routinely exceeds replacement part cost.

## 4. Swap-vs-repair worksheet

Fill both sides before choosing; do not choose from habit or truck-stock convenience.

| Line item | Bench repair | FRU swap |
|---|---|---|
| Labor time (minutes) | diagnosis + repair + test | swap + test |
| Loaded labor rate | $/hr (shop rate, typically $85–125/hr fully loaded) | same rate |
| Part cost | component-level part(s) | full module/assembly cost |
| Custody/reconciliation overhead (cash equipment only) | none, if no compartment opened | mandatory 2-person recount if a cash compartment's chain of custody is broken |
| **Total** | labor$ + part$ | labor$ + part$ + overhead$ |

Decision gate, in order:
1. Remaining SLA window shorter than the bench-repair time estimate, and the FRU is on the truck → **swap**, regardless of cost delta.
2. Wear/failure mode confirmed by gauge or diagnostic as component-level and within bench-repair time budget → **repair**, take the lower total.
3. Same code/asset has recurred 2+ times in 30 days → neither; escalate to root-cause review before doing either fix a third time.

## 5. Dual-custody / two-person integrity checklist (ATM cash compartments)

1. Two authorized custodians present before any cash compartment is opened — no exceptions for time pressure.
2. Count and log cassette/reject-bin contents *before* service action, both custodians sign.
3. Perform the mechanical fix.
4. Count and log contents *after* service action, both custodians sign, compare against pre-service count plus/minus any notes physically removed or added during service.
5. Variance beyond ±2 notes or ±$50 (whichever is defined in the site's cash-operations policy) → do not close the ticket as resolved; open a cash-variance investigation ticket per branch cash-operations procedure before leaving site.
6. Log the reconciliation record with the ticket number — it is the audit trail, not a formality.
