#!/usr/bin/env python3
"""Generate static per-role HTML pages under docs/roles/<slug>/ for SEO.

Reads data/roles.json + roles/<slug>/SKILL.md, converts the markdown body
to plain HTML with a minimal hand-rolled converter (no dependencies), and
writes one static page per role plus docs/sitemap.xml, robots.txt, feed.xml
and llms.txt. All of those are generated — never hand-edit them.

Re-run after any role content changes:
    python3 scripts/build_pages.py
"""
import html
import json
import posixpath
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "roles.json"

# Matches PAGE_SIZE in docs/app.js. The homepage SSRs only the first page of
# cards — real content for no-JS clients and crawlers — instead of all ~950,
# which is what drove the DOM past Lighthouse's excessive-DOM-size line
# (~5,800 nodes vs. its ~800-node target). app.js fetches docs/data/roles.json
# and fully replaces #role-list on load regardless, so the SSR'd cards were
# never load-bearing for the JS-driven search/filter UI in the first place —
# only for no-JS viewers and crawlers, both served by this trimmed page plus
# the complete index in sitemap.xml and llms.txt.
HOMEPAGE_PAGE_SIZE = 60
ROLES_DIR = ROOT / "roles"
OUT_DIR = ROOT / "docs" / "roles"
SITE_URL = "https://domainexperts.dev"
REPO_BLOB = "https://github.com/wonsukchoi/domain-experts/blob/main/"


def title_case(slug):
    return " ".join(w[0].upper() + w[1:] for w in slug.split("-"))


# The `description` field in each role's SKILL.md frontmatter is not just SEO
# copy — it's the literal AI-agent skill-trigger text ("Use when a task needs
# the judgment of..."), consumed verbatim by agent frameworks deciding whether
# to invoke this role. That's why every single role's description runs
# 300-500+ chars: completeness there matters more than SERP snippet length.
# Human search engines want 50-160 chars, so `seo_description()` below derives
# a short, distinct-per-role summary from the same source data (role name +
# category + first concrete use case) purely for <meta description>/OG/Twitter
# tags — the full `description` field is untouched and still used everywhere
# else (JSON-LD, llms.txt, on-page body, roles.json).
_SEO_DESC_TAIL_STOPWORDS = {
    "a", "an", "the", "for", "and", "or", "with", "to", "of", "in", "on",
    "at", "by", "from",
}


def _first_use_case(description):
    """First bullet after the description's leading em-dash, respecting
    parens so a parenthetical list's internal commas don't cause a cut
    mid-parenthesis."""
    dash = description.find("—")
    if dash == -1:
        return None
    rest = description[dash + 1:].strip()
    depth = 0
    cut = len(rest)
    for i, ch in enumerate(rest):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "," and depth == 0:
            cut = i
            break
    return rest[:cut].strip().rstrip(".")


def _trim_dangling(text):
    words = text.split()
    while words and (
        words[-1].lower().strip("()") in _SEO_DESC_TAIL_STOPWORDS
        or "".join(words).count("(") > "".join(words).count(")")
    ):
        words.pop()
    return " ".join(words)


def seo_description(slug, category, description):
    name = title_case(slug)
    bullet = _first_use_case(description)
    cat = category.replace("-", " ")
    if not bullet:
        return f"{name} AI agent skill — {cat} domain expertise for judgment-heavy tasks."
    prefix = f"{name} AI agent skill: {cat} expertise for "
    full = prefix + bullet[0].lower() + bullet[1:] + "."
    if len(full) <= 160:
        return full
    budget = 160 - len(prefix) - 1
    out = ""
    for w in bullet.split():
        cand = (out + " " + w).strip()
        if len(cand) > budget:
            break
        out = cand
    out = _trim_dangling(out)
    return prefix + out[0].lower() + out[1:] + "."


def split_frontmatter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


INLINE_CODE = re.compile(r"`([^`]+)`")
BOLD = re.compile(r"\*\*([^*]+)\*\*")
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def resolve_link(url, slug):
    if url.startswith("http://") or url.startswith("https://"):
        return url
    return REPO_BLOB + posixpath.normpath(f"roles/{slug}/{url}")


def inline(text, slug):
    text = html.escape(text)
    text = INLINE_CODE.sub(lambda m: f"<code>{m.group(1)}</code>", text)
    text = BOLD.sub(lambda m: f"<strong>{m.group(1)}</strong>", text)
    # The href must be re-escaped after resolve_link(). html.escape() ran above,
    # so the raw URL is recovered with unescape() (otherwise a '&' in a query
    # string double-encodes) — but writing that recovered string straight into
    # href="..." puts an attacker-supplied '"' back into an attribute context.
    # SKILL.md arrives through outside role PRs, so `[x](a" onfocus="...)` was
    # stored XSS. Escape once more on the way into the attribute.
    text = LINK.sub(
        lambda m: f'<a href="{html.escape(resolve_link(html.unescape(m.group(2)), slug))}">{m.group(1)}</a>',
        text,
    )
    return text


