# Red flags

Smell tests a shift supervisor or their manager should catch in the first pass over a week's numbers or a shift log.

### Cash drawer variance exceeding $2 on the same register three shifts running
- **Usually means:** A cashier undertrained on the count-back-change method, or a shared drawer with no individual login — less often, till skimming.
- **First question:** Is each cashier logging in and out of their own drawer, or is this a shared till across a shift change?
- **Data to pull:** POS drawer-assignment log and per-cashier variance history for the last two weeks.

### Prime cost above ~65% of net sales for two consecutive weeks
- **Usually means:** Scheduling built off a stale sales forecast rather than actual volume, or portioning drift on high-cost items — rarely a pricing problem at this timescale.
- **First question:** Did scheduled labor-hours track this week's sales forecast, or were shifts built off last month's template?
- **Data to pull:** Weekly SPLH by daypart against the schedule, and a plate-cost audit on the top five sellers.

### Comp/void total above ~2% of net sales in a week
- **Usually means:** A training gap at one register (ringing errors comped instead of corrected) or one employee routing personal discounts through the void key.
- **First question:** Is the comp/void concentrated on one register or one shift, or spread evenly across the team?
- **Data to pull:** Comp/void report broken out by employee ID and reason code.

### Ticket times over 90 seconds on three or more consecutive orders at a single station
- **Usually means:** Understaffing for the actual volume rather than the scheduled volume, or an equipment slowdown (fryer recovery time, a second register down).
- **First question:** Is this a headcount gap right now, or an equipment/ticket-routing problem?
- **Data to pull:** POS ticket-time log for the station, plus the schedule for that daypart.

### Same employee generating three or more shift-swap requests in a month with no stated pattern
- **Usually means:** An unstated availability conflict (second job, school schedule change) the employee hasn't disclosed, occasionally an early sign of disengagement before a quit.
- **First question:** Has anyone actually asked why, or is it just being approved each time?
- **Data to pull:** Swap-request log with reasons, cross-checked against the employee's original availability form.

### A minor employee's clock-in/out times outside the FLSA or state window without a flag
- **Usually means:** The schedule was built off the adult template and nobody checked the employee's date of birth against the age-restricted ruleset.
- **First question:** Does the scheduling system have this employee correctly flagged as a minor, with the applicable state overlay applied?
- **Data to pull:** Time-and-attendance report filtered to employees under 18, compared against FLSA and the specific state's minor-labor limits.

### Cold-holding temperature log with a gap, or every entry landing on a suspiciously round number
- **Usually means:** The log is being filled in from memory at end of shift rather than read live off the unit — a health-inspection finding waiting to happen.
- **First question:** Who filled this in, and when, relative to when the checks were supposedly performed?
- **Data to pull:** Time-stamped temp-log entries (if digital) against the POS clock-in time of whoever signed it.

### A single shift lead's PIN approving all comp/void overrides above the register-level threshold, with no other manager ID ever appearing
- **Usually means:** Either they're the only certified manager on that shift (normal), or the approval PIN is shared or left logged in (a control failure).
- **First question:** Is more than one manager PIN ever used to approve overrides on this register?
- **Data to pull:** Manager-override log by PIN and by register for the last 30 days.

### Drive-thru order-to-window time trending up over several weeks with no staffing change
- **Usually means:** Menu-board or POS software friction added recently, or a headset/equipment issue slowing order-taking — rarely a people problem at this point.
- **First question:** Did anything change on the tech side (menu update, POS version, headset battery life) around when the trend started?
- **Data to pull:** Drive-thru timer data segmented by order-taking time vs. window/runner time.

### Customer complaints clustering around one specific shift or one specific employee
- **Usually means:** A skills or attitude gap with that individual, or that shift is chronically understaffed and everyone on it is under strain.
- **First question:** Is this one person across many shifts, or many people on one shift?
- **Data to pull:** Complaint log tagged by shift and by employee, cross-referenced against that shift's SPLH.

### Overtime approved in the same week as a call-out or no-show
- **Usually means:** A gap was filled with the most expensive option reflexively, without checking cross-trained floaters or a shift-trade first.
- **First question:** Was every cheaper coverage option on the fallback ladder checked before overtime was approved?
- **Data to pull:** Overtime-approval log with reason codes, matched against the schedule for that day.

### A comp/void reason code of "other" or "manager discretion" used repeatedly by the same approver
- **Usually means:** Either genuine edge cases that don't fit the standard codes, or a shortcut being used to avoid documenting the real reason.
- **First question:** What would the correct, specific reason code have been for the last five "other" entries?
- **Data to pull:** Comp/void log filtered to non-standard reason codes, grouped by approver.
