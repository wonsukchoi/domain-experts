# Playbook

Filled reference tables and step sequences for the recurring judgment calls in the role. These are the numbers to check against, not descriptions of what to check.

## Body condition scoring (BCS)

### Beef cattle — 1–9 scale (Purdue/Texas A&M Extension standard)

| Score | Description | Target production stage |
|---|---|---|
| 1–2 | Emaciated, spine/ribs/hooks visible with no fat cover | Never a target; immediate intervention |
| 3 | Thin, some muscle wasting visible | Never a target |
| 4 | Borderline, ribs faintly visible | Acceptable only for open (non-pregnant) cows on maintenance ration |
| 5 | Moderate, smooth appearance over ribs | Target at calving for mature cows |
| 6 | Good, smooth fat cover over ribs and around tailhead | Target at calving for first-calf heifers and breeding bulls |
| 7 | Fleshy, some patchiness of fat evident | Acceptable pre-breeding, not sustained |
| 8–9 | Obese | Never a target; fertility and calving-ease risk |

**Rule of thumb:** score at weaning, pre-breeding, and 60–90 days pre-calving. A drop of more than 1 full point between any two checkpoints, with no ration change, triggers the population-vs-individual triage (SKILL.md decision framework step 1) before assuming it's one animal's issue.

### Dairy cattle — 1–5 scale (Edmonson et al., 1989)

| Score | Calving-window target | Risk if outside range |
|---|---|---|
| <2.0 | Never acceptable at calving | Ketosis, metritis, retained placenta risk sharply elevated |
| 2.5–3.25 | Target at calving | — |
| >3.75 | Avoid at calving | Dystocia, fatty liver risk |

## Dissolved oxygen (DO) response protocol — warmwater pond aquaculture

| DO reading (mg/L), dawn check | Status | Action |
|---|---|---|
| >5.0 | Healthy | Routine feeding, standard dawn/dusk log |
| 3.0–5.0 | Watch | Stand by aerators; recheck at 2-hour intervals through the morning |
| 2.0–3.0 | Elevated risk | Run all installed aeration continuously; hold feed until >4.0 mg/L confirmed |
| <2.0 | Crisis | Emergency aeration (see horsepower table below), feed withheld, recheck every 2 hours, call emergency aeration service if installed capacity is below the biomass requirement |
| <1.0 for 2+ hours | Active fish-kill event | All available aeration and water exchange; historical mortality in dense ponds runs 20–30% (SRAC data) |

**Emergency aeration horsepower guideline:** 1.0–1.5 HP per 1,000 lb of standing biomass during a crisis response (routine, non-crisis aeration is typically lower, around 0.5–1.0 HP per 1,000 lb). Example: a pond holding 97,500 lb of fish needs 97.5–146.25 HP in crisis; installed capacity should be checked against this range whenever stocking density is increased, not just at initial pond design.

**Highest-risk conditions:** consecutive hot days followed by a cloudy or overcast day (algae photosynthesis drops, but respiration and decomposition continue), recent algae bloom die-off, and any night with low wind (no surface mixing). Dawn is the daily low point — the last DO reading before sunrise is the one that matters, not the prior evening's.

## Quarantine and biosecurity sequencing — new animal introduction

| Day | Action |
|---|---|
| 0 | Animal arrives at isolation pen/pond, physically separated (minimum 10 ft or a water-source break for aquaculture) from resident population. Health certificate and transport record filed. |
| 0–1 | Visual and temperature baseline recorded. Footbath/boot-change protocol enforced for anyone entering isolation area before returning to the main population. |
| 7–14 | Interim health check: BCS or size/condition check, any discharge or lesion noted, temperature recheck. |
| 21 | Minimum release point for tested, low-risk introductions with clean interim checks — only with a veterinarian's written sign-off. |
| 30 | Standard default release point absent a veterinarian's shortened clearance. |
| Any point | Any transmissible sign (discharge, diarrhea, lesion, unexplained mortality in isolation group) resets the clock and moves the animal to isolation protocol rather than release, regardless of days already served. |

**Never:** release on schedule alone if an interim check flagged a concern; the calendar is a minimum, not a guarantee.

## Feed conversion ratio (FCR) benchmarks

| Species/system | Target FCR (feed:gain) | Escalation trigger |
|---|---|---|
| Channel catfish (pond) | 1.8–2.2:1 | >10–15% above 30-day rolling average with stable ration = investigate water quality/subclinical illness before assuming feed-quality issue |
| Tilapia (pond) | 1.6–1.8:1 | Same trigger threshold as catfish |
| Feedlot beef cattle | 6–8:1 | >10% above trailing 30-day average with stable ration = check for parasite load, water trough access, or heat stress before assuming ration problem |
| Broiler poultry | 1.6–1.8:1 | >10% deviation = check housing temperature and water access first |

**Worked check:** a catfish pond fed 1,000 lb of feed over 30 days that gained 480 lb of biomass has an FCR of 1,000 ÷ 480 = 2.08:1 — inside the 1.8–2.2 target band, no escalation. The same pond fed 1,000 lb producing only 400 lb of gain is at 2.5:1, roughly 20% above the band ceiling — escalation trigger met, pull the DO log and mortality count before assuming a feed-quality problem.

## Stocking density vs. installed aeration

| Species | Published density ceiling (no supplemental aeration beyond standard) | Density ceiling with added mechanical aeration |
|---|---|---|
| Channel catfish | ~3,000–4,000 fish/acre | Up to ~8,000 fish/acre with adequate HP/1,000 lb ratio maintained |
| Tilapia | ~2,000–3,000 fish/acre | Up to ~5,000 fish/acre with adequate aeration |

**Rule:** before increasing stocking beyond the unaided ceiling, confirm installed aeration HP against the biomass the higher density will produce at harvest weight, not at stocking weight — biomass at harvest is what determines oxygen demand, and it can be 5–8x the stocking-day figure.

## Low-stress handling — point-of-balance sequence

1. Approach the animal from outside its flight zone (the distance at which it first reacts to your presence — widens with fear/inexperience, narrows with habituation).
2. Enter the flight zone at an angle behind the point of balance (roughly the shoulder) to move the animal forward; enter in front of the point of balance to stop or back it up.
3. Move in a zigzag pattern parallel to the direction of desired travel rather than directly at the animal from behind — direct pressure from directly behind triggers circling, not forward movement.
4. At a repeated balk point in a chute or alley, stop and check for a shadow, a drain grate, a reflection, or a color/texture change at the animal's eye level before applying more pressure — the fix is almost always the facility, not the animal.
5. Never use an electric prod as the first tool; reserve it for a genuinely stalled, safe-to-approach animal after the facility check in step 4 has been ruled out.
