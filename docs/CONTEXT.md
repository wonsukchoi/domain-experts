# CONTEXT

## Current Task
2026-07-16 session: worked ESCO-BACKLOG.md's 260-role expansion list one-by-one (spec 2, full authoring pipeline). Drafted 8 roles: `chief-technology-officer`, `chief-data-officer`, `property-developer`, `book-publisher`, `central-bank-governor`, `pension-scheme-manager`, `correctional-services-manager`, `oil-gas-production-manager`. All lint clean, pushed to main. Paused here — 252 of 260 backlog roles remain.

## Key Decisions
- Recipe per role: mkdir + SKILL.md + references/ trio → check ESCO-BACKLOG.md box + link → add entry to `UNMAPPED_NOTES` in `scripts/generate_roadmap.py` (all these roles have no O*NET counterpart) → `git add` the role dir → `lint_roles.py <slug>` → `generate_roadmap.py` → `check_links.py` → commit → `git pull --rebase --autostash` → push. Repeat per role, not batched.
- Picks favored high-value, non-niche, no-overlap roles from ISCO 1 (Managers) first; ISCO 2 (Professionals, 128 roles) and ISCO 3 (Technicians, 53 roles) untouched.

## Next Steps
- Resume ESCO-BACKLOG.md one-by-one from ISCO 1 remaining: consul, diplomat, ambassador, police commissioner, public administration manager, licensing manager, quarry manager, rail operations manager, import export manager, movie distributor, and others — then move into ISCO 2/3.
- Same recipe each time: draft → checkbox + UNMAPPED_NOTES → lint → regenerate → commit/push individually.
