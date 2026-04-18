"""
Fresh-clone transform: apply Thailand overlays to all HTML files in docs/.
Run AFTER cloning main site and restoring Thailand-only JS/CSS/config files.
"""

import os
import re

DOCS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs"))

LANG_TOGGLE_BTN = '<button class="lang-btn notranslate" id="langToggle" translate="no">TH</button>'

THAI_FOOTER_CONTACT = """<h3 class="muted font-weight-600">Contact Details</h3>
                <span class="mr-15"
                  >\u200d\U0001f4e7 <a href="mailto:query@trippovention.co.th">query@trippovention.co.th</a></span
                >
                <br />
                <span>\U0001f4de <a href="tel:+66909177601">+66 90 917 7601</a></span>
                <br />
                <span
                  >\U0001f4ac
                  <a
                    href="https://wa.me/+66909177601"
                    target="_blank"
                    rel="noopener noreferrer"
                    >WhatsApp</a
                  ></span
                >
                <br />
                <p class="muted" style="margin-top: 8px; font-size: 13px">
                  India office:
                  <a href="tel:+911244182575">+91 124 418 2575</a> /
                  <a href="tel:+917303010446">+91 73030 10446</a>
                </p>"""

THAI_FOOTER_OFFICES = """<h3>Thailand Office</h3>
              <p>
                23/13 M, 12 Nong Pure Subdistrict, Bang Lamung District, Chonburi Province-20150
              </p>
              <div class="mt-20">
                <h3>India Office</h3>
                <p>
                  Unit No. - 337 A, 3rd Floor, Spaze IT Park, Tower A, Sector 49, Sohna Road,
                  Gurgaon, Haryana, India, 122018.
                </p>
              </div>"""

THAI_JSON_LD_ADDRESS = """"address": {
          "@type": "PostalAddress",
          "streetAddress": "23/13 M, 12 Nong Pure Subdistrict, Bang Lamung District",
          "addressLocality": "Chonburi",
          "addressRegion": "Chonburi Province",
          "postalCode": "20150",
          "addressCountry": "TH"
        }"""

