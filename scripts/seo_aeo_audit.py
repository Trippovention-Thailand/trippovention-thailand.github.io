#!/usr/bin/env python3
"""
Comprehensive SEO, AEO, Technical SEO and Sitemap Audit script for Trippovention Thailand.
Audits robots.txt, sitemap.xml, Bangkok destination pages, sightseeing pages, and reference pages.
"""

import os
import re
import json
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlparse

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
SITE_BASE = "https://trippovention.co.th"

class PageAuditor(HTMLParser):
    def __init__(self, filepath, rel_path):
        super().__init__()
        self.filepath = filepath
        self.rel_path = rel_path
        self.title = ""
        self.in_title = False
        self.meta_desc = ""
        self.canonical = ""
        self.robots = ""
        self.h1_tags = []
        self.in_h1 = False
        self.current_h1 = ""
        self.headings = [] # list of (tag, text)
        self.in_heading = None
        self.current_heading_text = ""
        self.images = [] # list of (src, alt, width, height, loading)
        self.links = [] # list of hrefs
        self.json_ld = []
        self.in_script_json_ld = False
        self.current_script_text = ""

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            name = attr_dict.get("name", "").lower()
            if name == "description":
                self.meta_desc = attr_dict.get("content", "")
            elif name == "robots":
                self.robots = attr_dict.get("content", "")
        elif tag == "link":
            rel = attr_dict.get("rel", "").lower()
            if rel == "canonical":
                self.canonical = attr_dict.get("href", "")
        elif tag == "h1":
            self.in_h1 = True
            self.current_h1 = ""
            self.in_heading = "h1"
            self.current_heading_text = ""
        elif tag in ["h2", "h3", "h4", "h5", "h6"]:
            self.in_heading = tag
            self.current_heading_text = ""
        elif tag == "img":
            src = attr_dict.get("src", "")
            alt = attr_dict.get("alt", None)
            width = attr_dict.get("width", "")
            height = attr_dict.get("height", "")
            loading = attr_dict.get("loading", "")
            self.images.append((src, alt, width, height, loading))
        elif tag == "a":
            href = attr_dict.get("href", "")
            if href:
                self.links.append(href)
        elif tag == "script":
            stype = attr_dict.get("type", "").lower()
            if stype == "application/ld+json":
                self.in_script_json_ld = True
                self.current_script_text = ""

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False
            self.h1_tags.append(self.current_h1.strip())
            if self.in_heading == "h1":
                self.headings.append(("h1", self.current_heading_text.strip()))
                self.in_heading = None
        elif tag in ["h2", "h3", "h4", "h5", "h6"]:
            if self.in_heading == tag:
                self.headings.append((tag, self.current_heading_text.strip()))
                self.in_heading = None
        elif tag == "script" and self.in_script_json_ld:
            self.in_script_json_ld = False
            self.json_ld.append(self.current_script_text.strip())
            self.current_script_text = ""

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_h1:
            self.current_h1 += data
        if self.in_heading:
            self.current_heading_text += data
        if self.in_script_json_ld:
            self.current_script_text += data


