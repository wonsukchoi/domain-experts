# Red flags

Smell tests a non-retail sales supervisor should catch in the first pass over a week's activity report or an account book.

### Call-abandonment rate above 3% over a rolling 30-day window, per campaign
- **Usually means:** Dialer pacing was pushed up to hit a dial-volume KPI without checking the compliance ceiling — less often, a genuine agent-availability shortfall during a spike in outbound volume.
- **First question:** Did dialer pacing change in the last two weeks, and was that change tied to a specific activity target?
- **Data to pull:** The dialer platform's abandonment report by campaign, and the pacing-ratio change log for the same period.

### Connect rate below ~15% while dial volume is at or above team average
- **Usually means:** A stale or previously-worked contact list, not an effort problem — the rep is dialing the right number of times into the wrong numbers.
- **First question:** When was this rep's contact list segment last refreshed, and is it shared with another rep showing the same pattern?
- **Data to pull:** CRM dial log with connect outcome by number, cross-checked against list-refresh date.

### A single rep holding more than roughly 2x the team-average book value or account count
- **Usually means:** Historical territory assignment or account inheritance, not superior selling — and the thin-book rep on the other end isn't underperforming, they're under-resourced.
- **First question:** How did this rep's book get to this size — inherited, won, or never rebalanced after a prior rep's departure?
- **Data to pull:** Trailing-12-month revenue and active-account count by rep, sorted against team average.

### Draw balance exceeding earned commissions for 3+ consecutive settlement periods
- **Usually means:** The rep's territory or quota is miscalibrated for what the book can actually produce, not a motivation problem — a persistent draw shortfall is a plan-design signal.
- **First question:** Has this rep's account book changed materially in the same window, or has the shortfall existed since the plan was set?
- **Data to pull:** Draw-vs.-earned-commission history by settlement period for the trailing two quarters.

### Discount or credit-term exceptions clustering on one rep's accounts
- **Usually means:** A rep discounting reflexively to hit activity or close-rate targets, or a legitimately harder segment of accounts routed to that rep — rarely random.
- **First question:** Are these exceptions concentrated on a few accounts repeatedly, or spread across this rep's whole book?
- **Data to pull:** Discount-approval log filtered by rep and by account, with the stated reason code for each.

### Quote-to-close (win) rate down more than 10 points quarter over quarter with flat activity
- **Usually means:** A pricing, product, or competitive shift the rep hasn't adjusted to, or a discovery-quality gap producing quotes that were never going to close — rarely a sudden effort drop when activity is unchanged.
- **First question:** Is the drop concentrated on one product line, one competitor matchup, or evenly spread?
- **Data to pull:** Closed-lost reason codes for the quarter, segmented by product line and competitor cited.

### A ramping hire graded against full quota instead of the ramp schedule
- **Usually means:** The scorecard or CRM report defaults to flat quota and nobody applied the ramp adjustment manually — an administrative gap, not a performance issue.
- **First question:** Is this rep still inside the documented ramp window, and was the ramp-adjusted target used in this comparison?
- **Data to pull:** Hire date against the ramp-schedule policy, and the specific target used in the attainment report.

### The same customer objection reported independently by 2+ reps in the same week
- **Usually means:** A real pricing or competitive shift in the market, not a coincidence of individual conversations.
- **First question:** Is this the same competitor or the same objection language across both reps' notes?
- **Data to pull:** CRM call/activity notes tagged with objection type, filtered to the current week across the team.

### A deal sitting in a "commit" or near-term forecast category with no logged activity in 21+ days
- **Usually means:** The deal stalled without the forecast category being updated to reflect it — an optimistic holdover, not a deal genuinely about to close.
- **First question:** What was the last logged next step, and did it have a date attached?
- **Data to pull:** Pipeline report filtered to commit-category deals, sorted by days since last activity.

### An outside sales rep spending a large share of scheduled time at the inside desk rather than in the field
- **Usually means:** Territory geography changed, gas/mileage cost pressure, or a genuine shift in how the account base wants to be worked — but it also erodes the basis for the rep's FLSA outside-sales exemption if it becomes the norm rather than the exception.
- **First question:** Is this a temporary pattern (a specific account crisis, weather) or has it become the rep's default week?
- **Data to pull:** Calendar/CRM check-in location data for the trailing month, against the exemption's "customarily and regularly away from the employer's place of business" standard.

### The same account appearing active in two different reps' pipelines
- **Usually means:** A territory boundary or account-assignment change that wasn't reflected in the CRM, occasionally two reps genuinely working the same lead from different entry points.
- **First question:** Which rep has the account of record per the current territory map, and does the other rep know?
- **Data to pull:** CRM account-owner field history against the current territory assignment sheet.

### Average deal size dropping sharply while deal volume rises for the same rep
- **Usually means:** Discounting to close more, smaller deals faster and hit an activity or close-count target, rather than a genuine shift in the account mix.
- **First question:** Is the discount rate on these deals higher than this rep's trailing average?
- **Data to pull:** Deal-size and discount-rate trend for the rep over the last two quarters.
