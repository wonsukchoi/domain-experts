# Telephone Operator — Playbook

## Call-type identification table

| Call type | What the CA does | Verbatim required? | Notes-after-call allowed? |
|---|---|---|---|
| TTY/text relay | Types hearing party's speech to caller; voices caller's typed text | Yes, unless caller requests summary | Metadata only |
| VRS (video relay) | Interprets between ASL and spoken English | Yes — interpretation is inherently non-literal but must be complete/accurate | Metadata only |
| STS (speech-to-speech) | Revoices a speech-disabled caller's words for the hearing party | Yes, exact words even if speech pattern requires the CA to speak them clearly | Metadata only |
| Directory assistance | Looks up a listing, reads back number or connects | N/A — not a relay call | Metadata only |
| Operator-assisted call completion | Places a collect/person-to-person/billed-to-third-party call | N/A | Metadata only |

## Directory-assistance disambiguation script

1. Take the query: name (or business name) + city/area if given.
2. Search the database. If exactly one match: read it back once ("I have [Name] at [partial address/area] — connecting you now") before dialing.
3. If more than one match:
   - Ask ONE disambiguating question, ranked by usefulness: street name > middle initial > business location/branch.
   - Example: "I have three listings for J. Smith in this area — do you know the street name?"
4. If the caller can't disambiguate and there are 2-3 matches: offer to read all matches with their distinguishing detail, let the caller choose.
5. If there are more than ~5 matches and no disambiguating detail: tell the caller the search is too broad and suggest they call back with a street name, or offer the general business/organization number if the query was for a company's main line.
6. Never guess a "most likely" match and connect without the caller's confirmation, even if one listing looks more prominent (e.g., a business's headquarters vs. a branch).

## Speed-of-answer tracking worksheet (filled example — matches SKILL.md worked example)

| Time window | Calls offered | Calls answered <10s | % within target | CAs staffed |
|---|---|---|---|---|
| 8:00–8:45 | 142 | 126 | 88.7% | 6 |
| 8:45–9:15 | 58 | 31 | 53.4% | 4 (coverage gap) |
| 9:15–10:00 | 140 | 119 | 85.0% | 6 |
| **Shift total** | **340** | **276** | **81.2%** | — |

Reading the table: don't stop at the shift-total row. A single low-coverage window can drag the average below target even when the rest of the shift is fine — always check for a sub-window before recommending an across-the-board fix.

## Refusal-eligible call checklist (per employer policy, applied narrowly)

- [ ] Call content is itself illegal under federal or state law (not merely offensive)
- [ ] Caller is using the relay service to harass the CA directly, not relay a call to a third party
- [ ] Employer's documented refusal procedure has been followed exactly, including the required logging step
- [ ] Refusal has been reported per the service's compliance-tracking requirement

If none of the boxes apply, the call proceeds — "I found it upsetting" or "the content was offensive" alone does not meet the refusal bar.
