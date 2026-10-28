#!/usr/bin/env python3
"""
Comprehensive SEO, AEO, Technical SEO, Sitemap and Quality Assurance Audit
specifically for Phuket Sightseeing Expansion.
"""

import os
import re
import json
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlparse

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
SITE_BASE = "https://trippovention.co.th"
PHUKET_DIR = os.path.join(DOCS_DIR, "packages", "thailand", "phuket")

class PageAuditor(HTMLParser):
    def __init__(self, filepath, rel_path):
        super().__init__()
        self.filepath = filepath
        self.rel_path = rel_path
        self.title = ""
        self.in_title = False
        self.meta_desc = ""
        self.canonical = ""
        self.h1_tags = []
        self.in_h1 = False
        self.current_h1 = ""
        self.images = []
        self.links = []
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
        elif tag == "link":
            rel = attr_dict.get("rel", "").lower()
            if rel == "canonical":
                self.canonical = attr_dict.get("href", "")
        elif tag == "h1":
            self.in_h1 = True
            self.current_h1 = ""
        elif tag == "img":
            src = attr_dict.get("src", "")
            alt = attr_dict.get("alt", None)
            self.images.append((src, alt))
        elif tag == "a":
            href = attr_dict.get("href", "")
            if href:
                self.links.append((href, attr_dict.get("title", "")))
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
        elif tag == "script" and self.in_script_json_ld:
            self.in_script_json_ld = False
            try:
                data = json.loads(self.current_script_text)
                self.json_ld.append(data)
            except Exception as e:
                self.json_ld.append({"__parse_error__": str(e), "raw": self.current_script_text[:100]})

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.in_h1:
            self.current_h1 += data
        elif self.in_script_json_ld:
            self.current_script_text += data

