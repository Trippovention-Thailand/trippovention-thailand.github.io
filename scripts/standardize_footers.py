#!/usr/bin/env python3
"""
Standardize the footer of all HTML pages using docs/index.html as the definitive reference.
Ensures:
- Consistent 3-column layout and text
- Official contact details with WhatsApp: +66 94 693 4392
- Standardized Quick Links including legal & policies (Terms, Privacy, Refund) and destination-specific links
- Thailand office address and official social links (Facebook profile, Instagram, YouTube, WhatsApp)
- Clean copyright row with section-border-top mt-40 pt-30
"""

import os
import glob
import re

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")

DEST_TITLES = {
    "phuket": "Phuket",
    "pattaya": "Pattaya",
    "bangkok": "Bangkok",
    "krabi": "Krabi",
    "chiang_mai": "Chiang Mai",
    "chiang_rai": "Chiang Rai",
    "koh_samui": "Koh Samui",
    "koh_phangan": "Koh Phangan",
    "koh_larn": "Koh Larn",
    "koh_mook": "Koh Mook",
    "phi_phi_island": "Phi Phi Island",
    "ayutthaya": "Ayutthaya",
    "hua_hin": "Hua Hin",
    "trang": "Trang",
    "koh_yao_yai": "Koh Yao Yai",
    "koh_samet": "Koh Samet"
}

def generate_standard_footer(rel_root, dest_folder=None):
    if dest_folder and dest_folder in DEST_TITLES:
        dest_title = DEST_TITLES[dest_folder]
        has_sightseeing = os.path.exists(os.path.join(DOCS_DIR, "packages", "thailand", dest_folder, "sightseeing.html"))
        
        sightseeing_line = f'              <a href="sightseeing.html">{dest_title} Sightseeing Catalogue</a><br />\n' if has_sightseeing else ''
        quick_links = f'''              <a href="{rel_root}index.html">Home</a><br />
              <a href="{rel_root}destinations.html">Destinations by Country</a><br />
              <a href="{rel_root}destinations-themes.html">Destinations by Theme</a><br />
              <a href="{rel_root}destinations-travelers.html">Destinations by Traveler</a><br />
              <a href="{rel_root}services.html">Services</a><br />
{sightseeing_line}              <a href="index.html">{dest_title} Tour Packages</a><br />
              <a href="{rel_root}contact.html">Contact</a><br />
              <a href="{rel_root}terms-and-conditions.html">Terms &amp; Conditions</a><br />
              <a href="{rel_root}privacy-policy.html">Privacy Policy</a><br />
              <a href="{rel_root}refund-policy.html">Refund Policy</a>'''
    else:
        quick_links = f'''              <a href="{rel_root}index.html">Home</a><br />
              <a href="{rel_root}destinations.html">Destinations by Country</a><br />
              <a href="{rel_root}destinations-themes.html">Destinations by Theme</a><br />
              <a href="{rel_root}destinations-travelers.html">Destinations by Traveler</a><br />
              <a href="{rel_root}services.html">Services</a><br />
              <a href="{rel_root}contact.html">Contact</a><br />
              <a href="{rel_root}terms-and-conditions.html">Terms &amp; Conditions</a><br />
              <a href="{rel_root}privacy-policy.html">Privacy Policy</a><br />
              <a href="{rel_root}refund-policy.html">Refund Policy</a>'''

    footer_html = f'''    <footer class="footer" role="contentinfo">
      <div class="container">
        <div class="grid cols-3">
          <div>
            <h3>Trippovention</h3>
            <p>
              Thailand-registered travel and ground operations company offering curated land packages, sightseeing, private transfers, and day trips.
            </p>
            <div class="mt-20">
              <h3 class="muted font-weight-600">Contact Details</h3>
              <span class="mr-15">📧
                <a href="mailto:query@trippovention.co.th">query@trippovention.co.th</a></span>
              <br />
              <span>📞 <a href="tel:+66946934392">+66 94 693 4392</a></span>
              <br />
              <span>💬
                <a href="https://wa.me/66946934392" target="_blank" rel="noopener noreferrer">WhatsApp: +66 94 693 4392</a></span>
              <br />
              <span>💬 LINE: +66 94 693 4392 or <a href="https://line.me/ti/p/~trippovention" target="_blank" rel="noopener noreferrer">trippovention</a></span>
            </div>
          </div>
          <div>
            <h3>Quick Links</h3>
            <div class="line-height-2">
{quick_links}
            </div>
          </div>
          <div>
            <h3>Thailand Office</h3>
            <p>
              Trippovention Co., Ltd.<br />23/13 M, 12 Nong Pure Subdistrict, Bang Lamung District, Chonburi Province - 20150
            </p>
            <div class="mt-20">
              <h3 class="muted font-weight-600">Follow Us</h3>
              <div class="social-icons">
                <a
                  href="https://www.facebook.com/profile.php?id=61590071764774"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Follow us on Facebook"
                  title="Facebook"
                >
                  <img
                    src="{rel_root}assets/images/social/facebook.svg"
                    alt="Facebook"
                    width="24"
                    height="24"
                    class="social-icon-white"
                    loading="lazy"
                  />
                </a>
                <a
                  href="https://www.instagram.com/trippoventioncoltd/"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Follow us on Instagram"
                  title="Instagram"
                >
                  <img
                    src="{rel_root}assets/images/social/instagram.svg"
                    alt="Instagram"
                    width="24"
                    height="24"
                    class="social-icon-white"
                    loading="lazy"
                  />
                </a>
                <a
                  href="https://www.youtube.com/@TrippoventionCoLtd"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Follow us on YouTube"
                  title="YouTube"
                >
                  <img
                    src="{rel_root}assets/images/social/youtube.svg"
                    alt="YouTube"
                    width="24"
                    height="24"
                    class="social-icon-white"
                    loading="lazy"
                  />
                </a>
                <a
                  href="https://wa.me/66946934392"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Chat on WhatsApp"
                  title="WhatsApp"
                >
                  <img
                    src="{rel_root}assets/images/social/whatsapp.svg"
                    alt="WhatsApp"
                    width="24"
                    height="24"
                    class="social-icon-white"
                    loading="lazy"
                  />
                </a>
              </div>
            </div>
          </div>
        </div>
        <div class="text-center section-border-top mt-40 pt-30">
          <p>© 2026 Trippovention. All Rights Reserved.</p>
        </div>
      </div>
    </footer>'''
    return footer_html

