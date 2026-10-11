#!/usr/bin/env python3
"""
Trippovention Thailand Search Index Builder
Crawls docs/ directory and builds docs/assets/search-index.json and docs/assets/search-data.js
"""

import os
import re
import json
from html import unescape

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT_DIR, 'docs')
INDEX_JSON_OUTPUT = os.path.join(DOCS_DIR, 'assets', 'search-index.json')
INDEX_JS_OUTPUT = os.path.join(DOCS_DIR, 'assets', 'search-data.js')

DESTINATIONS_META = {
    'bangkok': {
        'name': 'Bangkok',
        'keywords': ['bkk', 'dmk', 'suvarnabhumi', 'don mueang', 'capital', 'krung thep', 'chao phraya', 'temple of dawn', 'grand palace']
    },
    'phuket': {
        'name': 'Phuket',
        'keywords': ['hkt', 'patong', 'kata', 'karon', 'rawai', 'andaman', 'big buddha', 'old town phuket', 'promthep cape']
    },
    'pattaya': {
        'name': 'Pattaya',
        'keywords': ['utp', 'utapao', 'jomtien', 'coral island', 'koh larn', 'walking street', 'chonburi']
    },
    'krabi': {
        'name': 'Krabi',
        'keywords': ['kbv', 'ao nang', 'railay', 'phra nang', 'hong islands', 'four islands', 'emerald pool', 'hot springs', 'dragon crest']
    },
    'chiang_mai': {
        'name': 'Chiang Mai',
        'keywords': ['cnx', 'northern thailand', 'doi inthanon', 'lanna', 'night bazaar', 'elephants', 'sticky waterfall']
    },
    'chiang_rai': {
        'name': 'Chiang Rai',
        'keywords': ['cei', 'white temple', 'wat rong khun', 'blue temple', 'golden triangle', 'doi tung', 'hill tribe']
    },
    'koh_samui': {
        'name': 'Koh Samui',
        'keywords': ['usm', 'samui', 'chaweng', 'lamai', 'ang thong', 'surat thani', 'gulf of thailand', 'pig island']
    },
    'koh_larn': {
        'name': 'Koh Larn (Coral Island)',
        'keywords': ['coral island', 'pattaya island', 'tawaen beach', 'water sports']
    },
    'koh_phangan': {
        'name': 'Koh Phangan',
        'keywords': ['full moon party', 'haad rin', 'thong sala', 'samui archipelago']
    },
    'koh_samet': {
        'name': 'Koh Samet',
        'keywords': ['samet', 'rayong', 'sai kaew', 'national park island']
    },
    'hua_hin': {
        'name': 'Hua Hin',
        'keywords': ['cha am', 'royal beach resort', 'maruekhathaiyawan', 'pranburi']
    },
    'ayutthaya': {
        'name': 'Ayutthaya',
        'keywords': ['ancient capital', 'unesco world heritage', 'wat mahathat', 'buddha head in tree', 'ruins']
    },
    'koh_yao_yai': {
        'name': 'Koh Yao Yai',
        'keywords': ['koh yao', 'phang nga bay', 'peaceful island retreat', 'sanctuary']
    },
    'koh_mook': {
        'name': 'Koh Mook',
        'keywords': ['emerald cave', 'tham morakot', 'trang islands', 'dugong']
    },
    'trang': {
        'name': 'Trang',
        'keywords': ['trang islands', 'koh kradan', 'koh ngai', 'southern thailand']
    },
    'phi_phi_island': {
        'name': 'Phi Phi Island',
        'keywords': ['phi phi leh', 'phi phi don', 'maya bay', 'pileh lagoon', 'viking cave', 'the beach']
    }
}

SYNONYMS_AND_ALIASES = {
    'transfer': ['pickup', 'drop', 'taxi', 'cab', 'car', 'shuttle', 'private vehicle', 'van', 'minivan', 'transport', 'airport transfer', 'hotel transfer'],
    'package': ['tour', 'itinerary', 'holiday', 'trip', 'vacation', 'stay', 'deal'],
    'sightseeing': ['attraction', 'activities', 'things to do', 'tickets', 'excursion', 'experience', 'day tour'],
    'cruise': ['boat', 'yacht', 'catamaran', 'ferry', 'dinner cruise', 'sunset cruise', 'sailing'],
    'island': ['beaches', 'islands', 'island hopping', 'coastal', 'bay'],
    'elephant': ['sanctuary', 'ethical', 'wildlife', 'care program'],
    'honeymoon': ['romantic', 'couples', 'couples retreat', 'candlelight'],
    'family': ['kids', 'children', 'family holiday', 'family friendly']
}

