#!/usr/bin/env python3
"""
import_new_itineraries.py

Parses all .docx itineraries from both 'Itineraries' and 'New Itineraries' directories
and creates structured HTML package pages and destination landing index pages under
docs/packages/thailand/<destination>/ across 16 Thailand destinations.
"""

import os
import re
import zipfile
import xml.etree.ElementTree as ET

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
THAILAND_PACKAGES_DIR = os.path.join(DOCS_DIR, "packages", "thailand")

# Map of hero images based on destination key
HERO_IMAGE_MAP = {
    'ayutthaya': 'assets/images/packages/thailand/hero_thailand_culture.webp',
    'bangkok': 'assets/images/packages/thailand/hero_pattaya_bangkok.webp',
    'chiang-mai': 'assets/images/packages/thailand/hero_chiang_mai_chiang_rai.webp',
    'chiang-rai': 'assets/images/packages/thailand/hero_chiang_mai_chiang_rai_bangkok.webp',
    'hua-hin': 'assets/images/packages/thailand/hero_thailand_beach.webp',
    'koh-larn': 'assets/images/packages/thailand/hero_pattaya_bangkok_beach.webp',
    'koh-mook': 'assets/images/packages/thailand/hero_krabi_phuket.webp',
    'koh-phangan': 'assets/images/packages/thailand/hero_thailand_friends_traveler.webp',
    'koh-samet': 'assets/images/packages/thailand/hero_koh_samet_pattaya_bangkok.webp',
    'koh-samui': 'assets/images/packages/thailand/hero_koh_samui_bangkok.webp',
    'koh-yao-yai': 'assets/images/packages/thailand/hero_explore_more_thailand.webp',
    'krabi': 'assets/images/packages/thailand/hero_krabi_phuket.webp',
    'pattaya': 'assets/images/packages/thailand/hero_pattaya_bangkok_beach.webp',
    'phi-phi-island': 'assets/images/packages/thailand/hero_phuket_beach.webp',
    'phuket': 'assets/images/packages/thailand/hero_phuket_beach.webp',
    'trang': 'assets/images/packages/thailand/hero_thailand_wellness.webp'
}

