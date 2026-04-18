"""
Internal Link Checker for Thailand Site
Crawls all HTML files and validates internal links (href/src) resolve to real files.
"""

import os
import re
from urllib.parse import urlparse, unquote

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")

LINK_PATTERN = re.compile(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)

SKIP_PREFIXES = (
    "http://", "https://", "mailto:", "tel:", "javascript:", "data:",
    "#", "whatsapp:", "wa.me", "//",
)
SKIP_EXTENSIONS = (".webp", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".pdf", ".mp4")


def check_file(filepath, all_files_set):
    """Check all internal links in a file. Returns list of (file, link, issue)."""
    issues = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    file_dir = os.path.dirname(filepath)

    for match in LINK_PATTERN.finditer(content):
        link = match.group(1).strip()

        if any(link.lower().startswith(p) for p in SKIP_PREFIXES):
            continue

        # Strip query string and fragment
        clean = link.split("?")[0].split("#")[0]
        if not clean:
            continue

        # Skip image/media files (checked separately)
        ext = os.path.splitext(clean)[1].lower()
        if ext in SKIP_EXTENSIONS:
            continue

        # Resolve relative path
        target = os.path.normpath(os.path.join(file_dir, unquote(clean)))

        if not os.path.exists(target):
            rel_path = os.path.relpath(filepath, DOCS_DIR)
            issues.append((rel_path, link, "File not found"))

    return issues


def main():
    all_files = set()
    html_files = []

    for root, dirs, files in os.walk(DOCS_DIR):
        for f in files:
            full = os.path.join(root, f)
            all_files.add(full)
            if f.endswith(".html"):
                html_files.append(full)

    print(f"Scanning {len(html_files)} HTML files for broken internal links...\n")

    all_issues = []
    for filepath in sorted(html_files):
        issues = check_file(filepath, all_files)
        all_issues.extend(issues)

    if all_issues:
        print(f"Found {len(all_issues)} broken links:\n")
        for file, link, issue in sorted(all_issues):
            print(f"  {file}")
            print(f"    -> {link} ({issue})")
            print()
    else:
        print("No broken internal links found!")

    print(f"\nSummary: {len(all_issues)} broken links in {len(html_files)} files")


if __name__ == "__main__":
    main()
