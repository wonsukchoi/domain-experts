# Red flags

### Deployment frequency drops >30% quarter-over-quarter while headcount grows
- **Usually means:** coordination overhead outpacing team growth (too many teams touching shared code), or fear-driven caution after a recent bad incident that never got named and addressed.
- **First question:** "when was the last P1 incident relative to when this drop started?"
- **Data to pull:** DORA deploy-frequency dashboard overlaid on the incident timeline for the same window.

### On-call rotation attrition — 2+ engineers requesting off rotation in a quarter
- **Usually means:** the on-call load is undocumented toil (repeat pages for the same root cause) rather than genuine incidents, or the rotation is unfairly sized against team headcount.
- **First question:** "pull the last 10 pages — how many were the same underlying issue?"
- **Data to pull:** paging system dashboard grouped by alert source, last 90 days.

### A roadmap item reads "rewrite in [language/framework]" with no quantified pain cited
- **Usually means:** engineer discomfort with unfamiliar or disliked code, not a measured business or velocity problem — rewrites proposed this way have a poor industry hit rate.
- **First question:** "what metric moves if we do this, and what's it at today?"
- **Data to pull:** deploy frequency, incident rate, and hiring/attrition data tied to the system in question.

### Vendor/infra spend growing faster than headcount for 2+ consecutive quarters
- **Usually means:** unreviewed auto-scaling defaults, an unowned or duplicate SaaS subscription, or a system genuinely outgrowing its current architecture.
- **First question:** "which three line items grew the most, and does anyone own them?"
- **Data to pull:** cloud billing breakdown by service + SaaS subscription list with named owners.

### A critical system has a bus factor of 1
- **Usually means:** the system was built under deadline pressure by one engineer and never got a second reviewer or pairing rotation, often because it "just works" and nobody's had reason to touch it.
- **First question:** "if this person is out for a month starting today, what breaks?"
- **Data to pull:** commit history/code-ownership report (e.g. CODEOWNERS or git blame) for the system's core files.

### Postmortem action items open past 60 days, recurring across multiple incidents
- **Usually means:** action items are being generated faster than the org has capacity to close them, which usually means they're not being prioritized against feature work at all.
- **First question:** "who owns the backlog of open action items, and when did they last review it?"
- **Data to pull:** postmortem tracker filtered by open items with an age column.

### New engineer time-to-first-production-commit exceeds 2 weeks
- **Usually means:** onboarding docs are stale, local dev environment setup is broken or undocumented, or the codebase has tribal-knowledge dependencies nobody's written down.
- **First question:** "where did the last three new hires actually get stuck?"
- **Data to pull:** onboarding survey responses or a direct debrief from the last 3 hires.

### The same 3 people attend every architecture review for 12+ months
- **Usually means:** decision-making authority hasn't scaled with the org, creating a bottleneck and a single-point-of-failure on judgment, not just on code.
- **First question:** "who else in the org could make this call, and why aren't they in the room?"
- **Data to pull:** architecture review meeting attendance log.

### Test suite runtime growing faster than the codebase (superlinear)
- **Usually means:** tests are integration-heavy where unit tests would do, or test infrastructure (shared fixtures, DB resets) hasn't been re-architected since the suite was small.
- **First question:** "what's the slowest 10% of tests, and what are they actually testing?"
- **Data to pull:** CI timing report broken down by test file/suite.

### Security patch backlog aging past 90 days on any internet-facing service
- **Usually means:** patching isn't owned by anyone specific, or it's deprioritized against feature work every sprint without an explicit tradeoff decision being made.
- **First question:** "who decided this was lower priority than what shipped instead, and was that decision explicit?"
- **Data to pull:** vulnerability scanner report with age column, filtered to internet-facing services.
