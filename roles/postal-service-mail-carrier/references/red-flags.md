# Red flags

### End-of-day scan count differs from expected delivery-point count by more than 2%
- **Usually means:** one or more skipped scans, a double-scanned parcel, or a genuine gap in the delivery record.
- **First question:** which specific delivery points show no scan for today?
- **Data to pull:** end-of-day scan reconciliation report compared against the route's delivery point sequence file.

### Route actual time exceeds its evaluated standard by more than 10% for 3+ consecutive weeks
- **Usually means:** unaccounted route growth (new construction, apartment turnover) or a casing inefficiency that's crept in.
- **First question:** how many delivery points have been added or removed since the last Count and Inspection?
- **Data to pull:** DOIS route history and the add/delete log for the route.

### Dog-on-premises flag missing at an address with a prior documented incident
- **Usually means:** the flag lapsed on a system update, ownership change, or route-book handoff, not that the risk went away.
- **First question:** when was this flag last verified or refreshed?
- **Data to pull:** route book entry and the dog-warning database record for the address.

### Forecast heat index reaches the day's posted danger threshold with no adjusted break schedule
- **Usually means:** the day's safety protocol wasn't activated before the route started.
- **First question:** has a hydration/break schedule been posted for this shift?
- **Data to pull:** National Weather Service heat index forecast for the delivery area and the supervisor's daily safety briefing log.

### Hold-mail or forwarding order not reflected before delivery at a flagged address
- **Usually means:** a lag in the system record, or the carrier relying on memory instead of checking it.
- **First question:** does the current system show an active hold or forward order for this address today?
- **Data to pull:** forwarding-order database and hold-mail request record for the address.

### Same cluster box unit (CBU) reported blocked or damaged more than once in a week
- **Usually means:** recurring vandalism or a wear failure needing replacement, not a one-off jam.
- **First question:** how many repeat reports has this specific CBU had in the past month?
- **Data to pull:** CBU maintenance/repair ticket history.

### Substitute (T6/auxiliary) carrier delivers an unfamiliar route with no route-book review logged
- **Usually means:** elevated misdelivery and hazard risk for that day, since address-specific knowledge wasn't transferred.
- **First question:** did the substitute check out and review the route book and dog warnings before departure?
- **Data to pull:** route-book check-out log for the day.

### "Attempted — no access" scanned at the same delivery point more than 3 times in a month
- **Usually means:** a persistent access issue (locked gate, blocking obstacle, animal) rather than the customer repeatedly being absent.
- **First question:** what specifically is blocking delivery at this stop?
- **Data to pull:** scan history and carrier notes for that delivery point over the trailing month.

### Vehicle pre-trip inspection skipped or completed in under the standard time
- **Usually means:** time pressure from a heavy casing day overriding the safety check.
- **First question:** was the inspection actually performed, or only logged as complete?
- **Data to pull:** vehicle inspection log or telematics data compared against the scheduled departure time.
