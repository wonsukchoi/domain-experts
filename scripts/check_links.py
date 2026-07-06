#!/usr/bin/env python3
"""Check relative markdown links across the repo's top-level docs resolve to real files.

Skips:
- absolute URLs (http/https/mailto) — not this script's job
- in-file anchors (#foo)
- GitHub issue-tracker links (../issues/...) — resolved against the GitHub blob URL,
  not a real filesystem path
- known illustrative example paths in TEMPLATE.md/CONTRIBUTING.md (references/*.md
  shown as the pattern a real role uses, not meant to resolve inside the template itself)
"""
import glob
import os
import re
import sys

FILE_GLOBS = ["*.md", "docs/*.md", "commands/*.md", ".github/*.md", "data/*.md", "evals/*.md"]

# (file, link target) pairs that are intentionally illustrative, not real paths.
KNOWN_EXAMPLES = {
    ("TEMPLATE.md", "references/playbook.md"),
    ("TEMPLATE.md", "references/red-flags.md"),
    ("TEMPLATE.md", "references/vocabulary.md"),
    ("CONTRIBUTING.md", "references/red-flags.md"),
}

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def find_files():
    files = set()
    for pattern in FILE_GLOBS:
        files.update(glob.glob(pattern))
    return sorted(files)


def check(files):
    broken = []
    for f in files:
        text = open(f, encoding="utf-8", errors="replace").read()
        base_dir = os.path.dirname(f)
        for m in LINK_RE.finditer(text):
            target = m.group(2).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#"):
                continue
            if "issues/" in target or "/blob/main/" in target:
                continue
            if (f, target) in KNOWN_EXAMPLES:
                continue
            path_part = target.split("#")[0]
            if not path_part:
                continue
            resolved = os.path.normpath(os.path.join(base_dir, path_part))
            if not os.path.exists(resolved):
                broken.append((f, target, resolved))
    return broken


def main():
    broken = check(find_files())
    if broken:
        print(f"{len(broken)} broken relative link(s):")
        for f, target, resolved in broken:
            print(f"  {f}: [{target}] -> {resolved} (missing)")
        sys.exit(1)
    print("No broken relative links found.")


if __name__ == "__main__":
    main()
