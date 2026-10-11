#!/usr/bin/env python3
"""
Comprehensive SEO, AEO, and Technical Audit Script for Trippovention Thailand (trippovention.co.th)
Performs deep inspection of all HTML pages in docs/ directory.
"""

import os
import re
import json
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, unquote
from collections import defaultdict

DOCS_DIR = os.path.abspath("docs")
BASE_URL = "https://trippovention.co.th"

def audit_website():
    html_files = []
    for root, dirs, files in os.walk(DOCS_DIR):
        for f in files:
            if f.endswith(".html"):
                html_files.append(os.path.join(root, f))
    
    html_files.sort()
    print(f"Total HTML files found: {len(html_files)}")

    audit_results = {
        "summary": {
            "total_pages": len(html_files),
            "canonical_mismatches": 0,
            "missing_titles": 0,
            "short_titles": 0,
            "long_titles": 0,
            "duplicate_titles": 0,
            "missing_meta_descriptions": 0,
            "short_meta_descriptions": 0,
            "long_meta_descriptions": 0,
            "duplicate_meta_descriptions": 0,
            "missing_h1": 0,
            "multiple_h1": 0,
            "missing_image_alt": 0,
            "missing_image_dimensions": 0,
            "jsonld_parse_errors": 0,
            "broken_internal_links": 0,
            "sitemap_missing_pages": 0,
            "sitemap_extra_pages": 0,
            "sitemap_canonical_mismatches": 0,
        },
        "pages": {},
        "duplicate_titles_map": defaultdict(list),
        "duplicate_descriptions_map": defaultdict(list),
        "broken_links": [],
        "sitemap_issues": [],
        "heading_issues": [],
        "image_issues": [],
        "structured_data_inventory": defaultdict(int),
        "critical_issues": [],
        "high_issues": [],
        "medium_issues": [],
        "low_issues": []
    }

    # 1. Parse Sitemap
    sitemap_path = os.path.join(DOCS_DIR, "sitemap.xml")
    sitemap_urls = {}
    if os.path.exists(sitemap_path):
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
            ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            for u in root.findall('sm:url', ns):
                loc = u.find('sm:loc', ns)
                lastmod = u.find('sm:lastmod', ns)
                if loc is not None and loc.text:
                    sitemap_urls[loc.text.strip()] = lastmod.text.strip() if lastmod is not None else None
        except Exception as e:
            audit_results["critical_issues"].append(f"Failed to parse sitemap.xml: {e}")
    else:
        audit_results["critical_issues"].append("sitemap.xml not found in docs/ directory")

    # 2. Inspect each HTML page
    for file_path in html_files:
        rel_path = os.path.relpath(file_path, DOCS_DIR)
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()

        page_data = {
            "rel_path": rel_path,
            "title": None,
            "description": None,
            "canonical": None,
            "robots": None,
            "og_url": None,
            "h1_list": [],
            "h2_count": 0,
            "h3_count": 0,
            "word_count": 0,
            "images_count": 0,
            "images_missing_alt": 0,
            "images_missing_dimensions": 0,
            "json_ld_types": [],
            "internal_links_out": [],
            "is_in_sitemap": False
        }

        # Title
        m_title = re.search(r"<title>(.*?)</title>", html, re.DOTALL | re.IGNORECASE)
        if m_title:
            page_data["title"] = m_title.group(1).strip()
            audit_results["duplicate_titles_map"][page_data["title"]].append(rel_path)
            tlen = len(page_data["title"])
            if tlen < 25:
                audit_results["summary"]["short_titles"] += 1
                audit_results["medium_issues"].append(f"Short title ({tlen} chars) on {rel_path}: '{page_data['title']}'")
            elif tlen > 70:
                audit_results["summary"]["long_titles"] += 1
                audit_results["low_issues"].append(f"Long title ({tlen} chars) on {rel_path}: '{page_data['title']}'")
        else:
            audit_results["summary"]["missing_titles"] += 1
            audit_results["critical_issues"].append(f"Missing <title> tag on {rel_path}")

        # Meta Description
        m_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=(["\'])(.*?)\1', html, re.DOTALL | re.IGNORECASE)
        if not m_desc:
            m_desc = re.search(r'<meta\s+content=(["\'])(.*?)\1\s+name=["\']description["\']', html, re.DOTALL | re.IGNORECASE)
        if m_desc:
            page_data["description"] = m_desc.group(2).strip()
            audit_results["duplicate_descriptions_map"][page_data["description"]].append(rel_path)
            dlen = len(page_data["description"])
            if dlen < 50:
                audit_results["summary"]["short_meta_descriptions"] += 1
                audit_results["medium_issues"].append(f"Short meta description ({dlen} chars) on {rel_path}")
            elif dlen > 165:
                audit_results["summary"]["long_meta_descriptions"] += 1
                audit_results["low_issues"].append(f"Long meta description ({dlen} chars) on {rel_path}")
        else:
            audit_results["summary"]["missing_meta_descriptions"] += 1
            audit_results["high_issues"].append(f"Missing meta description on {rel_path}")

        # Canonical URL
        m_canon = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', html, re.IGNORECASE)
        if m_canon:
            page_data["canonical"] = m_canon.group(1).strip()
        else:
            audit_results["high_issues"].append(f"Missing canonical link tag on {rel_path}")

        # OG URL
        m_og_url = re.search(r'<meta\s+property=["\']og:url["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
        if m_og_url:
            page_data["og_url"] = m_og_url.group(1).strip()
            if page_data["canonical"] and page_data["og_url"] != page_data["canonical"]:
                audit_results["medium_issues"].append(f"Canonical mismatch with og:url on {rel_path}: canonical={page_data['canonical']}, og:url={page_data['og_url']}")

        # Robots meta tag
        m_robots = re.search(r'<meta\s+name=["\']robots["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
        if m_robots:
            page_data["robots"] = m_robots.group(1).strip().lower()
            if "noindex" in page_data["robots"]:
                audit_results["medium_issues"].append(f"Page marked noindex: {rel_path}")

        # Heading structure
        h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.DOTALL | re.IGNORECASE)
        page_data["h1_list"] = [re.sub(r"<[^>]+>", "", h).strip() for h in h1s]
        if len(h1s) == 0:
            audit_results["summary"]["missing_h1"] += 1
            audit_results["high_issues"].append(f"Missing <h1> on {rel_path}")
        elif len(h1s) > 1:
            audit_results["summary"]["multiple_h1"] += 1
            audit_results["medium_issues"].append(f"Multiple <h1> tags ({len(h1s)}) on {rel_path}: {page_data['h1_list']}")

        h2s = re.findall(r"<h2[^>]*>", html, re.IGNORECASE)
        h3s = re.findall(r"<h3[^>]*>", html, re.IGNORECASE)
        page_data["h2_count"] = len(h2s)
        page_data["h3_count"] = len(h3s)

        # Word count (excluding scripts and styles)
        text_clean = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.DOTALL | re.IGNORECASE)
        text_clean = re.sub(r"<[^>]+>", " ", text_clean)
        words = text_clean.split()
        page_data["word_count"] = len(words)

        # Images
        img_tags = re.findall(r"<img([^>]+)>", html, re.IGNORECASE)
        page_data["images_count"] = len(img_tags)
        for itag in img_tags:
            has_alt = 'alt=' in itag
            m_alt = re.search(r'alt=["\']([^"\']*)["\']', itag)
            alt_val = m_alt.group(1) if m_alt else None
            has_width = 'width=' in itag
            has_height = 'height=' in itag

            if not has_alt:
                page_data["images_missing_alt"] += 1
                audit_results["summary"]["missing_image_alt"] += 1
                audit_results["low_issues"].append(f"Image missing alt attribute in {rel_path}: {itag[:60]}")
            elif alt_val == "" and ("logo" in itag.lower() or "hero" in itag.lower()):
                audit_results["low_issues"].append(f"Hero/logo image has empty alt in {rel_path}: {itag[:60]}")

            if not (has_width and has_height):
                page_data["images_missing_dimensions"] += 1
                audit_results["summary"]["missing_image_dimensions"] += 1

        # Structured Data JSON-LD
        json_ld_blocks = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
        for block in json_ld_blocks:
            try:
                data = json.loads(block)
                if isinstance(data, list):
                    items = data
                else:
                    items = [data]
                for item in items:
                    stype = item.get("@type", "Unknown")
                    page_data["json_ld_types"].append(stype)
                    audit_results["structured_data_inventory"][stype] += 1
            except Exception as e:
                audit_results["summary"]["jsonld_parse_errors"] += 1
                audit_results["critical_issues"].append(f"JSON-LD syntax error on {rel_path}: {e}")

        # Internal Links Out & check validity
        links = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\']', html, re.IGNORECASE)
        curr_dir = os.path.dirname(file_path)
        for link in links:
            if link.startswith(("#", "tel:", "mailto:", "javascript:", "https://wa.me", "https://api.whatsapp.com")):
                continue
            if link.startswith("http://") or link.startswith("https://"):
                if not (link.startswith("https://trippovention.co.th") or link.startswith("http://trippovention.co.th")):
                    continue
                parsed = urlparse(link).path.lstrip("/")
                target = os.path.normpath(os.path.join(DOCS_DIR, parsed if parsed else "index.html"))
            else:
                parsed = unquote(urlparse(link).path)
                if not parsed:
                    continue
                target = os.path.normpath(os.path.join(curr_dir, parsed))

            if os.path.isdir(target):
                target = os.path.join(target, "index.html")

            if not os.path.exists(target):
                audit_results["broken_links"].append({
                    "source": rel_path,
                    "link": link,
                    "resolved": os.path.relpath(target, DOCS_DIR)
                })
                audit_results["summary"]["broken_internal_links"] += 1

        # Check Sitemap presence
        if rel_path == "index.html":
            expected_canon = f"{BASE_URL}/"
            expected_sitemap_url = f"{BASE_URL}/"
        elif rel_path.endswith("/index.html"):
            rel_dir = os.path.dirname(rel_path).replace("\\", "/")
            expected_canon = f"{BASE_URL}/{rel_dir}/"
            expected_sitemap_url = f"{BASE_URL}/{rel_dir}/"
        else:
            expected_canon = f"{BASE_URL}/{rel_path}"
            expected_sitemap_url = f"{BASE_URL}/{rel_path}"

        # check if in sitemap
        in_sitemap = (expected_sitemap_url in sitemap_urls)
        page_data["is_in_sitemap"] = in_sitemap
        if not in_sitemap and not (page_data["robots"] and "noindex" in page_data["robots"]) and rel_path not in ["404.html", "offline.html", "thank-you.html", "search.html"]:
            audit_results["summary"]["sitemap_missing_pages"] += 1
            audit_results["high_issues"].append(f"Indexable page missing from sitemap.xml: {rel_path}")

        audit_results["pages"][rel_path] = page_data

    # Check for duplicate titles and descriptions
    for title, pages in audit_results["duplicate_titles_map"].items():
        if len(pages) > 1:
            audit_results["summary"]["duplicate_titles"] += 1
            audit_results["high_issues"].append(f"Duplicate title ({len(pages)} pages): '{title}' across {pages}")

    for desc, pages in audit_results["duplicate_descriptions_map"].items():
        if len(pages) > 1:
            audit_results["summary"]["duplicate_meta_descriptions"] += 1
            audit_results["medium_issues"].append(f"Duplicate meta description ({len(pages)} pages) across {pages}")

    return audit_results

if __name__ == "__main__":
    results = audit_website()
    print("\n" + "="*80)
    print("AUDIT SUMMARY:")
    print("="*80)
    for k, v in results["summary"].items():
        print(f"  {k}: {v}")
    
    print("\n" + "="*80)
    print(f"CRITICAL ISSUES ({len(results['critical_issues'])}):")
    for i in results["critical_issues"][:20]:
        print(f"  [CRITICAL] {i}")
        
    print("\n" + "="*80)
    print(f"HIGH ISSUES ({len(results['high_issues'])}):")
    for i in results["high_issues"][:25]:
        print(f"  [HIGH] {i}")
        
    print("\n" + "="*80)
    print(f"STRUCTURED DATA INVENTORY:")
    for stype, count in sorted(results["structured_data_inventory"].items(), key=lambda x: -x[1]):
        print(f"  {stype}: {count} occurrences")

    # Save full JSON report
    out_json = "scripts/audit_results.json"
    with open(out_json, "w", encoding="utf-8") as f:
        # Convert defaultdicts
        clean_res = dict(results)
        clean_res["duplicate_titles_map"] = dict(clean_res["duplicate_titles_map"])
        clean_res["duplicate_descriptions_map"] = dict(clean_res["duplicate_descriptions_map"])
        clean_res["structured_data_inventory"] = dict(clean_res["structured_data_inventory"])
        json.dump(clean_res, f, indent=2)
    print(f"\nWrote full audit results to {out_json}")