EXPLORE_THAILAND_SECTION = """      <section class="section alt">
        <div class="container">
          <div class="section-title">
            <h2>Explore Thailand</h2>
            <p class="subtitle">Discover Thailand's tropical paradise with exclusive deals</p>
          </div>
          <div class="grid cols-3">
            <div class="card">
              <div class="img-wrap">
                <img
                  src="assets/images/packages/thailand/hero_pattaya_bangkok.webp"
                  alt="Pattaya and Bangkok city skyline and beach"
                  loading="lazy"
                />
                <span class="ribbon hot">\U0001f525 Popular</span>
              </div>
              <div class="body">
                <div class="badge">\U0001f3d6\ufe0f Pattaya &amp; Bangkok</div>
                <h3>Pattaya &amp; Bangkok Delight</h3>
                <p class="muted">Pattaya Beach \u2022 Walking Street \u2022 Grand Palace \u2022 Floating Market</p>
                <div class="price-row">
                  <span class="price-label">Starting from</span>
                  <span class="price-old">\u0e3f 19,999</span>
                  <span class="price">\u0e3f 16,999 <span class="muted">/ pax</span></span>
                </div>
                <a class="btn" href="packages/thailand/thailand_pattaya_and_bangkok_delight.html">View Details \u2192</a>
              </div>
            </div>
            <div class="card">
              <div class="img-wrap">
                <img
                  src="assets/images/packages/thailand/hero_krabi_phuket.webp"
                  alt="Krabi and Phuket tropical island escape"
                  loading="lazy"
                />
                <span class="ribbon">\u2728 Featured</span>
              </div>
              <div class="body">
                <div class="badge">\U0001f3dd\ufe0f Krabi &amp; Phuket</div>
                <h3>Tropical Twin Escape</h3>
                <p class="muted">Phi Phi Islands \u2022 Railay Beach \u2022 Patong \u2022 Big Buddha</p>
                <div class="price-row">
                  <span class="price-label">Starting from</span>
                  <span class="price-old">\u0e3f 24,999</span>
                  <span class="price">\u0e3f 21,999 <span class="muted">/ pax</span></span>
                </div>
                <a class="btn" href="packages/thailand/tropical_twin_escape_krabi_and_phuket_edition.html">View Details \u2192</a>
              </div>
            </div>
            <div class="card">
              <div class="img-wrap">
                <img
                  src="assets/images/packages/thailand/hero_thailand_culture.webp"
                  alt="Northern Thailand Chiang Mai temples and culture"
                  loading="lazy"
                />
                <span class="ribbon">\U0001f451 Royal</span>
              </div>
              <div class="body">
                <div class="badge">\u26f0\ufe0f Northern Thailand</div>
                <h3>Northern Discovery</h3>
                <p class="muted">Chiang Mai \u2022 Chiang Rai \u2022 White Temple \u2022 Night Bazaar</p>
                <div class="price-row">
                  <span class="price-label">Starting from</span>
                  <span class="price-old">\u0e3f 22,999</span>
                  <span class="price">\u0e3f 19,999 <span class="muted">/ pax</span></span>
                </div>
                <a class="btn" href="packages/thailand/thailand_northern_discovery.html">View Details \u2192</a>
              </div>
            </div>
            <div class="card">
              <div class="img-wrap">
                <img
                  src="assets/images/packages/thailand/hero_koh_samui_bangkok.webp"
                  alt="Koh Samui island and Bangkok city adventure"
                  loading="lazy"
                />
                <span class="ribbon">\U0001f31f Premium</span>
              </div>
              <div class="body">
                <div class="badge">\U0001f30a Island &amp; City</div>
                <h3>Island &amp; City Delight</h3>
                <p class="muted">Koh Samui \u2022 Bangkok \u2022 Temple Tours \u2022 Beach Relaxation</p>
                <div class="price-row">
                  <span class="price-label">Starting from</span>
                  <span class="price-old">\u0e3f 27,999</span>
                  <span class="price">\u0e3f 24,999 <span class="muted">/ pax</span></span>
                </div>
                <a class="btn" href="packages/thailand/thailand_island_and_city_delight.html">View Details \u2192</a>
              </div>
            </div>
            <div class="card">
              <div class="img-wrap">
                <img
                  src="assets/images/packages/thailand/hero_thailand_kids_traveler.webp"
                  alt="Thailand kids and family adventure"
                  loading="lazy"
                />
                <span class="ribbon">\U0001f3d4\ufe0f Adventure</span>
              </div>
              <div class="body">
                <div class="badge">\U0001f9d2 Kids Adventure</div>
                <h3>Kids Adventure Delight</h3>
                <p class="muted">Safari World \u2022 Elephant Sanctuary \u2022 Water Parks \u2022 Night Market</p>
                <div class="price-row">
                  <span class="price-label">Starting from</span>
                  <span class="price-old">\u0e3f 21,999</span>
                  <span class="price">\u0e3f 18,999 <span class="muted">/ pax</span></span>
                </div>
                <a class="btn" href="packages/thailand/thailand_kids_adventure_delight.html">View Details \u2192</a>
              </div>
            </div>
            <div class="card">
              <div class="img-wrap">
                <img
                  src="assets/images/packages/thailand/hero_phuket_beach.webp"
                  alt="Phuket beach luxury escape"
                  loading="lazy"
                />
                <span class="ribbon">\u23f0 Limited</span>
              </div>
              <div class="body">
                <div class="badge">\U0001f3d6\ufe0f Beach Escape</div>
                <h3>Phuket Beach Bliss</h3>
                <p class="muted">Kata Beach \u2022 Old Town \u2022 Phang Nga Bay \u2022 Sunset Cruise</p>
                <div class="price-row">
                  <span class="price-label">Starting from</span>
                  <span class="price-old">\u0e3f 19,999</span>
                  <span class="price">\u0e3f 16,999 <span class="muted">/ pax</span></span>
                </div>
                <a class="btn" href="packages/thailand/tropical_twin_escape_krabi_and_phuket_edition.html">View Details \u2192</a>
              </div>
            </div>
          </div>
        </div>
      </section>"""