def json_ld(payload):
    """Serialise JSON-LD for embedding in an inline <script> block.

    json.dumps escapes quotes but not '<' or '/', so a role description
    containing '</script>' closes the tag and injects markup into the page.
    \\u003c and friends are legal JSON string escapes, so the payload stays
    valid structured data while tag breakout becomes impossible.
    """
    return (
        json.dumps(payload)
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )


def markdown_to_html(body, slug):
    lines = body.split("\n")
    out = []
    list_stack = None  # 'ul' or 'ol'
    in_code = False
    code_buf = []

    def close_list():
        nonlocal list_stack
        if list_stack:
            out.append(f"</{list_stack}>")
            list_stack = None

    for line in lines:
        if line.strip().startswith("```"):
            if in_code:
                out.append(f"<pre><code>{html.escape(chr(10).join(code_buf))}</code></pre>")
                code_buf = []
                in_code = False
            else:
                close_list()
                in_code = True
            continue
        if in_code:
            code_buf.append(line)
            continue

        stripped = line.strip()
        if not stripped:
            close_list()
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            close_list()
            level = len(m.group(1)) + 1  # h1 reserved for page title
            level = min(level, 6)
            out.append(f"<h{level}>{inline(m.group(2), slug)}</h{level}>")
            continue

        m = re.match(r"^-\s+(.*)$", stripped)
        if m:
            if list_stack != "ul":
                close_list()
                out.append("<ul>")
                list_stack = "ul"
            out.append(f"<li>{inline(m.group(1), slug)}</li>")
            continue

        m = re.match(r"^\d+\.\s+(.*)$", stripped)
        if m:
            if list_stack != "ol":
                close_list()
                out.append("<ol>")
                list_stack = "ol"
            out.append(f"<li>{inline(m.group(1), slug)}</li>")
            continue

        close_list()
        out.append(f"<p>{inline(stripped, slug)}</p>")

    close_list()
    return "\n".join(out)


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; base-uri 'self'; form-action 'none'; script-src 'self' https://analytics.wonsukchoi.com; style-src 'self' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' https://img.shields.io; connect-src 'self' https://analytics.wonsukchoi.com">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{name} — Domain Experts</title>
<meta name="description" content="{seo_description}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="../../favicon.ico">
<link rel="apple-touch-icon" href="../../apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../style.css">
<meta property="og:title" content="{name} — Domain Experts">
<meta property="og:description" content="{seo_description}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Domain Experts">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="https://domainexperts.dev/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{name} — Domain Experts">
<meta name="twitter:description" content="{seo_description}">
<meta name="twitter:image" content="https://domainexperts.dev/og-image.png">
<script type="application/ld+json">{schema}</script>
<script type="application/ld+json">{breadcrumb}</script>
<script defer src="https://analytics.wonsukchoi.com/script.js" data-website-id="62eb52ba-75ab-4275-a3f0-794ae1d9035c"></script>
</head>
<body id="top">
<a href="#main-content" class="skip-link">Skip to content</a>
<header>
  <p class="links"><a href="../../index.html" class="back-link">&larr; All roles</a></p>
  <h1>{name}</h1>
  <p class="tagline role-tagline">{category} &middot; {status}</p>
</header>
<main class="role-page" id="main-content">
{content}
  <p class="source-link"><a href="{source}">View SKILL.md source on GitHub</a> &middot; maturity: {maturity}</p>
{jurisdictions}{related_roles}</main>
<footer>
  <p>Install this role: <code>npx domain-experts add {slug}</code></p>
  <p class="legal-links"><a href="../../privacy.html">Privacy</a> &middot; <a href="../../terms.html">Terms</a></p>
