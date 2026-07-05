#!/usr/bin/env python3
"""
Harvest real practitioner Q&A from Stack Exchange for parity testing.

Pulls high-vote questions with accepted, high-vote answers from a role's
matching SE site, and writes them to questions/<role-slug>.json. Content
is CC BY-SA (see README); source links and author attribution are kept.

Usage:
    python3 evals/parity/harvest_stackexchange.py <role-slug> <site> <tag> [n]
e.g.
    python3 evals/parity/harvest_stackexchange.py lawyer-contracts law contract-law 3
"""

import html
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.stackexchange.com/2.3"
OUT = Path(__file__).resolve().parent / "questions"

FILTER = "withbody"  # builtin filter that includes post bodies


def get(path, **params):
    params.setdefault("filter", FILTER)
    url = f"{API}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "domain-experts-parity/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def strip_html(s):
    s = re.sub(r"<pre><code>(.*?)</code></pre>", r"\n```\n\1\n```\n", s, flags=re.DOTALL)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    slug, site, tag = sys.argv[1:4]
    n = int(sys.argv[4]) if len(sys.argv) > 4 else 3

    qs = get(
        "/questions", site=site, tagged=tag, sort="votes", order="desc",
        pagesize=25, accepted="True",
    )["items"]

    picked = []
    for q in qs:
        if len(picked) >= n:
            break
        if q.get("score", 0) < 10 or "accepted_answer_id" not in q:
            continue
        body = strip_html(q.get("body", ""))
        if len(body) < 200 or len(body) > 4000:  # substantial but self-contained
            continue
        ans = get(f"/answers/{q['accepted_answer_id']}", site=site)["items"]
        if not ans:
            continue
        a = ans[0]
        if a.get("score", 0) < 10:
            continue
        a_body = strip_html(a.get("body", ""))
        if len(a_body) < 300:
            continue
        picked.append({
            "id": f"{slug}-se-{q['question_id']}",
            "question": f"{strip_html(q['title'])}\n\n{body}",
            "expert_answer": a_body,
            "source": {
                "site": site,
                "url": q.get("link", ""),
                "question_score": q.get("score"),
                "answer_score": a.get("score"),
                "answer_author": (a.get("owner") or {}).get("display_name", "unknown"),
                "license": "CC BY-SA",
            },
        })
        print(f"picked {picked[-1]['id']} (q{q['score']}/a{a['score']}): {strip_html(q['title'])[:70]}")

    if not picked:
        sys.exit("nothing matched the quality bar")
    OUT.mkdir(exist_ok=True)
    out_file = OUT / f"{slug}.json"
    existing = json.loads(out_file.read_text())["questions"] if out_file.exists() else []
    have = {e["id"] for e in existing}
    merged = existing + [p for p in picked if p["id"] not in have]
    out_file.write_text(json.dumps({"role": slug, "questions": merged}, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {out_file} ({len(merged)} questions)")


if __name__ == "__main__":
    main()
