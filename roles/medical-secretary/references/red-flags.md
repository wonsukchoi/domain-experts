# Medical Secretary — Red Flags

### Prior-authorization request submitted more than 2 business days after the order arrived
- **Usually means:** front-desk queue backlog, or the order wasn't flagged as auth-required at intake.
- **First question:** does this insurer/procedure combination have a known additional-info-request rate high enough that the remaining runway is already insufficient?
- **Data to pull:** the practice's auth-denial log for this insurer and procedure type over the last 12 months.

### Appointment booked more than 30 days out with no re-verification scheduled
- **Usually means:** the original eligibility check was treated as permanent instead of a snapshot.
- **First question:** is a 48–72-hour pre-visit re-verification on the calendar?
- **Data to pull:** original verification date and the payer's typical re-enrollment/plan-change cycle.

### Records-release request with no specific date range or record type named
- **Usually means:** either an inexperienced requestor or an attempt to get broader access than intended.
- **First question:** what specifically does the authorization document say is in scope?
- **Data to pull:** the signed authorization form or subpoena language, verbatim.

### Visit reason on the schedule doesn't match the diagnosis implied by the referring order
- **Usually means:** either a benefit-type mismatch (preventive vs. problem-focused) or a documentation error upstream.
- **First question:** has this been confirmed with the ordering clinician, or is it an assumption made to keep the schedule moving?
- **Data to pull:** the original order/referral document and the patient's stated reason for visit.

### Same-day urgent request arrives with zero open slots and no buffer slot remaining
- **Usually means:** the day's buffer capacity was already consumed by non-matching "urgent" requests earlier in the day.
- **First question:** does this request actually match the practice's defined urgent-symptom list, or is it being escalated on patient insistence alone?
- **Data to pull:** the urgent-symptom list and today's buffer-slot usage log.

### Psychotherapy notes included in a general records release
- **Usually means:** the release was pulled by date range/patient rather than by authorized record type, sweeping in notes that require separate authorization.
- **First question:** was psychotherapy-notes access specifically and separately authorized?
- **Data to pull:** the authorization document's exact language on record types covered.

### Prior-authorization denial received the week of the appointment
- **Usually means:** either the worst-case timeline wasn't planned for, or required documentation wasn't attached at submission.
- **First question:** what specifically did the denial cite as missing or insufficient?
- **Data to pull:** the denial letter/notice and the original submission packet for comparison.

### Patient reports a different insurance plan at check-in than what was verified at booking
- **Usually means:** a coverage change between booking and visit that the re-verification window should have caught — or re-verification wasn't done.
- **First question:** was the visit re-verified within the 48–72-hour window, and if so, why didn't it surface this?
- **Data to pull:** the re-verification log entry (or its absence) for this appointment.

### A clinician asks the front desk to "just pick a code" for an ambiguous visit
- **Usually means:** time pressure is being used to bypass the coding-clarification step.
- **First question:** can this wait 24 hours for the clinician to confirm, or does the visit need to be rescheduled instead of coded incorrectly?
- **Data to pull:** the referring order and any prior visit history that might disambiguate the visit type.
