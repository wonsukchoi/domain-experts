# Artifacts & templates

Filled examples, not descriptions. Numbers below are the "Converge" 650-attendee user conference from `SKILL.md`'s worked example, extended into the documents an event planner actually produces.

## RFP comparison grid

Normalize every venue proposal on the same rows before comparing headline room rate. Three venues bidding on the same 4-night, 650-attendee program:

| Term | Venue A (selected) | Venue B | Venue C |
|---|---|---|---|
| Room rate (ADR) | $219 | $199 | $235 |
| Room block (total nights) | 1,700 | 1,700 | 1,700 |
| Attrition threshold | 85% | 80% | 90% |
| Attrition base | full contracted block | full contracted block | block minus arrival/departure nights |
| Cutoff date | 30 days out | 21 days out | 45 days out |
| Comp room ratio | 1:45 | 1:50 | 1:35 |
| F&B minimum | $210,000 | $240,000 | $175,000 |
| AV | venue-exclusive (in-house) | venue-exclusive (in-house) | outside vendor permitted |
| Resort/facility fee | none | $18/room/night | none |
| Est. total cost per attendee | $2,050 | $2,180 | $1,960 |

**Read:** Venue B's lower room rate is offset by a stricter attrition base, a tighter cutoff, a higher F&B minimum, and a $18/night resort fee that doesn't show up until the master bill — its total-cost-per-attendee is the highest of the three despite the cheapest room rate. Venue C is cheapest per attendee and has the most favorable attrition base, but non-exclusive AV means production quality risk shifts onto the planner's own vendor vetting. Venue A was selected for the best balance of attrition base and F&B minimum sizing relative to this program's forecast, not for rate.

## Room-block pickup pacing tracker

Tracked weekly from block opening; the two checkpoints that matter are 75 days (last chance to file a formal block-reduction request under this contract's terms) and 30 days (cutoff).

| Checkpoint | Contracted requirement (85% of 1,700) | Actual pickup | Variance | Action |
|---|---|---|---|---|
| 120 days out | — (tracking only) | 410 | — | Monitor |
| 90 days out | — (tracking only) | 780 | — | Monitor |
| 75 days out | 1,445 (pace target: ~55%) | 890 (52%) | -3 pts vs. pace | **File block-reduction request if trend holds one more checkpoint — did not file; missed** |
| 60 days out | pace target: ~70% | 1,050 (62%) | -8 pts vs. pace | Marketing push to registered-not-booked list; still eligible to request reduction |
| 30 days out (cutoff) | 1,445 (100% of threshold) | 1,290 (76% of block) | short by 155 vs. threshold pace | Cutoff passes; unsold rooms released to public inventory; exposure now fixed pending final pickup |
| Event | 1,445 required | 1,390 final | **-55 room nights vs. threshold** | Settlement: attrition damages apply (see below) |

## AV production cost breakdown

Venue-exclusive AV package for a 3-day general session program plus 8 concurrent breakout rooms:

| Line item | Basis | Cost |
|---|---|---|
| General session production (LED wall, line-array audio, lighting, video switching, stage) | $45,000/day × 3 days | $135,000 |
| Breakout room AV (screen, audio, mic, confidence monitor) | 8 rooms × $1,200/day × 3 days | $28,800 |
| Webcast/streaming production (encoding, second-camera cut, on-demand capture) | flat package | $22,000 |
| **Total AV production** | | **$185,800** |

Reconcile this against the program design *before* signing the venue contract — general-session AV tier (single-camera vs. multi-camera switch, LED wall vs. projection) is the single largest lever on this number, and it is far cheaper to descope in the RFP stage than to renegotiate after signature.

## Post-event settlement worksheet

Final master bill reconciliation against every contracted minimum, before payment:

| Line item | Contracted term | Actual | Variance / settlement |
|---|---|---|---|
| Room revenue | 1,700 nights at $219 ADR | 1,390 nights picked up | $304,410 billed at actual pickup |
| Attrition damages | 85% threshold (1,445 nights), 80% ADR rebate on shortfall | 1,390 actual (55 short of threshold) | 55 × $219 × 0.80 = **$9,636** |
| F&B minimum | $210,000 | $184,300 spent | $25,700 shortfall + 24% service charge ($6,168) + 8% tax on shortfall+service charge ($2,549) = **$34,417** |
| AV production | $185,800 package (contracted flat rate) | as contracted, no overages | $185,800 |
| Comp rooms applied | 1,390 nights ÷ 45 = 30 comps owed | 30 applied, verified against folio | $0 net (confirm venue actually zeroed these — a common billing-error line) |
| Resort/facility fee | none in this contract | n/a | $0 |
| **Reconciled total (these lines only)** | | | **$534,263** |

This worksheet covers only the venue-contract lines; the full event budget (~$1,300,000, or ~$2,000/attendee at 650 attendees) also includes speaker fees, entertainment, staff travel, event-cancellation insurance, and the registration platform — none of which route through the venue master bill and none of which are subject to attrition or F&B-minimum clauses.