DESTINATION_METADATA = {
    'ayutthaya': {
        'name': 'Ayutthaya',
        'title': 'Ayutthaya Tour Packages | Trippovention',
        'meta_desc': 'Discover ancient Ayutthaya tour packages: UNESCO World Heritage temples, historical ruins & scenic river cruises.',
        'hero_title': 'Explore Ayutthaya Packages',
        'hero_sub': 'UNESCO Ancient Temples, Royal Palaces & Scenic River Cruises in Thailand',
        'image': '../../assets/images/packages/thailand/hero_thailand_culture.webp'
    },
    'bangkok': {
        'name': 'Bangkok',
        'title': 'Bangkok Tour Packages | Trippovention',
        'meta_desc': 'Discover exciting Bangkok tour packages: Grand Palace, Floating Markets, Safari World, Chao Phraya cruises & vibrant city escapes.',
        'hero_title': 'Explore Bangkok Packages',
        'hero_sub': 'Temples, Wildlife, Skyline & Culinary Adventures in Thailand\'s Capital',
        'image': '../../assets/images/packages/thailand/hero_pattaya_bangkok.webp'
    },
    'chiang-mai': {
        'name': 'Chiang Mai',
        'title': 'Chiang Mai Tour Packages | Trippovention',
        'meta_desc': 'Explore Chiang Mai tour packages: Doi Suthep, Elephant Sanctuaries, Night Bazaars & Lanna cultural retreats.',
        'hero_title': 'Explore Chiang Mai Packages',
        'hero_sub': 'Lanna Heritage, Mountain Sanctuaries & Vibrant Northern Thai Culture',
        'image': '../../assets/images/packages/thailand/hero_chiang_mai_chiang_rai.webp'
    },
    'chiang-rai': {
        'name': 'Chiang Rai',
        'title': 'Chiang Rai Tour Packages | Trippovention',
        'meta_desc': 'Book Chiang Rai tour packages: Wat Rong Khun White Temple, Blue Temple, Golden Triangle & tea plantations.',
        'hero_title': 'Explore Chiang Rai Packages',
        'hero_sub': 'The Iconic White Temple, Golden Triangle & Breathtaking Northern Highlands',
        'image': '../../assets/images/packages/thailand/hero_chiang_mai_chiang_rai_bangkok.webp'
    },
    'hua-hin': {
        'name': 'Hua Hin',
        'title': 'Hua Hin Tour Packages | Trippovention',
        'meta_desc': 'Experience Hua Hin tour packages: Royal beach resorts, night markets, Vana Nava water park & seaside serenity.',
        'hero_title': 'Explore Hua Hin Packages',
        'hero_sub': 'Royal Seaside Resort, Pristine Beaches & Relaxing Coastal Charms',
        'image': '../../assets/images/packages/thailand/hero_thailand_beach.webp'
    },
    'koh-larn': {
        'name': 'Koh Larn',
        'title': 'Koh Larn Coral Island Packages | Trippovention',
        'meta_desc': 'Book Koh Larn tour packages: Speedboat island transfers, water sports, white sand beaches & Pattaya day trips.',
        'hero_title': 'Explore Koh Larn Packages',
        'hero_sub': 'Crystal Turquoise Waters, Coral Reefs & White Sand Beach Escapes',
        'image': '../../assets/images/packages/thailand/hero_pattaya_bangkok_beach.webp'
    },
    'koh-mook': {
        'name': 'Koh Mook',
        'title': 'Koh Mook Tour Packages | Trippovention',
        'meta_desc': 'Discover Koh Mook tour packages: The famous Emerald Cave (Tham Morakot), tranquil beaches & Trang archipelago.',
        'hero_title': 'Explore Koh Mook Packages',
        'hero_sub': 'The Enchanting Emerald Cave & Unspoiled Andaman Island Serenity',
        'image': '../../assets/images/packages/thailand/hero_krabi_phuket.webp'
    },
    'koh-phangan': {
        'name': 'Koh Phangan',
        'title': 'Koh Phangan Tour Packages | Trippovention',
        'meta_desc': 'Book Koh Phangan tour packages: Tropical palm beaches, Full Moon festival vibes, waterfalls & island relaxation.',
        'hero_title': 'Explore Koh Phangan Packages',
        'hero_sub': 'Lush Tropical Jungles, Vibrant Beach Festivals & Hidden Bays',
        'image': '../../assets/images/packages/thailand/hero_thailand_friends_traveler.webp'
    },
    'koh-samet': {
        'name': 'Koh Samet',
        'title': 'Koh Samet Tour Packages | Trippovention',
        'meta_desc': 'Explore Koh Samet tour packages: Sai Kaew Beach, fire shows, turquoise waters & quick weekend island getaways.',
        'hero_title': 'Explore Koh Samet Packages',
        'hero_sub': 'Powdery Sand Beaches, Island Fire Shows & Sun-Kissed Relaxation',
        'image': '../../assets/images/packages/thailand/hero_koh_samet_pattaya_bangkok.webp'
    },
    'koh-samui': {
        'name': 'Koh Samui',
        'title': 'Koh Samui Tour Packages | Trippovention',
        'meta_desc': 'Discover Koh Samui tour packages: Chaweng Beach, Big Buddha, Ang Thong National Marine Park & luxury island resorts.',
        'hero_title': 'Explore Koh Samui Packages',
        'hero_sub': 'Tropical Gulf Islands, Angthong Marine Park & Luxury Beach Resorts',
        'image': '../../assets/images/packages/thailand/hero_koh_samui_bangkok.webp'
    },
    'koh-yao-yai': {
        'name': 'Koh Yao Yai',
        'title': 'Koh Yao Yai Tour Packages | Trippovention',
        'meta_desc': 'Book Koh Yao Yai tour packages: Tranquil island sanctuaries, Phang Nga Bay views & eco-luxury beach retreats.',
        'hero_title': 'Explore Koh Yao Yai Packages',
        'hero_sub': 'Peaceful Island Hideaways, Lime Rock Views & Untouched Nature',
        'image': '../../assets/images/packages/thailand/hero_explore_more_thailand.webp'
    },
    'krabi': {
        'name': 'Krabi',
        'title': 'Krabi Tour Packages | Trippovention',
        'meta_desc': 'Explore idyllic Krabi tour packages: 4 Island tours, Railay Beach, Emerald Pool, natural hot springs & tropical coastal escapes.',
        'hero_title': 'Explore Krabi Packages',
        'hero_sub': 'Limestone Cliffs, Emerald Lagoons & Pristine Tropical Island Escapes',
        'image': '../../assets/images/packages/thailand/hero_krabi_phuket.webp'
    },
    'pattaya': {
        'name': 'Pattaya',
        'title': 'Pattaya Tour Packages | Trippovention',
        'meta_desc': 'Book top Pattaya tour packages: Coral Island, Sanctuary of Truth, Nong Nooch Gardens & cabaret shows with private transfers.',
        'hero_title': 'Explore Pattaya Packages',
        'hero_sub': 'Sun-Kissed Beaches, Island Cruises, Theme Parks & Vibrant Entertainment',
        'image': '../../assets/images/packages/thailand/hero_pattaya_bangkok_beach.webp'
    },
    'phi-phi-island': {
        'name': 'Phi Phi Island',
        'title': 'Phi Phi Island Tour Packages | Trippovention',
        'meta_desc': 'Discover Phi Phi Island tour packages: Maya Bay, Pileh Lagoon, Monkey Beach, snorkeling cruises & paradise island stays.',
        'hero_title': 'Explore Phi Phi Island Packages',
        'hero_sub': 'Maya Bay, Emerald Lagoons & World-Famous Andaman Island Paradise',
        'image': '../../assets/images/packages/thailand/hero_phuket_beach.webp'
    },
    'phuket': {
        'name': 'Phuket',
        'title': 'Phuket Tour Packages | Trippovention',
        'meta_desc': 'Experience Phuket tour packages: Phi Phi Island, Phang Nga Bay, James Bond Island, Old Town & luxurious beach resorts.',
        'hero_title': 'Explore Phuket Packages',
        'hero_sub': 'Pearl of the Andaman: World-Class Beaches, Island Cruises & Tropical Luxury',
        'image': '../../assets/images/packages/thailand/hero_phuket_beach.webp'
    },
    'trang': {
        'name': 'Trang',
        'title': 'Trang Tour Packages | Trippovention',
        'meta_desc': 'Explore Trang tour packages: Hidden island paradises, Koh Kradan, Koh Chaki & authentic southern Thai coastal nature.',
        'hero_title': 'Explore Trang Packages',
        'hero_sub': 'Unspoiled Southern Thai Islands, Coral Reefs & Coastal Wonders',
        'image': '../../assets/images/packages/thailand/hero_thailand_wellness.webp'
    }
}

