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
    return fm


def load_roles():
    roles = {}
    for skill_file in sorted(ROLES_DIR.glob("*/SKILL.md")):
        slug = skill_file.parent.name
        fm = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
        roles[slug] = fm
    return roles


def load_onet():
    rows = []
    with open(ONET_TSV, encoding="utf-8") as f:
        next(f)  # header
        for line in f:
            code, title = line.rstrip("\n").split("\t", 1)
            rows.append((code, title))
    return rows


def main():
    roles = load_roles()
    onet_rows = load_onet()

    drafted = {}  # code -> slug
    unmapped_slugs = []
    for slug, fm in roles.items():
        code = fm.get("onet_soc_code")
        if code:
            drafted[code] = slug
        else:
            unmapped_slugs.append(slug)

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
    lines.append("**Status legend:** ✅ drafted in this repo · *(blank)* not started")
    lines.append("")
    lines.append(f"**Progress: {len(drafted)} / {len(onet_rows)} O*NET occupations drafted.**")
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
            status = "✅" if slug else ""
            link = f"[`{slug}`](./roles/{slug}/SKILL.md)" if slug else ""
            lines.append(f"| {status} | {code} | {title} | {link} |")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    lines.append("<!-- CHECKLIST END -->")
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
        "or the EU's [ESCO](https://esco.ec.europa.eu/en) taxonomies when proposing a new role in a PR."
    )
    lines.append("")

    ROADMAP_MD.write_text("\n".join(lines), encoding="utf-8")

    # --- README.md role-count block ---
    cat_counts = {}
    for slug, fm in roles.items():
        cat = fm.get("category", "uncategorized")
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

    block = []
    block.append("<!-- ROLE_COUNTS_START -->")
    block.append(f"**{len(roles)} roles drafted** ({len(drafted)} mapped to an O*NET occupation, {len(unmapped_slugs)} custom), across {len(cat_counts)} categories:")
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

    print(f"Wrote ROADMAP.md: {len(drafted)}/{len(onet_rows)} drafted.")
    print(f"Updated README.md role-count block: {len(roles)} total roles.")
    if unmapped_slugs:
        undocumented = [s for s in unmapped_slugs if s not in UNMAPPED_NOTES]
        if undocumented:
            print(f"NOTE: add reasons for {undocumented} to UNMAPPED_NOTES in this script.")


if __name__ == "__main__":
    main()
