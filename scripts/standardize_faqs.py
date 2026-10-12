import os
import re
import glob
import json

DOCS_DIR = 'docs'

DEST_NAMES = {
    'bangkok': 'Bangkok',
    'pattaya': 'Pattaya',
    'phuket': 'Phuket',
    'krabi': 'Krabi',
    'chiang_mai': 'Chiang Mai',
    'chiang_rai': 'Chiang Rai',
    'koh_samui': 'Koh Samui',
    'phi_phi_island': 'Phi Phi Islands',
    'ayutthaya': 'Ayutthaya',
    'hua_hin': 'Hua Hin',
    'koh_samet': 'Koh Samet',
    'koh_phangan': 'Koh Phangan',
    'koh_larn': 'Koh Larn (Coral Island)',
    'koh_yao_yai': 'Koh Yao Yai',
    'koh_mook': 'Koh Mook',
    'trang': 'Trang',
    'buddha': 'Sacred Buddha Circuit',
    'andaman': 'Andaman Islands',
    'india': 'India',
    'vietnam': 'Vietnam',
    'thailand': 'Thailand'
}

def clean_text(html_text):
    text = re.sub(r'<[^>]+>', '', html_text)
    return ' '.join(text.split())

def build_faq_html(subtitle, qa_pairs, faq_id="faq"):
    items_html = []
    for i, (q, a) in enumerate(qa_pairs):
        open_attr = ' open' if i == 0 else ''
        q_clean = q.strip()
        a_clean = a.strip()
        if not a_clean.startswith('<p'):
            a_clean = f'<p>{a_clean}</p>'
        
        item = f'''            <details class="faq-item"{open_attr}>
              <summary class="faq-question"><span>{q_clean}</span><span class="faq-chevron" aria-hidden="true">▾</span></summary>
              <div class="faq-answer">{a_clean}</div>
            </details>'''
        items_html.append(item)
    
    items_joined = '\n'.join(items_html)
    return f'''      <!-- FAQ Section -->
      <section class="section alt faq-section" id="{faq_id}">
        <div class="container">
          <div class="section-title">
            <h2>Frequently Asked Questions</h2>
            <p class="subtitle">{subtitle}</p>
          </div>
          <div class="faq-container">
{items_joined}
          </div>
        </div>
      </section>'''

def build_faq_jsonld(qa_pairs):
    main_entity = []
    for q, a in qa_pairs:
        q_text = clean_text(q)
        a_text = clean_text(a)
        main_entity.append({
            "@type": "Question",
            "name": q_text,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a_text
            }
        })
    
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": main_entity
    }
    return f'''    <script type="application/ld+json">
{json.dumps(schema, indent=6)}
    </script>'''

def update_file(file_path, subtitle, qa_pairs, faq_id="faq"):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_faq_html = build_faq_html(subtitle, qa_pairs, faq_id=faq_id)
    new_jsonld = build_faq_jsonld(qa_pairs)
    
    # Check if file has an existing FAQ section
    existing_sec_m = re.search(r'<section[^>]*id=[\"\'][^\"\']*faq[^\"\']*[\"\'][^>]*>.*?</section>', content, re.DOTALL | re.I)
    if not existing_sec_m:
        existing_sec_m = re.search(r'<section[^>]*>(?:(?!</section>).)*?Frequently Asked Questions.*?</section>', content, re.DOTALL | re.I)
    
    if existing_sec_m:
        content = content[:existing_sec_m.start()] + new_faq_html + content[existing_sec_m.end():]
    else:
        # Place right before CTA section
        cta_m = re.search(r'<section class=[\"\']section cta[\"\']', content, re.I)
        if cta_m:
            idx = cta_m.start()
            content = content[:idx] + new_faq_html + '\n\n      ' + content[idx:]
        else:
            footer_m = re.search(r'<footer', content, re.I)
            if footer_m:
                idx = footer_m.start()
                content = content[:idx] + new_faq_html + '\n\n      ' + content[idx:]
            else:
                return False
                
    # Update or insert FAQPage JSON-LD
    faq_jsonld_m = re.search(r'<script type=[\"\']application/ld\+json[\"\']>\s*\{[^{]*?\"@type\"\s*:\s*\"FAQPage\".*?</script>', content, re.DOTALL | re.I)
    if faq_jsonld_m:
        content = content[:faq_jsonld_m.start()] + new_jsonld.strip() + content[faq_jsonld_m.end():]
    else:
        body_end_m = re.search(r'</body>', content, re.I)
        if body_end_m:
            idx = body_end_m.start()
            content = content[:idx] + new_jsonld + '\n  ' + content[idx:]
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