def get_docx_paragraphs(path):
    with zipfile.ZipFile(path) as z:
        xml_content = z.read('word/document.xml')
    root = ET.fromstring(xml_content)
    paras = []
    for p in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        texts = [t.text for t in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
        if texts:
            paras.append(''.join(texts).strip())
    return paras

def parse_itinerary_docx(path):
    paras = get_docx_paragraphs(path)
    data = {
        'title': paras[0] if len(paras) > 0 else '',
        'subtitle': paras[1] if len(paras) > 1 else '',
        'duration': '',
        'price': 'On Request',
        'ideal_for': 'Families | Couples | Friends',
        'days': [],
        'inclusions': [],
        'exclusions': []
    }
    
    idx = 2
    while idx < len(paras):
        p = paras[idx]
        if 'Duration' in p and idx + 1 < len(paras):
            data['duration'] = paras[idx + 1]
            idx += 2
        elif 'Price Per Person' in p and idx + 1 < len(paras):
            data['price'] = paras[idx + 1]
            idx += 2
        elif 'Ideal For' in p and idx + 1 < len(paras):
            data['ideal_for'] = paras[idx + 1]
            idx += 2
        elif p == 'Detailed Itinerary':
            idx += 1
            break
        else:
            idx += 1
            
    current_day = None
    state = 'DAYS'
    
    while idx < len(paras):
        p = paras[idx]
        if p == 'Package Details':
            if current_day:
                data['days'].append(current_day)
                current_day = None
            state = 'DETAILS'
            idx += 1
            continue
            
        if state == 'DAYS':
            m_exact = re.match(r'^(Day\s+\d+)$', p, re.IGNORECASE)
            m_combined = re.match(r'^(Day\s+\d+)\s*[–:-]\s*(.*)$', p, re.IGNORECASE)
            
            if m_combined:
                if current_day:
                    data['days'].append(current_day)
                current_day = {
                    'day_num': m_combined.group(1).title(),
                    'day_title': m_combined.group(2).strip(),
                    'bullets': [],
                    'meals': '',
                    'tickets': ''
                }
            elif m_exact:
                if current_day:
                    data['days'].append(current_day)
                next_title = ''
                if idx + 1 < len(paras) and not paras[idx+1].startswith('Day ') and paras[idx+1] != 'Package Details':
                    next_title = paras[idx+1]
                    idx += 1
                current_day = {
                    'day_num': m_exact.group(1).title(),
                    'day_title': next_title.strip(),
                    'bullets': [],
                    'meals': '',
                    'tickets': ''
                }
            elif current_day:
                if 'Meals:' in p:
                    meals_part = p
                    if 'Tickets:' in meals_part:
                        parts = meals_part.split('Tickets:')
                        current_day['meals'] = parts[0].replace('Meals:', '').strip()
                        current_day['tickets'] = parts[1].strip()
                    else:
                        current_day['meals'] = meals_part.replace('Meals:', '').strip()
                elif 'Tickets:' in p:
                    current_day['tickets'] = p.replace('Tickets:', '').strip()
                else:
                    current_day['bullets'].append(p)
                    
        elif state == 'DETAILS':
            if 'What\'s Included' in p or 'Whats Included' in p:
                state = 'INCLUSIONS'
            elif 'What\'s Not Included' in p or 'Whats Not Included' in p:
                state = 'EXCLUSIONS'
        elif state == 'INCLUSIONS':
            if 'What\'s Not Included' in p or 'Whats Not Included' in p:
                state = 'EXCLUSIONS'
            else:
                data['inclusions'].append(p.lstrip('•- ').strip())
        elif state == 'EXCLUSIONS':
            data['exclusions'].append(p.lstrip('•- ').strip())
            
        idx += 1
        
    if current_day:
        data['days'].append(current_day)
        
    return data

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')

def build_package_html(dest_key, slug, data):
    dest_meta = DESTINATION_METADATA.get(dest_key, {
        'name': dest_key.replace('-', ' ').title(),
        'image': 'assets/images/packages/thailand/hero_explore_more_thailand.webp'
    })
    dest_name = dest_meta['name']
    title = f"{data['title']} - {data['duration']} | Trippovention"
    meta_desc = f"{data['title']}: {data['duration']} - {data['subtitle']}"
    canonical_url = f"https://trippovention.co.th/packages/thailand/{dest_key}/{slug}.html"
    
    # Days HTML cards
    days_html_list = []
    for day in data['days']:
        bullets_li = "\n".join([f"                <li>{b}</li>" for b in day['bullets']])
        tags_html = ""
        if day['meals']:
            tags_html += f'\n                <div class="tag">Meals: {day["meals"]}</div>'
        if day['tickets']:
            tags_html += f'\n                <div class="tag">Tickets: {day["tickets"]}</div>'
            
        tags_container = f'\n              <div class="tags-container">{tags_html}\n              </div>' if tags_html else ""
        
        day_card = f"""          <div class="card">
            <div class="body">
              <div class="badge">{day['day_num']}</div>
              <h3>{day['day_title']}</h3>
              <ul class="muted">
{bullets_li}
              </ul>{tags_container}
            </div>
          </div>"""
        days_html_list.append(day_card)
        
    days_html = "\n\n".join(days_html_list)
    
    # Inclusions & Exclusions
    inc_li = "\n".join([f"                <li>{inc}</li>" for inc in data['inclusions']])
    exc_li = "\n".join([f"                <li>{exc}</li>" for exc in data['exclusions']])
    
    hero_img = HERO_IMAGE_MAP.get(dest_key, 'assets/images/packages/thailand/hero_explore_more_thailand.webp')
    
    html = f"""<!doctype html>
<html lang="en">
  <head>
    <!-- Google Tag Manager -->
    <script>
      (function (w, d, s, l, i) {{
        w[l] = w[l] || [];
        w[l].push({{ "gtm.start": new Date().getTime(), event: "gtm.js" }});
        var f = d.getElementsByTagName(s)[0],
          j = d.createElement(s),
          dl = l != "dataLayer" ? "&l=" + l : "";
        j.async = true;
        j.src = "https://www.googletagmanager.com/gtm.js?id=" + i + dl;
        f.parentNode.insertBefore(j, f);
      }})(window, document, "script", "dataLayer", "GTM-NLPKQZJS");
    </script>
    <!-- End Google Tag Manager -->

    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <title>{title}</title>
    <meta name="description" content="{meta_desc}" />
    <meta name="author" content="Trippovention" />

    <meta property="og:type" content="website" />
    <meta property="og:url" content="{canonical_url}" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{meta_desc}" />
    <meta property="og:image" content="https://trippovention.co.th/{hero_img}" />

    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="{canonical_url}" />
    <meta property="twitter:title" content="{title}" />
    <meta property="twitter:description" content="{meta_desc}" />
    <meta property="twitter:image" content="https://trippovention.co.th/{hero_img}" />

    <link rel="canonical" href="{canonical_url}" />
    <link rel="icon" type="image/x-icon" href="../../../assets/images/favicon.ico" />
    <link rel="apple-touch-icon" sizes="180x180" href="../../../assets/images/favicon.png" />
    <link rel="manifest" href="../../../site.webmanifest" />
    <meta name="theme-color" content="#667eea" />
    <meta name="referrer" content="strict-origin-when-cross-origin" />

    <link rel="stylesheet" href="../../../assets/styles.css" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link rel="dns-prefetch" href="https://fonts.googleapis.com" />
    <link rel="dns-prefetch" href="https://fonts.gstatic.com" />
    <link rel="dns-prefetch" href="https://www.googletagmanager.com" />
    <link rel="preload" href="../../../assets/styles.css" as="style" />
    <link rel="preload" href="../../../assets/app.js" as="script" />
    <link rel="preload" href="../../../assets/images/logo.webp" as="image" type="image/webp" />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Inter:wght@400;500;600&display=swap"
      rel="stylesheet"
    />

    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-11395302765"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {{
        dataLayer.push(arguments);
      }}
      gtag("js", new Date());
      gtag("config", "AW-11395302765");
    </script>
  </head>

  <body>
    <a href="#main" class="skip-link" aria-label="Skip to main content" id="skip-link">
      Skip to main content
    </a>

    <nav class="nav" role="navigation" aria-label="Main navigation">
      <div class="container">
        <a class="brand" href="../../../index.html" aria-label="Go to Trippovention Home">
          <img
            src="../../../assets/images/logo.webp"
            alt="Trippovention"
            width="160"
            height="40"
            loading="lazy"
          />
        </a>
        <div class="menu" id="mobileMenu">
          <a href="../../../index.html">Home</a>
          <div class="has-dropdown">
            <a
              class="active"
              href="../../../destinations.html"
              aria-haspopup="true"
              aria-expanded="false"
            >
              Destinations <span class="dropdown-arrow">▼</span>
            </a>
            <div class="dropdown-menu" aria-label="Browse destinations">
              <a href="../../../destinations.html">By Country</a>
              <a href="../../../destinations-themes.html">By Theme</a>
              <a href="../../../destinations-travelers.html">By Traveler</a>
            </div>
          </div>
          <a href="../../../services.html">Services</a>
          <a href="../../../contact.html">Contact</a>
        </div>
        <div class="nav-right">
          <div class="actions">
            <button class="lang-btn notranslate" id="langToggle" translate="no">TH</button>
            <a class="icon" title="Call Us" href="tel:+66909177601">📞</a>
            <a
              class="icon"
              title="WhatsApp"
              href="https://wa.me/+66909177601"
              aria-label="Chat on WhatsApp"
              rel="noopener noreferrer"
              target="_blank"
            >
              <img
                src="../../../assets/images/social/whatsapp.svg"
                alt="WhatsApp"
                class="whatsapp-icon-nav whatsapp-green"
                loading="lazy"
              />
            </a>
            <button
              class="icon"
              title="Toggle Dark Mode"
              id="themeToggle"
              aria-label="Toggle dark mode"
            >
              🌙
            </button>
          </div>
          <button
            class="hamburger"
            id="hamburger"
            aria-label="Toggle navigation menu"
            aria-expanded="false"
          >
            <span></span><span></span><span></span>
          </button>
        </div>
      </div>
    </nav>

    <main id="main" tabindex="-1">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <div class="breadcrumb-container">
          <ol class="breadcrumb-list">
            <li class="breadcrumb-item">
              <a href="../../../index.html">🏠 Home</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item">
              <a href="../../../destinations.html">Destinations</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item">
              <a href="../index.html">Thailand</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item">
              <a href="index.html">{dest_name}</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item active" aria-current="page">
              {data['title']}
            </li>
          </ol>
        </div>
      </nav>

      <header class="hero compact hero-thailand">
        <div class="container">
          <h1>{data['title']}</h1>
          <p>{data['subtitle']}</p>
        </div>
      </header>

      <section class="section">
        <div class="container">
          <div class="grid cols-3">
            <div class="card info-card">
              <div class="body">
                <div class="info-icon">🗓️</div>
                <h2>Duration</h2>
                <p>{data['duration']}</p>
              </div>
            </div>
            <div class="card info-card card-premium">
              <div class="body">
                <div class="info-icon">💰</div>
                <h3>Price Per Person</h3>
                <div class="price-row">
                  <span class="price">{data['price']}</span>
                </div>
              </div>
            </div>
            <div class="card info-card">
              <div class="body">
                <div class="info-icon">👨‍👩‍👧‍👦</div>
                <h2>Ideal For</h2>
                <p>{data['ideal_for']}</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section alt">
        <div class="container">
          <div class="section-title">
            <h2>Detailed Itinerary</h2>
          </div>

          <div class="two">
{days_html}
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div class="section-title">
            <h2>Package Details</h2>
            <p class="subtitle">Everything you need to know about what's included</p>
          </div>

          <div class="two">
            <div class="card card-premium">
              <div class="body">
                <h3>✅ What's Included</h3>
                <ul style="line-height: 1.8">
{inc_li}
                </ul>
              </div>
            </div>

            <div class="card">
              <div class="body">
                <h3>❌ What's Not Included</h3>
                <ul class="muted" style="line-height: 1.8">
{exc_li}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section cta">
        <div class="container">
          <div class="section-title">
            <h2 class="text-white">Ready for {data['title']}?</h2>
            <p class="subtitle text-white-90">
              Book now and get instant confirmation with our best price guarantee
            </p>
          </div>
          <div class="text-center">
            <a
              class="btn btn-lg ghost"
              href="../../../contact.html?package=thailand-{dest_key}-{slug}"
              >📞 Get Custom Quote</a
            >
            <a
              class="btn btn-lg ghost ml-16"
              href="https://wa.me/+66909177601"
              target="_blank"
              rel="noopener noreferrer"
              >💬 WhatsApp Us</a
            >
          </div>
          <div class="grid cols-3 mt-40">
            <div class="stats">
              <span class="number text-white">2021</span>
              <span class="label text-white-90">Established</span>
            </div>
            <div class="stats">
              <span class="number text-white">10+</span>
              <span class="label text-white-90">Years Experience</span>
            </div>
            <div class="stats">
              <span class="number text-white">50K+</span>
              <span class="label text-white-90">Happy Travelers</span>
            </div>
          </div>
        </div>
      </section>
    </main>

    <footer class="footer" role="contentinfo">
      <div class="container">
        <div class="grid cols-3">
          <div>
            <h3>Trippovention</h3>
            <p>
              Your trusted travel partner for unforgettable journeys. We believe that travel should
              be transformative and memorable.
            </p>
            <div class="mt-20">
              <h3 class="muted font-weight-600">Contact Details</h3>
              <span class="mr-15"
                >📧 <a href="mailto:query@trippovention.co.th">query@trippovention.co.th</a></span
              >
              <br />
              <span>📞 <a href="tel:+66909177601">+66 90 917 7601</a></span>
              <br />
              <span>💬
                <a href="https://wa.me/+66909177601" target="_blank" rel="noopener noreferrer"
                  >WhatsApp</a
                ></span
              >
              <br />
              <p class="muted" style="margin-top: 8px; font-size: 13px">
                India office:
                <a href="tel:+911244182575">+91 124 418 2575</a> /
                <a href="tel:+917303010446">+91 73030 10446</a>
              </p>
            </div>
          </div>
          <div>
            <h3>Quick Links</h3>
            <ul>
              <li><a href="../../../index.html">Home</a></li>
              <li><a href="../../../destinations.html">Destinations</a></li>
              <li><a href="../../../services.html">Services</a></li>
              <li><a href="../../../contact.html">Contact Us</a></li>
              <li><a href="../../../privacy-policy.html">Privacy Policy</a></li>
              <li><a href="../../../terms-and-conditions.html">Terms &amp; Conditions</a></li>
            </ul>
          </div>
          <div>
            <h3>Thailand Office</h3>
            <p>
              23/13 M, 12 Nong Pure Subdistrict, Bang Lamung District, Chonburi Province-20150
            </p>
            <div class="mt-20">
              <h3>India Office</h3>
              <p>
                Unit No. - 337 A, 3rd Floor, Spaze IT Park, Tower A, Sector 49, Sohna Road,
                Gurgaon, Haryana, India, 122018.
              </p>
            </div>
          </div>
        </div>
        <div class="footer-bottom mt-40">
          <p>© 2026 Trippovention. All rights reserved.</p>
        </div>
      </div>
    </footer>
    <script src="../../../assets/app.js" defer></script>
  </body>
</html>"""
    return html

def build_destination_index_html(dest_key, packages):
    meta = DESTINATION_METADATA.get(dest_key, {
        'name': dest_key.replace('-', ' ').title(),
        'title': f"{dest_key.replace('-', ' ').title()} Tour Packages | Trippovention",
        'meta_desc': f"Discover top {dest_key.replace('-', ' ').title()} tour packages with Trippovention.",
        'hero_title': f"Explore {dest_key.replace('-', ' ').title()} Packages",
        'hero_sub': f"Handcrafted itineraries & tropical escapes in {dest_key.replace('-', ' ').title()}"
    })
    dest_name = meta['name']
    title = meta['title']
    meta_desc = meta['meta_desc']
    canonical_url = f"https://trippovention.co.th/packages/thailand/{dest_key}/"
    hero_img = HERO_IMAGE_MAP.get(dest_key, 'assets/images/packages/thailand/hero_explore_more_thailand.webp')
    
    cards_html_list = []
    for pkg in packages:
        card = f"""            <div class="card">
              <div class="img-wrap">
                <img
                  src="../../../{hero_img}"
                  alt="{pkg['title']}"
                  loading="lazy"
                />
                <span class="ribbon hot">🔥 Popular</span>
              </div>
              <div class="body">
                <div class="badge">🗓️ {pkg['duration']}</div>
                <h3>{pkg['title']}</h3>
                <p class="muted">{pkg['subtitle']}</p>
                <div class="price-row">
                  <span class="price-label">Starting from</span>
                  <span class="price">On Request</span>
                </div>
                <a class="btn" href="{pkg['slug']}.html">View Details →</a>
              </div>
            </div>"""
        cards_html_list.append(card)
        
    cards_html = "\n".join(cards_html_list)
    
    html = f"""<!doctype html>
<html lang="en">
  <head>
    <!-- Google Tag Manager -->
    <script>
      (function (w, d, s, l, i) {{
        w[l] = w[l] || [];
        w[l].push({{ "gtm.start": new Date().getTime(), event: "gtm.js" }});
        var f = d.getElementsByTagName(s)[0],
          j = d.createElement(s),
          dl = l != "dataLayer" ? "&l=" + l : "";
        j.async = true;
        j.src = "https://www.googletagmanager.com/gtm.js?id=" + i + dl;
        f.parentNode.insertBefore(j, f);
      }})(window, document, "script", "dataLayer", "GTM-NLPKQZJS");
    </script>
    <!-- End Google Tag Manager -->

    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <title>{title}</title>
    <meta name="description" content="{meta_desc}" />
    <meta name="author" content="Trippovention" />

    <meta property="og:type" content="website" />
    <meta property="og:url" content="{canonical_url}" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{meta_desc}" />
    <meta property="og:image" content="https://trippovention.co.th/{hero_img}" />

    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="{canonical_url}" />
    <meta property="twitter:title" content="{title}" />
    <meta property="twitter:description" content="{meta_desc}" />
    <meta property="twitter:image" content="https://trippovention.co.th/{hero_img}" />

    <link rel="canonical" href="{canonical_url}" />
    <link rel="icon" type="image/x-icon" href="../../../assets/images/favicon.ico" />
    <link rel="apple-touch-icon" sizes="180x180" href="../../../assets/images/favicon.png" />
    <link rel="manifest" href="../../../site.webmanifest" />
    <meta name="theme-color" content="#667eea" />
    <meta name="referrer" content="strict-origin-when-cross-origin" />

    <link rel="stylesheet" href="../../../assets/styles.css" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link rel="dns-prefetch" href="https://fonts.googleapis.com" />
    <link rel="dns-prefetch" href="https://fonts.gstatic.com" />
    <link rel="dns-prefetch" href="https://www.googletagmanager.com" />
    <link rel="preload" href="../../../assets/styles.css" as="style" />
    <link rel="preload" href="../../../assets/app.js" as="script" />
    <link rel="preload" href="../../../assets/images/logo.webp" as="image" type="image/webp" />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Inter:wght@400;500;600&display=swap"
      rel="stylesheet"
    />

    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-11395302765"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {{
        dataLayer.push(arguments);
      }}
      gtag("js", new Date());
      gtag("config", "AW-11395302765");
    </script>
  </head>

  <body>
    <a href="#main" class="skip-link" aria-label="Skip to main content" id="skip-link">
      Skip to main content
    </a>

    <nav class="nav" role="navigation" aria-label="Main navigation">
      <div class="container">
        <a class="brand" href="../../../index.html" aria-label="Go to Trippovention Home">
          <img
            src="../../../assets/images/logo.webp"
            alt="Trippovention"
            width="160"
            height="40"
            loading="lazy"
          />
        </a>
        <div class="menu" id="mobileMenu">
          <a href="../../../index.html">Home</a>
          <div class="has-dropdown">
            <a
              class="active"
              href="../../../destinations.html"
              aria-haspopup="true"
              aria-expanded="false"
            >
              Destinations <span class="dropdown-arrow">▼</span>
            </a>
            <div class="dropdown-menu" aria-label="Browse destinations">
              <a href="../../../destinations.html">By Country</a>
              <a href="../../../destinations-themes.html">By Theme</a>
              <a href="../../../destinations-travelers.html">By Traveler</a>
            </div>
          </div>
          <a href="../../../services.html">Services</a>
          <a href="../../../contact.html">Contact</a>
        </div>
        <div class="nav-right">
          <div class="actions">
            <button class="lang-btn notranslate" id="langToggle" translate="no">TH</button>
            <a class="icon" title="Call Us" href="tel:+66909177601">📞</a>
            <a
              class="icon"
              title="WhatsApp"
              href="https://wa.me/+66909177601"
              aria-label="Chat on WhatsApp"
              rel="noopener noreferrer"
              target="_blank"
            >
              <img
                src="../../../assets/images/social/whatsapp.svg"
                alt="WhatsApp"
                class="whatsapp-icon-nav whatsapp-green"
                loading="lazy"
              />
            </a>
            <button
              class="icon"
              title="Toggle Dark Mode"
              id="themeToggle"
              aria-label="Toggle dark mode"
            >
              🌙
            </button>
          </div>
          <button
            class="hamburger"
            id="hamburger"
            aria-label="Toggle navigation menu"
            aria-expanded="false"
          >
            <span></span><span></span><span></span>
          </button>
        </div>
      </div>
    </nav>

    <main id="main" tabindex="-1">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <div class="breadcrumb-container">
          <ol class="breadcrumb-list">
            <li class="breadcrumb-item">
              <a href="../../../index.html">🏠 Home</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item">
              <a href="../../../destinations.html">Destinations</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item">
              <a href="../index.html">Thailand</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item active" aria-current="page">
              {dest_name}
            </li>
          </ol>
        </div>
      </nav>

      <header class="hero compact hero-thailand">
        <div class="container">
          <h1>{meta['hero_title']}</h1>
          <p>{meta['hero_sub']}</p>
        </div>
      </header>

      <section class="section">
        <div class="container">
          <div class="section-title">
            <h2>{dest_name} Tour Packages</h2>
            <p class="subtitle">Handcrafted itineraries for an unforgettable vacation</p>
          </div>
          <div class="grid cols-3">
{cards_html}
          </div>
        </div>
      </section>

      <section class="section cta">
        <div class="container">
          <div class="section-title">
            <h2 class="text-white">Plan Your Trip to {dest_name}</h2>
            <p class="subtitle text-white-90">
              Get in touch with our Thailand travel experts for customized holiday packages
            </p>
          </div>
          <div class="text-center">
            <a
              class="btn btn-lg ghost"
              href="../../../contact.html?destination={dest_key}"
              >📞 Request Custom Itinerary</a
            >
            <a
              class="btn btn-lg ghost ml-16"
              href="https://wa.me/+66909177601"
              target="_blank"
              rel="noopener noreferrer"
              >💬 WhatsApp Us</a
            >
          </div>
        </div>
      </section>
    </main>

    <footer class="footer" role="contentinfo">
      <div class="container">
        <div class="grid cols-3">
          <div>
            <h3>Trippovention</h3>
            <p>
              Your trusted travel partner for unforgettable journeys. We believe that travel should
              be transformative and memorable.
            </p>
            <div class="mt-20">
              <h3 class="muted font-weight-600">Contact Details</h3>
              <span class="mr-15"
                >📧 <a href="mailto:query@trippovention.co.th">query@trippovention.co.th</a></span
              >
              <br />
              <span>📞 <a href="tel:+66909177601">+66 90 917 7601</a></span>
              <br />
              <span>💬
                <a href="https://wa.me/+66909177601" target="_blank" rel="noopener noreferrer"
                  >WhatsApp</a
                ></span
              >
              <br />
              <p class="muted" style="margin-top: 8px; font-size: 13px">
                India office:
                <a href="tel:+911244182575">+91 124 418 2575</a> /
                <a href="tel:+917303010446">+91 73030 10446</a>
              </p>
            </div>
          </div>
          <div>
            <h3>Quick Links</h3>
            <ul>
              <li><a href="../../../index.html">Home</a></li>
              <li><a href="../../../destinations.html">Destinations</a></li>
              <li><a href="../../../services.html">Services</a></li>
              <li><a href="../../../contact.html">Contact Us</a></li>
              <li><a href="../../../privacy-policy.html">Privacy Policy</a></li>
              <li><a href="../../../terms-and-conditions.html">Terms &amp; Conditions</a></li>
            </ul>
          </div>
          <div>
            <h3>Thailand Office</h3>
            <p>
              23/13 M, 12 Nong Pure Subdistrict, Bang Lamung District, Chonburi Province-20150
            </p>
            <div class="mt-20">
              <h3>India Office</h3>
              <p>
                Unit No. - 337 A, 3rd Floor, Spaze IT Park, Tower A, Sector 49, Sohna Road,
                Gurgaon, Haryana, India, 122018.
              </p>
            </div>
          </div>
        </div>
        <div class="footer-bottom mt-40">
          <p>© 2026 Trippovention. All rights reserved.</p>
        </div>
      </div>
    </footer>
    <script src="../../../assets/app.js" defer></script>
  </body>
</html>"""
    return html

def main():
    print("Starting import of all Thailand Itineraries...")
    
    # Collect all source folders from both 'Itineraries' and 'New Itineraries'
    source_roots = [
        os.path.join(PARENT_DIR, "Itineraries"),
        os.path.join(PARENT_DIR, "New Itineraries")
    ]
    
    dest_file_map = {}
    
    for sroot in source_roots:
        if not os.path.exists(sroot):
            continue
        for sub in os.listdir(sroot):
            sub_path = os.path.join(sroot, sub)
            if os.path.isdir(sub_path):
                dest_key = slugify(sub)
                if dest_key not in dest_file_map:
                    dest_file_map[dest_key] = []
                for f in os.listdir(sub_path):
                    if f.endswith('.docx') and not f.startswith('~$'):
                        fp = os.path.join(sub_path, f)
                        if fp not in dest_file_map[dest_key]:
                            dest_file_map[dest_key].append(fp)

    all_dest_packages = {}
    
    for dest_key in sorted(dest_file_map.keys()):
        all_dest_packages[dest_key] = []
        target_dir = os.path.join(THAILAND_PACKAGES_DIR, dest_key)
        os.makedirs(target_dir, exist_ok=True)
        
        file_paths = sorted(dest_file_map[dest_key])
        seen_slugs = set()
        
        for fp in file_paths:
            data = parse_itinerary_docx(fp)
            raw_name = os.path.splitext(os.path.basename(fp))[0]
            slug = slugify(raw_name)
            
            if slug in seen_slugs:
                continue
            seen_slugs.add(slug)
            
            pkg_info = {
                'title': data['title'],
                'subtitle': data['subtitle'],
                'duration': data['duration'],
                'price': data['price'],
                'slug': slug
            }
            all_dest_packages[dest_key].append(pkg_info)
            
            # Write individual package HTML page
            pkg_html = build_package_html(dest_key, slug, data)
            out_path = os.path.join(target_dir, f"{slug}.html")
            with open(out_path, 'w', encoding='utf-8') as out_f:
                out_f.write(pkg_html)
            print(f"Created: {out_path}")
            
        # Write destination index HTML page
        dest_index_html = build_destination_index_html(dest_key, all_dest_packages[dest_key])
        dest_index_path = os.path.join(target_dir, "index.html")
        with open(dest_index_path, 'w', encoding='utf-8') as out_f:
            out_f.write(dest_index_html)
        print(f"Created destination index: {dest_index_path}")
        
    print(f"Import completed successfully for {len(all_dest_packages)} destinations!")

if __name__ == "__main__":
    main()