def audit_page(filepath, rel_path):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    parser = PageAuditor(filepath, rel_path)
    parser.feed(content)

    issues = []
    warnings = []

    # Title check
    title = parser.title.strip()
    if not title:
        issues.append("Missing <title> tag.")
    elif len(title) < 20:
        warnings.append(f"Title too short ({len(title)} chars): '{title}'")
    elif len(title) > 75:
        warnings.append(f"Title might be truncated ({len(title)} chars): '{title}'")

    # Meta description check
    meta_desc = parser.meta_desc.strip()
    if not meta_desc:
        issues.append("Missing meta description.")
    elif len(meta_desc) < 50:
        warnings.append(f"Meta description too short ({len(meta_desc)} chars).")
    elif len(meta_desc) > 175:
        warnings.append(f"Meta description might be truncated ({len(meta_desc)} chars).")

    # Canonical check
    canonical = parser.canonical.strip()
    expected_url = f"{SITE_BASE}/{rel_path}".replace("/index.html", "/")
    if not canonical:
        issues.append("Missing canonical link tag.")
    else:
        # Check normalization
        norm_canonical = canonical.rstrip("/")
        norm_expected = expected_url.rstrip("/")
        if norm_canonical != norm_expected and canonical != f"{SITE_BASE}/{rel_path}":
            warnings.append(f"Canonical URL mismatch: found '{canonical}', expected '{expected_url}' or '{SITE_BASE}/{rel_path}'.")

    # Robots check
    if "noindex" in parser.robots.lower():
        issues.append(f"Page has 'noindex' directive: {parser.robots}")

    # H1 check
    if len(parser.h1_tags) == 0:
        issues.append("Missing H1 heading.")
    elif len(parser.h1_tags) > 1:
        warnings.append(f"Multiple H1 headings ({len(parser.h1_tags)}): {parser.h1_tags}")

    # Image alt check
    missing_alt = [img[0] for img in parser.images if img[1] is None or img[1].strip() == ""]
    if missing_alt:
        warnings.append(f"{len(missing_alt)} images missing alt text: {missing_alt[:3]}")

    # Images missing dimensions
    missing_dims = [img[0] for img in parser.images if not img[2] or not img[3]]
    # (Some utility icons might omit width/height, but hero/cards should have them)

    # JSON-LD check
    schemas_parsed = []
    if not parser.json_ld:
        warnings.append("No JSON-LD structured data found.")
    else:
        for idx, s_text in enumerate(parser.json_ld):
            try:
                data = json.loads(s_text)
                stype = data.get("@type", "Unknown")
                schemas_parsed.append(stype)
            except json.JSONDecodeError as e:
                issues.append(f"Invalid JSON in JSON-LD script #{idx+1}: {e}")

    # Check internal links for 404s
    broken_links = []
    page_dir = os.path.dirname(filepath)
    for link in parser.links:
        if link.startswith("#") or link.startswith("mailto:") or link.startswith("tel:") or link.startswith("javascript:"):
            continue
        if link.startswith("http://") or link.startswith("https://"):
            if not link.startswith(SITE_BASE):
                continue
            # Internal absolute
            path_part = urlparse(link).path.lstrip("/")
            target_path = os.path.join(DOCS_DIR, path_part)
            if target_path.endswith("/"):
                target_path = os.path.join(target_path, "index.html")
        else:
            # Relative path
            clean_link = link.split("?")[0].split("#")[0]
            if not clean_link:
                continue
            target_path = os.path.normpath(os.path.join(page_dir, clean_link))

        if not os.path.exists(target_path) and not os.path.exists(target_path + ".html") and not os.path.exists(os.path.join(target_path, "index.html")):
            broken_links.append(link)

    if broken_links:
        issues.append(f"{len(broken_links)} broken internal links: {broken_links[:5]}")

    return {
        "rel_path": rel_path,
        "title": title,
        "meta_desc": meta_desc,
        "canonical": canonical,
        "h1": parser.h1_tags,
        "schemas": schemas_parsed,
        "issues": issues,
        "warnings": warnings,
        "links_count": len(parser.links),
        "images_count": len(parser.images)
    }


