# Breeding-decision playbook

Filled templates for the three recurring executions: sire selection against EPD/genomic data, inbreeding screening, and AI/synchronization logistics. Populate the tables with the herd's actual numbers each cycle — the structure below is the reusable part.

## 1. Sire comparison table (EPD vs. GE-EPD vs. proven)

| Sire | Status | Marbling EPD | Accuracy | $B index | Progeny count | Read |
|---|---|---|---|---|---|---|
| Sire A | Progeny-proven | +1.25 | 0.91 | +92 | 340 across 60 herds | High confidence — value is close to final |
| Sire B | GE-EPD (genomic + pedigree, no progeny) | +1.15 | 0.62 | +81 | 0 | Genomic boost roughly equivalent to 10–15 progeny reports — treat as a good estimate, not settled |
| Sire C | Parent average only, no genomic test | +1.30 | 0.18 | +88 | 0 | Widest confidence band in the table — the highest number here is the least trustworthy one |

**Reading the table:** rank by accuracy-weighted expectation, not by the raw index. Sire C's +1.30 marbling looks best on paper; at 0.18 accuracy the realized value could land anywhere from roughly +0.4 to +2.2 once progeny data accumulates. Sire A's +1.25 at 0.91 accuracy is the safer bet for this season's calf crop; Sire B is the one to buy semen on now and re-evaluate once its first genomic-confirmed calves report, since its accuracy will jump fastest as progeny data lands.

## 2. Inbreeding-coefficient worksheet

For a candidate sire × dam(-group) pairing:

1. Pull the dam's 4-generation pedigree and identify any common ancestor with the sire.
2. Compute the additive relationship *a* between sire and dam through each common-ancestor path (halved per generation of separation from the common ancestor, summed across all paths).
3. Predicted inbreeding coefficient of the offspring: **F = 0.5 × a(sire, dam)**.
4. Apply the herd's ceiling:

| F range | Action |
|---|---|
| 0–6.25% (first-cousin equivalent or looser) | Proceed — normal range for an outbred commercial herd |
| 6.25–12.5% (first-cousin to half-sib equivalent) | Caution zone — requires a documented reason (e.g., deliberate line-breeding for a fixed trait) before approval |
| >12.5% (half-sib equivalent or closer) | Hard stop without explicit, written owner sign-off |

**Worked path example:** Dam is a daughter of Sire A-1 (relationship to her sire = 0.50). Candidate sire is Sire A-1's full brother (relationship between the brothers = 0.50). Relationship between candidate sire and dam = 0.50 × 0.50 = 0.25. F = 0.5 × 0.25 = **0.125 (12.5%)** — hard-stop range, route this dam to an unrelated sire.

## 3. AI vs. natural-service cost-per-pregnancy table

| Input | AI (fixed-time, CO-Synch + CIDR) | Natural service |
|---|---|---|
| Semen/bull cost per cow | $35 (elite sire straw) | $40 (amortized bull cost/cow/season) |
| Synchronization drugs + CIDR | $25 | — |
| Labor/vet (injections, AI technician) | $15 | — |
| **Cost per cow bred** | **$75** | **$40** |
| Expected conception (mature cows, first service) | 55–65% (use 58% as planning midpoint) | 85–92% over a full season with a fertile bull |
| **Cost per pregnancy** | $75 ÷ 0.58 ≈ **$129** | $40 ÷ 0.88 ≈ **$45** |

**Decision rule:** run the AI premium (cost-per-pregnancy delta) against the genetic-index value gap between the AI sire and the herd's current herd-sire average, per calf. If (index-value-per-calf gap) × (expected AI pregnancies) exceeds the total incremental AI spend over natural service for that group, AI clears; if not, use a single AI pass with cleanup-bull backup rather than a second synchronized pass, since the second pass repeats the full premium against a shrinking pool of open cows.

## 4. Estrus-synchronization timeline (CO-Synch + CIDR, 7-day protocol)

| Day | Action | Timing window |
|---|---|---|
| Day 0 | GnRH injection + CIDR insert | Morning, herd-wide same session |
| Day 7 | CIDR removal + PGF2α (prostaglandin) injection | Within 1 hour of the day-0 session time, 7 days later |
| Day 9–10 | Fixed-time AI + second GnRH injection | 66–72 hours after CIDR removal — the single most compliance-sensitive step; AI outside this window measurably drops conception |
| Day 30–35 | Pregnancy check (palpation or ultrasound) | Confirms conception rate for the batch; any open cow at this point goes to cleanup bull, not a repeat synchronization |

**Compliance note:** the protocol's published conception-rate benchmarks assume every step lands inside its window. A CIDR left in an extra day, or AI performed at hour 50 instead of hour 66–72, is a logistics failure that will show up as a lower realized conception rate — diagnose it as a timing-log problem before assuming the sire, semen, or cow fertility is at fault.

## 5. Replacement-heifer retention and culling math

For a stable 120-cow herd with a 90% weaned-calf crop and a target of holding herd size flat:
- Calves weaned: 120 × 0.90 = 108.
- Assume roughly half heifers: 54 heifer calves.
- Cows culled annually (open, poor performance, age): commonly 15–20% of the breeding herd — at 18%, that's 22 cows to replace.
- Replacement heifers needed: 22 (plus a buffer for heifers that fail to breed as yearlings, commonly retaining 25–30 heifers to net 22 bred replacements at an assumed 80–85% heifer conception rate: 22 ÷ 0.82 ≈ 27 heifers retained).
- Remaining heifer calves (54 − 27 = 27) and all steer calves are marketed, not retained — retaining materially more than the replacement math requires dilutes selection intensity on the female side, since more heifers are kept regardless of their own index ranking.
