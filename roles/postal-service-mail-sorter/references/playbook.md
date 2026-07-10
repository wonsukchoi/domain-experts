# Playbook

## Reject-rate investigation (filled example)

Run 4471, First-Class letters, DBCS-06, 250,000 pieces.

| Metric | Value |
|---|---|
| Pieces processed | 250,000 |
| Reject rate this run | 9.4% (23,500 pieces) |
| Contractual reject ceiling | 10% |
| 30-day baseline reject rate, this mail type/machine | 6.0% (15,000 pieces at this volume) |
| Excess rejects vs. baseline | 23,500 − 15,000 = 8,500 pieces |
| REC keying time per piece | ~4 seconds |
| Added REC labor this run | 8,500 × 4 sec = 34,000 sec = 566.7 min ≈ 9.4 hours |

**Investigation steps:**
1. Confirm the run is under the contractual ceiling (9.4% < 10% — compliant) but flag the baseline deviation anyway (+3.4 points).
2. Pull a sample of 50–100 rejected pieces; group by mailer batch/permit number.
3. If rejects concentrate in one batch (here, batch #7734), inspect print quality/barcode clarity on a physical sample from that batch.
4. If confirmed a print-quality issue, escalate to the mailer acceptance unit rather than requesting machine recalibration.
5. If rejects are evenly spread across batches instead, that points toward genuine OCR/barcode-read drift — escalate to maintenance for calibration check instead.

## Jam-log escalation (filled example)

DBCS-06, day shift, 8-hour run (480 minutes scheduled).

| Metric | Value |
|---|---|
| Jam count this shift | 14 |
| Average clear time per jam | 6 minutes |
| Total downtime from jams | 14 × 6 = 84 minutes |
| Jams per hour (over 8-hour shift) | 14 / 8 = 1.75/hour |
| Error code distribution | 11 of 14 jams logged as code F-22 (feed roller slip) |

Since 11 of 14 jams (78.6%) share the same error code, this is a component-specific pattern, not random mail-condition variation. Escalation to maintenance cites the code and frequency directly:

> DBCS-06 logged 14 jams this shift (1.75/hour), 11 of them code F-22 (feed roller slip) — 78.6% of all jams today. Requesting feed roller inspection/replacement rather than continued reactive clearing.

## REC backlog triage (filled example)

REC queue depth at shift end: 4,200 pieces. Historical average end-of-shift queue: 1,500 pieces. Next shift's typical clearing capacity: 2,000 pieces before its own new volume arrives.

- Backlog above capacity: 4,200 − 2,000 = 2,200 pieces the next shift cannot clear on top of its own normal load.
- Decision: escalate the 2,200-piece overflow to a second REC shift or a delivery-date adjustment for the affected batch, rather than letting it silently roll forward and compound with the next shift's own reject volume.
