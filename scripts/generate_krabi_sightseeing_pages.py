#!/usr/bin/env python3
"""
Generate individual detail pages for all Krabi sightseeing tours.
Follows Trippovention design system, typography, SEO metadata, breadcrumbs, and schema.
"""

import os

DEST_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "packages", "thailand", "krabi")

TOURS_DATA = [
    {
        "filename": "hong_islands_tour_by_longtail_boat.html",
        "title": "Hong Islands Tour by Longtail Boat | Trippovention Krabi",
        "h1": "Hong Islands Tour by Longtail Boat",
        "subtitle": "Authentic Wooden Longtail Cruise, Hidden Emerald Hong Lagoon, Lading Island & Coral Snorkeling",
        "meta_desc": "Experience an authentic Krabi island-hopping adventure aboard a traditional wooden longtail boat. Explore Hong Lagoon, Koh Lading, Pakbia Island & coral reefs with lunch.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/sightseeingoptions/hero_hong_islands_tour.webp",
        "duration": "7–8 Hours",
        "price": "THB 1,040",
        "price_note": "(Per Person)",
        "meetup": "Hotel Lobby (Krabi City & Ao Nang Hotels)",
        "overview_p1": "Experience the timeless serenity of the Andaman Sea aboard a traditional Southern Thai longtail boat. Drift at a leisurely pace past towering karst limestone monoliths rising from turquoise waters, soaking in the dramatic scenery of Than Bok Khorani National Park.",
        "overview_p2": "Glide through the narrow sea entrance into the magnificent enclosed emerald waters of Hong Lagoon, framed by sheer vertical cliffs. Relax on the powdery white sands of Koh Lading (Paradise Island), explore Pakbia Island's scenic sandbar at low tide, and snorkel among colorful tropical parrotfish and reef life. A delicious picnic lunch box and seasonal fruits are included.",
        "places_col1_title": "Hong Island & Hidden Lagoon",
        "places_col1_badge": "Signature Highlights",
        "places_col1_items": [
            ("Hong Island (Koh Hong)", "The crown jewel of the national park, boasting pelay white beach, calm crystal waters, and shade under limestone cliffs."),
            ("Hong Lagoon (Thale Nai)", "A breathtaking enclosed seawater lagoon surrounded by sheer vertical limestone walls accessed through a dramatic cliff passage."),
            ("Hong 360° Viewpoint", "Optional panoramic staircase climb delivering 360-degree aerial views over the Andaman Sea and Phang Nga Bay.")
        ],
        "places_col2_title": "Satellite Islands & Snorkeling",
        "places_col2_badge": "Island Highlights",
        "places_col2_items": [
            ("Koh Lading (Paradise Island)", "A tranquil sheltered cove with white sand, historical swallow-nest harvesting shelters, and calm swimming."),
            ("Pakbia Island", "Famous for unique weathered rock formations and scenic sand spit connecting neighboring islets at low tide."),
            ("Coral Reef Snorkeling", "Swim alongside colorful butterflyfish, sergeant majors, and vibrant soft corals in warm tropical waters.")
        ],
        "inclusions": [
            "Round-trip hotel transfers from Krabi Town and Ao Nang",
            "Traditional wooden longtail boat cruise with experienced captain",
            "Picnic lunch box and fresh seasonal tropical fruits",
            "Bottled drinking water throughout the day",
            "Snorkeling equipment (mask and snorkel)",
            "Standard life jacket for all guests",
            "Licensed English-speaking local tour guide",
            "Travel accident insurance"
        ],
        "exclusions": [
            "National Park Fee (THB 300 Adult / THB 150 Child, payable in cash on-site)",
            "Personal expenses and beach mat rentals",
            "Alcoholic beverages",
            "Tips & gratuities for captain and guide"
        ],
        "timing_text": "Daily departures<br /><strong>Hotel Pick-up:</strong> 07:45 AM – 08:30 AM<br />Return approx. 03:30 PM – 04:00 PM",
        "transport_text": "Shared air-conditioned minivan transfer to the pier, followed by authentic wooden longtail boat cruise.",
        "what_to_bring": "Swimwear, beach towel, reef-safe sunscreen, sunglasses, sun hat, waterproof bag, and Thai Baht cash for park entry.",
        "contact_tour_param": "Hong+Islands+Tour+by+Longtail+Boat"
    },
    {
        "filename": "krabi_4_islands_tour_by_longtail_boat.html",
        "title": "Krabi 4 Islands Tour by Longtail Boat | Trippovention Krabi",
        "h1": "Krabi 4 Islands Tour by Longtail Boat",
        "subtitle": "Classic Longtail Island Hopping, Koh Poda, Chicken Island, Talay Waek Sandbar & Phra Nang Cave",
        "meta_desc": "Explore Krabi's 4 iconic islands by traditional wooden longtail boat. Visit Koh Poda, Chicken Island, Tup Island sandbar & Phra Nang Cave Beach with lunch box.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/sightseeingoptions/hero_krabi_4_islands_tour.webp",
        "duration": "6–7 Hours",
        "price": "THB 700",
        "price_note": "(Per Person)",
        "meetup": "Hotel Lobby (Krabi City & Ao Nang Hotels)",
        "overview_p1": "Enjoy the authentic charm of Southern Thailand's seafaring heritage on this classic longtail boat tour visiting Krabi's famous 4-island archipelago. Perfect for travelers seeking a relaxed pace without the noise or rush of high-speed vessels.",
        "overview_p2": "Stroll across the iconic natural sandbar (Talay Waek) connecting Tup and Mor Islands at low tide, snap memorable photos beside Chicken Island's distinct rock formation, relax on Koh Poda's expansive powdery white sands, and explore the sacred spirit shrines and stalactites of Phra Nang Cave Beach on Railay Peninsula.",
        "places_col1_title": "Tup & Chicken Islands",
        "places_col1_badge": "Natural Wonder",
        "places_col1_items": [
            ("Talay Waek (Divided Sea)", "The world-famous phenomenon where crystal waters part at low tide to reveal a glistening white sandbar linking Tup and Mor islands."),
            ("Chicken Island (Koh Gai)", "An extraordinary limestone karst crag shaped like a giant rooster headland, surrounded by clear snorkeling waters."),
            ("Snorkeling Reefs", "Vibrant underwater gardens bustling with anemonefish, coral heads, and schooling damselfish.")
        ],
        "places_col2_title": "Koh Poda & Railay Phra Nang",
        "places_col2_badge": "Iconic Beaches",
        "places_col2_items": [
            ("Koh Poda Island", "A postcard-perfect island with broad white sand beaches and panoramic views across the turquoise sea toward towering karst rock pillars."),
            ("Phra Nang Cave Beach", "Renowned worldwide for sacred fishermen's Princess Cave (Tham Phra Nang), towering limestone cliffs, and tranquil swimming coves."),
            ("Railay Peninsula Views", "Gaze up at dramatic karst formations famous among world-class rock climbers.")
        ],
        "inclusions": [
            "Round-trip hotel transfers in Ao Nang and Krabi Town",
            "Traditional longtail boat cruise with experienced captain",
            "Delicious packed lunch box and seasonal fruit",
            "Bottled drinking water",
            "Snorkeling mask and snorkel",
            "Life jackets for all passengers",
            "English-speaking tour guide",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "National Park Entrance Fee (THB 200 Adult / THB 100 Child, cash on-site)",
            "Personal spending and souvenir shopping",
            "Optional water sports or beach loungers",
            "Tips and gratuities for crew"
        ],
        "timing_text": "Daily departures<br /><strong>Pick-up:</strong> 08:00 AM – 08:30 AM<br />Return approx. 03:00 PM – 03:30 PM",
        "transport_text": "Round-trip minivan transfer to the pier, followed by authentic wooden longtail boat island cruise.",
        "what_to_bring": "Swimwear, beach footwear, towel, reef-safe sunscreen, sunglasses, waterproof pouch, and Thai Baht cash for national park fee.",
        "contact_tour_param": "Krabi+4+Islands+Tour+by+Longtail+Boat"
    },
    {
        "filename": "krabi_7_islands_sunset_tour_by_longtail_boat.html",
        "title": "Krabi 7 Islands Sunset Tour by Longtail Boat | Trippovention Krabi",
        "h1": "Krabi 7 Islands Sunset Tour by Longtail Boat",
        "subtitle": "Afternoon Island Hopping, Andaman Sunset, Beachside BBQ Dinner & Bioluminescent Plankton Swim",
        "meta_desc": "Experience an enchanting sunset longtail tour in Krabi. Visit 7 islands, snorkel vibrant reefs, savor a beach BBQ dinner, and swim with glowing bioluminescent plankton.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/sightseeingoptions/hero_krabi_7_islands_sunset_tour.webp",
        "duration": "Approx. 6 Hours",
        "price": "THB 950",
        "price_note": "(Per Person)",
        "meetup": "Hotel Lobby (Krabi City & Ao Nang Hotels)",
        "overview_p1": "Escape the morning crowds with this leisurely afternoon longtail boat tour. Setting sail after midday, you will cruise past 7 scenic islands in the Krabi archipelago while basking in the golden glow of the afternoon Andaman sun.",
        "overview_p2": "Enjoy world-class snorkeling around Koh Tan Ming and Yawasam Island, wander the serene beaches of Koh Poda and Tup Island, and relax as the sky turns fiery crimson at sunset. The tour finishes with a freshly cooked beachside barbecue dinner and a magical dark-water swim with radiant bioluminescent plankton.",
        "places_col1_title": "Afternoon Island Exploration",
        "places_col1_badge": "Archipelago Highlights",
        "places_col1_items": [
            ("Poda, Chicken & Tup Islands", "Visit the quintessential Krabi islands in peaceful afternoon light with fewer tourists and calm waters."),
            ("Yawasam & Tan Ming Reefs", "Deep coral channels offering exceptional visibility, marine life, and soft coral gardens."),
            ("Phra Nang Beach", "Explore the dramatic cliffs and sacred sea princess cave as shadows lengthen over the sand.")
        ],
        "places_col2_title": "Sunset & Bioluminescence",
        "places_col2_badge": "Night Magic",
        "places_col2_items": [
            ("Andaman Golden Sunset", "Unobstructed horizon sunset views from the water and beach, perfect for unforgettable photography."),
            ("Beachside Barbecue Dinner", "Freshly grilled chicken, fish, rice, vegetable curry, and tropical fruits served right on the beach."),
            ("Glowing Plankton Night Swim", "Jump into calm, dark waters and watch microscopic dinoflagellates sparkle and glow blue around your hands and feet.")
        ],
        "inclusions": [
            "Round-trip hotel transfers from Ao Nang and Krabi Town",
            "Traditional longtail boat cruise with experienced captain",
            "Delicious beachside sunset dinner (BBQ buffet)",
            "Snorkeling equipment (mask and snorkel)",
            "Standard life jackets for all guests",
            "Bottled drinking water and fresh fruit",
            "Professional English-speaking guide",
            "Travel accident insurance"
        ],
        "exclusions": [
            "National Park entrance fee (THB 200 Adult / THB 100 Child, payable in cash)",
            "Personal alcoholic drinks",
            "Tips & gratuities for tour crew"
        ],
        "timing_text": "Daily operation<br /><strong>Pick-up:</strong> 01:30 PM – 02:00 PM<br />Return approx. 08:00 PM – 08:30 PM",
        "transport_text": "Minivan transfer from hotel lobby to the pier, followed by sunset longtail boat navigation.",
        "what_to_bring": "Swimwear, dry change of clothes, towel, light evening jacket or wrap, waterproof camera/phone case, and cash for park fee.",
        "contact_tour_param": "Krabi+7+Islands+Sunset+Tour+by+Longtail+Boat"
    },
    {
        "filename": "phi_phi_islands_day_trip_from_krabi.html",
        "title": "Phi Phi Islands Day Trip from Krabi by Speedboat | Trippovention",
        "h1": "Phi Phi Islands Day Trip from Krabi",
        "subtitle": "High-Speed Speedboat Cruise, Maya Bay, Emerald Pileh Lagoon, Viking Cave & Bamboo Island",
        "meta_desc": "Take an exhilarating speedboat day trip from Krabi to the Phi Phi Islands. Visit legendary Maya Bay, swim in Pileh Lagoon, snorkel Bamboo Island & enjoy buffet lunch.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phiphiisland/hero_phi_phi_island.webp",
        "duration": "8–9 Hours",
        "price": "Contact Us",
        "price_note": "(Special Offer)",
        "meetup": "Hotel Lobby (Krabi City & Ao Nang Hotels)",
        "overview_p1": "Cross the open Andaman Sea on a modern high-speed speedboat to Thailand's most renowned island destination: Phi Phi Leh and Phi Phi Don. Experience sheer limestone crags towering hundreds of meters above azure waters.",
        "overview_p2": "Walk upon the pristine sands of world-famous Maya Bay, step into the calm emerald pool of Pileh Lagoon, gaze at Viking Cave swifts' nest harvesting scaffolds, and encounter curious macaques at Monkey Beach. Indulge in an international buffet lunch on Phi Phi Don followed by coral reef snorkeling off powdery Bamboo Island.",
        "places_col1_title": "Phi Phi Leh Highlights",
        "places_col1_badge": "World Famous",
        "places_col1_items": [
            ("Maya Bay", "The world-famous bay made legendary by 'The Beach', strictly protected and offering powder-soft white sand and turquoise shallows."),
            ("Pileh Lagoon", "A breathtaking emerald-green natural swimming pool enclosed by sheer 100-meter karst cliffs."),
            ("Viking Cave", "Historic limestone cavern with prehistoric paintings and active bird's nest harvesting perches.")
        ],
        "places_col2_title": "Phi Phi Don & Bamboo Island",
        "places_col2_badge": "Beaches & Reefs",
        "places_col2_items": [
            ("Monkey Beach", "Lush coastal cove inhabited by playful wild crab-eating macaque monkeys."),
            ("Phi Phi Don Town", "The main inhabited island where you will enjoy a hearty buffet lunch in a seaside restaurant."),
            ("Bamboo Island (Koh Mai Phai)", "A flat uninhabited coral island ringed by pristine white sand beaches and thriving shallow reefs.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transfers in Krabi & Ao Nang",
            "High-speed modern speedboat cruise with experienced crew",
            "Delicious buffet lunch at restaurant on Phi Phi Don",
            "Fresh tropical seasonal fruits and drinking water",
            "Snorkeling equipment (mask and snorkel)",
            "Safety life jackets for all passengers",
            "Licensed English-speaking tour guide",
            "Marine travel accident insurance"
        ],
        "exclusions": [
            "Phi Phi National Park entrance fee (THB 400 Adult / THB 200 Child, paid on-site)",
            "Longtail boat shuttle inside Pileh Lagoon (optional rental)",
            "Personal purchases, snacks and souvenirs",
            "Tips & gratuities"
        ],
        "timing_text": "Daily operation<br /><strong>Pick-up:</strong> 07:45 AM – 08:30 AM<br />Return approx. 04:30 PM – 05:00 PM",
        "transport_text": "Shared air-conditioned minivan to the marina, followed by powerful twin/triple-engine speedboat crossing.",
        "what_to_bring": "Swimwear, sunscreen, sunglasses, beach towel, waterproof bag, flip-flops, and Thai Baht cash for national park fee.",
        "contact_tour_param": "Phi+Phi+Islands+Day+Trip+from+Krabi"
    },
    {
        "filename": "krabi_luxury_sunset_cruise.html",
        "title": "Krabi Luxury Sunset Cruise | Trippovention Krabi",
        "h1": "Krabi Luxury Sunset Cruise",
        "subtitle": "Modern Sailing Catamaran, Andaman Sunset Vistas, Gourmet Thai Dinner, SUP & Snorkeling",
        "meta_desc": "Sail in style on a luxury catamaran sunset cruise in Krabi. Enjoy cushioned sunbeds, SUP paddleboards, coral snorkeling, Pad Thai & Salt Baked Shrimp dinner.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/sightseeingoptions/hero_krabi_luxury_sunset_cruise.webp",
        "duration": "Approx. 5.5 Hours",
        "price": "Contact Us",
        "price_note": "(Premium Experience)",
        "meetup": "Hotel Lobby (Ao Nang & Krabi Town Hotels)",
        "overview_p1": "Step aboard an elegant, modern sailing catamaran for an exquisite afternoon and evening along Krabi's majestic coastline. Designed for comfort and understated luxury, this cruise offers ample lounge seating, shaded decks, and forward trampoline netting for sunbathing.",
        "overview_p2": "Cruise past towering karst cliffs, swim and snorkel in crystal-clear waters, try stand-up paddleboarding (SUP), and witness the sun sink beneath the Andaman Sea in a brilliant blaze of gold and pink. As twilight falls, enjoy a freshly prepared Thai gourmet dinner including signature Pad Thai and Salt Baked Shrimp served under the evening sky.",
        "places_col1_title": "Onboard Luxury & Watersports",
        "places_col1_badge": "VIP Comfort",
        "places_col1_items": [
            ("Spacious Modern Catamaran", "Dual-hull stability, cushioned open-air lounges, shaded dining saloon, and expansive sun-deck trampolines."),
            ("Stand-Up Paddleboards (SUP)", "Glide smoothly across calm island coves on premium inflatable paddleboards."),
            ("Guided Snorkeling Stops", "Explore rich coral channels around coastal islands with provided high-clarity masks.")
        ],
        "places_col2_title": "Gourmet Dining & Sunset",
        "places_col2_badge": "Culinary Journey",
        "places_col2_items": [
            ("Signature Thai Dinner", "Authentic Thai delicacies prepared fresh, featuring Pad Thai, Salt Baked Shrimp, chicken curry, and salads."),
            ("Golden Hour Panorama", "Unmatched photographic angles of Krabi's karst monoliths silhouetted against the sunset."),
            ("Starlit Cruise Return", "Sail gently back to port with ambient lounge music under a canopy of tropical stars.")
        ],
        "inclusions": [
            "Round-trip hotel transfers in Ao Nang and Krabi Town",
            "Catamaran sunset cruise with professional captain and crew",
            "Gourmet dinner buffet featuring Pad Thai & Salt Baked Shrimp",
            "Complimentary use of SUP paddleboards and snorkel equipment",
            "Life jackets for all guests",
            "Fresh tropical fruit platter and unlimited soft drinks & water",
            "English-speaking host and hospitality crew",
            "Comprehensive marine passenger insurance"
        ],
        "exclusions": [
            "Alcoholic beverages (available for purchase at onboard cash bar)",
            "National park fee if applicable",
            "Personal expenses",
            "Gratuities for the crew"
        ],
        "timing_text": "Daily departures<br /><strong>Pick-up:</strong> 01:15 PM – 02:00 PM<br />Return to harbor: approx. 07:30 PM",
        "transport_text": "Air-conditioned hotel minivan transfer to the marina, followed by luxury sailing catamaran cruise.",
        "what_to_bring": "Resort casual / swimwear, light jacket for evening sea breeze, towel, sunglasses, and camera.",
        "contact_tour_param": "Krabi+Luxury+Sunset+Cruise"
    },
    {
        "filename": "krabi_bioluminescent_swimming_experience.html",
        "title": "Bioluminescent Swimming Experience from Krabi | Trippovention",
        "h1": "Bioluminescent Swimming Experience from Krabi",
        "subtitle": "Evening Guided Marine Tour, Golden Sunset, Island Dinner & Magical Glowing Plankton Night Swim",
        "meta_desc": "Swim with glowing bioluminescent plankton in Krabi. Experience a magical evening marine tour with island snorkeling, sunset views & full dinner.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/sightseeingoptions/hero_krabi_7_islands_sunset_tour.webp",
        "duration": "Approx. 6.5 Hours",
        "price": "Contact Us",
        "price_note": "(Evening Tour)",
        "meetup": "Hotel Lobby (Krabi Town & Ao Nang)",
        "overview_p1": "Experience one of nature's most enchanting nocturnal spectacles: the glowing bioluminescent dinoflagellates of the Andaman Sea. This specialized evening excursion is crafted to provide optimal viewing conditions away from city light pollution.",
        "overview_p2": "The tour commences in the late afternoon with scenic island cruising and reef snorkeling. As the sun sets, savor a freshly prepared dinner while resting in a sheltered bay. When total darkness falls, slip into the warm tropical sea and watch millions of plankton burst into sparkling neon-blue light with every stroke of your hands and feet.",
        "places_col1_title": "Afternoon Sea Exploration",
        "places_col1_badge": "Coastal Magic",
        "places_col1_items": [
            ("Sheltered Archipelago Bays", "Cruise past limestone crags to secluded coves optimal for calm-water swimming."),
            ("Afternoon Coral Snorkeling", "Explore marine ecosystems when underwater visibility is clear and calm."),
            ("Sunset over Andaman Waters", "Watch twilight transform the horizon into pastel shades of lavender, orange, and indigo.")
        ],
        "places_col2_title": "Dinner & Bioluminescence",
        "places_col2_badge": "Night Wonder",
        "places_col2_items": [
            ("Evening Dinner & Hot Drinks", "Enjoy a satisfying meal accompanied by tea, coffee, and drinking water."),
            ("Bioluminescent Marine Plankton", "Swim in dark waters and witness the natural living luminescence ignite around your body."),
            ("Guided Safety Briefing", "Professional guides accompany you in the water with high-visibility safety lights and gear.")
        ],
        "inclusions": [
            "Round-trip hotel transfers from Krabi Town and Ao Nang",
            "Evening guided marine boat excursion",
            "Freshly prepared dinner and seasonal fruits",
            "Snorkeling mask, snorkel, and life jacket",
            "English and Thai-speaking marine guide",
            "First aid kit and safety equipment on board",
            "Travel accident insurance"
        ],
        "exclusions": [
            "National park fee if applicable",
            "Personal expenses and snacks",
            "Tips & gratuities for the crew"
        ],
        "timing_text": "Daily evening tour<br /><strong>Pick-up:</strong> 12:30 PM – 01:00 PM<br />Return approx. 08:00 PM – 08:30 PM",
        "transport_text": "Minivan transfer to the pier, followed by specialized evening marine tour boat.",
        "what_to_bring": "Swimwear, warm dry clothes for the ride back, towel, waterproof pouch, and light jacket.",
        "contact_tour_param": "Bioluminescent+Swimming+Experience+from+Krabi"
    },
    {
        "filename": "private_longtail_boat_tour_railay_and_4_islands.html",
        "title": "Private Longtail Boat Tour to Railay & 4 Islands | Trippovention",
        "h1": "Private Longtail Boat Tour to Railay & 4 Islands",
        "subtitle": "Exclusive Private Charter, Tailored Itinerary, Koh Poda, Chicken Island, Tup Sandbar & Phra Nang",
        "meta_desc": "Charter a private longtail boat in Krabi to Railay and the 4 Islands. Customize departure times, escape the crowds, and enjoy private island-hopping with captain.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/tourpackages/hero_krabi_and_phuket_coastal_romance.webp",
        "duration": "Approx. 6 Hours (Customizable)",
        "price": "Contact Us",
        "price_note": "(Private Charter)",
        "meetup": "Ao Nang Beachfront or Hotel Pier",
        "overview_p1": "The ultimate personalized island experience in Krabi. When you charter a private traditional wooden longtail boat, you set the pace, the departure time, and the itinerary. Escape tourist crowds by visiting the islands early in the morning or during serene afternoon hours.",
        "overview_p2": "Spend as much time as you desire relaxing on Koh Poda's powdery sand, stroll across the Talay Waek sandbar when it is quiet, explore the secluded caves of Railay and Phra Nang, or snorkel in quiet coral bays. Ideal for couples, proposals, honeymoons, family reunions, and small private gatherings.",
        "places_col1_title": "Archipelago Islands",
        "places_col1_badge": "Exclusive Access",
        "places_col1_items": [
            ("Koh Poda Island", "Broad white sands and clear shallows; stay longer without fixed tour group schedules."),
            ("Chicken & Tup Islands", "Time your visit to walk across the Talay Waek sandbar in peaceful solitude."),
            ("Private Snorkeling Coves", "Your captain navigates to secret sheltered spots with vibrant coral reefs.")
        ],
        "places_col2_title": "Railay Peninsula",
        "places_col2_badge": "Iconic Coast",
        "places_col2_items": [
            ("Phra Nang Cave Beach", "Admire soaring karst limestone overhangs, stalactites, and sacred Princess Cave."),
            ("Railay West Beach", "Famous crescent bay lined with limestone cliffs, luxury resorts, and gentle waves."),
            ("Customized Cruise Stops", "Request impromptu swim breaks anywhere along the scenic coastline.")
        ],
        "inclusions": [
            "Private wooden longtail boat exclusively for your private party",
            "Experienced local boat captain and fuel",
            "Snorkeling equipment (masks and snorkels)",
            "Standard life vests for adults and children",
            "Ice box with bottled drinking water and fresh tropical fruit platter",
            "Flexible departure time and customizable itinerary"
        ],
        "exclusions": [
            "National Park Entrance Fee (THB 200 Adult / THB 100 Child, paid on-site)",
            "Hotel minivan transfers (available as optional private add-on)",
            "Meals and snacks (feel free to bring your own picnic)",
            "Gratuities for the boat captain"
        ],
        "timing_text": "Flexible daily departures<br />Recommended slots: <strong>Morning:</strong> 08:00 AM – 02:00 PM | <strong>Sunset:</strong> 01:30 PM – 07:30 PM",
        "transport_text": "Private wooden longtail boat direct from Ao Nang beachfront or local pier.",
        "what_to_bring": "Swimwear, beach towels, sunglasses, sun hat, reef-safe sunscreen, snacks/picnic, and Thai Baht cash for park entry.",
        "contact_tour_param": "Private+Longtail+Boat+Tour+to+Railay+and+4+Islands"
    },
    {
        "filename": "ao_thalane_kayaking_tour.html",
        "title": "Kayaking at Ao Thalane (Half Day Canoe) | Trippovention Krabi",
        "h1": "Kayaking at Ao Thalane (Half Day Canoe)",
        "subtitle": "Guided Mangrove Eco Expedition, Soaring Karst Limestone Canyons & Pristine Coastal Lagoons",
        "meta_desc": "Paddle through the breathtaking mangrove forests and limestone canyons of Ao Thalane on a guided half-day kayaking tour in Krabi. Hotel transfers included.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/sightseeingoptions/hero_ao_thalane_kayaking.webp",
        "duration": "Approx. 4–5 Hours",
        "price": "THB 693",
        "price_note": "(Per Person)",
        "meetup": "Hotel Lobby (Krabi City & Ao Nang Hotels)",
        "overview_p1": "Ao Thalane is universally recognized as one of Southeast Asia's most spectacular coastal mangrove ecosystems. Sheltered by colossal karst limestone mountains, its winding mangrove waterways offer a tranquil haven far removed from bustling beach resorts.",
        "overview_p2": "Under the guidance of an experienced eco-guide, you will navigate easy-to-paddle sit-on-top kayaks through narrow canyon corridors, hidden lagoons, and ancient mangrove tree tunnels. Along the route, keep your eyes peeled for wild crab-eating macaques, giant monitor lizards, colorful kingfishers, and sea otters.",
        "places_col1_title": "Canyons & Mangroves",
        "places_col1_badge": "Eco Highlights",
        "places_col1_items": [
            ("Karst Limestone Canyons", "Paddle through soaring 100-meter vertical limestone cliff corridors carved by centuries of tidal flow."),
            ("Dense Mangrove Tunnels", "Navigate intricate root systems that serve as vital nurseries for marine life and birds."),
            ("Crocodile Cave & Hidden Lagoons", "Explore secret tidal chambers that open up dramatically into enclosed natural amphitheatres.")
        ],
        "places_col2_title": "Wildlife & Scenery",
        "places_col2_badge": "Nature Encounters",
        "places_col2_items": [
            ("Native Wildlife Spotting", "Encounter playful crab-eating macaques, vibrant kingfishers, egrets, and harmless monitor lizards."),
            ("Serene Mirror-Like Waters", "Protected waterways ensure zero ocean swell, making paddling smooth, safe, and effortless."),
            ("Eco Guide Narration", "Learn about the vital biodiversity of coastal wetland ecosystems from local experts.")
        ],
        "inclusions": [
            "Round-trip hotel transfers in Ao Nang and Krabi Town",
            "High-quality sit-on-top kayaks (single or double) and paddles",
            "Standard life jacket and waterproof dry bag",
            "Bottled drinking water and seasonal fruit refreshments",
            "Licensed English-speaking eco kayaking guide",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Lunch (available on full-day tour options)",
            "Personal souvenirs and snacks",
            "Tips & gratuities for guide and driver"
        ],
        "timing_text": "Morning & afternoon sessions daily<br /><strong>Morning:</strong> 08:30 AM – 12:30 PM<br /><strong>Afternoon:</strong> 01:30 PM – 05:30 PM",
        "transport_text": "Shared air-conditioned minivan transfer to Ao Thalane kayak pier.",
        "what_to_bring": "Quick-dry shorts/t-shirt, swimwear underneath, sun hat, sunglasses with strap, reef-safe sunscreen, and waterproof camera.",
        "contact_tour_param": "Kayaking+at+Ao+Thalane+Krabi"
    },
    {
        "filename": "klong_root_clear_water_canal_kayaking.html",
        "title": "Klong Root (Clear Water Canal) Kayaking | Trippovention Krabi",
        "h1": "Klong Root (Clear Water Canal) Kayaking",
        "subtitle": "Crystal Spring Canal Paddle, Submerged Freshwater Forests & Natural Swimming Lagoon",
        "meta_desc": "Paddle through the crystal-clear spring waters of Klong Root (Khlong Nam Sai) in Krabi. Discover underwater forests and swim in natural mineral lagoons.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/tourpackages/hero_krabi_tropical_escape.webp",
        "duration": "Approx. 3 Hours",
        "price": "Contact Us",
        "price_note": "(Eco Adventure)",
        "meetup": "Hotel Lobby (Ao Nang & Krabi Town)",
        "overview_p1": "Khlong Root (also known as Khlong Nam Sai or Clear Water Canal) is one of Krabi's most magical hidden natural gems. Fed by natural freshwater springs bubbling up through underground limestone strata, the canal boasts crystal clarity like glass.",
        "overview_p2": "Glide across serene freshwater that reveals submerged tree roots, lush aquatic flora, and schools of freshwater fish swimming beneath your kayak. The gentle paddle leads to a pristine natural swimming basin where you can plunge into cool, revitalizing mineral water surrounded by tropical greenery.",
        "places_col1_title": "Canal Paddle Highlights",
        "places_col1_badge": "Pure Nature",
        "places_col1_items": [
            ("Glass-Like Crystal Clarity", "Water so transparent you can clearly see ancient submerged driftwood and vibrant green riverbed moss."),
            ("Shaded Jungle Canopy", "Gentle paddling beneath lush tropical trees shielding you from intense tropical heat."),
            ("Zero Wave Action", "Calm freshwater conditions make this extraordinarily safe and pleasant for families with children.")
        ],
        "places_col2_title": "Natural Spring Lagoon",
        "places_col2_badge": "Refreshment",
        "places_col2_items": [
            ("Natural Mineral Swimming Pool", "Dive into refreshing 24°C natural freshwater pools with smooth sandy and pebbled bottoms."),
            ("Submerged Root Formations", "Fascinating natural driftwood sculptures created over centuries by spring water flow."),
            ("Peaceful Rural Surroundings", "Experience authentic Krabi countryside away from tour bus circuits.")
        ],
        "inclusions": [
            "Round-trip hotel transfers in Ao Nang and Krabi Town",
            "Sit-on-top kayak, lightweight paddles, and life jacket",
            "Local guide assistance and canal admission fee",
            "Bottled drinking water",
            "Use of basic changing and rinse facilities"
        ],
        "exclusions": [
            "Meals and snacks",
            "Personal expenses and lockers",
            "Tips & gratuities"
        ],
        "timing_text": "Daily departures<br /><strong>Morning Slot:</strong> 09:00 AM – 12:00 PM<br /><strong>Afternoon Slot:</strong> 02:00 PM – 05:00 PM",
        "transport_text": "Round-trip air-conditioned minivan transfer (approx. 20 minutes from Ao Nang).",
        "what_to_bring": "Swimwear, change of clothes, towel, waterproof pouch for phone, and sunglasses.",
        "contact_tour_param": "Klong+Root+Clear+Water+Canal+Kayaking"
    },
    {
        "filename": "khao_phanom_bencha_and_huay_toh_waterfall.html",
        "title": "Khao Phanom Bencha & Huay Toh Waterfall Tour | Trippovention",
        "h1": "Khao Phanom Bencha & Huay Toh Waterfall",
        "subtitle": "National Park Virgin Rainforest, 11 Cascading Waterfall Tiers, Natural Rock Pools & Giant Banyan Trees",
        "meta_desc": "Explore Khao Phanom Bencha National Park and the 11 tiers of Huay Toh Waterfall in Krabi. Hike shaded rainforest trails and swim in natural mountain pools.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/sightseeingoptions/hero_krabi_hot_springs_and_emerald_pool.webp",
        "duration": "Approx. 5–6 Hours",
        "price": "Contact Us",
        "price_note": "(Rainforest Tour)",
        "meetup": "Hotel Lobby (Ao Nang & Krabi Town)",
        "overview_p1": "Venture inland to the dramatic northern foothills of Khao Phanom Bencha, Krabi's highest mountain peak crowned with pristine, old-growth tropical rainforest. This protected national park is a sanctuary of biodiversity, roaring mountain streams, and cool mountain breezes.",
        "overview_p2": "Follow scenic shaded boardwalks and nature trails to Huay Toh Waterfall, which cascades down 11 distinctive limestone ledges. Each tier features deep, refreshing mountain pools perfect for cooling off after a hike. Marvel at centuries-old buttressed banyan trees and listen to the calls of hornbills, gibbons, and forest songbirds.",
        "places_col1_title": "Huay Toh Waterfall",
        "places_col1_badge": "11 Cascades",
        "places_col1_items": [
            ("Cascading Waterfall Tiers", "A dramatic series of 11 falls tumbling from mountain granite down into turquoise plunge pools."),
            ("Swimmable Rock Basins", "Pure mountain spring water basins providing an invigorating swim in clean, cool water."),
            ("Shaded Rainforest Viewing Decks", "Well-maintained wooden viewing platforms offering picturesque angles of the main cascade.")
        ],
        "places_col2_title": "National Park Flora & Fauna",
        "places_col2_badge": "Wildlife Haven",
        "places_col2_items": [
            ("Giant Dipterocarp Trees", "Towering rainforest giants with massive buttress root systems standing over 40 meters tall."),
            ("Birdwatching Opportunities", "Spot rare helmeted hornbills, banded pittas, and vibrant butterflies in their natural habitat."),
            ("Pristine Jungle Air", "Experience crisp mountain oxygen and soothing natural forest acoustics far from coastal noise.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transfers in Krabi and Ao Nang",
            "Khao Phanom Bencha National Park admission fee",
            "Professional English-speaking nature guide",
            "Bottled drinking water and fresh fruit snacks",
            "Travel accident insurance"
        ],
        "exclusions": [
            "Lunch (optional stop at local countryside restaurant)",
            "Personal gear and insect repellent",
            "Tips & gratuities"
        ],
        "timing_text": "Daily morning tour<br /><strong>Pick-up:</strong> 08:30 AM – 09:00 AM<br />Return approx. 02:00 PM – 02:30 PM",
        "transport_text": "Round-trip air-conditioned minivan transfer into Khao Phanom Bencha National Park.",
        "what_to_bring": "Comfortable walking shoes/sneakers, swimwear, towel, insect repellent, sun hat, and camera.",
        "contact_tour_param": "Khao+Phanom+Bencha+and+Huay+Toh+Waterfall"
    },
    {
        "filename": "railay_beach_rock_climbing_courses.html",
        "title": "Rock Climbing Courses at Railay Beach | Trippovention Krabi",
        "h1": "Rock Climbing Courses at Railay Beach",
        "subtitle": "World-Class Sport Climbing, Certified Instructors, Top-Rope Routes & Aerial Andaman Sea Vistas",
        "meta_desc": "Experience world-famous rock climbing on the karst cliffs of Railay Beach in Krabi. Half-day and full-day courses with certified instructors and gear included.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/sightseeingoptions/hero_railay_rock_climbing.webp",
        "duration": "Half Day (4h) or Full Day (8h)",
        "price": "Contact Us",
        "price_note": "(Professional Courses)",
        "meetup": "Railay Beach Climbing School / Ao Nang Boat Pier",
        "overview_p1": "Railay and Phra Nang Beach are universally recognized by the international mountaineering community as one of the world's premier sport climbing paradises. Towering vertical limestone karsts rise dramatically from white sand beaches and emerald Andaman waters.",
        "overview_p2": "Whether you are taking your first steps on vertical rock or are an experienced climber seeking local beta on challenging multipitch routes, our courses are led by licensed, safety-certified climbing instructors. You will learn rope management, knot craft, top-rope belaying, and balance footwork while scaling cliffs with breathtaking aerial ocean views.",
        "places_col1_title": "World-Renowned Crags",
        "places_col1_badge": "Legendary Routes",
        "places_col1_items": [
            ("1-2-3 Wall & Phra Nang Crag", "Famous beginner-to-intermediate natural limestone faces right on the beach, featuring grippy pockets and stalactites."),
            ("Wee's Present Wall", "Scenic coastal wall offering diverse climbing grades with panoramic views over Railay East and West."),
            ("Top-Rope Safety Setup", "All climbing is securely belayed on pre-rigged redundant anchor systems with certified climbing ropes.")
        ],
        "places_col2_title": "Skills & Curriculum",
        "places_col2_badge": "Certified Coaching",
        "places_col2_items": [
            ("Fundamental Footwork & Balance", "Master the art of climbing efficiently by using leg strength and body positioning."),
            ("Knot Tying & Belaying", "Hands-on instruction in figure-eight knots, harness double-backs, and tube/assisted belay devices."),
            ("Graded Routes for All Levels", "Over 1,000 bolted routes in the area, ensuring customized progression from grade 4b to 7c+.")
        ],
        "inclusions": [
            "Complete premium climbing gear (harness, climbing shoes, chalk bag, helmet, ropes)",
            "Licensed English-speaking certified climbing instructor (low coach-to-student ratio)",
            "Safety briefing and comprehensive belay instruction",
            "Bottled drinking water throughout the course",
            "Full-day course includes packed lunch on the beach",
            "Climbing insurance coverage"
        ],
        "exclusions": [
            "Round-trip longtail boat transit to Railay (if not booked with private transfer package)",
            "Personal climbing chalk/shoes (you may bring your own if preferred)",
            "Gratuities for climbing instructors"
        ],
        "timing_text": "Morning & Full-day sessions<br /><strong>Half Day:</strong> 09:00 AM – 01:00 PM or 01:30 PM – 05:30 PM<br /><strong>Full Day:</strong> 09:00 AM – 05:00 PM",
        "transport_text": "Meet at Railay climbing shop or coordinated boat transfer from Ao Nang beachfront.",
        "what_to_bring": "Comfortable flexible sportswear, socks for rental climbing shoes, sun protection, water bottle, and energetic mindset.",
        "contact_tour_param": "Rock+Climbing+Courses+at+Railay+Beach"
    },
    {
        "filename": "krabi_atv_nature_view_point_adventure.html",
        "title": "Krabi ATV Nature View Point Adventure | Trippovention Krabi",
        "h1": "Krabi ATV Nature View Point Adventure",
        "subtitle": "Off-Road Quad Biking, Rugged Jungle Trails, Plantation Paths & Scenic Limestone Viewpoints",
        "meta_desc": "Experience an exciting ATV quad biking adventure in Krabi. Ride through jungle trails, rubber plantations, and off-road tracks to scenic hillside viewpoints.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/kohsamui/sightseeingoptions/hero_atv_adventure_experience.webp",
        "duration": "Approx. 1–2 Hours",
        "price": "Contact Us",
        "price_note": "(Adventure Quad)",
        "meetup": "Hotel Lobby (Krabi City & Ao Nang Hotels)",
        "overview_p1": "Experience an adrenaline-pumping off-road expedition in Krabi with an ATV quad ride through dramatic natural terrain. Drive through tropical jungles, dirt paths, muddy tracks, and palm plantations inaccessible to standard vehicles.",
        "overview_p2": "Following an experienced trail marshal, you will ascend scenic elevated dirt paths leading to secluded viewpoints overlooking Krabi's majestic limestone karsts and countryside valleys. A thrilling outdoor activity suitable for adventure enthusiasts, couples, and active families.",
        "places_col1_title": "Off-Road Trails",
        "places_col1_badge": "Adrenaline Rush",
        "places_col1_items": [
            ("Jungle Dirt Tracks & Creeks", "Navigate varied terrain featuring muddy ruts, gravel inclines, and natural forest paths."),
            ("Palm Oil & Rubber Plantations", "Cruise past rows of tall tropical trees on private off-road agricultural acreage."),
            ("Hillside Viewpoint Climb", "Reach panoramic ridges offering wide vistas over Krabi's limestone towers and valleys.")
        ],
        "places_col2_title": "Safety & Machinery",
        "places_col2_badge": "Modern Quads",
        "places_col2_items": [
            ("Automatic 4-Stroke ATVs", "Modern automatic quad bikes that are easy to handle and require no previous gear-shifting experience."),
            ("Practice Circuit Run", "Safety briefing and test loop to ensure you feel 100% confident with throttle and brakes before hitting the trails."),
            ("Professional Trail Guide", "Lead and sweep guides ensure rider safety, pacing, and assistance throughout the route.")
        ],
        "inclusions": [
            "Round-trip hotel transfers in Ao Nang and Krabi Town",
            "ATV ride experience (single rider or rider with passenger)",
            "Protective full-face helmet and safety briefing",
            "English-speaking guide and trail marshals",
            "Welcome cold drink and seasonal fresh fruits",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Personal mud-proof clothing or bandanas (bandanas available for purchase)",
            "Personal expenses and lockers",
            "Tips & gratuities"
        ],
        "timing_text": "Multiple daily departures<br /><strong>Slot 1:</strong> 09:30 AM | <strong>Slot 2:</strong> 10:30 AM<br /><strong>Slot 3:</strong> 01:30 PM | <strong>Slot 4:</strong> 04:00 PM",
        "transport_text": "Round-trip air-conditioned minivan transfer directly to the ATV base camp.",
        "what_to_bring": "Clothes that you don't mind getting dusty or muddy, closed-toe sports shoes, sunglasses, and camera.",
        "contact_tour_param": "Krabi+ATV+Nature+View+Point+Adventure"
    },
    {
        "filename": "dragon_crest_mountain_hiking_tour.html",
        "title": "Dragon Crest Mountain (Khao Ngon Nak) Hiking Tour | Trippovention",
        "h1": "Dragon Crest Mountain (Khao Ngon Nak) Hiking Tour",
        "subtitle": "Challenging 3.7 km Rainforest Trek, 565m Summit Overlook, Legendary Hanging Rock & 360° Panorama",
        "meta_desc": "Hike the famous Dragon Crest Mountain (Khao Ngon Nak) in Krabi. Conquer the 565m summit for breathtaking 360-degree views of the Andaman Sea and Phang Nga Bay.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/sightseeingoptions/hero_dragon_crest_hiking.webp",
        "duration": "Approx. 4–5 Hours",
        "price": "Contact Us",
        "price_note": "(Guided Trek)",
        "meetup": "Hotel Lobby (Ao Nang, Klong Muang, Krabi Town)",
        "overview_p1": "Khao Ngon Nak (Dragon Crest Mountain) is heralded by international travelers and outdoor photographers as having the single most spectacular panoramic viewpoint in all of Southern Thailand. Located within Than Bok Khorani National Park, the trailhead begins in peaceful Tubkaek Beach.",
        "overview_p2": "Ascend a 3.7-kilometer jungle trail through pristine virgin rainforest, passing small cascades and ancient fig trees. Upon reaching the 565-meter summit plateau, you will be rewarded with a mind-blowing 360-degree panorama: the emerald Andaman Sea, Phang Nga Bay islands, and dramatic karst mountains stretching all the way to the horizon.",
        "places_col1_title": "The Summit Viewpoints",
        "places_col1_badge": "360° Wonder",
        "places_col1_items": [
            ("565-Meter Summit Ridge", "Stand above the clouds with uninterrupted views sweeping from Hong Islands across to Phi Phi and Ao Nang."),
            ("The Hanging Rock Ledge", "The legendary rock outcrop suspended over the vertical cliff abyss—the ultimate Krabi photo backdrop."),
            ("Sunrise / Morning Golden Hour", "Early departures catch cool mountain mist drifting across emerald canopy valleys.")
        ],
        "places_col2_title": "Rainforest Trail",
        "places_col2_badge": "3.7 km Trek",
        "places_col2_items": [
            ("Native Dipterocarp Canopy", "Shaded jungle trail with wooden steps, natural roots, and resting stations every 500 meters."),
            ("Waterfalls & Springs", "Pass small freshwater stream waypoints along the mid-mountain sections."),
            ("Guided Pace & Flora Beta", "Knowledgeable local trekking guide ensuring safe pacing, wildlife spotting, and hydration.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transfers from Ao Nang, Klong Muang & Krabi Town",
            "Than Bok Khorani National Park admission fee",
            "Licensed English-speaking local mountain trekking guide",
            "Bottled drinking water and isotonic energy snacks",
            "First aid kit and comprehensive trekker insurance"
        ],
        "exclusions": [
            "Hiking boots and trekking poles",
            "Personal meals and insect spray",
            "Tips & gratuities for the guide"
        ],
        "timing_text": "Early morning departure recommended<br /><strong>Pick-up:</strong> 06:30 AM – 07:00 AM (to beat tropical midday heat)<br />Return approx. 12:00 PM – 12:30 PM",
        "transport_text": "Round-trip air-conditioned minivan transfer to Tubkaek national park ranger station.",
        "what_to_bring": "Sturdy trainers or hiking shoes, breathable sportswear, backpack, small towel, sun protection, and camera.",
        "contact_tour_param": "Dragon+Crest+Mountain+Hiking+Tour"
    },
    {
        "filename": "stand_up_paddleboarding_ao_nang.html",
        "title": "Stand-Up Paddleboarding (SUP) in Ao Nang | Trippovention",
        "h1": "Stand-Up Paddleboarding (SUP) in Ao Nang",
        "subtitle": "Sunset Coastal Paddling, Calming Andaman Waters, Limestone Sea Cliffs & Action Photos",
        "meta_desc": "Experience stand-up paddleboarding (SUP) along the scenic coastline of Ao Nang in Krabi. Guided golden hour sessions with instruction and gear included.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/tourpackages/hero_thailand_coastal_adventure.webp",
        "duration": "Approx. 2 Hours",
        "price": "Contact Us",
        "price_note": "(Sunset Session)",
        "meetup": "Ao Nang Beachfront Station",
        "overview_p1": "Discover the tranquil pleasure of stand-up paddleboarding (SUP) along the stunning coastal waters of Ao Nang and Pai Plong Bay. Gliding standing up on calm water gives you an elevated, crystal-clear perspective of marine life and the seabed below.",
        "overview_p2": "Under the friendly guidance of a certified SUP coach, beginners will quickly master mounting, balancing, and stroke techniques. The tour departs in the late afternoon to catch the magical golden hour, paddling beneath soaring limestone cliffs as the sun dips below the Andaman horizon.",
        "places_col1_title": "Paddleboarding Highlights",
        "places_col1_badge": "Water Sport",
        "places_col1_items": [
            ("Pai Plong & Ao Nang Bays", "Paddle along dramatic limestone headlands framing secluded natural sandy coves."),
            ("Golden Hour Sunset Horizon", "Experience sunset directly from the water with reflections painting the sea in gold and bronze."),
            ("Gentle Full-Body Workout", "Build core balance and fitness effortlessly in a calm, meditative outdoor setting.")
        ],
        "places_col2_title": "Coaching & Equipment",
        "places_col2_badge": "Top Quality",
        "places_col2_items": [
            ("High-Stability Inflatable SUPs", "Wide, buoyant, premium inflatable boards suited for first-timers and intermediate paddlers alike."),
            ("Certified SUP Instructor", "Quick 15-minute shore clinic followed by gentle on-water coaching."),
            ("Waterproof Phone Case & Photos", "Instructor captures beautiful candid action photos of your sunset session.")
        ],
        "inclusions": [
            "Premium inflatable SUP board, paddle, and safety ankle leash",
            "Buoyancy life jacket",
            "Professional SUP instructor guidance and beginner clinic",
            "Waterproof phone pouch and digital action photos",
            "Chilled bottled drinking water"
        ],
        "exclusions": [
            "Hotel transfers (convenient walk-in at Ao Nang beach, or private transfer add-on)",
            "Personal beach towel",
            "Tips & gratuities"
        ],
        "timing_text": "Late afternoon daily<br /><strong>Sunset Session:</strong> 04:30 PM – 06:30 PM (subject to tide and sea conditions)",
        "transport_text": "Direct beachfront meet-up at central Ao Nang beach station.",
        "what_to_bring": "Swimwear, rash guard, sunglasses with floating strap, dry towel, and waterproof bag.",
        "contact_tour_param": "Stand+Up+Paddleboarding+Ao+Nang"
    },
    {
        "filename": "railay_beach_exploration_and_phra_nang_cave.html",
        "title": "Railay Beach Exploration & Phra Nang Cave | Trippovention Krabi",
        "h1": "Railay Beach Exploration & Phra Nang Cave",
        "subtitle": "Iconic Coastal Day Trip, Railay West, Phra Nang Princess Shrine, Limestone Karsts & Longtail Transit",
        "meta_desc": "Explore world-famous Railay Beach and Phra Nang Cave in Krabi. Relax on white sand beaches surrounded by towering cliffs with round-trip longtail boat transit.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/phiphiisland/hero_phi_phi_and_railay_coastal_escape.webp",
        "duration": "Approx. 4 Hours",
        "price": "Contact Us",
        "price_note": "(Coastal Day Trip)",
        "meetup": "Hotel Lobby (Ao Nang & Krabi Town)",
        "overview_p1": "Railay is a world unto itself: a secluded tropical peninsula cut off from the Krabi mainland by impassable, soaring limestone mountains, accessible solely by sea. It feels more like a magical offshore island than a mainland coast.",
        "overview_p2": "Hop on a scenic longtail boat shuttle from Ao Nang across emerald waves. Stroll along Railay West's sweeping crescent of white sand, wander through shaded limestone pathways linking to Railay East, and discover the mysterious stalactite-draped Princess Cave (Tham Phra Nang), revered by local sea gypsies and fishermen for good fortune.",
        "places_col1_title": "Railay Peninsula Highlights",
        "places_col1_badge": "World Famous",
        "places_col1_items": [
            ("Railay West Beach", "Expansive powdery beach bordered by vertical karst cliffs, emerald waters, and beachside cafes."),
            ("Phra Nang Cave Beach", "Voted among the world's most beautiful beaches, famous for sacred fisherman shrines and clear swimming."),
            ("Stalactite Caverns", "Gaze up at dramatic limestone dripstone formations, caves, and overhangs right on the beach.")
        ],
        "places_col2_title": "Atmosphere & Activities",
        "places_col2_badge": "Relax & Explore",
        "places_col2_items": [
            ("Rock Climbing Spectacle", "Watch international sport climbers scale sheer cliffs directly over the beach."),
            ("Jungle Trail Walking", "Paved footpaths connect beaches under the shade of limestone bluffs and wild banyan trees."),
            ("Relaxed Island Vibe", "Completely car-free environment with relaxed bohemian cafes and tropical juice bars.")
        ],
        "inclusions": [
            "Round-trip longtail boat shuttle between Ao Nang and Railay Beach",
            "Round-trip hotel minivan transfers from Ao Nang or Krabi Town",
            "Guided peninsula orientation walk",
            "Bottled drinking water",
            "Life jackets on all boat transfers",
            "Travel accident insurance"
        ],
        "exclusions": [
            "Personal food, drinks, and beachside lunches",
            "Optional rock climbing or kayak rentals on Railay",
            "Tips & gratuities"
        ],
        "timing_text": "Morning & afternoon departures daily<br /><strong>Morning:</strong> 09:00 AM – 01:00 PM<br /><strong>Afternoon:</strong> 01:30 PM – 05:30 PM",
        "transport_text": "Minivan to Ao Nang beachfront followed by scenic 15-minute longtail boat crossing.",
        "what_to_bring": "Beachwear, beach towel, sunglasses, sun hat, camera, and cash for beachfront cafes.",
        "contact_tour_param": "Railay+Beach+Exploration+and+Phra+Nang+Cave"
    },
    {
        "filename": "krabi_city_tour_half_day_private.html",
        "title": "Krabi City Tour (Half Day – Private) | Trippovention Krabi",
        "h1": "Krabi City Tour (Half Day – Private)",
        "subtitle": "Wat Tham Suea (Tiger Cave Temple), Giant Mud Crab Sculpture, Krabi River Promenade & Maharaj Market",
        "meta_desc": "Explore cultural Krabi on a private half-day city tour. Visit Tiger Cave Temple (Wat Tham Suea), the riverside Crab sculpture, and Maharaj market in a private vehicle.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/tourpackages/hero_krabi_and_phuket_nature_retreat.webp",
        "duration": "Approx. 4–5 Hours",
        "price": "THB 2,100",
        "price_note": "(Per Person / Private)",
        "meetup": "Hotel Lobby (Pickup from Krabi Hotel)",
        "overview_p1": "Discover the cultural, historical, and local lifestyle highlights of Krabi on an exclusive private city tour. Traveling in a private air-conditioned vehicle, you enjoy the flexibility to explore at your own pace without waiting for large tour groups.",
        "overview_p2": "Visit the renowned Wat Tham Suea (Tiger Cave Temple), situated in a lush tropical forest valley. Energetic visitors can challenge the 1,237 steps to the mountain summit Buddha statue with sweeping 360-degree views. Stroll along the Krabi River promenade to photograph the iconic Black Mud Crab and Sea Eagle bronze sculptures, and browse the vibrant tropical produce of Maharaj Morning Market.",
        "places_col1_title": "Cultural Highlights",
        "places_col1_badge": "Sacred Sites",
        "places_col1_items": [
            ("Wat Tham Suea (Tiger Cave Temple)", "Historic forest temple complex with sacred tiger footprint caves and ancient banyan trees."),
            ("Summit Buddha Overlook", "Optional 1,237-step stair climb leading to a golden Buddha overlooking Krabi's karst mountains."),
            ("Khao Khanap Nam Twin Mountains", "Krabi's iconic twin karst bluffs rising dramatically over the river mouth.")
        ],
        "places_col2_title": "Town & Local Lifestyle",
        "places_col2_badge": "Local Flavors",
        "places_col2_items": [
            ("Giant Mud Crab & Eagle Statues", "Krabi's beloved bronze landmark celebrating local marine life and coastal biodiversity."),
            ("Maharaj Food & Fruit Market", "Lively local marketplace showcasing exotic fruits (mangosteen, rambutan, durian) and Thai snacks."),
            ("Krabi Town Waterfront Walk", "Paved esplanade with views across mangrove channels and local longtail fishing boats.")
        ],
        "inclusions": [
            "Private air-conditioned vehicle (SUV or Van) with fuel",
            "Professional local driver",
            "Hotel pick-up and drop-off in Krabi Town or Ao Nang",
            "Chilled bottled drinking water",
            "Flexible schedule tailored to your interests"
        ],
        "exclusions": [
            "English-speaking tour guide (available upon advance request)",
            "Temple donations and admission tickets (if any)",
            "Meals and refreshments",
            "Tips & gratuities for the driver"
        ],
        "timing_text": "Morning & afternoon private slots<br /><strong>Morning Slot:</strong> 09:00 AM – 01:30 PM<br /><strong>Afternoon Slot:</strong> 01:30 PM – 06:00 PM",
        "transport_text": "Dedicated private air-conditioned SUV or minivan exclusively for your party.",
        "what_to_bring": "Modest clothing covering shoulders and knees for temple visits, comfortable walking shoes, camera, and cash for market snacks.",
        "contact_tour_param": "Krabi+City+Tour+Half+Day+Private"
    },
    {
        "filename": "traditional_thai_cooking_class_krabi.html",
        "title": "Traditional Thai Cooking Class with Local Chef | Trippovention",
        "h1": "Traditional Thai Cooking Class with Local Chef",
        "subtitle": "Organic Herb Garden Tour, Hands-On Wok Cooking, Curry Paste Grinding & 5-Course Feasting",
        "meta_desc": "Learn to cook authentic Thai dishes in Krabi with an expert local chef. Includes organic garden tour, curry paste grinding, 5 dishes & digital recipe book.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/sightseeingoptions/hero_thai_cooking_class.webp",
        "duration": "Approx. 3.5 Hours",
        "price": "Contact Us",
        "price_note": "(Culinary Workshop)",
        "meetup": "Hotel Lobby (Ao Nang & Krabi Town)",
        "overview_p1": "Immerse your senses in the vibrant aromas and bold flavors of Thai culinary tradition. Hosted in a beautiful open-air garden kitchen setting, this hands-on workshop unlocks the secret balance of sweet, sour, salty, and spicy that defines Thai cuisine.",
        "overview_p2": "Begin with a guided tour of an organic herb garden to pick and smell fresh galangal, lemongrass, sweet Thai basil, and kaffir lime leaves. Under the step-by-step guidance of a master Thai chef, pound authentic curry paste from scratch using a stone mortar and pestle, cook 5 signature dishes at your personal wok station, and savor your creations in a serene open-air dining pavilion.",
        "places_col1_title": "Culinary Experience",
        "places_col1_badge": "Hands-On",
        "places_col1_items": [
            ("Organic Herb Garden Tour", "Learn to identify and harvest traditional Thai medicinal herbs, roots, and aromatics."),
            ("Stone Mortar & Pestle Grinding", "Master the age-old art of grinding fresh chilies, herbs, and spices into fragrant curry pastes."),
            ("Individual Cooking Station", "Cook each dish at your dedicated high-flame wok station with fresh premium ingredients.")
        ],
        "places_col2_title": "Menu Highlights",
        "places_col2_badge": "5 Classic Dishes",
        "places_col2_items": [
            ("Signature Pad Thai", "Wok-tossed rice noodles with tamarind sauce, tofu, peanuts, and lime."),
            ("Green Curry or Massaman Curry", "Rich coconut milk curry cooked with your handcrafted curry paste."),
            ("Tom Yum Goong or Tom Kha Gai", "Iconic spicy-sour soup flavored with lemongrass and galangal."),
            ("Mango Sticky Rice & Spring Rolls", "Crispy golden appetizer and Thailand's beloved coconut mango dessert.")
        ],
        "inclusions": [
            "Round-trip hotel transfers in Ao Nang and Krabi Town",
            "Guided organic kitchen garden tour",
            "Individual wok cooking station and all fresh ingredients",
            "Preparation and cooking of 5 full authentic dishes",
            "Full meal feasting on your cooked creations",
            "Illustrated digital color recipe booklet to take home",
            "Culinary course certificate of participation"
        ],
        "exclusions": [
            "Alcoholic beverages and specialty drinks",
            "Personal spending",
            "Tips & gratuities for the culinary team"
        ],
        "timing_text": "Morning & afternoon sessions daily<br /><strong>Morning Class:</strong> 09:00 AM – 12:30 PM<br /><strong>Afternoon Class:</strong> 01:30 PM – 05:00 PM",
        "transport_text": "Air-conditioned hotel minivan transfer to the open-air garden culinary academy.",
        "what_to_bring": "An eager appetite, camera for food photography, and light comfortable clothing. Aprons provided.",
        "contact_tour_param": "Traditional+Thai+Cooking+Class+with+Local+Chef"
    },
    {
        "filename": "krabi_town_night_markets_and_street_food_walk.html",
        "title": "Krabi Town Night Markets & Street Food Walk | Trippovention",
        "h1": "Krabi Town Night Markets & Street Food Walk",
        "subtitle": "Weekend Walking Street, Authentic Southern Street Delicacies, Live Music & Artisan Crafts",
        "meta_desc": "Experience the vibrant food and culture of Krabi Town's Night Markets. Guided walking tour with street food tastings, local desserts, and artisan stalls.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/tourpackages/hero_krabi_and_phuket_nature_retreat.webp",
        "duration": "Approx. 3–4 Hours",
        "price": "Contact Us",
        "price_note": "(Evening Tour)",
        "meetup": "Hotel Lobby (Ao Nang & Krabi Town)",
        "overview_p1": "Experience the colorful evening energy of Krabi Town's famous Walking Street market (Thanon Khon Dern). When twilight falls, the central streets of the provincial capital burst into vibrant life with hundreds of food stalls, artisan craft makers, and local street performers.",
        "overview_p2": "Accompanied by a knowledgeable local foodie guide, you will wander through bustling lanes sampling Southern Thai street delights: crispy rotis with condensed milk, charcoal-grilled chicken satay with peanut sauce, spicy som tum papaya salad, fresh seafood skewers, and coconut ice cream. Enjoy live music on the public stage and shop for handmade jewelry and local souvenirs.",
        "places_col1_title": "Night Market Sights",
        "places_col1_badge": "Evening Culture",
        "places_col1_items": [
            ("Krabi Walking Street", "The famous pedestrian night bazaar operating every Friday, Saturday, and Sunday evening."),
            ("Live Stage Entertainment", "Enjoy local Thai musicians, youth dance troupes, and acoustic acts in the town square."),
            ("Handcrafted Souvenirs", "Browse batik sarongs, hand-carved coconut crafts, paintings, and handmade jewelry.")
        ],
        "places_col2_title": "Street Food Delights",
        "places_col2_badge": "Flavors of Krabi",
        "places_col2_items": [
            ("Crispy Thai Roti & Satay", "Warm freshly fried banana rotis and tender chicken satay grilled over charcoal."),
            ("Southern Thai Curries & Noodles", "Sample fiery Gaeng Som curries and fresh rice noodles with herb accompaniments."),
            ("Exotic Tropical Desserts", "Taste fresh coconut ice cream served inside real coconut shells with sweet sticky rice.")
        ],
        "inclusions": [
            "Round-trip hotel transfers from Ao Nang and Krabi Town",
            "Guided tour through Krabi Walking Street & Chao Fah Night Market",
            "Curated tasting samples of popular street foods and desserts",
            "Bottled drinking water",
            "English-speaking local host"
        ],
        "exclusions": [
            "Main personal meals and alcoholic beverages",
            "Personal shopping purchases and souvenirs",
            "Tips & gratuities for the guide"
        ],
        "timing_text": "Friday, Saturday & Sunday evenings<br /><strong>Pick-up:</strong> 05:30 PM – 06:00 PM<br />Return approx. 09:00 PM – 09:30 PM",
        "transport_text": "Round-trip air-conditioned minivan transfer between hotel and Krabi Town Walking Street.",
        "what_to_bring": "Casual comfortable clothes, walking sandals, camera, and cash (Thai Baht) for shopping and snacks.",
        "contact_tour_param": "Krabi+Town+Night+Markets+and+Street+Food+Walk"
    },
    {
        "filename": "banyan_tree_spa_krabi_luxury_wellness.html",
        "title": "Banyan Tree Spa Krabi Luxury Wellness Experience | Trippovention",
        "h1": "Banyan Tree Spa Krabi Luxury Wellness",
        "subtitle": "5-Star Rainforest Wellness Sanctuary, Royal Thai Massage, Aromatherapy & Holistic Healing",
        "meta_desc": "Indulge in award-winning luxury spa treatments at Banyan Tree Spa Krabi on Tubkaek Beach. Holistic body therapies, Royal Thai massages, and hydrotherapy salas.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/krabi/sightseeingoptions/hero_krabi_banyan_tree_spa.webp",
        "duration": "Approx. 1–2 Hours",
        "price": "Contact Us",
        "price_note": "(5-Star Wellness)",
        "meetup": "Direct at Banyan Tree Spa Krabi (Tubkaek Beach)",
        "overview_p1": "Nestled into the verdant forested hills of peaceful Tubkaek Beach, Banyan Tree Spa Krabi is universally acclaimed as one of Thailand's most prestigious sanctuaries of wellness and holistic relaxation. The spa features private wooden treatment salas surrounded by lush flora, water features, and tranquil sea breezes.",
        "overview_p2": "Master therapists trained at the renowned Banyan Tree Spa Academy utilize organic virgin coconut oils, aromatic herbs, and time-honored Asian healing traditions. Choose from signature Royal Thai massages that stretch and re-energize muscles, deeply soothing aromatherapy treatments, or the groundbreaking 'The Rainforest' hydrotherapy trail designed to revitalize mind, body, and spirit.",
        "places_col1_title": "Therapeutic Treatments",
        "places_col1_badge": "World-Class Care",
        "places_col1_items": [
            ("Master Certified Therapists", "Expert practitioners with rigorous anatomical training delivering intuitive healing touches."),
            ("Royal Thai Signature Massage", "Traditional deep stretching, acupressure point release, and rhythmic compression without oils."),
            ("Aromatherapy & Herbal Wraps", "Nourishing virgin coconut oil and warm herbal compress poultices melting muscle tension.")
        ],
        "places_col2_title": "Spa Sanctuary Facilities",
        "places_col2_badge": "VIP Ambiance",
        "places_col2_items": [
            ("The Rainforest Hydrotherapy", "Krabi's exclusive hydrothermal circuit featuring vitality pools, sensory rain walks, steam, and sauna."),
            ("Private Deluxe Treatment Villas", "Opulent open-air suites with private stone soaking tubs and rain showers."),
            ("Herbal Welcome & Post-Spa Lounge", "Relax after your treatment with warm lemongrass tea, chilled infused water, and fresh fruit.")
        ],
        "inclusions": [
            "Selected luxury spa therapy or massage treatment package",
            "Welcome herbal refreshment and cool scented towel",
            "Access to private treatment villa and shower amenities",
            "Post-treatment relaxation tea and fresh seasonal fruit platter",
            "Plush bathrobes, slippers, and premium organic toiletries provided"
        ],
        "exclusions": [
            "Hotel transfer (available upon request as private luxury transfer)",
            "Gratuities for the spa therapists",
            "Personal retail purchases from Banyan Tree Spa Gallery"
        ],
        "timing_text": "Open daily: 10:00 AM – 09:00 PM<br /><strong>Last Treatment Entry:</strong> 07:30 PM (Advance booking required)",
        "transport_text": "Direct arrival at Banyan Tree Krabi Resort (Tubkaek Beach) or optional private transfer.",
        "what_to_bring": "Comfortable clothes. All robes, disposable undergarments, and towels provided at the spa.",
        "contact_tour_param": "Banyan+Tree+Spa+Krabi+Luxury+Wellness+Experience"
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
    <title>{title}</title>
    <meta name="description" content="{meta_desc}" />
    <meta name="author" content="Trippovention" />

    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://trippovention.co.th/packages/thailand/krabi/{filename}" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{meta_desc}" />
    <meta property="og:image" content="{og_image}" />

    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="https://trippovention.co.th/packages/thailand/krabi/{filename}" />
    <meta property="twitter:title" content="{title}" />
    <meta property="twitter:description" content="{meta_desc}" />
    <meta property="twitter:image" content="{og_image}" />

    <link rel="canonical" href="https://trippovention.co.th/packages/thailand/krabi/{filename}" />
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
      {{
        "@context": "https://schema.org",
        "@type": "TouristTrip",
        "name": "{h1}",
        "description": "{meta_desc}",
        "touristType": ["Travelers", "Adventure Seekers", "Families", "Couples"],
        "offers": {{
          "@type": "Offer",
          "price": "{price}",
          "priceCurrency": "THB",
          "availability": "https://schema.org/InStock",
          "url": "https://trippovention.co.th/packages/thailand/krabi/{filename}"
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
            "name": "Krabi",
            "item": "https://trippovention.co.th/packages/thailand/krabi/"
          }},
          {{
            "@type": "ListItem",
            "position": 5,
            "name": "Sightseeing",
            "item": "https://trippovention.co.th/packages/thailand/krabi/sightseeing.html"
          }},
          {{
            "@type": "ListItem",
            "position": 6,
            "name": "{h1}",
            "item": "https://trippovention.co.th/packages/thailand/krabi/{filename}"
          }}
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
      </nav>

      <header class="hero compact hero-thailand">
        <div class="container">
          <h1>{h1}</h1>
          <p>{subtitle}</p>
        </div>
      </header>

      <section class="section">
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
      </section>

      <section class="section alt">
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
                <div class="badge">{places_col1_badge}</div>
                <h3>{places_col1_title}</h3>
                <ul class="muted" style="line-height: 1.9; margin-top: 12px;">
{places_col1_html}
                </ul>
              </div>
            </div>

            <div class="card">
              <div class="body">
                <div class="badge">{places_col2_badge}</div>
                <h3>{places_col2_title}</h3>
                <ul class="muted" style="line-height: 1.9; margin-top: 12px;">
{places_col2_html}
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
{inclusions_html}
                </ul>
              </div>
            </div>

            <div class="card">
              <div class="body">
                <h3>❌ Exclusions</h3>
                <ul class="muted" style="line-height: 1.8; margin-top: 12px;">
{exclusions_html}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div class="section-title">
            <h2>Tour Information &amp; Schedule</h2>
            <p class="subtitle">Practical guidelines for a smooth and memorable excursion</p>
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
      </section>

      <section class="section cta">
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
              href="../../../contact.html?destination=krabi&tour={contact_tour_param}"
              >📞 Request Custom Quote</a
            >
            <a
              class="btn btn-lg ghost ml-16"
              href="https://wa.me/66946934392?text=Hello,%20I%20am%20interested%20in%20booking%20the%20{contact_tour_param}%20in%20Krabi"
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
              <a href="sightseeing.html">Krabi Sightseeing</a><br />
              <a href="../../../contact.html">Contact Us</a>
            </div>
          </div>
          <div>
            <h3>Legal &amp; Social</h3>
            <div class="line-height-2">
              <a href="../../../privacy-policy.html">Privacy Policy</a><br />
              <a href="../../../terms-and-conditions.html">Terms &amp; Conditions</a><br />
              <a href="../../../refund-policy.html">Refund Policy</a>
            </div>
            <div class="social-links mt-20">
              <a
                href="https://www.facebook.com/trippovention"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Follow us on Facebook"
              >
                <img
                  src="../../../assets/images/social/facebook.svg"
                  alt="Facebook"
                  class="social-icon"
                  loading="lazy"
                />
              </a>
              <a
                href="https://www.instagram.com/trippovention"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Follow us on Instagram"
              >
                <img
                  src="../../../assets/images/social/instagram.svg"
                  alt="Instagram"
                  class="social-icon"
                  loading="lazy"
                />
              </a>
              <a
                href="https://wa.me/66946934392"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Chat with us on WhatsApp"
              >
                <img
                  src="../../../assets/images/social/whatsapp.svg"
                  alt="WhatsApp"
                  class="social-icon whatsapp-green"
                  loading="lazy"
                />
              </a>
            </div>
          </div>
        </div>
        <div class="text-center mt-40">
          <p class="muted">
            &copy; 2026 Trippovention. All rights reserved. Registered travel agency in Thailand.
          </p>
        </div>
      </div>
    </footer>

    <script src="../../../assets/app.js" defer></script>
    <script src="../../../assets/search.js" defer></script>
  </body>
</html>
"""

def generate_pages():
    for tour in TOURS_DATA:
        p1_items_html = "\n".join(f"                  <li><strong>{title}:</strong> {desc}</li>" for title, desc in tour["places_col1_items"])
        p2_items_html = "\n".join(f"                  <li><strong>{title}:</strong> {desc}</li>" for title, desc in tour["places_col2_items"])
        inc_html = "\n".join(f"                  <li>{item}</li>" for item in tour["inclusions"])
        exc_html = "\n".join(f"                  <li>{item}</li>" for item in tour["exclusions"])

        page_content = HTML_TEMPLATE.format(
            filename=tour["filename"],
            title=tour["title"],
            h1=tour["h1"],
            subtitle=tour["subtitle"],
            meta_desc=tour["meta_desc"],
            og_image=tour["og_image"],
            duration=tour["duration"],
            price=tour["price"],
            price_note=tour["price_note"],
            meetup=tour["meetup"],
            overview_p1=tour["overview_p1"],
            overview_p2=tour["overview_p2"],
            places_col1_badge=tour["places_col1_badge"],
            places_col1_title=tour["places_col1_title"],
            places_col1_html=p1_items_html,
            places_col2_badge=tour["places_col2_badge"],
            places_col2_title=tour["places_col2_title"],
            places_col2_html=p2_items_html,
            inclusions_html=inc_html,
            exclusions_html=exc_html,
            timing_text=tour["timing_text"],
            transport_text=tour["transport_text"],
            what_to_bring=tour["what_to_bring"],
            contact_tour_param=tour["contact_tour_param"]
        )

        out_path = os.path.join(DEST_DIR, tour["filename"])
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_content)
        print(f"Generated: {out_path}")

if __name__ == "__main__":
    generate_pages()
