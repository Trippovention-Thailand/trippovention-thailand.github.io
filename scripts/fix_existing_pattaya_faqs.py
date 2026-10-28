#!/usr/bin/env python3
"""
Update existing 5 Pattaya sightseeing pages with authentic, product-specific FAQs and FAQPage schema.
Replaces generic placeholder FAQs with accurate visitor information.
"""

import os
import re

PATTAYA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "packages", "thailand", "pattaya")

UPDATES = {
    "alcazar_cabaret_show.html": {
        "faqs": [
            ("What is the difference between Standard, VIP, and VIP Gold seats?", "Standard seats are located on the second tier / mezzanine. VIP seats occupy rows 6 through 15 on the main floor, offering great sightlines. VIP Gold seats are in rows 1 through 5 directly in front of the stage for the most immersive experience."),
            ("What are the showtimes for Alcazar Cabaret?", "Alcazar presents four daily performances: 05:00 PM, 06:30 PM, 08:00 PM, and 09:30 PM. Each show runs for approximately 70 minutes with no intermission."),
            ("Can audience members take photos with performers after the show?", "Yes! Following the finale, the entire cast gathers outside the theatre courtyard in their extravagant costumes. Guests can take photos with their favorite performers for a nominal cash tip (typically 50–100 THB per performer)."),
            ("Is Alcazar Cabaret suitable for children and families?", "Yes, Alcazar is an all-ages, family-friendly musical extravaganza featuring worldwide songs, comedy acts, and traditional cultural dance routines without explicit content.")
        ]
    },
    "coral_island_tour.html": {
        "faqs": [
            ("What is included in the Coral Island (Koh Larn) day tour?", "Our package includes shared round-trip speedboat transfer from Bali Hai Pier, safety life vests, a delicious Indian or seafood beachside lunch, and complimentary beach chair usage at Tawaen or Tien Beach."),
            ("Can I add water sports like parasailing or jet ski on the day?", "Yes, optional activities like parasailing, seawalker helmet diving, jet skiing, and banana boat rides can be booked in advance or arranged directly on the island through our tour coordinator."),
            ("What happens if there is rough weather or choppy seas?", "Guest safety is our highest priority. In the rare event of heavy storms or official marine police warnings, the tour will be rescheduled or alternative indoor activities offered according to our flexibility guarantee."),
            ("What should I bring for the Coral Island excursion?", "Bring swimwear, a beach towel, sun cream, sunglasses, waterproof dry bag for your phone, and cash in Thai Baht for personal snacks or souvenirs.")
        ]
    },
    "dolphin_show_with_tiger_park.html": {
        "faqs": [
            ("What is included in the Dolphin Show with Tiger Park combination?", "This comprehensive combo package includes admission and standard grandstand seating for the Pattaya Dolphinarium show, entrance to Tiger Park Pattaya with access to viewing walkways, and air-conditioned hotel transfers."),
            ("Are tiger cage interactions included in the base ticket?", "Base admission allows you to observe the tigers playing and resting from secure elevated walkways. Direct cage interactions with newborn cubs or full-grown tigers are optional add-ons that can be requested when customizing your package."),
            ("How long is the dolphin performance?", "The marine mammal show runs for approximately 50 minutes, featuring acrobatic Pacific bottlenose dolphins and charming South American fur seals performing synchronized tricks, jumps, and ball stunts."),
            ("Is this combination tour suitable for young children and seniors?", "Yes, both venues feature paved flat pathways, ramps for strollers/wheelchairs, air-conditioned gift shops, and covered shaded seating areas.")
        ]
    },
    "nong_nooch_tropical_garden.html": {
        "faqs": [
            ("How big is Nong Nooch Tropical Garden and how do we get around?", "Nong Nooch spans over 600 acres featuring 30+ themed gardens. Our package includes the panoramic hop-on hop-off sightseeing tram, making it effortless to explore the French Garden, Stonehenge replica, and Dinosaur Valley without walking long distances under the sun."),
            ("Are both cultural and elephant shows included in the ticket?", "Yes, our all-inclusive pass provides reserved seating for the spectacular Thai Cultural Dance & Martial Arts show in the air-conditioned theatre, as well as the world-renowned gentle elephant talent performance."),
            ("What is Dinosaur Valley at Nong Nooch?", "Dinosaur Valley is a massive outdoor prehistoric installation featuring life-size, scientifically accurate sculptures of hundreds of dinosaur species with sound effects—an absolute favorite for children and photographers!"),
            ("How much time is recommended to visit Nong Nooch?", "We recommend allowing at least 4 to 5 hours (half-day) to watch the cultural shows, ride the sightseeing tram through the botanical collections, and enjoy lunch at the resort's restaurants.")
        ]
    },
    "pattaya_city_tour_with_colosseum_show.html": {
        "faqs": [
            ("What landmarks are covered during the daytime city tour?", "The daytime itinerary includes the panoramic Pratumnak Hill viewpoint overlooking Pattaya Crescent Bay, the revered 18-meter golden statue at Wat Phra Yai (Big Buddha Temple), and a scenic drive along Pattaya Beach Road and Jomtien."),
            ("What time does the Colosseum Cabaret Show start?", "The Colosseum Show performs at 06:00 PM and 07:30 PM. Your tour guide will seamlessly transfer you from the daytime sightseeing portion directly to the Colosseum Theatre before showtime."),
            ("What makes the Colosseum Show unique compared to other cabarets?", "The Colosseum is housed in a colossal Roman amphitheatre-inspired complex with 1,250 amphitheatre seats, state-of-the-art hydraulic stage sets, and 14 kaleidoscopic acts showcasing cultural dances from China, India, Persia, and the West."),
            ("Are hotel pickups and return transfers included?", "Yes, this combo tour includes round-trip air-conditioned hotel transfers from central Pattaya hotels throughout the entire duration of the tour and evening show.")
        ]
    }
}

