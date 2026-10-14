#!/usr/bin/env python3
"""
Download and convert authentic images for Phuket Sightseeing products from Wikimedia Commons.
Converts existing JPGs in sightseeingoptions to WebP and generates all missing images.
"""

import os
import sys
import json
import urllib.request
import subprocess

TARGET_DIR = "docs/assets/images/packages/thailand/phuket/sightseeingoptions"
os.makedirs(TARGET_DIR, exist_ok=True)
TEMP_DIR = "/tmp/phuket_img_temp"
os.makedirs(TEMP_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "TrippoventionBot/1.0 (https://trippovention.co.th; contact@trippovention.co.th)"
}

IMAGE_TASKS = [
    {
        "filename": "hero_phuket_city_highlights.webp",
        "queries": ["Buildings in Old Phuket Town", "Old Phuket Town Sino-Portuguese", "Phuket Old Town architecture"]
    },
    {
        "filename": "hero_hanuman_world_zipline.webp",
        "queries": ["zipline Thailand rainforest", "tree top adventure Thailand", "Hanuman World Phuket"]
    },
    {
        "filename": "hero_simon_cabaret_show.webp",
        "queries": ["Simon Cabaret Phuket", "Simon Cabaret", "cabaret show Thailand dancers"]
    },
    {
        "filename": "hero_aquaria_phuket.webp",
        "queries": ["Aquaria Phuket", "aquarium shark tunnel oceanarium", "aquarium manta ray underwater"]
    },
    {
        "filename": "hero_phuket_thai_cooking_class.webp",
        "queries": ["Thai cooking class ingredients", "Thai cooking school wok", "cooking class Thailand food"]
    },
    {
        "filename": "hero_coral_and_racha_island.webp",
        "queries": ["Ko Racha Yai beach", "Racha Yai island", "Racha Island Thailand"]
    },
    {
        "filename": "hero_similan_islands_snorkeling.webp",
        "queries": ["Similan Island 01", "Similan Islands Thailand", "Similan Island sailing rock"]
    },
    {
        "filename": "hero_phuket_sunset_catamaran_cruise.webp",
        "queries": ["Sunset at sea with catamaran. Thailand.jpg", "sunset cruise Phuket catamaran", "sailing catamaran Thailand sunset"]
    },
    {
        "filename": "hero_phuket_scuba_diving_day_trip.webp",
        "queries": ["2010 Thailand Koh Phi Phi & Lanta scuba diving3.jpg", "Scuba diving coral reef Andaman", "scuba diving sea turtle Thailand"]
    },
    {
        "filename": "hero_phuket_old_town_heritage.webp",
        "queries": ["Soi Rommanee Phuket", "Phuket Old Town street", "Thalang Road Phuket"]
    },
    {
        "filename": "hero_phuket_luxury_spa_wellness.webp",
        "queries": ["Thai massage spa therapy", "Thai spa herbal ball massage", "traditional Thai massage herbal"]
    },
    {
        "filename": "hero_private_phuket_city_viewpoints.webp",
        "queries": ["Beautiful Sunset on Promthep Cape, Phuket island", "Promthep Cape sunset", "Karon Viewpoint Phuket"]
    },
    {
        "filename": "hero_khao_sok_cheow_lan_lake.webp",
        "queries": ["Trees rising out of Cheow Lan Lake", "Cheow Lan Lake limestone", "Khao Sok Cheow Lan"]
    },
    {
        "filename": "hero_andamanda_phuket_water_park.webp",
        "queries": ["Andamanda Phuket", "water park slides Thailand", "water park wave pool slide"]
    },
    {
        "filename": "hero_siam_niramit_phuket.webp",
        "queries": ["Siam Niramit Phuket", "Siam Niramit stage", "Thai cultural dance stage show"]
    },
    {
        "filename": "hero_phuket_surfing_sup.webp",
        "queries": ["Surfing Kata Beach Phuket", "stand up paddleboard tropical ocean", "surfing Andaman Thailand"]
    },
    {
        "filename": "hero_phuket_private_yacht_charter.webp",
        "queries": ["luxury sailing yacht Phuket", "private yacht Andaman Sea", "catamaran yacht Phuket turquoise"]
    },
    {
        "filename": "hero_phuket_big_buddha_wat_chalong.webp",
        "queries": ["Big Buddha Phuket", "Big Buddha statue Phuket", "Grand Pagoda - Wat Chalong.jpg"]
    }
]