# 1. Update the 19 existing pages by converting their existing Q&As
existing_19 = [
    'docs/transfers.html', 'docs/index.html', 'docs/day-trips.html', 'docs/sightseeing.html',
    'docs/services.html', 'docs/land-packages.html', 'docs/packages/india/index.html',
    'docs/packages/india/andaman/index.html', 'docs/packages/india/buddha/index.html',
    'docs/packages/thailand/index.html', 'docs/packages/thailand/koh_samui/index.html',
    'docs/packages/thailand/pattaya/index.html', 'docs/packages/thailand/phuket/index.html',
    'docs/packages/thailand/krabi/index.html', 'docs/packages/thailand/krabi/sightseeing.html',
    'docs/packages/thailand/chiang_mai/index.html', 'docs/packages/thailand/chiang_rai/index.html',
    'docs/packages/thailand/bangkok/index.html', 'docs/packages/vietnam/index.html'
]

print("Standardizing existing 19 pages...")
for p in existing_19:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract subtitle
    sub_m = re.search(r'<h2>[^<]*Frequently Asked Questions[^<]*</h2>\s*<p class=[\"\']subtitle[\"\']>([^<]+)</p>', content, re.I)
    subtitle = sub_m.group(1).strip() if sub_m else "Frequently asked questions and helpful travel details"
    
    # Extract existing Q&As
    sec_m = re.search(r'<section[^>]*>(?:(?!</section>).)*?Frequently Asked Questions.*?</section>', content, re.DOTALL | re.I)
    if sec_m:
        sec = sec_m.group(0)
        qa_pairs = re.findall(r'<h3[^>]*>(.*?)</h3>\s*<p[^>]*>(.*?)</p>', sec, re.DOTALL)
        if qa_pairs:
            cleaned_qa = [(re.sub(r'<[^>]+>', '', q).strip(), a.strip()) for q, a in qa_pairs]
            update_file(p, subtitle, cleaned_qa)
            print(f"  [Updated] {p} ({len(cleaned_qa)} FAQs)")

print("Existing 19 pages successfully converted to standardized accordion.")

