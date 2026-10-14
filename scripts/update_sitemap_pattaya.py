#!/usr/bin/env python3
"""
Add Pattaya sightseeing catalogue and all 19 new product pages to docs/sitemap.xml.
Maintains XML validity, formatting, priority, changefreq, and lastmod.
"""

import os
import xml.etree.ElementTree as ET

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
SITEMAP_PATH = os.path.join(DOCS_DIR, "sitemap.xml")

NEW_URLS = [
    # Catalogue page
    ("https://trippovention.co.th/packages/thailand/pattaya/sightseeing.html", "2026-10-15", "weekly", "0.8"),
    
    # 19 new sightseeing detail pages
    ("https://trippovention.co.th/packages/thailand/pattaya/sanctuary_of_truth_pattaya.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/columbia_pictures_aquaverse_tickets.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/ramayana_water_park_pattaya.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/underwater_world_pattaya.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/pattaya_dolphinarium_show.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/tiffanys_show_pattaya.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/colosseum_cabaret_show_pattaya.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/max_muay_thai_stadium_tickets.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/khao_kheow_open_zoo_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/pattaya_elephant_sanctuary_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/art_in_paradise_pattaya.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/atv_off_road_adventure_pattaya.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/khao_chi_chan_and_wat_yan_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/pattaya_city_landmarks_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/koh_larn_private_speedboat_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/pattaya_sunset_catamaran_cruise.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/scuba_diving_and_snorkeling_pattaya.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/harborland_pattaya_tickets.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/pattaya/pattaya_golf_package_with_transfers.html", "2026-10-15", "weekly", "0.7")
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
        print("All URLs already exist in sitemap. No updates needed.")
        return

    # Insert before </urlset>
    insert_str = "\n".join(added_blocks) + "\n"
    content = content.replace("</urlset>", f"{insert_str}</urlset>")

    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully added {len(added_blocks)} new URLs to sitemap.xml!")

if __name__ == "__main__":
    update_sitemap()
