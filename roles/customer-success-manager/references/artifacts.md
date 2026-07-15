# Account health & QBR artifacts

Filled templates, not descriptions of templates — populate with real numbers as-is.

## 1. Book segmentation table (health x value) — filled example

| Tier | ARR range | Health | Count of accounts | Attention model |
|---|---|---|---|---|
| High-value, healthy | $100K+ | Green | 8 | Light-touch monitoring, quarterly expansion conversation |
| High-value, at-risk | $100K+ | Yellow/Red | 3 (incl. Northwind Logistics) | Immediate, hands-on intervention — top priority |
| Mid-value, healthy | $30K-$100K | Green | 22 | Automated health monitoring, biannual QBR |
| Mid-value, at-risk | $30K-$100K | Yellow/Red | 6 | Triaged individually — diagnose before committing heavy effort |
| Low-value, any health | Under $30K | Any | 21 | Mostly automated playbooks; manual effort only for high-confidence save opportunities |

## 2. Health score model (filled example, components and weights)

| Signal | Weight | Northwind Logistics (this account) |
|---|---|---|
| Key-feature usage trend (8-week) | 35% | −40% (red) |
| Stakeholder engagement breadth | 25% | 1 active stakeholder, down from 3 (red) |
| Support ticket sentiment | 15% | No tickets filed — neutral, not a positive signal here |
| NPS/CSAT (last survey) | 15% | 8/10 (from 60 days before champion departure — stale, not current) |
| Time-to-first-value achieved on schedule | 10% | Yes, achieved in original onboarding (positive, historical) |
| **Composite score** | | **Red — usage and stakeholder signals dominate; stale NPS doesn't offset current risk** |

**Rule applied:** the model is checked against actual churn outcomes at least annually — an account with this scoring pattern (usage + stakeholder both dropping) that later churned would validate the weighting; if accounts with this pattern routinely renewed anyway, the weights need revisiting.

## 3. QBR value-recap template (filled — see Worked example in SKILL.md for full narrative)

> **Outcome achieved:** Your logistics coordination team has saved an estimated 15 hours/week using [feature], valued at approximately $45,000/year in avoided labor cost per your team's own prior calculation.
> **What changed:** [Champion name]'s departure 6 weeks ago coincided with a usage dip among their former team — 17 of the original 42 weekly users. The remaining 25 users are still actively achieving the core workflow outcome.
> **What we're doing:** Rebuilding the stakeholder relationship with [new contact/Ops Manager], re-onboarding the affected team members, and tracking usage recovery over the next 4 weeks.
> **What we need from you:** A confirmed point of contact for the logistics team going forward, and a 30-minute call to walk through the re-onboarding plan.

## 4. Stakeholder map (filled example, before and after champion departure)

| Role | Name/status before | Name/status after departure |
|---|---|---|
| Economic buyer | CFO (aware, not engaged) | CFO (unchanged — reach out to confirm continued buy-in) |
| Champion / day-to-day owner | VP Ops (departed 6 weeks ago) | Vacant — Ops Manager identified as likely successor, not yet engaged |
| End users | 42 active | 25 active |
| Executive sponsor | None previously engaged | Gap — target for multi-threading this quarter |

**Rule applied:** every account above the book's high-value threshold should have at least 2 active stakeholder relationships; this account had 1, which is the structural risk being corrected now.
