# Dispatcher — Red Flags

### Driver stationary on telematics past the expected check-in interval (>10 min)
- **Usually means:** Driver stopped for a legitimate reason (traffic, bathroom, waiting on customer) and hasn't updated status, or a vehicle/personal safety issue.
- **First question:** "Have I placed a direct call yet, or am I assuming it's fine?"
- **Data to pull:** Live telematics location, time-stationary duration, driver's last voice/text contact.

### Same driver runs over-estimate on job type X repeatedly (3+ times in a rolling week)
- **Usually means:** The estimated job duration for that job type is systematically wrong, not that the driver is slow.
- **First question:** "Is this a driver-specific pattern or a job-type-wide pattern?"
- **Data to pull:** Job-type average actual-vs-estimated duration across all drivers, not just this one.

### Coverage gap recurring on the same day-of-week for 3+ consecutive weeks
- **Usually means:** Structural understaffing for that day, not a one-off scheduling accident.
- **First question:** "Is this a staffing-level problem I should escalate, or am I patching it with on-call every week?"
- **Data to pull:** Weekly open-job-count vs. scheduled-capacity for that day of week, on-call-pull frequency.

### Customer calls in before dispatcher proactively communicated a delay
- **Usually means:** The ETA-slip communication threshold was missed — either the slip wasn't caught in time or the notify-first default wasn't followed.
- **First question:** "At what point did I know this ETA was slipping, and did I notify before or after they called?"
- **Data to pull:** Timestamp of ETA-slip detection vs. timestamp of customer-inbound call.

### Named-driver request overridden by nearest-available logic without flagging it
- **Usually means:** The assignment tool or a rushed dispatcher defaulted to distance and missed the customer's stated preference.
- **First question:** "Was the named-driver constraint visible on this job, and did I check it before assigning?"
- **Data to pull:** Job intake notes for named-driver requests, assignment log for override reasoning.

### A driver's self-reported status contradicts telematics (e.g. marked "en route" but stationary 20+ min)
- **Usually means:** Manual status update lagging reality, or a device/app issue, or the driver is avoiding reporting a problem.
- **First question:** "Do I trust the self-report or the telematics feed here, and have I asked the driver directly?"
- **Data to pull:** Telematics timeline vs. status-update timeline for the shift.

### Priority/SLA account job assigned to the technician with the longest realistic ETA among available options
- **Usually means:** Distance-only ranking was applied without checking the SLA flag, or the SLA flag wasn't visible in the queue.
- **First question:** "Was this job flagged as an SLA account, and did the assignment ranking account for it?"
- **Data to pull:** SLA-account list, assignment timestamp vs. SLA deadline, ranked candidate list at time of assignment.

### Dispatcher re-sequences the board three or more times in an hour without capacity changing
- **Usually means:** Reacting to symptoms (a late job here, a delay there) instead of recognizing an underlying capacity shortfall.
- **First question:** "Am I solving individual jobs or is the whole board over capacity?"
- **Data to pull:** Open-job count vs. available-driver count over that hour.
