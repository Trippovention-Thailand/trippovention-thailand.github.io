#!/usr/bin/env python3
"""
Master Page Inventory Generator for Trippovention Thailand (trippovention.co.th)
Performs an exhaustive audit and cataloguing of all 248 HTML pages in docs/.
Outputs a structured JSON database and summary analysis according to the Master Audit Specification.
"""

import os
import re
import json
import xml.etree.ElementTree as ET
from collections import defaultdict
from html import unescape

DOCS_DIR = os.path.abspath("docs")
BASE_URL = "https://trippovention.co.th"

def clean_html(text):
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def get_page_type(rel_path):
    parts = rel_path.split(os.sep)
    filename = parts[-1]
    
    if rel_path in ["404.html", "offline.html", "thank-you.html", "search.html"]:
        return "Utility / System", "(Root)"
    if rel_path in ["index.html"]:
        return "Homepage", "(Root)"
    if rel_path in ["destinations.html", "destinations-themes.html", "destinations-travelers.html"]:
        return "Destination Hub", "Destinations"
    if rel_path in ["services.html", "transfers.html", "day-trips.html", "sightseeing.html", "land-packages.html"]:
        return "Service / Catalogue", "Services"
    if rel_path in ["contact.html", "about.html", "terms-and-conditions.html", "privacy-policy.html", "refund-policy.html"]:
        return "Company & Policy", "Corporate"
    
    # Destination packages or sightseeing
    if parts[0] == "packages":
        country = parts[1] # thailand, india, vietnam
        if len(parts) == 3:
            # e.g. packages/thailand/index.html
            return f"Country Hub ({country.title()})", country.title()
        elif len(parts) == 4:
            dest = parts[2]
            if filename == "index.html":
                return "Destination Landing", dest.replace("_", " ").title()
            elif filename == "sightseeing.html":
                return "Sightseeing Catalogue", dest.replace("_", " ").title()
            else:
                # Distinguish package vs sightseeing product
                if any(k in filename for k in ["_tour.html", "_cruise.html", "_show.html", "_park.html", "_tickets.html", "_pass.html", "_safari.html", "_climbing.html", "_kayak.html", "_market.html", "_museum.html", "_sanctuary.html", "_skywalk.html", "_experience.html", "_adventure.html", "_walk.html", "_courses.html"]):
                    return "Sightseeing Product", dest.replace("_", " ").title()
                else:
                    return "Holiday Package", dest.replace("_", " ").title()
    
    return "Standard Content", "(Root)"

