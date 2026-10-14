#!/usr/bin/env python3
"""
Fix boilerplate/marine FAQ text in existing Bangkok sightseeing pages.
Ensures Bangkok-specific, accurate content for visible FAQs and FAQPage schema.
"""

import os
import re

BANGKOK_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "packages", "thailand", "bangkok")

UPDATES = {
    "full_day_bangkok_city_tour.html": {
        "faqs": [
            ("What is included in the Full Day Bangkok City Tour?", "This full-day sightseeing tour includes roundtrip transport from central Bangkok hotels in an air-conditioned vehicle, licensed English-speaking professional guidance, entrance fees to designated temples and cultural landmarks, and chilled drinking water throughout the excursion."),
            ("Where is the pickup point and what time does the tour start?", "Complimentary shared or private hotel pickup is available from central Bangkok hotels (Sukhumvit, Silom, Sathorn, Siam, and Pratunam). Pickup typically takes place between 08:00 AM and 08:30 AM, with return around 04:30 PM."),
            ("What items and clothing should I wear on this temple tour?", "We recommend wearing modest attire that covers your shoulders and knees or ankles, as strictly required by sacred Buddhist temples. Wear comfortable walking shoes, a sun hat, sunglasses, and bring a camera for photos."),
            ("How do I check availability and confirm my tour reservation?", "Click 'Get Custom Quote' or contact our destination team via WhatsApp (+66 94 693 4392). We verify vehicle and licensed guide availability for your preferred date and guide you through our straightforward offline booking process.")
        ]
    },
    "princess_chao_phraya_dinner_cruise.html": {
        "faqs": [
            ("What is included in the Princess Chao Phraya Dinner Cruise?", "This evening cruise includes a 2-hour luxury voyage on the Chao Phraya River, a welcome drink, an extensive international and seafood buffet dinner, hot tea and coffee, and live musical entertainment."),
            ("Where is the boarding point and what time does the cruise depart?", "Cruising typically boards from Asiatique The Riverfront Pier or IconSiam Pier. Check-in is required between 06:30 PM and 07:15 PM, with the vessel sailing from 07:30 PM to 09:30 PM."),
            ("What is the dress code for the dinner cruise?", "Smart casual attire is recommended. The indoor dining salons are fully air-conditioned, while the open-air upper deck enjoys scenic evening breezes."),
            ("How do I check availability and confirm my dinner cruise reservation?", "Click 'Get Custom Quote' or contact our destination team via WhatsApp (+66 94 693 4392). We verify table availability, upper deck seating preferences, and coordinate your reservation with official booking vouchers.")
        ]
    },
    "safari_world_and_marine_park.html": {
        "faqs": [
            ("What is included in the Safari World & Marine Park package?", "Our comprehensive package includes full-day admission to both Safari Park (Open Zoo) and Marine Park, the 45-minute safari drive-through, access to all 7 daily animal shows (Dolphin, Sea Lion, Orangutan, Stunt Shows), a delicious international lunch buffet, and round-trip transfers from central Bangkok."),
            ("Where is the pickup point and what time does the excursion depart?", "Complimentary hotel pickup is available from central Bangkok hotels between 08:00 AM and 08:30 AM. The return transfer departs Safari World around 04:00 PM, arriving back in downtown Bangkok by 05:00–05:30 PM."),
            ("What should I bring for a day at Safari World?", "We recommend wearing light, comfortable clothing and walking shoes. Bring a sun hat, sunglasses, sunscreen, a camera, and small cash for optional giraffe feeding fruit buckets (100–150 THB)."),
            ("How do I check availability and confirm my Safari World tickets?", "Click 'Get Custom Quote' or contact our team via WhatsApp (+66 94 693 4392). We arrange guaranteed entry vouchers, dietary lunch arrangements, and seamless hotel transport.")
        ]
    }
}

def update_file(filename, data):
    fpath = os.path.join(BANGKOK_DIR, filename)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Build visible FAQ html
    visible_items = []
    for i, (q, a) in enumerate(data["faqs"]):
        is_open = " open" if i == 0 else ""
        visible_items.append(f"""            <details class="faq-item"{is_open}>
              <summary class="faq-question"><span>{q}</span><span class="faq-chevron" aria-hidden="true">▾</span></summary>
              <div class="faq-answer"><p>{a}</p></div>
            </details>""")
    visible_faq_html = "\n".join(visible_items)

    # Replace visible FAQ container
    content = re.sub(
        r'<div class="faq-container">.*?</div>\s*</div>\s*</section>',
        f'<div class="faq-container">\n{visible_faq_html}\n          </div>\n        </div>\n      </section>',
        content,
        flags=re.DOTALL
    )

    # Build schema items
    schema_items = []
    for q, a in data["faqs"]:
        schema_items.append(f"""            {{
                  "@type": "Question",
                  "name": "{q}",
                  "acceptedAnswer": {{
                        "@type": "Answer",
                        "text": "{a}"
                  }}
            }}""")
    schema_faq_str = ",\n".join(schema_items)

    # Replace schema FAQPage
    schema_replacement = f"""<script type="application/ld+json">
{{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
{schema_faq_str}
      ]
}}
    </script>"""

    content = re.sub(
        r'<script type="application/ld\+json">\s*\{\s*"@context":\s*"https://schema.org",\s*"@type":\s*"FAQPage".*?</script>',
        schema_replacement,
        content,
        flags=re.DOTALL
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated FAQs in {filename}")

def main():
    for fname, data in UPDATES.items():
        update_file(fname, data)

if __name__ == "__main__":
    main()
