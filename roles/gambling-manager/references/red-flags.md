# Red flags & diagnostics

Signals an experienced gaming manager notices instantly. Load this when triaging a hold, integrity, or compliance question — not for general reasoning (that's `SKILL.md`).

### Hold variance beyond ~2 standard deviations for the sample size dealt
- **Usually means:** something real is happening — most likely a single concentrated player session, then dealer procedure, then equipment, then (least likely) advantage play or cheating
- **First question:** "Is this variance concentrated in one player's session, or spread across the whole shift?"
- **Data to pull:** hand-by-hand or spin-by-spin log with player IDs, standard deviation calculation for the actual sample size

### A player's bet spread ratio exceeds roughly 1:5 or more with correlation to shoe/deck composition
- **Usually means:** possible card counting (legal advantage play) — not cheating unless paired with marked cards, collusion, or equipment tampering
- **First question:** "Is the bet pattern correlated with count-favorable situations, and is there any sign of equipment/collusion involvement?"
- **Data to pull:** bet-by-bet log correlated with true count or remaining-deck composition at each bet

### A dealer's payout or procedure error rate is elevated on one specific shift or table
- **Usually means:** training gap, fatigue, or a specific dealer needing retraining — rarely intentional on first occurrence
- **First question:** "Is this the same dealer across multiple flagged incidents, or different dealers on the same table/shift?"
- **Data to pull:** procedure/error log by dealer and by table over the review period

### Single patron's cash transactions approach $10,000 aggregate for the gaming day
- **Usually means:** a mechanical CTR filing trigger — not a judgment call regardless of how the patron presents
- **First question:** "What's the aggregate cash-in and cash-out for this patron across all stations today?"
- **Data to pull:** cage transaction log aggregated by patron ID for the full gaming day

### Multiple transactions each just under the reporting threshold from the same patron
- **Usually means:** possible structuring (intentional threshold avoidance) — a suspicious-activity signal regardless of individual transaction legitimacy
- **First question:** "Were these transactions split across time or location in a way that looks deliberate?"
- **Data to pull:** full transaction timeline for the patron across all cage stations for the day

### A comp or credit decision is being justified by "the player was really upset" rather than theo
- **Usually means:** comp policy is drifting from theo-based pricing toward complaint-based pricing, which erodes margin without proportional loyalty return
- **First question:** "What's this player's calculated theo for the session, and does the comp request align with policy for that theo tier?"
- **Data to pull:** player tracking theo calculation for the session in question

### A suspected advantage player is being treated with the same response protocol as suspected cheating
- **Usually means:** the distinction between legal technique and rule-violating technique hasn't been made before escalating
- **First question:** "Is there any equipment manipulation, marked cards, or collusion involved — or is this purely public-information-based play?"
- **Data to pull:** surveillance review specifically checking for physical tampering or collusion indicators, separate from the betting pattern itself

### A game protection action (limit change, ejection) has no contemporaneous documentation of the reasoning
- **Usually means:** if this decision is challenged later (discrimination claim, regulatory inquiry), there's no record of what was actually observed and why the action was taken
- **First question:** "What specifically was documented at the time, not reconstructed afterward?"
- **Data to pull:** incident log timestamp and content vs. the timestamp of the action taken
