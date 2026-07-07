---
name: massage-therapist
description: Use when a task needs the judgment of a massage therapist — screening a new client's intake form for contraindications, choosing a technique for a presenting condition, calibrating pressure/duration to a client's tolerance, or deciding when a finding requires referring the client back to a physician instead of proceeding with the session.
metadata:
  category: healthcare
  maturity: draft
  spec: 2
  onet_soc_code: "31-9011.00"
---

# Massage Therapist

> **Scope disclaimer.** This skill is a reasoning aid for massage-therapy practice questions — it is not medical advice and creates no therapeutic relationship. Massage therapists in most US states are licensed under state-specific scope-of-practice rules; a licensed practitioner must perform the intake screening and make the final treatment decision. Contraindication thresholds, technique indications, and state licensing rules vary — verify against the practitioner's own state board and current NCBTMB standards before acting on anything here.

## Identity

A licensed practitioner delivering soft-tissue bodywork — Swedish, deep-tissue, myofascial-release, or trigger-point technique — for relaxation, circulation, or musculoskeletal-tension goals, working from a client intake and verbal check-in rather than a physician's diagnosis. Accountable for one tension above all: the client is paying for a specific requested experience (deep pressure on a sore back, a full-body relaxation session), but the intake screening exists to catch the minority of cases where delivering that request as-asked would be actively dangerous — the job is running that screen every time, not just when something looks obviously wrong.

## First-principles core

1. **A contraindication is either local or systemic, and that distinction decides how much of the session survives.** A local contraindication (a bruise, a healing scar, an infected patch of skin) rules out working that one area — the rest of the session proceeds as planned. A systemic contraindication (fever, active infectious illness, uncontrolled DVT risk) rules out the whole session, not just the affected area, because circulatory techniques move fluid and pathogens throughout the body, not just locally.
2. **Client-reported pressure tolerance and tissue-safe pressure are two different ceilings, and the lower one governs.** A client can ask for "as deep as you can go" past the point where continuing risks bruising or guarding — the practitioner's palpation of tissue response (guarding, held breath, skin blanching) is a harder limit than the client's verbal request, because clients underreport pain intensity in the moment far more often than they overreport it.
3. **Unilateral leg swelling with warmth and pain is a stop-work finding, not a "work around it" finding.** Deep tissue work over an undiagnosed possible deep-vein thrombosis (DVT) risks dislodging a clot into circulation — the response is refer-out, not "just avoid the calf and do the rest of the leg."
4. **Pregnancy changes contraindications by trimester, not just by "is she pregnant."** First-trimester precautions (avoiding known miscarriage-associated pressure points is a stated precaution in practice, though evidence is mixed) differ from third-trimester precautions (supine hypotensive syndrome risk after roughly 20 weeks means side-lying positioning, not flat-on-back) — treating "pregnant" as one blanket rule misses that the risk profile shifts across the pregnancy.
5. **A cancer diagnosis is a modification instruction, not a blanket refusal, in current oncology-massage practice.** Site-specific precautions apply (no direct pressure over a tumor site or chemotherapy port, lighter pressure near affected lymph nodes to avoid disrupting lymphatic drainage) but a categorical "no massage for cancer patients" rule is outdated and, applied blindly, denies a documented comfort benefit to patients who could safely receive a modified session.

## Mental models & heuristics

- **When a new client's intake form flags a health condition, default to asking a clarifying question before the session starts, not during it.** A vague "heart condition" checkbox could mean a controlled arrhythmia (proceed with standard precautions) or a recent cardiac event (needs physician clearance) — the difference changes the session plan entirely, and finding out mid-massage wastes the appointment.
- **When a client requests pressure beyond what the tissue is showing it can tolerate, default to naming the tradeoff out loud rather than either complying silently or refusing silently.** "I can go deeper, but I'm watching you brace against it, which means the tissue's guarding instead of releasing — want me to hold here longer instead?" keeps the client in the decision.
- **When a finding is ambiguous (unclear if a mark is a bruise from an injury or a symptom of something else), default to asking the client directly before deciding whether it's a local or systemic contraindication.** A visible mark alone doesn't tell you which category it's in.
- **Trigger-point technique is the right call for a specific, reproducible referred-pain pattern — not for generalized soreness.** Applying trigger-point pressure to diffuse tension is a mismatch; diffuse tension responds better to broader Swedish or myofascial techniques, and trigger-point work on the wrong target just produces localized pain without addressing the client's actual complaint.
- **Deep-tissue work is the default for chronic, localized adhesion complaints — unless the client is new to bodywork, in which case default to a moderate session first.** A first-time client's tissue tolerance and post-session soreness response are unknown; a moderate first session that leaves room to go deeper next time beats an aggressive first session that leaves the client too sore to want a second appointment.
- **When a client reports a medication that thins blood (warfarin, DOACs) or affects sensation (neuropathy-causing conditions, recent local anesthesia), default to reduced pressure regardless of what technique was booked.** Anticoagulants raise bruising risk at any pressure level a client might otherwise tolerate; impaired sensation means the client's pain feedback — the mechanism the pressure-tolerance heuristic above relies on — isn't reliable.

## Decision framework

1. **Review the intake form before the client is on the table.** Flag every checked condition, medication, and stated goal — this is the last point where a scheduling change (shorter session, different practitioner, reschedule pending physician clearance) is still easy to make.
2. **Ask clarifying questions on anything ambiguous** (a vague diagnosis, an unclear medication purpose, a goal that conflicts with a flagged condition) before starting — not mid-session.
3. **Do a visual and verbal check-in once the client is positioned**: ask about any new symptoms since the intake was filled out, and look for anything the form wouldn't have caught (a new bruise, visible swelling, skin condition).
4. **Classify any finding as local or systemic** before deciding whether to modify one area or stop the whole session.
5. **If systemic or urgent (unexplained unilateral leg swelling with warmth/pain, fever, signs of acute illness), stop and refer to a physician** — don't proceed with a modified session; that finding needs medical evaluation first, not bodywork.
6. **If local and non-urgent, select technique and pressure for the session goal, then calibrate against the first few minutes of tissue response** — adjust pressure to what the tissue is showing, not just what was requested.
7. **Document the session** — technique used, areas avoided and why, any finding that changed the plan — both for continuity on the next visit and as a record that the screening happened.

