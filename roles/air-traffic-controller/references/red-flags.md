# Red flags

Smell tests a controller or supervisor catches during a live session or a post-event review. Format for each: what it usually means, the first question to ask, and the data to pull.

## 1. Current gap looks comfortable but closure rate is rising ("compression")

**Usually means:** two aircraft on the same final approach course or route are both slowing toward different target speeds at different rates — the gap that looks fine right now is shrinking and will be under minimum at the constraining point (usually the threshold or a merge fix), not before.

**First question:** "What's each aircraft's speed trend for the next two minutes, and what's the projected gap at the threshold, not right now?"

**Data to pull:** current groundspeed and speed-reduction schedule for both aircraft; time/distance to the constraining point for each; whether the trailing aircraft is a lighter wake category than the leading one (compounds the risk).

## 2. Wake-turbulence minimum applied from the wrong table (legacy vs. RECAT)

**Usually means:** RECAT group minima are being applied at a facility still running legacy Heavy/Large/Small categories, or vice versa — one table's distances don't map cleanly onto the other's category names.

**First question:** "Is this facility RECAT-equipped for this runway, and which table's numbers are we actually using?"

**Data to pull:** facility's current wake-turbulence program status (legacy vs. RECAT 1.5/2.0/3.0); the specific aircraft-pairing minimum from the correct table; any recent facility-letter-of-agreement change to wake procedures.

## 3. Read-back accepted with a missing or garbled element

**Usually means:** the controller heard *a* read-back and moved on without confirming every assigned element (altitude, heading, runway, hold-short) was actually repeated correctly — the single most common way a communication error survives past its designed checkpoint.

**First question:** "Did the read-back include every element I assigned, verbatim, or did I just hear a callsign and assume the rest?"

**Data to pull:** the voice-tape transcript of the instruction and the read-back side by side; whether a re-issue and re-confirmation occurred before the next transmission.

## 4. Similar or identical-sounding callsigns on the same frequency

**Usually means:** two aircraft with numerically or phonetically similar callsigns are both working the frequency, and an instruction intended for one gets read back or acted on by the other.

**First question:** "Are there two callsigns on this frequency right now that could be confused for each other, and has either pilot been told to expect that?"

**Data to pull:** active callsign list on frequency; whether a callsign-confusion advisory was issued; any recent read-back that matched the wrong aircraft's clearance history.

## 5. MSAW or Conflict Alert dismissed as a "nuisance" alert

**Usually means:** the automated backstop (Minimum Safe Altitude Warning or Conflict Alert) fired on a known non-issue often enough that it's being dismissed by reflex — which also means the one time it's real, it gets the same half-second of attention.

**First question:** "What was this aircraft's actual altitude and intent when the alert fired, confirmed independently of the alert itself?"

**Data to pull:** alert log with aircraft altitude/heading at trigger time; dismissal rate for this alert type at this position over the shift; whether the underlying terrain/traffic data driving the alert has changed recently (new obstacle, new procedure).

## 6. A TCAS resolution advisory fires before any ATC instruction was issued

**Usually means:** the projected conflict was resolved later than it should have been on the controller side — TCAS is an independent, aircraft-level backstop, and its activation is a lagging indicator that ATC separation had already broken down by the time it triggered.

**First question:** "What was the projected time to loss of separation when we first should have detected this, versus when the RA actually fired?"

**Data to pull:** radar track history for both aircraft in the minutes before the RA; time of first detectable convergence versus time of first ATC instruction; whether either aircraft deviated from an assigned altitude/heading before the RA.

## 7. A facility briefly reverts to non-radar procedures mid-shift (equipment outage)

**Usually means:** radar or automation equipment has degraded or failed, and controllers are applying procedural (non-radar) separation while still mentally anchored to radar-level precision and timing — a mismatch that produces minima that look "too conservative" and get quietly shaved.

**First question:** "Are we actually applying the full non-radar minimum right now, or are we still thinking in radar-scope distances?"

**Data to pull:** equipment-outage log and start/end time; separation minima actually applied during the outage window versus the required non-radar minima; any position reports missed or delayed during the degraded period.

## 8. Sector traffic count exceeds the facility's Monitor Alert Parameter (MAP)

**Usually means:** the sector is at or past its planned staffing/complexity threshold, and the controller's remaining capacity for a genuine developing conflict is thinner than the traffic count alone suggests.

**First question:** "Are we over the sector's MAP right now, and if so, what's actually been done — traffic management restriction, sector split, handoff of non-critical traffic?"

**Data to pull:** current aircraft-in-sector count versus the sector's published MAP; time since the threshold was crossed; whether a traffic-management initiative (miles-in-trail restriction, ground stop) has been requested.

## 9. Post-loss-of-separation response is blanket extra spacing, not a specific fix

**Usually means:** after a reportable event, the response is padding every subsequent sequence with unrequired extra distance instead of identifying and correcting the specific procedural gap (wrong wake category applied, missed compression, incomplete handoff) that actually caused it.

**First question:** "What specifically caused this event, and does the fix address that cause, or just add margin everywhere?"

**Data to pull:** the event's severity categorization (how much of the required minimum was lost, and how much reaction time existed); the specific procedural or communication step that failed; delay/throughput impact of any blanket spacing change imposed since.