def transform_all_html(html, rel_path):
    # ── 1. Domain swap ──
    html = html.replace("trippovention.com", "trippovention.co.th")

    # ── 2. Homepage title ──
    html = html.replace(
        "Trippovention - Tours &amp; Visa Services | 15+ Years Experience",
        "Trippovention - Worldwide Tours &amp; Travel Experts | 15+ Years Experience",
    )
    html = html.replace(
        "Trippovention - Tours & Visa Services | 15+ Years Experience",
        "Trippovention - Worldwide Tours & Travel Experts | 15+ Years Experience",
    )

    # ── 3. Nav primary phone ──
    html = html.replace('href="tel:+918750888875"', 'href="tel:+66909177601"')

    # ── 4. Nav WhatsApp ──
    html = html.replace(
        'href="https://wa.me/+918750888875"', 'href="https://wa.me/+66909177601"'
    )

    # ── 5. langToggle injection ──
    if 'id="langToggle"' not in html:
        html = re.sub(
            r'(<div\s+class="actions">\s*\n)',
            r"\g<1>            " + LANG_TOGGLE_BTN + "\n",
            html,
        )

    # ── 6. Remove Visa nav links (any depth) ──
    html = re.sub(
        r'\s*<a\s+href="(?:\.\./)*visa/index\.html[^"]*"[^>]*>\s*Visa\s*</a>\s*\n?',
        "\n",
        html,
    )

    # ── 7. Remove Visa from footer Quick Links ──
    html = re.sub(
        r'\s*<a\s+href="(?:\.\./)*visa/index\.html[^"]*">\s*Visa\s*</a><br\s*/?>\s*\n?',
        "\n",
        html,
    )

    # ── 8. Footer contact details block ──
    contact_pat = re.compile(
        r'<h3 class="muted font-weight-600">Contact Details</h3>'
        r'.*?'
        r'</div>\s*</div>',
        re.DOTALL,
    )
    m = contact_pat.search(html)
    if m and "+91 87508 88875" in m.group(0):
        html = (
            html[: m.start()]
            + THAI_FOOTER_CONTACT
            + "\n              </div>\n            </div>"
            + html[m.end() :]
        )

    # ── 9. Footer offices: Corporate first -> Thailand first ──
    offices_pat = re.compile(
        r'<h3>Corporate Office</h3>\s*<p>[^<]*?Gurgaon[^<]*?</p>\s*'
        r'<div class="mt-20">\s*<h3>Thailand Office</h3>\s*<p>[^<]*?Chonburi[^<]*?</p>\s*</div>',
        re.DOTALL,
    )
    html = offices_pat.sub(THAI_FOOTER_OFFICES, html)

    # ── 10. JSON-LD inline: India address -> Thailand ──
    india_addr_pat = re.compile(
        r'"address"\s*:\s*\{[^}]*"addressCountry"\s*:\s*"IN"[^}]*\}', re.DOTALL
    )
    html = india_addr_pat.sub(THAI_JSON_LD_ADDRESS, html)

    # ── 11. JSON-LD phone ──
    html = html.replace(
        '"telephone": "+91-87508-88875"', '"telephone": "+66-90-917-7601"'
    )

    # ── 12. Remaining visible +91 primary phone text ──
    html = html.replace(">+91 87508 88875</a>", ">+66 90 917 7601</a>")

    # ── 13. Refund-policy special number ──
    html = html.replace("tel:+919205055461", "tel:+66909177601")
    html = html.replace("+91 92050 55461", "+66 90 917 7601")

    # ── 14. OG/twitter description - visa mentions ──
    html = html.replace(
        "India tours, worldwide experiences, and hassle-free visa services",
        "Thailand tours, worldwide experiences, and practical trip planning support",
    )
    html = html.replace("hassle-free visa services", "practical trip planning support")
    html = html.replace(
        "visa services, and custom packages",
        "custom packages, and ground operations support",
    )

    # ── 15. "Why Choose" card: visa -> trusted support ──
    html = html.replace(
        "<h3>Seamless Visa Services</h3>",
        "<h3>Trusted Travel Support</h3>",
    )
    html = html.replace(
        "We specialize in providing seamless visa services, ensuring your travel plans are\n"
        "                  hassle-free with end-to-end processing.",
        "We provide end-to-end travel support, ensuring your plans are hassle-free with\n"
        "                  expert guidance from booking to return.",
    )

    # ── 16. Hero CTA: Explore India -> Explore Thailand ──
    html = html.replace(
        'href="packages/india/index.html">Explore India</a>',
        'href="packages/thailand/index.html">Explore Thailand</a>',
    )

    # ── 17. Remove Visa Processing section from homepage ──
    visa_section_pat = re.compile(
        r'\n\s*<section class="section">\s*\n\s*<div class="container">\s*\n\s*'
        r'<div class="section-title">\s*\n\s*'
        r'<h2>Seamless Visa Processing for Global Travel</h2>.*?</section>',
        re.DOTALL,
    )
    html = visa_section_pat.sub("", html)

    # ── 18. Replace "Incredible India" section with "Explore Thailand" ──
    india_section_pat = re.compile(
        r'<section class="section alt">\s*\n\s*<div class="container">\s*\n\s*'
        r'<div class="section-title">\s*\n\s*'
        r'<h2>Incredible India</h2>.*?</section>',
        re.DOTALL,
    )
    html = india_section_pat.sub(EXPLORE_THAILAND_SECTION, html)

    # ── 19. FAQ schema: neutralize visa references ──
    html = html.replace(
        "Trippovention offers comprehensive travel services including visa assistance, tour packages",
        "Trippovention offers comprehensive travel services including tour packages",
    )
    html = html.replace(
        "Which countries can I get visa assistance for?",
        "Which countries does Trippovention offer tours to?",
    )
    html = html.replace(
        "We provide visa assistance for multiple countries including Singapore, Dubai, Malaysia, Thailand, Australia, UK, USA, Schengen countries (Europe), and more. Our experienced team handles document preparation, application submission, and follow-up for hassle-free visa processing.",
        "We offer tour packages to many countries including Singapore, Dubai, Malaysia, Thailand, Australia, UK, USA, European countries, and more. Our experienced team creates customized itineraries and handles ground operations for a seamless travel experience.",
    )

    # ── 20. Services page: Visa Assistance card ──
    html = html.replace(
        "<h3>Visa Assistance</h3>",
        "<h3>Ground Operations</h3>",
    )
    html = re.sub(
        r"End-to-end visa documentation and processing for all major destinations\. Our\s*\n\s*experts handle the paperwork so you can focus on planning your trip\.",
        "End-to-end ground support for all major destinations. Our\n                  experts handle logistics so you can focus on enjoying your trip.",
        html,
    )
    html = html.replace("📋 Documentation", "🚗 Transport")
    html = html.replace("⚡ Fast Processing", "⚡ Seamless Support")

    # ── 21. Services structured data ──
    html = html.replace(
        'name: "Visa Assistance",\n                description: "Expert visa services for all major countries"',
        'name: "Ground Operations",\n                description: "Expert ground support for all major destinations"',
    )

    # ── 22. Services page titles ──
    html = html.replace(
        "Travel Services - Tours, Visa, Flights &amp; Hotels | Trippovention",
        "Travel Services - Tours, Flights &amp; Hotels | Trippovention",
    )

    # ── 23. Contact page: Visa Assistance option ──
    html = html.replace(
        '<option value="Visa Assistance">Visa Assistance</option>',
        '<option value="Ground Operations">Ground Operations</option>',
    )

    # ── 24. Terms: visa -> ground ops ──
    html = html.replace(
        "Flight Bookings, Hotel\n                Reservations, Holiday Packages, Visa Assistance, Cruise Bookings",
        "Flight Bookings, Hotel\n                Reservations, Holiday Packages, Ground Operations, Cruise Bookings",
    )

    # ── 25. Thank-you page: visa card -> ground ops ──
    html = html.replace(
        '<div class="feature-icon">🛂</div>\n                <h3>Visa Services</h3>',
        '<div class="feature-icon">🌍</div>\n                <h3>Ground Operations</h3>',
    )
    html = html.replace(
        "Hassle-free visa assistance for tourist, business, and transit visas. Expert\n                  guidance for smooth processing.",
        "Seamless ground operations and travel support for all your destinations. Expert\n                  guidance for a smooth journey.",
    )
    html = re.sub(
        r'<a class="btn" href="(?:\.\./)*visa/index\.html[^"]*">[^<]*</a>',
        '<a class="btn" href="services.html">Learn More</a>',
        html,
    )

    # ── 26. Any remaining visa/index.html links ──
    html = re.sub(
        r'<a\s+[^>]*href="(?:\.\./)*visa/index\.html[^"]*"[^>]*>[^<]*</a>',
        "",
        html,
    )

    # ── 27. Package hub visa requirement sections: clean up ──
    # Remove entire "Visa Requirements" comment-delimited sections
    html = re.sub(
        r'<!--\s*Visa\s+Requirements?\s*-->\s*<section[^>]*>.*?</section>\s*',
        "",
        html,
        flags=re.DOTALL | re.IGNORECASE,
    )

    # ── 28. Remove "Apply Visa" CTAs ──
    html = re.sub(
        r'\s*<a[^>]*>[^<]*Apply\s+Visa[^<]*</a>\s*',
        "",
        html,
        flags=re.IGNORECASE,
    )

    # ── 29. Replace "Get Visa Assistance" buttons ──
    html = re.sub(
        r'\s*<a[^>]*>[^<]*(?:Get\s+)?Visa\s+Assistance[^<]*</a>\s*',
        "",
        html,
        flags=re.IGNORECASE,
    )

    # ── 30. Clean up "View All Visa Services" button ──
    html = re.sub(
        r'\s*<a[^>]*href="[^"]*visa[^"]*"[^>]*class="btn[^"]*"[^>]*>[^<]*Visa[^<]*</a>\s*',
        "",
        html,
        flags=re.IGNORECASE,
    )

    return html


def main():
    count = 0
    errors = []
    for dp, dn, fns in os.walk(DOCS):
        for f in sorted(fns):
            if not f.endswith(".html"):
                continue
            fpath = os.path.join(dp, f)
            rel = os.path.relpath(fpath, DOCS).replace("\\", "/")
            try:
                with open(fpath, "r", encoding="utf-8") as fh:
                    html = fh.read()
                result = transform_all_html(html, rel)
                with open(fpath, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(result)
                count += 1
            except Exception as e:
                errors.append((rel, str(e)))
                print(f"  ERROR {rel}: {e}")

    print(f"Transformed {count} HTML files, {len(errors)} errors")
    if errors:
        for p, e in errors:
            print(f"  {p}: {e}")


if __name__ == "__main__":
    main()
