# Public Safety Telecommunicator — Red Flags

### Breathing status unresolved past ~30 seconds of questioning
- **Usually means:** the caller is too panicked to check accurately, or is describing agonal (irregular, gasping) breathing without realizing it counts as "not breathing" for protocol purposes.
- **First question:** "Put your hand on their chest — is it moving up and down, yes or no?"
- **Data to pull:** elapsed time since call answer; if past 30 seconds with no clear answer, escalate toward arrest-protocol questioning rather than repeating the same question.

### Displayed location doesn't match caller's own description
- **Usually means:** a VoIP registered location that's gone stale, a wireless location fix with wide uncertainty, or a caller physically somewhere other than where the phone/account is tied to.
- **First question:** "Can you confirm the address you're at right now?"
- **Data to pull:** ANI/ALI record type (landline, wireless Phase I/II, VoIP registered) and its known accuracy tier for this call type.

### Caller volume/tone escalating instead of stabilizing after initial guidance
- **Usually means:** questions are too open-ended for the caller's stress level, or the caller senses the telecommunicator isn't tracking the urgency.
- **First question:** switch immediately to short, closed-ended, command-form questions ("Yes or no — is he breathing?") instead of open ones.
- **Data to pull:** none — this is a real-time communication-style correction, not a data lookup.

### Weapon, hazmat, or scene-safety mention buried inside a medical complaint
- **Usually means:** the caller led with the medical symptom and only mentioned the safety issue in passing, or assumed it was obvious.
- **First question:** "Is there a weapon there now?" / "Is anyone else in danger?" — ask explicitly, don't assume the card's medical questions will surface it.
- **Data to pull:** flag the case for law-enforcement co-response regardless of the medical determinant code.

### Non-English or unintelligible caller past the first exchange
- **Usually means:** language barrier, not necessarily medical incapacitation — don't assume the caller can't communicate at all.
- **First question:** activate three-way interpretation immediately rather than attempting single-word English prompts.
- **Data to pull:** which language, if identifiable from the first exchange, to route to the right interpreter line faster.

### Call goes silent or drops mid-interview
- **Usually means:** connectivity loss, caller incapacitation, or situation resolved — these require different responses and can't be distinguished without attempting contact.
- **First question:** attempt callback immediately; if no answer, check whether enough location/nature information was captured before the drop to dispatch on partial information.
- **Data to pull:** last confirmed location and nature captured before disconnect.

### Determinant code assigned but an independent safety signal contradicts the acuity level
- **Usually means:** the protocol card's medical logic and the actual scene-safety picture are answering two different questions — a low medical-acuity call can still be a high officer-safety call.
- **First question:** "Is the situation currently safe for you and for responders?"
- **Data to pull:** whether a co-responding unit (law enforcement) is needed regardless of the medical determinant code.

### Every ambiguous call over a shift trending toward the highest determinant tier
- **Usually means:** a defensive "always pick the worst case" habit rather than genuine case-by-case escalation — this degrades system-wide unit availability.
- **First question:** for the last several Echo/Delta assignments, would the next Key Question have actually ruled out the higher tier if asked before escalating?
- **Data to pull:** shift-level determinant-code distribution compared to historical baseline for the same call-type mix.

### Post-dispatch background questions delaying the pre-arrival instruction start
- **Usually means:** treating the script as strictly sequential even after the concurrent-dispatch moment has passed.
- **First question:** has compression/pre-arrival coaching started yet, or is the telecommunicator still working medical-history questions first?
- **Data to pull:** timestamp gap between dispatch transmission and first pre-arrival instruction — should be seconds, not the better part of a minute.
