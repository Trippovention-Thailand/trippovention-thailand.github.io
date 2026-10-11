"""
Generate sitemap.xml and image-sitemap.xml for trippovention.co.th
Scans docs/ for all HTML files and referenced images.
Excludes visa/ pages.
"""

import os
import re
import subprocess
from datetime import date

DOCS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs"))
DOMAIN = "https://trippovention.co.th"
TODAY = date.today().isoformat()

EXCLUDED_PAGES = {
    "404.html",
    "offline.html",
    "search.html",
    "thank-you.html",
}

def get_lastmod(filepath):
    """Retrieve last modification date from git log, fallback to file mtime."""
    try:
        res = subprocess.run(
            ["git", "log", "-1", "--format=%as", "--", filepath],
            capture_output=True,
            text=True,
            check=False
        )
        val = res.stdout.strip()
        if val:
            return val
    except Exception:
        pass
    try:
        mtime = os.path.getmtime(filepath)
        return date.fromtimestamp(mtime).isoformat()
    except Exception:
        return TODAY

def get_priority(rel_path):
    if rel_path in ("index.html", ""):
        return "1.0"
    if rel_path in ("contact.html", "destinations.html", "destinations-themes.html",
                     "destinations-travelers.html", "services.html", "land-packages.html",
                     "sightseeing.html", "transfers.html", "day-trips.html"):
        return "0.9"
    if rel_path.endswith("/index.html") or rel_path.endswith("/"):
        return "0.85"
    if rel_path in ("privacy-policy.html", "refund-policy.html", "terms-and-conditions.html"):
        return "0.5"
    return "0.7"

def is_page_indexable(file_path, rel_path):
    if rel_path in EXCLUDED_PAGES:
        return False
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            m = re.search(r'<meta\s+name=["\']robots["\']\s+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
            if m and "noindex" in m.group(1).lower():
                return False
    except Exception:
        pass
    return True

def generate_sitemap():
    entries = []
    for dp, dn, fns in os.walk(DOCS_ROOT):
        rel_dir = os.path.relpath(dp, DOCS_ROOT).replace("\\", "/")
        if rel_dir == ".":
            rel_dir = ""

        parts = rel_dir.split("/") if rel_dir else []
        if "visa" in parts:
            continue

        for f in sorted(fns):
            if not f.endswith(".html"):
                continue
            rel = f"{rel_dir}/{f}" if rel_dir else f
            abs_path = os.path.join(dp, f)

            if not is_page_indexable(abs_path, rel):
                continue

            # Canonical URL mapping
            if rel == "index.html":
                url = f"{DOMAIN}/"
            elif f == "index.html":
                url = f"{DOMAIN}/{rel_dir}/"
            else:
                url = f"{DOMAIN}/{rel}"

            priority = get_priority(rel)
            lastmod = get_lastmod(abs_path)
            entries.append((url, priority, lastmod))

    # Sort deterministically
    entries.sort(key=lambda x: (-float(x[1]), x[0]))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for url, priority, lastmod in entries:
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append("    <changefreq>weekly</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")

    lines.append("</urlset>")
    lines.append("")

    sitemap_path = os.path.join(DOCS_ROOT, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))

    print(f"Generated sitemap.xml with {len(entries)} URLs")
    return entries


def generate_image_sitemap():
    image_entries = []
    img_dir = os.path.join(DOCS_ROOT, "assets", "images")

    if not os.path.exists(img_dir):
        print("No assets/images directory found")
        return

    for dp, dn, fns in os.walk(img_dir):
        for f in sorted(fns):
            if not f.lower().endswith((".webp", ".jpg", ".jpeg", ".png")):
                continue
            rel = os.path.relpath(os.path.join(dp, f), DOCS_ROOT).replace("\\", "/")
            img_url = f"{DOMAIN}/{rel}"
            title = os.path.splitext(f)[0].replace("_", " ").replace("-", " ").title()
            image_entries.append((img_url, title))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
    lines.append('        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">')

    page_url = f"{DOMAIN}/"
    lines.append("  <url>")
    lines.append(f"    <loc>{page_url}</loc>")

    for img_url, title in image_entries:
        lines.append("    <image:image>")
        lines.append(f"      <image:loc>{img_url}</image:loc>")
        lines.append(f"      <image:title>{title}</image:title>")
        lines.append("    </image:image>")

    lines.append("  </url>")
    lines.append("</urlset>")
    lines.append("")

    img_sitemap_path = os.path.join(DOCS_ROOT, "image-sitemap.xml")
    with open(img_sitemap_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))

    print(f"Generated image-sitemap.xml with {len(image_entries)} images")


if __name__ == "__main__":
    generate_sitemap()
    generate_image_sitemap()
