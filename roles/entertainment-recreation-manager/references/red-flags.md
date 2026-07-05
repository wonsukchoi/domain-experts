# Red flags & diagnostics

Signals an experienced entertainment/recreation manager notices instantly. Load this when triaging a safety, staffing, or capacity question — not for general reasoning (that's `SKILL.md`).

### Conditions approaching an attraction's certified operating limit on a high-attendance day
- **Usually means:** nothing operationally different from any other day — the limit doesn't move for attendance, but the pressure to delay a shutdown decision is higher
- **First question:** "What's the current reading against the certified limit, and is the monitoring interval tight enough given how close we are?"
- **Data to pull:** real-time condition monitoring log against the attraction's certified limits documentation

### Staffing schedule was finalized more than 2 weeks before the operating date with no revision since
- **Usually means:** the schedule reflects a seasonal-average assumption, not current forecast signals (weather, advance sales, local events) that have since changed
- **First question:** "Has advance ticket sales or weather forecast for this specific date diverged from what the schedule assumed when it was built?"
- **Data to pull:** current advance sales and weather forecast vs. the assumptions used when the schedule was set

### A rain-day or contingency plan is identical regardless of the day's revenue potential
- **Usually means:** contingency planning wasn't sized to revenue concentration — a slow Tuesday and a sold-out holiday weekend are getting the same level of backup investment
- **First question:** "What's this specific day's forecast revenue relative to a typical day, and does the contingency plan scale with that?"
- **Data to pull:** advance sales/forecast attendance for the specific date vs. seasonal average

### Wait times on one specific attraction are consistently the top guest complaint, with no virtual queue or capacity management in place
- **Usually means:** capacity allocation tools are being applied uniformly (or not at all) rather than targeted at the actual binding constraint on guest satisfaction
- **First question:** "What's the wait-time distribution across all attractions, and is this specific one a clear outlier?"
- **Data to pull:** wait-time data by attraction, guest satisfaction survey verbatims/ratings by attraction

### Seasonal staff supervision ratio on a physically risky activity (aquatics, rides, adventure) was reduced during a demand surge
- **Usually means:** labor cost pressure is being resolved by cutting a safety-relevant supervision ratio rather than by adjusting scheduling or capacity elsewhere
- **First question:** "What's the current supervisor-to-participant or supervisor-to-operator ratio for this activity right now, and how does it compare to the standard policy ratio?"
- **Data to pull:** current shift staffing roster for the specific activity vs. the certified/policy minimum ratio

### Season pass pricing hasn't been revisited despite a material change in average visit frequency or secondary spend per visit
- **Usually means:** the pricing model is stale relative to actual demand-smoothing and spend behavior, potentially leaving revenue on the table or underpricing relative to actual value delivered
- **First question:** "When was the season pass pricing model last recalculated against actual visit-frequency and per-cap spend data?"
- **Data to pull:** season pass holder visit frequency and per-visit secondary spend data vs. the assumptions embedded in current pricing

### An attraction resumes operation immediately after a single reading returns within limit
- **Usually means:** the resume criteria may not require the sustained-return-to-range confirmation that's standard practice, risking a premature restart during genuinely marginal conditions
- **First question:** "How many consecutive in-range readings triggered the resume decision, and is that consistent with the documented resume protocol?"
- **Data to pull:** the decision log showing readings and timestamps around the shutdown and resume
