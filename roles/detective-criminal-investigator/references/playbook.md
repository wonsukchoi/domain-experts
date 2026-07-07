# Detective / Criminal Investigator — Playbook

## Timeline reconciliation worksheet

Anchor every timestamp-dependent claim to at least one independently verified time source before building a case timeline.

| Source | Reported time | Independently verified? | Correction applied | Corrected time |
|---|---|---|---|---|
| Store DVR (robbery start) | 00:04:40 | No — consumer DVR clock, not network-synced | −12:42 (drift measured against POS log below) | 23:51:58 |
| Store POS system (reference transaction) | 23:48:10 | Yes — network-time-synced | none | 23:48:10 |
| Same POS transaction, as it appears on DVR footage | 00:00:52 | — (this is the drift-measurement pair) | — | — |
| Suspect's carrier text record | 23:52:00 | Yes — carrier network-synced, subpoenaed | none | 23:52:00 |
| 911 call (unrelated case, comparison example) | 23:47:02 | Yes — carrier-logged call time | none | 23:47:02 |

**Drift calculation:** same event (POS transaction) logged at 23:48:10 (verified) and 00:00:52 (DVR). Elapsed from 23:48:10 to 00:00:52 = 12 min 42 sec. DVR is running **12:42 fast**. Apply this correction to every other DVR-sourced timestamp in the case before comparing it to any other source.

**Distance/speed/time check, once timestamps are corrected:**

```
required_speed_mph = distance_miles / (elapsed_minutes / 60)
```

| Claim | Distance | Elapsed (corrected) | Required speed | Plausible for route/mode? |
|---|---|---|---|---|
| Suspect travels from tower location to scene | 6.1 mi | 2 sec (23:51:58 → 23:52:00) | ≈11,000 mph | No — physically impossible; alibi holds |

If required speed is within a plausible range for the route (e.g., under ~40 mph on surface streets, higher on a highway with no lights), the timeline does *not* clear the suspect — say so plainly rather than treating "tight" timing as automatically exculpatory or automatically incriminating.

## PEACE-model interview structure (filled example)

| Stage | Purpose | Example prompt used | What NOT to do here |
|---|---|---|---|
| Preparation and Planning | Review case file, identify what's known vs. unknown before the interview | (internal — no interviewee present) | Walking in without a documented list of what you need to learn |
| Engage and Explain | Establish rapport, explain the interview's purpose and structure | "I want to hear your account of the evening in your own words — I'll ask questions after." | Presenting evidence or your own theory before the account is given |
| Account | Open-ended account first, then targeted follow-up, then any inconsistencies raised without accusation | "Walk me through the evening starting from when you left work." → "You mentioned leaving at 6, but your card shows a purchase at 6:40 near the office — can you help me understand that?" | Leading questions ("You were near the office at 6:40, weren't you?") |
| Closure | Summarize what was said, give the interviewee a chance to add or correct | "Let me read back what I have — tell me if I've got anything wrong or missing." | Ending abruptly without a summary check |
| Evaluate | Assess the account against independently verified facts, decide what still needs verification | (internal — cross-reference against corrected timeline, records) | Treating the interview itself as the final verification step |

## Probable-cause affidavit element checklist (filled example)

| Element | Included? | Source | Exculpatory fact considered? |
|---|---|---|---|
| Physical description match to suspect | Yes | Witness description, cross-referenced to booking photo | Witness's initial 911 call described a different jacket color — noted and explained (suspect changed jackets per second witness) |
| Cell-site placement near scene at relevant time | Yes | CSLI, sector-level, ~1.8 mi radius | Sector radius stated explicitly — not overstated as pinpoint |
| Prior relevant record | Yes, if applicable | Records check | — |
| Corrected timeline consistency | Yes | Timeline reconciliation worksheet above | Any DVR-drift correction applied and shown, not silently omitted |
| Known fact cutting against guilt | **Must be affirmatively checked, not left blank by default** | Full case file review | E.g., a second witness's partial identification of someone else — included with context, not omitted |

**Fallback if a known exculpatory fact exists and the affidavit is time-sensitive:** include the fact with a brief characterization of its weight (e.g., "a second witness offered a partial identification of another individual, but was unable to view the suspect directly and described lighting conditions as poor") rather than either omitting it or delaying the affidavit indefinitely. Silence on a known fact is the higher-risk path.
