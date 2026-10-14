#!/usr/bin/env python3
"""
Generate individual detail pages for the 19 new Bangkok sightseeing tours.
Follows Trippovention design system, typography, SEO metadata, breadcrumbs, 
genuine Bangkok-specific FAQs, and schema.
"""

import os

DEST_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "packages", "thailand", "bangkok")

TOURS_DATA = [
    {
        "filename": "grand_palace_and_wat_phra_kaew_tour.html",
        "title": "Grand Palace & Wat Phra Kaew Tour Bangkok | Trippovention",
        "h1": "Grand Palace & Wat Phra Kaew Tour",
        "subtitle": "Royal Grandeur, Sacred Emerald Buddha & Golden Stupas of Siam's Royal Court",
        "meta_desc": "Explore Bangkok's Grand Palace and Wat Phra Kaew (Temple of the Emerald Buddha) with a licensed guide. Discover Thai royal history and intricate temple art.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_grand_palace.webp",
        "duration": "3–4 Hours",
        "price": "THB 1,450",
        "price_note": "(Per Person)",
        "meetup": "Central Bangkok Hotel Pickup or Grand Palace Gate Meeting Point",
        "overview_p1": "Step into the spiritual and ceremonial heart of the Kingdom of Thailand at the Grand Palace, established in 1782 by King Rama I. Marvel at the dazzling golden chedis, multi-tiered spires, and elaborate mural paintings depicting the Ramakien epic along the royal cloisters.",
        "overview_p2": "Within the complex stands Wat Phra Kaew, home to the revered Emerald Buddha (Phra Kaew Morakot), carved from a single block of jadeite. Accompanied by a knowledgeable licensed guide, you will learn the royal rituals, architectural symbolism, and strict customs governing this sacred national sanctuary.",
        "places_col1_title": "Grand Palace Grounds",
        "places_col1_badge": "Royal Architecture",
        "places_col1_items": [
            ("Chakri Maha Prasat Hall", "Iconic royal throne hall blending 19th-century European neoclassical architecture with traditional Thai tiered roofs."),
            ("Dusit Maha Prasat Hall", "Exquisite ceremonial hall used for royal coronation ceremonies and lying-in-state services."),
            ("Royal Cloister Murals", "Over 2 kilometers of masterfully restored historic murals illustrating the complete Thai Ramakien epic.")
        ],
        "places_col2_title": "Wat Phra Kaew Sanctuary",
        "places_col2_badge": "Sacred Landmark",
        "places_col2_items": [
            ("The Emerald Buddha", "Thailand's most venerated Buddhist relic, adorned in seasonal royal gold garments changed by the King."),
            ("Phra Si Rattana Chedi", "Towering gilded stupa enshrining holy relics of the Buddha, glistening in the Bangkok sun."),
            ("Model of Angkor Wat", "Intricate scale model commissioned by King Rama IV celebrating classical Khmer temple architecture.")
        ],
        "inclusions": [
            "Official admission ticket to Grand Palace & Temple of the Emerald Buddha",
            "Licensed English-speaking professional tour guide",
            "Shared air-conditioned transfer or private transport (based on package)",
            "Chilled bottled drinking water",
            "Comprehensive traveler accident insurance"
        ],
        "exclusions": [
            "Dress code clothing rentals (temple requires shoulders and ankles covered)",
            "Personal spending, food and refreshments",
            "Gratuities and tips for guide and driver"
        ],
        "timing_text": "Morning Departures (08:30 AM – 12:00 PM) or Afternoon Departures (01:00 PM – 04:30 PM).<br />Palace gates strictly close admissions at 03:30 PM.",
        "transport_text": "Air-conditioned modern minivan or private vehicle transfer from central Bangkok hotels.",
        "what_to_bring": "Modest clothing covering shoulders and knees/ankles (no sleeveless tops, shorts, or tight leggings), slip-on comfortable shoes, sun hat, sunglasses, and camera.",
        "contact_tour_param": "Grand+Palace+and+Wat+Phra+Kaew+Tour",
        "faqs": [
            ("What is the dress code for visiting the Grand Palace?", "The Grand Palace enforces Thailand's strictest dress code. Both men and women must wear shirts with sleeves covering shoulders, and trousers or long skirts covering ankles. Transparent fabric, sleeveless tops, shorts, ripped jeans, and tight sportswear are strictly prohibited."),
            ("Are admission tickets included in the tour price?", "Yes, official entrance tickets to both the Grand Palace and Wat Phra Kaew are included in our guided package price with no hidden costs."),
            ("Can visitors take photos inside Wat Phra Kaew?", "Photography is permitted throughout the open palace courtyards and exterior cloisters, but is strictly prohibited inside the main Ubosot chapel where the Emerald Buddha sits."),
            ("How early should I book my Grand Palace tour?", "We recommend reserving at least 48 to 72 hours in advance during peak season (November to April) to ensure licensed guide availability and preferred morning time slots.")
        ]
    },
    {
        "filename": "wat_pho_and_reclining_buddha_tour.html",
        "title": "Wat Pho & Reclining Buddha Tour Bangkok | Trippovention",
        "h1": "Wat Pho & Reclining Buddha Tour",
        "subtitle": "Colossal 46-Meter Gold Reclining Buddha, Royal Chedis & Birthplace of Traditional Thai Massage",
        "meta_desc": "Visit Wat Pho in Bangkok to see the 46-meter Reclining Buddha, mother-of-pearl soles, 91 royal chedis, and the historic birthplace of traditional Thai massage.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_wat_pho.webp",
        "duration": "2–3 Hours",
        "price": "THB 950",
        "price_note": "(Per Person)",
        "meetup": "Central Bangkok Hotel Lobby or Wat Pho Main Entrance",
        "overview_p1": "Wat Pho (Temple of the Reclining Buddha) is one of Bangkok's oldest, largest, and most serene temple compounds, predating the founding of Bangkok as the capital city. Its highlight is the massive 46-meter-long, 15-meter-high gilded reclining Buddha statue representing Buddha entering Nirvana.",
        "overview_p2": "Beyond the iconic statue, Wat Pho is celebrated as Thailand's first public university and the historical birthplace of traditional Thai massage. Wander past courtyards filled with 91 ceramic stupas (chedis), marble stone inscriptions recognized by UNESCO, and Chinese guardian statues.",
        "places_col1_title": "Temple Treasures",
        "places_col1_badge": "Iconic Art",
        "places_col1_items": [
            ("The Reclining Buddha", "Massive gold-leaf covered image with intricately inlaid mother-of-pearl feet illustrating the 108 auspicious laksanas (marks of the Buddha)."),
            ("108 Bronze Alms Bowls", "Drop bronze coins into 108 holy alms bowls lining the chapel wall to attract good karma and support monastery upkeep."),
            ("Phra Maha Chedi Si Rajakarn", "Four monumental 42-meter stupas tiled in colored mosaics honoring the first four Chakri monarchs.")
        ],
        "places_col2_title": "Heritage & Wellness",
        "places_col2_badge": "Living Heritage",
        "places_col2_items": [
            ("Traditional Thai Massage Pavilion", "World-renowned national massage academy where authentic therapeutic Thai massage is still taught and practiced."),
            ("Hermit Exercise Statues", "Bronze sculptures illustrating classical yoga-like self-healing postures (Ruesi Dat Ton)."),
            ("Phra Ubosot Main Chapel", "Sacred ordination hall featuring gold and crystal Buddha images and exquisite mother-of-pearl doors.")
        ],
        "inclusions": [
            "Official entrance admission ticket to Wat Pho complex",
            "Expert English-speaking licensed cultural guide",
            "Bottled drinking water",
            "Optional hotel pickup and return (based on package choice)",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "On-site massage treatments (available optionally on-site)",
            "Personal souvenirs and offerings",
            "Guide and driver gratuities"
        ],
        "timing_text": "Morning Departures (09:00 AM – 11:30 AM) or Afternoon Departures (01:30 PM – 04:00 PM).<br />Daily operations.",
        "transport_text": "Air-conditioned van transfers or easy meet-up near MRT Sanam Chai station.",
        "what_to_bring": "Modest clothing covering shoulders and knees, slip-on shoes (shoes must be removed when entering temple halls), and camera.",
        "contact_tour_param": "Wat+Pho+and+Reclining+Buddha+Tour",
        "faqs": [
            ("Can I receive a traditional Thai massage at Wat Pho during the visit?", "Yes, Wat Pho is the headquarters for traditional Thai medicine and massage. You can purchase walk-in traditional Thai massage or herbal treatments directly at the massage pavilion inside the temple grounds."),
            ("What is the dress requirement at Wat Pho?", "Visitors must dress respectfully with covered shoulders and knees. Shoes must be removed before stepping onto temple carpets, and shoe bags are provided at chapel entrances."),
            ("Is Wat Pho close to the Grand Palace?", "Yes, Wat Pho is situated directly south of the Grand Palace, separated by just a short 7-minute walk, making them an ideal combined morning excursion."),
            ("Is this tour suitable for seniors and families?", "Yes, Wat Pho features wide, mostly level stone pathways with shaded pavilions and peaceful courtyard gardens suitable for all ages.")
        ]
    },
    {
        "filename": "wat_arun_temple_of_dawn_tour.html",
        "title": "Wat Arun (Temple of Dawn) Tour Bangkok | Trippovention",
        "h1": "Wat Arun – Temple of Dawn Tour",
        "subtitle": "Iconic Riverside Khmer-Style Prang, Porcelain Mosaics & Chao Phraya Cross-River Ferry",
        "meta_desc": "Discover Wat Arun (The Temple of Dawn) in Bangkok. Climb the iconic riverside prang adorned in colorful Chinese porcelain and enjoy Chao Phraya River views.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_wat_arun.webp",
        "duration": "2–3 Hours",
        "price": "THB 850",
        "price_note": "(Per Person)",
        "meetup": "Central Bangkok Hotel Pickup or Tha Tien Pier Crossing",
        "overview_p1": "Perched on the west bank of the Chao Phraya River in Thonburi, Wat Arun Ratchawararam (commonly known as the Temple of Dawn) is one of Thailand's most striking visual landmarks. Named after Aruna, the Hindu god of dawn, its central prang catches the morning sunrise and glows dramatically at twilight.",
        "overview_p2": "Ascend the steep steps of the central 70-meter-high Khmer-style tower, encrusted with thousands of pieces of colorful glazed Chinese porcelain and sea shells that once served as ballast on trade junks. Take in panoramic vistas over the winding Chao Phraya River, the Grand Palace skyline, and historic riverside neighborhoods.",
        "places_col1_title": "Architectural Highlights",
        "places_col1_badge": "Riverside Icon",
        "places_col1_items": [
            ("Central Prang Spire", "Majestic 70-meter tower representing Mount Meru, the center of the universe in Buddhist and Hindu cosmology."),
            ("Glazed Porcelain Mosaics", "Fascinating floral mosaics crafted from antique Chinese ceramics, broken porcelain shards, and seashells."),
            ("Guardian Giants (Yak)", "Two towering mythical daemon sentinels guarding the entrance to the ordination hall.")
        ],
        "places_col2_title": "Cultural Experience",
        "places_col2_badge": "Local Life",
        "places_col2_items": [
            ("Cross-River Ferry Experience", "Short scenic river crossing aboard the traditional wooden commuter ferry between Tha Tien and Wat Arun."),
            ("Thai Traditional Costume Rental", "Popular local photo experience with optional traditional Thai silk outfits available near temple entrance."),
            ("Riverside Ordination Chapel", "Peaceful inner courtyard featuring murals depicting Prince Siddhartha's life.")
        ],
        "inclusions": [
            "Official entrance admission ticket to Wat Arun",
            "Cross-river passenger ferry ticket (Tha Tien to Wat Arun)",
            "Professional English-speaking licensed guide",
            "Bottled cold drinking water",
            "Travel accident insurance"
        ],
        "exclusions": [
            "Optional Thai traditional costume rental photoshoots",
            "Personal refreshments and souvenirs",
            "Gratuities for guide"
        ],
        "timing_text": "Morning (09:00 AM – 11:30 AM) or Sunset Afternoon (03:30 PM – 06:00 PM).<br />Daily departures.",
        "transport_text": "Air-conditioned transfers or scenic river boat arrival via Tha Tien pier.",
        "what_to_bring": "Modest clothing covering shoulders and knees, comfortable walking shoes with good grip for steep steps, and camera.",
        "contact_tour_param": "Wat+Arun+Temple+of+Dawn+Tour",
        "faqs": [
            ("Can you climb the steep steps at Wat Arun?", "Visitors can climb to the first terrace of the central prang for closer inspection of the intricate porcelain tiles and river views. Upper terraces are cordoned off for structural preservation."),
            ("What is the best time of day to visit Wat Arun?", "Early mornings (08:30–10:00 AM) offer cooler temperatures and softer light for photography, while late afternoons allow you to experience the riverside as the sunset casts a golden hue over the river."),
            ("Is traditional Thai costume rental available on-site?", "Yes, numerous licensed costume rental boutiques operate just outside the temple gates offering traditional silk Chut Thai outfits and accessories for photos."),
            ("How do we cross the river to get there?", "Our tour includes the charming local river ferry from Tha Tien pier directly across to the temple dock, offering classic waterfront photo angles along the way.")
        ]
    },
    {
        "filename": "bangkok_temples_and_heritage_tour.html",
        "title": "Bangkok Temples & Heritage Tour | Trippovention",
        "h1": "Bangkok Temples & Cultural Heritage Tour",
        "subtitle": "Wat Traimit (Solid Gold Buddha), Wat Pho Reclining Buddha & Marble Temple Wat Benchamabophit",
        "meta_desc": "Experience Bangkok's most famous temples: the 5.5-ton solid gold Buddha at Wat Traimit, the Reclining Buddha at Wat Pho, and the Italian marble Wat Benchamabophit.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_bangkok_temples_heritage.webp",
        "duration": "4–5 Hours",
        "price": "THB 1,650",
        "price_note": "(Per Person)",
        "meetup": "Central Bangkok Hotel Lobby (Complimentary Pickup)",
        "overview_p1": "Immerse yourself in Bangkok's rich religious heritage and architectural wonders on this curated half-day temple expedition. Discover three of the capital's most significant sanctuaries, each representing a distinct era of royal Thai craftsmanship and Buddhist devotion.",
        "overview_p2": "Stand in awe before the world's largest solid gold Buddha statue at Wat Traimit in Chinatown, witness the majestic 46-meter Reclining Buddha at Wat Pho, and admire the immaculate white Italian Carrara marble architecture of Wat Benchamabophit (The Marble Temple).",
        "places_col1_title": "Chinatown & Old City",
        "places_col1_badge": "Sacred Highlights",
        "places_col1_items": [
            ("Wat Traimit (Golden Buddha)", "Home to the world's largest solid gold statue—weighing 5.5 tons and dating back to the Sukhothai period."),
            ("Yaowarat Gateway", "Scenic drive past Bangkok Chinatown's monumental ceremonial Chinese gate and vibrant goldsmith district."),
            ("Wat Pho Reclining Buddha", "Grand 46-meter gilded Buddha image and historic royal chedis.")
        ],
        "places_col2_title": "Dusit Royal District",
        "places_col2_badge": "Marble Masterpiece",
        "places_col2_items": [
            ("Wat Benchamabophit (Marble Temple)", "Exquisite late-19th-century temple faced with imported white Italian Carrara marble."),
            ("Cloister Gallery of 52 Buddhas", "Open courtyard housing 52 bronze Buddha statues showcasing different Asian artistic periods."),
            ("Government District Drive", "Scenic drive past Ananta Samakhom Throne Hall, Dusit Palace, and Rajadamnern Avenue.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transfers from central Bangkok",
            "Official entrance admission tickets to Wat Traimit, Wat Pho, and Wat Benchamabophit",
            "Licensed English-speaking professional tour guide",
            "Chilled bottled drinking water",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Food, meals and personal spending",
            "Gratuities for guide and driver"
        ],
        "timing_text": "Morning Tour: 08:00 AM – 12:30 PM | Afternoon Tour: 01:00 PM – 05:30 PM.<br />Daily departures.",
        "transport_text": "Round-trip shared air-conditioned minivan or private transport with hotel pickup.",
        "what_to_bring": "Modest clothing covering shoulders and knees/ankles, slip-on shoes, sun hat, and camera.",
        "contact_tour_param": "Bangkok+Temples+and+Heritage+Tour",
        "faqs": [
            ("Are all temple admission tickets included?", "Yes, admission fees for all three temples (Wat Traimit, Wat Pho, and Wat Benchamabophit) are completely included in your package."),
            ("Is hotel pickup available across all Bangkok areas?", "Complimentary pickup is provided for hotels in Sukhumvit (Soi 1–33 & 2–26), Silom, Sathorn, Siam, and Pratunam. Outlying pickups can be arranged for a modest supplement."),
            ("How long do we spend at each temple?", "Typically 45 to 60 minutes at each temple, giving plenty of time for detailed guide explanations, photo opportunities, and respectful contemplation."),
            ("What should I wear for this heritage tour?", "Dress respectfully with covered shoulders and knees. Shorts, sleeveless vests, and short skirts are strictly forbidden at active Buddhist temples.")
        ]
    },
    {
        "filename": "chao_phraya_river_sightseeing_cruise.html",
        "title": "Chao Phraya River Sightseeing Cruise Bangkok | Trippovention",
        "h1": "Chao Phraya River Sightseeing Cruise",
        "subtitle": "Hop-On Hop-Off Chao Phraya Tourist Boat, Riverside Landmarks & Historic Piers",
        "meta_desc": "Cruise the River of Kings in Bangkok with an unlimited hop-on hop-off Chao Phraya day pass. Discover Wat Arun, IconSiam, Grand Palace, and riverside heritage.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_chao_phraya_river_cruise.webp",
        "duration": "2–3 Hours (Or Full Day Pass)",
        "price": "THB 650",
        "price_note": "(Per Person)",
        "meetup": "Sathorn Pier (BTS Saphan Taksin) or any designated Chao Phraya Tourist Boat pier",
        "overview_p1": "Experience the bustling energy of the River of Kings aboard the open-deck Chao Phraya Sightseeing Boat. Cruise smoothly past iconic landmarks, century-old churches, royal temples, modern waterfront skyscrapers, and bustling merchant piers.",
        "overview_p2": "With an unlimited all-day hop-on hop-off boat pass, you can explore Bangkok at your own pace without traffic jams. Hop off at Tha Tien for Wat Pho, Wat Arun Pier for the Temple of Dawn, Tha Chang for the Grand Palace, or IconSiam for world-class waterfront retail.",
        "places_col1_title": "Historic Piers & Temples",
        "places_col1_badge": "Cultural Stops",
        "places_col1_items": [
            ("Tha Maharaj / Tha Chang Pier", "Direct access to Grand Palace, Temple of the Emerald Buddha, and riverside cafes."),
            ("Wat Arun Pier", "Step straight off the boat into the grounds of the majestic Temple of Dawn."),
            ("Tha Tien Pier", "Gateway to Wat Pho Reclining Buddha, rooftop bars, and local street markets.")
        ],
        "places_col2_title": "Modern Riverfronts",
        "places_col2_badge": "Lifestyle Stops",
        "places_col2_items": [
            ("IconSiam Pier", "Award-winning luxury destination featuring the indoor SookSiam floating market and multimedia water fountain show."),
            ("Asiatique The Riverfront Pier", "Lively evening boardwalk with dining, giant Ferris wheel, and night markets."),
            ("Phra Arthit Pier", "Access to bohemian Banglamphu, historic fortresses, and Khao San Road.")
        ],
        "inclusions": [
            "Unlimited All-Day Chao Phraya Tourist Boat Pass (Blue Flag route)",
            "Chao Phraya river route map and guidebook",
            "Onboard English route announcements and safety crew",
            "Life jackets on board all vessels",
            "Travel insurance coverage"
        ],
        "exclusions": [
            "Attraction admission tickets at individual piers",
            "Food, snacks and drinks",
            "Hotel transfers to Sathorn Pier"
        ],
        "timing_text": "Boats operate daily every 30 minutes from 08:30 AM to 06:30 PM.<br />Unlimited boarding throughout operating hours.",
        "transport_text": "Board at Sathorn Central Pier (directly connected to BTS SkyTrain Saphan Taksin Station).",
        "what_to_bring": "Comfortable clothes, sunglasses, sun hat, camera, and Thai Baht cash for shopping at piers.",
        "contact_tour_param": "Chao+Phraya+River+Sightseeing+Cruise",
        "faqs": [
            ("How frequent are the sightseeing boats?", "Chao Phraya Tourist Boats depart approximately every 30 minutes between Sathorn Pier and Phra Arthit Pier throughout the day."),
            ("Where do I collect my boat pass?", "You can present your digital booking confirmation voucher at the ticket booth at Sathorn Central Pier (BTS Saphan Taksin) or Tha Maharaj Pier to collect your physical day pass."),
            ("Can I hop on and off as many times as I want?", "Yes, the All-Day River Pass gives you unlimited rides across all 11 designated tourist piers until 06:30 PM."),
            ("Are boats wheelchair or stroller accessible?", "Most modern catamarans on this route provide wide ramps and designated space for strollers and wheelchairs with crew assistance at major piers.")
        ]
    },
    {
        "filename": "bangkok_canals_private_longtail_boat_tour.html",
        "title": "Bangkok Canals Private Longtail Boat Tour | Trippovention",
        "h1": "Bangkok Canals Private Longtail Boat Tour",
        "subtitle": "Thonburi Khlongs Exploration, Wooden Stilt Houses, Wat Paknam Big Buddha & Artist's House",
        "meta_desc": "Cruise Bangkok's historic Thonburi canals on a private traditional wooden longtail boat. See traditional stilt houses, the giant Wat Paknam Buddha, and Baan Silapin.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_bangkok_longtail_boat_canals.webp",
        "duration": "2 Hours",
        "price": "THB 1,800",
        "price_note": "(Per Person / Private Tour)",
        "meetup": "Sathorn Pier or Tha Tien Pier (Private Captain Meetup)",
        "overview_p1": "Discover why Bangkok was historically hailed as the 'Venice of the East' on this intimate private longtail boat cruise through the timeless canal network (khlongs) of Thonburi on the western bank of the Chao Phraya River.",
        "overview_p2": "Venture into tranquil waterways where life moves at a serene pace. Drift past traditional teakwood stilt houses, floating orchid gardens, and local fruit orchards. Gaze up at the monumental 69-meter-tall golden Buddha at Wat Paknam Phasi Charoen rising dramatically above the waterways.",
        "places_col1_title": "Canal Life & Heritage",
        "places_col1_badge": "Old Bangkok",
        "places_col1_items": [
            ("Thonburi Khlongs", "Labyrinth of serene historical canals untouched by modern roadway expansion."),
            ("Waterfront Stilt Homes", "Authentic glimpse into local everyday life where monks travel by boat and residents fish from wooden docks."),
            ("Bangkok Yai Lock Gate", "Historic hydraulic water lock regulating tide levels between the Chao Phraya and Thonburi canals.")
        ],
        "places_col2_title": "Iconic Landmarks",
        "places_col2_badge": "Spiritual Sights",
        "places_col2_items": [
            ("Wat Paknam Giant Buddha", "Breathtaking waterside views of the 69-meter bronze seated Buddha statue from the canal level."),
            ("Artist's House (Baan Silapin)", "200-year-old wooden canal-side shophouse showcasing traditional Thai puppets, masks, and artisan crafts."),
            ("Wat Khun Chan", "Vibrant temple complex adorned with dramatic Hindu-Buddhist statues along Khlong Dan.")
        ],
        "inclusions": [
            "Exclusive private wooden longtail boat charter for your party",
            "Experienced licensed local boat captain",
            "Certified life jackets for all passengers",
            "Bottled cold drinking water",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Fish feeding bread pellets (available from local dock vendors for 20 THB)",
            "Beverages or snacks at the Artist's House",
            "Hotel road transfers (can be added on request)",
            "Gratuities for boat captain"
        ],
        "timing_text": "Flexible departure times from 08:30 AM to 04:30 PM daily.<br />Morning (09:00 AM) and Late Afternoon (03:30 PM) recommended for cooler light.",
        "transport_text": "Private longtail boat charter departing from Sathorn Pier or Tha Tien Pier.",
        "what_to_bring": "Sunscreen, sunglasses, sun hat, camera, and cash for dockside refreshments.",
        "contact_tour_param": "Bangkok+Canals+Private+Longtail+Boat+Tour",
        "faqs": [
            ("Is the longtail boat tour completely private for my group?", "Yes, this experience is exclusively chartered for your party, ensuring a personalized pace, private seating, and flexibility to pause for photos."),
            ("Will we see the giant Wat Paknam Buddha statue from the boat?", "Yes, cruising past Wat Paknam provides one of Bangkok's most famous and spectacular photo perspectives of the giant 69-meter golden Buddha."),
            ("Is the canal boat tour safe for young children and elderly travelers?", "Yes, all boats are equipped with certified life jackets, travel at moderate speeds along calm inland waters, and provide shaded canvas canopies."),
            ("What happens if it rains during our canal cruise?", "All longtail boats feature protective overhead canvas roofs and clear plastic side rain curtains that can be unrolled immediately in case of tropical showers.")
        ]
    },
    {
        "filename": "white_orchid_river_dinner_cruise.html",
        "title": "White Orchid Chao Phraya Dinner Cruise Bangkok | Trippovention",
        "h1": "White Orchid Chao Phraya Dinner Cruise",
        "subtitle": "International & Seafood Buffet, Live Cabaret Show, 360° Open-Air Deck & Illuminated Sights",
        "meta_desc": "Sail aboard the White Orchid Chao Phraya River Dinner Cruise in Bangkok. Enjoy an international seafood buffet, live cabaret show, music, and illuminated temple views.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_white_orchid_river_cruise.webp",
        "duration": "2 Hours (Evening Cruise)",
        "price": "THB 1,250",
        "price_note": "(Per Person)",
        "meetup": "Asiatique The Riverfront Pier or IconSiam Pier Check-in Counter",
        "overview_p1": "Spend an unforgettable evening aboard the White Orchid River Cruise, one of Bangkok's premier multi-deck dining vessels. Glide along the historic Chao Phraya River as the capital's iconic monuments—including Wat Arun, the Grand Palace, and Rama VIII Bridge—glow under night illumination.",
        "overview_p2": "Indulge in a lavish international and seafood buffet dinner accompanied by live pop music performances and an entertaining onboard classical and cabaret performance. The expansive 360-degree open-air top deck offers unmatched skyline views and refreshing evening river breezes.",
        "places_col1_title": "Dining & Entertainment",
        "places_col1_badge": "Onboard Luxury",
        "places_col1_items": [
            ("International & Seafood Buffet", "Generous selection of grilled river prawns, fresh sushi, Thai curries, Western dishes, and tropical desserts."),
            ("Live Cabaret & Thai Dance", "Dazzling onboard performance featuring graceful classical Thai dance and vibrant cabaret entertainment."),
            ("Live Musical Duo", "Talented live musicians performing romantic ballads and popular international hits throughout dinner.")
        ],
        "places_col2_title": "Nighttime Landmarks",
        "places_col2_badge": "Illuminated Views",
        "places_col2_items": [
            ("Illuminated Wat Arun", "Gaze up at the glowing golden spire of the Temple of Dawn from the open river."),
            ("Grand Palace & Wat Phra Kaew", "Magnificent royal walls and temple roofs illuminated in brilliant amber and gold light."),
            ("Rama VIII Cable Bridge", "Spectacular single-tower cable-stayed bridge spanning the northern riverfront.")
        ],
        "inclusions": [
            "2-hour luxury evening cruise along the Chao Phraya River",
            "Welcome drink upon boarding",
            "Lavish international and seafood buffet dinner with hot tea & coffee",
            "Live entertainment: classical Thai dance show, cabaret show, and live music",
            "Passenger marine insurance coverage"
        ],
        "exclusions": [
            "Alcoholic beverages and special cocktails (available for purchase onboard)",
            "Hotel road transfers to the pier (can be pre-arranged on request)",
            "Tips for onboard service staff"
        ],
        "timing_text": "Check-in: 06:30 PM – 07:15 PM at Asiatique Pier.<br />Cruising Time: 07:45 PM – 09:45 PM daily.",
        "transport_text": "Boarding at Asiatique The Riverfront Pier (easily reached by free river shuttle from BTS Saphan Taksin).",
        "what_to_bring": "Smart casual attire (air-conditioned indoor salons can be cool, while top deck is open-air), camera, and reservation voucher.",
        "contact_tour_param": "White+Orchid+River+Dinner+Cruise",
        "faqs": [
            ("What is the difference between the White Orchid and Princess dinner cruises?", "White Orchid is celebrated for its signature live cabaret performance in addition to live music, and features an expansive open-air top deck with 360-degree unobstructed views."),
            ("Is there vegetarian or Indian food available on the buffet?", "Yes, the international buffet includes clearly labeled vegetarian options, fresh salads, pasta, and select Indian curries alongside Thai specialties and grilled seafood."),
            ("Where does the cruise depart from?", "The White Orchid typically departs from Asiatique The Riverfront Pier. Specific boarding pier details and check-in desk numbers are confirmed on your travel voucher."),
            ("Can we request upper deck outdoor seating?", "Yes, upper deck outdoor seating can be requested at the time of booking, subject to availability and fair weather conditions.")
        ]
    },
    {
        "filename": "safari_world_open_zoo_drive_tour.html",
        "title": "Safari World Open Zoo Drive Tour Bangkok | Trippovention",
        "h1": "Safari World Open Zoo Drive Tour",
        "subtitle": "8-Kilometer Scenic Safari Park Drive, Free-Roaming African Wildlife & Lion Feeding Show",
        "meta_desc": "Experience Bangkok's Safari World Open Zoo drive-through tour. View free-roaming lions, tigers, zebras, and giraffes in an open African-style savannah setting.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_safari_world_open_zoo.webp",
        "duration": "4–5 Hours",
        "price": "THB 1,150",
        "price_note": "(Per Person)",
        "meetup": "Central Bangkok Hotel Pickup or Safari World Main Gate",
        "overview_p1": "Embark on an exciting wildlife expedition through Safari Park, Thailand's premier 8-kilometer open zoo spanning hundreds of acres. Witness majestic African and Asian wild animals roaming freely in wide-open, naturalistic environments reminiscent of the African wilderness.",
        "overview_p2": "From the comfort of an air-conditioned coach or private safari vehicle, observe herds of zebras, rhinos, ostriches, and antelopes grazing peacefully. The highlight of the morning safari drive is entering the secured carnivore zone to watch the thrilling daily lion and tiger feeding show.",
        "places_col1_title": "Herbivore Savannah",
        "places_col1_badge": "Open Safari",
        "places_col1_items": [
            ("African Savannah Zone", "Roam among hundred-strong herds of zebras, white rhinos, wildebeests, and African crowned cranes."),
            ("Giraffe Feeding Terrace", "World's largest captive giraffe herd with over 200 giraffes roaming across natural parkland."),
            ("Waterfowl Lake", "Picturesque natural lake home to thousands of pelicans, flamingos, and rare migratory birds.")
        ],
        "places_col2_title": "Carnivore Kingdom",
        "places_col2_badge": "Wild Encounters",
        "places_col2_items": [
            ("Lion & Tiger Feeding Show", "Thrilling daily spectacle where park rangers feed majestic Bengal tigers and African lions from a secured cage vehicle."),
            ("Himalayan Black Bears", "Watch black bears splashing in water ponds and foraging in rocky enclosures."),
            ("Predator Habitats", "Carefully landscaped, double-gated sanctuary providing safe viewing of apex predators.")
        ],
        "inclusions": [
            "Official admission ticket to Safari World Open Zoo (Safari Park)",
            "45-minute guided drive through the 8-kilometer open safari reserve",
            "Round-trip air-conditioned coach transfer from central Bangkok",
            "Access to the Lion & Tiger Feeding observation",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Marine Park admission (can be upgraded to full combo package)",
            "Food, lunch buffet and personal refreshments",
            "Giraffe feeding fruit buckets (purchased on-site for 100–150 THB)"
        ],
        "timing_text": "Morning departures from hotel: 08:00 AM – 08:30 AM.<br />Safari Park drive operates 09:00 AM – 04:30 PM (closed Mondays).",
        "transport_text": "Round-trip shared air-conditioned minivan or private transport from Bangkok city center.",
        "what_to_bring": "Casual comfortable clothes, sunglasses, sun hat, camera with zoom lens, and personal spending money.",
        "contact_tour_param": "Safari+World+Open+Zoo+Drive+Tour",
        "faqs": [
            ("Can we drive our own car through Safari World Open Zoo?", "Yes, private vehicles are permitted, or you can ride the park's official air-conditioned safari coach with panoramic viewing windows."),
            ("What time does the Lion Feeding Show take place?", "The lion and tiger feeding typically occurs once daily at 09:45 AM. Our morning tour is scheduled to ensure you arrive in time for this spectacle."),
            ("Is Marine Park included with this ticket?", "This specific package covers the Safari Park Open Zoo drive. If you wish to visit the dolphin shows, sea lion shows, and buffet lunch, please book our 'Safari World & Marine Park Full Day' package."),
            ("How far is Safari World from central Bangkok?", "Safari World is located in the Min Buri district, approximately 45 to 60 minutes northeast of central Bangkok depending on traffic.")
        ]
    },
    {
        "filename": "siam_amazing_park_bangkok.html",
        "title": "Siam Amazing Park Bangkok Tickets | Trippovention",
        "h1": "Siam Amazing Park (Water & Theme Park)",
        "subtitle": "World's Largest Wave Pool, 5 Themed Amusement Zones, Giant Water Slides & International Buffet",
        "meta_desc": "Book Siam Amazing Park Bangkok tickets. Enjoy the Guinness World Record giant wave pool, water slides, Vortex roller coaster, and unlimited rides in 5 themed zones.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_siam_amazing_park.webp",
        "duration": "6–7 Hours (Full Day)",
        "price": "THB 950",
        "price_note": "(Per Person / Unlimited Pass)",
        "meetup": "Central Bangkok Hotel Pickup or Siam Amazing Park Main Entrance",
        "overview_p1": "Established in 1980 and formerly known as Siam Park City, Siam Amazing Park is Thailand's largest amusement and water theme park. Certified by Guinness World Records for housing the world's largest wave pool (spanning 13,600 square meters), it offers a full day of thrilling escapism for families and adventure seekers.",
        "overview_p2": "The expansive 120-acre complex is divided into five themed zones: Water World, X-Zone, Family World, Fantasy World, and Small World. Experience high-speed adrenaline on the 33-meter Speed Slide, loop upside down on the suspended Vortex coaster, or relax under coconut palms along the artificial golden sand beach.",
        "places_col1_title": "Water World Zone",
        "places_col1_badge": "World Record Pool",
        "places_col1_items": [
            ("Guinness Record Wave Pool", "Enormous 13,600 sq. meter artificial sea creating gentle ocean swells and rolling waves."),
            ("7-Story Speed Slide", "Rainbow-colored 33-meter high rainbow water slide certified as one of the tallest in Southeast Asia."),
            ("Flowing River & Spa Pool", "Lazy meandering river and bubbling hot tub lagoons surrounded by tropical greenery.")
        ],
        "places_col2_title": "Adventure Theme Zones",
        "places_col2_badge": "Thrill Rides",
        "places_col2_items": [
            ("Vortex Suspended Coaster", "765-meter inverted looping roller coaster reaching speeds of up to 80 km/h."),
            ("Boomerang & Giant Drop", "Forward-and-backward looping coaster and a 75-meter vertical free-fall tower."),
            ("Si-Am Tower", "109-meter revolving observation tower offering 360-degree aerial views across Bangkok.")
        ],
        "inclusions": [
            "Full-Day Unlimited Ride Pass for all 5 amusement zones and Water World",
            "Access to the world-record wave pool and giant water slides",
            "International buffet lunch (when buffet option is selected)",
            "Park facilities, changing rooms and shower access",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Locker and towel rental fees (nominal cash fee on-site)",
            "Swimwear and swimming gear",
            "Hotel road transfers (optional add-on available)"
        ],
        "timing_text": "Park Open Daily: 10:00 AM – 06:00 PM.<br />Buffet Lunch served: 11:30 AM – 02:00 PM.",
        "transport_text": "Located in Khan Na Yao district; reachable by taxi, MRT Pink Line, or private hotel transfer.",
        "what_to_bring": "Swimwear, change of dry clothes, beach towel, waterproof bag, flip-flops, sunscreen, and cash for lockers.",
        "contact_tour_param": "Siam+Amazing+Park+Bangkok",
        "faqs": [
            ("Are towels and lockers available for rent at the park?", "Yes, clean towels, swim rings, and secure electronic lockers are available for rent at Water World for a small daily fee."),
            ("Are children under a certain height admitted free?", "Children under 100 cm in height typically receive complimentary park admission when accompanied by a paying adult."),
            ("Are rides safe and regularly inspected?", "Yes, all roller coasters and aquatic facilities are certified according to international ISO safety standards and supervised by certified lifeguards."),
            ("Can adults enjoy the water park as well as children?", "Absolutely. Siam Amazing Park features extreme thrill coasters in the X-Zone and giant speed slides alongside family-friendly splash areas and shaded beach loungers.")
        ]
    },
    {
        "filename": "sea_life_bangkok_ocean_world.html",
        "title": "SEA LIFE Bangkok Ocean World Tickets | Trippovention",
        "h1": "SEA LIFE Bangkok Ocean World",
        "subtitle": "Southeast Asia's Largest Aquarium, 270° Ocean Tunnel, Shark Walk & Living Coral Reefs",
        "meta_desc": "Book discounted SEA LIFE Bangkok Ocean World tickets at Siam Paragon. Explore Southeast Asia's largest aquarium featuring 30,000 marine animals and a 270° ocean tunnel.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_sea_life_bangkok_ocean_world.webp",
        "duration": "2–3 Hours",
        "price": "THB 1,190",
        "price_note": "(Per Person / Standard Admission)",
        "meetup": "Siam Paragon Shopping Centre (Basement B1-B2 Floor), BTS Siam Station",
        "overview_p1": "Located in the heart of downtown Bangkok beneath the luxury Siam Paragon shopping complex, SEA LIFE Bangkok Ocean World is Southeast Asia's largest indoor aquarium. Spanning over 10,000 square meters, it houses more than 30,000 marine creatures representing 400 species from around the world.",
        "overview_p2": "Walk through the spectacular 270-degree underwater ocean tunnel where Sand Tiger sharks, giant stingrays, and schools of trevally glide gracefully overhead. Discover 11 immersive zones, from the magical Coral Reef to the Antarctic Penguin Ice Adventure and interactive Touch Pool.",
        "places_col1_title": "Deep Sea Encounters",
        "places_col1_badge": "Marine Highlights",
        "places_col1_items": [
            ("270° Ocean Tunnel", "Walk along the ocean floor as giant sand tiger sharks, eagle rays, and moray eels swim all around you."),
            ("Shark Walk", "Step courageously across a transparent acrylic glass floor with five species of sharks swimming directly beneath your feet."),
            ("Open Ocean Feeding Show", "Watch professional scuba divers hand-feed stingrays and sharks in the massive 8-meter-deep main tank.")
        ],
        "places_col2_title": "Wildlife Habitats",
        "places_col2_badge": "Themed Zones",
        "places_col2_items": [
            ("Penguin Ice Adventure", "Observe charming Gentoo and African penguins waddling on snow banks and diving through sub-zero waters."),
            ("Living Coral Reef", "Vibrant underwater garden showcasing clownfish, sea anemones, lionfish, and delicate seahorses."),
            ("Rainforest & Giant Otters", "Walk through lush indoor jungle paths to spot Asian small-clawed otters and freshwater Amazon stingrays.")
        ],
        "inclusions": [
            "Official standard entrance ticket to SEA LIFE Bangkok Ocean World",
            "Access to all 11 immersive aquarium zones and living exhibitions",
            "Scheduled daily animal feeding shows and educational presentations",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Glass Bottom Ocean Boat ride (available as an optional ticket upgrade)",
            "4D Cinema experience (available as an optional ticket upgrade)",
            "Behind-the-Scenes Tour and Shark Dive experience",
            "Hotel transfers (Siam Paragon is directly connected to BTS Siam)"
        ],
        "timing_text": "Open daily: 10:00 AM – 08:00 PM (Last admission at 07:00 PM).<br />Animal feeding sessions take place throughout the day.",
        "transport_text": "Conveniently located at Siam Paragon, B1-B2 Floor; direct covered walkway from BTS Siam Station (Exit 5).",
        "what_to_bring": "Digital booking voucher, camera (flash photography disabled in animal zones), and light jacket for the Penguin zone.",
        "contact_tour_param": "SEA+LIFE+Bangkok+Ocean+World+Tickets",
        "faqs": [
            ("How do I get to SEA LIFE Bangkok Ocean World?", "Take the BTS SkyTrain to BTS Siam Station (interchange station). Take Exit 5 directly into Siam Paragon shopping mall and descend to basement level B1/B2."),
            ("Can I combine SEA LIFE Bangkok with Madame Tussauds?", "Yes! We offer a popular combo ticket that includes both SEA LIFE Bangkok and Madame Tussauds at nearby Siam Discovery at a discounted rate."),
            ("Is the aquarium fully wheelchair and stroller accessible?", "Yes, the entire facility is equipped with gentle ramps, wide viewing tunnels, and elevator access suitable for strollers and wheelchairs."),
            ("How much time should I allocate for the visit?", "Most families and visitors spend between 2 and 2.5 hours exploring the 11 zones and watching the diver feeding demonstrations.")
        ]
    },
    {
        "filename": "madame_tussauds_bangkok.html",
        "title": "Madame Tussauds Bangkok Tickets | Trippovention",
        "h1": "Madame Tussauds Bangkok",
        "subtitle": "Interactive Celebrity Wax Museum at Siam Discovery, World Leaders, Sports Stars & Pop Icons",
        "meta_desc": "Visit Madame Tussauds Bangkok at Siam Discovery. Walk the red carpet with world leaders, sports legends, Hollywood actors, and Thai celebrities in 8 themed zones.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_madame_tussauds_bangkok.webp",
        "duration": "1.5–2 Hours",
        "price": "THB 890",
        "price_note": "(Per Person / Standard Entry)",
        "meetup": "Siam Discovery Centre (4th Floor), BTS Siam or National Stadium Station",
        "overview_p1": "Step onto the red carpet and mingle with the world's most famous icons at Madame Tussauds Bangkok, located on the 4th floor of the ultra-modern Siam Discovery shopping center. Unlike traditional museums, there are no velvet ropes or barriers—you can get up close, pose, touch, and photograph every figure.",
        "overview_p2": "Spanning eight interactive zones, encounter lifelike wax figures of global political leaders, legendary historical figures, Hollywood movie stars, Grammy-winning pop musicians, sports champions, and celebrated Thai film stars. Complete your visit with fun themed photo props and interactive video stations.",
        "places_col1_title": "Hollywood & Pop Culture",
        "places_col1_badge": "A-List Celebrities",
        "places_col1_items": [
            ("Music Room", "Pose on stage with global pop sensations like Beyoncé, Lady Gaga, Michael Jackson, and Katy Perry."),
            ("A-List Hollywood Lounge", "Walk the red carpet beside Leonardo DiCaprio, Angelina Jolie, Brad Pitt, and Jackie Chan."),
            ("Film & TV Characters", "Battle alongside Marvel superheroes or sit beside kung-fu master Bruce Lee.")
        ],
        "places_col2_title": "History & Sports Stars",
        "places_col2_badge": "World Figures",
        "places_col2_items": [
            ("Leaders & Royal Court", "Stand in the Oval Office beside world presidents or sit with Mahatma Gandhi and the Dalai Lama."),
            ("Sports Champions Zone", "Challenge Cristiano Ronaldo to a penalty kick or step into the boxing ring with Muhammad Ali."),
            ("Wax-Making Exhibition", "Fascinating behind-the-scenes display revealing how sculptors create lifelike wax masterpieces over hundreds of hours.")
        ],
        "inclusions": [
            "Official standard admission ticket to Madame Tussauds Bangkok",
            "Access to all 8 themed celebrity and historical wax galleries",
            "Access to interactive photo props and experiential booths",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Wax hand molding souvenir (optional fee on-site)",
            "Professional photo studio prints",
            "Hotel transfers (Siam Discovery is directly connected to BTS SkyTrain)"
        ],
        "timing_text": "Open Daily: 10:00 AM – 07:00 PM (Last admission 06:00 PM).<br />Flexible entry throughout operating hours.",
        "transport_text": "4th Floor, Siam Discovery; easily accessible via BTS Siam (covered skybridge) or BTS National Stadium.",
        "what_to_bring": "Digital booking voucher, camera or smartphone with full battery, and smiling pose!",
        "contact_tour_param": "Madame+Tussauds+Bangkok+Tickets",
        "faqs": [
            ("Can you touch the wax figures and take photos with them?", "Yes! Madame Tussauds Bangkok is completely interactive. There are no velvet ropes, so visitors are encouraged to touch, pose, hug, and photograph every figure."),
            ("How do I get to Siam Discovery?", "Take the BTS SkyTrain to BTS Siam or BTS National Stadium. Walk across the skybridge straight into Siam Discovery and take the escalators to the 4th floor."),
            ("Is there an age limit for children?", "Madame Tussauds is welcoming to visitors of all ages. Children under 3 years old enter free of charge."),
            ("Can I buy a combo ticket with SEA LIFE Bangkok?", "Yes, we offer an excellent-value Twin Attractions Combo pass combining Madame Tussauds and SEA LIFE Bangkok Ocean World, located just minutes apart in Siam.")
        ]
    },
    {
        "filename": "calypso_cabaret_show_bangkok.html",
        "title": "Calypso Cabaret Show Bangkok | Trippovention",
        "h1": "Calypso Cabaret Show Bangkok",
        "subtitle": "Legendary Broadway-Style Transgender Cabaret, Dazzling Costumes & Choreography at Asiatique",
        "meta_desc": "Experience Bangkok's legendary Calypso Cabaret show at Asiatique The Riverfront. Enjoy world-class Broadway-style dance, dazzling costumes, and comedy performances.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_calypso_cabaret_show.webp",
        "duration": "1.5 Hours (Show Duration: 70 Mins)",
        "price": "THB 1,100",
        "price_note": "(Per Person / Standard Seat)",
        "meetup": "Calypso Cabaret Theatre, Asiatique The Riverfront (Warehouse 3)",
        "overview_p1": "Established in 1988, Calypso Cabaret is Bangkok's pioneer ladyboy cabaret theatre, celebrated globally for its high-energy Broadway-style musical revues, glamorous staging, and exceptional choreographic artistry. Located in the lively riverside warehouse district of Asiatique The Riverfront, Calypso offers top-tier theatrical entertainment.",
        "overview_p2": "Enjoy 16 dazzling variety acts that celebrate diversity, cultural humor, and show-stopping pop numbers. From Marilyn Monroe and Elvis Presley tributes to geisha dances and Chinese opera satires, each scene showcases breathtaking handcrafted costumes, sparkling jewels, and extraordinary talent.",
        "places_col1_title": "Performance Acts",
        "places_col1_badge": "Stage Extravaganza",
        "places_col1_items": [
            ("Broadway Musical Numbers", "High-energy tributes to classic Broadway hits with synchronized group choreography."),
            ("Cultural Variety Acts", "Glamorous theatrical interpretations of Japanese, Korean, Chinese, and Thai cultural dances."),
            ("Comedy & Lip-Sync Satires", "Lighthearted comedic sketches and dramatic lip-sync performances that captivate the audience.")
        ],
        "places_col2_title": "Theatre & Venue",
        "places_col2_badge": "Asiatique Riverfront",
        "places_col2_items": [
            ("State-of-the-Art Theatre", "Intimate tiered-seating auditorium with crystal-clear acoustics and theatrical lighting."),
            ("Asiatique Boardwalk", "Bustling waterfront market filled with artisan boutiques, riverfront restaurants, and a giant Ferris wheel."),
            ("Cast Photo Meet & Greet", "Opportunity to take memorable photos with the dazzling performers outside the theatre after the curtain falls.")
        ],
        "inclusions": [
            "Official reserved admission ticket to Calypso Cabaret Show",
            "One complimentary drink (choice of beer, wine, whiskey, or soft drink)",
            "English-speaking theatre usher service",
            "Travel accident insurance"
        ],
        "exclusions": [
            "Optional Thai set dinner before the show (can be booked as an add-on)",
            "Cast photo tips (customary small tip if posing with performers after the show)",
            "Hotel road transfers (convenient free boat shuttle from BTS Saphan Taksin)"
        ],
        "timing_text": "Nightly Show Times: 07:30 PM (Show 1) and 09:00 PM (Show 2).<br />Check-in 30 minutes prior to curtain call.",
        "transport_text": "Asiatique Warehouse 3; take BTS to Saphan Taksin Station, then board the free Asiatique shuttle boat at Sathorn Pier.",
        "what_to_bring": "Digital booking voucher, camera or smartphone, and light jacket for the air-conditioned theatre.",
        "contact_tour_param": "Calypso+Cabaret+Show+Bangkok",
        "faqs": [
            ("Is Calypso Cabaret suitable for families with children?", "Yes, Calypso is a tasteful, artistic Broadway-style musical revue focused on theatrical dance, comedy, and glamour. It is family-friendly and welcoming to all age groups."),
            ("How do I get to Asiatique The Riverfront?", "Take the BTS SkyTrain to BTS Saphan Taksin Station (Exit 2). Walk to Sathorn Pier and board the free Asiatique river ferry which departs every 15 minutes."),
            ("Is a drink included with the ticket?", "Yes, every standard ticket includes one complimentary beverage of your choice from the bar upon entry."),
            ("Can we take photos during the performance?", "Non-flash photography and short video clips from your seat are permitted during the performance. Flash photography is strictly prohibited.")
        ]
    },
    {
        "filename": "mirinn_cabaret_theatre_bangkok.html",
        "title": "Mirinn Cabaret & Cultural Show Bangkok | Trippovention",
        "h1": "Mirinn Cabaret & Thai Cultural Show",
        "subtitle": "Vibrant Thai Dance, Muay Thai Demonstrations, Spectacular Cabaret & Extravagant Staging",
        "meta_desc": "Watch the vibrant Mirinn Cabaret Show in Bangkok featuring traditional Thai martial arts, Muay Thai fight choreography, and dazzling transgender cabaret performances.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_mirinn_cabaret_theatre.webp",
        "duration": "1.5 Hours",
        "price": "THB 950",
        "price_note": "(Per Person / Standard Seat)",
        "meetup": "Mirinn Theatre, RCA (Royal City Avenue), Bang Kapi, Huai Khwang",
        "overview_p1": "Mirinn Cabaret Theatre delivers a unique and dynamic theatrical fusion that sets it apart from traditional cabaret shows in Thailand. Combining glamorous international cabaret choreography with authentic Muay Thai martial arts demonstrations and graceful classical Thai royal dances, Mirinn offers an action-packed 70-minute spectacle.",
        "overview_p2": "Enjoy lavish costume changes, aerial stunts, live boxing choreography, and modern sound-and-light production at the dedicated theatre at RCA. The show celebrates Thai heritage alongside energetic international music tracks from around the globe.",
        "places_col1_title": "Martial Arts & Heritage",
        "places_col1_badge": "Muay Thai Action",
        "places_col1_items": [
            ("Muay Thai Boxing Choreography", "Thrilling live exhibition of ancient Muay Boran techniques and dynamic modern kickboxing stage fights."),
            ("Classical Thai Kinnaree Dance", "Graceful performance depicting mythical half-bird, half-human celestial dancers from Thai mythology."),
            ("Sword & Staff Martial Arts", "Acrobatic ancient weapons demonstrations set to pulsating traditional drums.")
        ],
        "places_col2_title": "Glamorous Cabaret",
        "places_col2_badge": "World Variety",
        "places_col2_items": [
            ("International Pop Revues", "High-energy dance spectacles featuring popular hits from K-Pop, Hollywood, and Bollywood."),
            ("Elaborate Feather Costumes", "Spectacular handmade crystal headpieces, iridescent silk robes, and dramatic feather backdrops."),
            ("Cast Meet & Greet", "Lively photo session with the cast and martial artists immediately following the finale.")
        ],
        "inclusions": [
            "Official admission ticket to Mirinn Cabaret & Thai Show (Standard or VIP)",
            "One complimentary soft drink or water",
            "Reserved theatre seat with clear stage sightlines",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Optional international buffet dinner (available as an upgrade)",
            "Cast tips for individual souvenir photos",
            "Hotel road transfers (can be arranged upon request)"
        ],
        "timing_text": "Nightly Show Times: 06:00 PM and 07:30 PM.<br />Daily performances.",
        "transport_text": "Located at RCA Plaza, Rama 9; easily accessible by taxi or MRT Phetchaburi / Rama 9 stations.",
        "what_to_bring": "Digital voucher, camera/smartphone, and casual evening clothing.",
        "contact_tour_param": "Mirinn+Cabaret+and+Thai+Show+Bangkok",
        "faqs": [
            ("What makes Mirinn Theatre different from other cabarets?", "Mirinn is unique because it integrates authentic Muay Thai kickboxing and martial arts acrobatics directly into its glamorous cabaret and cultural dance acts."),
            ("Is dinner available at the theatre?", "Yes, you can upgrade your booking to include a delicious Thai and international buffet dinner served prior to showtime in the theatre's adjacent dining salon."),
            ("Is the show suitable for children and families?", "Yes, the performance is completely family-oriented, featuring acrobatic stunts, cultural music, and energetic dance numbers that appeal to all ages."),
            ("Where is Mirinn Theatre located?", "Mirinn is situated at RCA Plaza on Rama 9 Road, one of Bangkok's central entertainment and dining hubs, accessible via MRT Phetchaburi.")
        ]
    },
    {
        "filename": "bangkok_midnight_tuk_tuk_tour.html",
        "title": "Bangkok Midnight Food & Tuk Tuk Tour | Trippovention",
        "h1": "Bangkok Midnight Food & Tuk Tuk Tour",
        "subtitle": "Open-Air Tuk Tuk Ride, Legendary Street Food Stalls, Flower Market & Wat Pho at Night",
        "meta_desc": "Zip through Bangkok's illuminated streets in a private tuk-tuk on an evening food tour. Taste Michelin-guide street food, visit Wat Pho at night, and explore the flower market.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_bangkok_midnight_tuk_tuk.webp",
        "duration": "4 Hours (Evening 07:00 PM – 11:00 PM)",
        "price": "THB 1,750",
        "price_note": "(Per Person / Small Group)",
        "meetup": "Central Bangkok MRT Station Meetup Point (e.g. MRT Sam Yan or Hua Lamphong)",
        "overview_p1": "When darkness falls, Bangkok transforms into a buzzing culinary wonderland. Hop aboard an iconic motorized three-wheeled Tuk Tuk and zoom through illuminated avenues, historic alleyways, and royal boulevards to uncover the city's legendary nighttime street food institutions.",
        "overview_p2": "Led by an expert English-speaking local foodie guide, you will savor award-winning Pad Thai, aromatic Guay Tiew Kua Gai (crispy fried chicken noodles), handmade dim sum, and sweet mango sticky rice. Conclude the evening wandering through the peaceful, floodlit courtyards of Wat Pho and the bustling 24-hour Flower Market.",
        "places_col1_title": "Street Food Tastings",
        "places_col1_badge": "Michelin Tastings",
        "places_col1_items": [
            ("Legendary Pad Thai Stall", "Taste iconic wok-charred Pad Thai wrapped in delicate egg ribbons at a celebrated heritage vendor."),
            ("Crispy Chicken Flat Noodles", "Watch street chefs sear wide rice noodles over blazing charcoal flames in Chinatown."),
            ("Mango Sticky Rice & Sweets", "Indulge in sweet golden mangoes paired with fragrant warm coconut sticky rice and roasted mung beans.")
        ],
        "places_col2_title": "Night Sightseeing",
        "places_col2_badge": "Illuminated Sights",
        "places_col2_items": [
            ("Wat Pho by Night", "Experience the serene, tranquil magic of the Temple of the Reclining Buddha's illuminated golden stupas without daytime crowds."),
            ("Pak Khlong Talad (Flower Market)", "Walk through Thailand's largest 24-hour wholesale flower market bursting with fresh orchids, jasmine, and marigold garlands."),
            ("Secret Rooftop River View", "Sip a refreshing beverage overlooking the illuminated Wat Arun across the tranquil Chao Phraya River.")
        ],
        "inclusions": [
            "Private or small-group Tuk Tuk transport with dedicated driver for 4 hours",
            "Licensed English-speaking professional food and heritage guide",
            "All street food tastings and non-alcoholic drinks (4–5 tasting stops)",
            "Entrance to Wat Pho temple grounds by night",
            "One complimentary drink at a scenic riverside rooftop bar",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Alcoholic beverages (available for personal purchase at bar stop)",
            "Personal souvenirs and takeaway snacks",
            "Tuk-tuk driver and guide tips"
        ],
        "timing_text": "Nightly departures: 07:00 PM – 11:00 PM.<br />Advance reservation required.",
        "transport_text": "Open-air motorized Tuk Tuk transport throughout the tour; return drop-off to your central hotel.",
        "what_to_bring": "Empty stomach, comfortable walking shoes, camera, and light rain poncho (just in case).",
        "contact_tour_param": "Bangkok+Midnight+Food+and+Tuk+Tuk+Tour",
        "faqs": [
            ("Are vegetarian or dietary restrictions accommodated?", "Yes, we can readily accommodate vegetarians, non-pork eaters, and mild spice preferences. Please notify us during your enquiry."),
            ("Can children participate in the night tuk-tuk tour?", "Yes, older children and teens love riding in open-air tuk-tuks! Families with young children can also request car or minivan transport if preferred."),
            ("Is the food sanitary and safe to eat?", "All tasting stops are carefully vetted by our culinary team, featuring busy heritage stalls with high ingredient turnover and Michelin Bib Gourmand recognitions."),
            ("Is hotel drop-off included at the end of the tour?", "Yes, at the conclusion of the evening (around 11:00 PM), your tuk-tuk driver will drop you off directly at your central Bangkok hotel lobby.")
        ]
    },
    {
        "filename": "damnoen_saduak_floating_market_tour.html",
        "title": "Damnoen Saduak Floating Market Tour Bangkok | Trippovention",
        "h1": "Damnoen Saduak Floating Market Tour",
        "subtitle": "Iconic Canal Markets, Traditional Paddle Boat Ride, Local Food Vendors & Sugar Palm Farm",
        "meta_desc": "Experience the world-famous Damnoen Saduak Floating Market from Bangkok. Ride a wooden paddle boat along narrow canals filled with fruit vendors and noodle boats.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_damnoen_saduak_floating_market.webp",
        "duration": "6 Hours (Morning Half Day)",
        "price": "THB 990",
        "price_note": "(Per Person)",
        "meetup": "Central Bangkok Hotel Lobby (Complimentary Pickup)",
        "overview_p1": "Escape the urban bustle and travel southwest through coconut groves and salt flats to Ratchaburi province, home to Damnoen Saduak—Thailand's most famous and photogenic floating market. Established over 150 years ago, these historic canals provide a vibrant window into traditional river life.",
        "overview_p2": "Step aboard a traditional wooden longtail paddle boat and glide through the lively canal intersections. Bargain with friendly local vendors paddling wooden canoes laden with sweet mangoes, baby coconuts, fresh pad thai, and handmade handicrafts.",
        "places_col1_title": "Market Canals",
        "places_col1_badge": "Floating Market",
        "places_col1_items": [
            ("Wooden Paddle Boat Ride", "Intimate boat ride along bustling canals where vendors cook piping hot noodle soup right from their wooden boats."),
            ("Waterfront Boardwalk Walk", "Stroll along elevated wooden walkways lined with souvenir stalls, silk shops, and spice merchants."),
            ("Canal Intersection Photospot", "Famous arch bridge view looking down over the colorful tangle of vendor canoes.")
        ],
        "places_col2_title": "Rural Heritage",
        "places_col2_badge": "Local Culture",
        "places_col2_items": [
            ("Coconut Sugar Farm", "Visit a traditional roadside cottage industry to watch natural coconut palm sap boiled into golden caramel-like palm sugar."),
            ("Salt Evaporation Fields", "Scenic rural drive past the ancient coastal sea-salt evaporation pans of Samut Sakhon."),
            ("Seasonal Fruit Orchards", "Glimpse rural Thai agricultural lifestyle away from the metropolitan center.")
        ],
        "inclusions": [
            "Round-trip shared air-conditioned minivan transport from central Bangkok",
            "Traditional wooden paddle boat ride through Damnoen Saduak canals",
            "Visit to a traditional coconut palm sugar workshop",
            "Licensed English-speaking professional tour guide",
            "Chilled bottled drinking water",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Personal food tastings (boat noodles, coconut ice cream, fruit)",
            "Souvenir shopping along the canals",
            "Driver and guide gratuities"
        ],
        "timing_text": "Early Morning Hotel Pickup: 06:30 AM – 07:15 AM.<br />Return to Bangkok approx. 01:30 PM.<br />Daily departures.",
        "transport_text": "Round-trip air-conditioned minibus with hotel pickup in central Bangkok.",
        "what_to_bring": "Sun hat, sunglasses, sunscreen, camera, and Thai Baht cash in small denominations (20, 50, 100 Baht) for shopping from boats.",
        "contact_tour_param": "Damnoen+Saduak+Floating+Market+Tour",
        "faqs": [
            ("Why does the tour depart so early in the morning?", "Damnoen Saduak is liveliest between 08:30 AM and 11:00 AM before the midday heat and heavy crowds arrive. Departing early ensures the best photo opportunities and authentic trading atmosphere."),
            ("How far is Damnoen Saduak from central Bangkok?", "The market is located approximately 100 kilometers (about 1.5 to 2 hours drive) southwest of Bangkok in Ratchaburi province."),
            ("Is the paddle boat ride included in the tour price?", "Yes, our tour includes the scenic wooden paddle boat ride along the main trading canals."),
            ("Can I buy food directly from the boat vendors?", "Yes, you can wave down boat vendors to purchase delicious coconut ice cream served in fresh coconut shells, fresh spring rolls, and hot boat noodles for 50–80 THB.")
        ]
    },
    {
        "filename": "maeklong_railway_market_and_floating_market_tour.html",
        "title": "Maeklong Railway Market & Floating Market Tour | Trippovention",
        "h1": "Maeklong Railway & Floating Market Tour",
        "subtitle": "World-Famous Train Track Market, Retracting Awnings & Damnoen Saduak Boat Ride",
        "meta_desc": "Experience two world-famous markets in one day from Bangkok: the folding umbrella market on the Maeklong train tracks and Damnoen Saduak Floating Market.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_maeklong_railway_market.webp",
        "duration": "7 Hours (Full Day)",
        "price": "THB 1,290",
        "price_note": "(Per Person / Combo Day Tour)",
        "meetup": "Central Bangkok Hotel Lobby (Complimentary Pickup)",
        "overview_p1": "Combine Thailand's two most extraordinary and legendary traditional markets in an unforgettable full-day excursion. Witness the sensational spectacle of the Maeklong Railway Market (Talad Rom Hup), followed by the vibrant sights, sounds, and aromas of Damnoen Saduak Floating Market.",
        "overview_p2": "At Maeklong, watch vendors calmly pull back their canvas awnings and baskets of produce within seconds as a rumbling passenger train brushes mere inches past market stalls. Then transfer to Damnoen Saduak to board a traditional wooden boat and navigate the bustling trading canals.",
        "places_col1_title": "Maeklong Railway Market",
        "places_col1_badge": "Train Track Miracle",
        "places_col1_items": [
            ("Folding Umbrella Spectacle", "Watch market stalls retract awnings and clear the tracks as the siren wails and the passenger train crawls past."),
            ("Railway Track Walk", "Stroll directly along the active railway tracks lined with fresh seafood, tropical durians, and spices."),
            ("Local Train Station", "Historic terminal station where travelers can capture photos alongside the classic diesel locomotive.")
        ],
        "places_col2_title": "Damnoen Saduak Market",
        "places_col2_badge": "Canal Adventure",
        "places_col2_items": [
            ("Paddle Boat Cruise", "Glide through the lively trading canals aboard a wooden longtail boat surrounded by vendor canoes."),
            ("Canal Street Food", "Sample freshly cooked mango sticky rice, grilled chicken skewers, and sweet coconut pancakes."),
            ("Coconut Sugar Workshop", "Observe traditional palm sugar boiling over clay woodfired kilns.")
        ],
        "inclusions": [
            "Round-trip air-conditioned minivan transport from central Bangkok hotels",
            "Licensed English-speaking professional tour guide",
            "Guided visit to Maeklong Railway Market synchronized with the train passing schedule",
            "Wooden paddle boat ride through Damnoen Saduak Floating Market",
            "Stop at traditional coconut palm sugar farm",
            "Bottled drinking water",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Personal food, snacks and lunch",
            "Souvenir purchases at market stalls",
            "Tips for tour guide and driver"
        ],
        "timing_text": "Hotel Pickup: 06:45 AM – 07:30 AM.<br />Train Passing Time synchronized approx. 08:30 AM or 11:10 AM.<br />Return to Bangkok approx. 02:30 PM.",
        "transport_text": "Round-trip shared air-conditioned minivan with hotel pickup and drop-off in central Bangkok.",
        "what_to_bring": "Comfortable light walking clothes, walking shoes, sun hat, sunglasses, camera with fast shutter, and cash in small denominations.",
        "contact_tour_param": "Maeklong+Railway+Market+and+Floating+Market+Tour",
        "faqs": [
            ("Will we definitely see the train pass through the market?", "Yes, our tour itinerary is precisely scheduled around the State Railway of Thailand train arrival times so you can safely watch and photograph the market awnings retract."),
            ("Is it safe standing near the train tracks?", "Yes, the train travels at a slow walking speed (approx. 15 km/h) through the market, sounding its horn continuously while shopkeepers and our guide ensure all guests stand safely behind the yellow marker lines."),
            ("Can we ride the train itself?", "The standard tour views the train passing from the market tracks for optimal photography. An optional upgrade to ride one station into Maeklong can be arranged on private tours."),
            ("How much time is spent at each market?", "Approximately 1 to 1.5 hours at Maeklong Railway Market, followed by 1.5 to 2 hours at Damnoen Saduak Floating Market, including the boat ride and free time for lunch.")
        ]
    },
    {
        "filename": "chinatown_yaowarat_street_food_tour.html",
        "title": "Chinatown & Yaowarat Street Food Tour Bangkok | Trippovention",
        "h1": "Chinatown & Yaowarat Street Food Tour",
        "subtitle": "Michelin-Recommended Stalls, Neon-Lit Alleys, Exotic Delicacies & Heritage Walking Tour",
        "meta_desc": "Explore Bangkok Chinatown (Yaowarat) on a guided evening walking food tour. Taste 6 to 8 Michelin Bib Gourmand street dishes, dim sum, and Thai-Chinese desserts.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_chinatown_yaowarat_bangkok.webp",
        "duration": "3–4 Hours (Evening)",
        "price": "THB 1,200",
        "price_note": "(Per Person / Small Group)",
        "meetup": "MRT Wat Mangkon Station (Exit 1), Bangkok Chinatown",
        "overview_p1": "Bangkok's Chinatown, centered along neon-drenched Yaowarat Road, is universally recognized as one of the world's greatest street food epicenters. Established in 1782 by Chinese merchants who relocated during the founding of Bangkok, the district retains an intoxicating blend of heritage shophouses, herbal dispensaries, and sizzling food stalls.",
        "overview_p2": "Accompanied by a passionate local foodie guide, weave through labyrinthine side alleys (sois) that most tourists miss. Savor 6 to 8 curated tastings—from crispy pork belly and Michelin-recognized pepper noodle broth to charcoal-toasted buns filled with warm pandan custard and black sesame dumplings in ginger tea.",
        "places_col1_title": "Curated Tastings",
        "places_col1_badge": "Street Flavors",
        "places_col1_items": [
            ("Michelin Guay Jub", "Peppery rolled rice noodle soup with crispy roasted pork belly recognized by the Michelin Bib Gourmand guide."),
            ("Charcoal Grilled Buns", "Warm, crispy-on-the-outside buns overflowing with rich chocolate, condensed milk, or pandan custard."),
            ("Handmade Dim Sum & Dumplings", "Steamed pork-and-shrimp siu mai and chive dumplings seasoned with soy and crispy garlic.")
        ],
        "places_col2_title": "Chinatown Heritage",
        "places_col2_badge": "Hidden Alleys",
        "places_col2_items": [
            ("Wat Mangkon Kamalawat", "Bangkok's largest and most important Chinese Buddhist temple, adorned with red lanterns and incense coils."),
            ("Trok Mo Fresh Market", "Atmospheric narrow market alley bustling with vendors selling tropical spices, dried fish, and Chinese herbs."),
            ("Yaowarat Neon Boulevard", "Iconic nighttime view of Yaowarat Road illuminated under towering red and gold neon signs.")
        ],
        "inclusions": [
            "Expert English-speaking licensed local culinary guide",
            "6 to 8 curated food and dessert tastings",
            "Local herbal drinks (chrysanthemum tea, butterfly pea, and iced tea)",
            "Guided cultural walking tour through hidden alleys and temples",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Alcoholic beverages and beer (available for personal purchase)",
            "Hotel road transfers (easily reachable via MRT Wat Mangkon station)",
            "Gratuities for food guide"
        ],
        "timing_text": "Nightly departures: 05:30 PM – 09:00 PM.<br />Small group size capped for personalized experience.",
        "transport_text": "Walking tour starting directly at MRT Wat Mangkon Station (Blue Line).",
        "what_to_bring": "Comfortable walking shoes, empty stomach, camera, and cash for optional extra snacks.",
        "contact_tour_param": "Chinatown+Yaowarat+Street+Food+Tour",
        "faqs": [
            ("Can dietary requirements like vegetarian or no-pork be accommodated?", "Yes, please inform us when enquiring. Chinatown offers fantastic vegetarian, seafood, and chicken alternatives at every stop."),
            ("How do I meet the guide?", "The tour begins at Exit 1 of MRT Wat Mangkon Station, right in the center of Chinatown. Your guide will be waiting holding a Trippovention welcome sign."),
            ("Is there a lot of walking involved?", "The walking tour covers approximately 2.5 kilometers at an easy, leisurely pace with frequent seated stops at eateries every 15 to 20 minutes."),
            ("Is it safe to eat street food in Yaowarat?", "Yes, we exclusively patronize established heritage vendors with high daily food turnover, stellar hygiene standards, and Michelin guide accolades.")
        ]
    },
    {
        "filename": "ayutthaya_historical_park_full_day_tour.html",
        "title": "Ayutthaya Historical Park Full-Day Tour from Bangkok | Trippovention",
        "h1": "Ayutthaya Historical Park Full-Day Tour",
        "subtitle": "UNESCO World Heritage Ancient Siamese Capital, Wat Mahathat Tree Buddha & Wat Chaiwatthanaram",
        "meta_desc": "Explore the UNESCO World Heritage ancient capital of Ayutthaya on a full-day tour from Bangkok. Visit Wat Mahathat, Wat Chaiwatthanaram, and enjoy a Thai buffet lunch.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_ayutthaya_historical_park.webp",
        "duration": "8–9 Hours (Full Day Excursion)",
        "price": "THB 1,950",
        "price_note": "(Per Person / With Lunch)",
        "meetup": "Central Bangkok Hotel Lobby (Complimentary Pickup)",
        "overview_p1": "Journey 80 kilometers north of Bangkok to Ayutthaya, the illustrious capital of the Kingdom of Siam from 1350 until its destruction in 1767. Recognized as a UNESCO World Heritage Site, this magnificent archaeological park showcases monumental red-brick prangs, serene seated Buddhas, and soaring bell-shaped chedis.",
        "overview_p2": "Accompanied by an expert historical guide, explore the famous Buddha head entwined in banyan tree roots at Wat Mahathat, wander the expansive royal grounds of Wat Phra Si Sanphet, marvel at the giant reclining Buddha at Wat Lokayasutharam, and photograph the majestic riverside Khmer-style prangs of Wat Chaiwatthanaram.",
        "places_col1_title": "Historic Temples",
        "places_col1_badge": "UNESCO Ruins",
        "places_col1_items": [
            ("Wat Mahathat", "World-renowned sandstone Buddha head serenely entwined in the ancient roots of a sacred banyan tree."),
            ("Wat Phra Si Sanphet", "Grand royal temple within the ancient palace compound featuring three majestic restored royal stupas."),
            ("Wat Lokayasutharam", "Colossal 42-meter-long outdoor reclining Buddha statue draped in bright saffron robes.")
        ],
        "places_col2_title": "Riverside Splendor",
        "places_col2_badge": "Royal Architecture",
        "places_col2_items": [
            ("Wat Chaiwatthanaram", "Spectacular 17th-century riverside Khmer-style temple complex modeled after Angkor Wat, famous from historical films."),
            ("Bang Pa-In Summer Palace (Optional)", "Eclectic royal summer retreat blending Thai, Chinese, and European neoclassical pavilions."),
            ("Ayutthaya Buffet Lunch", "Delicious buffet lunch featuring traditional Central Thai specialties and tropical fruits.")
        ],
        "inclusions": [
            "Round-trip air-conditioned minibus or private vehicle transport from Bangkok",
            "Official entrance admission tickets to all designated Ayutthaya Historical Park temples",
            "Delicious Thai buffet lunch at a local riverside restaurant",
            "Certified licensed English-speaking historical guide",
            "Chilled bottled drinking water and refreshing towels",
            "Comprehensive travel accident insurance"
        ],
        "exclusions": [
            "Personal spending and souvenir shopping",
            "Optional Bang Pa-In palace golf cart rental",
            "Tips for tour guide and driver"
        ],
        "timing_text": "Hotel Pickup: 07:00 AM – 07:45 AM.<br />Return to Bangkok approx. 04:30 PM – 05:30 PM.<br />Daily departures.",
        "transport_text": "Round-trip air-conditioned minivan transport with hotel pickup and drop-off in central Bangkok.",
        "what_to_bring": "Modest clothing covering shoulders and knees (active Buddhist ruins), sun hat, sunglasses, sunscreen, comfortable walking shoes, and camera.",
        "contact_tour_param": "Ayutthaya+Historical+Park+Full+Day+Tour",
        "faqs": [
            ("How long is the drive from Bangkok to Ayutthaya?", "Ayutthaya is located approximately 80 kilometers north of central Bangkok. The drive takes about 1 hour and 15 minutes to 1.5 hours via the expressway."),
            ("What is the dress code for Ayutthaya Historical Park?", "Even though many temples are ancient ruins, they remain sacred consecrated sites. Visitors must wear clothing covering shoulders and knees. Sleeveless shirts and short shorts are strictly prohibited."),
            ("Are entrance fees and lunch included?", "Yes, all temple entrance tickets and a full Thai buffet lunch at a local restaurant are included in your tour price."),
            ("Is Ayutthaya suitable for children and seniors?", "Yes, the historical park grounds are relatively flat with paved walkways. Wheelchair access is feasible around the main viewing courtyards of Wat Mahathat and Wat Chaiwatthanaram.")
        ]
    },
    {
        "filename": "ancient_city_and_erawan_museum_tour.html",
        "title": "Ancient City (Muang Boran) & Erawan Museum Tour | Trippovention",
        "h1": "Ancient City (Muang Boran) & Erawan Museum",
        "subtitle": "World's Largest Open-Air Museum, Giant Three-Headed Elephant & Recreated Thai Kingdoms",
        "meta_desc": "Visit the Ancient City (Muang Boran) and Erawan Museum in Samut Prakan from Bangkok. Explore the world's largest open-air museum and 250-ton three-headed bronze elephant.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_ancient_city_muang_boran.webp",
        "duration": "7–8 Hours (Full Day Excursion)",
        "price": "THB 1,750",
        "price_note": "(Per Person / With Transfers)",
        "meetup": "Central Bangkok Hotel Lobby (Complimentary Pickup)",
        "overview_p1": "Discover the architectural soul and mythical grandeur of Thailand in one extraordinary day. Located in neighboring Samut Prakan just south of Bangkok, the Ancient City (Muang Boran) is the world's largest open-air museum, spanning over 300 acres shaped precisely like the map of Thailand.",
        "overview_p2": "Explore more than 120 scaled and life-sized replicas of Thailand's most revered palaces, sacred sanctuaries, and lost monuments from the Dvaravati, Sukhothai, and Ayutthaya eras. Combine this with the awe-inspiring Erawan Museum, crowned by a monumental 250-ton, 39-meter-tall three-headed bronze elephant housing divine celestial art.",
        "places_col1_title": "Ancient City (Muang Boran)",
        "places_col1_badge": "Open-Air Museum",
        "places_col1_items": [
            ("Sanphet Prasat Palace", "Stunning full-scale reconstruction of the lost royal throne hall of Ayutthaya destroyed in 1767."),
            ("Pavilion of the Enlightened", "Spectacular gilded wooden temple rising majestically over tranquil lotus-filled lagoons."),
            ("Bicycle & Tram Exploration", "Enjoy peaceful sightseeing by electric golf cart, open tram, or complimentary bicycle across 300 acres.")
        ],
        "places_col2_title": "Erawan Museum",
        "places_col2_badge": "Three-Headed Elephant",
        "places_col2_items": [
            ("Monumental Bronze Elephant", "Colossal 39-meter-tall, 250-ton bronze sculpture of Airavata, the mythical three-headed elephant."),
            ("Stained-Glass Zodiac Ceiling", "Breathtaking stained-glass dome created by German master craftsman Jacob Schwarzkopf representing world harmony."),
            ("Cosmic Heaven Chamber", "Sacred celestial shrine located inside the elephant's belly displaying ancient Buddha statues.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transfers from central Bangkok",
            "Official admission ticket to Ancient City (Muang Boran)",
            "Complimentary bicycle use or guided tram ride within Ancient City",
            "Official admission ticket to the Erawan Museum",
            "Licensed English-speaking professional tour guide",
            "Bottled drinking water",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Optional private electric golf cart rental (available on-site for ~350 THB/hr)",
            "Personal food, lunch and refreshments",
            "Driver and guide gratuities"
        ],
        "timing_text": "Morning Hotel Pickup: 08:30 AM – 09:00 AM.<br />Return to Bangkok hotel approx. 04:30 PM.<br />Daily departures.",
        "transport_text": "Round-trip air-conditioned minivan transport with hotel pickup and drop-off in central Bangkok.",
        "what_to_bring": "Modest clothing covering shoulders and knees (for temple interiors), comfortable walking shoes, sunglasses, sun hat, and camera.",
        "contact_tour_param": "Ancient+City+and+Erawan+Museum+Tour",
        "faqs": [
            ("How do visitors get around the 300-acre Ancient City?", "Admission includes access to the park's hop-on hop-off tram service and complimentary bicycles. Private 4-seat and 6-seat electric golf carts are also available for rent with a valid driver's license."),
            ("Can you go inside the giant three-headed elephant at Erawan Museum?", "Yes! Visitors can ascend via a spiral staircase or elevator inside one of the elephant's massive legs to reach the top chamber inside the belly, which houses a serene shrine representing Buddhist heaven."),
            ("How far are these attractions from Bangkok?", "Both sites are located in Samut Prakan, just south of Bangkok city limits, approximately 35 to 45 minutes drive from downtown via the Southern Expressway."),
            ("Is lunch included in this tour?", "Lunch is not included in the standard package, but there are multiple authentic Thai food stalls, waterfront restaurants, and a floating market food village inside Ancient City.")
        ]
    }
]

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
  <head>
    <!-- Google Tag Manager -->
    <script>
      (function (w, d, s, l, i) {
        w[l] = w[l] || [];
        w[l].push({ "gtm.start": new Date().getTime(), event: "gtm.js" });
        var f = d.getElementsByTagName(s)[0],
          j = d.createElement(s),
          dl = l != "dataLayer" ? "&l=" + l : "";
        j.async = true;
        j.src = "https://www.googletagmanager.com/gtm.js?id=" + i + dl;
        f.parentNode.insertBefore(j, f);
      })(window, document, "script", "dataLayer", "GTM-NLPKQZJS");
    </script>
    <!-- End Google Tag Manager -->

    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <title>{{TITLE}}</title>
    <meta name="description" content="{{META_DESC}}" />
    <meta name="author" content="Trippovention" />

    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://trippovention.co.th/packages/thailand/bangkok/{{FILENAME}}" />
    <meta property="og:title" content="{{TITLE}}" />
    <meta property="og:description" content="{{META_DESC}}" />
    <meta property="og:image" content="{{OG_IMAGE}}" />

    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="https://trippovention.co.th/packages/thailand/bangkok/{{FILENAME}}" />
    <meta property="twitter:title" content="{{TITLE}}" />
    <meta property="twitter:description" content="{{META_DESC}}" />
    <meta property="twitter:image" content="{{OG_IMAGE}}" />

    <link rel="canonical" href="https://trippovention.co.th/packages/thailand/bangkok/{{FILENAME}}" />
    <link rel="icon" type="image/x-icon" href="../../../assets/images/favicon.ico" />
    <link rel="apple-touch-icon" sizes="180x180" href="../../../assets/images/favicon.png" />
    <link rel="manifest" href="../../../site.webmanifest" />
    <meta name="theme-color" content="#667eea" />
    <meta name="referrer" content="strict-origin-when-cross-origin" />

    <link rel="stylesheet" href="../../../assets/styles.css" />
    <link rel="stylesheet" href="../../../assets/search.css" />
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
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("js", new Date());
      gtag("config", "AW-11395302765");
    </script>

    <!-- Structured Data -->
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "TouristTrip",
        "name": "{{H1}}",
        "description": "{{META_DESC}}",
        "touristType": ["Travelers", "Families", "Couples", "Sightseeing Seekers"],
        "offers": {
          "@type": "Offer",
          "price": "{{PRICE_CLEAN}}",
          "priceCurrency": "THB",
          "availability": "https://schema.org/InStock",
          "url": "https://trippovention.co.th/packages/thailand/bangkok/{{FILENAME}}"
        },
        "provider": {
          "@type": "TravelAgency",
          "name": "Trippovention",
          "url": "https://trippovention.co.th"
        }
      }
    </script>
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://trippovention.co.th/"
          },
          {
            "@type": "ListItem",
            "position": 2,
            "name": "Destinations",
            "item": "https://trippovention.co.th/destinations.html"
          },
          {
            "@type": "ListItem",
            "position": 3,
            "name": "Thailand",
            "item": "https://trippovention.co.th/packages/thailand/"
          },
          {
            "@type": "ListItem",
            "position": 4,
            "name": "Bangkok",
            "item": "https://trippovention.co.th/packages/thailand/bangkok/"
          },
          {
            "@type": "ListItem",
            "position": 5,
            "name": "Sightseeing",
            "item": "https://trippovention.co.th/packages/thailand/bangkok/sightseeing.html"
          },
          {
            "@type": "ListItem",
            "position": 6,
            "name": "{{H1}}",
            "item": "https://trippovention.co.th/packages/thailand/bangkok/{{FILENAME}}"
          }
        ]
      }
    </script>
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
{{FAQ_SCHEMA_ITEMS}}
        ]
      }
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
            <a class="icon" title="Call Us" href="tel:+66946934392">📞</a>
            <a
              class="icon"
              title="WhatsApp"
              href="https://wa.me/66946934392"
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
              <a href="index.html">Bangkok</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item">
              <a href="sightseeing.html">Sightseeing</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item active" aria-current="page">
              {{H1}}
            </li>
          </ol>
        </div>
      </nav>

      <header class="hero compact hero-thailand">
        <div class="container">
          <h1>{{H1}}</h1>
          <p>{{SUBTITLE}}</p>
        </div>
      </header>

      <section class="section">
        <div class="container">
          <div class="grid cols-3">
            <div class="card info-card">
              <div class="body">
                <div class="info-icon">⏱️</div>
                <h2>Duration</h2>
                <p>{{DURATION}}</p>
              </div>
            </div>
            <div class="card info-card card-premium">
              <div class="body">
                <div class="info-icon">💰</div>
                <h3>Tour Price</h3>
                <div class="price-row">
                  <span class="price">{{PRICE}} <small style="font-size: 13px; font-weight: normal; color: var(--text-muted);">{{PRICE_NOTE}}</small></span>
                </div>
              </div>
            </div>
            <div class="card info-card">
              <div class="body">
                <div class="info-icon">📍</div>
                <h2>Meet-up Location</h2>
                <p>{{MEETUP}}</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section alt">
        <div class="container">
          <div class="section-title">
            <h2>Tour Overview &amp; Description</h2>
            <p class="subtitle">{{SUBTITLE}}</p>
          </div>
          <div class="card" style="padding: 28px;">
            <p style="font-size: 16px; line-height: 1.8; margin-bottom: 20px;">
              {{OVERVIEW_P1}}
            </p>
            <p style="font-size: 16px; line-height: 1.8; margin-bottom: 0;">
              {{OVERVIEW_P2}}
            </p>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div class="section-title">
            <h2>Places Covered &amp; Highlights</h2>
            <p class="subtitle">Experience the highlights and sights included on this journey</p>
          </div>

          <div class="two">
            <div class="card">
              <div class="body">
                <div class="badge">{{PLACES_COL1_BADGE}}</div>
                <h3>{{PLACES_COL1_TITLE}}</h3>
                <ul class="muted" style="line-height: 1.9; margin-top: 12px;">
{{PLACES_COL1_HTML}}
                </ul>
              </div>
            </div>

            <div class="card">
              <div class="body">
                <div class="badge">{{PLACES_COL2_BADGE}}</div>
                <h3>{{PLACES_COL2_TITLE}}</h3>
                <ul class="muted" style="line-height: 1.9; margin-top: 12px;">
{{PLACES_COL2_HTML}}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section alt">
        <div class="container">
          <div class="section-title">
            <h2>Inclusions &amp; Exclusions</h2>
            <p class="subtitle">Comprehensive breakdown of services included in this package</p>
          </div>

          <div class="two">
            <div class="card card-premium">
              <div class="body">
                <h3>✅ Inclusions</h3>
                <ul style="line-height: 1.8; margin-top: 12px;">
{{INCLUSIONS_HTML}}
                </ul>
              </div>
            </div>

            <div class="card">
              <div class="body">
                <h3>❌ Exclusions</h3>
                <ul class="muted" style="line-height: 1.8; margin-top: 12px;">
{{EXCLUSIONS_HTML}}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div class="section-title">
            <h2>Tour Information &amp; Practical Guidelines</h2>
            <p class="subtitle">Essential details for a smooth, comfortable and memorable experience</p>
          </div>

          <div class="grid cols-3">
            <div class="card">
              <div class="body text-center">
                <div class="feature-icon">⏰</div>
                <h3>Tour Timing</h3>
                <p class="muted">
                  {{TIMING_TEXT}}
                </p>
              </div>
            </div>
            <div class="card">
              <div class="body text-center">
                <div class="feature-icon">🚐</div>
                <h3>Transport &amp; Transfers</h3>
                <p class="muted">
                  {{TRANSPORT_TEXT}}
                </p>
              </div>
            </div>
            <div class="card">
              <div class="body text-center">
                <div class="feature-icon">🎒</div>
                <h3>What to Bring</h3>
                <p class="muted">
                  {{WHAT_TO_BRING}}
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- FAQ Section (AEO & Answer Engine Optimization) -->
      <section class="section alt faq-section" id="faq">
        <div class="container">
          <div class="section-title">
            <h2>Frequently Asked Questions</h2>
            <p class="subtitle">Quick answers to common questions about this Bangkok activity</p>
          </div>
          <div class="faq-container">
{{FAQ_ACCORDION_HTML}}
          </div>
        </div>
      </section>

      <section class="section cta">
        <div class="container">
          <div class="section-title">
            <h2 class="text-white">Enquire About {{H1}}</h2>
            <p class="subtitle text-white-90">
              Get the best rates on Bangkok sightseeing, activities, and private arrangements with Trippovention
            </p>
          </div>
          <div class="text-center">
            <a
              class="btn btn-lg ghost"
              href="../../../contact.html?destination=bangkok&tour={{CONTACT_TOUR_PARAM}}"
              >📞 Request Custom Quote</a
            >
            <a
              class="btn btn-lg ghost ml-16"
              href="https://wa.me/66946934392?text=Hello,%20I%20am%20interested%20in%20booking%20the%20{{CONTACT_TOUR_PARAM}}%20in%20Bangkok"
              target="_blank"
              rel="noopener noreferrer"
              >💬 WhatsApp: +66 94 693 4392</a
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
              be transformative, authentic, and memorable.
            </p>
            <div class="mt-20">
              <h3 class="muted font-weight-600">Contact Details</h3>
              <span class="mr-15"
                >📧 <a href="mailto:query@trippovention.co.th">query@trippovention.co.th</a></span
              >
              <br />
              <span>📞 <a href="tel:+66946934392">+66 94 693 4392</a></span>
              <br />
              <span>💬
                <a href="https://wa.me/66946934392" target="_blank" rel="noopener noreferrer"
                  >WhatsApp</a
                ></span
              >
            </div>
          </div>
          <div>
            <h3>Quick Links</h3>
            <div class="line-height-2">
              <a href="../../../index.html">Home</a><br />
              <a href="../../../destinations.html">Destinations by Country</a><br />
              <a href="../../../destinations-themes.html">Destinations by Theme</a><br />
              <a href="../../../destinations-travelers.html">Destinations by Traveler</a><br />
              <a href="../../../services.html">Services</a><br />
              <a href="sightseeing.html">Bangkok Sightseeing Catalogue</a><br />
              <a href="index.html">Bangkok Tour Packages</a><br />
              <a href="../../../contact.html">Contact Us</a>
            </div>
          </div>
          <div>
            <h3>Thailand Office</h3>
            <p>
              23/13 M, 12 Nong Pure Subdistrict, Bang Lamung District, Chonburi Province-20150
            </p>
            <div class="mt-20">
              <h3 class="muted font-weight-600">Follow Us</h3>
              <div class="social-icons">
                <a
                  href="https://facebook.com/trippovention"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Follow us on Facebook"
                  title="Facebook"
                >
                  <img
                    src="../../../assets/images/social/facebook.svg"
                    alt="Facebook"
                    width="24"
                    height="24"
                    class="social-icon-white"
                    loading="lazy"
                  />
                </a>
                <a
                  href="https://instagram.com/trippovention"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Follow us on Instagram"
                  title="Instagram"
                >
                  <img
                    src="../../../assets/images/social/instagram.svg"
                    alt="Instagram"
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
                    src="../../../assets/images/social/whatsapp.svg"
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
        <div class="footer-bottom mt-40 text-center section-border-top pt-30">
          <p>© 2026 Trippovention. All rights reserved.</p>
        </div>
      </div>
    </footer>

    <script src="../../../assets/app.js"></script>
    <script src="../../../assets/search.js" defer=""></script>
  </body>
