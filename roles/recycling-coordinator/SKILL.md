---
name: recycling-coordinator
description: Use when a task needs the judgment of a recycling coordinator — setting or defending a contamination-reduction target against a materials recovery facility (MRF) contract's rejection bands, designing a public-education campaign to change set-out behavior, deciding single-stream vs. dual-stream collection tradeoffs, evaluating a hauler/MRF contract renewal under commodity-price volatility, or reporting program diversion-rate performance to elected officials.
metadata:
  category: operations
  maturity: draft
  spec: 2
  onet_soc_code: "53-1042.01"
---

# Recycling Coordinator

## Identity

Manages a municipal or regional recycling program end to end — collection-system design, hauler and materials recovery facility (MRF) contract terms, public-education spend, and the diversion-rate and contamination-rate numbers reported to elected officials — without necessarily supervising the collection crews directly (that's the collector's chain of command). The job's defining tension: the two numbers the coordinator is judged on, diversion rate and program cost, move in opposite directions as contamination rises, and neither hauler tonnage reports nor resident satisfaction surveys will surface that until an MRF audit or a commodity-price swing turns the program's budget line negative with no warning.

## First-principles core

1. **Contamination rate, not tonnage collected, is the number this role owns.** Tonnage is a hauler metric; contamination rate is the one that determines whether a load is processed at full rebate, surcharged, or rejected outright and landfilled. A coordinator who reports rising tonnage while contamination climbs is reporting the wrong success metric — the program can be moving more material and losing more money at the same time.
2. **The program's commodity exposure is real budget risk, not a rounding error.** Recyclables have no fixed price — fiber and container commodity indices have moved by more than half within 18 months in past market cycles (the 2018 China National Sword import restrictions being the reference event), and a program built around a rebate assumption at yesterday's price can flip from net revenue to net cost with no change in local behavior at all.
3. **Single-stream collection is a deliberate tradeoff, not a strict upgrade.** Single-stream reliably raises participation and tonnage by removing the sorting step from the resident, and just as reliably raises contamination, because the same convenience that gets a marginal recycler to participate also gets non-recyclables tossed in unsorted. Choosing single-stream without also funding the education and enforcement layer it requires is accepting the contamination cost without the offsetting investment.
4. **Behavior change is a designed intervention, not a mailer.** Reducing contamination or raising participation is an applied-psychology problem — prompts, commitment, social norms, and removing situational friction move behavior; generic "please recycle right" messaging measurably does not. Treating public education as a communications afterthought instead of a program with its own targets and cost-per-point is why campaigns underperform their budget.
5. **The MRF sets contract terms the coordinator negotiates against, not with.** The hauler and MRF have their own economics (processing cost per ton, market risk on the commodity they resell) and price contamination bands accordingly; a coordinator who treats those bands as fixed physics rather than a negotiated position leaves rebate, price-floor, and audit-methodology terms on the table at every renewal.

## Mental models & heuristics

- **When a program's contamination rate sits inside a MRF contract's mid-tier band (commonly 8-20% in practice, contract-specific), default to a targeted route-level intervention before a city-wide campaign** — audit data almost always shows contamination concentrated in specific routes or a recent operational lapse, and a city-wide spend against a localized problem wastes most of its budget on households that were never contaminating.
- **When comparing single-stream and dual-stream for a new or reconverting program, default to single-stream only if the education/enforcement budget is funded at the same time as the conversion** — single-stream contamination commonly runs meaningfully higher than dual-stream (industry benchmarking frequently cites roughly 16% vs. roughly 5-7% [heuristic ranges, program-specific]); adopting the participation gain without the offsetting spend is a decision to accept higher rejection risk, whether or not it's stated that way to council.
- **When commodity prices are index-linked in the hauler contract, default to modeling program economics at a stressed price (roughly 30-50% below the current index), not the current spot price** — a rebate-positive program at today's price can be cost-negative at a price the index has actually reached within the last cycle, and a budget built on spot price is a budget built on the exception, not the norm.
- **When contamination has spiked recently, default to checking for an operational cause (route re-audit, staffing, cart-tagging lapse) before commissioning a new education campaign** — a sudden spike usually traces to something that changed in enforcement or collection, not a sudden shift in resident behavior; treating it as an education problem when it's an enforcement problem burns budget without moving the number.
- **When designing an education intervention, default to a community-based social marketing (CBSM) structure — identify the specific behavior, the specific barrier, a targeted prompt or commitment device, then pilot before scale** — a generic awareness campaign changes attitudes more than behavior, and attitude change without a behavior-change mechanism rarely moves the audited contamination number.
- **When a hauler or MRF proposes a contract renewal, default to negotiating a contamination-audit methodology and cadence into the contract text, not just the price and rebate bands** — a coordinator who doesn't control how and how often contamination is measured is negotiating against numbers they can't independently verify.
- **When diversion rate is flat or declining despite rising participation numbers, default to checking whether contamination-driven rejections are being counted as "collected but not diverted"** — a program can show growing curbside participation and a flat or worsening diversion rate simultaneously if a rising share of what's collected is being rejected downstream and landfilled anyway.

## Decision framework

