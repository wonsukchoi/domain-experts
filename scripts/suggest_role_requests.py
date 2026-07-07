#!/usr/bin/env python3
"""
Opens "role request" issues for O*NET occupations not yet drafted, so the
backlog in ROADMAP.md turns into concrete, claimable GitHub issues instead
of just a checklist nobody browses.

Picks candidates in O*NET-SOC code order (matches how this repo has
actually been closing out ROADMAP.md, group by group), skipping any code
that already has an open role-request issue. Boosts codes that also show
up in data/gap-log.jsonl's unresolved `match` queries, when that file has
entries.

Usage:
    python3 scripts/suggest_role_requests.py [--count 5] [--dry-run]

Requires the `gh` CLI, authenticated (GH_TOKEN/GITHUB_TOKEN in env is
enough — this is how it runs in CI via .github/workflows/role-requests.yml).
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_roadmap import load_roles, load_onet, load_gaps  # noqa: E402

REPO = "wonsukchoi/domain-experts"


def drafted_codes():
    roles = load_roles()
    codes = set()
    for slug, fm in roles.items():
        if fm.get("status") == "deprecated":
            continue
        code = fm.get("onet_soc_code")
        if code:
            codes.add(code)
    return codes


def open_role_request_titles():
    """Existing open role-request issue titles, so we never double-file one."""
    try:
        out = subprocess.run(
            ["gh", "issue", "list", "--repo", REPO, "--label", "role-request",
             "--state", "open", "--limit", "200", "--json", "title"],
            capture_output=True, text=True, check=True, timeout=30,
        )
        return {row["title"] for row in json.loads(out.stdout)}
    except (subprocess.CalledProcessError, FileNotFoundError, json.JSONDecodeError) as e:
        print(f"warning: couldn't list existing issues ({e}); proceeding without dedup", file=sys.stderr)
        return set()


def gap_boosted_codes(uncovered_titles_lower):
    """SOC codes whose occupation title words also appear in recent unresolved
    `match` queries — a real signal, when gap-log.jsonl has anything in it."""
    boosted = set()
    for g in load_gaps(limit=200):
        q = g["query"].lower()
        for code, title_lower in uncovered_titles_lower.items():
            words = [w for w in re.findall(r"[a-z]+", title_lower) if len(w) > 3]
            if words and all(w in q for w in words[:2]):
                boosted.add(code)
    return boosted


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=5, help="max new issues to open")
    ap.add_argument("--dry-run", action="store_true", help="print candidates, open nothing")
    args = ap.parse_args()

    onet_rows = load_onet()
    drafted = drafted_codes()
    # "All Other" is O*NET's residual catch-all bucket for a major group, not
    # a distinct job — bad material for a non-derivable, non-generic role, so
    # skip it here even though it's still a valid manual ROADMAP.md pick.
    uncovered = [
        (code, title) for code, title in onet_rows
        if code not in drafted and "All Other" not in title
    ]
    if not uncovered:
        print("Every O*NET occupation is drafted — nothing to request.")
        return

    uncovered_titles_lower = {code: title.lower() for code, title in uncovered}
    boosted = gap_boosted_codes(uncovered_titles_lower)
    uncovered.sort(key=lambda ct: (ct[0] not in boosted, ct[0]))

    existing_titles = open_role_request_titles()

    opened = 0
    for code, title in uncovered:
        if opened >= args.count:
            break
        issue_title = f"role request: {title} ({code})"
        if issue_title in existing_titles:
            continue
        boost_note = " — also shows up in recent unresolved `match` queries." if code in boosted else ""
        body = (
            f"Auto-suggested from [ROADMAP.md](../blob/main/ROADMAP.md)'s O*NET checklist: "
            f"**{title}** (`{code}`) has no drafted role yet.{boost_note}\n\n"
            "Want to write it? See [CONTRIBUTING.md](../blob/main/CONTRIBUTING.md) for the "
            "exact recipe (spec 2: `SKILL.md` + `references/` trio, worked example with real "
            "reconciling numbers, run `scripts/lint_roles.py` to 0 errors before opening the PR).\n\n"
            "Comment below to claim it, or add task examples if you'd rather someone else write it."
        )
        if args.dry_run:
            print(f"[dry-run] would open: {issue_title}")
            opened += 1
            continue
        subprocess.run(
            ["gh", "issue", "create", "--repo", REPO, "--title", issue_title,
             "--body", body, "--label", "role-request"],
            check=True,
        )
        print(f"opened: {issue_title}")
        opened += 1

    if opened == 0:
        print("No new candidates — every near-term uncovered occupation already has an open issue.")


if __name__ == "__main__":
    main()