</html>
"""

def generate_pages():
    os.makedirs(DEST_DIR, exist_ok=True)
    count = 0
    for data in TOURS_DATA:
        # Col 1 highlights
        col1_lines = []
        for name, desc in data["places_col1_items"]:
            col1_lines.append(f"                  <li><strong>{name}:</strong> {desc}</li>")
        places_col1_html = "\n".join(col1_lines)

        # Col 2 highlights
        col2_lines = []
        for name, desc in data["places_col2_items"]:
            col2_lines.append(f"                  <li><strong>{name}:</strong> {desc}</li>")
        places_col2_html = "\n".join(col2_lines)

        # Inclusions
        inc_lines = [f"                  <li>✓ {item}</li>" for item in data["inclusions"]]
        inclusions_html = "\n".join(inc_lines)

        # Exclusions
        exc_lines = [f"                  <li>✗ {item}</li>" for item in data["exclusions"]]
        exclusions_html = "\n".join(exc_lines)

        # Price clean for schema
        price_clean = data["price"].replace("THB", "").replace(",", "").strip()

        # FAQs
        faq_acc_items = []
        faq_schema_items = []
        for i, (q, a) in enumerate(data.get("faqs", [])):
            is_open = " open" if i == 0 else ""
            faq_acc_items.append(f"""            <details class="faq-item"{is_open}>
              <summary class="faq-question"><span>{q}</span><span class="faq-chevron" aria-hidden="true">▾</span></summary>
              <div class="faq-answer"><p>{a}</p></div>
            </details>""")
            
            # JSON-LD entity
            faq_schema_items.append(f"""          {{
            "@type": "Question",
            "name": "{q}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{a}"
            }}
          }}""")

        faq_accordion_html = "\n".join(faq_acc_items)
        faq_schema_str = ",\n".join(faq_schema_items)

        replacements = {
            "{{TITLE}}": data["title"],
            "{{H1}}": data["h1"],
            "{{SUBTITLE}}": data["subtitle"],
            "{{META_DESC}}": data["meta_desc"],
            "{{OG_IMAGE}}": data["og_image"],
            "{{FILENAME}}": data["filename"],
            "{{DURATION}}": data["duration"],
            "{{PRICE}}": data["price"],
            "{{PRICE_NOTE}}": data["price_note"],
            "{{PRICE_CLEAN}}": price_clean,
            "{{MEETUP}}": data["meetup"],
            "{{OVERVIEW_P1}}": data["overview_p1"],
            "{{OVERVIEW_P2}}": data["overview_p2"],
            "{{PLACES_COL1_TITLE}}": data["places_col1_title"],
            "{{PLACES_COL1_BADGE}}": data["places_col1_badge"],
            "{{PLACES_COL1_HTML}}": places_col1_html,
            "{{PLACES_COL2_TITLE}}": data["places_col2_title"],
            "{{PLACES_COL2_BADGE}}": data["places_col2_badge"],
            "{{PLACES_COL2_HTML}}": places_col2_html,
            "{{INCLUSIONS_HTML}}": inclusions_html,
            "{{EXCLUSIONS_HTML}}": exclusions_html,
            "{{TIMING_TEXT}}": data["timing_text"],
            "{{TRANSPORT_TEXT}}": data["transport_text"],
            "{{WHAT_TO_BRING}}": data["what_to_bring"],
            "{{CONTACT_TOUR_PARAM}}": data["contact_tour_param"],
            "{{FAQ_ACCORDION_HTML}}": faq_accordion_html,
            "{{FAQ_SCHEMA_ITEMS}}": faq_schema_str
        }

        html_content = HTML_TEMPLATE
        for token, val in replacements.items():
            html_content = html_content.replace(token, str(val))

        out_path = os.path.join(DEST_DIR, data["filename"])
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        count += 1
        print(f"Generated: {data['filename']}")

    print(f"\nSuccessfully generated {count} Bangkok sightseeing detail pages!")

if __name__ == "__main__":
    generate_pages()

