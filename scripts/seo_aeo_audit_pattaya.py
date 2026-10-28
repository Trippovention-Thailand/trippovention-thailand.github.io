#!/usr/bin/env python3
"""
Comprehensive SEO, AEO, Technical SEO, Sitemap and Quality Assurance Audit
specifically for Pattaya Sightseeing Expansion.
"""

import os
import re
import json
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlparse

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
SITE_BASE = "https://trippovention.co.th"
PATTAYA_DIR = os.path.join(DOCS_DIR, "packages", "thailand", "pattaya")

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

def audit_pattaya():
    print("=" * 70)
    print("STARTING PATTAYA EXPANSION QA & SEO/AEO AUDIT")
    print("=" * 70)

    # 1. Sitemap Audit
    sitemap_path = os.path.join(DOCS_DIR, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        sitemap_xml = f.read()
    sitemap_tree = ET.fromstring(sitemap_xml)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = set()
    for u in sitemap_tree.findall("sm:url", ns):
        loc = u.find("sm:loc", ns)
        if loc is not None and loc.text:
            sitemap_urls.add(loc.text.strip())

    print(f"✓ Total URLs in sitemap.xml: {len(sitemap_urls)}")

    # 2. Check Parent Page Connection
    parent_path = os.path.join(PATTAYA_DIR, "index.html")
    with open(parent_path, "r", encoding="utf-8") as f:
        parent_content = f.read()

    tile_found = "EXPLORE MORE OPTIONS OF SIGHTSEEING OF PATTAYA" in parent_content
    tile_link_correct = 'href="sightseeing.html"' in parent_content
    print(f"✓ Parent page sightseeing tile exists: {tile_found}")
    print(f"✓ Sightseeing tile correctly links to sightseeing.html: {tile_link_correct}")
    if not (tile_found and tile_link_correct):
        print("  ERROR: Parent page connection failed!")

    # 3. Floating Market Prohibition Check
    print("\n--- Checking Floating Market Exclusion ---")
    pattaya_files = [os.path.join(PATTAYA_DIR, f) for f in os.listdir(PATTAYA_DIR) if f.endswith(".html")]
    floating_market_violations = []
    for pf in pattaya_files:
        with open(pf, "r", encoding="utf-8") as f:
            content = f.read().lower()
            if "pattaya floating market" in content:
                floating_market_violations.append(os.path.basename(pf))
    
    if floating_market_violations:
        print(f"  ❌ VIOLATION: 'Pattaya Floating Market' found in: {floating_market_violations}")
    else:
        print("  ✓ PASSED: Zero mentions of Pattaya Floating Market across all Pattaya pages.")

    # 4. Audit Catalogue and Product Pages
    print("\n--- Auditing Catalogue & Product Pages ---")
    pages_to_audit = [
        "sightseeing.html",
        "sanctuary_of_truth_pattaya.html",
        "alcazar_cabaret_show.html",
        "coral_island_tour.html",
        "dolphin_show_with_tiger_park.html",
        "nong_nooch_tropical_garden.html",
        "pattaya_city_tour_with_colosseum_show.html",
        "columbia_pictures_aquaverse_tickets.html",
        "ramayana_water_park_pattaya.html",
        "underwater_world_pattaya.html",
        "pattaya_dolphinarium_show.html",
        "tiffanys_show_pattaya.html",
        "colosseum_cabaret_show_pattaya.html",
        "max_muay_thai_stadium_tickets.html",
        "khao_kheow_open_zoo_tour.html",
        "pattaya_elephant_sanctuary_tour.html",
        "art_in_paradise_pattaya.html",
        "atv_off_road_adventure_pattaya.html",
        "khao_chi_chan_and_wat_yan_tour.html",
        "pattaya_city_landmarks_tour.html",
        "koh_larn_private_speedboat_tour.html",
        "pattaya_sunset_catamaran_cruise.html",
        "scuba_diving_and_snorkeling_pattaya.html",
        "harborland_pattaya_tickets.html",
        "pattaya_golf_package_with_transfers.html"
    ]

    all_passed = True
    for filename in pages_to_audit:
        filepath = os.path.join(PATTAYA_DIR, filename)
        if not os.path.exists(filepath):
            print(f"❌ MISSING FILE: {filename}")
            all_passed = False
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            raw_html = f.read()

        parser = PageAuditor(filepath, filename)
        parser.feed(raw_html)

        # Validations
        errors = []
        # Title check
        if not parser.title or len(parser.title) < 15:
            errors.append(f"Title missing or too short: '{parser.title}'")

        # Meta desc check
        if not parser.meta_desc or len(parser.meta_desc) < 30:
            errors.append(f"Meta description missing or too short: '{parser.meta_desc}'")

        # H1 check
        if len(parser.h1_tags) != 1:
            errors.append(f"Expected exactly 1 H1, found {len(parser.h1_tags)}: {parser.h1_tags}")

        # Canonical check
        expected_canonical = f"{SITE_BASE}/packages/thailand/pattaya/{filename}"
        if parser.canonical != expected_canonical:
            errors.append(f"Canonical mismatch: expected '{expected_canonical}', got '{parser.canonical}'")

        # Sitemap check
        if expected_canonical not in sitemap_urls:
            errors.append(f"Page missing from sitemap.xml: {expected_canonical}")

        # JSON-LD Schema check
        schema_types = []
        for s in parser.json_ld:
            if isinstance(s, dict):
                st = s.get("@type", "")
                if isinstance(st, list):
                    schema_types.extend(st)
                else:
                    schema_types.append(st)
        
        if filename == "sightseeing.html":
            if "TouristDestination" not in schema_types or "BreadcrumbList" not in schema_types or "FAQPage" not in schema_types:
                errors.append(f"Catalogue missing schema: found {schema_types}")
        else:
            if ("TouristTrip" not in schema_types and "Product" not in schema_types) or "BreadcrumbList" not in schema_types or "FAQPage" not in schema_types:
                errors.append(f"Product page missing schema: found {schema_types}")

        # Image existence check
        for src, alt in parser.images:
            if not alt or not alt.strip():
                errors.append(f"Image missing alt attribute: {src}")
            # check local disk existence
            if src.startswith("../../../"):
                img_disk = os.path.join(DOCS_DIR, src.replace("../../../", ""))
            elif src.startswith("/"):
                img_disk = os.path.join(DOCS_DIR, src.lstrip("/"))
            elif not src.startswith("http"):
                img_disk = os.path.join(PATTAYA_DIR, src)
            else:
                img_disk = None

            if img_disk and not os.path.exists(img_disk):
                errors.append(f"Image not found on disk: {src} -> {img_disk}")

        # Internal link check
        for href, title in parser.links:
            if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("https://wa.me") or href.startswith("https://"):
                continue
            clean_href = href.split("?")[0].split("#")[0]
            if clean_href.startswith("../../../"):
                link_disk = os.path.join(DOCS_DIR, clean_href.replace("../../../", ""))
            elif clean_href.startswith("../"):
                link_disk = os.path.join(DOCS_DIR, "packages", "thailand", clean_href.replace("../", ""))
            else:
                link_disk = os.path.join(PATTAYA_DIR, clean_href)

            if not os.path.exists(link_disk):
                errors.append(f"Broken internal link: {href} (resolved: {link_disk})")

        if errors:
            print(f"❌ {filename}: {len(errors)} errors")
            for err in errors:
                print(f"    - {err}")
            all_passed = False
        else:
            print(f"✓ {filename}: Perfect (Title, H1, Meta, Canonical, Schema {schema_types}, Images, Links)")

    print("\n" + "=" * 70)
    if all_passed:
        print("ALL 25 PATTAYA SIGHTSEEING PAGES PASSED AUDIT WITH 100% SUCCESS!")
    else:
        print("AUDIT FINISHED WITH SOME ISSUES TO RESOLVE.")
    print("=" * 70)

if __name__ == "__main__":
    audit_pattaya()
