#!/usr/bin/env python3
"""
Download and convert authentic images for Pattaya Sightseeing products from Wikimedia Commons.
Resizes and converts to WebP format.
"""

import os
import sys
import json
import urllib.request
import subprocess

TARGET_DIR = "docs/assets/images/packages/thailand/pattaya/sightseeingoptions"
os.makedirs(TARGET_DIR, exist_ok=True)
TEMP_DIR = "/tmp/pattaya_img_temp"
os.makedirs(TEMP_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "TrippoventionBot/1.0 (https://trippovention.co.th; contact@trippovention.co.th)"
}

IMAGE_TASKS = [
    {
        "filename": "hero_sanctuary_of_truth_pattaya.webp",
        "queries": ["Sanctuary of Truth Pattaya", "Sanctuary of Truth"]
    },
    {
        "filename": "hero_columbia_pictures_aquaverse.webp",
        "queries": ["Columbia Pictures Aquaverse", "Cartoon Network Amazone Pattaya water slide", "water park Pattaya slide"]
    },
    {
        "filename": "hero_ramayana_water_park.webp",
        "queries": ["Ramayana Water Park", "Ramayana Water Park Pattaya", "water park Thailand slide"]
    },
    {
        "filename": "hero_underwater_world_pattaya.webp",
        "queries": ["Underwater World Pattaya", "aquarium shark tunnel Thailand", "oceanarium underwater tunnel"]
    },
    {
        "filename": "hero_pattaya_dolphinarium.webp",
        "queries": ["Pattaya Dolphinarium", "dolphin show Pattaya", "dolphin show Thailand"]
    },
    {
        "filename": "hero_tiffanys_show_pattaya.webp",
        "queries": ["Tiffany's Show Pattaya", "Tiffany Show Pattaya", "cabaret show Pattaya"]
    },
    {
        "filename": "hero_colosseum_cabaret_show.webp",
        "queries": ["Colosseum Show Pattaya", "Colosseum Cabaret Pattaya", "cabaret theatre Pattaya"]
    },
    {
        "filename": "hero_max_muay_thai_stadium.webp",
        "queries": ["Max Muay Thai Pattaya", "Muay Thai stadium match", "Muay Thai fight Thailand"]
    },
    {
        "filename": "hero_khao_kheow_open_zoo.webp",
        "queries": ["Khao Kheow Open Zoo", "Khao Kheow Zoo"]
    },
    {
        "filename": "hero_art_in_paradise_pattaya.webp",
        "queries": ["Art in Paradise Pattaya", "Art in Paradise trick art"]
    },
    {
        "filename": "hero_atv_off_road_adventure.webp",
        "queries": ["ATV Thailand tour", "quad bike off road Thailand", "ATV trail Pattaya"]
    },
    {
        "filename": "hero_khao_chi_chan_buddha_mountain.webp",
        "queries": ["Khao Chi Chan", "Buddha Mountain Pattaya", "Laser Buddha Pattaya"]
    },
    {
        "filename": "hero_pattaya_viewpoint_big_buddha.webp",
        "queries": ["Wat Phra Yai Pattaya", "Big Buddha Pattaya", "Pattaya Viewpoint Pratumnak"]
    },
    {
        "filename": "hero_koh_larn_private_speedboat.webp",
        "queries": ["Koh Larn beach Pattaya", "Ko Lan speedboat", "Koh Larn Pattaya island"]
    },
    {
        "filename": "hero_pattaya_sunset_catamaran_cruise.webp",
        "queries": ["Catamaran sunset Thailand", "sailing catamaran Pattaya", "yacht cruise Pattaya"]
    },
    {
        "filename": "hero_pattaya_scuba_diving_snorkeling.webp",
        "queries": ["Scuba diving coral reef Thailand", "snorkeling Koh Larn", "scuba diving Pattaya reef"]
    },
    {
        "filename": "hero_harborland_indoor_playground.webp",
        "queries": ["HarborLand indoor playground", "indoor playground slides children", "indoor play park ball pit"]
    },
    {
        "filename": "hero_pattaya_golf_championship.webp",
        "queries": ["Siam Country Club Pattaya", "golf course Pattaya", "golf course Thailand fairways"]
    }
]

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
    
    # Use sips to resize to max width 1200 or 800
    subprocess.run(["sips", "-Z", "1200", temp_img], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Convert to webp with cwebp
    cwebp_cmd = ["cwebp", "-q", "80", temp_img, "-o", out_path]
    subprocess.run(cwebp_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
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
