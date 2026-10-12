#!/usr/bin/env python3
import os
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIR = os.path.join(ROOT, "docs", "packages", "thailand", "krabi")

with open(os.path.join(ROOT, "scripts", "generate_krabi_sightseeing_pages.py"), "r", encoding="utf-8") as f:
    text = f.read()

# Extract TOURS_DATA
start_marker = "TOURS_DATA = ["
end_marker = "]\n\nHTML_TEMPLATE"
s_idx = text.find(start_marker)
e_idx = text.find(end_marker)
tours_data_str = text[s_idx + len("TOURS_DATA = "):e_idx + 1]

# Safely evaluate TOURS_DATA
import ast
TOURS_DATA = ast.literal_eval(tours_data_str)
print(f"Extracted {len(TOURS_DATA)} tour configurations.")

# Read hong_islands_tour.html as base template
template_path = os.path.join(DEST_DIR, "hong_islands_tour.html")
with open(template_path, "r", encoding="utf-8") as f:
    base_template = f.read()

for tour in TOURS_DATA:
    fn = tour["filename"]
    title = tour["title"]
    h1 = tour["h1"]
    subtitle = tour["subtitle"]
    meta_desc = tour["meta_desc"]
    og_image = tour["og_image"]
    duration = tour["duration"]
    price = tour["price"]
    price_note = tour["price_note"]
    meetup = tour["meetup"]
    overview_p1 = tour["overview_p1"]
    overview_p2 = tour["overview_p2"]
    timing_text = tour["timing_text"]
    transport_text = tour["transport_text"]
    what_to_bring = tour["what_to_bring"]
    contact_param = tour["contact_tour_param"]

    p1_items_html = "\n".join(f"                  <li><strong>{t}:</strong> {d}</li>" for t, d in tour["places_col1_items"])
    p2_items_html = "\n".join(f"                  <li><strong>{t}:</strong> {d}</li>" for t, d in tour["places_col2_items"])
    inc_html = "\n".join(f"                  <li>{item}</li>" for item in tour["inclusions"])
    exc_html = "\n".join(f"                  <li>{item}</li>" for item in tour["exclusions"])

    doc = base_template

    # Replace title
    import re
    doc = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", doc)
    
    # Replace meta description
    doc = re.sub(r'<meta\s+name="description"\s+content=".*?"\s*/>', f'<meta name="description" content="{meta_desc}" />', doc)
    
    # Replace OG tags
    doc = re.sub(r'<meta property="og:url" content=".*?" />', f'<meta property="og:url" content="https://trippovention.co.th/packages/thailand/krabi/{fn}" />', doc)
    doc = re.sub(r'<meta property="og:title" content=".*?" />', f'<meta property="og:title" content="{title}" />', doc)
    doc = re.sub(r'<meta property="og:description" content=".*?" />', f'<meta property="og:description" content="{meta_desc}" />', doc)
    doc = re.sub(r'<meta property="og:image" content=".*?" />', f'<meta property="og:image" content="{og_image}" />', doc)
    
    # Replace Twitter tags
    doc = re.sub(r'<meta property="twitter:url" content=".*?" />', f'<meta property="twitter:url" content="https://trippovention.co.th/packages/thailand/krabi/{fn}" />', doc)
    doc = re.sub(r'<meta property="twitter:title" content=".*?" />', f'<meta property="twitter:title" content="{title}" />', doc)
    doc = re.sub(r'<meta property="twitter:description" content=".*?" />', f'<meta property="twitter:description" content="{meta_desc}" />', doc)
    doc = re.sub(r'<meta property="twitter:image" content=".*?" />', f'<meta property="twitter:image" content="{og_image}" />', doc)
    
    # Replace Canonical
    doc = re.sub(r'<link rel="canonical" href=".*?" />', f'<link rel="canonical" href="https://trippovention.co.th/packages/thailand/krabi/{fn}" />', doc)
    
    # Replace JSON-LD TouristTrip
    schema_tourist_trip = f'''  <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "TouristTrip",
        "name": "{h1}",
        "description": "{meta_desc}",
        "touristType": ["Travelers", "Families", "Couples", "Adventure"],
        "offers": {{
          "@type": "Offer",
          "price": "{price}",
          "priceCurrency": "THB",
          "availability": "https://schema.org/InStock",
          "url": "https://trippovention.co.th/packages/thailand/krabi/{fn}"
        }},
        "provider": {{
          "@type": "TravelAgency",
          "name": "Trippovention",
          "url": "https://trippovention.co.th"
        }}
      }}
    </script>'''
    doc = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context":\s*"https://schema.org",\s*"@type":\s*"TouristTrip".*?</script>', schema_tourist_trip, doc, flags=re.DOTALL)

    # Replace breadcrumbs: add Sightseeing step if not present, and update active item
    new_breadcrumb = f'''      <nav class="breadcrumb" aria-label="Breadcrumb">
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
              <a href="index.html">Krabi</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item">
              <a href="sightseeing.html">Sightseeing</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item active" aria-current="page">
              {h1}
            </li>
          </ol>
        </div>
      </nav>'''
    doc = re.sub(r'<nav class="breadcrumb".*?</nav>', new_breadcrumb, doc, flags=re.DOTALL)

    # Hero section
    new_hero = f'''      <header class="hero compact hero-thailand">
        <div class="container">
          <h1>{h1}</h1>
          <p>{subtitle}</p>
        </div>
      </header>'''
    doc = re.sub(r'<header class="hero compact hero-thailand">.*?</header>', new_hero, doc, flags=re.DOTALL)

    # Info grid
    new_info_grid = f'''      <section class="section">
        <div class="container">
          <div class="grid cols-3">
            <div class="card info-card">
              <div class="body">
                <div class="info-icon">⏱️</div>
                <h2>Duration</h2>
                <p>{duration}</p>
              </div>
            </div>
            <div class="card info-card card-premium">
              <div class="body">
                <div class="info-icon">💰</div>
                <h3>Tour Price</h3>
                <div class="price-row">
                  <span class="price">{price} <small style="font-size: 13px; font-weight: normal; color: var(--text-muted);">{price_note}</small></span>
                </div>
              </div>
            </div>
            <div class="card info-card">
              <div class="body">
                <div class="info-icon">📍</div>
                <h2>Meet-up Location</h2>
                <p>{meetup}</p>
              </div>
            </div>
          </div>
        </div>
      </section>'''
    doc = re.sub(r'<section class="section">\s*<div class="container">\s*<div class="grid cols-3">\s*<div class="card info-card">.*?</section>', new_info_grid, doc, flags=re.DOTALL, count=1)

    # Overview section
    new_overview = f'''      <section class="section alt">
        <div class="container">
          <div class="section-title">
            <h2>Tour Overview &amp; Description</h2>
            <p class="subtitle">{subtitle}</p>
          </div>
          <div class="card" style="padding: 28px;">
            <p style="font-size: 16px; line-height: 1.8; margin-bottom: 20px;">
              {overview_p1}
            </p>
            <p style="font-size: 16px; line-height: 1.8; margin-bottom: 0;">
              {overview_p2}
            </p>
          </div>
        </div>
      </section>'''
    doc = re.sub(r'<section class="section alt">\s*<div class="container">\s*<div class="section-title">\s*<h2>Tour Overview &amp; Description</h2>.*?</section>', new_overview, doc, flags=re.DOTALL)

    # Places Covered / Highlights
    new_places = f'''      <section class="section">
        <div class="container">
          <div class="section-title">
            <h2>Places Covered &amp; Highlights</h2>
            <p class="subtitle">Experience the highlights and sights included on this journey</p>
          </div>

          <div class="two">
            <div class="card">
              <div class="body">
                <div class="badge">{tour["places_col1_badge"]}</div>
                <h3>{tour["places_col1_title"]}</h3>
                <ul class="muted" style="line-height: 1.9; margin-top: 12px;">
{p1_items_html}
                </ul>
              </div>
            </div>

            <div class="card">
              <div class="body">
                <div class="badge">{tour["places_col2_badge"]}</div>
                <h3>{tour["places_col2_title"]}</h3>
                <ul class="muted" style="line-height: 1.9; margin-top: 12px;">
{p2_items_html}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>'''
    doc = re.sub(r'<section class="section">\s*<div class="container">\s*<div class="section-title">\s*<h2>Places Covered.*?</h2>.*?</section>', new_places, doc, flags=re.DOTALL)

    # Inclusions & Exclusions
    new_inc_exc = f'''      <section class="section alt">
        <div class="container">
          <div class="section-title">
            <h2>Inclusions &amp; Exclusions</h2>
            <p class="subtitle">Detailed breakdown of included services and exclusions</p>
          </div>

          <div class="two">
            <div class="card card-premium">
              <div class="body">
                <h3>✅ Inclusions</h3>
                <ul style="line-height: 1.8; margin-top: 12px;">
{inc_html}
                </ul>
              </div>
            </div>

            <div class="card">
              <div class="body">
                <h3>❌ Exclusions</h3>
                <ul class="muted" style="line-height: 1.8; margin-top: 12px;">
{exc_html}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>'''
    doc = re.sub(r'<section class="section alt">\s*<div class="container">\s*<div class="section-title">\s*<h2>Inclusions &amp; Exclusions</h2>.*?</section>', new_inc_exc, doc, flags=re.DOTALL)

    # Tour Information & Schedule
    new_schedule = f'''      <section class="section">
        <div class="container">
          <div class="section-title">
            <h2>Tour Information &amp; Schedule</h2>
            <p class="subtitle">Helpful timing and practical guidelines for your day</p>
          </div>

          <div class="grid cols-3">
            <div class="card">
              <div class="body text-center">
                <div class="feature-icon">⏰</div>
                <h3>Tour Timing</h3>
                <p class="muted">
                  {timing_text}
                </p>
              </div>
            </div>
            <div class="card">
              <div class="body text-center">
                <div class="feature-icon">🚐</div>
                <h3>Transport &amp; Transfers</h3>
                <p class="muted">
                  {transport_text}
                </p>
              </div>
            </div>
            <div class="card">
              <div class="body text-center">
                <div class="feature-icon">🎒</div>
                <h3>What to Bring</h3>
                <p class="muted">
                  {what_to_bring}
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>'''
    doc = re.sub(r'<section class="section">\s*<div class="container">\s*<div class="section-title">\s*<h2>Tour Information &amp; Schedule</h2>.*?</section>', new_schedule, doc, flags=re.DOTALL)

    # CTA section
    new_cta = f'''      <section class="section cta">
        <div class="container">
          <div class="section-title">
            <h2 class="text-white">Book {h1}</h2>
            <p class="subtitle text-white-90">
              Get the best rates on Krabi sightseeing and tours with Trippovention
            </p>
          </div>
          <div class="text-center">
            <a
              class="btn btn-lg ghost"
              href="../../../contact.html?destination=krabi&tour={contact_param}"
              >📞 Request Custom Quote</a
            >
            <a
              class="btn btn-lg ghost ml-16"
              href="https://wa.me/66946934392?text=Hello,%20I%20am%20interested%20in%20booking%20the%20{contact_param}%20in%20Krabi"
              target="_blank"
              rel="noopener noreferrer"
              >💬 WhatsApp: +66 94 693 4392</a>
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
      </section>'''
    doc = re.sub(r'<section class="section cta">.*?</section>', new_cta, doc, flags=re.DOTALL)

    # Footer quick links: ensure Krabi Sightseeing is included
    doc = doc.replace('<a href="../../../services.html">Services</a><br />', '<a href="../../../services.html">Services</a><br />\n              <a href="sightseeing.html">Krabi Sightseeing</a><br />')

    out_file = os.path.join(DEST_DIR, fn)
    with open(out_file, "w", encoding="utf-8") as out_fp:
        out_fp.write(doc)
    print(f"Successfully generated: {fn}")

print("All 19 individual Krabi tour detail pages generated successfully!")
