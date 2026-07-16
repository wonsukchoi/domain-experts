#!/usr/bin/env python3
"""
Regenerates ROADMAP.md's occupation checklist and the role-count summary
block in README.md from data/onet_occupations.tsv plus the current
contents of roles/*/SKILL.md.

Run after adding, removing, or re-mapping a role:
    python3 scripts/generate_roadmap.py

Only touches the marked auto-generated sections in ROADMAP.md and
README.md (between the START/END comment markers) — hand-written
prose elsewhere in those files is left alone.
"""
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ONET_TSV = REPO_ROOT / "data" / "onet_occupations.tsv"
ROLES_DIR = REPO_ROOT / "roles"
ROADMAP_MD = REPO_ROOT / "ROADMAP.md"
README_MD = REPO_ROOT / "README.md"

MAJOR_GROUPS = [
    ("11", "Management"),
    ("13", "Business and Financial Operations"),
    ("15", "Computer and Mathematical"),
    ("17", "Architecture and Engineering"),
    ("19", "Life, Physical, and Social Science"),
    ("21", "Community and Social Service"),
    ("23", "Legal"),
    ("25", "Educational Instruction and Library"),
    ("27", "Arts, Design, Entertainment, Sports, and Media"),
    ("29", "Healthcare Practitioners and Technical"),
    ("31", "Healthcare Support"),
    ("33", "Protective Service"),
    ("35", "Food Preparation and Serving Related"),
    ("37", "Building and Grounds Cleaning and Maintenance"),
    ("39", "Personal Care and Service"),
    ("41", "Sales and Related"),
    ("43", "Office and Administrative Support"),
    ("45", "Farming, Fishing, and Forestry"),
    ("47", "Construction and Extraction"),
    ("49", "Installation, Maintenance, and Repair"),
    ("51", "Production"),
    ("53", "Transportation and Material Moving"),
    ("55", "Military Specific"),
]

