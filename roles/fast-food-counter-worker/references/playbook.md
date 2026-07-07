# Playbook

Filled operational templates a front-counter worker executes directly at the register, headset, or kiosk-assist station — not descriptions of what they'd contain.

## Order-taking and read-back sequence (filled example, drive-thru headset)

| Step | Action | Spec | What breaks if skipped |
|---|---|---|---|
| 1 | Greet and take order verbally | Scripted greeting, no ad-lib substitutions | Sets guest expectation for pace |
| 2 | Enter each item and modifier into POS as spoken | One modifier per line, not bundled into free text | Bundled modifiers get missed by the kitchen display |
| 3 | Read the full order back to the guest | Item, size, and every modifier stated aloud, not just item names | Wrong modifiers reach the window uncaught |
| 4 | Run the suggestive-sell prompt once | One offer (upsize/combo/add-on) tied to what was ordered | A second attempt after a decline slows the line for no measurable gain |
| 5 | State the total and pull the guest forward | Total stated before card/cash is requested | Guest arrives at window unprepared to pay, adds delay there instead |

## Till count-in / count-out (filled example, $150 starting bank)

| Time | Task | Threshold / spec | Sign-off |
|---|---|---|---|
| Shift start | Count starting bank against posted amount | Must equal $150 exactly or logged as a variance before first sale | initials + count |
| During shift | Confirm register/terminal total matches ticket total before handing off change or receipt | Every transaction, no exceptions for a short line | — |
| Bank exceeds $200 over starting amount | Drop excess into the safe | Per store's drop threshold, not held at register | initials + drop amount |
| Shift end/handoff | Count bank against POS total for the login | ≤$1–2 variance: log and move on; recurring variance on the same login across shifts: flag to MOD | initials + variance |

## Suggestive-sell script (filled example)

| Order contains | Scripted prompt | Stop condition |
|---|---|---|
| Any entrée without a drink | "Can I get you a drink with that?" | Accept the first answer, yes or no |
| A single-size item (not already a combo) | "Want to make that a combo for $1.50 more?" | One offer only, even if declined |
| A combo or entrée with no dessert | "Add a [item] for $1.99?" | Do not repeat after a decline, regardless of shift attach-rate standing |

Target attach rate: roughly 30% of eligible orders taking at least one prompted add-on, tracked per register login over a shift — a shift average below about 15% usually means the prompt is being skipped, not that guests are uniformly declining; a rate above 45% for one worker against a store average near 30% is usually a sign the second-attempt rule is being ignored, not exceptional selling skill.

## Complaint-response ladder (counter-worker authority ceiling)

1. **Acknowledge without conceding fault** — "Let's get that fixed for you" — before discussing any remedy.
2. **Offer the standard remedy** (remake the item, replace a missing component, refund the specific item) — within the worker's own authorization ceiling, commonly items under about $5–10 without a manager PIN.
3. **If the guest declines the standard remedy or the item is above the ceiling**, call the MOD rather than authorizing anything beyond it yourself.
4. **If the complaint mentions illness, an injury, or a foreign object**, call the MOD immediately regardless of dollar amount or the guest's stated request — this tier is about exposure, not the size of the remedy.
5. **Log the outcome** (item, reason, remedy given) at the register or comp log before moving to the next order, not from memory at the end of the shift.

## Allergen-question response (filled example)

| Guest question | Correct response | Incorrect response |
|---|---|---|
| "Does the bun have sesame?" (known ingredient card answer: yes) | "Yes, the bun has sesame." | Guessing without checking the card |
| "Is the fry oil shared with anything with peanuts?" (not on the worker's reference card) | "Let me check with a manager before I answer that." | "I don't think so" or any hedge stated as fact |
| "Can you list every allergen in this sauce?" | Read directly from the ingredient card/app, verbatim | Paraphrasing from memory of a similar item |

The "Big 9" major allergens requiring disclosure if present: milk, eggs, fish, crustacean shellfish, tree nuts, peanuts, wheat, soybeans, and sesame (sesame added under the FASTER Act, effective January 2023).

## Order-accuracy vs. speed-of-service trade-off table (filled example, per-order seconds)

| Action | Time cost | Error-rate effect (this store's tracked data) |
|---|---|---|
| Verbal read-back | +4 sec/order | 8% → 2% error rate at window |
| Second bagger/runner called during a queue backup | 0 sec/order (parallel task) | No measured error-rate effect; reduces order-to-window time directly |
| Skipping suggestive-sell repeat after decline | 0 sec saved beyond the single prompt | N/A — prevents line-speed loss, not an accuracy lever |

Read this table as: the read-back is the one step with a real time cost that's worth paying every time; calling for support is the lever for the speed number that costs nothing in accuracy.