def convert_existing_jpgs():
    jpgs = [
        ("hero_carnival_magic_show_with_dinner.jpg", "hero_carnival_magic_show_with_dinner.webp"),
        ("hero_james_bond_island_speedboat_tour.jpg", "hero_james_bond_island_speedboat_tour.webp"),
        ("hero_phuket_elephant_sanctuary.jpg", "hero_phuket_elephant_sanctuary.webp"),
        ("hero_phuket_fantasea_show_with_dinner.jpg", "hero_phuket_fantasea_show_with_dinner.webp")
    ]
    for src_name, dst_name in jpgs:
        src = os.path.join(TARGET_DIR, src_name)
        dst = os.path.join(TARGET_DIR, dst_name)
        if os.path.exists(src) and (not os.path.exists(dst) or os.path.getsize(dst) < 1000):
            print(f"Converting existing JPG {src_name} -> {dst_name}...")
            temp_img = os.path.join(TEMP_DIR, "conv_temp.jpg")
            subprocess.run(["sips", "-Z", "1200", src, "--out", temp_img], check=True, stdout=subprocess.DEVNULL)
            subprocess.run(["cwebp", "-q", "80", temp_img, "-o", dst], check=True, stdout=subprocess.DEVNULL)
            print(f"  Converted {dst_name} ({os.path.getsize(dst)} bytes)")

def copy_repo_images():
    # Copy phi phi maya bay day trip image to hero_phi_phi_maya_bamboo.webp
    src = "docs/assets/images/packages/thailand/daytrips/hero_phi_phi_maya_bay_speedboat_day_trip.webp"
    dst = os.path.join(TARGET_DIR, "hero_phi_phi_maya_bamboo.webp")
    if os.path.exists(src) and (not os.path.exists(dst) or os.path.getsize(dst) < 1000):
        print(f"Copying {src} -> {dst}...")
        subprocess.run(["cp", src, dst], check=True)
        print(f"  Copied hero_phi_phi_maya_bamboo.webp ({os.path.getsize(dst)} bytes)")

def search_wikimedia(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrnamespace=6&gsrlimit=5&prop=imageinfo&iiprop=url|size|mime"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            pages = data.get("query", {}).get("pages", {})
            results = []
            for page in pages.values():
                info_list = page.get("imageinfo", [])
                if info_list:
                    info = info_list[0]
                    img_url = info.get("url", "")
                    mime = info.get("mime", "")
                    w = info.get("width", 0)
                    h = info.get("height", 0)
                    if ("jpeg" in mime or "png" in mime or "jpg" in mime) and w >= 600 and h >= 400:
                        results.append((img_url, w, h, page.get("title", "")))
            return results
    except Exception as e:
        print(f"Error searching {query}: {e}")
        return []

def download_and_convert(img_url, out_path):
    temp_img = os.path.join(TEMP_DIR, "raw_img")
    curl_cmd = [
        "curl", "-s", "-L",
        "-H", "User-Agent: TrippoventionBot/1.0 (https://trippovention.co.th; contact@trippovention.co.th)",
        img_url, "-o", temp_img
    ]
    subprocess.run(curl_cmd, check=True)
    
    # Use sips to resize to max width 1200
    subprocess.run(["sips", "-Z", "1200", temp_img], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Convert to webp with cwebp
    cwebp_cmd = ["cwebp", "-q", "80", temp_img, "-o", out_path]
    subprocess.run(cwebp_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    convert_existing_jpgs()
    copy_repo_images()

    for task in IMAGE_TASKS:
        out_file = os.path.join(TARGET_DIR, task["filename"])
        if os.path.exists(out_file) and os.path.getsize(out_file) > 10000:
            print(f"Already exists: {task['filename']}")
            continue
        
        print(f"Processing: {task['filename']}...")
        found = False
        for q in task["queries"]:
            print(f"  Searching '{q}'...")
            results = search_wikimedia(q)
            if results:
                # pick highest resolution
                results.sort(key=lambda x: x[1] * x[2], reverse=True)
                img_url, w, h, title = results[0]
                print(f"  Found: {title} ({w}x{h}) -> {img_url}")
                try:
                    download_and_convert(img_url, out_file)
                    print(f"  Saved {task['filename']} ({os.path.getsize(out_file)} bytes)")
                    found = True
                    break
                except Exception as e:
                    print(f"  Failed to convert {title}: {e}")
        
        if not found:
            print(f"  WARNING: Could not find image for {task['filename']}")

if __name__ == "__main__":
    main()