# Roles that don't map to a distinct O*NET occupation, with why. Update
# this by hand when adding a role that has no onet_soc_code.
UNMAPPED_NOTES = {
    "product-manager": "No distinct O*NET occupation for tech/software product management; closest broad match (`11-3021.00` Computer and Information Systems Managers) doesn't capture the role well enough to link.",
    "devops-sre": "Site Reliability Engineering is a post-O*NET-taxonomy specialization within `15-1244.00`/`15-1241.00`-type titles; no distinct SOC code exists.",
    "customer-success-manager": "A SaaS-era role that doesn't fit the closest O*NET candidates (`43-4051.00` Customer Service Representatives is too junior/generic).",
    "technical-recruiter": "Falls inside the broader `13-1071.00` Human Resources Specialists occupation rather than having its own code.",
    "ml-engineer": "No distinct O*NET occupation for ML/AI engineering; folds into `15-2051.00` Data Scientists (already used by `data-scientist`) or `15-1252.00` Software Developers (already used by `software-engineer`) depending on taxonomy version.",
    "data-engineer": "No distinct O*NET occupation for general pipeline/ETL data engineering; closest candidates (`15-1243.00` Database Architects, taken by `database-architect`, and `15-1243.01` Data Warehousing Specialists, which is BI/warehouse-specific) don't capture the role.",
    "frontend-engineer": "No distinct O*NET occupation for frontend performance/accessibility engineering; folds into `15-1254.00` Web Developers (already used by `full-stack-developer`) or `15-1252.00` Software Developers (already used by `software-engineer`).",
    "mobile-engineer": "No distinct O*NET occupation for mobile app engineering; folds into `15-1252.00` Software Developers (already used by `software-engineer`).",
    "platform-engineer": "Platform engineering is a post-O*NET-taxonomy specialization, same 15-1244.00/15-1241.00-adjacent territory as devops-sre; no distinct SOC code exists.",
    "chief-technology-officer": "ESCO-sourced role (ISCO 1330.3); no distinct O*NET occupation — closest candidate (`11-3021.00` Computer and Information Systems Managers) is IT-operations-framed and already used by `computer-information-systems-manager`, which doesn't capture the exec technology-strategy/board-facing scope of this role.",
    "chief-data-officer": "ESCO-sourced role (ISCO 1330.1); no distinct O*NET occupation — closest candidates (`11-3021.00` Computer and Information Systems Managers, taken by `computer-information-systems-manager`, and `15-2051.01` Business Intelligence Analysts) are IT-ops or analyst-framed and don't capture the enterprise data-governance/monetization scope of this exec role.",
    "property-developer": "ESCO-sourced role (ISCO 1323.1.2); no distinct O*NET occupation — closest candidates (`11-9021.00` Construction Managers, taken by `construction-manager`, and `13-2023.00` Appraisers and Assessors of Real Estate, taken by `real-estate-appraiser`) cover execution and valuation but not the deal-origination/capital-stack judgment this role centers on.",
    "book-publisher": "ESCO-sourced role (ISCO 1349.7); no distinct O*NET occupation — closest broad match (`11-9199.00` Managers, All Other) is a residual catch-all that doesn't capture the acquisition-economics/print-run judgment this role centers on.",
    "central-bank-governor": "ESCO-sourced role (ISCO 1112.1); no distinct O*NET occupation — O*NET's `11-1011.00` Chief Executives (taken by `chief-executive`) is a generic private-sector executive category that doesn't capture the monetary-policy/lender-of-last-resort judgment this role centers on.",
    "embedded-firmware-engineer": "No distinct O*NET occupation for embedded/firmware software engineering; `17-2072.00` Electronics Engineers, Except Computer explicitly excludes computer-related work, and `15-1252.00` Software Developers (taken by `software-engineer`) doesn't capture the hardware-interfacing specifics.",
}


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    block = m.group(1)
    fm = {}
    cat_m = re.search(r"^\s*category:\s*(\S+)", block, re.MULTILINE)
    if cat_m:
        fm["category"] = cat_m.group(1)
    code_m = re.search(r'^\s*onet_soc_code:\s*"?([\d.\-]+)"?', block, re.MULTILINE)
    if code_m:
        fm["onet_soc_code"] = code_m.group(1)
    desc_m = re.search(r"^description:\s*(.+)$", block, re.MULTILINE)
    if desc_m:
        fm["description"] = desc_m.group(1).strip().strip('"').strip("'")
    mat_m = re.search(r"^\s*maturity:\s*(\S+)", block, re.MULTILINE)
    if mat_m:
        fm["maturity"] = mat_m.group(1)
    spec_m = re.search(r"^\s*spec:\s*(\S+)", block, re.MULTILINE)
    fm["spec"] = int(spec_m.group(1)) if spec_m else 1
    parent_m = re.search(r"^\s*parent:\s*(\S+)", block, re.MULTILINE)
    if parent_m:
        fm["parent"] = parent_m.group(1)
    status_m = re.search(r"^\s*status:\s*(\S+)", block, re.MULTILINE)
    fm["status"] = status_m.group(1) if status_m else "active"
    audited_m = re.search(r'^\s*last_audited:\s*"?([\d\-]+)"?', block, re.MULTILINE)
    if audited_m:
        fm["last_audited"] = audited_m.group(1)
    score_m = re.search(r"^\s*audit_score:\s*(\d+)", block, re.MULTILINE)
    if score_m:
        fm["audit_score"] = int(score_m.group(1))
    return fm


