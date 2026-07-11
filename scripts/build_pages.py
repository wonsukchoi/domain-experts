#!/usr/bin/env python3
"""Generate static per-role HTML pages under docs/roles/<slug>/ for SEO.

Reads data/roles.json + roles/<slug>/SKILL.md, converts the markdown body
to plain HTML with a minimal hand-rolled converter (no dependencies), and
writes one static page per role plus docs/sitemap.xml.

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
ROLES_DIR = ROOT / "roles"
OUT_DIR = ROOT / "docs" / "roles"
SITE_URL = "https://domainexperts.dev"
REPO_BLOB = "https://github.com/wonsukchoi/domain-experts/blob/main/"


def title_case(slug):
    return " ".join(w[0].upper() + w[1:] for w in slug.split("-"))


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
    text = LINK.sub(
        lambda m: f'<a href="{resolve_link(html.unescape(m.group(2)), slug)}">{m.group(1)}</a>',
        text,
    )
    return text


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
<title>{name} — Domain Experts</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="../../favicon.ico">
<link rel="apple-touch-icon" href="../../apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../style.css">
<meta property="og:title" content="{name} — Domain Experts">
<meta property="og:description" content="{description}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Domain Experts">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="https://domainexperts.dev/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{name} — Domain Experts">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="https://domainexperts.dev/og-image.png">
<script type="application/ld+json">{schema}</script>
<script type="application/ld+json">{breadcrumb}</script>
<script defer src="https://analytics.wonsukchoi.com/script.js" data-website-id="62eb52ba-75ab-4275-a3f0-794ae1d9035c"></script>
</head>
<body id="top">
<header>
  <p class="links"><a href="../../index.html">&larr; All roles</a></p>
  <h1>{name}</h1>
  <p class="tagline role-tagline">{category} &middot; {status}</p>
</header>
<main class="role-page">
{content}
  <p class="source-link"><a href="{source}">View SKILL.md source on GitHub</a> &middot; maturity: {maturity}</p>
{jurisdictions}</main>
<footer>
  <p>Install this role: <code>npx domain-experts add {slug}</code></p>
</footer>
<a href="#top" class="to-top" id="to-top" aria-label="Back to top">&uarr;</a>
<script>
  var toTop = document.getElementById("to-top");
  window.addEventListener("scroll", function () {{
    toTop.classList.toggle("visible", window.scrollY > 400);
  }}, {{ passive: true }});
</script>
</body>
</html>
"""


def sync_roles_json():
    dest = ROOT / "docs" / "data" / "roles.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(DATA.read_text())


def build():
    sync_roles_json()
    data = json.loads(DATA.read_text())
    roles = data["roles"]
    urls = []
    added_dates = role_added_dates()
    today = datetime.now(timezone.utc).date().isoformat()

    for r in roles:
        slug = r["slug"]
        skill_path = ROOT / r["skill"]
        if not skill_path.exists():
            continue
        raw = skill_path.read_text()
        body = split_frontmatter(raw)
        content_html = markdown_to_html(body, slug)
        canonical = f"{SITE_URL}/roles/{slug}/"
        schema = json.dumps({
            "@context": "https://schema.org",
            "@type": "DefinedTerm",
            "name": title_case(slug),
            "description": r["description"],
            "url": canonical,
            "inDefinedTermSet": f"{SITE_URL}/",
        })
        breadcrumb = json.dumps({
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
            f' &middot; <a href="{REPO_BLOB}roles/{slug}/references/jurisdictions/{j}.md">{j.upper()}</a>'
            for j in overlays
        )
        jurisdictions_html = f'  <p class="jurisdictions">Jurisdiction: {badges}</p>\n'

        page = PAGE_TEMPLATE.format(
            name=html.escape(title_case(slug)),
            description=html.escape(r["description"]),
            canonical=canonical,
            content=content_html,
            source=REPO_BLOB + r["skill"],
            category=html.escape(r["category"]),
            status=html.escape(r["status"]),
            maturity=html.escape(r["maturity"]),
            slug=slug,
            schema=schema,
            breadcrumb=breadcrumb,
            jurisdictions=jurisdictions_html,
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

    (ROOT / "docs" / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"
    )

    inject_index_schema(roles)
    build_feed(roles)

    print(f"Built {len(urls)} role pages + sitemap.xml + robots.txt + feed.xml")


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