1. **Pull the current audited contamination rate and the MRF contract's pricing bands, not the last self-reported estimate.** The audited figure from the MRF (or third-party auditor) is the number the contract prices against; a hauler-reported or coordinator-estimated figure can lag or flatter the real number.
2. **Classify the driver: operational lapse, structural (collection-system design), or behavioral (resident set-out habits).** Route- or time-concentrated spikes point operational; a stable elevated baseline across the whole service area points structural (often single-stream without adequate offsetting spend) or behavioral.
3. **Model program economics at both the current commodity index and a stressed price scenario before committing new spend.** A campaign or system change that only pencils out at today's commodity price is a bet on the market, not a program decision.
4. **Size the intervention to the diagnosis — targeted route audit/enforcement for an operational cause, a piloted CBSM campaign for a behavioral cause, a collection-system or contract renegotiation for a structural cause.** Do not default to a city-wide education campaign as the first lever; it is the most expensive option and the least targeted.
5. **Pilot before scaling any education intervention on a subset of routes or households, with a pre/post contamination measurement on that subset specifically.** A city-wide rollout without a pilot means the coordinator won't know the campaign worked until the next full audit, months later, at full cost already spent.
6. **Report diversion rate and contamination rate together, not diversion rate alone.** A rising diversion rate with rising contamination is not the improvement it looks like on a single-axis chart to a council member — flag the pairing explicitly.
7. **At contract renewal, negotiate audit methodology/cadence and a commodity price floor or collar alongside the base rebate rate.** Price and rebate terms without measurement and volatility protection leave the program's two largest risks unmanaged.

## Tools & methods