</footer>
<a href="#top" class="to-top" id="to-top" aria-label="Back to top">&uarr;</a>
<script src="../../to-top.js" defer></script>
</body>
</html>
"""


def sync_roles_json():
    dest = ROOT / "docs" / "data" / "roles.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(DATA.read_text())


def related_roles_html(role, roles_by_category):
    peers = [r for r in roles_by_category.get(role["category"], []) if r["slug"] != role["slug"]]
    if not peers:
        return ""
    picks = peers[:6]
    items = "\n".join(
        f'  <li><a href="../{html.escape(p["slug"])}/">{html.escape(title_case(p["slug"]))}</a></li>'
        for p in picks
    )
    return (
        '  <nav class="related-roles" aria-label="Related roles">\n'
        "  <h3>Related roles</h3>\n"
        "  <ul>\n"
        f"{items}\n"
        "  </ul>\n"
        "  </nav>\n"
    )


def role_card_html(r):
    slug = r["slug"]
    return (
        f'<a class="role-card" href="roles/{html.escape(slug)}/">\n'
        f"  <h3>{html.escape(title_case(slug))}</h3>\n"
        '  <div class="badges">\n'
        f'    <span class="badge">{html.escape(r["category"])}</span>\n'
        f'    <span class="badge status-{html.escape(r["status"])}">{html.escape(r["status"])}</span>\n'
        "  </div>\n"
        f'  <p>{html.escape(r["description"])}</p>\n'
        "</a>"
    )


def inject_static_role_list(roles):
    # Sentinel comments, not the surrounding <div>, bound the replaced region.
    # role_card_html() nests a <div class="badges"> inside every card, so a
    # naive (<div id="role-list"...>)(.*?)(</div>) regex matches that inner
    # div's close tag instead of the container's — it never removes the old
    # cards, just inserts a fresh batch ahead of them. Every rebuild
    # compounded the duplication (954 roles ended up as 50,612 rendered
    # cards / 405k lines). Comments can't nest or appear in escaped card
    # content, so this bound is unambiguous no matter how many divs a card
    # contains.
    index_path = ROOT / "docs" / "index.html"
    html_text = index_path.read_text()
    cards = "\n".join(role_card_html(r) for r in roles[:HOMEPAGE_PAGE_SIZE])
    replacement = f"<!-- BEGIN:role-cards -->\n{cards}\n<!-- END:role-cards -->"
    if "<!-- BEGIN:role-cards -->" in html_text:
        html_text = re.sub(
            r"<!-- BEGIN:role-cards -->.*?<!-- END:role-cards -->",
            lambda m: replacement,
            html_text,
            count=1,
            flags=re.DOTALL,
        )
    else:
        # One-time migration from the old, unbounded div-based format.
        # Anchored on the page's known trailing structure (</div> closing
        # #role-list, then </section></main>) rather than the ambiguous
        # opening tag, since that's what actually delimits the end reliably.
        html_text = re.sub(
            r'(<div id="role-list" class="role-list">).*?(</div>\s*</section>\s*</main>)',
            lambda m: m.group(1) + "\n" + replacement + m.group(2),
            html_text,
            count=1,
            flags=re.DOTALL,
        )
    index_path.write_text(html_text)


# AI crawlers get their own robots.txt groups. `User-agent: *` already allows
# them, so this changes nothing today — it is a durable declaration. robots.txt
# matching is most-specific-group-wins, so once a named group exists these
# crawlers stop reading the `*` group entirely, and a future `Disallow:` added
# there for ordinary search bots can no longer silently cut off AI access as a
# side effect. (`Sitemap:` is a non-group record and stays visible to all.)
AI_CRAWLERS = [
    ("GPTBot", "OpenAI — ChatGPT browsing and training"),
    ("OAI-SearchBot", "OpenAI — ChatGPT search index"),
    ("ChatGPT-User", "OpenAI — user-initiated page fetches"),
    ("ClaudeBot", "Anthropic — Claude"),
    ("Claude-User", "Anthropic — user-initiated page fetches"),
    ("PerplexityBot", "Perplexity"),
    ("Google-Extended", "Google — Gemini / AI Overviews grounding"),
    ("Applebot-Extended", "Apple Intelligence"),
    ("CCBot", "Common Crawl — feeds most open training corpora"),
]

# Descriptions all read "Use when a task needs the judgment of <role> — <triggers>".
# The head is boilerplate plus the role name, which the link text already carries;
# the triggers after the dash are the only part that tells one role from another.
DESCRIPTION_HEAD = re.compile(r"^Use when a task needs the judgment of .*?\s+—\s+")
LLMS_SUMMARY_CHARS = 180

CATEGORY_TITLES = {
    "design": "Design",
    "engineering": "Engineering",
    "finance": "Finance",
    "healthcare": "Healthcare",
    "legal": "Legal",
    "marketing": "Marketing",
    "operations": "Operations",
    "other": "Other",
    "product": "Product",
    "sales": "Sales",
}


def llms_summary(description):
    """One-line trigger summary for llms.txt.

    Role descriptions arrive through outside PRs, so newlines are collapsed
    before the string is written into a line-oriented format — otherwise a
    crafted description could forge extra list entries or a whole `##` section
    in the generated file. Same untrusted input that produced the stored XSS
    fixed in the HTML path; plain text has no markup to escape, but it does
    have line structure to protect.
    """
    text = " ".join(description.split())
    text = DESCRIPTION_HEAD.sub("", text)
    if len(text) <= LLMS_SUMMARY_CHARS:
        return text
    cut = text[:LLMS_SUMMARY_CHARS].rsplit(" ", 1)[0].rstrip(" ,;:—-")
    return cut + "…"


def build_llms_txt(roles):
    """Write docs/llms.txt — the llmstxt.org index for this site.

    An agent lands here asking "is there a role for X, and how do I load it?".
    So the header answers the second question outright (the CLI is the whole
    product surface), and the body is the complete 950+ role list grouped by
    category — a partial list would make a "not covered yet" answer wrong.
    """
    lines = [
        "# Domain Experts",
        "",
        "> Open source library of job-role definitions — the decision thresholds, "
        "trade-off rules and failure modes of real practitioners, structured as "
        "SKILL.md files any AI agent can load and reason from.",
        "",
        "Each role below is a page at `/roles/<slug>/`; the underlying SKILL.md "
        "and its `references/` live in the GitHub repo. Roles are US-baseline, "
        "with jurisdiction overlays noted per role.",
        "",
        "To load one into an agent rather than read it: "
        "`npx domain-experts add <slug>`, or `npx domain-experts match \"<task>\"` "
        "to find the right slug first. `npx domain-experts init <slug>` also "
        "installs the router skill and the `/domain-expert` command.",
        "",
        "## Start here",
        "",
        f"- [Role index]({SITE_URL}/): all roles, searchable by name and category.",
        f"- [README]({REPO_BLOB}README.md): what a role contains and why prompting "
        "for one is not equivalent.",
        f"- [Authoring spec]({REPO_BLOB}AUTHORING.md): the v2 structure every new role follows.",
        f"- [Contributing]({REPO_BLOB}CONTRIBUTING.md): how to add or upgrade a role.",
        "",
    ]

    by_category = {}
    for r in roles:
        by_category.setdefault(r["category"], []).append(r)

    # Named categories alphabetically, "other" last — it is a catch-all, not a peer.
    ordered = sorted(k for k in by_category if k != "other")
    if "other" in by_category:
        ordered.append("other")

    for category in ordered:
        entries = sorted(by_category[category], key=lambda r: r["slug"])
        lines.append(f"## {CATEGORY_TITLES.get(category, title_case(category))}")
        lines.append("")
        for r in entries:
            lines.append(
                f"- [{title_case(r['slug'])}]({SITE_URL}/roles/{r['slug']}/): "
                f"{llms_summary(r['description'])}"
            )
        lines.append("")

    lines += [
        "## Optional",
        "",
        f"- [Sitemap]({SITE_URL}/sitemap.xml): every page with last-modified dates.",
        f"- [Feed]({SITE_URL}/feed.xml): newly added roles.",
        f"- [Roadmap]({REPO_BLOB}ROADMAP.md): requested roles not yet written.",
        "",
    ]

    (ROOT / "docs" / "llms.txt").write_text("\n".join(lines))


def build_robots_txt():
    groups = [f"User-agent: *\nAllow: /\n"]
    for agent, note in AI_CRAWLERS:
        groups.append(f"# {note}\nUser-agent: {agent}\nAllow: /\n")
    body = "\n".join(groups)
    (ROOT / "docs" / "robots.txt").write_text(
        f"{body}\nSitemap: {SITE_URL}/sitemap.xml\n"
    )


def build():
    sync_roles_json()
    data = json.loads(DATA.read_text())
    roles = data["roles"]
    urls = []
    added_dates = role_added_dates()
    today = datetime.now(timezone.utc).date().isoformat()

    roles_by_category = {}
    for r in roles:
        roles_by_category.setdefault(r["category"], []).append(r)

    for r in roles:
        slug = r["slug"]
        skill_path = ROOT / r["skill"]
        if not skill_path.exists():
            continue
        raw = skill_path.read_text()
        body = split_frontmatter(raw)
        content_html = markdown_to_html(body, slug)
        canonical = f"{SITE_URL}/roles/{slug}/"
        schema = json_ld({
            "@context": "https://schema.org",
            "@type": "DefinedTerm",
            "name": title_case(slug),
            "description": r["description"],
            "url": canonical,
            "inDefinedTermSet": f"{SITE_URL}/",
        })
        breadcrumb = json_ld({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Domain Experts", "item": f"{SITE_URL}/"},
                {"@type": "ListItem", "position": 2, "name": title_case(slug), "item": canonical},
            ],
        })

        jurisdictions = r.get("jurisdictions") or ["us"]
        overlays = [j for j in jurisdictions if j != "us"]
        badges = "US (baseline)" + "".join(
            f' &middot; <a href="{html.escape(f"{REPO_BLOB}roles/{slug}/references/jurisdictions/{j}.md")}">'
            f"{html.escape(j.upper())}</a>"
            for j in overlays
        )
        jurisdictions_html = f'  <p class="jurisdictions">Jurisdiction: {badges}</p>\n'

        page = PAGE_TEMPLATE.format(
            name=html.escape(title_case(slug)),
            seo_description=html.escape(seo_description(slug, r["category"], r["description"])),
            canonical=canonical,
            content=content_html,
            source=html.escape(REPO_BLOB + r["skill"]),
            category=html.escape(r["category"]),
            status=html.escape(r["status"]),
            maturity=html.escape(r["maturity"]),
            slug=slug,
            schema=schema,
            breadcrumb=breadcrumb,
            jurisdictions=jurisdictions_html,
            related_roles=related_roles_html(r, roles_by_category),
        )

        page_dir = OUT_DIR / slug
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / "index.html").write_text(page)

        iso = added_dates.get(r["skill"])
        lastmod = datetime.fromisoformat(iso).date().isoformat() if iso else today
        urls.append((f"{SITE_URL}/roles/{slug}/", lastmod))

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
               f"  <url><loc>{SITE_URL}/</loc><lastmod>{today}</lastmod></url>"]
    for u, lastmod in urls:
        sitemap.append(f"  <url><loc>{u}</loc><lastmod>{lastmod}</lastmod></url>")
    sitemap.append("</urlset>")
    (ROOT / "docs" / "sitemap.xml").write_text("\n".join(sitemap) + "\n")

    build_robots_txt()

    inject_index_schema(roles)
    inject_static_role_list(roles)
    build_feed(roles)
    build_llms_txt(roles)

    print(
        f"Built {len(urls)} role pages + sitemap.xml + robots.txt + feed.xml + llms.txt"
    )


def role_added_dates():
    out = subprocess.run(
        ["git", "log", "--diff-filter=A", "--name-only",
         "--format=COMMIT:%aI", "--", "roles/*/SKILL.md"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    dates = {}
    current = None
    for line in out.splitlines():
        if line.startswith("COMMIT:"):
            current = line[len("COMMIT:"):]
        elif line.strip():
            dates.setdefault(line, current)
    return dates


def build_feed(roles):
    dates = role_added_dates()
    items = []
    for r in roles:
        path = f"roles/{r['slug']}/SKILL.md"
        iso = dates.get(path)
        dt = datetime.fromisoformat(iso) if iso else datetime.now(timezone.utc)
        items.append((dt, r))
    items.sort(key=lambda pair: pair[0], reverse=True)

    rfc822 = lambda dt: dt.strftime("%a, %d %b %Y %H:%M:%S %z")
    now = rfc822(datetime.now(timezone.utc))

    entries = []
    for dt, r in items:
        url = f"{SITE_URL}/roles/{r['slug']}/"
        entries.append(
            "  <item>\n"
            f"    <title>{html.escape(title_case(r['slug']))}</title>\n"
            f"    <link>{url}</link>\n"
            f"    <guid>{url}</guid>\n"
            f"    <pubDate>{rfc822(dt)}</pubDate>\n"
            f"    <description>{html.escape(r['description'])}</description>\n"
            "  </item>"
        )

    feed = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0">\n'
        "<channel>\n"
        "  <title>Domain Experts — New Roles</title>\n"
        f"  <link>{SITE_URL}/</link>\n"
        "  <description>New job-role agent skills added to Domain Experts.</description>\n"
        f"  <lastBuildDate>{now}</lastBuildDate>\n"
        + "\n".join(entries)
        + "\n</channel>\n</rss>\n"
    )
    (ROOT / "docs" / "feed.xml").write_text(feed)


def inject_index_schema(roles):
    schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "url": f"{SITE_URL}/roles/{r['slug']}/",
                "name": title_case(r["slug"]),
            }
            for i, r in enumerate(roles)
        ],
    }
    index_path = ROOT / "docs" / "index.html"
    html_text = index_path.read_text()
    html_text = re.sub(
        r'(<script type="application/ld\+json" id="role-schema">)(.*?)(</script>)',
        lambda m: m.group(1) + json.dumps(schema) + m.group(3),
        html_text,
        flags=re.DOTALL,
    )
    index_path.write_text(html_text)


if __name__ == "__main__":
    build()