def audit():
    print("=" * 70)
    print("PHUKET SIGHTSEEING EXPANSION: SEO / AEO / TECHNICAL AUDIT")
    print("=" * 70)

    # 1. Target files to audit
    target_files = [
        "sightseeing.html",
        "index.html",
        # Existing 5
        "carnival_magic_show.html",
        "elephant_sanctuary.html",
        "james_bond_island_speedboat_tour.html",
        "phi_phi_island_and_khai_island_tour.html",
        "phuket_fantasea_show.html",
        # 19 New
        "phuket_city_highlights_tour.html",
        "phi_phi_maya_bamboo_island_tour.html",
        "hanuman_world_zipline_and_atv_adventure.html",
        "simon_cabaret_show_phuket.html",
        "aquaria_phuket_tickets.html",
        "phuket_thai_cooking_class.html",
        "coral_and_racha_island_tour.html",
        "similan_islands_snorkeling_tour.html",
        "phuket_sunset_catamaran_cruise.html",
        "phuket_scuba_diving_day_trip.html",
        "phuket_old_town_heritage_walking_tour.html",
        "private_phuket_city_and_viewpoints_tour.html",
        "khao_sok_national_park_day_trip.html",
        "andamanda_phuket_water_park_tickets.html",
        "siam_niramit_phuket_show.html",
        "phuket_surfing_and_stand_up_paddleboarding.html",
        "phuket_private_yacht_charter.html",
        "phuket_viewpoints_and_big_buddha_tour.html"
    ]

    total_audited = 0
    passed_checks = 0
    issues = []

    # 2. Audit each page
    for filename in target_files:
        filepath = os.path.join(PHUKET_DIR, filename)
        if not os.path.exists(filepath):
            issues.append(f"MISSING FILE: {filepath}")
            continue

        total_audited += 1
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        auditor = PageAuditor(filepath, filename)
        auditor.feed(content)

        # Check Title
        if not auditor.title or len(auditor.title.strip()) < 15:
            issues.append(f"{filename}: Weak or missing title: '{auditor.title}'")
        else:
            passed_checks += 1

        # Check Meta Description
        if not auditor.meta_desc or len(auditor.meta_desc.strip()) < 50:
            issues.append(f"{filename}: Weak or missing meta description: '{auditor.meta_desc}'")
        else:
            passed_checks += 1

        # Check Canonical
        if filename == "index.html":
            expected_canonical = f"{SITE_BASE}/packages/thailand/phuket/"
        else:
            expected_canonical = f"{SITE_BASE}/packages/thailand/phuket/{filename}"
        if auditor.canonical != expected_canonical:
            issues.append(f"{filename}: Canonical mismatch. Expected {expected_canonical}, got {auditor.canonical}")
        else:
            passed_checks += 1

        # Check H1
        if len(auditor.h1_tags) == 0:
            issues.append(f"{filename}: Missing H1 tag")
        elif len(auditor.h1_tags) > 1:
            issues.append(f"{filename}: Multiple H1 tags found: {auditor.h1_tags}")
        else:
            passed_checks += 1

        # Check Images Alt tags and Existence
        for src, alt in auditor.images:
            if alt is None or alt.strip() == "":
                issues.append(f"{filename}: Image missing alt text: {src}")
            else:
                passed_checks += 1

            # Check local file existence if relative
            if not src.startswith("http") and not src.startswith("data:"):
                # resolve path relative to file
                img_path = os.path.normpath(os.path.join(os.path.dirname(filepath), src))
                if not os.path.exists(img_path):
                    issues.append(f"{filename}: Image file not found locally: {src} -> {img_path}")
                else:
                    passed_checks += 1

        # Check JSON-LD
        has_schema_error = False
        for schema in auditor.json_ld:
            if "__parse_error__" in schema:
                issues.append(f"{filename}: Invalid JSON-LD schema syntax: {schema['__parse_error__']}")
                has_schema_error = True
        if not has_schema_error and len(auditor.json_ld) > 0:
            passed_checks += 1

        # Check Internal Links (verify local targets exist)
        for href, _ in auditor.links:
            # Skip external, anchor, mailto, tel, whatsapp
            if (
                href.startswith("http")
                or href.startswith("#")
                or href.startswith("mailto:")
                or href.startswith("tel:")
                or href.startswith("javascript:")
            ):
                continue
            
            # Remove query string / anchor
            clean_href = href.split("?")[0].split("#")[0]
            if not clean_href:
                continue

            target_path = os.path.normpath(os.path.join(os.path.dirname(filepath), clean_href))
            if not os.path.exists(target_path):
                issues.append(f"{filename}: Broken relative link to: {href} (resolved: {target_path})")
            else:
                passed_checks += 1

    # 3. Check Sitemap
    sitemap_path = os.path.join(DOCS_DIR, "sitemap.xml")
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            sitemap_content = f.read()
        
        sitemap_tree = ET.fromstring(sitemap_content)
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        sitemap_locs = {el.text.strip() for el in sitemap_tree.findall("sm:url/sm:loc", ns) if el.text}

        for filename in target_files:
            if filename == "index.html":
                expected_url = f"{SITE_BASE}/packages/thailand/phuket/"
            else:
                expected_url = f"{SITE_BASE}/packages/thailand/phuket/{filename}"
            if expected_url not in sitemap_locs:
                issues.append(f"SITEMAP MISSING: {expected_url}")
            else:
                passed_checks += 1

    # 4. Check LLMS.txt
    llms_path = os.path.join(DOCS_DIR, "llms.txt")
    if os.path.exists(llms_path):
        with open(llms_path, "r", encoding="utf-8") as f:
            llms_content = f.read()
        if "https://trippovention.co.th/packages/thailand/phuket/sightseeing.html" in llms_content:
            passed_checks += 1
        else:
            issues.append("llms.txt: Missing Phuket sightseeing catalogue link")

    # 5. Check Enquiry & Offline Flow Rules
    for filename in target_files:
        filepath = os.path.join(PHUKET_DIR, filename)
        if not os.path.exists(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            c = f.read().lower()
        forbidden_keywords = ["add to cart", "checkout", "shopping cart", "stripe", "paypal", "instant booking"]
        for kw in forbidden_keywords:
            if kw in c:
                issues.append(f"{filename}: Found forbidden transactional term: '{kw}'")

    print(f"\nAudit completed for {total_audited} pages.")
    print(f"Passed Quality Checks: {passed_checks}")
    print(f"Total Issues Found: {len(issues)}")

    if issues:
        print("\nISSUES DETECTED:")
        for idx, iss in enumerate(issues, start=1):
            print(f"  {idx}. {iss}")
        return False
    else:
        print("\n✅ PERFECT PASS! 0 issues found across all SEO, AEO, canonical, sitemap, image, and link checks!")
        return True

if __name__ == "__main__":
    success = audit()
    exit(0 if success else 1)
