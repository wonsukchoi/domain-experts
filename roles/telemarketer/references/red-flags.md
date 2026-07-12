# Red flags

Smell tests a telemarketing floor lead catches inside the first look at a shift's numbers or a compliance question.

## 1. Abandonment rate above 2.5% mid-shift

**Usually means:** dialer pacing is set too aggressively for the current connect rate — the predictive model is dialing more lines ahead of agent availability than the live answer rate supports.

**First question:** "What's the lines-per-agent ratio right now, and when was it last adjusted?"

**Data to pull:** rolling abandonment rate for the current 30-day campaign window (not just today), lines-per-agent setting, connect-rate trend for the last hour. The 3% figure is a legal ceiling measured over 30 days — a single bad afternoon at 4% can already put the month over the line even if today's isolated number looks recoverable.

## 2. Right-party-contact rate below ~15% on a "fresh" list

**Usually means:** the list is bad data — stale numbers, disconnected lines, or a scrub date older than claimed — more often than it means the script or agents are underperforming.

**First question:** "When was this list actually scrubbed against DNC, and where did the numbers originate?"

**Data to pull:** list source and acquisition date, last scrub date, wrong-number and disconnected disposition counts as a share of total dials. If wrong-number/disconnected dispositions exceed roughly 20% of connects, the list itself is the problem.

## 3. Close rate reported only as a percentage of total dials

**Usually means:** whoever is reporting hasn't decomposed the funnel, so a genuine pitch-stage problem and a genuine connect-stage problem look identical from the top-line number.

**First question:** "Break that down — connect rate, right-party-contact rate, and close rate on pitches actually delivered. Which stage moved?"

**Data to pull:** stage-by-stage disposition counts for the period in question, same metrics for the prior comparable period, side-by-side.

## 4. Agents editing or skipping the identification/purpose disclosure

**Usually means:** agents are optimizing for a faster hook at the expense of a legally mandated statement — often because the disclosure as written sounds stiff and agents route around it rather than rewriting it into the hook.

**First question:** "Pull three recent call recordings — is the company name and purpose actually stated, and within how many seconds?"

**Data to pull:** QA scoring on disclosure compliance specifically (separate from tone/close scoring), a sample of recent call recordings, the current script's disclosure placement.

## 5. Spike in "remove me" / Do-Not-Call requests not logged same-day

**Usually means:** either agents are pushing past the request before logging it, or the disposition-code workflow has a lag that lets a request sit unprocessed past the point it should have blocked a re-dial.

**First question:** "Show me the time gap between the recorded 'remove me' request and the disposition code being entered — and has that number been re-dialed since?"

**Data to pull:** call recordings for flagged calls, disposition-code timestamps versus call-end timestamps, re-dial history against the DNC-flagged numbers.

## 6. List used without a documented consent trail for cell numbers

**Usually means:** the list was purchased or aggregated without capturing whether prior express consent (sufficient for a live agent call) or prior express written consent (required for autodialed/prerecorded calls to cells) was obtained — a gap that doesn't surface until a complaint or lawsuit.

**First question:** "For the cell numbers on this list, where's the signed or e-signed consent record, not just an opt-in checkbox?"

**Data to pull:** the list vendor's consent documentation, the specific consent language shown to the consumer at capture, the date and method of capture.

## 7. Dialing into a state with its own telemarketing statute without a separate check

**Usually means:** the campaign is running under federal TSR/TCPA compliance alone, missing a stricter state consent requirement (Florida, Oklahoma, Washington are the most litigated) that federal safe harbor does not preempt.

**First question:** "Has this list been filtered or consent-upgraded for area codes in states with their own mini-TCPA statute?"

**Data to pull:** area-code breakdown of the list against the current list of states with active mini-TCPA statutes, consent basis on file for those records specifically.

## 8. Pacing increased right after a slow-connect hour

**Usually means:** someone is compensating for a low-connect stretch by pushing the dialer harder, which raises abandonment risk exactly when it's least likely to be caught — a slow hour with tight pacing already has less agent slack to absorb a spike.

**First question:** "What was the abandonment rate in the hour right after the pacing change?"

**Data to pull:** pacing-change log with timestamps, abandonment rate in the hour before and after each change, connect-rate trend across the same window.

## 9. QA scores dropping while close rate rises

**Usually means:** agents are trading compliance or professionalism for short-term conversions — pressure tactics, glossing objections, or skipping qualification — a pattern that shows up later as cancellations, chargebacks, or complaints rather than in the close number itself.

**First question:** "Pull the call recordings behind this week's closes — what's actually being said before the close?"

**Data to pull:** QA rubric scores by agent over the period, close rate by agent over the same period, correlation between the two; post-sale cancellation rate for the same cohort of closes once it's available.

## 10. Post-sale cancellation or chargeback rate rising after a close-rate jump

**Usually means:** the close-rate gain came from a harder push or an unclear pitch rather than a genuinely better offer or fit — the sale happened, but the customer didn't understand or want what they agreed to.

**First question:** "What's the 30-day cancellation rate for sales from the period where close rate jumped, compared to the prior period?"

**Data to pull:** cancellation/chargeback rate by sale cohort and by agent, call recordings for a sample of cancelled sales, script or pacing changes that coincided with the close-rate jump.
