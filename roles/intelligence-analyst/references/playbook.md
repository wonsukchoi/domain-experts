# Intelligence Analyst — Playbook

## Admiralty source-reliability / information-credibility grading

Grade every report on two independent axes. Never let a high source-reliability grade pull a low-credibility claim upward.

**Source reliability (A–F):**

| Grade | Meaning |
|---|---|
| A | Completely reliable — long, verified track record |
| B | Usually reliable — minor doubt, generally accurate history |
| C | Fairly reliable — doubt exists, some accurate reporting history |
| D | Not usually reliable — significant doubt |
| E | Unreliable — history of inaccuracy |
| F | Reliability cannot be judged — no track record |

**Information credibility (1–6):**

| Grade | Meaning |
|---|---|
| 1 | Confirmed by other independent sources |
| 2 | Probably true — logical, consistent with other information |
| 3 | Possibly true — reasonably logical, not confirmed |
| 4 | Doubtful — possible but not logical, no other confirmation |
| 5 | Improbable — contradicted by other information |
| 6 | Cannot be judged |

A report is written as reliability+credibility, e.g. "B2" — usually reliable source, probably true. An A-rated informant's uncorroborated tip on a specific new claim is still "A6" or "A3" until that specific claim is independently checked, not automatically "A1."

## ACH matrix template (filled example — narcotics distribution case)

Question: Is the same supply source behind the fentanyl-pressed pills recovered at three separate overdose scenes?

| Evidence | Grade | H1: Same source | H2: Different sources, same pill press design (widely available) | H3: Coincidental similarity |
|---|---|---|---|---|
| Pill stamp/logo identical across 3 scenes | A2 | C | N (stamp dies are also mass-produced and shared across networks) | I (identical stamp across 3 unrelated scenes is a low-probability coincidence) |
| Fentanyl concentration within 8% across all 3 samples (lab) | A1 | C | I (different sources rarely hit near-identical concentration without shared supply) | I |
| Two of three scenes had phone contact with same number in prior 72 hrs | C3 | C | N | I |
| Third scene's phone data unavailable (device destroyed) | F6 | N (absence of data, not evidence) | N | N |

Inconsistency count: H1 = 0, H2 = 2, H3 = 3. Select H1; confidence = high (2 A-rated, 1 C-rated corroborating, no disqualifying inconsistencies). The F6 row is excluded from the inconsistency count — missing data is not evidence against any hypothesis, and treating it as such is a common scoring error.

## Link-chart centrality check (filled example)

11-node network from financial-transaction and phone-contact data. Raw connection counts (degree centrality) vs. structural importance (betweenness centrality — how often a node sits on the shortest path between two other nodes):

| Node | Degree (# direct connections) | Betweenness (# shortest paths through this node) |
|---|---|---|
| Node C ("hub" — large social circle) | 9 | 4 |
| Node F (few connections, bridges two clusters) | 3 | 14 |
| Node A (named in initial tip) | 5 | 6 |

Naive read: Node C, with the most connections, is the target. Correct read: Node F, despite having only 3 direct connections, sits on 14 of the shortest paths between the two otherwise-separate clusters — removing Node F would fragment the network into two disconnected groups, which is the structural signature of a facilitator (e.g., a supplier bridging two distribution crews), not a popular social contact. Node C's high degree count more often indicates a social hub with weak diagnostic value (family member, mutual friend) unless corroborated by transaction data.

## RFI (Request for Information) tracker — filled example

| RFI # | Gap | Requested from | Status | Closes which ACH cell |
|---|---|---|---|---|
| RFI-14 | Scene 3 device forensic recovery | Digital forensics unit | Pending, 5-day SLA | E4 (currently F6 — no data) |
| RFI-15 | Pill press die serial/batch trace | DEA lab | Submitted | E1 confirmation source |

Track RFIs against specific matrix cells, not general "more information" — an open RFI with no named cell it would close is a sign the request wasn't actually necessary to the assessment.
