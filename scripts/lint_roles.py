#!/usr/bin/env python3
"""
Lint roles/*/SKILL.md (and references/) against AUTHORING.md.

Usage:
    python3 scripts/lint_roles.py                 # lint every role
    python3 scripts/lint_roles.py <slug> [...]    # lint specific roles
    python3 scripts/lint_roles.py --added <path> [...]
        # paths of newly added SKILL.md files (from git diff in CI);
        # these roles MUST be spec 2 — legacy format is not accepted
        # for new roles.

Spec versions (metadata.spec in frontmatter):
    absent / 1  — legacy role: frontmatter checks only
    2           — current spec: full structural checks

Exit code 1 if any error. Warnings don't fail the build.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROLES = ROOT / "roles"

CATEGORIES = {
    "engineering", "product", "design", "finance", "legal",
    "marketing", "sales", "operations", "healthcare", "other",
}
MATURITIES = {"draft", "reviewed-by-practitioner", "mature"}
STATUSES = {"active", "needs-refresh", "deprecated"}

REQUIRED_SECTIONS = [
    "Identity",
    "First-principles core",
    "Mental models & heuristics",
    "Decision framework",
    "Tools & methods",
    "Communication style",
    "Common failure modes",
    "Worked example",
    "Going deeper",
    "Sources",
]

# Conservative subset of AUTHORING.md's banned list — phrases that are
# near-always filler. Case-insensitive. Applied to SKILL.md body of
# spec-2 roles only.
BANNED = [
    "it's important to",
    "utilize",
    "ensure alignment",
    "drive value",
    "in today's",
    "holistic",
    "best practices",  # unqualified use; if qualified, rephrase anyway
]

# Soft line budgets (warn only).
BUDGETS = {"SKILL.md": (60, 140)}


def parse_frontmatter(text):
    """Minimal YAML-ish frontmatter parser (same spirit as generate_roadmap)."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^\s*([A-Za-z_]+):\s*(.*)$", line)
        if km:
            fm[km.group(1)] = km.group(2).strip().strip('"').strip("'")
    return fm


def section_bodies(text):
    """Map '## Heading' -> body text."""
    parts = re.split(r"^## +(.+?)\s*$", text, flags=re.MULTILINE)
    out = {}
    for i in range(1, len(parts) - 1, 2):
        out[parts[i].strip()] = parts[i + 1]
    return out


