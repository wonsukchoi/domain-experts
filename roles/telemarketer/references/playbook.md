# Playbook

Operational tools a telemarketer or campaign lead actually runs, filled with real structure and example numbers — adapt the specifics, keep the shape.

## 1. Pre-dial compliance checklist

Run against every list before the first dial, not once at list purchase.

```
LIST: Home-security web-inquiry leads, sourced [date]
□ National DNC scrub run within last 31 days — scrub date: __________
□ Internal/company-specific DNC list cross-checked — 0 matches carried forward
□ Consent basis documented per record:
    - Landline, no autodialer/prerecorded message → prior express consent sufficient
    - Cell phone + autodialer or prerecorded voice → PRIOR EXPRESS WRITTEN CONSENT
      required (signed/e-signed disclosure, not just an opt-in checkbox)
□ Destination states checked against mini-TCPA list (FL, OK, WA, and any others
  active this quarter) — stricter consent rule applied if list touches them
□ Calling window set to 8:00am–9:00pm in the CALLED PARTY'S time zone, not the
  dialer's origin zone (list segmented by area code / known time zone)
□ Caller ID displays a real, callable number and the entity's actual name —
  no masked or spoofed number
```

A list that fails any line gets scrubbed or removed before dialing, not fixed retroactively after the campaign starts.

## 2. Dialer pacing worksheet

Predictive dialers pace off a live statistical model; the operator sets the aggressiveness. Work the ceiling backward, don't creep up to it.

```
Legal ceiling (TSR):              3.0% abandonment, 30-day rolling measure
Target operating ceiling:         2.0% (1-point margin for a bad hour)
Current shift abandonment:        2.3%  <- ACTION: drop 1 line/agent now
Lines per agent (before):         3.2
Lines per agent (after adjust):   2.6
Re-check interval:                every 60 minutes during active dialing
```

**Rule:** any reading above 2.5% mid-shift triggers an immediate pacing cut, not a note for the end-of-day review — the 3% figure is a rolling 30-day average, so one bad afternoon can already be the violation even if it doesn't show until the monthly number is pulled.

## 3. Opening-hook formulas

Structure: **who you are + specific reason tied to them + a two-second permission ask.** Never lead with the offer.

**Warm/opt-in list (they inquired):**
> "Hi [name], this is [agent] with [company] — you filled out a request about [specific product] pricing on [date], and I've got that ready for you. Got two minutes?"

**Cold consumer list (no prior contact):**
> "Hi [name], this is [agent] with [company] — I'm calling [specific, concrete reason: e.g., "because folks on your street just had two break-ins reported this month"], not to sell you anything on this call, just to see if it's relevant to you. Can I ask one quick question?"

**Compliance-mandated disclosure, folded in (not read separately):**
> "This is [agent] calling from [actual company name] about [actual purpose] — nothing recorded is going to bill you today, I just want to see if this fits."

**What breaks it:** leading with the product name and price before the reason; reading the disclosure as a separate legal-sounding block instead of inside the hook sentence; any hesitation on "who is this" — hesitation reads as a scam call and ends the conversation regardless of script quality.

## 4. Objection matrix — stall vs. substantive

| Signal | Type | Timing | Response pattern |
|---|---|---|---|
| "Not interested" within first 10 sec, before any value stated | Stall (reflex) | Pre-pitch | One pattern-interrupt question tied to the hook — do not repeat the pitch |
| "How much is this going to cost me" after pitch | Substantive (price) | Post-pitch | Answer directly with the number, then value context — never dodge to "let's get you started first" |
| "I need to talk to my spouse/partner" after pitch | Substantive (authority) | Post-pitch | Offer a specific callback window, not "I'll just call back later" — vague callbacks convert near zero |
| "Take me off your list" / "Stop calling" — any point | Compliance stop | Any | Log DNC immediately, end call, no further attempt — never treat as a soft objection |
| Long pause, no clear objection, after full pitch | Ambiguous | Post-pitch | Direct closing question ("Does this make sense for your situation, yes or no?") rather than re-pitching |

**Rule:** a stall met with a repeated or harder pitch converts worse than a stall met with a single reframe question — escalating past a reflex confirms the prospect's "pushy salesperson" read.

## 5. Daily metrics rollup template

Filled example, one shift, 8,000-dial campaign:

```
CAMPAIGN: Home-security add-on, Tuesday shift, 4 agents
Dials:                    8,000
Connect rate:              32%   (2,560)   [benchmark: 25-35% typical]
Abandonment rate:         2.3%   (59/2,560) [ceiling: 3.0% rolling 30-day; target 2.0%]
Right-party-contact rate:  78%   (1,951/2,501) [benchmark: >15% flags a bad list below this]
Early-stall rate:           40%   (780/1,951) [flag: >35% means the hook needs work]
Pitch-to-close rate:        8.2%  (96/1,171)  [benchmark: 5-10% warm list, 1.5-2.5% cold]
Blended close (of dials):   1.2%  (96/8,000)  [reported number — do not diagnose from this alone]

ACTIONS TODAY:
1. Cut dialer pacing 1 line/agent — abandonment margin too thin.
2. Rewrite opening hook to reference the specific inquiry — stall rate above flag line.
3. No change to pitch/close script — performing above benchmark.
```

The blended close rate is what gets reported up; the five component rates above it are what get diagnosed from. Never skip straight to the blended number when something looks wrong.