# 2. Add destination hubs FAQs
DESTINATION_HUBS_FAQS = {
    'docs/packages/thailand/phi_phi_island/index.html': (
        "Quick facts on island hopping, Maya Bay, ferry transfers, and national park fees",
        [
            ("How do I travel to the Phi Phi Islands from Phuket or Krabi?",
             "The Phi Phi Islands are accessible via passenger ferries (approx. 1.5 to 2 hours) or fast speedboats (approx. 45 to 60 minutes) departing daily from Rassada Pier in Phuket and Klong Jilad Pier in Krabi. Trippovention coordinates seamless hotel pickups, pier transfers, and ferry tickets."),
            ("What are the must-see highlights and activities on Phi Phi?",
             "Key attractions include world-famous Maya Bay on Phi Phi Leh, the stunning emerald waters of Pileh Lagoon, Viking Cave, Monkey Beach, and the panoramic Phi Phi Don Viewpoint. We offer full-day island hopping tours, sunset cruises, and private longtail charters."),
            ("Are national park entrance fees included in Phi Phi tours?",
             "Phi Phi Leh is part of Hat Noppharat Thara-Mu Ko Phi Phi National Park. The foreign visitor entrance fee is THB 400 per adult and THB 200 per child. Depending on your customized quote, this can be prepaid or settled directly at the national park ranger station."),
            ("How do I request a quotation or customized Phi Phi package?",
             "Click 'Request Custom Quote' or message our team on WhatsApp (+66 90 917 7601). We will verify boat schedules and resort availability for your travel dates and provide a detailed quotation.")
        ]
    ),
    'docs/packages/thailand/ayutthaya/index.html': (
        "Essential details on UNESCO historical temple tours, day trips, and transfers from Bangkok",
        [
            ("What are the most famous temple ruins to visit in Ayutthaya?",
             "Must-see historic sites include Wat Mahathat (famous Buddha head entwined in banyan tree roots), Wat Phra Si Sanphet (royal chedis), Wat Chaiwatthanaram (scenic riverside temple), and the giant reclining Buddha at Wat Lokayasutharam."),
            ("How long does a day trip from Bangkok to Ayutthaya take?",
             "Ayutthaya is located approximately 80 km north of Bangkok (about 1 to 1.5 hours by private air-conditioned vehicle). Our day tours typically run 7 to 8 hours, including hotel transfers, guided temple exploration, and an authentic local lunch."),
            ("What is the dress code for visiting Ayutthaya historical temples?",
             "As active sacred sites, modest dress is strictly enforced: shoulders and knees must be fully covered (no sleeveless shirts, short skirts, or ripped clothing). Comfortable walking shoes and sun protection are strongly recommended."),
            ("How do I book a private Ayutthaya tour or transfer?",
             "Click 'Get Custom Quote' or contact us via WhatsApp (+66 90 917 7601). We provide private vehicle options (sedans, SUVs, luxury VIP minivans) with licensed English-speaking guides and door-to-door Bangkok hotel pickup.")
        ]
    ),
    'docs/packages/thailand/hua_hin/index.html': (
        "Helpful insights on seaside holidays, royal heritage, Bangkok transfers, and attractions",
        [
            ("How far is Hua Hin from Bangkok and what transfer options are available?",
             "Hua Hin is approximately 200 km southwest of Bangkok (around 2.5 to 3 hours drive). Trippovention provides private door-to-door vehicle transfers from Suvarnabhumi Airport (BKK), Don Mueang Airport (DMK), or Bangkok hotels with professional drivers."),
            ("What are the top attractions and activities in Hua Hin?",
             "Key highlights include the iconic Hua Hin Railway Station, the royal Mrigadayavan Palace, Khao Takiab (Monkey Mountain), Cicada Weekend Night Market, and day trips to Phraya Nakhon Cave in Khao Sam Roi Yot National Park and Monsoon Valley Vineyard."),
            ("Is Hua Hin suitable for family vacations and senior travelers?",
             "Hua Hin is one of Thailand's most peaceful coastal destinations, known for calm shallow beaches, family waterparks like Vana Nava, world-class golf courses, and accessible luxury beachfront resorts, making it ideal for relaxed family and multi-generational holidays."),
            ("Can I combine Hua Hin with Bangkok in a single holiday package?",
             "Yes! We offer popular multi-day twin-destination itineraries combining vibrant Bangkok sightseeing with relaxing beach stays in Hua Hin, inclusive of private intercity transfers, handpicked hotels, and curated excursions.")
        ]
    ),
    'docs/packages/thailand/koh_samet/index.html': (
        "Quick facts on white sand beaches, Ban Phe pier transfers, and national park guidelines",
        [
            ("How do I get to Koh Samet from Bangkok or Pattaya?",
             "Travel to Ban Phe Pier in Rayong by private vehicle (approx. 2.5 hours from Bangkok, 1 hour from Pattaya), followed by a 15-minute speedboat or 35-minute ferry transfer directly to the island's beaches. Trippovention manages the complete end-to-end transfer."),
            ("What is Koh Samet best known for?",
             "Koh Samet is celebrated for its powder-soft white sand beaches (such as Sai Kaew Beach and Ao Phai), clear turquoise waters, beachfront dining with evening fire shows, and being one of Thailand's sunniest islands with low rainfall throughout the year."),
            ("Are national park fees payable on Koh Samet?",
             "Yes, Koh Samet is part of Khao Laem Ya-Mu Ko Samet National Park. Foreign visitors pay an entry fee (THB 200 per adult, THB 100 per child) upon arrival at the island pier, which remains valid for the duration of your stay."),
            ("How can I request a customized Koh Samet holiday?",
             "Submit an enquiry through our contact form or chat with our destination team on WhatsApp (+66 90 917 7601). We arrange boutique beach resort bookings, private transfers, and island activities with manual confirmation.")
        ]
    ),
    'docs/packages/thailand/koh_phangan/index.html': (
        "Essential facts on island exploration, ferry routes, beaches, and custom travel packages",
        [
            ("How do I travel to Koh Phangan?",
             "Most travelers fly into Koh Samui or Surat Thani, followed by a high-speed catamaran or ferry (approx. 30 minutes from Koh Samui; 2.5 hours from Surat Thani) arriving at Thong Sala Pier. Trippovention coordinates combined flight, pier, and ferry connections."),
            ("What is there to do on Koh Phangan beyond the Full Moon Party?",
             "Beyond Haad Rin, northern and eastern Koh Phangan (Thong Nai Pan, Haad Yao, Bottle Beach) offers pristine secluded beaches, yoga and wellness retreats, coral reef diving, and scenic hiking to Than Sadet Waterfall."),
            ("Can Koh Phangan be combined with Koh Samui and Koh Tao?",
             "Yes, island-hopping itineraries connecting Koh Samui, Koh Phangan, and Koh Tao are among our most popular Gulf of Thailand packages. We manage all inter-island ferries, private island transport, and hotel reservations."),
            ("How do I get a custom quote for Koh Phangan?",
             "Contact our team via our query form or WhatsApp with your travel dates and preferred island zone. We will verify resort availability and ferry schedules to deliver your tailored itinerary.")
        ]
    ),
    'docs/packages/thailand/koh_larn/index.html': (
        "Helpful information on Pattaya speedboat transfers, water sports, and Coral Island day tours",
        [
            ("How do I reach Koh Larn from Pattaya?",
             "Speedboats departing from Pattaya Bali Hai Pier reach Koh Larn in just 15 to 20 minutes, while local passenger ferries take about 40 to 45 minutes to arrive at Tawaen Beach or Na Baan Pier. Trippovention provides private speedboat day tours with hotel pickup."),
            ("What activities are available on Koh Larn?",
             "Popular activities include parasailing, sea walking, banana boat rides, jet skiing, snorkeling in clear waters, and relaxing on scenic beaches like Tawaen Beach, Tien Beach, and Samae Beach."),
            ("Are water sports and lunches included in the Coral Island day trip?",
             "Our standard Coral Island tour includes roundtrip speedboat transfers, life jackets, and a beachside Indian or international lunch. Parasailing, sea walking, and banana boat activities can be packaged in advance or chosen on-site."),
            ("How do I enquire about a Koh Larn day excursion?",
             "Click 'Request Custom Quote' or chat on WhatsApp (+66 90 917 7601). Inform us of your group size and date, and we will share available departure times and quote options.")
        ]
    ),
    'docs/packages/thailand/koh_yao_yai/index.html': (
        "Important details on Phang Nga Bay speedboats, luxury eco-resorts, and serene island life",
        [
            ("Where is Koh Yao Yai and how do you get there?",
             "Koh Yao Yai is an unspoiled island nestled in Phang Nga Bay halfway between Phuket and Krabi. It is reachable via a 30-minute speedboat from Bang Rong Pier in Phuket or Ao Nang/Tha Len Pier in Krabi."),
            ("What makes Koh Yao Yai a unique destination?",
             "Koh Yao Yai offers tranquil, unhurried island life with traditional fishing villages, rubber plantations, secluded white sand sandbanks (Laem Had Beach), and stunning luxury eco-resorts with views across Phang Nga limestone karsts."),
            ("Is Koh Yao Yai suitable for honeymoons and couples?",
             "Absolutely. The island is celebrated for its quiet luxury, private pool villas, untouched beaches, and privacy away from mass tourist crowds, making it one of Thailand's finest romantic retreats."),
            ("How can I plan a Koh Yao Yai stay with Trippovention?",
             "Contact our travel specialists with your dates. We arrange private airport transfers, luxury speedboat crossings, and handpicked villa stays with personalized offline confirmation.")
        ]
    ),
    'docs/packages/thailand/koh_mook/index.html': (
        "Essential travel facts on the Emerald Cave, Trang island transfers, and tide schedules",
        [
            ("What is the main highlight of visiting Koh Mook?",
             "Koh Mook is world-renowned for the magical Emerald Cave (Tham Morakot). Visitors swim through an 80-meter dark sea tunnel guided by torchlight, emerging into a breathtaking hidden lagoon surrounded by towering vertical limestone cliffs."),
            ("How do you get to Koh Mook?",
             "Koh Mook is reached via a 30-minute longtail boat or 15-minute speedboat from Kuan Tung Ku Pier in Trang, or via island-hopping speedboats connecting Koh Lanta, Koh Ngai, and Koh Kradan."),
            ("When is the best time to visit the Emerald Cave?",
             "The cave can only be safely entered during mid-tide when water levels permit swimming through the entrance tunnel. Our experienced local captains time visits specifically according to daily tide tables for optimal safety and daylight."),
            ("How do I request a Koh Mook & Trang island holiday?",
             "Submit your inquiry through our contact form. Our team will verify boat schedules and eco-resort availability to provide a comprehensive quotation.")
        ]
    ),
    'docs/packages/thailand/trang/index.html': (
        "Practical guide on Trang Andaman islands, breakfast food culture, and southern road transfers",
        [
            ("What travel experiences does Trang offer?",
             "Trang province in southern Thailand is famous for its pristine Andaman islands (Koh Mook, Koh Kradan, Koh Ngai), underwater wedding heritage, lush botanical gardens, prehistoric caves (Tham Le Khao Kob), and its legendary breakfast food culture."),
            ("How do I travel to Trang?",
             "Domestic flights operate daily from Bangkok Don Mueang (DMK) to Trang Airport (TST). Alternatively, private road transfers from Krabi take approximately 2 hours, connecting directly to Trang town and island piers."),
            ("Can Trang be combined with Krabi and Phuket?",
             "Yes! We specialize in Southern Thailand island odysseys that seamlessly link Phuket, Krabi, and Trang via private vehicles and speedboats, showcasing both famous landmarks and hidden gems."),
            ("How do I get in touch to book a Trang itinerary?",
             "Reach out to our team via WhatsApp (+66 90 917 7601) or our contact page. We will build a customized travel itinerary with transparent pricing and manual voucher fulfillment.")
        ]
    ),
    'docs/destinations.html': (
        "Answers to common questions about our destination coverage across Thailand, India, and Vietnam",
        [
            ("Which destinations does Trippovention specialize in?",
             "Trippovention specializes in comprehensive ground operations and curated tour packages across Thailand (16 top destinations), Incredible India (golden triangle, sacred Buddhist circuits, and Andaman islands), and Vietnam (Hanoi, Halong Bay, Da Nang, and Phu Quoc)."),
            ("How do I choose the best destination for my travel style?",
             "Explore our curated categories by theme (honeymoon, family, adventure, relaxation) or by traveler type. If you are uncertain which destination fits your dates and budget, contact our destination team for tailored recommendations."),
            ("Can I combine multiple countries in one itinerary?",
             "Yes! We create multi-country Southeast Asia itineraries, combining Thailand with Vietnam, or India pilgrimage packages with leisure beach extensions, managing all private road transfers, domestic flights, and local guides."),
            ("How do I get a custom multi-destination quotation?",
             "Click 'Request Custom Quote' or message our specialists on WhatsApp (+66 90 917 7601). We will design a custom itinerary with verified hotel options and transparent pricing.")
        ]
    ),
    'docs/destinations-themes.html': (
        "Helpful insights on our theme-based travel packages, customization, and group itineraries",
        [
            ("What travel themes can I choose from on Trippovention?",
             "We offer handcrafted itineraries tailored to specific travel styles including Romantic Honeymoon getaways, Action & Adventure escapes, Family-Friendly holidays, Spiritual & Heritage tours, and Island Hopping retreats."),
            ("Can thematic itineraries be personalized for our group?",
             "Yes, 100%. Every theme is fully customizable. We can adjust activity intensity, hotel tiers, private transport, and meal preferences (such as Pure Vegetarian, Jain, or Halal dining) to suit your party."),
            ("Are activities, entrance tickets, and guides included in themed packages?",
             "Our themed packages include curated activities, verified attraction admissions, and licensed English-speaking local guides as detailed in each itinerary. Check specific inclusions or request a tailored quotation."),
            ("How do I check availability for a themed holiday?",
             "Submit an inquiry through our contact form or chat with us on WhatsApp (+66 90 917 7601). Our team will verify seasonal availability and deliver your custom proposal.")
        ]
    ),
    'docs/destinations-travelers.html': (
        "Everything you need to know about tailoring trips for families, couples, groups, and seniors",
        [
            ("What traveler categories does Trippovention design packages for?",
             "We offer dedicated holiday packages tailored for Families with Kids, Couples & Honeymooners, Groups of Friends, Solo Travelers, and Senior Citizens, with accommodations and pacing matched to each demographic."),
            ("What makes your family packages kid-friendly and safe?",
             "Our family packages feature spacious family-friendly resorts, child-appropriate attraction tickets (waterparks, wildlife sanctuaries, theme parks), private vehicles with courteous drivers, and relaxed pacing without rushed schedules."),
            ("Do you provide accessible transport and gentle pacing for senior travelers?",
             "Yes. Our senior travel itineraries prioritize ground-floor or elevator-accessible hotels, minimal walking steps, private air-conditioned transport with luggage assistance, and unhurried daily schedules."),
            ("How can I request a quotation for our specific travel group?",
             "Contact us via our website form or WhatsApp (+66 90 917 7601) specifying your group composition (adults, children, seniors). Our team will tailor the ideal itinerary and share a transparent quote.")
        ]
    ),
    'docs/contact.html': (
        "Common questions about contacting our team, response times, and booking workflow",
        [
            ("How quickly will your team respond to my travel enquiry?",
             "Our destination specialists review and respond to inquiries within 24 business hours. For immediate assistance or urgent travel dates, message our team directly via WhatsApp (+66 90 917 7601)."),
            ("Where is Trippovention's Thailand office located?",
             "Our Thailand headquarters is located in Chonburi Province (23/13 M, 12 Nong Pure Subdistrict, Bang Lamung District), supporting ground operations across Bangkok, Pattaya, Phuket, and Krabi, alongside our established operations base in India."),
            ("How does Trippovention's offline booking process work?",
             "Browse our product catalog online, submit an inquiry or WhatsApp message with your travel dates and preferences, receive a personalized quotation from our team, and finalize booking details and payment through secure offline confirmation."),
            ("Can I request custom changes to itineraries and transfers?",
             "Yes, absolutely. All holiday packages, day excursions, and private transfer routes can be fully customized according to your group size, hotel preferences, and schedule.")
        ]
    )
}

