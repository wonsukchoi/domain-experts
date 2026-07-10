# Playbook

Filled worksheets a Nuclear Technician actually runs in the field. Numbers are worked examples to adapt to the site's own survey data and administrative limits — never a substitute for them.

## 1. Pre-job stay-time and dose-budget worksheet

Used before any RWP is issued for work in a radiologically controlled area with a measurable dose rate.

**Filled example — steam generator manway inspection:**

| Field | Value |
|---|---|
| Job | Manway inspection, SG-1B |
| Point-of-work dose rate (re-surveyed same shift) | 180 mrem/hr contact |
| General-area dose rate (for comparison only — not used for stay time) | 60 mrem/hr |
| Task duration (total hands-on) | 40 minutes |
| Individual EPD alarm setpoint | 100 mrem |
| Job administrative dose budget (collective) | 120 mrem |
| Stay time at point-of-work rate | 100 ÷ 180 = 33.3 min/worker |
| Workers needed (⌈duration ÷ stay time⌉) | ⌈40 ÷ 33.3⌉ = 2 |
| Split | Worker A: 20 min → 60 mrem. Worker B: 20 min → 60 mrem. |
| Collective dose predicted | 180 mrem/hr × 0.667 hr = 120 mrem |
| Budget check | 120 mrem predicted vs. 120 mrem budget — **no margin; escalate for shielding or budget increase before proceeding** |

**Rule:** always compute stay time from the point-of-work rate, never the general-area rate — the general-area number only tells you whether the point-of-work re-survey is even necessary (it is, whenever the two differ by more than instrument/geometry noise, roughly >20%).

**When the budget check fails (predicted ≥ budget, as above):** options in preference order — (1) temporary shielding to cut the point dose rate, (2) engineering fix to remove the source (flush, drain, remove component) if the schedule allows, (3) add workers to shorten individual stay time (does not reduce collective dose, only individual dose — use only when the constraint is the individual alarm, not the collective budget), (4) request a documented budget increase from the ALARA committee with justification, as a last resort.

## 2. Airborne radioactivity / DAC-hour tracking table

Used whenever grinding, cutting, or other resuspension work occurs in a radiologically controlled area, or a continuous air monitor is required by the RWP.

**Filled example — grinding job, 3-hour duration:**

| Time | Sample result (% of DAC) | Cumulative DAC-hrs (mid-interval × duration) | Action |
|---|---|---|---|
| 0:00–0:30 | 8% | 0.5 × 0.08 = 0.04 | Continue, respirators per RWP baseline |
| 0:30–1:00 | 15% | 0.04 + 0.5×0.15 = 0.115 | Continue, note upward trend |
| 1:00–1:30 | 27% | 0.115 + 0.5×0.27 = 0.25 | **≥25% of DAC — escalate respiratory protection posture (upgrade to supplied-air or full-face if not already in use), notify RP supervisor** |
| 1:30–2:00 | 22% | 0.25 + 0.5×0.22 = 0.36 | Confirm escalation held, continue |
| 2:00–2:30 | 30% | 0.36 + 0.5×0.30 = 0.51 | Reconfirm respiratory posture adequate; consider work stoppage if trend keeps rising |

**Rule:** the 25%-of-DAC trigger is a posture-escalation trigger, not a stop-work trigger by itself — stop work is triggered separately if results exceed 100% of DAC, if the escalated respiratory protection can't be achieved, or if cumulative DAC-hours for the shift approach the worker's annual intake tracking limit.

## 3. Frisking / contamination survey log

Used at controlled-area exit points and for item release surveys.

**Filled example — personnel exit frisk, portal monitor alarm:**

| Field | Value |
|---|---|
| Background at friskers (logged daily) | 350 cpm |
| Plant alarm setpoint | background + 300 cpm = 650 cpm |
| Alarm reading | 720 cpm, left hand |
| Re-frisk (same location, same detector) | 705 cpm — **confirmed, not a transient/background artifact** |
| Action | Hold at exit, notify RP, decon (glove change / hand wash), re-frisk after decon |
| Post-decon reading | 340 cpm — released |
| Item/area follow-up | Survey the glovebox/tool the worker last handled — contamination has a source |

**Filled example — item release (free-release) survey:**

| Field | Value |
|---|---|
| Item | Hand tool bag leaving RCA |
| Site free-release limit (beta-gamma, removable) | 1,000 dpm/100 cm² |
| Smear result | 420 dpm/100 cm² |
| Direct scan (fixed + removable) | 2× background, consistent with smear |
| Disposition | Released — documented on release survey form with instrument ID, calibration date, surveyor initials |

**Rule:** a "reads background" quick frisk is not a release survey — item release requires a documented smear count against the site's specific free-release limit for the radionuclide(s) present, with instrument ID and calibration date recorded.

## 4. RWP dose-plan template (fields that can't be left blank)

```
RWP #: ___          JOB: ___                    DATE: ___
POINT-OF-WORK SURVEY: ___ mrem/hr, surveyed ___ (date/time), by ___
  (must be <24 hr old at job start, or re-verified if work/lineup
   changed since — cite what changed if re-verifying)
CONTAMINATION STATUS: fixed ___ dpm/100cm² / removable ___ dpm/100cm²
AIRBORNE STATUS: last sample ___ % DAC, CAM required? Y/N
STAY TIME CALC: ___ mrem/hr × ___ workers × ___ min = ___ mrem collective
  vs. JOB BUDGET: ___ mrem   [MUST show predicted ≤ budget before issue]
EPD ALARM SETPOINT: ___ mrem      DOSE RATE ALARM: ___ mrem/hr
RESPIRATORY PROTECTION: none / half-face / full-face / supplied-air
STOP-WORK TRIGGERS: EPD alarm, dose rate alarm, CAM alarm, unbriefed
  condition change, shielding disturbed — contact RP before resuming
WORKER BRIEFED (initials): ___   RP APPROVAL: ___
```

The two fields most often skipped under time pressure: the **point-of-work re-survey date/time** (vs. relying on a general posting) and the **predicted-vs-budget check** written down before work starts, not estimated verbally.
