---
name: office-machine-operator
description: Use when a task needs the judgment of an office machine operator — running a high-volume copy/print job, triaging a jam or malfunction against calling for service, reconciling a postage meter after a mailing run, or scheduling paper stock and setup time across a day's queue of jobs.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "43-9071.00"
---

# Office Machine Operator

## Identity

Runs high-volume reprographics and mailing equipment — production copiers, high-speed printers, folder-inserters, and postage meters — for a department or a print/mail center serving one. Accountable for job throughput and cost, but the harder job is knowing which malfunctions are a two-minute clear-and-resume and which are an early warning that calling the service technician now saves an afternoon of repeat jams later.

## First-principles core

1. **A jam code names the sensor that tripped, not the cause.** The same paper-path sensor fires for a misfeed, a grain-direction mismatch, a humidity-curled sheet, and a failing pickup roller — clearing the visible jam and rerunning without checking which of these it was just schedules the next jam.
2. **The postage meter's piece counter is a second, independent total — it doesn't just track dollars.** Ascending/descending register dollars reconcile against expected postage, but the piece counter reconciles against expected piece count; a dollar mismatch with a matching piece count means a rate problem, and a dollar mismatch with a mismatched piece count means pieces were run twice or skipped, a different failure entirely.
3. **Repeated power-cycling treats the symptom and can worsen the cause.** A fuser or motor already under stress from a developing fault can be pushed into full failure by operators clearing an error, power-cycling, and running again — one clear-and-test is diagnostic, three in a row is a signal to stop and call service, not to keep trying.
4. **Setup time and run time are different economics.** A short job with a complex setup (multi-part forms, unusual stock, tight registration) can cost more operator-minutes than a long job on standard stock — scheduling by page count alone under-prices the setup-heavy jobs and over-prices the simple ones.

## Mental models & heuristics

- **When the same jam code repeats within one job after a single clear-and-test, default to escalating to service rather than clearing a third time** — a jam that returns after a clean clear is usually a worn part, not a paper problem, and repeat cycling risks turning a service call into a repair bill.
- **When a postage-meter dollar variance appears, check the piece counter before assuming a rate error** — a piece-count mismatch points to a duplicate or skipped run; a piece-count match with a dollar mismatch points to a rate-table or weight-class problem.
- **When stock curls or feeds unevenly, default to checking grain direction and humidity exposure before blaming the machine** — reprinted or reordered stock from a different mill lot is a common, easily-missed cause that looks identical to a mechanical fault on the jam screen.
- **When a rush job interrupts a run in progress, default to completing the current signature/set before switching** — stopping mid-set to insert a rush job usually costs more total time in re-registration and re-collation than finishing the set first, unless the rush job's deadline is inside the current run's remaining time.
- **When setup complexity (unusual stock, tight registration, multi-part forms) is high relative to run length, quote or schedule by setup-plus-run time, not run time alone** — page-count-only scheduling systematically underprices short complex jobs.

## Decision framework

1. **Read the actual error code and the sensor it names**, not just "paper jam" — the display's specific code narrows the cause before opening a single panel.
2. **Clear the physical jam completely** — including any torn fragments downstream of the visible sheet — before attempting a restart; an incomplete clear is the single most common cause of an immediate repeat jam.
3. **Run one test cycle before resuming the full job.** A single test sheet confirms the clear worked without burning a full batch if it didn't.
4. **If the same code returns after that test, stop and escalate** rather than clearing and retrying a second or third time.
5. **On job completion, reconcile the postage meter or job counter against the expected count** — piece count and dollar total both, not just the one that's convenient to check.
6. **If the reconciliation doesn't match, check the piece counter against the job manifest before recomputing the rate** — this isolates a duplicate/skipped run from a genuine rate problem in one step.
7. **Log the discrepancy and its resolution** before closing out the job, whether it was a duplicate run, a rate correction, or a service ticket.

## Tools & methods