def lint_role(role_dir, require_v2, errors, warnings, all_slugs):
    slug = role_dir.name
    skill = role_dir / "SKILL.md"

    def err(msg):
        errors.append(f"{slug}: {msg}")

    def warn(msg):
        warnings.append(f"{slug}: {msg}")

    if not skill.is_file():
        err("missing SKILL.md")
        return

    text = skill.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        err("SKILL.md has no frontmatter block")
        return

    # --- frontmatter checks (all spec versions) ---
    if fm.get("name") != slug:
        err(f"frontmatter name '{fm.get('name')}' != directory name '{slug}'")
    desc = fm.get("description", "")
    if len(desc) < 60:
        err("description under 60 chars — must name concrete task types")
    if fm.get("category") not in CATEGORIES:
        err(f"category '{fm.get('category')}' not in allowed set")
    if fm.get("maturity") not in MATURITIES:
        err(f"maturity '{fm.get('maturity')}' not in allowed set")
    soc = fm.get("onet_soc_code")
    if soc and not re.fullmatch(r"\d{2}-\d{4}\.\d{2}", soc):
        err(f"onet_soc_code '{soc}' not in XX-XXXX.XX form")

    # --- optional lifecycle/hierarchy fields (all spec versions) ---
    parent = fm.get("parent")
    if parent:
        if parent == slug:
            err("parent cannot equal the role's own slug")
        elif parent not in all_slugs:
            err(f"parent '{parent}' is not an existing role slug")
    status = fm.get("status")
    if status and status not in STATUSES:
        err(f"status '{status}' not in allowed set {sorted(STATUSES)}")
    last_audited = fm.get("last_audited")
    if last_audited and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", last_audited):
        err(f"last_audited '{last_audited}' not in YYYY-MM-DD form")
    audit_score = fm.get("audit_score")
    if audit_score is not None and audit_score != "":
        if not re.fullmatch(r"\d+", audit_score) or not 0 <= int(audit_score) <= 18:
            err(f"audit_score '{audit_score}' must be an integer 0-18")

    spec = fm.get("spec", "1")
    if spec not in ("1", "2"):
        err(f"spec '{spec}' unknown (expected 1 or 2)")
        return
    if require_v2 and spec != "2":
        err("new role must be spec 2 (see AUTHORING.md); legacy format "
            "is only grandfathered for pre-existing roles")
        return
    if spec != "2":
        return  # legacy role: frontmatter checks only

    # --- spec 2: structural checks ---
    body = text.split("---\n", 2)[2] if text.count("---\n") >= 2 else text
    lo, hi = BUDGETS["SKILL.md"]
    n = len(text.splitlines())
    if not lo <= n <= hi:
        warn(f"SKILL.md is {n} lines (budget {lo}-{hi})")

    sections = section_bodies(body)
    for s in REQUIRED_SECTIONS:
        if s not in sections:
            err(f"missing required section '## {s}'")

    low = body.lower()
    for phrase in BANNED:
        if phrase in low:
            err(f"banned phrase in SKILL.md: '{phrase}'")

    we = sections.get("Worked example", "")
    if len(re.findall(r"\d", we)) < 10:
        err("Worked example has almost no digits — needs real, "
            "reconciling numbers")

    # Going deeper links must resolve.
    gd = sections.get("Going deeper", "")
    links = re.findall(r"\]\((references/[^)#]+)\)", gd)
    if not links:
        err("Going deeper has no references/ links")
    for rel in links:
        if not (role_dir / rel).is_file():
            err(f"Going deeper link does not resolve: {rel}")

    # Cross-role links (anywhere in body) must point at an existing role
    # and an existing file within it.
    for rel in re.findall(r"\]\((\.\./[^)#]+)\)", body):
        target = (role_dir / rel).resolve()
        try:
            target_slug = target.relative_to(ROLES.resolve()).parts[0]
        except ValueError:
            err(f"cross-role link escapes roles/: {rel}")
            continue
        if target_slug not in all_slugs:
            err(f"cross-role link points at unknown role '{target_slug}': {rel}")
        elif not target.is_file():
            err(f"cross-role link does not resolve: {rel}")

    # --- references/ checks ---
    refs = role_dir / "references"
    if not refs.is_dir():
        err("missing references/ directory")
        return

    ref_files = {p.name for p in refs.glob("*.md")}
    for required in ("red-flags.md", "vocabulary.md"):
        if required not in ref_files:
            err(f"references/ missing {required}")
    if not ref_files - {"red-flags.md", "vocabulary.md"}:
        err("references/ has no deep-dive file (playbook.md / artifacts.md "
            "/ role-specific equivalent)")

    rf_path = refs / "red-flags.md"
    if rf_path.is_file():
        rf = rf_path.read_text(encoding="utf-8").lower()
        n_means = len(re.findall(r"usually means", rf))
        n_q = len(re.findall(r"first question", rf))
        n_pull = len(re.findall(r"(?:data to )?pull:|look at:|check(?: to run)?:", rf))
        if min(n_means, n_q, n_pull) < 5:
            err(f"red-flags.md too thin: {n_means}x 'usually means', "
                f"{n_q}x 'first question', {n_pull}x 'pull' — need >=5 "
                "complete flags (signal/means/question/data)")

    v_path = refs / "vocabulary.md"
    if v_path.is_file():
        v = v_path.read_text(encoding="utf-8").lower()
        n_use = len(re.findall(r"in use:|usage:", v))
        n_mis = len(re.findall(r"misuse", v))
        if min(n_use, n_mis) < 8:
            err(f"vocabulary.md too thin: {n_use}x 'in use', {n_mis}x "
                "'misuse' — need >=8 misuse-aware terms")


def main(argv):
    added_paths = []
    slugs = []
    it = iter(argv)
    for a in it:
        if a == "--added":
            added_paths = list(it)  # everything after --added
            break
        slugs.append(a)

    added_slugs = set()
    for p in added_paths:
        parts = Path(p).parts
        if "roles" in parts:
            added_slugs.add(parts[parts.index("roles") + 1])

    if slugs:
        role_dirs = [ROLES / s for s in slugs]
    else:
        role_dirs = sorted(d for d in ROLES.iterdir() if d.is_dir())
    role_dirs = list(dict.fromkeys(role_dirs + [ROLES / s for s in added_slugs]))

    all_slugs = {d.name for d in ROLES.iterdir() if d.is_dir()}

    errors, warnings = [], []
    n_v2 = 0
    for d in role_dirs:
        if not d.is_dir():
            errors.append(f"{d.name}: role directory not found")
            continue
        text = (d / "SKILL.md").read_text(encoding="utf-8") if (d / "SKILL.md").is_file() else ""
        fm = parse_frontmatter(text) or {}
        if fm.get("spec") == "2":
            n_v2 += 1
        lint_role(d, require_v2=d.name in added_slugs, errors=errors,
                  warnings=warnings, all_slugs=all_slugs)

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(role_dirs)} roles linted ({n_v2} at spec 2, "
          f"{len(role_dirs) - n_v2} legacy) — "
          f"{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
