#!/usr/bin/env python3
"""
Update existing 5 Phuket sightseeing pages with authentic, product-specific FAQs and FAQPage schema.
Replaces generic placeholder FAQs with accurate visitor information.
"""

import os
import re

PHUKET_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "packages", "thailand", "phuket")

UPDATES = {
    "carnival_magic_show.html": {
        "faqs": [
            ("What is Carnival Magic and what are the main attractions?", "Carnival Magic is Phuket's dazzling 40-acre nighttime carnival theme park located in Kamala. It features the Carnival Fun Fair shopping street, the colossal 3,000-seat Bird of Paradise buffet restaurant, the record-breaking River Carnival indoor parade pageant, and the Kingdom of Lights walk-through illumination zone boasting over 40 million glowing LED lights."),
            ("What are the opening days and showtimes for Carnival Magic?", "Carnival Magic opens on Mondays, Wednesdays, and Saturdays from 05:30 PM to 11:30 PM. The grand River Carnival parade begins at 08:30 PM inside the River Palace Theatre, followed by the enchanting Kingdom of Lights illumination walk."),
            ("Is the Bird of Paradise dinner buffet suitable for vegetarians and halal diners?", "Yes! The Bird of Paradise buffet is one of the largest in Asia, featuring dedicated certified Halal kitchens, extensive vegetarian and Indian counters, Western roast meats, and traditional Thai delicacies prepared fresh."),
            ("Is hotel transfer included in the Carnival Magic package?", "Our all-inclusive package includes round-trip air-conditioned hotel transfers from hotels across Patong, Kata, Karon, Kamala, Bangtao, and Phuket Town directly to the park gates.")
        ]
    },
    "elephant_sanctuary.html": {
        "faqs": [
            ("Does Phuket Elephant Sanctuary permit elephant riding?", "No, absolutely not. Phuket Elephant Sanctuary is a pioneer of ethical elephant tourism in Southern Thailand and enforces a strict 100% no-riding, hands-off observation philosophy. Rescued Asian elephants roam, forage, and bathe freely in natural rainforest surroundings."),
            ("What can visitors do during the ethical sanctuary experience?", "Guests observe retired elephants as they socialize, graze, and swim from a safe distance along Thailand's longest canopy walkway (500 meters). You will prepare nutritious snacks of bananas, watermelons, and pineapples, feed the elephants respectfully, and learn their rescue stories from conservation guides."),
            ("What is the 500-meter canopy walkway?", "The custom-built elevated canopy walkway allows visitors to watch elephants roaming through their natural jungle habitat, ponds, and open grasslands without crowding or disturbing them, providing unmatched 360-degree photography angles."),
            ("Are hotel transfers and meals included in the package?", "Yes, our program includes round-trip air-conditioned transfers from your Phuket hotel, a fresh vegetarian and vegan Thai buffet meal, rain boots/umbrellas if needed, and comprehensive travel accident insurance.")
        ]
    },
    "james_bond_island_speedboat_tour.html": {
        "faqs": [
            ("What are the main sights visited on the James Bond Island excursion?", "This iconic day trip takes you through Phang Nga Bay National Park to visit Koh Tapu (the 20-meter needle-shaped limestone karst featured in 'The Man with the Golden Gun'), Khao Ping Kan (leaning rock), sea-cave canoeing at Koh Hong or Koh Panak, and the Muslim floating stilt village at Koh Panyee."),
            ("Is sea-cave canoeing included and who paddles the canoe?", "Yes, sea canoeing through hidden sea lagoons and limestone caves (hong) is fully included! Experienced local paddle guides steer each inflatable two-person canoe, so you can sit back, relax, and take stunning photographs."),
            ("Are National Park admission fees included in the tour price?", "Yes, official Ao Phang Nga National Park entrance fees (typically 300 THB for adults and 150 THB for children) are completely included in our guided package with zero hidden surcharges at the pier."),
            ("What lunch is provided at the Koh Panyee floating village?", "Guests enjoy a fresh, delicious buffet lunch served at a covered waterside restaurant on Koh Panyee stilt village, featuring freshly prepared Thai seafood, halal chicken, stir-fried vegetables, and vegetarian options.")
        ]
    },
    "phi_phi_island_and_khai_island_tour.html": {
        "faqs": [
            ("What is the itinerary for the Phi Phi & Khai Islands tour?", "Cruising by modern speedboat, you will visit world-famous Maya Bay (filming location of 'The Beach'), Pileh Lagoon for emerald swimming, Viking Cave to view swiftlet bird nests, Monkey Beach, enjoy a buffet lunch on Phi Phi Don, and finish with shallow snorkeling among colorful fish at tranquil Khai Nok Island."),
            ("Can visitors swim at Maya Bay?", "Maya Bay allows visitors to walk onto the pristine white-sand beach and take photos. However, swimming in the bay itself is restricted by marine national park authorities to protect the recovering blacktip reef shark population and coral reefs. Swimming is encouraged at nearby Pileh Lagoon!"),
            ("Are snorkeling masks and life vests provided?", "Yes, sanitized snorkeling masks, clean snorkels, and certified safety life vests in adult and child sizes are provided free of charge for all passengers."),
            ("How long is the speedboat journey from Phuket to Phi Phi?", "The modern twin- or triple-engine speedboat crossing from Phuket's eastern marina (Rassada or Royal Phuket Marina) to the Phi Phi archipelago takes approximately 45 to 60 minutes across scenic open waters.")
        ]
    },
    "phuket_fantasea_show.html": {
        "faqs": [
            ("What is Phuket FantaSea and what does the evening include?", "Phuket FantaSea is a 60-acre cultural theme park in Kamala celebrating Thai mythology and folklore. The package includes admission to the Festival Village carnival shopping street, the magnificent Golden Kinnaree 4,000-seat royal buffet restaurant, and the 70-minute 'Fantasy of a Kingdom' theatrical stage show inside the Palace of the Elephants theatre."),
            ("What is the 'Fantasy of a Kingdom' stage show?", "Staged inside an ancient Khmer-style stone palace, the show combines classical Thai cultural dance, aerial acrobatics, pyrotechnics, illusions, and 4D special effects portraying the legends of Prince Kamala."),
            ("What time does the park open and when does the show start?", "The park and Festival Village open at 05:30 PM, the Golden Kinnaree buffet dinner is served from 06:00 PM to 08:30 PM, and the grand theatre performance begins promptly at 09:00 PM (gates close at 08:50 PM)."),
            ("Are cameras allowed inside the theatre?", "Photography and video recording devices (including mobile phones) are strictly prohibited inside the Palace of the Elephants theatre to protect intellectual property and animal safety. Free secure cloakroom lockers are provided in the theatre lobby.")
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
    filepath = os.path.join(PHUKET_DIR, filename)
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