def load_roles():
    # Count only roles git knows about (tracked or staged). Untracked
    # in-progress role dirs would bake counts into README/ROADMAP that a
    # clean checkout can't reproduce, failing the CI regeneration check.
    # `git add` a new role before running this script.
    import subprocess
    try:
        out = subprocess.run(
            ["git", "ls-files", "roles/*/SKILL.md"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True,
        ).stdout
        known = {REPO_ROOT / line for line in out.splitlines() if line}
    except (subprocess.CalledProcessError, FileNotFoundError):
        known = None  # not a git checkout — fall back to filesystem

    roles = {}
    skipped = []
    for skill_file in sorted(ROLES_DIR.glob("*/SKILL.md")):
        if known is not None and skill_file not in known:
            skipped.append(skill_file.parent.name)
            continue
        slug = skill_file.parent.name
        fm = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
        roles[slug] = fm
    if skipped:
        print(
            "NOTE: skipped untracked role dirs (git add them first): "
            + ", ".join(skipped)
        )
    return roles


def load_gaps(limit=20):
    """Frequency-rank data/gap-log.jsonl — queries bin/cli.js's `match` couldn't
    confidently resolve. Repeated near-identical queries under one parent role
    are the signal that a specialization leaf should be drafted."""
    import json
    from collections import Counter

    path = REPO_ROOT / "data" / "gap-log.jsonl"
    if not path.is_file():
        return []

    entries = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    counts = Counter(e.get("query", "").strip().lower() for e in entries)
    latest_raw, latest_ts, latest_candidates = {}, {}, {}
    for e in entries:
        key = e.get("query", "").strip().lower()
        ts = e.get("ts", "")
        if ts >= latest_ts.get(key, ""):
            latest_ts[key] = ts
            latest_raw[key] = e.get("query", "")
            latest_candidates[key] = e.get("candidates", [])

    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], latest_ts.get(kv[0], "")))
    return [
        {
            "query": latest_raw[key],
            "count": count,
            "last_seen": latest_ts.get(key, ""),
            "candidates": latest_candidates.get(key, []),
        }
        for key, count in ranked[:limit]
    ]


def load_onet():
    rows = []
    with open(ONET_TSV, encoding="utf-8") as f:
        next(f)  # header
        for line in f:
            code, title = line.rstrip("\n").split("\t", 1)
            rows.append((code, title))
    return rows


def write_roles_json(roles):
    import json
    out = [
        {
            "slug": slug,
            "description": fm.get("description", ""),
            "category": fm.get("category", ""),
            "maturity": fm.get("maturity", ""),
            "spec": fm.get("spec", 1),
            "onet_soc_code": fm.get("onet_soc_code"),
            "parent": fm.get("parent"),
            "status": fm.get("status", "active"),
            "last_audited": fm.get("last_audited"),
            "audit_score": fm.get("audit_score"),
            "skill": f"roles/{slug}/SKILL.md",
            "references": sorted(
                p.name for p in (ROLES_DIR / slug / "references").glob("*.md")
            ) if (ROLES_DIR / slug / "references").is_dir() else [],
            # "us" is the implicit baseline every SKILL.md is written to — no
            # overlay file needed for it. Overlay files add deltas on top.
            "jurisdictions": ["us"] + sorted(
                p.stem for p in (ROLES_DIR / slug / "references" / "jurisdictions").glob("*.md")
                if p.stem != "us"
            ) if (ROLES_DIR / slug / "references" / "jurisdictions").is_dir() else ["us"],
        }
        for slug, fm in sorted(roles.items())
    ]
    path = REPO_ROOT / "data" / "roles.json"
    path.write_text(json.dumps({"count": len(out), "roles": out}, indent=2) + "\n")
    print(f"Wrote data/roles.json: {len(out)} roles.")


