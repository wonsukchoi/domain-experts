# Red flags

Smell tests a senior controls/electronics technician catches before signing off a ticket or a panel is closed back up.

### Same VFD fault code recurs 2+ times on one drive within 30 days

- **Usually means:** the prior visit cleared the trip without confirming the fault-code category against a live test — a component was reset or swapped on a guess rather than on a confirmed root cause.
- **First question:** "Pull the last three fault-log entries on this drive — same code, same category confirmed each time, or just reset and restarted?"
- **Data to pull:** drive fault-log history (timestamps, code, category), parts consumed per visit, load/ambient conditions logged at each trip.

### I/O module status LED and ladder-program bit disagree

- **Usually means:** if the LED is lit and the bit is false, an addressing/mapping or card-channel fault on the PLC side; if the LED is off and the field device's own indicator shows active, a wiring/terminal fault between device and card.
- **First question:** "Which side of the card does the LED confirm — is the signal present at the terminal, or not?"
- **Data to pull:** online-monitor screenshot of the tag/bit value, physical LED state at time of test, force-table status for that address.

### Board or drive swap requested without a fault-log category on the ticket

- **Usually means:** the swap decision was made from the fault code's name alone, skipping the input/output/internal/regen category check that would point at a cheaper, faster fix.
- **First question:** "What category does this fault code fall into, and what did the category-specific test (megger, DB-resistor ohm check, fan check) show?"
- **Data to pull:** fault-log entry with code and timestamp, category test result, swap-vs-repair worksheet completion.

### Live-panel diagnostic performed with no PPE-category check against the arc-flash label

- **Usually means:** the technician treated "just a quick reading" as exempt from the label's incident-energy requirement, confusing the NFPA 70E permit exception with a PPE exception.
- **First question:** "What does this panel's arc-flash label say for incident energy and PPE category, and what was actually worn?"
- **Data to pull:** panel's arc-flash label photo or record, PPE worn as logged on the ticket, date of the site's last arc-flash study.

### Arc-flash label missing, illegible, or older than the site's re-study interval (commonly every 5 years or after a documented electrical modification)

- **Usually means:** the panel's PPE requirement can no longer be trusted — equipment changes (breaker upsizing, transformer changes, utility fault-current changes) since the last study can shift the incident-energy number substantially.
- **First question:** "When was this panel's arc-flash study last performed, and has anything upstream of it changed since?"
- **Data to pull:** arc-flash study date and revision history for this panel, one-line diagram change log, utility fault-current data on file.

### Two or more simultaneous down-calls triaged in call-received order

- **Usually means:** dispatch or the technician defaulted to first-come-first-served instead of ranking by downtime-cost-per-hour ÷ estimated repair time, leaving the higher-value line down longer than necessary.
- **First question:** "What's the $/hr and estimated repair time on each open call, and does the dispatch order match the priority-weight ranking?"
- **Data to pull:** downtime-cost-per-hour by line (from production/finance), estimated repair time logged at call intake, actual dispatch sequence.

### Drive swap completed without an auto-tune or parameter reload logged

- **Usually means:** the replacement drive is running on default or copied parameters that don't match the actual motor nameplate, which produces subtle overcurrent or performance faults later that look unrelated to the swap.
- **First question:** "Was the motor auto-tune run after the swap, and do the drive's motor parameters match this motor's nameplate?"
- **Data to pull:** post-swap parameter file, motor nameplate data, auto-tune completion log or timestamp.

### Repeated "no fault found" closures on the same intermittent I/O point

- **Usually means:** a marginal connection, a cable-drag-chain flex point, or EMI/noise coupling that a static continuity test doesn't catch under load or motion.
- **First question:** "Was the fault reproduced under actual motion/load conditions on-site, or only checked at rest?"
- **Data to pull:** conditions logged at each NFF visit (was the axis cycling, was the fault present during the check), cable routing diagram for drag-chain or flex-conduit runs on that axis.

### Safety-rated circuit (E-stop chain, light curtain, safety PLC logic) edited without a re-validation record

- **Usually means:** the edit was treated like a routine standard-I/O rung change instead of a change to a certified safety function, which can silently invalidate the machine's rated stop time or category.
- **First question:** "Was this safety circuit's stop-time and category re-validated after the change, and is that record on file?"
- **Data to pull:** pre- and post-change safety validation test record, machine's safety-function certification documentation, change-control log entry for the edit.
