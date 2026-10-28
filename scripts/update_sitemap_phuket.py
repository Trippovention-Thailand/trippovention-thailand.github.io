#!/usr/bin/env python3
"""
Add Phuket sightseeing catalogue and all 19 new product pages to docs/sitemap.xml.
Maintains XML validity, formatting, priority, changefreq, and lastmod.
"""

import os
import xml.etree.ElementTree as ET

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
SITEMAP_PATH = os.path.join(DOCS_DIR, "sitemap.xml")

NEW_URLS = [
    # Catalogue page
    ("https://trippovention.co.th/packages/thailand/phuket/sightseeing.html", "2026-10-15", "weekly", "0.8"),
    
    # 19 new sightseeing detail pages
    ("https://trippovention.co.th/packages/thailand/phuket/phuket_city_highlights_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/phi_phi_maya_bamboo_island_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/hanuman_world_zipline_and_atv_adventure.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/simon_cabaret_show_phuket.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/aquaria_phuket_tickets.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/phuket_thai_cooking_class.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/coral_and_racha_island_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/similan_islands_snorkeling_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/phuket_sunset_catamaran_cruise.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/phuket_scuba_diving_day_trip.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/phuket_old_town_heritage_walking_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/private_phuket_city_and_viewpoints_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/khao_sok_national_park_day_trip.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/andamanda_phuket_water_park_tickets.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/siam_niramit_phuket_show.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/phuket_surfing_and_stand_up_paddleboarding.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/phuket_private_yacht_charter.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/phuket/phuket_viewpoints_and_big_buddha_tour.html", "2026-10-15", "weekly", "0.7")
]

def update_sitemap():
    with open(SITEMAP_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse existing URLs to avoid duplicates
    existing_locs = set()
    tree = ET.fromstring(content)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    for url_el in tree.findall("sm:url", ns):
        loc = url_el.find("sm:loc", ns)
        if loc is not None and loc.text:
            existing_locs.add(loc.text.strip())

    added_blocks = []
    for loc, lastmod, changefreq, priority in NEW_URLS:
        if loc not in existing_locs:
            block = f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""
            added_blocks.append(block)

    if not added_blocks:
        print("All URLs already present in sitemap.xml!")
        return

    # Insert before </urlset>
    insert_str = "\n".join(added_blocks) + "\n"
    if "</urlset>" in content:
        content = content.replace("</urlset>", insert_str + "</urlset>")
    else:
        raise ValueError("Invalid sitemap: </urlset> not found")

    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully added {len(added_blocks)} new Phuket URLs to {SITEMAP_PATH}")

if __name__ == "__main__":
    update_sitemap()