print("Adding FAQs to destination hubs and thematic pages...")
for path, (sub, qas) in DESTINATION_HUBS_FAQS.items():
    if os.path.exists(path):
        update_file(path, sub, qas)
        print(f"  [Added] {path}")

print("Destination hubs and thematic pages completed.")

# 3. Add FAQs to all 149 individual product detail pages
print("Processing 149 individual product detail pages...")

exclude_files = set(existing_19 + list(DESTINATION_HUBS_FAQS.keys()) + [
    'docs/404.html', 'docs/offline.html', 'docs/thank-you.html',
    'docs/privacy-policy.html', 'docs/terms-and-conditions.html',
    'docs/refund-policy.html', 'docs/search.html'
])

all_html = glob.glob('docs/**/*.html', recursive=True)
product_count = 0

for p in all_html:
    if p in exclude_files:
        continue
    
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Extract H1
    h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', c, re.DOTALL)
    title = clean_text(h1_m.group(1)) if h1_m else "Tour Package"
    # Clean redundant suffixes
    title = re.sub(r'\s*\|\s*Trippovention.*$', '', title).strip()
    
    # Destination from path
    parts = p.split('/')
    dest_key = parts[3] if len(parts) > 4 else parts[2] if len(parts) > 3 else 'thailand'
    dest_name = DEST_NAMES.get(dest_key, dest_key.replace('_', ' ').title())
    
    # Classify product type
    is_multi_day = bool(re.search(r'<h3>Day\s*1\b|<h4>Day\s*1\b|Days\s*/\s*\d+\s*Nights', c, re.I))
    is_attraction = bool(re.search(r'Operating Hours|Last Admission|Show Time|Cruise Schedule|Ticket Options', c, re.I))
    
    if is_attraction:
        sub = f"Practical visiting information and booking details for {title}"
        qas = [
            (f"What is included with admission to {title}?",
             f"Admission includes access to the attraction's main exhibits, themed zones, or scheduled entertainment as outlined under 'What\'s Included'. Meals, retail merchandise, and personal expenses are excluded unless explicitly specified in the package description."),
            (f"Are hotel transfers included with this attraction ticket?",
             f"Unless explicitly booked as an inclusive tour with transport, standard admission tickets do not include hotel transfers. Private or shared roundtrip transfers from your hotel in {dest_name} can be added to your custom quote upon request."),
            (f"What are the operating hours and recommended duration for {title}?",
             f"Operating schedules vary by attraction. Most guests spend between 1 to 3 hours enjoying the experiences and taking photos. Please check the visiting details section above or ask our team for recommended visit time slots."),
            (f"How do I check ticket availability and request a quotation?",
             f"Click 'Request Custom Quote' or message us on WhatsApp (+66 90 917 7601) with your preferred visit date and number of tickets. Our team will verify slot availability and share current promotional rates.")
        ]
    elif is_multi_day:
        sub = f"Everything you need to know about the {title} holiday package"
        qas = [
            (f"What is included in this {title} package?",
             f"This curated holiday package includes verified hotel accommodations with daily breakfast, private or scheduled airport transfers, intercity transport, and guided sightseeing tours as detailed in the daily itinerary. International airfare, personal travel insurance, and optional activities are excluded."),
            (f"Can this itinerary, hotel category, and duration be customized?",
             f"Yes, 100%. All Trippovention packages can be tailored to match your specific travel dates, preferred hotel tier (3-star, 4-star, or 5-star luxury), travel pacing, and special dietary requirements (including Indian Vegetarian, Jain, or Halal dining)."),
            (f"How do I request a custom quotation and check dates?",
             f"Click 'Get Custom Quote' or message our destination specialists on WhatsApp (+66 90 917 7601). Share your travel dates and traveler count, and we will verify hotel and vehicle availability to provide a customized proposal within 24 hours."),
            (f"How are bookings confirmed and payments handled?",
             f"Trippovention operates via an offline quotation model. Once you approve your tailored itinerary and quote, our team provides payment instructions (bank transfer or secure payment link) and issues your formal confirmation vouchers.")
        ]
    else: # day_trip
        sub = f"Essential information for your {title} in {dest_name}"
        qas = [
            (f"What is included in the {title}?",
             f"This day tour typically includes roundtrip transport, licensed English-speaking guidance, safety equipment (such as life jackets and snorkeling gear for marine tours), drinking water, and lunch where stated in the itinerary. National park entry fees may be included or paid on-site."),
            (f"Where is the pickup point and what time does the tour start?",
             f"Complimentary shared or private hotel pickup is available from central hotels across {dest_name}. Your exact pickup time and driver contact will be reconfirmed in your booking voucher prior to departure."),
            (f"What items should I bring on this excursion?",
             f"We recommend bringing swimwear, a towel, sunscreen, sunglasses, comfortable walking or water shoes, a waterproof bag for mobile devices, and local Thai Baht cash for national park fees or personal souvenirs."),
            (f"How do I check availability and confirm my tour reservation?",
             f"Click 'Get Custom Quote' or contact our destination team via WhatsApp (+66 90 917 7601). We will verify sea conditions and vehicle availability for your date and guide you through our straightforward offline booking process.")
        ]
    
    ok = update_file(p, sub, qas)
    if ok:
        product_count += 1

print(f"Processed and updated {product_count} product detail pages with tailored FAQs and JSON-LD.")