EXCLUDE_FILES = {
    '404.html',
    'offline.html',
    'thank-you.html',
    'search.html',
    'privacy-policy.html',
    'refund-policy.html',
    'terms-and-conditions.html'
}

def clean_html(text):
    if not text:
        return ''
    text = re.sub(r'<[^>]+>', ' ', text)
    text = unescape(text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_meta_content(html, name_or_prop):
    match = re.search(rf'<meta\s+[^>]*(?:name|property)=["\']{re.escape(name_or_prop)}["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
    if not match:
        match = re.search(rf'<meta\s+[^>]*content=["\']([^"\']+)["\'][^>]*(?:name|property)=["\']{re.escape(name_or_prop)}["\']', html, re.I)
    return clean_html(match.group(1)) if match else ''

def extract_tag_text(html, tag):
    match = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', html, re.I | re.DOTALL)
    return clean_html(match.group(1)) if match else ''

def detect_category_and_destination(rel_path, title, desc, h1):
    combined = f"{rel_path} {title} {desc} {h1}".lower()
    
    # Destination detection
    dest_name = 'Thailand'
    for key, meta in DESTINATIONS_META.items():
        if key.replace('_', '-') in rel_path or key in rel_path or meta['name'].lower() in combined:
            dest_name = meta['name']
            break
            
    # Category detection
    if rel_path == 'index.html':
        return 'Overview', 'Thailand'
    if rel_path in ['destinations.html', 'destinations-themes.html', 'destinations-travelers.html']:
        return 'Destination', 'Thailand'
    if 'transfers.html' in rel_path or 'transfer' in rel_path:
        return 'Transfer', dest_name
    if 'day-trips.html' in rel_path or 'daytrip' in rel_path:
        return 'Day Trip', dest_name
    if 'sightseeing' in rel_path or 'tour' in rel_path and ('show' in combined or 'safari' in combined or 'park' in combined or 'cruise' in combined or 'climbing' in combined or 'kayak' in combined or 'experience' in combined or 'sanctuary' in combined or 'spa' in combined):
        return 'Sightseeing', dest_name
    if 'packages/' in rel_path:
        if rel_path.endswith('/index.html'):
            return 'Destination', dest_name
        return 'Package', dest_name
    if 'land-packages.html' in rel_path:
        return 'Package', 'Thailand'
    if 'services.html' in rel_path:
        return 'Service', 'Thailand'
    if 'contact.html' in rel_path:
        return 'Contact', 'Thailand'
        
    return 'General', dest_name

def extract_image_url(html, rel_path):
    # Try og:image
    og_img = extract_meta_content(html, 'og:image')
    if og_img:
        # Convert absolute trippovention URL to relative path from root
        og_img = re.sub(r'^https?://[^/]+/', '', og_img)
        return og_img
        
    # Try first img in img-wrap or hero
    img_match = re.search(r'<div class="img-wrap">\s*<img[^>]+src=["\']([^"\']+)["\']', html)
    if not img_match:
        img_match = re.search(r'<header class="hero[^"]*">\s*<div[^>]*>.*?<img[^>]+src=["\']([^"\']+)["\']', html, re.DOTALL)
    if not img_match:
        img_match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', html)
        
    if img_match:
        src = img_match.group(1)
        # Normalize relative path to root
        cur_dir = os.path.dirname(rel_path)
        norm = os.path.normpath(os.path.join(cur_dir, src)).replace('\\', '/')
        if norm.startswith('./'):
            norm = norm[2:]
        return norm
    return 'assets/images/logo.webp'

def extract_price(html):
    match = re.search(r'<span class="price[^"]*">([^<]+)</span>', html)
    if match:
        p = clean_html(match.group(1))
        if p and p != 'Current Offer':
            return p
    return ''

def build_keywords(title, desc, dest, category, rel_path):
    tokens = set()
    for text in [title, desc, dest, category, rel_path]:
        for word in re.findall(r'[a-zA-Z0-9]+', text.lower()):
            if len(word) >= 2:
                tokens.add(word)
                
    # Add destination aliases
    dest_key = dest.lower().replace(' ', '_').replace('-', '_')
    for k, v in DESTINATIONS_META.items():
        if k in dest_key or v['name'].lower() == dest.lower():
            for kw in v['keywords']:
                tokens.add(kw.lower())
                
    # Add category and concept synonyms
    for term, syns in SYNONYMS_AND_ALIASES.items():
        if term in tokens:
            for s in syns:
                tokens.add(s.lower())
                
    return list(tokens)

def parse_card_products_from_page(html, rel_path, default_cat, default_dest):
    """Extract individual product cards from aggregate pages like transfers.html, sightseeing.html, day-trips.html"""
    products = []
    # Find all <div class="card">
    card_chunks = re.findall(r'<div class="card"[^>]*>(.*?)</div>\s*</div>', html, re.DOTALL)
    if not card_chunks:
        # alternative card closing pattern
        card_chunks = re.findall(r'<div class="card[^"]*"[^>]*>(.*?)(?=<div class="card|\Z)', html, re.DOTALL)
        
    for chunk in card_chunks:
        # Check for card title in h3
        h3_match = re.search(r'<h3[^>]*>(.*?)</h3>', chunk, re.DOTALL)
        if not h3_match:
            continue
        title = clean_html(h3_match.group(1))
        if not title or 'explore more' in title.lower() or 'trippovention' in title.lower():
            continue
            
        desc_match = re.search(r'<p class="muted[^"]*">(.*?)</p>', chunk, re.DOTALL)
        desc = clean_html(desc_match.group(1)) if desc_match else ''
        
        badge_match = re.search(r'<div class="badge[^"]*">(.*?)</div>', chunk, re.DOTALL)
        badge = clean_html(badge_match.group(1)) if badge_match else ''
        
        price_match = re.search(r'<span class="price[^"]*">(.*?)</span>', chunk, re.DOTALL)
        price = clean_html(price_match.group(1)) if price_match else ''
        
        img_match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', chunk)
        img = ''
        if img_match:
            src = img_match.group(1)
            cur_dir = os.path.dirname(rel_path)
            norm = os.path.normpath(os.path.join(cur_dir, src)).replace('\\', '/')
            if norm.startswith('./'): norm = norm[2:]
            img = norm
            
        # Target link: look for a.btn href
        link_match = re.search(r'<a[^>]+class=["\'][^"\']*btn[^"\']*["\'][^>]+href=["\']([^"\']+)["\']', chunk)
        if link_match:
            link = link_match.group(1)
            if link.startswith('#') or link.startswith('tel:') or link.startswith('mailto:') or 'wa.me' in link:
                url = rel_path
            elif link.startswith('http'):
                url = re.sub(r'^https?://[^/]+/', '', link)
            else:
                cur_dir = os.path.dirname(rel_path)
                url = os.path.normpath(os.path.join(cur_dir, link)).replace('\\', '/')
                if url.startswith('./'): url = url[2:]
        else:
            url = rel_path
            
        # Refine destination from title or badge
        dest = default_dest
        for k, v in DESTINATIONS_META.items():
            if v['name'].lower() in title.lower() or v['name'].lower() in badge.lower():
                dest = v['name']
                break
                
        keywords = build_keywords(title, desc + ' ' + badge, dest, default_cat, url)
        
        products.append({
            'id': re.sub(r'[^a-z0-9]+', '-', f"{default_cat}-{title}".lower()).strip('-'),
            'title': title,
            'url': url,
            'category': default_cat,
            'destination': dest,
            'description': desc,
            'badge': badge,
            'price': price,
            'image': img or 'assets/images/logo.webp',
            'keywords': keywords
        })
        
    return products

def parse_krabi_sightseeing_page(html, rel_path):
    """Specifically parse all 24 activities from packages/thailand/krabi/sightseeing.html"""
    activities = []
    article_chunks = re.findall(r'<article class="card sightseeing-card"[^>]*data-id=["\']([^"\']+)["\'][^>]*data-name=["\']([^"\']+)["\'][^>]*data-category=["\']([^"\']+)["\'][^>]*data-price=["\']([^"\']+)["\'][^>]*>(.*?)</article>', html, re.DOTALL)
    for art_id, name, cat_code, price_raw, body in article_chunks:
        desc_match = re.search(r'<p class="muted">(.*?)</p>', body, re.DOTALL)
        desc = clean_html(desc_match.group(1)) if desc_match else ''
        
        img_match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', body)
        img = ''
        if img_match:
            src = img_match.group(1)
            cur_dir = os.path.dirname(rel_path)
            img = os.path.normpath(os.path.join(cur_dir, src)).replace('\\', '/')
            
        price_match = re.search(r'<span class="price">([^<]+)</span>', body)
        price_text = clean_html(price_match.group(1)) if price_match else (f"THB {price_raw}" if price_raw and price_raw != '0' else 'Current Offer')
        
        badge_match = re.search(r'<span class="badge">([^<]+)</span>', body)
        badge = clean_html(badge_match.group(1)) if badge_match else 'Krabi Sightseeing'
        
        # Link to contact inquiry with tour prefill or direct to page
        url = f"{rel_path}#catalogue"
        
        cat_display = 'Sightseeing'
        if 'romantic' in cat_code:
            cat_display = 'Sightseeing'
        elif 'nature' in cat_code:
            cat_display = 'Sightseeing'
        elif 'adventure' in cat_code:
            cat_display = 'Sightseeing'
            
        kw = build_keywords(name, desc, 'Krabi', cat_display, rel_path)
        activities.append({
            'id': f"krabi-activity-{art_id}",
            'title': name,
            'url': rel_path,
            'category': cat_display,
            'destination': 'Krabi',
            'description': desc,
            'badge': badge,
            'price': price_text,
            'image': img or 'assets/images/packages/thailand/krabi/hero_krabi.webp',
            'keywords': kw
        })
    return activities

def main():
    print(f"Scanning docs directory: {DOCS_DIR}")
    indexed_items = []
    seen_urls = set()
    
    # 1. Walk docs/
    for root, dirs, files in os.walk(DOCS_DIR):
        for f in files:
            if not f.endswith('.html'):
                continue
            if f in EXCLUDE_FILES:
                continue
                
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, DOCS_DIR).replace('\\', '/')
            
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as fp:
                html = fp.read()
                
            title = extract_tag_text(html, 'title')
            # Clean generic branding suffixes
            clean_title = re.sub(r'\s*\|\s*Trippovention.*$', '', title).strip()
            
            h1 = extract_tag_text(html, 'h1')
            desc = extract_meta_content(html, 'description')
            if not desc:
                lead_match = re.search(r'<p class="(?:lead|subtitle|muted)[^"]*">(.*?)</p>', html, re.DOTALL)
                desc = clean_html(lead_match.group(1)) if lead_match else ''
                
            category, destination = detect_category_and_destination(rel_path, clean_title, desc, h1)
            img = extract_image_url(html, rel_path)
            price = extract_price(html)
            
            keywords = build_keywords(clean_title, desc + ' ' + h1, destination, category, rel_path)
            
            item_id = re.sub(r'[^a-z0-9]+', '-', f"{category}-{rel_path}".lower()).strip('-')
            
            # Format display title
            display_title = clean_title if clean_title else h1
            if not display_title:
                display_title = os.path.splitext(f)[0].replace('_', ' ').title()
                
            indexed_items.append({
                'id': item_id,
                'title': display_title,
                'url': rel_path,
                'category': category,
                'destination': destination,
                'description': desc[:220] + ('...' if len(desc) > 220 else ''),
                'badge': category,
                'price': price or '',
                'image': img,
                'keywords': keywords
            })
            seen_urls.add(rel_path)
            
            # Special parsing for aggregate catalogue pages
            if rel_path == 'transfers.html':
                transfer_cards = parse_card_products_from_page(html, rel_path, 'Transfer', 'Thailand')
                for t in transfer_cards:
                    t['id'] = 'transfers-' + t['id']
                    indexed_items.append(t)
            elif rel_path == 'day-trips.html':
                day_trip_cards = parse_card_products_from_page(html, rel_path, 'Day Trip', 'Thailand')
                for d in day_trip_cards:
                    d['id'] = 'daytrips-' + d['id']
                    indexed_items.append(d)
            elif rel_path == 'packages/thailand/krabi/sightseeing.html':
                krabi_acts = parse_krabi_sightseeing_page(html, rel_path)
                indexed_items.extend(krabi_acts)
            elif rel_path == 'sightseeing.html':
                sightseeing_cards = parse_card_products_from_page(html, rel_path, 'Sightseeing', 'Thailand')
                for s in sightseeing_cards:
                    s['id'] = 'sightseeing-' + s['id']
                    indexed_items.append(s)

    # De-duplicate by title + destination + category
    unique_items = []
    seen_keys = set()
    for item in indexed_items:
        key = f"{item['title'].lower()}|{item['url'].lower()}"
        if key not in seen_keys:
            seen_keys.add(key)
            unique_items.append(item)
            
    print(f"Total unique search items indexed: {len(unique_items)}")
    
    # Save search-index.json
    os.makedirs(os.path.dirname(INDEX_JSON_OUTPUT), exist_ok=True)
    with open(INDEX_JSON_OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(unique_items, f, ensure_ascii=False, indent=2)
        
    # Save search-data.js for instant offline / CORS-free local execution
    with open(INDEX_JS_OUTPUT, 'w', encoding='utf-8') as f:
        f.write('/* Auto-generated Trippovention Search Index Data */\n')
        f.write('window.TRIPPOVENTION_SEARCH_DATA = ')
        json.dump(unique_items, f, ensure_ascii=False)
        f.write(';\n')
        
    print(f"Wrote {INDEX_JSON_OUTPUT} ({os.path.getsize(INDEX_JSON_OUTPUT) / 1024:.1f} KB)")
    print(f"Wrote {INDEX_JS_OUTPUT} ({os.path.getsize(INDEX_JS_OUTPUT) / 1024:.1f} KB)")

if __name__ == '__main__':
    main()
