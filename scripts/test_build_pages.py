#!/usr/bin/env python3
"""Injection regression tests for scripts/build_pages.py.

Role content (SKILL.md bodies, frontmatter descriptions, jurisdiction codes)
arrives through outside pull requests, so every one of these strings is
attacker-controlled. Each case below produced live markup in the generated
page before 2026-07-28.

Run: python3 scripts/test_build_pages.py
"""
import json
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

if FAILURES:
    print(f"\n{len(FAILURES)} injection check(s) failed: {', '.join(FAILURES)}")
    sys.exit(1)
print("\nAll injection checks passed.")