def main():
    roles = load_roles()
    write_roles_json(roles)
    onet_rows = load_onet()
    gaps = load_gaps()

    deprecated_slugs = sorted(
        slug for slug, fm in roles.items() if fm.get("status") == "deprecated"
    )
    needs_refresh_slugs = sorted(
        slug for slug, fm in roles.items() if fm.get("status") == "needs-refresh"
    )
    # Deprecated roles drop out of coverage counts/checklist but stay in
    # data/roles.json and get their own appendix below.
    active_roles = {
        slug: fm for slug, fm in roles.items() if fm.get("status") != "deprecated"
    }

    drafted = {}  # code -> slug
    unmapped_slugs = []
    for slug, fm in active_roles.items():
        code = fm.get("onet_soc_code")
        if code:
            drafted[code] = slug
        else:
            unmapped_slugs.append(slug)

    legacy_slugs = sorted(
        slug for slug, fm in active_roles.items() if fm.get("spec", 1) != 2
    )

    by_major = {}
    for code, title in onet_rows:
        by_major.setdefault(code[:2], []).append((code, title))

    # --- ROADMAP.md ---
    lines = []
    lines.append("# Roadmap — O*NET occupation checklist")
    lines.append("")
    lines.append(
        "Master backlog of human expert roles to eventually cover in this repo, sourced from the "
        "U.S. Department of Labor's [O*NET database](https://www.onetcenter.org/database.html) "
        "(public domain, CC-licensed, release 30.3), which covers "
        f"{len(onet_rows):,} detailed occupations across {len(MAJOR_GROUPS)} major groups."
    )
    lines.append("")
    lines.append(
        "This is the checklist, not a commitment — it exists so contributors can see what's "
        "uncovered and claim a role via PR instead of duplicating effort or guessing what's "
        "missing. O*NET is US-centric and salaried-employment-framed; it's a strong systematic "
        "backbone but not the only valid source of roles (see \"Roles outside this list\" at the "
        "bottom)."
    )
    lines.append("")
    lines.append(
        "**Status legend:** ✅ drafted at current spec · ♻️ drafted, awaiting "
        "spec-2 upgrade (see [Spec-2 upgrade queue](#spec-2-upgrade-queue)) · "
        "*(blank)* not started"
    )
    lines.append("")
    lines.append(
        f"**Progress: {len(drafted)} / {len(onet_rows)} O*NET occupations drafted"
        f" · {len(legacy_slugs)} drafted roles awaiting spec-2 upgrade.**"
    )
    lines.append("")
    remaining_codes = [(c, t) for c, t in onet_rows if c not in drafted]
    all_other_remaining = sum(1 for c, t in remaining_codes if "All Other" in t)
    military_only_remaining = sum(
        1 for c, t in remaining_codes if c.startswith("55-") and "All Other" not in t
    )
    other_remaining = (
        len(remaining_codes) - all_other_remaining - military_only_remaining
    )
    if other_remaining == 0:
        lines.append(
            f"Of the {len(remaining_codes)} occupations not yet drafted, "
            f"{all_other_remaining} are \"All Other\" catch-all codes (residual "
            "categories with no distinct practitioner to write) and "
            f"{military_only_remaining} are group 55 military occupations (out of "
            "scope for this repo) — every other real, specific O*NET occupation is "
            "drafted."
        )
        lines.append("")
    lines.append("<!-- CHECKLIST START -->")
    lines.append("")

    for code_prefix, group_title in MAJOR_GROUPS:
        occs = by_major.get(code_prefix, [])
        drafted_in_group = sum(1 for c, _ in occs if c in drafted)
        lines.append("<details>")
        lines.append(
            f"<summary><strong>{code_prefix} — {group_title}</strong> "
            f"({drafted_in_group}/{len(occs)} drafted)</summary>"
        )
        lines.append("")
        lines.append("| Status | O*NET-SOC Code | Occupation | Repo role |")
        lines.append("|---|---|---|---|")
        for code, title in occs:
            slug = drafted.get(code)
            if slug:
                status = "✅" if roles[slug].get("spec", 1) == 2 else "♻️"
            else:
                status = ""
            link = f"[`{slug}`](./roles/{slug}/SKILL.md)" if slug else ""
            lines.append(f"| {status} | {code} | {title} | {link} |")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    lines.append("<!-- CHECKLIST END -->")
    lines.append("")
    lines.append("## Spec-2 upgrade queue")
    lines.append("")
    lines.append(
        "Roles drafted before the current spec — they lack the `references/` "
        "trio (deep-dive, `red-flags.md`, `vocabulary.md`) and the spec-2 "
        "SKILL.md structure. This queue is the standing TODO for upgrade "
        "sessions: pick the top unclaimed entry and follow the \"Exact recipe "
        "for upgrading a legacy role to spec 2\" in "
        "[CONTRIBUTING.md](./CONTRIBUTING.md). A role drops off this list "
        "automatically once its frontmatter says `spec: 2` and this script "
        "is re-run."
    )
    lines.append("")
    if legacy_slugs:
        lines.append(f"**{len(legacy_slugs)} roles awaiting upgrade:**")
        lines.append("")
        lines.append("| Repo role | Category |")
        lines.append("|---|---|")
        for slug in legacy_slugs:
            cat = roles[slug].get("category", "")
            lines.append(f"| [`{slug}`](./roles/{slug}/SKILL.md) | {cat} |")
    else:
        lines.append("**Queue empty — every drafted role is at spec 2.** 🎉")
    lines.append("")
    lines.append("## Roles outside this list")
    lines.append("")
    lines.append(
        "Some roles already in this repo don't map cleanly to a single O*NET occupation — either "
        "because O*NET's granularity is coarser (a whole occupation covers what industry practice "
        "splits into several distinct roles) or because the role is a newer specialization O*NET "
        "hasn't caught up to yet:"
    )
    lines.append("")
    lines.append("| Repo role | Why it's not mapped |")
    lines.append("|---|---|")
    for slug in sorted(unmapped_slugs):
        note = UNMAPPED_NOTES.get(slug, "_(reason not documented yet — add to UNMAPPED_NOTES in scripts/generate_roadmap.py)_")
        lines.append(f"| [`{slug}`](./roles/{slug}/SKILL.md) | {note} |")
    lines.append("")
    lines.append("## Beyond O*NET")
    lines.append("")
    lines.append(
        "O*NET is US-centric and skews toward formal, salaried employment. For international "
        "coverage or informal/entrepreneurial roles it doesn't capture well, consider "
        "cross-referencing the ILO's "
        "[ISCO](https://ilostat.ilo.org/resources/concepts-and-definitions/classification-occupation/) "
        "or the EU's [ESCO](https://esco.ec.europa.eu/en) taxonomies when proposing a new role in a PR. "
        "A curated ESCO diff already exists: [`ESCO-BACKLOG.md`](./ESCO-BACKLOG.md) lists 260 ESCO "
        "occupations with no counterpart here, triaged from the full taxonomy in "
        "[`data/esco_occupations.tsv`](./data/esco_occupations.tsv)."
    )
    lines.append("")
    lines.append("## Requested but missing")
    lines.append("")
    lines.append(
        "Queries the CLI's `match` command couldn't confidently resolve, logged to "
        "`data/gap-log.jsonl` and ranked by frequency here. A query that keeps recurring "
        "under one parent role's shadow — e.g. a narrow niche a generic role doesn't quite "
        "cover — is the concrete signal to draft a specialization leaf."
    )
    lines.append("")
    if gaps:
        lines.append("| Query | Times seen | Last seen | Closest candidates |")
        lines.append("|---|---|---|---|")
        for g in gaps:
            cands = ", ".join(f"`{c}`" for c in g["candidates"]) or "_none_"
            lines.append(f"| {g['query']} | {g['count']} | {g['last_seen'][:10]} | {cands} |")
    else:
        lines.append("**No unresolved queries logged yet.**")
    lines.append("")
    lines.append("## Needs refresh")
    lines.append("")
    lines.append(
        "Roles flagged `status: needs-refresh` in frontmatter — a periodic re-score "
        "against AUTHORING.md's rubric came back below threshold, or a cited source "
        "went stale. Not removed from the library, just due for a revision PR."
    )
    lines.append("")
    if needs_refresh_slugs:
        lines.append("| Repo role | Last audited | Audit score |")
        lines.append("|---|---|---|")
        for slug in needs_refresh_slugs:
            fm = roles[slug]
            lines.append(
                f"| [`{slug}`](./roles/{slug}/SKILL.md) | "
                f"{fm.get('last_audited', '_never_')} | "
                f"{fm.get('audit_score', '_none_')}/18 |"
            )
    else:
        lines.append("**None currently flagged.**")
    lines.append("")
    lines.append("## Deprecated")
    lines.append("")
    lines.append(
        "Roles flagged `status: deprecated` — failed re-audit repeatedly, or the "
        "niche itself went obsolete. Excluded from the counts and checklist above; "
        "files stay in the repo (moved to `roles/_deprecated/<slug>/`), nothing is "
        "deleted."
    )
    lines.append("")
    if deprecated_slugs:
        lines.append("| Repo role | Category |")
        lines.append("|---|---|")
        for slug in deprecated_slugs:
            cat = roles[slug].get("category", "")
            lines.append(f"| `{slug}` | {cat} |")
    else:
        lines.append("**None currently deprecated.**")
    lines.append("")

    ROADMAP_MD.write_text("\n".join(lines), encoding="utf-8")

    # --- README.md role-count block ---
    cat_counts = {}
    for slug, fm in active_roles.items():
        cat = fm.get("category", "uncategorized")
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    onet_pct = len(drafted) / len(onet_rows) * 100
    bar_slots = 20
    filled = round(bar_slots * onet_pct / 100)
    coverage_bar = "█" * filled + "░" * (bar_slots - filled)

    block = []
    block.append("<!-- ROLE_COUNTS_START -->")
    block.append(f"**{len(active_roles)} roles drafted** ({len(drafted)} mapped to an O*NET occupation, {len(unmapped_slugs)} custom; {len(active_roles) - len(legacy_slugs)} at spec 2, {len(legacy_slugs)} awaiting upgrade), across {len(cat_counts)} categories:")
    block.append("")
    block.append(f"**O\\*NET coverage:** `{coverage_bar}` {onet_pct:.1f}% ({len(drafted)} / {len(onet_rows):,} occupations)")
    block.append("")
    for cat in sorted(cat_counts):
        block.append(f"- **{cat}**: {cat_counts[cat]}")
    block.append("")
    block.append("Browse all roles in [`roles/`](./roles/), or see [`ROADMAP.md`](./ROADMAP.md) for the full O*NET-backed checklist of what's covered and what's not.")
    block.append("<!-- ROLE_COUNTS_END -->")
    new_block = "\n".join(block)

    readme_text = README_MD.read_text(encoding="utf-8")
    pattern = re.compile(
        r"<!-- ROLE_COUNTS_START -->.*?<!-- ROLE_COUNTS_END -->", re.DOTALL
    )
    if pattern.search(readme_text):
        readme_text = pattern.sub(new_block, readme_text)
    else:
        raise SystemExit(
            "README.md is missing <!-- ROLE_COUNTS_START/END --> markers — add them where "
            "the role summary should go, then re-run this script."
        )
    README_MD.write_text(readme_text, encoding="utf-8")

    print(f"Wrote ROADMAP.md: {len(drafted)}/{len(onet_rows)} drafted, "
          f"{len(legacy_slugs)} in spec-2 upgrade queue.")
    print(f"Updated README.md role-count block: {len(roles)} total roles.")
    if unmapped_slugs:
        undocumented = [s for s in unmapped_slugs if s not in UNMAPPED_NOTES]
        if undocumented:
            print(f"NOTE: add reasons for {undocumented} to UNMAPPED_NOTES in this script.")


if __name__ == "__main__":
    main()
