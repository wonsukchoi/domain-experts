# Office Machine Operator — Playbook

## Jam-triage sequence

1. **Read the error code exactly as displayed** — note the code and the paper-path zone it names (e.g. "E-042, fuser exit sensor") before opening any panel.
2. **Open only the indicated access panel(s)** and remove the visible jammed sheet, checking for torn fragments left behind — an incomplete clear is the top cause of an immediate repeat jam.
3. **Close all panels fully** — most machines refuse to run, or misreport a jam, with a panel not fully latched.
4. **Run one test cycle** (a single sheet or the smallest available test print) before resuming the full job.
5. **If the test clears cleanly, resume the job from the last confirmed-good sheet or set** — not from the beginning, unless the job's collation makes a partial restart unsafe.
6. **If the same code returns on the test cycle, stop.** Do not clear and retry a second time on the same code. Escalate to service (Escalation table below).
7. **Log the code, the zone, and the resolution** (cleared-and-resumed, or escalated) in the job's run log.

## Jam-code-to-cause reference (illustrative — confirm against the specific machine's service manual)

| Symptom pattern | Likely cause | Check first |
|---|---|---|
| Jam at feed tray, intermittent, worse on humid days | Stock moisture/curl | Stock storage humidity, days since stock was opened |
| Jam at feed tray, consistent on one specific ream | Grain direction mismatch for this machine's feed path | Ream's grain-direction marking vs. machine's short-grain/long-grain spec |
| Jam at fuser exit, recurring after clear-and-test | Fuser roller wear or fuser-exit sensor fault | Impression count since last fuser service; escalate if above service-interval threshold |
| Jam at registration, only on multi-part/carbonless forms | Registration tolerance too tight for stock thickness | Registration setting for this stock type vs. standard-stock default |
| No jam, but repeated light/dark banding on output | Developer or toner-cartridge fault, not a feed issue | Cartridge fill level and page count since install |

## Postage-meter reconciliation

1. **Record ascending and descending register readings before the run.**
2. **Run the job.**
3. **Record ascending and descending readings after the run**; compute actual postage used = ascending-after − ascending-before.
4. **Compute expected postage** = manifest piece count × the rate class used.
5. **If actual ≈ expected within a small rounding tolerance, close the job.**
6. **If actual ≠ expected, check the meter's piece counter against the manifest piece count first** — a piece-count mismatch means pieces were run twice or skipped (check for a jam-recovery restart mid-run); a piece-count match with a dollar mismatch means the rate class or weight-break was wrong, not the run itself.
7. **File a discrepancy log entry** naming the mismatch type and resolution before closing the job, regardless of which type it was.

## Setup-vs-run scheduling worksheet (filled example)

| Job | Page count | Est. run time | Est. setup time | Total | Stock/complexity note |
|---|---|---|---|---|---|
| A — standard letter mail merge | 1,200 | 18 min | 5 min | 23 min | Standard 20lb stock, no special registration |
| B — 3-part carbonless invoice | 150 | 6 min | 22 min | 28 min | Tight registration, multi-part stock — setup dominates despite low page count |
| C — annual report booklet | 400 | 25 min | 15 min | 40 min | Folder-inserter setup for saddle-stitch |

Job B, scheduled by page count alone, looks like the shortest job in the queue (150 pages). Scheduled by total time, it's actually longer than Job A (1,200 pages) — the setup-heavy jobs need to be queued by total time, not page count, or the day's schedule runs long without an obvious cause.