def generate_faq_html(faqs):
    html = ['          <div class="faq-container">']
    for idx, (q, a) in enumerate(faqs):
        open_attr = " open" if idx == 0 else ""
        html.append(f'            <details class="faq-item"{open_attr}>')
        html.append(f'              <summary class="faq-question"><span>{q}</span><span class="faq-chevron" aria-hidden="true">▾</span></summary>')
        html.append(f'              <div class="faq-answer"><p>{a}</p></div>')
        html.append('            </details>')
    html.append('          </div>')
    return "\n".join(html)

def generate_faq_schema(faqs):
    entities = []
    for q, a in faqs:
        entities.append(f'''          {{
            "@type": "Question",
            "name": "{q}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{a}"
            }}
          }}''')
    entity_str = ",\n".join(entities)
    return f'''    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
{entity_str}
        ]
      }}
    </script>'''

def update_file(filename, data):
    filepath = os.path.join(PATTAYA_DIR, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        return
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Update FAQ container HTML
    new_faq_html = generate_faq_html(data["faqs"])
    faq_container_regex = r'<div class="faq-container">[\s\S]*?</div>\s*</div>\s*</section>'
    replacement = f'{new_faq_html}\n        </div>\n      </section>'
    content = re.sub(faq_container_regex, replacement, content)
    
    # 2. Update FAQ schema
    new_faq_schema = generate_faq_schema(data["faqs"])
    faq_schema_regex = r'<script type="application/ld\+json">\s*\{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"FAQPage"[\s\S]*?</script>'
    if re.search(faq_schema_regex, content):
        content = re.sub(faq_schema_regex, new_faq_schema, content)
    else:
        # Insert before </head>
        content = content.replace("</head>", f"{new_faq_schema}\n  </head>")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully updated FAQs for {filename}")

def main():
    for filename, data in UPDATES.items():
        update_file(filename, data)

if __name__ == "__main__":
    main()
