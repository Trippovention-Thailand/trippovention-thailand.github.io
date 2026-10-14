#!/usr/bin/env python3
"""
Add Bangkok sightseeing catalogue and all new product pages to docs/sitemap.xml.
Maintains XML validity, formatting, priority, changefreq, and lastmod.
"""

import os
import xml.etree.ElementTree as ET

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
SITEMAP_PATH = os.path.join(DOCS_DIR, "sitemap.xml")

NEW_URLS = [
    # Catalogue page
    ("https://trippovention.co.th/packages/thailand/bangkok/sightseeing.html", "2026-10-15", "weekly", "0.8"),
    
    # 19 new sightseeing detail pages
    ("https://trippovention.co.th/packages/thailand/bangkok/ancient_city_and_erawan_museum_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/ayutthaya_historical_park_full_day_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/bangkok_canals_private_longtail_boat_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/bangkok_midnight_tuk_tuk_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/bangkok_temples_and_heritage_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/calypso_cabaret_show_bangkok.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/chao_phraya_river_sightseeing_cruise.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/chinatown_yaowarat_street_food_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/damnoen_saduak_floating_market_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/grand_palace_and_wat_phra_kaew_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/madame_tussauds_bangkok.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/maeklong_railway_market_and_floating_market_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/mirinn_cabaret_theatre_bangkok.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/safari_world_open_zoo_drive_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/sea_life_bangkok_ocean_world.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/siam_amazing_park_bangkok.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/wat_arun_temple_of_dawn_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/wat_pho_and_reclining_buddha_tour.html", "2026-10-15", "weekly", "0.7"),
    ("https://trippovention.co.th/packages/thailand/bangkok/white_orchid_river_dinner_cruise.html", "2026-10-15", "weekly", "0.7")
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
        print("All URLs already exist in sitemap.xml.")
        return

    # Insert before </urlset>
    new_entries_str = "\n".join(added_blocks) + "\n"
    content = content.replace("</urlset>", new_entries_str + "</urlset>")

    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Added {len(added_blocks)} new URLs to docs/sitemap.xml.")

if __name__ == "__main__":
    update_sitemap()