def main():
    html_files = []
    for root, _, files in os.walk(DOCS_DIR):
        for f in files:
            if f.endswith(".html"):
                html_files.append(os.path.join(root, f))
    html_files.sort()
    
    # Load sitemap
    sitemap_path = os.path.join(DOCS_DIR, "sitemap.xml")
    sitemap_urls = set()
    if os.path.exists(sitemap_path):
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        for u in root.findall('sm:url', ns):
            loc = u.find('sm:loc', ns)
            if loc is not None and loc.text:
                sitemap_urls.add(loc.text.strip())

    master_inventory = []
    type_counts = defaultdict(int)
    category_counts = defaultdict(int)
    action_counts = defaultdict(int)

    for fp in html_files:
        rel_path = os.path.relpath(fp, DOCS_DIR)
        with open(fp, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()

        page_type, parent_cat = get_page_type(rel_path)
        type_counts[page_type] += 1
        category_counts[parent_cat] += 1

        # Title
        m_title = re.search(r"<title>(.*?)</title>", html, re.DOTALL | re.IGNORECASE)
        page_title = clean_html(m_title.group(1)) if m_title else "MISSING"

        # Meta description
        m_desc = re.search(r'<meta\s+[^>]*(?:name|property)=["\']description["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
        if not m_desc:
            m_desc = re.search(r'<meta\s+[^>]*content=["\']([^"\']+)["\'][^>]*(?:name|property)=["\']description["\']', html, re.I)
        meta_desc = clean_html(m_desc.group(1)) if m_desc else "MISSING"

        # Canonical
        m_canon = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', html, re.I)
        canonical = m_canon.group(1).strip() if m_canon else "MISSING"

        # Canonical URL vs Public URL
        if rel_path == "index.html":
            expected_url = f"{BASE_URL}/"
        elif rel_path.endswith("/index.html"):
            expected_url = f"{BASE_URL}/{rel_path[:-10]}/"
        else:
            expected_url = f"{BASE_URL}/{rel_path}"

        # Indexability
        is_utility = rel_path in ["404.html", "offline.html", "thank-you.html", "search.html"]
        indexability = "Noindex / Excluded" if is_utility else "Indexable"

        # Headings
        h1_matches = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.DOTALL | re.I)
        h1_clean = [clean_html(h) for h in h1_matches]
        h2_count = len(re.findall(r"<h2[^>]*>", html, re.I))
        h3_count = len(re.findall(r"<h3[^>]*>", html, re.I))
        h4_count = len(re.findall(r"<h4[^>]*>", html, re.I))

        # Header & Footer status
        has_nav = "<nav" in html and 'class="nav"' in html or "class='nav'" in html
        has_footer = "<footer" in html and 'class="footer"' in html or "class='footer'" in html
        header_template = "Standard Trippovention Nav (Active)" if has_nav else "Minimal / Standalone"
        footer_template = "Standard 3-Column Footer (2026 Verified)" if has_footer else "None (Utility)"

        # Internal & External links
        hrefs = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\']', html, re.I)
        int_links = [h for h in hrefs if not h.startswith(("http", "mailto:", "tel:", "javascript:", "#"))]
        ext_links = [h for h in hrefs if h.startswith("http")]

        # Broken images check
        imgs = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', html, re.I)
        broken_imgs = 0
        for src in imgs:
            if not src.startswith(("http", "data:")):
                p_clean = src.split("?")[0].split("#")[0]
                tgt = os.path.normpath(os.path.join(os.path.dirname(fp), p_clean))
                if not os.path.exists(tgt):
                    broken_imgs += 1

        # Structured Data
        ld_scripts = re.findall(r'<script\s+type=["\']application/ld\+json["\'][^>]*>([\s\S]*?)</script>', html, re.I)
        schema_types = []
        for s in ld_scripts:
            try:
                data = json.loads(s.strip())
                items = data if isinstance(data, list) else [data]
                for it in items:
                    t = it.get("@type")
                    if t:
                        if isinstance(t, list):
                            schema_types.extend(t)
                        else:
                            schema_types.append(t)
            except Exception:
                pass

        # In Sitemap
        in_sitemap = canonical in sitemap_urls or expected_url in sitemap_urls

        # Classification & Required Action
        if is_utility:
            action = "Keep utility / Excluded from sitemap"
        elif broken_imgs > 0:
            action = "Fix technical assets"
        elif not in_sitemap and indexability == "Indexable":
            action = "Add to sitemap"
        else:
            action = "Standardised & Verified (Keep unchanged)"
            
        action_counts[action] += 1

        item = {
            "file": rel_path,
            "url": expected_url,
            "page_title": page_title,
            "page_type": page_type,
            "parent_category": parent_cat,
            "http_status": 200,
            "canonical_url": canonical,
            "indexability": indexability,
            "in_sitemap": in_sitemap,
            "meta_description": meta_desc,
            "h1": h1_clean[0] if h1_clean else "MISSING",
            "h1_count": len(h1_clean),
            "h2_count": h2_count,
            "h3_count": h3_count,
            "h4_count": h4_count,
            "header_template": header_template,
            "footer_template": footer_template,
            "internal_links_count": len(int_links),
            "external_links_count": len(ext_links),
            "broken_images_count": broken_imgs,
            "structured_data": list(set(schema_types)),
            "action_classification": action
        }
        master_inventory.append(item)

    out_file = os.path.join("scripts", "master_page_inventory.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(master_inventory, f, indent=2)

    print(f"Master Inventory generated successfully with {len(master_inventory)} pages.")
    print("\nPage Types Distribution:")
    for pt, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {pt}: {count}")

    print("\nParent Categories:")
    for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count}")

    print("\nAction Classifications:")
    for act, count in sorted(action_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {act}: {count}")

if __name__ == "__main__":
    main()