def audit_sitemap():
    sitemap_path = os.path.join(DOCS_DIR, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        return {"error": "sitemap.xml not found"}

    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
    except Exception as e:
        return {"error": f"Failed to parse sitemap.xml: {e}"}

    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = []
    missing_files = []
    duplicate_locs = set()
    seen_locs = set()

    for url_el in root.findall("sm:url", ns):
        loc_el = url_el.find("sm:loc", ns)
        lastmod_el = url_el.find("sm:lastmod", ns)
        priority_el = url_el.find("sm:priority", ns)
        changefreq_el = url_el.find("sm:changefreq", ns)

        if loc_el is not None and loc_el.text:
            loc = loc_el.text.strip()
            if loc in seen_locs:
                duplicate_locs.add(loc)
            seen_locs.add(loc)

            # verify file existence
            parsed = urlparse(loc)
            path = parsed.path.lstrip("/")
            file_path = os.path.join(DOCS_DIR, path)
            if file_path.endswith("/"):
                file_path = os.path.join(file_path, "index.html")

            if not os.path.exists(file_path):
                missing_files.append((loc, file_path))

            urls.append({
                "loc": loc,
                "lastmod": lastmod_el.text if lastmod_el is not None else None,
                "priority": priority_el.text if priority_el is not None else None,
                "changefreq": changefreq_el.text if changefreq_el is not None else None
            })

    return {
        "total_urls": len(urls),
        "duplicates": list(duplicate_locs),
        "missing_files": missing_files,
        "sample_urls": urls[:5]
    }


def main():
    print("==================================================================")
    print("TRIPPOVENTION THAILAND: BASELINE SEO & TECHNICAL AUDIT")
    print("==================================================================")

    # 1. Sitemap Audit
    sitemap_res = audit_sitemap()
    print(f"\n[SITEMAP AUDIT]")
    if "error" in sitemap_res:
        print(f"Error: {sitemap_res['error']}")
    else:
        print(f"Total URLs in sitemap: {sitemap_res['total_urls']}")
        print(f"Duplicate locs: {len(sitemap_res['duplicates'])}")
        print(f"Sitemap URLs pointing to non-existent files: {len(sitemap_res['missing_files'])}")
        if sitemap_res['missing_files']:
            for loc, fpath in sitemap_res['missing_files'][:5]:
                print(f"  Missing: {loc} -> {fpath}")

    # 2. Bangkok Directory Audit
    bangkok_dir = os.path.join(DOCS_DIR, "packages", "thailand", "bangkok")
    bangkok_files = sorted([f for f in os.listdir(bangkok_dir) if f.endswith(".html")])
    print(f"\n[BANGKOK PAGES AUDIT] ({len(bangkok_files)} files found)")

    bangkok_results = []
    for f in bangkok_files:
        fpath = os.path.join(bangkok_dir, f)
        rel_path = os.path.relpath(fpath, DOCS_DIR)
        res = audit_page(fpath, rel_path)
        bangkok_results.append(res)
        print(f"\nFile: {f}")
        print(f"  Title: {res['title']}")
        print(f"  H1: {res['h1']}")
        print(f"  Canonical: {res['canonical']}")
        print(f"  Schemas: {res['schemas']}")
        if res['issues']:
            print(f"  ISSUES: {res['issues']}")
        if res['warnings']:
            print(f"  WARNINGS: {res['warnings']}")

    # 3. Reference Krabi Sightseeing Page Audit
    krabi_sightseeing = os.path.join(DOCS_DIR, "packages", "thailand", "krabi", "sightseeing.html")
    if os.path.exists(krabi_sightseeing):
        rel_path = os.path.relpath(krabi_sightseeing, DOCS_DIR)
        krabi_res = audit_page(krabi_sightseeing, rel_path)
        print(f"\n[REFERENCE: KRABI SIGHTSEEING AUDIT]")
        print(f"  Title: {krabi_res['title']}")
        print(f"  H1: {krabi_res['h1']}")
        print(f"  Canonical: {krabi_res['canonical']}")
        print(f"  Schemas: {krabi_res['schemas']}")
        if krabi_res['issues']:
            print(f"  ISSUES: {krabi_res['issues']}")
        if krabi_res['warnings']:
            print(f"  WARNINGS: {krabi_res['warnings']}")

    # Check the specific Bangkok tile link in Bangkok index.html
    bkk_index_path = os.path.join(bangkok_dir, "index.html")
    with open(bkk_index_path, "r", encoding="utf-8") as f:
        bkk_index_content = f.read()

    tile_match = re.search(r'<h3>EXPLORE MORE OPTIONS OF SIGHTSEEING OF BANGKOK</h3>.*?<a class="btn" href="([^"]+)">', bkk_index_content, re.DOTALL)
    print(f"\n[BANGKOK SIGHTSEEING TILE CHECK]")
    if tile_match:
        print(f"  Current tile target: {tile_match.group(1)}")
    else:
        print("  Tile could not be found with regex pattern.")

if __name__ == "__main__":
    main()