def process_file(filepath):
    rel_path = os.path.relpath(filepath, DOCS_DIR)
    parts = rel_path.split(os.sep)

    # Skip error/offline pages that intentionally have minimal templates
    if rel_path in ["offline.html", "404.html"]:
        return False, "Skipped (utility/error page)"

    # Determine relative root and destination folder
    depth = len(parts) - 1
    rel_root = "" if depth == 0 else "../" * depth

    dest_folder = None
    if len(parts) >= 4 and parts[0] == "packages" and parts[1] == "thailand":
        dest_folder = parts[2]

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    footer_regex = r'<footer\s+class=["\']footer["\'][\s\S]*?</footer>'
    if not re.search(footer_regex, content):
        return False, "No footer found"

    # Avoid modifying docs/index.html itself since it is the master template
    if filepath == os.path.join(DOCS_DIR, "index.html"):
        return False, "Master reference template (skipped)"

    new_footer = generate_standard_footer(rel_root, dest_folder)
    updated_content = re.sub(footer_regex, new_footer, content)

    if updated_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated_content)
        return True, "Standardized"
    else:
        return False, "Already standardized"

def main():
    print("=" * 70)
    print("STANDARDIZING FOOTERS ACROSS ALL HTML PAGES")
    print("Reference: docs/index.html")
    print("=" * 70)

    total_files = 0
    updated_files = 0

    for root, _, files in os.walk(DOCS_DIR):
        for f in files:
            if f.endswith(".html"):
                fp = os.path.join(root, f)
                total_files += 1
                changed, msg = process_file(fp)
                if changed:
                    updated_files += 1
                    rel = os.path.relpath(fp, DOCS_DIR)
                    print(f"Updated: {rel}")

    print(f"\nCompleted footer standardization:")
    print(f"Total HTML files checked: {total_files}")
    print(f"Total HTML files updated: {updated_files}")

if __name__ == "__main__":
    main()
