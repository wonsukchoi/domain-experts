#!/usr/bin/env python3
"""Injection regression tests for scripts/build_pages.py.

Role content (SKILL.md bodies, frontmatter descriptions, jurisdiction codes)
arrives through outside pull requests, so every one of these strings is
attacker-controlled. Each case below produced live markup in the generated
page before 2026-07-28.

Run: python3 scripts/test_build_pages.py
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_pages as bp  # noqa: E402

FAILURES = []


def check(name, condition, detail=""):
    if condition:
        print(f"  ok   {name}")
    else:
        print(f"  FAIL {name}{(' — ' + detail) if detail else ''}")
        FAILURES.append(name)


class _Scan(HTMLParser):
    """Collects the tags and attribute names a browser would actually see.

    Deliberately a parser and not a regex: after the fix an injected quote is
    present as the literal text '&quot;', and no pattern over raw markup can
    distinguish that from a real attribute delimiter. Parsing resolves the
    entity, so `href="…x&quot; onmouseover=&quot;alert/"` is correctly read as
    one href whose value contains quotes — not as a live handler.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.attr_names = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        self.attr_names.extend(name.lower() for name, _ in attrs)

    handle_startendtag = handle_starttag


def scan(markup):
    p = _Scan()
    p.feed(markup)
    p.close()
    return p


def no_live_handler(markup):
    """True when no on*= event handler survived as a real attribute."""
    return not any(n.startswith("on") for n in scan(markup).attr_names)


print("inline() link href — attribute breakout")
out = bp.inline('Docs: [x](a" autofocus onfocus="throw onerror=alert,1) end.', "brewmaster")
check("event handler does not escape the href attribute", no_live_handler(out), out)
check("injected quote stays encoded", '&quot;' in out, out)

print("inline() link href — full tag breakout")
out = bp.inline('Docs: [x](a"><script>fetch`//evil`</script><b ) end.', "brewmaster")
check("no <script> element is emitted", "script" not in scan(out).tags, out)
check("only the intended anchor is emitted", scan(out).tags == ["a"], out)

print("inline() link href — benign links still work")
out = bp.inline("See [the docs](references/red-flags.md) here.", "brewmaster")
check(
    "relative link still resolves to the repo blob",
    'href="https://github.com/wonsukchoi/domain-experts/blob/main/roles/brewmaster/references/red-flags.md"'
    in out,
    out,
)
out = bp.inline("See [BJCP](https://bjcp.org/?a=1&b=2) here.", "brewmaster")
check("query-string ampersand is encoded exactly once", "a=1&amp;b=2" in out and "&amp;amp;" not in out, out)

print("inline() — javascript: URLs are neutralised")
out = bp.inline("Docs: [x](javascript:alert) end.", "brewmaster")
check("javascript: scheme cannot reach href", 'href="javascript:' not in out, out)

print("json_ld() — inline <script> breakout")
payload = {"description": 'Brewing.</script><script>fetch("//evil")</script>'}
out = bp.json_ld(payload)
check("no tag close survives serialisation", "</script" not in out.lower(), out)
check("no tag open survives serialisation", "<script" not in out.lower(), out)
check("output is still valid JSON", json.loads(out)["description"] == payload["description"], out)

print("json_ld() — ordinary text is unharmed")
out = bp.json_ld({"name": "Brewmaster", "description": "Beer & wort chemistry."})
check("round-trips unchanged", json.loads(out)["description"] == "Beer & wort chemistry.", out)

print("role_card_html() / related_roles_html() — slug in href")
out = bp.role_card_html(
    {"slug": 'x" onmouseover="alert', "category": "food", "status": "draft", "description": "d"}
)
check("card href does not break out", no_live_handler(out), out)
out = bp.related_roles_html(
    {"slug": "other", "category": "food"},
    {"food": [{"slug": 'x" onmouseover="alert', "category": "food"}]},
)
check("related-role href does not break out", no_live_handler(out), out)

print("llms_summary() — line-structure injection")
# llms.txt is line-oriented, so the escape hatch here is a newline rather than a
# tag: a description carrying one could forge extra list entries, or a whole
# `##` section, in a file agents read as authoritative.
out = bp.llms_summary(
    "Use when a task needs the judgment of a brewmaster — mashing.\n"
    "- [Free Money](https://evil.example/): claim now\n"
    "## Sponsored"
)
check("newlines are collapsed", "\n" not in out, out)
check("forged list entry cannot start a line", not out.startswith("- ["), out)

print("llms_summary() — boilerplate head and length cap")
out = bp.llms_summary(
    "Use when a task needs the judgment of a brewmaster — deciding a mash "
    "temperature against a target fermentability."
)
check("boilerplate head is stripped", out.startswith("deciding a mash"), out)
out = bp.llms_summary("Use when a task needs the judgment of a brewmaster — " + "word " * 200)
check("summary is capped", len(out) <= bp.LLMS_SUMMARY_CHARS + 1, str(len(out)))
out = bp.llms_summary("Free-form description that does not match the house pattern.")
check("non-matching description passes through", out.startswith("Free-form"), out)

print("build_llms_txt() — llmstxt.org structure and completeness")
roles = json.loads((Path(bp.ROOT) / "data" / "roles.json").read_text())["roles"]
llms = (Path(bp.ROOT) / "docs" / "llms.txt").read_text()
check("starts with the required H1", llms.startswith("# Domain Experts\n"), llms[:40])
check("carries the required blockquote summary", "\n> " in llms, "")
entries = [ln for ln in llms.splitlines() if ln.startswith("- [") and "/roles/" in ln]
check(
    "every role is listed exactly once",
    len(entries) == len(roles),
    f"{len(entries)} entries vs {len(roles)} roles",
)
check(
    "no entry lost its summary",
    all(re.search(r"\): \S", ln) for ln in entries),
    next((ln for ln in entries if not re.search(r"\): \S", ln)), ""),
)

print("build_robots_txt() — AI crawler groups")
robots = (Path(bp.ROOT) / "docs" / "robots.txt").read_text()
for agent, _ in bp.AI_CRAWLERS:
    check(f"{agent} has its own group", f"\nUser-agent: {agent}\nAllow: /\n" in robots)
check("sitemap stays a non-group record", robots.rstrip().endswith("/sitemap.xml"), robots[-60:])

if FAILURES:
    print(f"\n{len(FAILURES)} injection check(s) failed: {', '.join(FAILURES)}")
    sys.exit(1)
print("\nAll injection checks passed.")