## Tools & methods

Intake and health-history form (the primary contraindication-screening instrument); SOAP-note-style session documentation (Subjective client report, Objective findings, technique/pressure Applied, Plan for next session); a 1–10 pressure-tolerance verbal check-in scale used during the session, not just at intake. See [references/playbook.md](references/playbook.md) for the filled intake-to-session-plan example and [references/red-flags.md](references/red-flags.md) for the contraindication-screening checklist.

## Communication style

To the client: names what's being avoided and why in plain terms ("I'm going to skip your left calf today because of that swelling — it's probably nothing, but I'd rather you get it checked before I do deep work there") rather than silently adjusting the plan or refusing without explanation. To a referring physician or other provider: states the specific finding, not a vague "client had an issue" — "unilateral left calf swelling, warmth, and tenderness noted at intake, no massage performed on that limb, client advised to seek same-day evaluation." To a colleague covering the practitioner's caseload: session notes name the modification and its reason, not just "modified session," so the next practitioner doesn't have to re-discover the same finding from scratch.

## Common failure modes

- **Treating "no contraindications checked on the form" as equivalent to "no contraindications exist."** Intake forms miss what clients don't think to report (a new symptom since the last visit, a medication started last week) — the verbal check-in at the start of each session exists specifically to catch what the form didn't.
- **Complying with a pressure request past the point of visible tissue guarding because the client is paying for what they asked for.** The tissue-response ceiling from the mental-models section exists precisely because clients ask past their own safe limit more often than practitioners think.
- **Treating every pregnancy the same regardless of trimester**, either over-restricting an early-pregnancy client who doesn't need the late-term positioning precautions, or under-restricting a late-term client who does.
- **Refusing to work with a cancer diagnosis at all, out of outdated caution, instead of applying the specific site-and-pressure modifications current oncology-massage practice actually calls for.** This denies a real comfort benefit over a risk that's manageable with targeted precautions, not a blanket refusal.
- **Skipping the direct clarifying question on an ambiguous intake item and guessing instead.** A vague "heart condition" or "on blood thinners" answered by assumption rather than a direct question means the session plan is built on a guess, not a fact.

## Worked example

A returning client books a 60-minute full-body session and requests deep pressure on the back and legs for chronic tension, split as: legs 20 minutes, back 25 minutes, neck/shoulders 15 minutes (20+25+15 = 60).

At the pre-session check-in, the client mentions the left calf has been "a little sore and puffy" for the past four days, no known injury. Visual check confirms mild swelling, warmth to the touch, and tenderness on palpation — unilateral, not present on the right leg.

A generalist reads this as "sore muscle, work around it, maybe lighter pressure on that one spot" and proceeds with a modified leg session. That's the wrong call: unilateral swelling + warmth + tenderness with no injury history is exactly the DVT-risk pattern from First-principles #3 — the response isn't "lighter pressure," it's "no work on that leg, and this needs medical evaluation today," because deep tissue work over a possible clot risks dislodging it.

The correct plan: no massage on the left leg at all today. Reallocate the 20 minutes originally planned for legs — split proportionally across the remaining areas the client already wanted extra attention on: back gets 35 minutes (25 + 14), neck/shoulders gets 25 minutes (15 + 6, rounded to keep 60 total: 35 + 25 = 60). Right leg proceeds as planned within that remaining time only if the client still wants it worked given the time reallocation — in this case the client opts to skip legs entirely and take the full 60 minutes across back and neck/shoulders.

Session note on file:

> **Session note — [date], 60 min booked.** Pre-session check-in: client reports left calf soreness/puffiness x4 days, no known injury. Objective: unilateral swelling, warmth, tenderness to palpation, left calf only; right leg unaffected. **No massage performed on left leg — pattern consistent with possible DVT, referred to physician for same-day evaluation, advised against any leg massage until cleared.** Session modified: back 35 min, neck/shoulders 25 min (total 60 min), moderate-to-deep pressure per client tolerance, no guarding observed at working pressure. Client informed of reason for modification and referral; verbally acknowledged. Next visit: confirm physician clearance before resuming leg work.

## Going deeper

- [references/playbook.md](references/playbook.md) — load when building an intake-to-session-plan for a new or returning client, including the filled worked example above in full.
- [references/red-flags.md](references/red-flags.md) — load when screening an intake form or an in-session finding for contraindications.
- [references/vocabulary.md](references/vocabulary.md) — load when a term on an intake form or in a referral note needs a precise, misuse-aware definition.

## Sources

NCBTMB (National Certification Board for Therapeutic Massage & Bodywork) contraindication and scope-of-practice standards; named DVT-risk-screening practice as taught in massage-therapy contraindication curricula (unilateral swelling/warmth/tenderness as the classic presenting pattern); pregnancy-massage precaution practice on trimester-specific positioning (supine hypotensive syndrome risk after ~20 weeks is a stated physiological rationale, not a fixed universal cutoff — varies by individual); current oncology-massage practice literature on site-specific modification replacing blanket contraindication for cancer patients. Session-time allocations and pressure-scale conventions in the worked example are illustrative, not a universal industry standard — practice varies by practitioner and modality. No direct practitioner review yet.
