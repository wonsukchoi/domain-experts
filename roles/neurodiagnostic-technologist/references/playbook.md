# Neurodiagnostic playbook

Filled protocol sequences for the three most common study types. Adjust to local lab/OR protocol — these are working defaults, not a substitute for the site's written procedure.

## 1. Routine outpatient EEG — setup and activation sequence

**Pre-recording checklist**

| Step | Action | Target/threshold |
|---|---|---|
| 1 | Confirm order and clinical question | Match montage/activation plan to indication (e.g., "R/O absence" → prioritize hyperventilation + photic; "R/O nocturnal events" → prioritize sleep) |
| 2 | Apply 21 electrodes per international 10-20 system + ground + EKG | Impedance <5 kOhm per electrode, balanced across homologous pairs |
| 3 | Set acquisition parameters | Sensitivity 7 uV/mm (range 5-10), LFF 1 Hz, HFF 70 Hz, 60 Hz notch off unless line noise uncontrolled otherwise |
| 4 | Record clean awake baseline | Minimum 20 minutes of technically satisfactory background before/around activation procedures |

**Activation sequence (typical order)**

1. **Baseline eyes-closed/eyes-open** — 2-3 min, establishes posterior dominant rhythm and reactivity.
2. **Hyperventilation** — 3-5 minutes continuous deep breathing (skip if contraindicated: recent stroke, cardiopulmonary disease, sickle cell, pregnancy per site protocol); record 1-2 min post-HV for any delayed buildup.
3. **Photic stimulation** — flash rates stepped 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 Hz (some labs also step down); watch for driving response vs. photoparoxysmal response.
4. **Drowsiness/sleep, if achievable** — highest-yield state for epileptiform activity; do not artificially rouse the patient the moment they doze off.

**Escalation rule:** if a clinical event or clear electrographic seizure occurs during recording, stop the standard sequence, annotate onset/offset and clinical semiology in real time, and notify the on-call physician before ending the study — a captured event outranks completing the activation checklist.

## 2. Continuous EEG (cEEG) — ICU escalation workflow

| Trigger | Technologist action | Escalation |
|---|---|---|
| New rhythmic/periodic pattern, static morphology over minutes | Annotate, note frequency/location, continue routine review cadence | Flag for next physician review, not an immediate page unless clinical change accompanies it |
| Pattern evolving in frequency, location, or morphology over 30-60 sec | Annotate evolution explicitly (e.g., "2 Hz → 3.5 Hz over 45 sec, spreading from left temporal to bifrontal") | Page on-call physician immediately — evolving pattern is the strongest bedside marker of a true ictal event |
| Patient develops new unresponsiveness, gaze deviation, or automatisms | Mark event with exact timestamp and clinical description | Page immediately regardless of what the trace looks like — clinical correlation drives the page, not just the waveform |
| Seizure-detection software alert | Review the flagged segment against raw trace before acting | Confirm or dismiss within minutes; do not let an unconfirmed algorithm alert sit unreviewed |
| End of scheduled monitoring window (commonly 24-48 hr for suspected nonconvulsive status epilepticus per ACNS consensus practice) | Summarize event count, pattern evolution, and any treatment-correlated changes | Recommend continuation or discontinuation to the ordering physician with specific findings, not "no seizures seen" alone if periodic patterns were present |

## 3. Intraoperative neuromonitoring (IONM) — baseline-to-alarm workflow

**Baseline establishment (before incision/instrumentation)**

1. Record SSEP (posterior tibial ± median nerve as indicated) after anesthesia induction stabilizes, before any surgical intervention.
2. Record transcranial MEP baseline at the lowest stimulation intensity producing a reproducible response; note that intensity as the reference threshold.
3. Confirm baseline technical quality (stable amplitude/latency across ≥2 consecutive averages) before calling it the case reference — a single noisy trace is not a valid baseline.
4. Document anesthetic regimen at baseline (agent, MAC/infusion rate) — a regimen change later in the case is the first alternative explanation to rule out for any signal change.

**Alarm criteria (case-specific baseline as denominator)**

| Modality | Warning criterion | Action |
|---|---|---|
| SSEP | Amplitude decrease >50% AND/OR latency increase >10% from that case's baseline | Alert surgeon and anesthesia immediately; check anesthesia record and surgical timeline for correlation before or while alerting |
| MEP | Loss of previously reproducible response, or sustained rise in stimulation threshold | Alert immediately — treat as more binary than SSEP; a partial amplitude drop with response still present is monitored closely but is not by itself the same signal as loss of response |
| Free-run EMG | Sustained neurotonic discharge (not brief burst) | Alert if sustained beyond a few seconds — brief bursts from routine retraction are common and not independently alarm-worthy |

**Post-alert sequence**

1. State the specific change (modality, side, % amplitude, % latency, onset time) to the surgeon in one sentence.
2. Cross-check anesthesia record timestamp against surgical-step timestamp — if the last anesthetic change was more than ~10 minutes earlier, treat the surgical maneuver as the more likely cause.
3. Repeat the recording after any corrective action (MAP increase, correction released, retractor repositioned) and re-run the same nerve/side to confirm recovery direction, not just "looks better."
4. Document time of alert, values at alert, corrective action taken, and time/values at recovery — this note is the case's medico-legal record of the monitoring response.