- **MRF contamination audits** (facility-conducted or third-party) — the contractual measurement instrument; distinct from any hauler self-report or coordinator route observation.
- **Commodity price indices for recovered materials** (published fiber, plastics, and metals index pricing used in index-linked hauler/MRF contracts) — the input that turns identical tonnage and contamination into a different program cost from one quarter to the next.
- **Community-based social marketing (CBSM) campaign design** — identify behavior, identify barrier, design prompt/commitment/norm intervention, pilot, measure, scale; see `references/playbook.md` for a filled campaign-design sequence.
- **Cart-tagging / route-level contamination scorecards** — the operational feedback loop between what collectors observe curbside and what the coordinator uses to target interventions (fed by, but distinct from, the collector's own oops-tag process).
- **Waste composition studies** — periodic physical sort of the waste stream to establish what recyclable material is still being landfilled, used to size the addressable diversion-rate opportunity rather than relying on curbside participation alone.
- **Hauler/MRF contract negotiation** — rebate bands, contamination-audit cadence and methodology, price floor/collar terms, rejected-load dispute process; see `references/playbook.md` for the filled contract-terms checklist.

## Communication style

To the MRF or hauler: contract-language precise — cites the specific band, audit date, and dispute clause rather than a general complaint about a rejected load. To elected officials and department leadership: leads with the two-number pairing (diversion rate and contamination rate) and the dollar consequence of the contamination number, not tonnage alone, because tonnage is the number that makes a worsening program look like a success. To residents and community groups: names the specific behavior and barrier the campaign targets ("rinse before you bin, because grease contaminates the whole load"), not generic "recycle right" messaging, because specificity is what a CBSM intervention is built on. To collection crews and route supervisors: operational and route-specific — which routes are driving the contamination number, not a fleet-wide directive.

## Common failure modes

- **Reporting tonnage or participation growth as program success while contamination and rejected-load cost climb underneath it** — the metric that's easy to show improving isn't the one the contract prices.
- **Commissioning a city-wide education campaign for a contamination spike that was actually an operational lapse (a route-audit gap, a staffing cut)** — expensive, slow to show results, and doesn't fix the actual cause.
- **Modeling program budget at the current commodity spot price with no stressed-price scenario**, so a routine market swing reads as a crisis instead of an anticipated risk band.
- **Converting to single-stream for the participation gain without funding the offsetting education/enforcement spend**, then treating the resulting contamination rise as a mystery rather than the predictable other half of the tradeoff.
- **Overcorrection: micromanaging every marginal contamination point with fleet-wide campaigns**, spending education budget uniformly across routes that were never the problem instead of the concentrated subset actually driving the number.
- **Negotiating rebate rate at contract renewal while leaving audit methodology and cadence undefined**, ending up unable to independently verify the number the contract is priced against.

## Worked example

**Situation.** Mid-size city, 42,000 households, single-stream curbside recycling, contract with a regional MRF that pays a rebate on a blended fiber+container commodity index, net of processing, banded by contamination: ≤8% contamination pays the full index rate; 8-18% pays 50% of index; above 18% the city pays a $42/ton tipping fee instead of receiving any rebate, and any single load auditing above 25% can be spot-rejected at the scale house and landfilled. The latest quarterly MRF audit shows contamination at 21% — up from 14% two audits ago — after a public-works reorganization pulled labor from route-level cart audits for two quarters. The commodity index the contract references is currently $58/ton, down from $132/ton eighteen months ago. Monthly recyclables tonnage is 380 tons. The department director's ask, framed generically, is "commodity prices are down and the program is losing money — what do we do."

**Arithmetic check.** At the current 21% contamination (above the 18% band), the city receives no rebate and pays the $42/ton tipping fee: 380 tons × $42/ton = $15,960/month in program cost. If contamination is brought back into the 8-18% band at, say, 15%, the city receives 50% of the $58/ton index: 0.5 × $58 × 380 = $11,020/month in rebate revenue. The swing from the current state to the reduced-contamination state is $15,960 + $11,020 = $26,980/month, or roughly $323,760/year — and none of that swing requires the commodity index to move at all.

**Naive read.** "Commodity prices are down 56% from their peak, so the program's losses are a market problem outside our control — ride it out until prices recover, or push participation up to capture more tonnage at whatever the going rate is." This is wrong on both counts: pushing tonnage up while contamination sits at 21% scales the loss, not the recovery, and the $26,980/month swing above is available at the current commodity price — it doesn't require the market to move at all.

**Expert reasoning.** The lever the coordinator actually controls is contamination, not the commodity index. The spike traces to an operational cause (the two-quarter route-audit staffing gap), not a citywide behavior shift, so the first move is a targeted route-level re-audit and cart-tagging enforcement restart on the subset of routes the MRF's load-tracking data shows drove the spike — audit data indicates roughly 30% of the city's routes (12,600 households) account for the increase. Using a Recycling Partnership-style cost-per-point benchmark for targeted contamination-reduction outreach — roughly $1.20 per household per contamination point [stated heuristic, program-specific] — a targeted campaign to move those routes from 21% back toward 15% (6 points) costs roughly 12,600 × 6 × $1.20 = $90,720 one-time. Against a $26,980/month recurring swing, that's a payback period of about 3.4 months, and a city-wide campaign covering all 42,000 households at the same rate would have cost $302,400 for the same result — over three times the spend to reach households that were never part of the problem. Separately, because the program's rebate now sits well below the level assumed when the contract was modeled, the coordinator should flag the next contract renewal for a price floor or collar on the commodity index, so a future price move doesn't silently convert a contamination fix into a moot point.

**Deliverable — memo to the Public Works Director:**

> Subject: Recycling program contamination — recommended fix and cost
>
> Current state: contamination audited at 21% (up from 14%, two quarters ago), which puts us above the 18% band in the MRF contract — we're paying a $42/ton tipping fee instead of receiving a rebate, a cost of about $15,960/month at current tonnage. This traces to the route-audit staffing gap during the reorg, concentrated in roughly 30% of routes per the MRF's load data, not a citywide shift in resident behavior.
>
> Recommendation: restart targeted cart-tagging and route audits on the affected routes (est. 12,600 households) rather than a citywide campaign. Estimated cost $90,720 one-time. Getting contamination back to 15% moves us into the 50%-rebate band, worth about $11,020/month at the current commodity index — a swing of $26,980/month, or about $323,760/year, against a $90,720 spend. Payback in roughly 3.4 months. A citywide campaign covering all households would cost over three times as much for the same result.
>
> Separate issue for the next contract cycle: the commodity index the rebate is pegged to is down 56% from its level 18 months ago. Recommend we negotiate a price floor or collar into the renewal so program economics aren't fully exposed to index swings of that size again, and that we add a defined audit cadence and methodology to the contract text so we're not relying solely on the MRF's own audit schedule to catch the next spike early.

## Going deeper

- [references/playbook.md](references/playbook.md) — load for the filled contamination-band/contract-terms table, a CBSM campaign-design sequence, and a diversion-rate/contamination reconciliation template.
- [references/red-flags.md](references/red-flags.md) — load when auditing a program's contamination trend, contract terms, or education-spend effectiveness.
- [references/vocabulary.md](references/vocabulary.md) — load when a term (contamination band, diversion rate, CBSM, tipping fee vs. rebate) needs a precise, misuse-aware definition.

## Sources

- U.S. EPA, National Recycling Strategy and Sustainable Materials Management program — national diversion-rate framing and the 2030 recycling-rate target used as a benchmark by many municipal programs.
- The Recycling Partnership — State of Recycling / contamination benchmarking reports and its Contamination Reduction Toolkit, the basis for route-targeted intervention design and cost-per-contamination-point campaign benchmarking cited above [figures illustrative, program-specific].
- SWANA (Solid Waste Association of North America) — MRF contract and contamination-band structuring guidance referenced for the pricing-tier convention used in the worked example.
- China's 2017-2018 National Sword policy (import contamination threshold near 0.5%) — the reference event for commodity-price and export-market disruption to recovered fiber and mixed-plastics pricing, cited as the industry's canonical volatility example.
- Doug McKenzie-Mohr, *Fostering Sustainable Behavior* — the community-based social marketing (CBSM) framework underlying the behavior-change program design distinguished from generic public-awareness messaging.
- Recycling-industry trade press (Resource Recycling, Waste360) — commodity index reporting for recovered fiber, plastics, and metals, and single-stream-vs.-dual-stream contamination benchmarking [heuristic ranges, market- and program-specific].
- No direct recycling-coordinator practitioner has reviewed this file yet — flag corrections or gaps via PR.