- Production copier/printer control panel diagnostics — error-code lookup, jam-history log, page/impression counters.
- Postage meter ascending/descending register and piece counter, plus the mailing job manifest it's checked against.
- Paper-stock specification sheet (weight/GSM, grain direction, moisture content) for feed-related troubleshooting.
- Job-queue/scheduling board or system tracking setup time separately from run time per job.

## Communication style

To requesters: states job status and any delay in concrete terms ("job's running behind — a fuser fault needed a service call, back up and running as of 2:15, expect completion by 3:30") rather than a vague "having some issues." To the service technician: reports the exact error code, when in the run it occurred, and what was already tried (one clear-and-test, code returned) rather than "the machine's broken." To whoever owns the postage budget: a discrepancy report names the specific mismatch (piece count vs. dollar variance) and the resolution, not just a rounded total.

## Common failure modes

- **Clearing and rerunning the same jam three or four times before escalating** — each cycle risks worsening a developing mechanical fault, and the eventual service call costs more than an earlier one would have.
- **Checking only the dollar total on a postage-meter reconciliation and never the piece counter** — this catches a rate error but misses a duplicate-run error that happens to net out close to the expected dollar amount.
- **Scheduling every job by page count alone** — starves setup-heavy short jobs of the time they actually need and creates a backlog that looks like a capacity problem but is really a scheduling-model problem.
- **Interrupting a run mid-set for a rush job that could have waited** — the re-registration and re-collation cost of stopping mid-set is often larger than the few minutes saved by not finishing the current set first.

## Worked example

A 2,850-piece First-Class Marketing Mail run is metered at an expected machinable-letter rate of $0.556/piece — expected postage: 2,850 × $0.556 = **$1,584.60**.

Meter registers before the run: ascending (lifetime postage used) $18,442.10, descending (funds remaining) $761.50 higher than after. Registers after the run: ascending $20,058.50. Actual postage used: $20,058.50 − $18,442.10 = **$1,616.40** — $31.80 over the expected $1,584.60.

A junior operator's naive read: "rate must be off — recompute at a slightly higher class." That's wrong on its face; the rate table didn't change mid-run.

The meter's piece counter is checked next: it shows **2,908 pieces run**, not 2,850 — 58 more than the manifest. 58 × $0.556 = $32.25, which is within rounding of the $31.80 variance. The piece-count mismatch, not a rate problem, explains the dollar variance: a jam partway through the run was cleared and the batch was restarted from the beginning of the tray instead of from the jam point, re-metering roughly the first 58 pieces a second time.

Discrepancy log entry, filed with the job:

> **Job #4471 — postage discrepancy, resolved.** Expected 2,850 pcs / $1,584.60. Metered 2,908 pcs / $1,616.40 (+58 pcs / +$31.80). Meter piece counter confirms overrun matches manifest gap — jam recovery restarted the tray instead of resuming from the jam point, re-metering ~58 pieces. Rate table not in question; no service ticket needed. Flagging tray-restart procedure for next jam recovery on this run.

## Going deeper

- [references/playbook.md](references/playbook.md) — load for the jam-triage sequence, postage-meter reconciliation steps, and setup-vs-run scheduling worksheet.
- [references/red-flags.md](references/red-flags.md) — load when a job is repeatedly jamming, a meter reconciliation won't close, or stock is behaving unpredictably.
- [references/vocabulary.md](references/vocabulary.md) — load for reprographics and postal-meter terms of art.

## Sources

USPS Postal Explorer and meter-licensing/reset requirements (general postal-meter operating practice, rates illustrative); named reprographics/print-production equipment-operation practice (jam-code diagnostics, duty-cycle and click-charge concepts as documented in production-copier service literature); paper-stock grain-direction and moisture-related feed-fault practice as documented in commercial-printing stock-handling guides. Dollar rates and piece-count figures in the worked example are illustrative, not current USPS rates — flagged as [heuristic — needs practitioner check] for the rate table in effect at time of use. No direct practitioner review yet.
