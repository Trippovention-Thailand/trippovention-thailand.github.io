#!/usr/bin/env python3
"""
Generate individual detail pages for the 19 new Phuket sightseeing tours.
Follows Trippovention design system, typography, SEO metadata, breadcrumbs, 
genuine Phuket-specific FAQs, and schema.
"""

import os

DEST_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "packages", "thailand", "phuket")

TOURS_DATA = [
    {
        "filename": "phuket_city_highlights_tour.html",
        "title": "Phuket City Highlights & Landmarks Tour | Trippovention",
        "h1": "Phuket City Highlights & Landmarks Tour",
        "subtitle": "Karon Viewpoint, Big Buddha, Wat Chalong, Cashew Nut Factory & Historic Old Town",
        "meta_desc": "Explore Phuket's cultural landmarks and viewpoints on a guided city tour. Visit Karon Viewpoint, Big Buddha, Wat Chalong, and charming Sino-Portuguese Phuket Old Town.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_city_highlights.webp",
        "duration": "Half Day (4–5 Hours)",
        "price": "THB 950",
        "price_note": "(Per Person)",
        "meetup": "Round-trip pickup from Patong, Kata, Karon, and Phuket Town hotels",
        "overview_p1": "Discover the vibrant culture, rich maritime history, and breathtaking coastal vistas of Thailand's largest island on the Phuket City Highlights & Landmarks Tour. Designed as the perfect introductory excursion for first-time visitors and families, this comprehensive half-day tour takes you beyond the beaches to explore the island's most revered cultural monuments and panoramic vantage points.",
        "overview_p2": "Travel in comfortable air-conditioned transport accompanied by a knowledgeable local guide. From the three-bay vista at Karon Viewpoint and the spiritual serenity of Wat Chalong to the pastel Sino-Portuguese shophouses of Phuket Old Town and artisanal cashew nut processing, you will experience the authentic heritage and natural beauty of Phuket in a relaxed, well-paced itinerary.",
        "places_col1_title": "Sacred Temples & Historic Quarters",
        "places_col1_badge": "Culture & Heritage",
        "places_col1_items": [
            ("Wat Chalong (Wat Chaithararam)", "Phuket's most revered temple complex, housing the 60-meter-tall Grand Pagoda (Chedi) containing an authentic bone relic fragment of Lord Buddha."),
            ("Phuket Old Town Heritage Street", "Stroll past beautifully preserved 19th-century Sino-Portuguese shophouses, heritage cafes, vibrant street murals, and historic shrines along Thalang Road."),
            ("Cashew Nut Processing Factory", "Discover the fascinating cultivation and processing of local cashew nuts with tastings of various roasted and honey-glazed flavors.")
        ],
        "places_col2_title": "Coastal Panoramas & Landmarks",
        "places_col2_badge": "Panoramic Lookouts",
        "places_col2_items": [
            ("Karon Viewpoint (Kho Sam Haad)", "Famous hillside lookout offering a postcard-perfect view of three iconic beaches: Kata Noi, Kata Yai, and Karon Beach."),
            ("Big Buddha of Phuket (Nakkerd Hill)", "Marvel at the monumental 45-meter white Burmese marble Buddha statue commanding sweeping 360-degree views over Chalong Bay and Kata."),
            ("Windmill Viewpoint & Yanui Vista", "Scenic overlook between Ya Nui and Nai Harn beaches featuring rotating white windmills and crystal-clear turquoise waters.")
        ],
        "inclusions": [
            "Round-trip hotel transfers from Patong, Kata, Karon, and Phuket Town",
            "Professional English-speaking licensed local tour guide",
            "Air-conditioned passenger minivan transportation",
            "Admission and temple entrance fees",
            "Complimentary bottled drinking water and cold refreshing towels",
            "Comprehensive travel accident insurance coverage"
        ],
        "exclusions": [
            "Transfers from remote outer areas (Maikhao, Naiyang, Cape Panwa, Rawai - small surcharge applies)",
            "Personal snacks, meals, and specialized souvenir purchases",
            "Gratuities for tour guide and driver (optional)"
        ],
        "timing_text": "Morning Session: 08:30 AM – 01:30 PM.<br />Afternoon Session: 01:30 PM – 06:30 PM (ideal for sunset views).",
        "transport_text": "Pick-up and drop-off included for hotels in Patong, Kata, Karon, and Phuket Town. Remote area transfers arranged on request.",
        "what_to_bring": "Modest clothing covering knees and shoulders for temple visits, comfortable walking shoes, sunscreen, sunglasses, and camera.",
        "contact_tour_param": "Phuket+City+Highlights+Tour",
        "faqs": [
            ("What is the dress code for visiting Wat Chalong and Big Buddha?", "Visitors must dress respectfully when entering temple grounds and sacred religious areas. Shoulders, upper arms, and knees must be covered. Sleeveless tops, miniskirts, short shorts, and transparent clothing are prohibited. Sarongs or cover-ups are available at the entrance if required."),
            ("Are morning or afternoon departures better for the city tour?", "Both sessions offer distinctive highlights. The morning tour benefits from cooler temperatures and quieter temples, while the afternoon departure is timed so you can experience late afternoon golden light and coastal sunset colors from the scenic viewpoints."),
            ("Is the Phuket City Highlights Tour suitable for elderly travelers and families?", "Yes, this tour is very accessible for all age groups. Transport is in air-conditioned minivans, and walking distances between vehicle drop-offs and viewpoints are short and on paved paths. Wheelchair access is available across Wat Chalong's main courtyards."),
            ("Can we customize our stops on this tour?", "Trippovention offers this itinerary both as a small-group join-in tour and as a private chauffeured tour. On the private option, you can adjust timings, linger longer at Phuket Old Town cafes, or add specific photography stops to suit your preferences.")
        ]
    },
    {
        "filename": "phi_phi_maya_bamboo_island_tour.html",
        "title": "Phi Phi, Maya Bay & Bamboo Island Premium Speedboat Tour | Trippovention",
        "h1": "Phi Phi, Maya Bay & Bamboo Island Premium Tour",
        "subtitle": "Maya Bay, Pileh Lagoon, Viking Cave, Monkey Beach, and Pristine Bamboo Island Snorkeling",
        "meta_desc": "Book premium Phi Phi Islands speedboat tour from Phuket including Maya Bay, crystal-clear Pileh Lagoon swimming, Viking Cave, Monkey Beach, and Bamboo Island lunch.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_phi_phi_maya_bamboo.webp",
        "duration": "Full Day (8–9 Hours)",
        "price": "THB 2,100",
        "price_note": "(Per Person)",
        "meetup": "Phuket Royal Marina or Ao Chalong Pier (with hotel transfer)",
        "overview_p1": "Embark on the ultimate Andaman Sea voyage to the world-famous Phi Phi archipelago aboard a modern, twin-engine speedboat. Renowned worldwide for its soaring limestone cliffs, electric-blue lagoons, and powder-soft white sand beaches, Phi Phi stands as Thailand's crowning tropical jewel.",
        "overview_p2": "Walk the iconic powdery white sands of Maya Bay—the setting for 'The Beach'—swim in the emerald waters of enclosed Pileh Lagoon, photograph ancient paintings at Viking Cave, observe macaques at Monkey Beach, and unwind on the secluded coral shores of uninhabited Bamboo Island (Koh Mai Phai) with an authentic beach buffet lunch.",
        "places_col1_title": "Phi Phi Leh Highlights",
        "places_col1_badge": "Limestone Marvels",
        "places_col1_items": [
            ("Maya Bay", "World-renowned enclosed bay framed by 100-meter limestone karsts with pristine coral restoration reefs and baby blacktip reef sharks."),
            ("Pileh Lagoon (Emerald Pool)", "A breathtaking natural lagoon carved into limestone cliffs, offering calm, turquoise waters perfect for jumping and floating."),
            ("Viking Cave & Monkey Beach", "Historic sea cavern where swiftlet birds' nests are harvested, followed by close-up views of wild long-tailed macaques on Monkey Beach.")
        ],
        "places_col2_title": "Bamboo Island & Phi Phi Don",
        "places_col2_badge": "Snorkeling & Relaxation",
        "places_col2_items": [
            ("Bamboo Island (Koh Mai Phai)", "A picture-postcard tropical island encircled by a ring of pure white coral sand and shallow turquoise reef flats."),
            ("Phi Phi Don Island Buffet Lunch", "Delicious Thai and international buffet lunch served at a beachside restaurant overlooking Ton Sai Bay."),
            ("Shark Point & Coral Snorkel Stops", "Two guided open-water snorkeling sessions among schools of sergeant majors, parrotfish, and sea anemones.")
        ],
        "inclusions": [
            "Round-trip hotel transfers by air-conditioned van from major Phuket resort zones",
            "Modern speed boat travel with licensed boat captain and experienced crew",
            "Certified English-speaking marine tour guide",
            "Sanitized snorkeling mask, snorkel, and premium life jacket",
            "Delicious Thai buffet lunch, seasonal fresh tropical fruits, and soft drinks on board",
            "National Park entrance fee assistance and travel accident insurance"
        ],
        "exclusions": [
            "National Park fees (payable in cash at pier: THB 400 per adult, THB 200 per child)",
            "Optional longtail boat ride in Pileh Lagoon (available for rent at lagoon)",
            "Fins/flippers (available for rent at the departure pier)",
            "Personal alcoholic drinks and gratuities"
        ],
        "timing_text": "Full day tour: 07:30 AM pick-up from hotel. Speedboat departs pier at 09:00 AM, returns to pier at 05:00 PM.",
        "transport_text": "Round-trip hotel transfers included for Patong, Kata, Karon, Rawai, Nai Harn, and Phuket Town.",
        "what_to_bring": "Swimwear, beach towel, reef-safe sunscreen, sunglasses, hat, change of clothes, waterproof phone bag, and cash for national park fees.",
        "contact_tour_param": "Phi+Phi+Maya+Bamboo+Island+Tour",
        "faqs": [
            ("Is swimming permitted inside Maya Bay?", "To protect the delicate marine ecosystem and resident blacktip reef sharks, wading into the water at Maya Bay is permitted up to knee height, but full swimming is strictly prohibited by national park authorities. Plenty of deep-water swimming and snorkeling take place at Pileh Lagoon and Bamboo Island."),
            ("Is this speedboat tour safe for pregnant women or people with back problems?", "Speedboat travel across open sea can be bumpy depending on wind and wave conditions. For safety reasons, maritime regulations prohibit pregnant women and passengers with severe back, neck, or spinal problems from joining open-sea speedboat tours."),
            ("Are national park entrance fees included in the tour price?", "National Park entrance fees for the Hat Noppharat Thara-Mu Ko Phi Phi National Park (THB 400 per adult, THB 200 per child) are set by the Thai Department of National Parks and are collected in cash at the marina reception before boarding."),
            ("What happens in case of rough seas or tropical storms?", "Passenger safety is our top operational priority. If the Marine Department issues weather warnings or wave heights exceed safety limits, tours are either rescheduled to a calmer day or rerouted to sheltered bays, or fully refunded.")
        ]
    },
    {
        "filename": "hanuman_world_zipline_and_atv_adventure.html",
        "title": "Hanuman World Zipline & ATV Jungle Adventure Phuket | Trippovention",
        "h1": "Hanuman World Zipline & ATV Adventure",
        "subtitle": "Canopy Ziplining, Sky Walk Bridge, Roller Zipline & Rugged Jungle ATV Expedition",
        "meta_desc": "Experience Hanuman World Phuket with treetop ziplines, roller zipline, sky walk, and thrilling off-road ATV quad biking through lush tropical rainforests.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_hanuman_world_zipline.webp",
        "duration": "Half Day (3–4 Hours) / Full Day",
        "price": "THB 2,200",
        "price_note": "(Per Person)",
        "meetup": "Hanuman World Base Camp, Wichit, Phuket (with hotel transfer)",
        "overview_p1": "Soar high above the rainforest canopy and conquer rugged jungle tracks with Phuket's premier eco-adventure at Hanuman World. Set within 100,000 square meters of lush tropical hillside jungle in Wichit, this state-of-the-art outdoor park combines exhilarating aerial challenges with raw off-road motorized excitement.",
        "overview_p2": "Glide between giant ancient banyan trees across 16 or 30 treetop platforms, spiral down abseil points, conquer sky bridges, and brave the 800-meter-long Roller Zipline—a high-speed twisting gravity coaster through the trees. Follow up with an adrenaline-pumping ATV quad bike trail traversing mud trails, river crossings, and hillside ridges.",
        "places_col1_title": "Canopy & Roller Zipline Thrills",
        "places_col1_badge": "Aerial Adventure",
        "places_col1_items": [
            ("Treetop Zipline Course", "Fly across up to 30 jungle platforms connected by high-speed dual-wire cable ziplines reaching lengths of up to 400 meters."),
            ("Twisting Roller Zipline", "An 800-meter roller coaster zipline curving, diving, and swooping through the forest branches at up to 40 km/h."),
            ("Sky Walk Treetop Bridge", "Elevated timber canopy walkway offering 360-degree panoramic rainforest views and educational insights on tropical flora.")
        ],
        "places_col2_title": "All-Terrain Vehicle (ATV) Safari",
        "places_col2_badge": "Off-Road Action",
        "places_col2_items": [
            ("Jungle Trail ATV Track", "Guide-led quad bike expedition navigating gravel tracks, natural forest obstacles, mud pits, and steep hill climbs."),
            ("Panoramic Ridge Stops", "Scenic jungle viewpoint halts overlooking Phuket's forested interior with photography breaks."),
            ("Safety Briefing & Training Track", "Introductory practice circuit to master quad bike steering, throttle control, and braking before tackling the wild trails.")
        ],
        "inclusions": [
            "Round-trip hotel transfers from major Phuket beach districts",
            "World-standard Petzl harnesses, dual safety carabiners, and climbing helmets",
            "Expert certified English-speaking safety instructors (2 guides per small group)",
            "Automatic ATV quad bike hire, safety helmet, and protective goggles",
            "Complimentary drinking water, seasonal fruit refreshments, and locker storage",
            "First-aid certified staff and comprehensive accident insurance"
        ],
        "exclusions": [
            "Souvenir action photos and onboard GoPro video recordings (available for purchase)",
            "Buffet lunch (included only on selected full-day combination packages)",
            "Personal spending and instructor tips"
        ],
        "timing_text": "Morning Departures: 08:00 AM, 10:00 AM.<br />Afternoon Departures: 01:00 PM, 03:00 PM.",
        "transport_text": "Hotel pickup available across Patong, Kata, Karon, Rawai, Kamala, and Phuket Town.",
        "what_to_bring": "Comfortable athletic clothes, closed-toe sports shoes (mandatory; no flip-flops), insect repellent, and sunscreen.",
        "contact_tour_param": "Hanuman+World+Zipline+ATV+Adventure",
        "faqs": [
            ("What are the age, height, and weight restrictions for ziplining?", "Participants must be at least 4 years old. The maximum weight limit for zipline and roller zipline activities is 120 kg (264 lbs). Pregnant women and individuals with heart conditions or spinal injuries cannot participate."),
            ("Do I need a driver's license to ride an ATV quad bike?", "No formal driver's license is required. Operators must be at least 15 years old to drive an ATV independently. Children aged 4–14 can ride as passengers behind an adult rider or instructor on double quad bikes."),
            ("What footwear is required for Hanuman World?", "Sturdy closed-toe athletic sneakers or hiking shoes are mandatory. Open-toe sandals, flip-flops, crocs, and high heels are strictly forbidden on ziplines and ATVs for safety reasons."),
            ("Are lockers available to store personal items and phones?", "Yes, complimentary secure electronic lockers are provided at the welcome lounge to store bags, wallets, and non-essential items. Small zipped waist pouches or secured neck-strap phone cases are allowed on the course.")
        ]
    },
    {
        "filename": "simon_cabaret_show_phuket.html",
        "title": "Phuket Simon Cabaret Show Tickets & Transfers | Trippovention",
        "h1": "Phuket Simon Cabaret Show",
        "subtitle": "World-Famous Transgender Cultural Music, Dance & Extravagant Costume Spectacular in Patong",
        "meta_desc": "Reserve VIP seats for Phuket Simon Cabaret in Patong. Enjoy world-class theatrical performances, stunning glamour costumes, and dynamic music and dance choreography.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_simon_cabaret_show.webp",
        "duration": "1 Hour 15 Minutes",
        "price": "THB 900",
        "price_note": "(Per Person)",
        "meetup": "Simon Cabaret Theatre (Sirirat Road, Patong Beach) or Hotel Transfer",
        "overview_p1": "Since opening its doors in 1991, Phuket Simon Cabaret has established itself as one of Southeast Asia's most iconic and celebrated theatrical entertainment shows. Housed in an intimate, air-conditioned 600-seat theatre on Sirirat Road in South Patong, the show delivers a dazzling, family-friendly evening of glamour, comedy, and high-energy showmanship.",
        "overview_p2": "Featuring an exceptional cast of talented transgender performers adorned in feathered headdresses, sparkling crystal ballgowns, and elaborate cultural regalia, the show takes audiences on a whirlwind musical journey spanning Hollywood Broadway, Bollywood extravaganzas, traditional Thai folklore, Chinese operatics, and modern pop anthems.",
        "places_col1_title": "Theatrical & Musical Acts",
        "places_col1_badge": "World Music & Dance",
        "places_col1_items": [
            ("Broadway & Hollywood Divas", "Show-stopping tributes to international divas with synchronized choreography and shimmering sequined gowns."),
            ("Carnival & Latin Rhythms", "High-tempo Rio-style carnival acts with cascading plumes of colorful ostrich feathers and infectious Latin beats."),
            ("Asian Cultural Extravaganzas", "Graceful classical routines featuring authentic Thai, Korean, and Chinese courtly dance traditions and folklore.")
        ],
        "places_col2_title": "Theatre & Production Features",
        "places_col2_badge": "World-Class Staging",
        "places_col2_items": [
            ("State-of-the-Art Sound & Lighting", "Cutting-edge surround sound acoustics, moving spotlight rigs, and dynamic projection backdrops."),
            ("VIP Amphitheatre Seating", "Comfortable, tiered VIP velvet seats on the ground level providing unobstructed stage sightlines."),
            ("Post-Show Courtyard Meet & Greet", "Opportunity to take memorable souvenir photos with the glamourous stars in the outdoor theatre plaza.")
        ],
        "inclusions": [
            "Official reserved admission ticket to Phuket Simon Cabaret",
            "Choice of VIP Main Floor or Standard Upper Tier seating",
            "75-minute live theatrical performance with full ensemble cast",
            "Air-conditioned theatre access with plush seating",
            "Optional round-trip hotel transfer from Patong, Karon, or Kata"
        ],
        "exclusions": [
            "Round-trip hotel transfers (unless transfer option is selected)",
            "Beverages, drinks, and snacks from the lobby bar",
            "Photo tips for performers during the post-show courtyard meet-and-greet (customary THB 100 per photo)"
        ],
        "timing_text": "Daily Showtimes: 06:00 PM, 07:30 PM, and 09:00 PM.<br />Doors open 30 minutes prior to performance.",
        "transport_text": "Located at 8 Sirirat Road, Patong Beach, Kathu, Phuket. Hotel pickup available from all major beach zones.",
        "what_to_bring": "Smart casual attire, camera for exterior and courtyard photos, and cash for post-show photo gratuities.",
        "contact_tour_param": "Phuket+Simon+Cabaret+Show",
        "faqs": [
            ("Is Phuket Simon Cabaret suitable for children and families?", "Yes, Simon Cabaret is completely family-friendly. It is a world-class theatrical song-and-dance musical revue without any explicit content, nudity, or offensive language. Audiences of all ages, including seniors and young children, enjoy the vibrant colors and joyful music."),
            ("Is photography or video recording allowed inside the theatre during the show?", "No, photography and video recording inside the auditorium during the performance are strictly prohibited to respect copyright and avoid distracting performers. However, you can take photos outside with the cast in the courtyard after the show."),
            ("What is the difference between VIP and Regular seating?", "VIP seats are located in the central orchestra rows on the lower tier close to the stage, providing the best sightlines and immersion. Regular seats are situated on the raised upper tier and outer flanks."),
            ("How early should we arrive before showtime?", "We recommend arriving at the theatre 30 to 45 minutes before curtain call to collect your physical seat tickets from the box office, enjoy a welcome beverage at the bar, and find your seats comfortably.")
        ]
    },
    {
        "filename": "aquaria_phuket_tickets.html",
        "title": "Aquaria Phuket & AR Trick Eye Museum Tickets | Trippovention",
        "h1": "Aquaria Phuket & AR Trick Eye Museum",
        "subtitle": "Thailand's Largest Oceanarium, 25,000+ Marine Creatures & Interactive 4D Trick Eye Art",
        "meta_desc": "Visit Aquaria Phuket at Central Phuket Floresta. Explore 4 thematic ocean zones, stingray feeding, mermaid shows, and the mind-bending AR Trick Eye Museum.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_aquaria_phuket.webp",
        "duration": "2–3 Hours",
        "price": "THB 850",
        "price_note": "(Per Person)",
        "meetup": "Aquaria Phuket (B1 Floor, Central Phuket Floresta, Wichit, Phuket)",
        "overview_p1": "Escape into an enchanting underwater world at Aquaria Phuket, the largest and most advanced oceanarium in Thailand. Situated beneath the upscale Central Phuket Floresta luxury mall in Phuket Town, this 104,000-square-foot indoor marine park holds over 7 million liters of water and is home to more than 25,000 marine animals across 300 diverse aquatic species.",
        "overview_p2": "Journey through four immersive thematic zones: the freshwater Mystic Forest inspired by Thai mythology, the Coastal Haven featuring playful Humboldt penguins and otters, the South China Sea main ocean tank with soaring stingrays and zebra sharks, and the Station Aquarius touch pools. Combine your visit with the adjoining AR Trick Eye Museum, where optical illusion 3D murals come alive through augmented reality.",
        "places_col1_title": "Aquarium Thematic Zones",
        "places_col1_badge": "Marine Wonder",
        "places_col1_items": [
            ("Ocean Myth & Main Giant Tank", "Thailand's largest acrylic ocean observation window featuring blacktip reef sharks, giant rays, sea turtles, and schooling trevallies."),
            ("Mystic Forest & Giant Freshwater Fish", "Discover monster freshwater species including Mekong giant catfish, arapaimas, and freshwater stingrays in ancient temple settings."),
            ("Penguin & Otter Cove (Coastal Haven)", "Encounter charismatic Humboldt penguins waddling across rocks and playful Asian small-clawed otters.")
        ],
        "places_col2_title": "Interactive Shows & AR Trick Eye",
        "places_col2_badge": "4D Entertainment",
        "places_col2_items": [
            ("Live Mermaid & Diver Feeding Shows", "Enchanting live mermaid synchronized underwater swimming performances and thrilling shark and ray feedings."),
            ("AR Trickeye Museum 4D Optical Illusions", "Interact with lifelike 3D wall paintings and augmented reality animations using a mobile app to create incredible photos."),
            ("Touch Pool Interactive Lab", "Gently touch live starfish, sea cucumbers, and horseshoe crabs under marine educator supervision.")
        ],
        "inclusions": [
            "Official admission ticket to Aquaria Phuket Oceanarium",
            "Admission ticket to AR Trick Eye 4D Optical Illusion Museum",
            "Access to all daily animal feeding sessions and live mermaid performances",
            "Use of interactive touch pool and educational discovery zones",
            "Full air-conditioned indoor comfort and wheelchair access"
        ],
        "exclusions": [
            "Hotel transfers (can be added on request)",
            "Dining at the underwater restaurant (Su Va Na)",
            "Behind-the-scenes guided tour or VR underwater experiences",
            "Professional souvenir printed photos"
        ],
        "timing_text": "Open daily from 10:30 AM to 07:00 PM (Last admission at 06:00 PM).<br />Mermaid shows scheduled daily at 01:30 PM and 03:30 PM.",
        "transport_text": "Located on Floor B1, Central Phuket Floresta, Wichit, Mueang Phuket. Free underground mall parking available.",
        "what_to_bring": "Smartphone with fully charged battery and camera for 3D photos, light cardigan or sweater (aquarium is pleasantly cool).",
        "contact_tour_param": "Aquaria+Phuket+Tickets",
        "faqs": [
            ("Is Aquaria Phuket suitable for rainy days in Phuket?", "Aquaria Phuket is the premier rainy-day attraction on the island. Fully indoor and air-conditioned within Central Phuket Floresta, visitors can spend hours admiring marine life, enjoying 4D optical illusions, and browsing world-class shopping and dining without worrying about tropical weather."),
            ("How do we use the AR Trick Eye Museum app?", "Before entering the Trick Eye Museum, download the free 'XR Museum' app on your iOS or Android smartphone. Pointing your camera at the 3D murals triggers animated augmented-reality effects like erupting volcanoes, swimming sea dragons, and flying fairies."),
            ("How long does a visit to Aquaria Phuket take?", "A leisurely visit through Aquaria Phuket takes approximately 1.5 to 2 hours. Exploring the AR Trick Eye Museum takes an additional 45 to 60 minutes, making the combined experience roughly 2.5 to 3 hours."),
            ("Can we dine inside the aquarium?", "Yes, Aquaria is home to 'Su Va Na', an exclusive marine fine-dining restaurant where guests can enjoy gourmet meals directly beside the main giant ocean aquarium tank. Advance table reservations are required.")
        ]
    },
    {
        "filename": "phuket_thai_cooking_class.html",
        "title": "Authentic Thai Cooking Class with Local Market Tour Phuket | Trippovention",
        "h1": "Authentic Thai Cooking Class with Market Tour",
        "subtitle": "Chef-Guided Fresh Market Ingredient Selection & Hands-On 4-Course Thai Culinary Workshop",
        "meta_desc": "Learn to cook authentic Thai dishes in Phuket. Enjoy guided morning market tour, master classic curries, Pad Thai, Tom Yum, and mango sticky rice with your recipe book.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_thai_cooking_class.webp",
        "duration": "Half Day (4 Hours)",
        "price": "THB 1,600",
        "price_note": "(Per Person)",
        "meetup": "Culinary School in Kathu / Chalong (with hotel transfer)",
        "overview_p1": "Uncover the secrets of Thailand's internationally acclaimed gastronomy with an interactive, hands-on cooking masterclass in Phuket. Beyond learning recipes, this immersive culinary journey teaches you how to balance the fundamental flavor pillars of Thai food: sweet, sour, salty, spicy, and creamy.",
        "overview_p2": "Begin with a guided morning visit to a bustling local produce market to touch, smell, and select fresh galangal, kaffir lime leaves, lemongrass, and Thai chilies. At your individual cooking station, pound fresh curry paste from scratch with a stone mortar, cook four classic Thai dishes under expert chef supervision, and feast upon your own delicious creations.",
        "places_col1_title": "Market Tour & Master Skills",
        "places_col1_badge": "Hands-On Cooking",
        "places_col1_items": [
            ("Local Morning Produce Market", "Guided exploration of a local fresh market, learning to identify exotic herbs, tropical produce, and freshly pressed coconut cream."),
            ("Handmade Curry Paste from Scratch", "Pound fresh shallots, garlic, dried red chilies, coriander root, and lemongrass in a traditional granite mortar and pestle."),
            ("Individual Cooking Workstations", "Fully equipped prep counter and dedicated gas wok burner with personalized step-by-step guidance.")
        ],
        "places_col2_title": "4-Course Menu Highlights",
        "places_col2_badge": "Signature Dishes",
        "places_col2_items": [
            ("Tom Yum Goong / Tom Kha Gai", "Iconic hot and sour prawn soup infused with lemongrass and lime, or velvety coconut chicken galangal soup."),
            ("Pad Thai Goong / Green Chicken Curry", "Stir-fried rice noodles with tamarind sauce and tiger prawns, or fragrant Green Curry (Gaeng Keow Wan)."),
            ("Mango Sticky Rice (Khao Niew Mamuang)", "Sweet warm coconut sticky rice served with ripe golden honey mangoes and toasted mung beans.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transfers from major beach resorts",
            "Chef-guided walking tour of the local fresh morning market",
            "All fresh organic cooking ingredients, spices, and cooking equipment",
            "Individual cooking workstation with gas stove and apron",
            "Four full courses prepared, cooked, and savored by you",
            "Printed full-color recipe booklet and official culinary certificate"
        ],
        "exclusions": [
            "Alcoholic beverages and beer (available for purchase)",
            "Specialized take-home spices and mortar sets (optional on-site store)",
            "Chef and kitchen crew gratuities"
        ],
        "timing_text": "Morning Class (includes market tour): 09:00 AM – 01:00 PM.<br />Afternoon Class (garden herbal tour): 02:00 PM – 06:00 PM.",
        "transport_text": "Hotel transfers included from Patong, Kata, Karon, Kamala, and Phuket Town.",
        "what_to_bring": "Comfortable light clothing, empty stomach to enjoy your culinary creations, and camera for cooking action photos.",
        "contact_tour_param": "Phuket+Thai+Cooking+Class",
        "faqs": [
            ("Can dietary requirements like vegetarian, vegan, or gluten-free be accommodated?", "Yes, absolutely! At your personal cooking station, all ingredients are prepped individually. We easily substitute tofu, mushrooms, gluten-free tamari, or adjust chili spice levels according to your personal dietary needs."),
            ("Do I need any previous cooking experience to join the class?", "Not at all. Our cooking classes are designed for beginners, enthusiastic home cooks, and food lovers of all levels. Our English-speaking Thai chef provides clear, step-by-step instructions and assists throughout."),
            ("Can children participate in the cooking class?", "Children aged 7 and above can actively cook at their own station under parental supervision. Children aged 4–6 can join as accompanying observers or share a cooking station with a parent."),
            ("Do we receive the recipes to take home?", "Yes, every participant receives a beautifully printed recipe booklet complete with ingredient measurements, substitution guides, and step-by-step cooking instructions to recreate your favorite Thai meals at home.")
        ]
    },
    {
        "filename": "coral_and_racha_island_tour.html",
        "title": "Coral & Racha Island Speedboat Snorkeling Tour from Phuket | Trippovention",
        "h1": "Coral & Racha Island Speedboat Day Tour",
        "subtitle": "Turquoise Waters of Koh Hey, Banana Beach Water Sports & Racha Yai Coral Snorkeling",
        "meta_desc": "Discover Coral Island (Koh Hey) and Racha Yai on a full-day speedboat excursion from Phuket. Enjoy white sandy beaches, vibrant coral reefs, and buffet lunch.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_coral_and_racha_island.webp",
        "duration": "Full Day (7–8 Hours)",
        "price": "THB 1,450",
        "price_note": "(Per Person)",
        "meetup": "Chalong Pier, Phuket (with round-trip hotel transfer)",
        "overview_p1": "Escape to two of Phuket's most beautiful neighboring islands on a scenic speedboat day cruise to Coral Island (Koh Hey) and Racha Yai Island (Koh Racha). Located just 9 and 20 kilometers south of Phuket respectively, these islands offer tranquil tropical shores, crystal-clear visibility, and powdery white sand beaches.",
        "overview_p2": "Spend your morning at Coral Island's vibrant Banana Beach, relaxing under swaying palm trees or engaging in optional thrilling water sports such as parasailing, sea walking, or banana boat rides. In the afternoon, cruise to Racha Yai to snorkel in translucent aquamarine bays surrounded by colorful parrotfish, triggerfish, and living coral reefs.",
        "places_col1_title": "Coral Island (Koh Hey)",
        "places_col1_badge": "Beach & Water Sports",
        "places_col1_items": [
            ("Banana Beach / Long Beach", "Stunning curve of white sand fringed by jungle hills, perfect for sunbathing, swimming, and beach photography."),
            ("Optional Thrill Water Sports", "Participate in thrilling parasailing over the bay, sea walking along the seabed, or banana boat rides."),
            ("Shallow Reef Snorkeling", "Snorkel directly off the beach among schools of butterflyfish and vibrant sea urchins.")
        ],
        "places_col2_title": "Racha Yai Island (Koh Racha)",
        "places_col2_badge": "Aquamarine Snorkeling",
        "places_col2_items": [
            ("Patok Bay & Siam Bay", "Horseshoe-shaped sheltered bays boasting crystal-clear underwater visibility up to 25 meters deep."),
            ("Deep Coral Reef Snorkel Stop", "Open-water boat snorkeling session guided by marine instructors over healthy coral garden heads."),
            ("Island Buffet Lunch", "Relish a hearty Thai buffet lunch served at a cliffside or beachside island restaurant.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transfers from major Phuket beach districts",
            "Modern high-speed twin-engine boat with experienced captain and crew",
            "Professional English-speaking licensed marine guide",
            "Sanitized snorkeling mask, snorkel tube, and life jacket",
            "Delicious Thai buffet lunch, drinking water, and seasonal fruits",
            "Comprehensive travel accident insurance coverage"
        ],
        "exclusions": [
            "Optional beach water sports (parasailing, sea walking, scuba, banana boat)",
            "Beach lounge chair hire fees on Coral Island (approx. THB 50–100)",
            "Fins/flippers rental (available at pier)",
            "Personal spending, alcoholic drinks, and gratuities"
        ],
        "timing_text": "Full day tour: 08:00 AM hotel pickup. Speedboat departs Chalong Pier at 09:00 AM, returns at 04:30 PM.",
        "transport_text": "Hotel pickup included for Patong, Kata, Karon, Rawai, Nai Harn, and Chalong.",
        "what_to_bring": "Swimwear, beach towel, reef-safe sun cream, sunglasses, hat, change of clothes, and pocket money for optional water sports.",
        "contact_tour_param": "Coral+and+Racha+Island+Tour",
        "faqs": [
            ("How far are Coral and Racha Islands from Phuket?", "Coral Island is only 15 minutes by speedboat from Chalong Pier, making it an easy, gentle boat ride. Continuing to Racha Yai takes approximately 25 to 30 minutes. This makes it an ideal island excursion for families with young children or those prone to seasickness."),
            ("Can we book water sports like parasailing or sea walking on the day?", "Yes, you can easily purchase water sports directly upon arrival at Banana Beach on Coral Island. Trippovention guides can help you book certified instructors for parasailing, sea walking helmet diving, or banana boat fun."),
            ("Is Coral and Racha Island suitable for beginner snorkelers?", "Yes! Coral Island features shallow, calm waters right off the beach where beginners and children can safely wade with masks and spot fish. Racha Yai provides deeper, crystalline waters with superior clarity for intermediate snorkelers."),
            ("Are beach chairs and umbrellas available on the islands?", "Yes, shaded beach loungers and parasols are available along both Long Beach and Banana Beach on Coral Island for a nominal fee of THB 50 to 100 per day.")
        ]
    },
    {
        "filename": "similan_islands_snorkeling_tour.html",
        "title": "Similan Islands Snorkeling Day Tour from Phuket (Seasonal) | Trippovention",
        "h1": "Similan Islands Snorkeling Excursion",
        "subtitle": "World-Renowned Granite Boulders, Donald Duck Bay & Sea Turtle Snorkeling (Open Oct 15–May 15)",
        "meta_desc": "Experience world-class snorkeling at Similan Islands National Park from Phuket. Visit Donald Duck Bay, Sail Rock, pristine crystal beaches, and coral reefs with sea turtles.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_similan_islands_snorkeling.webp",
        "duration": "Full Day (10–12 Hours)",
        "price": "THB 2,800",
        "price_note": "(Per Person)",
        "meetup": "Thap Lamu Pier / Phuket Hotel Pickup (early morning departure)",
        "overview_p1": "Venture into one of the world's top ten marine destinations with an exhilarating day tour to the Similan Islands Marine National Park (Mu Ko Similan). Located 85 kilometers northwest of Phuket in the Andaman Sea, this pristine archipelago of nine granite islands is celebrated for its powder-soft white beaches, towering megalithic granite formations, and crystalline turquoise seas.",
        "overview_p2": "Strictly open to visitors only seven months a year (from October 15 to May 15) to preserve its delicate ecosystem, the Similans offer world-class snorkeling. Hike up to the iconic Sail Rock overlooking Donald Duck Bay on Koh Similan (Island No. 8), swim alongside wild green sea turtles at Koh Ba Ngu (Island No. 9), and relax on the white sands of Princess Bay on Koh Miang (Island No. 4).",
        "places_col1_title": "Koh Similan (Island No. 8)",
        "places_col1_badge": "Iconic Landscapes",
        "places_col1_items": [
            ("Sail Rock & Donald Duck Bay", "Hike up the natural granite staircase to the world-famous Sail Rock viewpoint overlooking the electric-blue bay below."),
            ("Pristine Coral Beach", "Sink your toes into sand so fine and white it feels like powdered flour, fringed by dramatic wind-sculpted granite boulders."),
            ("Snorkeling at Hin Phousar", "Explore underwater granite swim-throughs teeming with clownfish, blue-spotted rays, and moray eels.")
        ],
        "places_col2_title": "Koh Miang & Koh Ba Ngu",
        "places_col2_badge": "Turtle & Coral Encounters",
        "places_col2_items": [
            ("Koh Ba Ngu (Island No. 9) Snorkel", "Prime snorkeling spot known as Christmas Point, famous for sightings of wild hawksbill and green sea turtles."),
            ("Princess Bay (Koh Miang No. 4)", "Idyllic island hosting national park headquarters, offering lush rainforest walking trails and two breathtaking beaches."),
            ("East of Eden Reef Gardens", "Marvel at sprawling staghorn, brain, and table corals bathed in exceptional 30-meter water visibility.")
        ],
        "inclusions": [
            "Round-trip transfers by comfortable air-conditioned van from Phuket hotels to Thap Lamu Pier",
            "Speedboat journey with certified boat captain and trained crew",
            "Professional English-speaking marine ecologist tour guide",
            "Sanitized premium snorkel mask, breathing tube, and life vest",
            "Light breakfast at departure pier, picnic buffet lunch, snacks, and fresh tropical fruit",
            "Official Similan National Park entrance fee and government insurance"
        ],
        "exclusions": [
            "Fins/flippers (available for rent at Thap Lamu Pier)",
            "Personal spending, specialized souvenirs, and guide gratuities",
            "Accommodation on the islands (overnight stays are no longer permitted by National Parks)"
        ],
        "timing_text": "Seasonal Operation: Open October 15 to May 15 only.<br />Pick-up from Phuket: 05:45 AM – 06:30 AM. Returns to hotel: approx. 07:00 PM.",
        "transport_text": "Round-trip transfers included from Patong, Kata, Karon, Kamala, Bang Tao, and Phuket Town to Thap Lamu Pier.",
        "what_to_bring": "Copy of passport ID (mandatory for national park registration), swimwear, beach towel, reef-friendly sun cream, and camera.",
        "contact_tour_param": "Similan+Islands+Snorkeling+Tour",
        "faqs": [
            ("Why are the Similan Islands only open from October 15 to May 15?", "The Thai Department of National Parks strictly closes the Similan Islands from May 16 to October 14 each year during the monsoon season. This mandatory closure ensures passenger safety during monsoon swells and allows marine ecosystems, coral reefs, and nesting sea turtles to regenerate without human disturbance."),
            ("Why is passport information required for booking?", "Under Thai National Park regulations, all visitors to the Similan Islands must be registered in advance with their full name, nationality, and passport number. Please provide accurate details when booking and bring a digital or paper copy of your passport on the tour day."),
            ("Are shoes allowed on the Similan Islands?", "To protect the fine coral sands, outdoor shoes and hard-soled footwear must be removed before stepping onto the islands. Only barefoot walking or soft neoprene aqua swimming socks are permitted on the beaches and trails."),
            ("How long is the boat ride from the pier to the Similans?", "The speedboat journey from Thap Lamu Pier in Phang Nga to the first Similan island takes approximately 75 to 90 minutes across open sea. Motion sickness tablets are provided complimentary at the pier before departure.")
        ]
    },
    {
        "filename": "phuket_sunset_catamaran_cruise.html",
        "title": "Phuket Sunset Catamaran Yacht Cruise to Promthep Cape | Trippovention",
        "h1": "Phuket Sunset Catamaran Yacht Cruise",
        "subtitle": "Luxury Sailing to Promthep Cape & Koh Hey, Tropical Sunset Canapés & Onboard DJ Music",
        "meta_desc": "Sail the Andaman Sea on a luxury sailing catamaran cruise from Phuket. Witness spectacular sunsets at Promthep Cape, enjoy snorkeling, drinks, and barbecue dinner on board.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_sunset_catamaran_cruise.webp",
        "duration": "5 Hours (Late Afternoon to Dusk)",
        "price": "THB 1,950",
        "price_note": "(Per Person)",
        "meetup": "Chalong Pier / Kan Eang Pier (with hotel transfer)",
        "overview_p1": "Indulge in the ultimate romantic maritime experience aboard a sleek, double-hulled luxury sailing catamaran cruise off the southern coast of Phuket. Designed for travelers seeking relaxed elegance, great music, and unforgettable golden-hour vistas, this afternoon-to-sunset voyage showcases the dramatic coastal headlands of Phuket from the sea.",
        "overview_p2": "Cruise past scenic rocky coves to Coral Island for an afternoon of refreshing swimming, stand-up paddleboarding, and snorkeling. As the sun begins its descent, hoist the sails toward Promthep Cape and Laem Krating. Relax on the forward trampoline netting with chilled wine and freshly prepared BBQ dinner while watching the sky ignite into fiery crimson and violet hues.",
        "places_col1_title": "Afternoon Island Exploration",
        "places_col1_badge": "Tropical Cruising",
        "places_col1_items": [
            ("Coral Island (Koh Hey) Mooring", "Drop anchor in a calm turquoise bay for refreshing ocean dips, snorkeling among reef fish, or stand-up paddleboarding."),
            ("Luxury Catamaran Deck Lounging", "Stretch out on wide trampoline sun nets suspended above the waves or relax in the shaded cockpit lounge."),
            ("Water Toys & Ocean Fun", "Complimentary use of inflatable sea floats, snorkeling gear, and stand-up paddleboards.")
        ],
        "places_col2_title": "Promthep Cape Golden Hour",
        "places_col2_badge": "Sunset Spectacle",
        "places_col2_items": [
            ("Promthep Cape from the Ocean", "Unobstructed view of Phuket's southernmost peninsula bathed in vibrant orange and magenta twilight."),
            ("Onboard Sunset BBQ Dinner", "Savor grilled chicken skewers, fresh seafood satay, seasonal salads, and tropical fruits prepared fresh by onboard chefs."),
            ("Sunset Toast & Chillout Music", "Sip a complimentary glass of sparkling wine as the sun dips below the Andaman horizon to ambient lounge music.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transfers from Patong, Kata, Karon, Rawai, and Chalong",
            "5-hour sailing excursion aboard a modern luxury sailing catamaran",
            "Welcome tropical mocktail and chilled refreshing towel upon boarding",
            "Onboard dinner with BBQ skewers, Thai specialties, and fresh seasonal fruit",
            "One complimentary glass of wine or sparkling toast per adult",
            "Snorkeling equipment, life jackets, and stand-up paddleboard usage",
            "Comprehensive marine accident insurance"
        ],
        "exclusions": [
            "Additional alcoholic drinks, cocktails, and beer (available at onboard cash bar)",
            "Transfers from remote northern Phuket areas (Bang Tao, Mai Khao - surcharge applies)",
            "Crew and captain gratuities"
        ],
        "timing_text": "Afternoon departure: 01:00 PM – 01:45 PM hotel pickup. Catamaran sails 02:30 PM to 07:00 PM.",
        "transport_text": "Round-trip transfers included from Kata, Karon, Patong, Rawai, Nai Harn, and Chalong.",
        "what_to_bring": "Resort-casual swimwear or sunset cruise attire, sunglasses, light windbreaker jacket for post-sunset breeze, and camera.",
        "contact_tour_param": "Phuket+Sunset+Catamaran+Cruise",
        "faqs": [
            ("Is a catamaran cruise more stable than a monohull speedboat?", "Yes, catamarans feature two parallel hulls providing significantly greater stability, minimal rocking, and expansive flat deck space. This makes them exceptionally comfortable, smooth, and ideal for passengers who might typically feel seasick."),
            ("Is this tour suitable for couples and romantic occasions?", "The sunset catamaran cruise is widely regarded as one of Phuket's top romantic experiences for couples, anniversaries, honeymooners, and small groups of friends celebrating special occasions in a relaxed, elegant atmosphere."),
            ("Can we swim and snorkel during the cruise?", "Yes, the catamaran anchors at a sheltered bay off Coral Island for approximately 90 minutes during the afternoon, allowing guests to swim, use snorkel equipment, or paddle on stand-up paddleboards before sailing to the sunset viewpoint."),
            ("What happens if it rains during the sunset cruise?", "The catamaran features a large covered saloon and shaded dining cockpit with panoramic windows. If light rain occurs, guests stay dry while sailing. In case of severe weather advisories, the trip is rescheduled or fully refunded.")
        ]
    },
    {
        "filename": "phuket_scuba_diving_day_trip.html",
        "title": "Phuket Scuba Diving Day Trip to Racha Yai (2 Dives) | Trippovention",
        "h1": "Phuket Scuba Diving Day Trip (Racha Yai)",
        "subtitle": "Certified & Discover Scuba Diving with PADI Instructors, Underwater Statues & Coral Reefs",
        "meta_desc": "Experience premier scuba diving from Phuket at Racha Yai Island. Includes 2 guided boat dives, full scuba gear, PADI divemasters, and onboard breakfast & buffet lunch.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_scuba_diving_day_trip.webp",
        "duration": "Full Day (7–8 Hours)",
        "price": "THB 3,400",
        "price_note": "(Per Person)",
        "meetup": "Chalong Pier Dive Boat Departure (with hotel transfer)",
        "overview_p1": "Delve beneath the crystal-clear waters of the Andaman Sea with a premier scuba diving day trip to Racha Yai Island. Situated 20 kilometers south of Phuket, Racha Yai is internationally renowned for its calm, sheltered bays, exceptional underwater visibility ranging from 15 to 30 meters, and diverse marine life.",
        "overview_p2": "Whether you are a certified diver looking to explore submerged motorbikes and concrete elephant statues at Siam Bay, or a complete beginner eager to experience Discover Scuba Diving for the first time, our professional PADI instructors provide safe, small-ratio guided dives. Enjoy a spacious 3-deck dive boat equipped with sundeck, dive platform, and freshly cooked buffet meals.",
        "places_col1_title": "Racha Yai Dive Sites",
        "places_col1_badge": "Submerged Wonders",
        "places_col1_items": [
            ("Siam Bay & Underwater Sculptures", "Explore submerged concrete elephant statues, giant oyster shells, and temple gate replicas covered in soft corals."),
            ("Bungalow Bay Reefs", "Sheltered bay with a gentle sloping sandy bottom, hard coral pinnacles, moray eels, and schools of yellowtail barracuda."),
            ("Homerock & Lucy's Reef", "Vibrant drift dive site adorned with gorgonian sea fans, anemone clownfish colonies, and occasional passing manta rays.")
        ],
        "places_col2_title": "Vessel Comfort & PADI Standards",
        "places_col2_badge": "First-Class Service",
        "places_col2_items": [
            ("Spacious 3-Deck Custom Dive Vessel", "Large dive deck, freshwater rinse showers, air-conditioned saloon, and rooftop padded sun terrace."),
            ("PADI Certified Instruction", "Small diver ratios (maximum 4 certified divers per divemaster; 2 beginners per instructor) for personalized safety."),
            ("Freshly Cooked Onboard Meals", "Hot breakfast served during the outward cruise, followed by a delicious freshly prepared Thai buffet lunch.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transfers from Patong, Kata, Karon, Rawai, and Chalong",
            "Two guided open-water boat dives at Racha Yai with PADI Divemaster/Instructor",
            "Full scuba equipment hire (BCD, regulator, wetsuit, mask, fins, weights, and tanks)",
            "Freshly prepared hot breakfast, buffet lunch, afternoon snacks, and fresh fruits",
            "Unlimited drinking water, coffee, tea, and electrolytes",
            "Specialized hyperbaric chamber diver insurance coverage"
        ],
        "exclusions": [
            "Optional 3rd dive (available on board for certified divers: THB 800)",
            "Underwater photography/GoPro hire or private camera guide",
            "Nitrox tank fills (available for certified Enriched Air divers)",
            "Crew and dive guide gratuities"
        ],
        "timing_text": "Full day tour: 07:15 AM – 07:45 AM hotel pickup. Dive boat departs Chalong at 08:30 AM, returns at 04:30 PM.",
        "transport_text": "Hotel transfers included from Patong, Karon, Kata, Chalong, Rawai, and Nai Harn.",
        "what_to_bring": "Diver certification card and logbook (for certified divers), swimwear, towel, dry clothes, and sunscreen.",
        "contact_tour_param": "Phuket+Scuba+Diving+Day+Trip",
        "faqs": [
            ("Can beginners dive without a scuba certification?", "Yes! Beginners can participate in the PADI Discover Scuba Diving (DSD) program. You will receive an easy-to-understand safety and equipment briefing from a certified PADI instructor, practice basic breathing skills in shallow water, and complete two guided dives up to a maximum depth of 12 meters."),
            ("How long must I wait before flying after scuba diving?", "Under standard international diving medical guidelines, you must allow a minimum of 18 hours (24 hours recommended) between your last dive and boarding a commercial aircraft. Do not book a diving tour if you have a flight departing the following morning."),
            ("What marine life can I expect to see at Racha Yai?", "Racha Yai is home to a rich variety of marine species including sea turtles, honeycomb moray eels, blue-spotted ribbon-tail stingrays, giant trevallies, lionfish, pufferfish, and colorful anemone clownfish."),
            ("Can non-diving family members or friends join the boat as snorkelers?", "Yes! Non-diving companions are welcome to join as snorkelers or boat passengers at a discounted rate. They can enjoy the spacious sun deck, delicious onboard meals, and snorkel in the crystal-clear shallow bays while divers are underwater.")
        ]
    },
    {
        "filename": "phuket_old_town_heritage_walking_tour.html",
        "title": "Phuket Old Town Heritage & Street Food Walking Tour | Trippovention",
        "h1": "Phuket Old Town Heritage & Street Food Tour",
        "subtitle": "Sino-Portuguese Architecture on Thalang Road, Soi Romanee Murals & UNESCO Gastronomy Tastings",
        "meta_desc": "Explore Phuket Old Town with a local heritage guide. Discover Sino-Portuguese shophouses, street art murals, historic Chinese shrines, and authentic Peranakan delicacies.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_old_town_heritage.webp",
        "duration": "3.5 Hours",
        "price": "THB 850",
        "price_note": "(Per Person)",
        "meetup": "Phuket Old Town Clock Tower / Queen Sirikit Park (or hotel transfer)",
        "overview_p1": "Step back into the 19th-century tin-mining boom era of Phuket with a captivating heritage and street food walking tour through Phuket Old Town. Recognized as a UNESCO City of Gastronomy, Phuket Town boasts a rich cultural tapestry where Chinese tin miners, Siamese locals, and Malay Peranakan merchants created a unique architectural and culinary legacy.",
        "overview_p2": "Wander through historic Thalang Road, Dibuk Road, and the colorful pastel lanes of Soi Romanee lined with ornate Sino-Portuguese shophouses and whimsical street murals. Along the way, visit incense-scented Chinese Taoist shrines, traditional herbal apothecaries, and savor authentic local delicacies like Hokkien noodles, crispy roti pancakes, and traditional Peranakan coconut pastries.",
        "places_col1_title": "Sino-Portuguese Architectural Gems",
        "places_col1_badge": "Living History",
        "places_col1_items": [
            ("Thalang Road & Soi Romanee", "Admire the ornate archways, shuttered wooden windows, and pastel Sino-colonial facades of restored 19th-century merchant houses."),
            ("San Chao Seng Tham (Shrine of the Serene Light)", "A hidden 130-year-old Chinese Taoist shrine tucked down a narrow alleyway adorned with intricate dragon sculptures and frescoes."),
            ("Phuket Heritage Street Murals", "Discover whimsical urban wall murals depicting traditional tin miners, local food vendors, and historic street life.")
        ],
        "places_col2_title": "UNESCO Gastronomy Tastings",
        "places_col2_badge": "Local Flavors",
        "places_col2_items": [
            ("Hokkien Fried Noodles (Mee Hokkien)", "Savor rich stir-fried yellow egg noodles with pork, squid, and greens bathed in a savory seafood broth with a poached egg."),
            ("Phuket Spring Rolls & Dim Sum", "Taste freshly rolled Popiah (fresh spring rolls with sweet bean sauce) and traditional Phuket-style morning dim sum."),
            ("O-Aew Shaved Ice Dessert", "Cool down with Phuket's signature refreshing dessert made from jellied O-aew fig seeds, red beans, shaved ice, and sweet syrup.")
        ],
        "inclusions": [
            "Guided walking tour with licensed English-speaking local heritage expert",
            "Four authentic street food tastings and a refreshing local herbal drink",
            "Visit to Chinese historic shrine, heritage shophouse, and herbal dispensary",
            "Illustrated Old Town walking map and heritage guide",
            "Optional hotel transfer (available on booking)"
        ],
        "exclusions": [
            "Hotel pickup and drop-off (unless hotel transfer add-on is selected)",
            "Additional personal food, coffee, and souvenir purchases",
            "Guide gratuities"
        ],
        "timing_text": "Morning Walk: 09:00 AM – 12:30 PM (cooler temperatures & morning markets).<br />Afternoon Walk: 03:00 PM – 06:30 PM (captures golden hour and evening street stalls).",
        "transport_text": "Meet at Phuket Old Town Clock Tower (Surin Circle) or select hotel pickup option.",
        "what_to_bring": "Comfortable walking shoes, breathable light clothing, sun umbrella or hat, camera, and appetite for street food.",
        "contact_tour_param": "Phuket+Old+Town+Walking+Tour",
        "faqs": [
            ("How much walking is involved on the tour?", "The tour covers approximately 2.5 kilometers of flat, paved sidewalks at an easy, leisurely pace with frequent seated stops at historic shophouses, temples, and tasting stalls. It is suitable for all fitness levels."),
            ("Can vegetarian food tastings be arranged?", "Yes! Phuket has a rich vegetarian heritage (home to the famous annual Phuket Vegetarian Festival). We easily arrange vegetarian or halal alternatives for all food tastings upon advance notice."),
            ("Is the Old Town tour better on Sunday for the Walking Street market?", "Sunday afternoon is vibrant because Thalang Road transforms into the bustling 'Lard Yai' Sunday Walking Street Market starting at 04:00 PM. Weekday tours offer a calmer experience with easier access to interior shophouses and uncrowded photo spots."),
            ("Where is the meeting point if we arrange our own transport?", "For guests using their own transport, the meeting point is conveniently located beside the historic Phuket Clock Tower at Surin Circle in central Phuket Town. Metered taxis and Grab rides can drop you directly at the meeting spot.")
        ]
    },
    {
        "filename": "phuket_luxury_spa_and_wellness.html",
        "title": "Phuket Luxury Thai Spa & Wellness Treatment Packages | Trippovention",
        "h1": "Phuket Luxury Thai Spa & Wellness Retreat",
        "subtitle": "Traditional Royal Thai Massage, Herbal Compress, Aromatherapy Oil & Floral Foot Bath",
        "meta_desc": "Rejuvenate body and mind with luxury Thai spa packages in Phuket. Featuring traditional herbal compresses, warm coconut oil massages, body scrubs, and peaceful botanical gardens.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_luxury_spa_wellness.webp",
        "duration": "2–3 Hours",
        "price": "THB 1,500",
        "price_note": "(Per Person)",
        "meetup": "Award-Winning Day Spa Oasis in Patong / Kata / Laguna (transfers available)",
        "overview_p1": "Surrender to blissful tranquility and restore total physical harmony with an award-winning luxury spa experience in Phuket. Set amidst serene tropical botanical gardens, trickling lotus ponds, and teakwood treatment pavilions, our partner wellness sanctuaries represent the pinnacle of traditional Siamese healing and holistic wellness.",
        "overview_p2": "Begin your journey with an invigorating kaffir lime and sea salt floral foot ritual, followed by your choice of therapeutic treatments: ancient Royal Thai acupressure massage, steaming organic herbal compresses (Luk Pra Kob), warm coconut oil body therapy, or exfoliating tropical body scrubs. Conclude with warm herbal tea and seasonal fruit in a peaceful relaxation lounge.",
        "places_col1_title": "Signature Treatment Rituals",
        "places_col1_badge": "Holistic Healing",
        "places_col1_items": [
            ("Traditional Royal Thai Massage (Nuad Thai)", "Centuries-old therapeutic healing art combining acupressure, rhythmic muscle compression, and passive yoga stretching."),
            ("Hot Herbal Ball Compress (Luk Pra Kob)", "Steamed muslin bundles of turmeric, lemongrass, camphor, and plai applied along meridian lines to relieve muscle tension."),
            ("Aromatherapy Essential Oil Therapy", "Gentle Swedish-inspired flowing massage using customized pure essential oils (jasmine, lemongrass, or lavender).")
        ],
        "places_col2_title": "Spa Sanctuary Facilities",
        "places_col2_badge": "Botanical Serenity",
        "places_col2_items": [
            ("Private Teakwood Treatment Villas", "Air-conditioned private suites with terrazzo bathtubs, private rain showers, and tranquil garden views."),
            ("Floral Foot Cleansing Ritual", "Soothing foot bath infused with fresh kaffir lime slices, sea salts, and fragrant orchid petals."),
            ("Post-Treatment Herbal Tea Lounge", "Unwind after your therapy with hot organic bael fruit tea, herbal infusions, and fresh tropical fruit.")
        ],
        "inclusions": [
            "Choice of 120-minute or 150-minute luxury spa treatment package",
            "Welcome refreshing herbal welcome beverage and cool scented towel",
            "Signature floral foot bath ritual with natural scrubs",
            "Certified licensed Thai massage therapists with extensive training",
            "Private treatment room with individual shower and luxury amenities",
            "Post-treatment hot herbal tea and seasonal fruit refreshments"
        ],
        "exclusions": [
            "Round-trip private hotel transfers (available on request for nominal fee)",
            "Specialized take-home organic spa and body care products",
            "Therapist gratuities"
        ],
        "timing_text": "Appointments available daily between 10:00 AM and 09:00 PM.<br />Advance reservation recommended to secure preferred time slots.",
        "transport_text": "Convenient spa sanctuary branches located in Patong, Kata, Kamala, and Laguna Phuket.",
        "what_to_bring": "Comfortable clothes; all treatment robes, disposable spa underwear, towels, and toiletries are provided.",
        "contact_tour_param": "Phuket+Luxury+Spa+Retreat",
        "faqs": [
            ("Can couples enjoy treatments together in the same private suite?", "Yes, all our luxury spa sanctuaries feature spacious double and triple private treatment villas with twin massage tables and sunken floral bathtubs, ideal for couples, honeymooners, or friends traveling together."),
            ("Are spa treatments suitable for pregnant women?", "Yes, specialized Prenatal Motherhood Massages are available for women in their second and third trimesters (after 12 weeks of pregnancy). Therapists use gentle techniques, side-lying support pillows, and pure fragrance-free carrier oils."),
            ("Can I adjust the massage pressure during my treatment?", "Absolutely. Before your treatment begins, you will fill out a consultation questionnaire indicating your preferred pressure (soft, medium, or firm) and any areas of focus or injury. You can always ask your therapist to adjust pressure at any point."),
            ("What should I wear during the spa treatment?", "You do not need to bring any special attire. The spa provides comfortable loose-fitting Thai massage pyjamas for dry Thai massages, and plush bathrobes, slippers, and hygienic disposable underwear for oil and scrub treatments.")
        ]
    },
    {
        "filename": "private_phuket_city_and_viewpoints_tour.html",
        "title": "Private Phuket City & Scenic Viewpoints Custom Tour | Trippovention",
        "h1": "Private Phuket City & Scenic Viewpoints Tour",
        "subtitle": "100% Flexible VIP Itinerary with Private Air-Conditioned Van & Dedicated Local Chauffeur",
        "meta_desc": "Discover Phuket on your own terms with a private vehicle and chauffeur. Visit Promthep Cape, Big Buddha, Wat Chalong, Windmill Viewpoint, and Old Town at your own pace.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_private_phuket_city_viewpoints.webp",
        "duration": "6 Hours / 8 Hours Full Day",
        "price": "THB 2,500",
        "price_note": "(Per Vehicle - Up to 10 Pax)",
        "meetup": "Pick up directly at your Phuket hotel, villa, or resort lobby",
        "overview_p1": "Experience the ultimate freedom and comfort of exploring Phuket on a 100% customizable private sightseeing tour. Ideal for families with children, senior travelers, romantic couples, and small private groups, this tour gives you complete control over your sightseeing schedule without the rush of join-in tour groups.",
        "overview_p2": "Travel in a modern, spacious air-conditioned minivan driven by an experienced, courteous local chauffeur. Choose your own stops from Phuket's finest sights—including the Big Buddha, Wat Chalong, Promthep Cape, Windmill Viewpoint, Karon Viewpoint, Phuket Old Town cafes, or seaside seafood restaurants in Rawai—and explore each destination at your own relaxed pace.",
        "places_col1_title": "Popular Cultural Stops",
        "places_col1_badge": "Tailored Culture",
        "places_col1_items": [
            ("Big Buddha of Phuket", "Marvel at the 45-meter marble monument on Nakkerd Hill with panoramic 360-degree views across the southern island."),
            ("Wat Chalong Royal Temple", "Explore the historic Grand Pagoda, admire golden statues, and experience traditional Thai Buddhist culture."),
            ("Phuket Old Town Sino-Portuguese Lanes", "Stroll boutique cafes, art galleries, and historic shophouses along Thalang Road and Soi Romanee.")
        ],
        "places_col2_title": "Breathtaking Coastal Viewpoints",
        "places_col2_badge": "Scenic Panoramas",
        "places_col2_items": [
            ("Promthep Cape & Windmill Lookout", "Phuket's legendary sunset cape and adjacent windmill plateau overlooking Nai Harn and Ya Nui beaches."),
            ("Karon Viewpoint (Three Beaches Vista)", "Spectacular coastal overlook framing Kata Noi, Kata, and Karon bays."),
            ("Rawai Seafood Market & Pier", "Select live Andaman lobster, prawns, and fish at the gypsy market and have it cooked fresh at seaside eateries.")
        ],
        "inclusions": [
            "Private modern air-conditioned Toyota Commuter VIP minivan for up to 10 passengers",
            "Professional, polite local driver with extensive Phuket island knowledge",
            "Fuel, parking fees, highway tolls, and all vehicle operating costs",
            "Direct hotel or private villa lobby pickup and drop-off anywhere in Phuket",
            "Chilled bottled drinking water and refreshing towels",
            "Comprehensive commercial vehicle passenger insurance"
        ],
        "exclusions": [
            "Licensed English-speaking tour guide (optional add-on available for THB 1,500)",
            "Temple donations and admission tickets to paid attractions (e.g., museums, shows)",
            "Meals, drinks, and personal restaurant expenses",
            "Overtime hourly surcharge (THB 300 per additional hour beyond booked duration)"
        ],
        "timing_text": "Choice of 6-Hour Half-Day or 8-Hour Full-Day hire.<br />Flexible start time between 07:00 AM and 01:00 PM.",
        "transport_text": "Direct pickup from any hotel, resort, villa, or Phuket International Airport (HKT).",
        "what_to_bring": "Camera, comfortable footwear, modest clothing for temples, sunglasses, and spending money for shopping and meals.",
        "contact_tour_param": "Private+Phuket+City+Tour",
        "faqs": [
            ("Can we customize the itinerary on the day of the tour?", "Yes! Your private tour is 100% flexible. You can follow our suggested best-route itinerary or request specific stops, cafe breaks, shopping halts, and photo spots on the morning of your trip. Your driver will advise on optimal travel routing to avoid peak traffic."),
            ("What is the difference between a private driver and a tour guide?", "Your chauffeur is an experienced professional local driver who handles all navigation, parking, and transfers safely. If you also wish to have an English-speaking licensed guide accompany you inside temples and explain history and culture in depth, an optional guide can be added on request."),
            ("Can the tour include airport pickup or drop-off?", "Yes! You can begin your private tour with an airport pickup upon arrival at Phuket International Airport (HKT), tour the island, and end with a drop-off at your hotel—or vice versa on your departure day."),
            ("How many passengers can the private minivan accommodate?", "Our standard private Toyota Commuter VIP minivans comfortably accommodate up to 9–10 passengers with carry-on bags, or up to 6–7 passengers with large luggage.")
        ]
    },
    {
        "filename": "khao_sok_national_park_day_trip.html",
        "title": "Khao Sok National Park & Cheow Lan Lake Day Trip from Phuket | Trippovention",
        "h1": "Khao Sok National Park & Cheow Lan Lake Excursion",
        "subtitle": "Ancient Rainforest, Longtail Boat Cruise through Guilin Limestone Karsts & Floating Raft Lunch",
        "meta_desc": "Experience Khao Sok National Park and Cheow Lan Lake on a day trip from Phuket. Scenic longtail cruise, emerald waters, limestone pinnacles, and swimming at floating bungalows.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_khao_sok_cheow_lan_lake.webp",
        "duration": "Full Day (11–12 Hours)",
        "price": "THB 2,900",
        "price_note": "(Per Person)",
        "meetup": "Pick up from Phuket hotels (early morning 06:30 AM departure)",
        "overview_p1": "Journey inland from Phuket into the primeval wilderness of Khao Sok National Park, home to one of the oldest evergreen rainforests on Earth—dating back over 160 million years. This epic full-day eco-adventure takes you to Cheow Lan Lake, an immense 165-square-kilometer emerald freshwater lake ringed by towering limestone peaks rising sheer from the mist.",
        "overview_p2": "Board a classic traditional wooden longtail boat at Ratchaprapha Dam to cruise through the awe-inspiring karst scenery known as Thailand's 'Little Guilin'. Marvel at the iconic Khao Sam Kler three-limestone pinnacles, enjoy a hearty southern Thai buffet lunch at a floating bamboo raft house, kayak on the calm emerald lake, and swim in pure freshwater surrounded by untouched nature.",
        "places_col1_title": "Cheow Lan Lake Highlights",
        "places_col1_badge": "Limestone Karsts",
        "places_col1_items": [
            ("Ratchaprapha Dam & Lake Cruise", "Scenic longtail boat cruise cutting through mirror-calm emerald waters between 500-meter vertical limestone cliffs."),
            ("Khao Sam Kler (Three Brothers)", "The signature photographic landmark of Cheow Lan Lake featuring three jagged limestone pinnacles rising dramatically from the depths."),
            ("Floating Raft House Relaxation", "Step onto a traditional floating raft house community on the lake for lunch, relaxation, and scenic mountain views.")
        ],
        "places_col2_title": "Eco-Adventures & Swimming",
        "places_col2_badge": "Freshwater Wilderness",
        "places_col2_items": [
            ("Freshwater Lake Swimming & Kayaking", "Dive directly into warm, crystalline freshwater and paddle self-guided kayaks around peaceful jungle bays."),
            ("Khao Sok Viewpoint Halt", "Panoramic morning viewpoint halt overlooking the vast forested mountain ranges of Surat Thani province."),
            ("Rainforest Flora & Wildlife Observation", "Spot hornbills, gibbons, wild langurs, and kingfishers inhabiting the lakeside jungle canopy.")
        ],
        "inclusions": [
            "Round-trip air-conditioned minivan transfers from Phuket hotels",
            "Scenic traditional longtail boat excursion across Cheow Lan Lake",
            "Professional English-speaking licensed eco-tour guide",
            "Traditional southern Thai buffet lunch served at floating raft house",
            "Complimentary use of lake kayaks and life jackets",
            "Drinking water, seasonal fruits, and comprehensive accident insurance"
        ],
        "exclusions": [
            "Khao Sok National Park entrance fee (THB 300 adult, THB 150 child - payable at pier)",
            "Optional bamboo cave trekking or jungle hike (subject to seasonal water levels)",
            "Personal spending, snacks, and guide gratuities"
        ],
        "timing_text": "Full day tour: 06:30 AM – 07:15 AM hotel pickup. Returns to Phuket hotel around 07:00 PM.",
        "transport_text": "Round-trip hotel transfers included from major Phuket beach districts and Phuket Town.",
        "what_to_bring": "Swimwear, change of dry clothes, towel, insect repellent, waterproof bag for phone and electronics, and cash for park entry.",
        "contact_tour_param": "Khao+Sok+National+Park+Day+Trip",
        "faqs": [
            ("How far is Khao Sok and Cheow Lan Lake from Phuket?", "Cheow Lan Lake is located approximately 160 kilometers north of Phuket in Surat Thani province. The scenic drive takes about 2.5 to 3 hours each way in a comfortable air-conditioned van, with a rest stop along the route. The extraordinary scenery makes it well worth the day trip."),
            ("Is swimming in Cheow Lan Lake safe?", "Yes, swimming in the lake is exceptionally clean, warm, and safe. The water is deep and calm with zero ocean currents. Life jackets are provided and mandatory for all water activities."),
            ("Can elderly travelers or children enjoy this tour?", "Yes, this excursion requires minimal strenuous physical exertion as most of the day involves boat cruising, scenic sightseeing, floating raft relaxation, and gentle swimming."),
            ("Are overnight stays available at the floating raft houses?", "Trippovention offers both full-day excursions and 2-Day/1-Night overnight packages at luxury floating raft houses on Cheow Lan Lake. Contact our travel team for overnight itineraries and customized private transfers.")
        ]
    },
    {
        "filename": "andamanda_phuket_water_park_tickets.html",
        "title": "Andamanda Phuket Water Park Admission Tickets | Trippovention",
        "h1": "Andamanda Phuket Water Park Day Pass",
        "subtitle": "25 Themed Water Slides, 3-Meter Artificial Wave Pool & Thai Mythological Adventure",
        "meta_desc": "Book Andamanda Phuket water park tickets. Enjoy 5 themed zones based on Thai mythology, thrilling drop slides, lazy river, and Southeast Asia's biggest wave pool.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_andamanda_phuket_water_park.webp",
        "duration": "Full Day (5–6 Hours)",
        "price": "THB 1,450",
        "price_note": "(Per Person)",
        "meetup": "Andamanda Phuket (Kathu District, Central Phuket) or Hotel Transfer",
        "overview_p1": "Immerse your family in a world of mythical wonder and high-octane aquatic thrills at Andamanda Phuket, the island's premier water and entertainment destination. Spanning over 22 acres in Kathu, this massive 4.5-billion-baht water kingdom is themed around classical Thai mythology, hidden treasures, and the legends of the Andaman Sea.",
        "overview_p2": "Featuring five distinct themed zones—The Pearl Palace, Coral World, The Great Andaman Bay, Naga Jungle, and Emerald Forest—Andamanda boasts 25 exhilarating water attractions. Conquer Southeast Asia's longest lazy river, brave heart-racing vertical drop slides, surf a 3-meter artificial ocean wave pool, and relax beside a stunning replica of Koh Tapu (James Bond Island).",
        "places_col1_title": "Signature Thrill Slides",
        "places_col1_badge": "High-Adrenaline",
        "places_col1_items": [
            ("Naga Jungle & Dragon Drop", "Experience heart-pounding vertical drop slides and high-speed enclosed spiral water tubes reaching thrilling speeds."),
            ("Eagle Flyer & Racing Slides", "Multi-lane mat racing slides and raft drop chutes where friends can race head-to-head into massive splash basins."),
            ("Curved Water Coasters", "Propelled uphill water coasters twisting through lush artificial limestone rock formations.")
        ],
        "places_col2_title": "Family Zones & Wave Pool",
        "places_col2_badge": "Family Leisure",
        "places_col2_items": [
            ("The Great Andaman Bay & Wave Pool", "Southeast Asia's largest wave pool generating artificial surf waves up to 3 meters high with a sandy beach and replica James Bond Island."),
            ("Rolling Ripples Lazy River", "Southeast Asia's longest lazy river (550 meters) gently winding through jungle landscapes and mystical caves."),
            ("Coral World (Kids' Splash Kingdom)", "Vibrant interactive splash area for young children featuring miniature slides, water cannons, and a giant tipping bucket.")
        ],
        "inclusions": [
            "Full-day unlimited admission ticket to Andamanda Phuket Water Park",
            "Unlimited access to all 25 water slides, wave pools, and themed attractions",
            "Complimentary use of park life vests and inflatable swim tubes",
            "Access to sandy beach relaxation zones and sun loungers",
            "Emergency medical first-aid coverage and trained lifeguards"
        ],
        "exclusions": [
            "Hotel pickup and drop-off (available as an optional transfer add-on)",
            "Locker and towel rentals (available via RFID cashless wristband on-site)",
            "Food, beverages, and tropical cocktails from park restaurants and swim-up bars",
            "Private VIP luxury cabana rental"
        ],
        "timing_text": "Open daily from 10:00 AM to 07:00 PM.<br />Wave pool sessions run continuously throughout the day.",
        "transport_text": "Located at 333/3 Moo 1, Kathu, Phuket (15 mins from Patong, 10 mins from Phuket Town).",
        "what_to_bring": "Appropriate swimwear (no metal buckles or zippers on slides), towel, waterproof sunscreen, and sunglasses.",
        "contact_tour_param": "Andamanda+Phuket+Water+Park",
        "faqs": [
            ("Are towels and lockers available at Andamanda Phuket?", "Yes, digital RFID lockers and fresh towels are available for rent at the main locker pavilion. The park operates a completely cashless RFID wristband system, allowing you to load credit for food, locker rental, and souvenirs without carrying cash."),
            ("Is outside food and drinks permitted inside the park?", "Outside food and beverages are not allowed inside Andamanda, with exceptions for baby food and medically required dietary items. The park offers multiple international restaurants, Thai street food stalls, and swim-up bars."),
            ("What are the height restrictions for major thrill slides?", "Most major high-thrill slides require a minimum height of 122 cm (48 inches) for safety reasons. Children under 122 cm have full access to Coral World, the kid-friendly splash fortress, lazy river, and the shallow margins of the wave pool."),
            ("Is Andamanda Water Park close to Patong Beach?", "Yes, Andamanda is located in Kathu, just an easy 15-minute drive over the hill from Patong Beach and 10 minutes from Phuket Town, making it very accessible by taxi or hotel transfer.")
        ]
    },
    {
        "filename": "siam_niramit_phuket_show.html",
        "title": "Siam Niramit Phuket Cultural Show Tickets & Dinner | Trippovention",
        "h1": "Siam Niramit Phuket Cultural Spectacular",
        "subtitle": "100+ Performers, Flying Angels, Live River on Stage & Traditional Thai Village Experience",
        "meta_desc": "Experience Siam Niramit Phuket cultural show with optional international buffet. Marvel at 700 years of Thai history, river stunts on stage, and authentic heritage village.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_siam_niramit_phuket.webp",
        "duration": "Evening (3–4 Hours)",
        "price": "THB 1,700",
        "price_note": "(Per Person)",
        "meetup": "Siam Niramit Phuket Compound (Bypass Road, Rassada, Phuket)",
        "overview_p1": "Immerse yourself in Thailand's rich history, spiritual traditions, and vibrant cultural celebrations at Siam Niramit Phuket. Billed as one of the world's largest stage productions, this monumental theatrical extravaganza brings 700 years of Siamese heritage to life across a gigantic 65-meter-wide stage in a 1,750-seat state-of-the-art auditorium.",
        "overview_p2": "Before the main curtain rises, explore the charming Traditional Thai Village—a living museum where artisans demonstrate silk weaving, rice pounding, and traditional cooking in authentic wooden houses representing Thailand's four distinct regions. Enjoy a lavish international buffet dinner and outdoor fountain performances before being captivated by airborne angels, thunderous battle scenes, and a real river flowing across the stage.",
        "places_col1_title": "Three Theatrical Acts",
        "places_col1_badge": "Epic Production",
        "places_col1_items": [
            ("Act 1: Journey Back into History", "Spectacular reenactments of ancient Siam: the ancient northern kingdom of Lanna, South Sea maritime traders, and Ayutthaya royal court."),
            ("Act 2: Journey Beyond Imagination", "Visually stunning depiction of the three Buddhist realms: fiery Hell, mystical Himmapan Forest with mythical creatures, and Blissful Heaven."),
            ("Act 3: Journey Through Joyous Festivals", "Joyous celebration of Thailand's greatest festive traditions: floating lanterns during Loy Krathong and water splashing during Songkran.")
        ],
        "places_col2_title": "Cultural Village & Outdoor Pre-Show",
        "places_col2_badge": "Living Heritage",
        "places_col2_items": [
            ("Traditional Thai Village of the Four Regions", "Wander through authentic stilt houses depicting Northern, Central, Southern, and Isan rural lifestyles with artisan workshops."),
            ("Outdoor Courtyard Entertainment", "Enjoy live Thai boxing (Muay Thai) demonstrations, classical live gamelan music, and traditional folk dances in the outdoor plaza."),
            ("Grand International Buffet Dinner", "Feast on a vast selection of freshly prepared Thai favorites, international roast carving stations, vegetarian dishes, and desserts.")
        ],
        "inclusions": [
            "Official reserved admission ticket to Siam Niramit Phuket Stage Spectacular",
            "Choice of Silver, Gold, or Platinum theatre seating",
            "Access to the outdoor Traditional Thai Cultural Village and live courtyard shows",
            "Sumptuous international and Thai buffet dinner (when dinner option is selected)",
            "Optional round-trip hotel transfer from major Phuket beaches"
        ],
        "exclusions": [
            "Round-trip hotel transfers (unless transfer package is selected)",
            "Alcoholic beverages and specialty drinks from the bar",
            "Souvenir photos and traditional costume photo rentals",
            "Performer tips in the outdoor courtyard"
        ],
        "timing_text": "Park gates open at 05:30 PM. Buffet dinner served from 05:30 PM to 08:00 PM.<br />Main Stage Show starts at 08:30 PM (duration: 80 minutes).",
        "transport_text": "Located at 55/81 Moo 5, Chalermprakiat Ror 9 Road (Bypass Road), Rassada, Phuket.",
        "what_to_bring": "Smart casual clothing, camera for outdoor village (auditorium photography is not permitted), and light jacket.",
        "contact_tour_param": "Siam+Niramit+Phuket+Show",
        "faqs": [
            ("What time should we arrive at Siam Niramit?", "We recommend arriving between 05:30 PM and 06:00 PM. This provides ample time to explore the Traditional Thai Village, feed fish from wooden boats, watch the outdoor cultural pre-shows, and enjoy your international buffet dinner before the main theatre doors open at 08:00 PM."),
            ("Is photography permitted during the main show?", "Photography and video recording inside the main theatre auditorium are strictly prohibited. The staff will securely store cameras and tablets at the free cloakroom check-in before entering the auditorium. You are free to take unlimited photos in the outdoor village and plaza."),
            ("Is Siam Niramit suitable for all ages?", "Yes, Siam Niramit is a universally acclaimed family production suitable for children, parents, and seniors. The visual spectacle, flying aerialists, special effects, and animal puppets keep all age groups enthralled."),
            ("What food options are available at the buffet?", "The extensive buffet features dedicated stations for Thai classics (Pad Thai, green curry, Tom Yum), western pastas, carved meats, Indian vegetarian curries, fresh salads, fresh fruits, and traditional Thai desserts.")
        ]
    },
    {
        "filename": "phuket_surfing_and_stand_up_paddleboarding.html",
        "title": "Phuket Surfing & Stand-Up Paddleboard Lessons & Hire | Trippovention",
        "h1": "Phuket Surfing & Stand-Up Paddleboard Experience",
        "subtitle": "ISA-Certified Surf Lessons on Kata Beach & Scenic Flat-Water Stand-Up Paddleboarding",
        "meta_desc": "Learn to surf or stand-up paddleboard on Kata and Bang Tao beaches in Phuket. Includes ISA-certified coaching, rashguard, premium board rental, and safety instruction.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_surfing_sup.webp",
        "duration": "2 Hours Lesson / Half-Day Board Hire",
        "price": "THB 1,200",
        "price_note": "(Per Person)",
        "meetup": "Kata Beach or Bang Tao Surf Club, Phuket",
        "overview_p1": "Catch your first wave or glide peacefully across tranquil tropical lagoons with Phuket's top-rated surfing and Stand-Up Paddleboard (SUP) experiences. With warm tropical water year-round and gentle, forgiving beach breaks, Phuket is recognized as Thailand's surf capital.",
        "overview_p2": "During the southwest monsoon swell season (May to October), Kata Beach transforms into a surfing haven perfect for beginners and intermediate riders under the guidance of ISA-certified instructors. During the calm dry season (November to April), take advantage of mirror-flat coastal bays and serene mangrove waterways for scenic stand-up paddleboarding excursions.",
        "places_col1_title": "Surf Lessons & Technique",
        "places_col1_badge": "Catch the Waves",
        "places_col1_items": [
            ("Beachfront Theory & Pop-Up Drills", "Learn ocean safety, wave reading, board positioning, paddling power, and correct pop-up footwork on the sand."),
            ("In-Water Guided Wave Catching", "Your coach stays by your side in the water, pushing you into ideal waves and providing real-time stance adjustments."),
            ("Soft-Top Safe Beginner Boards", "Ride high-volume foam soft-top surfboards that maximize stability, floatation, and safety for beginners.")
        ],
        "places_col2_title": "Stand-Up Paddleboard (SUP)",
        "places_col2_badge": "Coastal Gliding",
        "places_col2_items": [
            ("Scenic Bay & Island Paddling", "Paddle along the picturesque coastline of Kata, Yanui, or Bang Tao, admiring coastal cliffs and marine life beneath your board."),
            ("Core Balance & Fitness", "Enjoy an invigorating low-impact full-body workout improving balance, core strength, and mindfulness on the ocean."),
            ("Sunset Paddle Sessions", "Experience magical golden hour paddling as the tropical sun dips below the Andaman horizon.")
        ],
        "inclusions": [
            "2-hour comprehensive beginner surfing or SUP lesson with ISA-certified coach",
            "High-quality foam soft-top surfboard or premium epoxy SUP board with paddle",
            "UV protective quick-dry rashguard and safety ankle leash",
            "Shower facilities, fresh towels, and secure luggage storage",
            "Drinking water and tropical fruit refreshment",
            "Comprehensive sports accident insurance"
        ],
        "exclusions": [
            "Hotel transfers (can be arranged upon request)",
            "Professional beachfront photography or action camera hire",
            "Post-session board rental extension"
        ],
        "timing_text": "Surf Lessons (May–Oct): Morning 09:00 AM, 11:00 AM; Afternoon 02:00 PM, 04:00 PM.<br />SUP Sessions (Nov–Apr): Morning 08:30 AM; Sunset 04:30 PM.",
        "transport_text": "Beach club base located at Kata Beach South or Bang Tao Beach, Phuket.",
        "what_to_bring": "Swimwear / boardshorts, sunscreen (waterproof reef-safe), dry clothes for after, and water bottle.",
        "contact_tour_param": "Phuket+Surfing+and+SUP+Experience",
        "faqs": [
            ("Do I need to be a strong swimmer to take a surf lesson?", "Basic swimming ability is required. All beginner surf lessons take place in waist-to-chest-deep water inside the sandbar break, ensuring you can always stand up safely. Your instructor is right beside you in the water at all times."),
            ("What is the best time of year to surf in Phuket?", "Phuket's primary surfing season runs during the southwest monsoon from May to October, when consistent Indian Ocean groundswells produce gentle 2-to-5-foot waves at Kata, Nai Harn, and Kalim beaches. From November to April, conditions are calm and ideal for Stand-Up Paddleboarding (SUP)."),
            ("Can children take surf lessons?", "Yes! Children aged 6 and above can take surf lessons. For young children, we provide dedicated 1-on-1 private coaching to ensure maximum safety, fun, and personalized attention."),
            ("What should I wear for surfing or paddleboarding?", "Wear comfortable swimwear or boardshorts. We provide protective UV-rated rashguards to shield your skin from the sun and prevent chest abrasion from the surfboard deck.")
        ]
    },
    {
        "filename": "phuket_private_yacht_charter.html",
        "title": "Phuket Private Luxury Yacht & Catamaran Charter | Trippovention",
        "h1": "Phuket Private Luxury Yacht Charter",
        "subtitle": "Exclusive VIP Island Hopping to Maiton, Coral, or Racha Islands with Private Crew & Captain",
        "meta_desc": "Charter a private luxury motor yacht or sailing catamaran in Phuket. Tailored island-hopping itineraries, snorkeling equipment, stand-up paddleboards, and VIP hospitality.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_private_yacht_charter.webp",
        "duration": "Full Day (8 Hours) or Half Day Sunset",
        "price": "THB 19,500",
        "price_note": "(Per Charter - Up to 15 Guests)",
        "meetup": "Phuket Boat Lagoon / Ao Po Grand Marina / Chalong Pier",
        "overview_p1": "Elevate your Thailand vacation to the height of luxury with an exclusive private yacht or catamaran charter across the turquoise waters of the Andaman Sea. Tailored exclusively for discerning families, corporate VIPs, and celebratory gatherings, a private yacht charter offers complete privacy, flexibility, and five-star hospitality.",
        "overview_p2": "Cruise at your own pace to secluded tropical archipelagos—including Maiton Island's resident dolphin grounds, Racha Yai's crystal bays, or the dramatic limestone pillars of Phang Nga Bay. With a dedicated licensed captain, attentive private crew, gourmet catering options, and water sports toys, your day on the water is completely bespoke.",
        "places_col1_title": "Custom Island Routes",
        "places_col1_badge": "VIP Itineraries",
        "places_col1_items": [
            ("Maiton Island Dolphin Quest & Snorkel", "Cruise to private Maiton Island, renowned for its wild pod of playful Indo-Pacific bottlenose dolphins and pristine shallow coral reefs."),
            ("Racha Yai & Coral Island Combo", "Anchor in turquoise lagoons with 25-meter underwater clarity, secluded white sandy beaches, and vibrant marine life."),
            ("Phang Nga Bay & Hong Island Caves", "Sail between towering 300-meter karst pinnacles with private sea kayaking into hidden limestone hongs.")
        ],
        "places_col2_title": "Onboard Luxury Amenities",
        "places_col2_badge": "Five-Star Comfort",
        "places_col2_items": [
            ("Air-Conditioned Saloon & Sun Deck", "Expansive interior living lounge, state-of-the-art Bluetooth sound system, outdoor flybridge, and cushioned sun loungers."),
            ("Water Sports & Toys", "Complimentary use of stand-up paddleboards, inflatable sea pools, high-end snorkeling gear, and fishing lines."),
            ("Gourmet Catering & Refreshments", "Optional freshly prepared seafood BBQ, gourmet fruit platters, soft drinks, and ice; bring your own wine with zero corkage fees.")
        ],
        "inclusions": [
            "Exclusive private charter of yacht/catamaran for your party (up to licensed capacity)",
            "Licensed professional yacht captain and dedicated private service crew",
            "Fuel for selected charter itinerary and harbor marina fees",
            "Complimentary drinking water, ice, soft drinks, and fresh seasonal tropical fruit",
            "Snorkeling equipment, life jackets, and stand-up paddleboard usage",
            "Comprehensive marine vessel passenger insurance"
        ],
        "exclusions": [
            "Round-trip VIP minivan transfers to marina (can be arranged on request)",
            "National park entrance fees (if visiting national park islands)",
            "Onboard gourmet catering lunch (custom menu packages available on request)",
            "Alcoholic beverages (guests may bring their own wine and spirits with zero corkage fees)",
            "Crew and captain gratuities"
        ],
        "timing_text": "Full Day Charter: 09:00 AM – 05:00 PM (8 Hours).<br />Half Day Sunset Charter: 02:00 PM – 06:30 PM (4.5 Hours).",
        "transport_text": "Departs from Royal Phuket Marina, Phuket Boat Lagoon, Ao Po Grand Marina, or Chalong Pier.",
        "what_to_bring": "Swimwear, resort wear, sunglasses, hat, reef-safe sunscreen, beach towels, and music playlist on your phone.",
        "contact_tour_param": "Private+Phuket+Yacht+Charter",
        "faqs": [
            ("Can we bring our own alcoholic drinks and wine on board?", "Yes, absolutely! Guests are welcome to bring their own wine, champagne, beer, and spirits on board. We provide ice, glassware, and refrigeration with zero corkage fees."),
            ("Can we customize the charter itinerary and stops?", "Yes, your charter is completely private and customizable. Prior to departure, our marine specialist and captain will discuss your preferred highlights—whether that means wild dolphin spotting, quiet beach relaxation, deep-water snorkeling, or a sunset dinner cruise."),
            ("What catering options are available on the yacht?", "We offer a variety of onboard catering options ranging from casual Thai buffet lunches and freshly grilled Andaman seafood BBQs to gourmet picnic platters and canapés. Alternatively, we can reserve a beachfront restaurant table at an island resort along your route."),
            ("What happens if there is bad weather on our charter date?", "The safety and comfort of our guests is paramount. If the marine authorities issue severe weather warnings or wave conditions are unsafe, our charter team will work with you to reschedule to an alternative date or provide a full refund.")
        ]
    },
    {
        "filename": "phuket_viewpoints_and_big_buddha_tour.html",
        "title": "Phuket Viewpoints, Wat Chalong & Big Buddha Guided Tour | Trippovention",
        "h1": "Phuket Viewpoints, Wat Chalong & Big Buddha Tour",
        "subtitle": "45-Meter Marbled Buddha atop Nakkerd Hill, Grand Pagoda of Wat Chalong & Coastal Lookout Panoramas",
        "meta_desc": "Guided tour of Phuket's top panoramic viewpoints and sacred landmarks. Marvel at Big Buddha on Nakkerd Hill, visit Wat Chalong, Windmill Viewpoint, and Promthep Cape.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_big_buddha_wat_chalong.webp",
        "duration": "Half Day (4–5 Hours)",
        "price": "THB 950",
        "price_note": "(Per Person)",
        "meetup": "Direct hotel pickup across Patong, Karon, Kata, Rawai, and Phuket Town",
        "overview_p1": "Immerse yourself in Phuket's most awe-inspiring scenic vistas and sacred spiritual landmarks on this guided half-day viewpoints and temple excursion. Designed for travelers seeking breathtaking panoramic photography and deep cultural discovery, this tour connects the island's most iconic coastal outlooks and monumental religious shrines.",
        "overview_p2": "Ascend the lush summit of Nakkerd Hill to stand beneath the majestic 45-meter Big Buddha statue, marveling at sweeping 360-degree views across Chalong Bay, Kata, and Rawai. Pay homage at Wat Chalong, the island's spiritual heart, before continuing to the wind-swept coastal plateaus of Windmill Viewpoint and Promthep Cape.",
        "places_col1_title": "Sacred Island Monuments",
        "places_col1_badge": "Spiritual Landmarks",
        "places_col1_items": [
            ("The Great Buddha of Phuket", "The towering 45-meter white Burmese marble statue atop Nakkerd Hill with panoramic 360-degree vistas across southern Phuket."),
            ("Wat Chalong (Wat Chaithararam)", "Phuket's largest Buddhist temple complex, featuring the Grand Pagoda enshrining a holy bone relic of Lord Buddha."),
            ("Buddhist Blessing & Merit Making", "Experience traditional temple rituals, light lotus incense, and receive a ceremonial blessing from temple monks.")
        ],
        "places_col2_title": "Iconic Coastal Lookouts",
        "places_col2_badge": "Dramatic Vistas",
        "places_col2_items": [
            ("Promthep Cape (Laem Promthep)", "Thailand's most famous coastal headland jutting into the Andaman Sea with sweeping views of Koh Racha and Koh Hey."),
            ("Windmill Viewpoint", "Hilltop lookout perched above Ya Nui Beach featuring rotating wind turbines and emerald-blue water views."),
            ("Karon Viewpoint (Kho Sam Haad)", "Legendary vantage point framing Kata Noi, Kata, and Karon crescent beaches in a single vista.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transfers from Patong, Kata, Karon, Rawai, and Phuket Town",
            "Professional English-speaking licensed local tour guide",
            "All entrance fees and temple admissions",
            "Chilled bottled drinking water and refreshing towels",
            "Comprehensive travel accident insurance coverage"
        ],
        "exclusions": [
            "Transfers from remote areas (Bang Tao, Laguna, Mai Khao - small surcharge applies)",
            "Personal donations and souvenir purchases",
            "Guide and driver gratuities"
        ],
        "timing_text": "Morning Tour: 08:30 AM – 01:00 PM.<br />Afternoon Tour: 01:30 PM – 06:30 PM (captures sunset at Promthep Cape).",
        "transport_text": "Pick-up and drop-off included for Patong, Kata, Karon, Rawai, Nai Harn, and Phuket Town.",
        "what_to_bring": "Modest clothing covering shoulders and knees for temple visits, comfortable shoes, sunglasses, and camera.",
        "contact_tour_param": "Phuket+Viewpoints+and+Big+Buddha+Tour",
        "faqs": [
            ("What should I wear when visiting the Big Buddha and Wat Chalong?", "Both the Big Buddha and Wat Chalong are active Buddhist religious sanctuaries. Visitors must dress respectfully: shoulders, chest, and knees must be covered. Sleeveless shirts, crop tops, short shorts, and sheer clothing are strictly prohibited. Free sarongs or wraps are provided at the entrance if required."),
            ("Is Big Buddha wheelchair accessible?", "The main lower plateau and viewpoint terrace surrounding the Big Buddha are wheelchair accessible via paved pathways and ramps. The upper terrace immediately beneath the statue requires climbing stairs."),
            ("Is the morning or afternoon tour better for photos?", "The morning tour offers clearer morning skies, less road traffic, and gentle lighting at Wat Chalong. The afternoon tour is immensely popular for capturing the golden sunset glow at Promthep Cape and Windmill Viewpoint."),
            ("Are monkeys present around the Big Buddha and viewpoints?", "Wild macaques occasionally inhabit the forested trees along Nakkerd Hill and Promthep Cape. We advise guests to admire them from a distance and avoid feeding them or carrying exposed food.")
        ]
    }
]

def generate_tour_page(t):
    url = f"https://trippovention.co.th/packages/thailand/phuket/{t['filename']}"
    
    col1_items_html = "\n".join([f'                  <li><strong>{title}:</strong> {desc}</li>' for title, desc in t["places_col1_items"]])
    col2_items_html = "\n".join([f'                  <li><strong>{title}:</strong> {desc}</li>' for title, desc in t["places_col2_items"]])
    
    inc_html = "\n".join([f'                  <li>{item}</li>' for item in t["inclusions"]])
    exc_html = "\n".join([f'                  <li>{item}</li>' for item in t["exclusions"]])
    
    faqs_str = ""
    faq_schema_items = []
    for q, a in t["faqs"]:
        faqs_str += f'''            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>{q}</span>
                <span class="faq-icon" aria-hidden="true">+</span>
              </button>
              <div class="faq-answer">
                <p>{a}</p>
              </div>
            </div>\n'''
        
        # Escape quotes for schema
        q_clean = q.replace('"', '\\"')
        a_clean = a.replace('"', '\\"')
        faq_schema_items.append(f'''          {{
            "@type": "Question",
            "name": "{q_clean}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{a_clean}"
            }}
          }}''')
    faq_schema_str = ",\n".join(faq_schema_items)

    html = f'''<!doctype html>
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
    <title>{t["title"]}</title>
    <meta name="description" content="{t["meta_desc"]}" />
    <meta name="author" content="Trippovention" />

    <meta property="og:type" content="website" />
    <meta property="og:url" content="{url}" />
    <meta property="og:title" content="{t["title"]}" />
    <meta property="og:description" content="{t["meta_desc"]}" />
    <meta property="og:image" content="{t["og_image"]}" />

    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="{url}" />
    <meta property="twitter:title" content="{t["title"]}" />
    <meta property="twitter:description" content="{t["meta_desc"]}" />
    <meta property="twitter:image" content="{t["og_image"]}" />

    <link rel="canonical" href="{url}" />
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
      function gtag() {{
        dataLayer.push(arguments);
      }}
      gtag("js", new Date());
      gtag("config", "AW-11395302765");
    </script>

    <!-- Structured Data -->
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "TouristTrip",
        "name": "{t['h1']}",
        "description": "{t['meta_desc']}",
        "touristType": ["Sightseeing Travelers", "Culture Seekers", "Families", "Adventure Enthusiasts"],
        "offers": {{
          "@type": "Offer",
          "price": "{t['price'].replace('THB ', '').replace(',', '')}",
          "priceCurrency": "THB",
          "availability": "https://schema.org/InStock",
          "url": "{url}"
        }},
        "provider": {{
          "@type": "TravelAgency",
          "name": "Trippovention",
          "url": "https://trippovention.co.th"
        }}
      }}
    </script>
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://trippovention.co.th/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "Destinations",
            "item": "https://trippovention.co.th/destinations.html"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "Thailand",
            "item": "https://trippovention.co.th/packages/thailand/"
          }},
          {{
            "@type": "ListItem",
            "position": 4,
            "name": "Phuket",
            "item": "https://trippovention.co.th/packages/thailand/phuket/"
          }},
          {{
            "@type": "ListItem",
            "position": 5,
            "name": "Sightseeing",
            "item": "https://trippovention.co.th/packages/thailand/phuket/sightseeing.html"
          }},
          {{
            "@type": "ListItem",
            "position": 6,
            "name": "{t['h1']}",
            "item": "{url}"
          }}
        ]
      }}
    </script>
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
{faq_schema_str}
        ]
      }}
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
                width="20" height="20" class="whatsapp-icon-nav whatsapp-green"
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
              <a href="index.html">Phuket</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item">
              <a href="sightseeing.html">Sightseeing</a>
            </li>
            <li class="breadcrumb-separator">›</li>
            <li class="breadcrumb-item active" aria-current="page">
              {t["h1"]}
            </li>
          </ol>
        </div>
      </nav>

      <header class="hero compact hero-thailand">
        <div class="container">
          <h1>{t["h1"]}</h1>
          <p>{t["subtitle"]}</p>
        </div>
      </header>

      <section class="section">
        <div class="container">
          <div class="grid cols-3">
            <div class="card info-card">
              <div class="body">
                <div class="info-icon">⏱️</div>
                <h2>Duration</h2>
                <p>{t["duration"]}</p>
              </div>
            </div>
            <div class="card info-card card-premium">
              <div class="body">
                <div class="info-icon">💰</div>
                <h3>Tour Price</h3>
                <div class="price-row">
                  <span class="price">{t["price"]} <small style="font-size: 13px; font-weight: normal; color: var(--text-muted);">{t["price_note"]}</small></span>
                </div>
              </div>
            </div>
            <div class="card info-card">
              <div class="body">
                <div class="info-icon">📍</div>
                <h2>Meet-up Location</h2>
                <p>{t["meetup"]}</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section alt">
        <div class="container">
          <div class="section-title">
            <h2>Tour Overview &amp; Description</h2>
            <p class="subtitle">{t["subtitle"]}</p>
          </div>
          <div class="card" style="padding: 28px;">
            <p style="font-size: 16px; line-height: 1.8; margin-bottom: 20px;">
              {t["overview_p1"]}
            </p>
            <p style="font-size: 16px; line-height: 1.8; margin-bottom: 0;">
              {t["overview_p2"]}
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
                <div class="badge">{t["places_col1_badge"]}</div>
                <h3>{t["places_col1_title"]}</h3>
                <ul class="muted" style="line-height: 1.9; margin-top: 12px;">
{col1_items_html}
                </ul>
              </div>
            </div>

            <div class="card">
              <div class="body">
                <div class="badge">{t["places_col2_badge"]}</div>
                <h3>{t["places_col2_title"]}</h3>
                <ul class="muted" style="line-height: 1.9; margin-top: 12px;">
{col2_items_html}
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
                  {t["timing_text"]}
                </p>
              </div>
            </div>
            <div class="card">
              <div class="body text-center">
                <div class="feature-icon">🚐</div>
                <h3>Transport &amp; Transfers</h3>
                <p class="muted">
                  {t["transport_text"]}
                </p>
              </div>
            </div>
            <div class="card">
              <div class="body text-center">
                <div class="feature-icon">🎒</div>
                <h3>What to Bring</h3>
                <p class="muted">
                  {t["what_to_bring"]}
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
            <p class="subtitle">Quick answers to common questions about this Phuket activity</p>
          </div>
          <div class="faq-container">
{faqs_str}
          </div>
        </div>
      </section>

      <section class="section cta">
        <div class="container">
          <div class="section-title">
            <h2 class="text-white">Enquire About {t["h1"]}</h2>
            <p class="subtitle text-white-90">
              Get the best rates on Phuket sightseeing, activities, and private arrangements with Trippovention
            </p>
          </div>
          <div class="text-center">
            <a
              class="btn btn-lg ghost"
              href="../../../contact.html?destination=phuket&tour={t['contact_tour_param']}"
              >📞 Request Custom Quote</a
            >
            <a
              class="btn btn-lg ghost ml-16"
              href="https://wa.me/66946934392?text=Hello,%20I%20am%20interested%20in%20booking%20the%20{t['contact_tour_param']}%20in%20Phuket"
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
              <a href="sightseeing.html">Phuket Sightseeing Catalogue</a><br />
              <a href="index.html">Phuket Tour Packages</a><br />
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
        <div class="footer-bottom">
          <p>&copy; 2026 Trippovention. All rights reserved.</p>
        </div>
      </div>
    </footer>

    <script src="../../../assets/app.js" defer></script>
    <script src="../../../assets/search.js" defer></script>
  </body>
</html>
'''
    return html

def main():
    os.makedirs(DEST_DIR, exist_ok=True)
    for tour in TOURS_DATA:
        filepath = os.path.join(DEST_DIR, tour["filename"])
        html_content = generate_tour_page(tour)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated: {tour['filename']}")
    print(f"\nSuccessfully generated all {len(TOURS_DATA)} Phuket sightseeing product pages!")

if __name__ == "__main__":
    main()
