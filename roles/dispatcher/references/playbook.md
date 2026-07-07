# Dispatcher — Playbook

## Assignment-ranking table (filled example)

New job: residential no-heat call, submitted 9:12am, no SLA (standard 4-hour window quoted to customer: by 1:12pm).

| Driver | Distance | Current status | Telematics | Realistic ETA | Assign? |
|---|---|---|---|---|---|
| Tech 1 | 1.8 mi | En route to job, ETA 9:20am | Moving, on-route | ~9:50am (after finishing current job, est. 25 min) | No — busy, later than Tech 2 |
| Tech 2 | 4.2 mi | Available since 9:05am | Stationary at yard | ~9:22am | **Yes** — nearest confirmed-available |
| Tech 3 | 0.6 mi | En route, ETA 9:14am | Stationary 14 min, check-in interval 10 min | N/A — status check required | Hold — call before considering |
| Tech 4 | 6.5 mi | Mid-job, historical overrun 20% | Moving | Unreliable — job likely to run past estimate | No — unless Tech 2/3 both unavailable |

Decision: assign to Tech 2. Tech 3 flagged for immediate welfare check (independent of this job) due to stationary-past-interval signal.

## ETA-slip communication script

**Under 10 minutes, next check-in is sooner:** No proactive contact — let the next scheduled check-in carry the update.

**10-30 minutes, no next check-in scheduled soon:** Proactive text/call to customer.
> "Quick update — [Tech name] is running about [X] minutes behind due to [one-line reason: prior job ran long / traffic / parts pickup]. New estimated arrival is [time]. Let us know if that window doesn't work."

**Over 30 minutes or SLA account:** Call, not text. Offer a concrete alternative (reschedule to next available window, or escalate to next available technician) rather than just the new ETA.

## Coverage-gap escalation sequence

1. Quantify the gap: open jobs remaining today vs. technicians with capacity to take them, in count form (e.g. "6 open jobs, 3 technicians with capacity" = gap of 3).
2. Check on-call/overflow roster for available pickup before touching the schedule.
3. If no on-call capacity: rank open jobs by customer commitment tightness (SLA account > same-day promise > flexible-window) and push the loosest-commitment jobs to the next available window first.
4. Notify affected customers of the push before end of the current window, not after it's already missed.
5. Log the gap size and resolution (on-call pulled / jobs pushed / both) for end-of-day capacity review — a recurring gap on the same day-of-week is a staffing signal, not a one-off.

## Silent-driver escalation timeline

| Time since expected check-in | Action |
|---|---|
| 0-5 min past interval | No action — normal variance in check-in timing |
| 5-10 min past interval, telematics shows movement | Note it, no call yet |
| 10+ min past interval, telematics stationary | Direct call to driver |
| No answer on direct call, 5 min further | Call driver's emergency contact / dispatch supervisor per fleet safety protocol |
| No contact established, 15 min further | Escalate to welfare-check protocol (varies by fleet — may include sending nearest driver to last known location) |
