#!/usr/bin/env python3
"""
Generate the Phuket Sightseeing Catalogue Page:
docs/packages/thailand/phuket/sightseeing.html
Modeled directly on docs/packages/thailand/krabi/sightseeing.html, Bangkok, and Pattaya catalogues.
Preserves design system, typography, colors, centered curated collections,
search/filtering engine, 24 experiences, 10 FAQs, and JSON-LD schemas.
"""

import os

CATALOGUE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs", "packages", "thailand", "phuket", "sightseeing.html"
)

EXPERIENCES = [
    {
        "id": "hkt-01",
        "name": "Phuket City Highlights & Landmarks Tour",
        "link": "phuket_city_highlights_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_city_highlights.webp",
        "alt": "Phuket City Highlights Tour Wat Chalong and Karon Viewpoint",
        "ribbon": "🏛️ Top Rated",
        "category": "city-culture",
        "category_label": "City & Culture",
        "collections": "city-culture",
        "duration": "half-day",
        "duration_hours": "4.5",
        "duration_label": "⏱️ Half Day (4–5 Hrs)",
        "tour_type": "guided",
        "tour_type_label": "Guided Minivan Tour",
        "styles": "culture,family",
        "price": "950",
        "price_display": "THB 950",
        "price_unit": "Price Per Person",
        "highlights": [
            "Wat Chalong Grand Pagoda enshrining Lord Buddha bone relic",
            "Panoramic 3-bay coastal outlook at Karon Viewpoint",
            "Historic Sino-Portuguese shophouses and street murals in Old Town",
            "Cashew nut factory processing and local product tastings"
        ],
        "enquiry_param": "Phuket+City+Highlights+Tour"
    },
    {
        "id": "hkt-02",
        "name": "Phi Phi, Maya Bay & Bamboo Island Premium Tour",
        "link": "phi_phi_maya_bamboo_island_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phi_phi_maya_bamboo.webp",
        "alt": "Phi Phi Islands Maya Bay and Bamboo Island speedboat tour from Phuket",
        "ribbon": "⭐ Bestseller",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "full-day",
        "duration_hours": "8.5",
        "duration_label": "⏱️ Full Day (8–9 Hrs)",
        "tour_type": "speedboat",
        "tour_type_label": "Speedboat Tour",
        "styles": "beach,adventure",
        "price": "2100",
        "price_display": "THB 2,100",
        "price_unit": "Price Per Person",
        "highlights": [
            "Set foot on the powdery white coral sands of world-famous Maya Bay",
            "Swim and jump into the turquoise waters of enclosed Pileh Lagoon",
            "Snorkel pristine shallow reefs and unwind on idyllic Bamboo Island",
            "Full buffet lunch at Phi Phi Don and sights of Viking Cave & Monkey Beach"
        ],
        "enquiry_param": "Phi+Phi+Maya+Bamboo+Island+Tour"
    },
    {
        "id": "hkt-03",
        "name": "Carnival Magic Show with Dinner",
        "link": "carnival_magic_show.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_carnival_magic_show_with_dinner.webp",
        "alt": "Carnival Magic Phuket nighttime theme park with dinner",
        "ribbon": "✨ Guinness Record",
        "category": "shows-entertainment",
        "category_label": "Shows & Entertainment",
        "collections": "shows-entertainment,waterparks-family",
        "duration": "evening",
        "duration_hours": "5",
        "duration_label": "⏱️ Evening (5–6 Hrs)",
        "tour_type": "show",
        "tour_type_label": "Theme Park & Show",
        "styles": "family,luxury",
        "price": "2200",
        "price_display": "THB 2,200",
        "price_unit": "Price Per Person",
        "highlights": [
            "Kingdom of Lights illuminated park featuring 40+ million glowing LEDs",
            "Colossal River Carnival indoor parade pageant and acrobatic floats",
            "Lavish dinner at the 3,000-seat Bird of Paradise buffet restaurant",
            "Round-trip air-conditioned hotel transfers from major beach resorts"
        ],
        "enquiry_param": "Carnival+Magic+Show+with+Dinner"
    },
    {
        "id": "hkt-04",
        "name": "Phuket Ethical Elephant Sanctuary",
        "link": "elephant_sanctuary.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_elephant_sanctuary.webp",
        "alt": "Ethical Elephant Sanctuary Phuket rescued elephant care",
        "ribbon": "🌿 100% Ethical",
        "category": "nature-wildlife",
        "category_label": "Nature & Wildlife",
        "collections": "nature-wildlife",
        "duration": "half-day",
        "duration_hours": "4",
        "duration_label": "⏱️ Half Day (4 Hrs)",
        "tour_type": "guided",
        "tour_type_label": "Eco Sanctuary Experience",
        "styles": "nature,family",
        "price": "2500",
        "price_display": "THB 2,500",
        "price_unit": "Price Per Person",
        "highlights": [
            "Strict no-riding, ethical observation sanctuary supporting rescued elephants",
            "Prepare nutritional herbal fruit balls and feed gentle pachyderms",
            "Observe elephants splashing and bathing naturally in freshwater lagoons",
            "Educational talk by passionate mahouts and vegetarian Thai buffet lunch"
        ],
        "enquiry_param": "Phuket+Elephant+Sanctuary"
    },
    {
        "id": "hkt-05",
        "name": "James Bond Island & Phang Nga Bay Tour",
        "link": "james_bond_island_speedboat_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_james_bond_island_speedboat_tour.webp",
        "alt": "James Bond Island Koh Tapu Phang Nga Bay speedboat tour Phuket",
        "ribbon": "🎬 Cinematic Icon",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "full-day",
        "duration_hours": "8",
        "duration_label": "⏱️ Full Day (8 Hrs)",
        "tour_type": "speedboat",
        "tour_type_label": "Speedboat & Canoe",
        "styles": "nature,adventure",
        "price": "1800",
        "price_display": "THB 1,800",
        "price_unit": "Price Per Person",
        "highlights": [
            "Iconic Koh Tapu limestone nail karst featured in 007's The Man with the Golden Gun",
            "Paddle inflatable sea canoes through hidden caves and limestone hongs at Koh Hong",
            "Visit the stilted Muslim seafaring fishing village of Koh Panyee",
            "Delicious seafood buffet lunch and mangrove river delta cruising"
        ],
        "enquiry_param": "James+Bond+Island+Tour"
    },
    {
        "id": "hkt-06",
        "name": "Phi Phi & Khai Islands Speedboat Tour",
        "link": "phi_phi_island_and_khai_island_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phi_phi_island_and_khai_island_tour_with_lunch_round_trip_transfer.webp",
        "alt": "Phi Phi Island and Khai Island speedboat tour with lunch Phuket",
        "ribbon": "🐠 Snorkeling Classic",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "full-day",
        "duration_hours": "8",
        "duration_label": "⏱️ Full Day (8 Hrs)",
        "tour_type": "speedboat",
        "tour_type_label": "Speedboat Tour",
        "styles": "beach,family",
        "price": "1900",
        "price_display": "THB 1,900",
        "price_unit": "Price Per Person",
        "highlights": [
            "Explore Phi Phi Leh highlights including Maya Bay, Pileh Cove & Viking Cave",
            "Snorkel crystal shallow waters right off the white sandy beaches of Khai Nok",
            "Buffet lunch served on Phi Phi Don Island with scenic bay views",
            "Abundant tropical fish encounters ideal for kids and beginner snorkelers"
        ],
        "enquiry_param": "Phi+Phi+and+Khai+Island+Tour"
    },
    {
        "id": "hkt-07",
        "name": "Phuket FantaSea Cultural Show with Dinner",
        "link": "phuket_fantasea_show.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_fantasea_show_with_dinner.webp",
        "alt": "Phuket FantaSea cultural theme park show Kamala Beach",
        "ribbon": "🎪 Cultural Classic",
        "category": "shows-entertainment",
        "category_label": "Shows & Entertainment",
        "collections": "shows-entertainment",
        "duration": "evening",
        "duration_hours": "4.5",
        "duration_label": "⏱️ Evening (4–5 Hrs)",
        "tour_type": "show",
        "tour_type_label": "Cultural Show & Dinner",
        "styles": "culture,family",
        "price": "2100",
        "price_display": "THB 2,100",
        "price_unit": "Price Per Person",
        "highlights": [
            "Palace of the Elephants 3,000-seat theatrical auditorium spectacle",
            "Las Vegas-style staging, aerial acrobatics, pyrotechnics & Thai folklore",
            "Grand Golden Kinnaree 4,000-seat royal banquet buffet dinner",
            "Carnival Village shopping street with traditional games and artisan crafts"
        ],
        "enquiry_param": "Phuket+FantaSea+Show+with+Dinner"
    },
    {
        "id": "hkt-08",
        "name": "Hanuman World Zipline & ATV Adventure",
        "link": "hanuman_world_zipline_and_atv_adventure.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_hanuman_world_zipline.webp",
        "alt": "Hanuman World Phuket treetop zipline and ATV adventure",
        "ribbon": "⚡ High Thrill",
        "category": "adventure-outdoor",
        "category_label": "Adventure & Outdoor",
        "collections": "adventure-outdoor",
        "duration": "half-day",
        "duration_hours": "3.5",
        "duration_label": "⏱️ 3–4 Hours",
        "tour_type": "adventure",
        "tour_type_label": "Canopy & Off-Road",
        "styles": "adventure",
        "price": "2200",
        "price_display": "THB 2,200",
        "price_unit": "Price Per Person",
        "highlights": [
            "Soar through pristine tropical rainforest canopy on high-speed dual ziplines",
            "Brave the 800m Roller Zipline curving and swooping through the trees",
            "Elevated Sky Walk treetop bridge with panoramic jungle valley views",
            "Rugged guide-led ATV quad bike expedition tackling muddy jungle trails"
        ],
        "enquiry_param": "Hanuman+World+Zipline+ATV+Adventure"
    },
    {
        "id": "hkt-09",
        "name": "Phuket Simon Cabaret Show",
        "link": "simon_cabaret_show_phuket.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_simon_cabaret_show.webp",
        "alt": "Phuket Simon Cabaret transgender musical show in Patong",
        "ribbon": "💃 Glamour & Dance",
        "category": "shows-entertainment",
        "category_label": "Shows & Entertainment",
        "collections": "shows-entertainment",
        "duration": "evening",
        "duration_hours": "1.25",
        "duration_label": "⏱️ 1 Hr 15 Mins",
        "tour_type": "show",
        "tour_type_label": "Musical Theatre Show",
        "styles": "culture,family",
        "price": "900",
        "price_display": "THB 900",
        "price_unit": "Price Per Person",
        "highlights": [
            "Phuket's legendary ladyboy musical cabaret performing since 1991 in Patong",
            "Extravagant feathered costumes, glittering ballgowns & grand stage sets",
            "High-energy song-and-dance tributes spanning Broadway, Bollywood & pop",
            "Family-friendly theatrical revue suitable for travelers of all ages"
        ],
        "enquiry_param": "Phuket+Simon+Cabaret+Show"
    },
    {
        "id": "hkt-10",
        "name": "Aquaria Phuket & AR Trick Eye Museum",
        "link": "aquaria_phuket_tickets.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_aquaria_phuket.webp",
        "alt": "Aquaria Phuket oceanarium and AR Trick Eye museum",
        "ribbon": "🦈 Marine Wonder",
        "category": "waterparks-family",
        "category_label": "Family Attractions",
        "collections": "waterparks-family",
        "duration": "half-day",
        "duration_hours": "2.5",
        "duration_label": "⏱️ 2–3 Hours",
        "tour_type": "attraction",
        "tour_type_label": "Indoor Oceanarium",
        "styles": "family,nature",
        "price": "850",
        "price_display": "THB 850",
        "price_unit": "Price Per Person",
        "highlights": [
            "Thailand's largest oceanarium housing 25,000+ aquatic animals across 4 zones",
            "Massive panoramic ocean tank window with stingrays, sharks & sea turtles",
            "Enchanting live mermaid synchronized swimming and diver feeding shows",
            "Interactive AR Trick Eye Museum 4D augmented reality photo galleries"
        ],
        "enquiry_param": "Aquaria+Phuket+Tickets"
    },
    {
        "id": "hkt-11",
        "name": "Authentic Thai Cooking Class with Market Tour",
        "link": "phuket_thai_cooking_class.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_thai_cooking_class.webp",
        "alt": "Thai cooking class with local fresh morning market tour Phuket",
        "ribbon": "👨‍🍳 Culinary Master",
        "category": "food-wellness",
        "category_label": "Food & Wellness",
        "collections": "food-wellness",
        "duration": "half-day",
        "duration_hours": "4",
        "duration_label": "⏱️ 4 Hours",
        "tour_type": "guided",
        "tour_type_label": "Interactive Workshop",
        "styles": "culture,family",
        "price": "1600",
        "price_display": "THB 1,600",
        "price_unit": "Price Per Person",
        "highlights": [
            "Chef-guided morning walking tour of vibrant local produce market",
            "Hand-pound aromatic green and red curry pastes with granite mortar & pestle",
            "Individual wok cooking stations to master 4 classic Thai dishes from scratch",
            "Printed full-color recipe booklet and gourmet meal tasting"
        ],
        "enquiry_param": "Phuket+Thai+Cooking+Class"
    },
    {
        "id": "hkt-12",
        "name": "Coral & Racha Island Speedboat Day Tour",
        "link": "coral_and_racha_island_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_coral_and_racha_island.webp",
        "alt": "Coral Island Koh Hey and Racha Yai speedboat tour from Phuket",
        "ribbon": "🏝️ Island Hopping",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "full-day",
        "duration_hours": "7.5",
        "duration_label": "⏱️ Full Day (7–8 Hrs)",
        "tour_type": "speedboat",
        "tour_type_label": "Speedboat Tour",
        "styles": "beach,adventure",
        "price": "1450",
        "price_display": "THB 1,450",
        "price_unit": "Price Per Person",
        "highlights": [
            "Relax on white sandy Banana Beach at Coral Island with shallow coral reefs",
            "Optional water sports including parasailing, sea walker & banana boat rides",
            "Snorkel the crystal-clear 20m visibility waters of Patok Bay at Racha Yai",
            "Delicious Thai buffet lunch and round-trip transfers from Chalong Pier"
        ],
        "enquiry_param": "Coral+and+Racha+Island+Tour"
    },
    {
        "id": "hkt-13",
        "name": "Similan Islands Snorkeling Excursion (Seasonal)",
        "link": "similan_islands_snorkeling_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_similan_islands_snorkeling.webp",
        "alt": "Similan Islands National Park snorkeling day tour from Phuket",
        "ribbon": "🌊 World Top 10",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "full-day",
        "duration_hours": "11",
        "duration_label": "⏱️ Full Day (11 Hrs)",
        "tour_type": "speedboat",
        "tour_type_label": "Speedboat Expedition",
        "styles": "nature,adventure",
        "price": "2800",
        "price_display": "THB 2,800",
        "price_unit": "Price Per Person",
        "highlights": [
            "Strictly seasonal marine park open only from October 15 to May 15",
            "Hike up to the world-famous Sail Rock viewpoint overlooking Donald Duck Bay",
            "Encounter wild sea turtles and schools of tropical fish in 30m visibility",
            "Flour-soft powder white beaches and majestic granite boulder formations"
        ],
        "enquiry_param": "Similan+Islands+Snorkeling+Tour"
    },
    {
        "id": "hkt-14",
        "name": "Phuket Sunset Catamaran Yacht Cruise",
        "link": "phuket_sunset_catamaran_cruise.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_sunset_catamaran_cruise.webp",
        "alt": "Sunset catamaran sailing cruise to Promthep Cape Phuket",
        "ribbon": "🌅 Romantic Cruise",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "half-day",
        "duration_hours": "5",
        "duration_label": "⏱️ 5 Hours (Sunset)",
        "tour_type": "cruises-boats",
        "tour_type_label": "Luxury Sailing Catamaran",
        "styles": "luxury,beach",
        "price": "1950",
        "price_display": "THB 1,950",
        "price_unit": "Price Per Person",
        "highlights": [
            "Luxury double-hulled sailing catamaran with expansive trampoline sun nets",
            "Snorkeling, swimming & stand-up paddleboarding off secluded Coral Island",
            "Unobstructed golden-hour sunset vistas off Promthep Cape and Laem Krating",
            "Onboard barbecue chicken & seafood dinner with sparkling sunset toast"
        ],
        "enquiry_param": "Phuket+Sunset+Catamaran+Cruise"
    },
    {
        "id": "hkt-15",
        "name": "Phuket Scuba Diving Day Trip (Racha Yai)",
        "link": "phuket_scuba_diving_day_trip.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_scuba_diving_day_trip.webp",
        "alt": "Scuba diving day trip to Racha Yai Island from Phuket",
        "ribbon": "🤿 2 Boat Dives",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "full-day",
        "duration_hours": "7.5",
        "duration_label": "⏱️ Full Day (7–8 Hrs)",
        "tour_type": "guided",
        "tour_type_label": "Guided Scuba Dives",
        "styles": "adventure,nature",
        "price": "3400",
        "price_display": "THB 3,400",
        "price_unit": "Price Per Person",
        "highlights": [
            "Two guided boat dives at Racha Yai with certified PADI Divemasters",
            "Submerged concrete elephant statues and artificial reefs at Siam Bay",
            "Suitable for both certified divers and first-time Discover Scuba beginners",
            "Spacious 3-deck dive vessel with hot breakfast and freshly cooked buffet lunch"
        ],
        "enquiry_param": "Phuket+Scuba+Diving+Day+Trip"
    },
    {
        "id": "hkt-16",
        "name": "Phuket Old Town Heritage & Street Food Tour",
        "link": "phuket_old_town_heritage_walking_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_old_town_heritage.webp",
        "alt": "Phuket Old Town heritage walking tour and street food tasting",
        "ribbon": "🍜 UNESCO Flavors",
        "category": "city-culture",
        "category_label": "City & Culture",
        "collections": "city-culture,food-wellness",
        "duration": "half-day",
        "duration_hours": "3.5",
        "duration_label": "⏱️ 3.5 Hours",
        "tour_type": "guided",
        "tour_type_label": "Walking & Food Tour",
        "styles": "culture,family",
        "price": "850",
        "price_display": "THB 850",
        "price_unit": "Price Per Person",
        "highlights": [
            "Stroll pastel Sino-Portuguese shophouses along Thalang Road and Soi Romanee",
            "Visit the 130-year-old hidden Shrine of the Serene Light (San Chao Seng Tham)",
            "Taste 4 authentic local dishes in Thailand's designated UNESCO City of Gastronomy",
            "Sample Hokkien fried noodles, fresh popiah rolls & signature O-Aew shaved ice"
        ],
        "enquiry_param": "Phuket+Old+Town+Walking+Tour"
    },
    {
        "id": "hkt-17",
        "name": "Phuket Luxury Thai Spa & Wellness Retreat",
        "link": "phuket_luxury_spa_and_wellness.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_luxury_spa_wellness.webp",
        "alt": "Luxury Thai spa wellness treatment in botanical pavilion Phuket",
        "ribbon": "🌿 Holistic Wellness",
        "category": "food-wellness",
        "category_label": "Food & Wellness",
        "collections": "food-wellness",
        "duration": "half-day",
        "duration_hours": "2.5",
        "duration_label": "⏱️ 2–3 Hours",
        "tour_type": "attraction",
        "tour_type_label": "Spa Sanctuary",
        "styles": "luxury",
        "price": "1500",
        "price_display": "THB 1,500",
        "price_unit": "Price Per Person",
        "highlights": [
            "Tranquil botanical garden spa pavilions in Patong, Kata, or Laguna",
            "Traditional Royal Thai acupressure massage and steaming herbal ball compress",
            "Aromatherapy warm essential oil body massage and floral foot bath ritual",
            "Complimentary post-treatment organic bael herbal tea and tropical refreshments"
        ],
        "enquiry_param": "Phuket+Luxury+Spa+Retreat"
    },
    {
        "id": "hkt-18",
        "name": "Private Phuket City & Scenic Viewpoints Tour",
        "link": "private_phuket_city_and_viewpoints_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_private_phuket_city_viewpoints.webp",
        "alt": "Private VIP minivan tour of Phuket viewpoints and landmarks",
        "ribbon": "👑 100% Private",
        "category": "city-culture",
        "category_label": "City & Culture",
        "collections": "city-culture",
        "duration": "full-day",
        "duration_hours": "8",
        "duration_label": "⏱️ 6–8 Hours Flexible",
        "tour_type": "private",
        "tour_type_label": "Private Minivan Hire",
        "styles": "luxury,family",
        "price": "2500",
        "price_display": "THB 2,500",
        "price_unit": "Per Van (Up to 10 Pax)",
        "highlights": [
            "Dedicated private Toyota Commuter VIP van and experienced local chauffeur",
            "100% customizable itinerary: Big Buddha, Wat Chalong, Promthep Cape & Old Town",
            "Explore at your own relaxed pace without fixed group schedules",
            "Direct hotel, private villa, or Phuket International Airport pickup"
        ],
        "enquiry_param": "Private+Phuket+City+Tour"
    },
    {
        "id": "hkt-19",
        "name": "Khao Sok National Park & Cheow Lan Lake Excursion",
        "link": "khao_sok_national_park_day_trip.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_khao_sok_cheow_lan_lake.webp",
        "alt": "Khao Sok National Park Cheow Lan Lake longtail boat day trip from Phuket",
        "ribbon": "🌲 Primeval Wilderness",
        "category": "adventure-outdoor",
        "category_label": "Adventure & Nature",
        "collections": "adventure-outdoor,nature-wildlife",
        "duration": "full-day",
        "duration_hours": "11.5",
        "duration_label": "⏱️ Full Day (11–12 Hrs)",
        "tour_type": "guided",
        "tour_type_label": "Eco Rainforest Trip",
        "styles": "nature,adventure",
        "price": "2900",
        "price_display": "THB 2,900",
        "price_unit": "Price Per Person",
        "highlights": [
            "Explore 160-million-year-old ancient evergreen rainforests in Surat Thani",
            "Traditional longtail cruise through towering limestone karsts of Cheow Lan Lake",
            "Photograph iconic Khao Sam Kler (Three Brothers) jagged limestone pinnacles",
            "Southern Thai buffet lunch and freshwater swimming at a floating raft house"
        ],
        "enquiry_param": "Khao+Sok+National+Park+Day+Trip"
    },
    {
        "id": "hkt-20",
        "name": "Andamanda Phuket Water Park Day Pass",
        "link": "andamanda_phuket_water_park_tickets.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_andamanda_phuket_water_park.webp",
        "alt": "Andamanda Phuket water park slides and wave pool in Kathu",
        "ribbon": "🌊 25 Attractions",
        "category": "waterparks-family",
        "category_label": "Family Attractions",
        "collections": "waterparks-family",
        "duration": "full-day",
        "duration_hours": "6",
        "duration_label": "⏱️ Full Day (5–6 Hrs)",
        "tour_type": "attraction",
        "tour_type_label": "Themed Water Park",
        "styles": "family,adventure",
        "price": "1450",
        "price_display": "THB 1,450",
        "price_unit": "Price Per Person",
        "highlights": [
            "Massive 22-acre Thai mythological water world with 5 distinct themed zones",
            "25 exhilarating water slides including vertical drop chutes and raft coasters",
            "Southeast Asia's largest wave pool generating surf waves up to 3 meters",
            "550m Rolling Ripples lazy river winding through artificial jungle caves"
        ],
        "enquiry_param": "Andamanda+Phuket+Water+Park"
    },
    {
        "id": "hkt-21",
        "name": "Siam Niramit Phuket Cultural Spectacular",
        "link": "siam_niramit_phuket_show.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_siam_niramit_phuket.webp",
        "alt": "Siam Niramit Phuket grand stage cultural show with dinner",
        "ribbon": "🎭 Grand Stage",
        "category": "shows-entertainment",
        "category_label": "Shows & Entertainment",
        "collections": "shows-entertainment",
        "duration": "evening",
        "duration_hours": "3.5",
        "duration_label": "⏱️ Evening (3–4 Hrs)",
        "tour_type": "show",
        "tour_type_label": "Cultural Production",
        "styles": "culture,family",
        "price": "1700",
        "price_display": "THB 1,700",
        "price_unit": "Price Per Person",
        "highlights": [
            "Colossal 65m stage production with 100+ performers and 500+ authentic costumes",
            "Airborne angels, live river on stage, thunder effects & 700 years of Siamese history",
            "Traditional Thai Village of Four Regions living museum and Muay Thai demos",
            "Grand international dinner buffet with extensive Thai, Western & Indian cuisines"
        ],
        "enquiry_param": "Siam+Niramit+Phuket+Show"
    },
    {
        "id": "hkt-22",
        "name": "Phuket Surfing & Stand-Up Paddleboard Experience",
        "link": "phuket_surfing_and_stand_up_paddleboarding.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_surfing_sup.webp",
        "alt": "Surfing and stand-up paddleboarding lessons Kata Beach Phuket",
        "ribbon": "🏄 Surfing Capital",
        "category": "adventure-outdoor",
        "category_label": "Adventure & Water Sports",
        "collections": "adventure-outdoor",
        "duration": "half-day",
        "duration_hours": "2",
        "duration_label": "⏱️ 2 Hours / Half Day",
        "tour_type": "adventure",
        "tour_type_label": "Ocean Sports Lesson",
        "styles": "adventure,beach",
        "price": "1200",
        "price_display": "THB 1,200",
        "price_unit": "Price Per Person",
        "highlights": [
            "ISA-certified surf coaches providing beginner lessons on safe sandy breaks",
            "Catch gentle monsoon waves at Kata Beach (May–Oct) with foam soft-top boards",
            "Scenic flat-water stand-up paddleboard (SUP) cruising during calm season (Nov–Apr)",
            "Includes protective rashguard, shower facilities, lockers, and sports insurance"
        ],
        "enquiry_param": "Phuket+Surfing+and+SUP+Experience"
    },
    {
        "id": "hkt-23",
        "name": "Phuket Private Luxury Yacht Charter",
        "link": "phuket_private_yacht_charter.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_private_yacht_charter.webp",
        "alt": "Private luxury catamaran yacht charter in Andaman Sea Phuket",
        "ribbon": "🛥️ VIP Charter",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "full-day",
        "duration_hours": "8",
        "duration_label": "⏱️ Full Day (8 Hrs)",
        "tour_type": "private",
        "tour_type_label": "Private Yacht Charter",
        "styles": "luxury,beach",
        "price": "19500",
        "price_display": "THB 19,500",
        "price_unit": "Per Yacht (Up to 15 Pax)",
        "highlights": [
            "Exclusive private catamaran or motor yacht charter with professional captain & crew",
            "Tailored route to Maiton Island dolphin grounds, Coral Island, or Racha Yai",
            "Onboard Bluetooth sound system, stand-up paddleboards & high-end snorkel gear",
            "BYO alcoholic drinks with zero corkage fees, ice, glassware, and fresh tropical fruit"
        ],
        "enquiry_param": "Private+Phuket+Yacht+Charter"
    },
    {
        "id": "hkt-24",
        "name": "Phuket Viewpoints, Wat Chalong & Big Buddha Tour",
        "link": "phuket_viewpoints_and_big_buddha_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_big_buddha_wat_chalong.webp",
        "alt": "Phuket Big Buddha atop Nakkerd Hill and Wat Chalong temple tour",
        "ribbon": "🧘 Sacred Panoramas",
        "category": "city-culture",
        "category_label": "City & Culture",
        "collections": "city-culture",
        "duration": "half-day",
        "duration_hours": "4.5",
        "duration_label": "⏱️ Half Day (4–5 Hrs)",
        "tour_type": "guided",
        "tour_type_label": "Scenic & Cultural Tour",
        "styles": "culture,family",
        "price": "950",
        "price_display": "THB 950",
        "price_unit": "Price Per Person",
        "highlights": [
            "Ascend Nakkerd Hill to stand beneath the monumental 45m white marble Big Buddha",
            "Admire sweeping 360-degree vistas over Chalong Bay, Kata, and southern Phuket",
            "Pay respects at Wat Chalong temple and receive a traditional monk blessing",
            "Dramatic coastal viewpoints at Windmill Viewpoint and legendary Promthep Cape"
        ],
        "enquiry_param": "Phuket+Viewpoints+and+Big+Buddha+Tour"
    }
]

FAQS_DATA = [
    (
        "What are the absolute must-do sightseeing activities in Phuket for first-time visitors?",
        "For first-time visitors to Phuket, we recommend balancing island-hopping with cultural discovery: (1) A full-day speedboat excursion to Phi Phi Islands and Maya Bay or the dramatic limestone karsts of James Bond Island in Phang Nga Bay; (2) The Phuket City Highlights Tour visiting Karon Viewpoint, the 45-meter Big Buddha atop Nakkerd Hill, Wat Chalong temple, and colorful Sino-Portuguese Phuket Old Town; (3) An evening cultural spectacular such as Carnival Magic or Phuket Simon Cabaret; and (4) An ethical elephant interaction experience at Phuket Elephant Sanctuary."
    ),
    (
        "How do Phuket island tours operate, and what is the difference between Phi Phi and Phang Nga Bay?",
        "Phi Phi Islands (located 45km southeast of Phuket in the open Andaman Sea) are world-famous for turquoise crystalline waters, coral reef snorkeling, sheer karst cliffs, and powdery beaches like Maya Bay and Bamboo Island. Phang Nga Bay (located 35km northeast of Phuket) is a sheltered, emerald-green bay surrounded by hundreds of vertical limestone pillars, featuring sea-cave kayaking into hidden hongs and the famous James Bond Island (Koh Tapu). Both depart in modern twin-engine or triple-engine speedboats with hotel transfers, buffet lunch, and guide service included."
    ),
    (
        "Are hotel pickups and drop-offs included in Phuket sightseeing tours?",
        "Yes, the vast majority of our join-in and private sightseeing tours include complimentary round-trip hotel transfers from Phuket's main beach districts—including Patong, Kata, Karon, Rawai, Chalong, and Phuket Town. For hotels located in northern or more secluded areas (such as Mai Khao, Nai Yang, Naithon, or Cape Panwa), a small geographic zone transfer surcharge may apply, which is always confirmed clearly before booking."
    ),
    (
        "When is the best time of year for island tours, diving, and boat excursions in Phuket?",
        "Phuket enjoys warm tropical temperatures year-round. The peak dry season runs from November through April, characterized by calm, turquoise seas, sunny blue skies, and optimal underwater visibility for snorkeling, diving, and catamaran sailing. Seasonal marine national parks like the Similan Islands are open exclusively from October 15 to May 15. The green/monsoon season (May to October) brings refreshing tropical showers and larger ocean swells, making it ideal for surfing at Kata Beach and lush jungle adventures like Hanuman World ziplining."
    ),
    (
        "What are the top family-friendly attractions and sightseeing tours in Phuket?",
        "Phuket is an exceptional family destination. Top attractions for travelers with kids include: (1) Andamanda Phuket Water Park, featuring 25 themed slides, a 550m lazy river, and a gentle wave pool; (2) Aquaria Phuket & AR Trick Eye Museum at Central Floresta, offering indoor ocean tanks and interactive 3D photos; (3) Phuket Elephant Sanctuary for educational, safe elephant feeding; (4) The Coral and Khai Island speedboat tours, offering calm shallow waters where children can snorkel right off the beach; and (5) Carnival Magic's dazzling Kingdom of Lights theme park."
    ),
    (
        "Are the elephant sanctuaries promoted by Trippovention ethical and cruelty-free?",
        "Yes, absolutely. Trippovention is firmly committed to responsible wildlife tourism. We partner exclusively with ethical elephant sanctuaries that observe strict no-riding, no-chains, and no-hooks policies. Rescued elephants roam freely across forested acreage and bathe naturally in freshwater lagoons. Guests participate in educational feeding, preparing herbal nutrition balls, and observing natural pachyderm behaviors without exploitation or forced performance."
    ),
    (
        "What is the dress code for visiting Phuket's temples, viewpoints, and Big Buddha?",
        "Wat Chalong, the Big Buddha atop Nakkerd Hill, and Chinese Taoist shrines are active religious sites. Visitors are required to dress respectfully: shoulders, chests, and knees must be covered. Sleeveless tank tops, plunge necklines, crop tops, and short shorts are strictly prohibited. Free sarongs and wraps are available at the entrance gates if you need to cover up. Modest, lightweight cotton clothing and slip-on shoes (which can be easily removed when entering temple halls) are recommended."
    ),
    (
        "Are national park fees included in the tour price for Phi Phi and Similan Islands?",
        "Under Thai Department of National Parks regulations, marine park conservation fees are assessed directly by government officers at marina departure piers or island ranger stations. For the Similan Islands tour, national park fees are included in the all-inclusive package price. For Phi Phi and Phang Nga Bay speedboat tours, national park fees (typically THB 400 per adult and THB 200 per child) are either included or collected in cash at registration on the morning of departure as clearly specified on your tour voucher."
    ),
    (
        "How does the booking and enquiry process work with Trippovention for Phuket tours?",
        "Trippovention operates on a dedicated enquiry-led, offline personal booking model. Simply click 'Enquire Now' or 'Request Custom Quote' on any product card, or message our destination specialists via WhatsApp at +66 94 693 4392. Our team confirms real-time availability, verifies hotel pickup schedules, applies multi-tour package savings, and provides an official digital itinerary voucher with full operational support."
    ),
    (
        "What is your weather and cancellation policy for open-sea boat excursions?",
        "Guest safety is our highest operational priority. If Thai Marine Department authorities issue small-boat sea advisories or stormy sea conditions prevent safe navigation, boat tours are promptly rescheduled to a calmer day or rerouted to sheltered inland bays. If rescheduling is not possible during your holiday dates, all payments for weather-cancelled tours are refunded in full. We recommend scheduling open-sea island tours during the first half of your Phuket stay for maximum flexibility."
    )
]

def generate_catalogue_html():
    cards_html = ""
    item_list_elements = []

    for idx, exp in enumerate(EXPERIENCES, start=1):
        highlights_li = "\n".join([f"                        <li>{hl}</li>" for hl in exp["highlights"]])
        card = f"""            <!-- Product Card {idx}: {exp['name']} -->
            <div
              class="card product-card"
              data-id="{exp['id']}"
              data-name="{exp['name'].lower()}"
              data-category="{exp['category']}"
              data-collections="{exp['collections']}"
              data-duration="{exp['duration']}"
              data-duration-hours="{exp['duration_hours']}"
              data-tour-type="{exp['tour_type']}"
              data-styles="{exp['styles']}"
              data-price="{exp['price']}"
            >
              <div class="card-image-wrap">
                <img
                  src="{exp['img']}"
                  alt="{exp['alt']}"
                  width="800"
                  height="450"
                  loading="lazy"
                />
                <span class="card-ribbon">{exp['ribbon']}</span>
                <span class="card-badge">{exp['category_label']}</span>
              </div>
              <div class="body">
                <h3>{exp['name']}</h3>
                <div class="card-meta">
                  <span>{exp['duration_label']}</span>
                  <span>•</span>
                  <span>{exp['tour_type_label']}</span>
                </div>
                <div class="price-row">
                  <div>
                    <span class="price-from">From</span>
                    <span class="price">{exp['price_display']}</span>
                  </div>
                  <span class="price-unit">{exp['price_unit']}</span>
                </div>
                <ul class="highlights-list">
{highlights_li}
                </ul>
                <div class="card-actions">
                  <a href="{exp['link']}" class="btn btn-outline">View Details</a>
                  <a
                    href="../../../contact.html?destination=phuket&tour={exp['enquiry_param']}"
                    class="btn btn-primary"
                    >Enquire Now →</a
                  >
                </div>
              </div>
            </div>"""
        cards_html += card + "\n\n"

        item_list_elements.append(f"""          {{
            "@type": "ListItem",
            "position": {idx},
            "name": "{exp['name']}",
            "url": "https://trippovention.co.th/packages/thailand/phuket/{exp['link']}"
          }}""")

    item_list_json = ",\n".join(item_list_elements)

    faqs_html = ""
    faq_schema_elements = []
    for q, a in FAQS_DATA:
        faqs_html += f"""            <div class="faq-item">
              <button class="faq-question" aria-expanded="false">
                <span>{q}</span>
                <span class="faq-icon" aria-hidden="true">+</span>
              </button>
              <div class="faq-answer">
                <p>{a}</p>
              </div>
            </div>\n"""
        
        q_clean = q.replace('"', '\\"')
        a_clean = a.replace('"', '\\"')
        faq_schema_elements.append(f"""          {{
            "@type": "Question",
            "name": "{q_clean}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{a_clean}"
            }}
          }}""")
    
    faq_schema_json = ",\n".join(faq_schema_elements)

    html = f"""<!doctype html>
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
    <title>Phuket Sightseeing Tours & Activities | Trippovention Thailand</title>
    <meta
      name="description"
      content="Explore the comprehensive Phuket sightseeing catalogue. Discover verified island-hopping speedboat tours to Phi Phi & James Bond Island, cultural viewpoints, ethical elephant sanctuaries, world-class evening shows, water parks, and outdoor adventures with Trippovention Thailand."
    />
    <meta name="author" content="Trippovention" />

    <!-- Open Graph / Social Sharing -->
    <meta property="og:type" content="website" />
    <meta
      property="og:url"
      content="https://trippovention.co.th/packages/thailand/phuket/sightseeing.html"
    />
    <meta
      property="og:title"
      content="Phuket Sightseeing Tours & Activities | Trippovention Thailand"
    />
    <meta
      property="og:description"
      content="Discover Phuket's top sightseeing activities, island-hopping tours to Phi Phi & James Bond, cultural landmarks, night shows, water parks, and private excursions."
    />
    <meta
      property="og:image"
      content="https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_city_highlights.webp"
    />

    <!-- Twitter Card -->
    <meta property="twitter:card" content="summary_large_image" />
    <meta
      property="twitter:url"
      content="https://trippovention.co.th/packages/thailand/phuket/sightseeing.html"
    />
    <meta
      property="twitter:title"
      content="Phuket Sightseeing Tours & Activities | Trippovention Thailand"
    />
    <meta
      property="twitter:description"
      content="Discover Phuket's top sightseeing activities, island-hopping tours to Phi Phi & James Bond, cultural landmarks, night shows, water parks, and private excursions."
    />
    <meta
      property="twitter:image"
      content="https://trippovention.co.th/assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_city_highlights.webp"
    />

    <link
      rel="canonical"
      href="https://trippovention.co.th/packages/thailand/phuket/sightseeing.html"
    />
    <link rel="icon" type="image/x-icon" href="../../../assets/images/favicon.ico" />
    <link rel="apple-touch-icon" sizes="180x180" href="../../../assets/images/favicon.png" />
    <link rel="manifest" href="../../../site.webmanifest" />
    <meta name="theme-color" content="#667eea" />
    <meta name="referrer" content="strict-origin-when-cross-origin" />

    <!-- Stylesheets -->
    <link rel="stylesheet" href="../../../assets/styles.css" />
    <link rel="stylesheet" href="../../../assets/search.css" />

    <!-- Google Fonts & Preload -->
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

    <!-- Google Tag Manager Configuration -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-11395302765"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {{
        dataLayer.push(arguments);
      }}
      gtag("js", new Date());
      gtag("config", "AW-11395302765");
    </script>

    <!-- Structured Data: TouristDestination -->
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "TouristDestination",
        "name": "Phuket Sightseeing Tours & Activities",
        "description": "Explore the comprehensive Phuket sightseeing catalogue. Discover verified island-hopping speedboat tours to Phi Phi and James Bond Island, cultural viewpoints, ethical elephant sanctuaries, world-class evening shows, water parks, and outdoor adventures with Trippovention Thailand.",
        "url": "https://trippovention.co.th/packages/thailand/phuket/sightseeing.html",
        "touristType": [
          "Beach Lovers",
          "Culture Seekers",
          "Families",
          "Adventure Travelers",
          "Couples",
          "Group Travelers"
        ],
        "provider": {{
          "@type": "TravelAgency",
          "name": "Trippovention",
          "url": "https://trippovention.co.th"
        }}
      }}
    </script>

    <!-- Structured Data: BreadcrumbList -->
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
          }}
        ]
      }}
    </script>

    <!-- Structured Data: ItemList (Catalogue Product Inventory) -->
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Phuket Sightseeing Catalogue Products",
        "numberOfItems": {len(EXPERIENCES)},
        "itemListElement": [
{item_list_json}
        ]
      }}
    </script>

    <!-- Structured Data: FAQPage (AEO Optimization) -->
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
{faq_schema_json}
        ]
      }}
    </script>
  </head>

  <body>
    <!-- Skip Link -->
    <a href="#main" class="skip-link" aria-label="Skip to main content" id="skip-link">
      Skip to main content
    </a>

    <!-- Navigation Header -->
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
      <!-- Breadcrumb Navigation -->
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
            <li class="breadcrumb-item active" aria-current="page">
              Sightseeing
            </li>
          </ol>
        </div>
      </nav>

      <!-- Hero Header Section -->
      <header class="hero compact hero-thailand">
        <div class="container">
          <h1>Phuket Sightseeing &amp; Activities</h1>
          <p>
            Curated island tours, cultural viewpoints, shows, water parks &amp; experiences across Phuket and the Andaman Sea
          </p>
        </div>
      </header>

      <!-- Catalogue Introduction -->
      <section class="section" style="padding-bottom: 20px;">
        <div class="container">
          <div class="section-title">
            <h2>Discover the Best of Phuket</h2>
            <p class="subtitle">
              From world-renowned limestone islands to sacred temples and vibrant nighttime revues
            </p>
          </div>
          <div class="card" style="padding: 28px; line-height: 1.8; font-size: 16px;">
            <p style="margin-bottom: 16px;">
              Welcome to the official <strong>Phuket Sightseeing &amp; Activities Catalogue</strong> by Trippovention Thailand. As Thailand's premier tropical island, Phuket serves as the gateway to world-class marine national parks, turquoise coral lagoons, sacred hilltop shrines, and vibrant Sino-Portuguese cultural quarters.
            </p>
            <p style="margin-bottom: 0;">
              Every tour and excursion featured in this catalogue has been verified by our local operations team for safety, reliable hotel transfers, and exceptional quality. As an enquiry-led travel company, Trippovention provides personalized advice, multi-tour discounts, and dedicated offline booking support without online booking fees or rigid group constraints.
            </p>
          </div>
        </div>
      </section>

      <!-- Curated Collections Center-Aligned Pill Cards -->
      <section class="section alt" style="padding-top: 30px; padding-bottom: 30px;">
        <div class="container">
          <div class="section-title" style="margin-bottom: 24px;">
            <h2>Curated Collections</h2>
            <p class="subtitle">Quickly jump to Phuket's signature sightseeing themes</p>
          </div>
          <div class="collections-carousel" id="collectionsCarousel">
            <button class="collection-pill-card active" data-collection="all" type="button">
              <span class="icon">✨</span>
              <span class="name">All Experiences</span>
              <span class="count">24 Tours</span>
            </button>
            <button class="collection-pill-card" data-collection="island-tours" type="button">
              <span class="icon">🏝️</span>
              <span class="name">Island Hopping &amp; Boats</span>
              <span class="count">8 Tours</span>
            </button>
            <button class="collection-pill-card" data-collection="city-culture" type="button">
              <span class="icon">🏛️</span>
              <span class="name">City &amp; Old Town</span>
              <span class="count">4 Tours</span>
            </button>
            <button class="collection-pill-card" data-collection="shows-entertainment" type="button">
              <span class="icon">🎭</span>
              <span class="name">Night Shows &amp; Theatre</span>
              <span class="count">4 Shows</span>
            </button>
            <button class="collection-pill-card" data-collection="adventure-outdoor" type="button">
              <span class="icon">⚡</span>
              <span class="name">Ziplines &amp; Outdoor</span>
              <span class="count">3 Adventures</span>
            </button>
            <button class="collection-pill-card" data-collection="nature-wildlife" type="button">
              <span class="icon">🐘</span>
              <span class="name">Ethical Wildlife</span>
              <span class="count">2 Excursions</span>
            </button>
            <button class="collection-pill-card" data-collection="waterparks-family" type="button">
              <span class="icon">🌊</span>
              <span class="name">Water Parks &amp; Family</span>
              <span class="count">2 Parks</span>
            </button>
            <button class="collection-pill-card" data-collection="food-wellness" type="button">
              <span class="icon">🍲</span>
              <span class="name">Thai Cooking &amp; Spa</span>
              <span class="count">2 Experiences</span>
            </button>
          </div>
        </div>
      </section>

      <!-- Search, Filter & Catalogue Section -->
      <section class="section" id="catalogueSection">
        <div class="container">
          <!-- Interactive Filter Toolbar -->
          <div class="catalogue-toolbar card" style="padding: 20px; margin-bottom: 30px;">
            <!-- Primary Search Row -->
            <div class="toolbar-primary-row">
              <div class="search-input-wrap">
                <span class="search-icon-symbol" aria-hidden="true">🔍</span>
                <input
                  type="text"
                  id="phuketSearchInput"
                  class="catalogue-search-input"
                  placeholder="Search Phuket activities by name, landmark or keyword (e.g. Phi Phi, James Bond, Big Buddha)..."
                  aria-label="Search Phuket activities"
                />
                <button
                  type="button"
                  id="searchClearBtn"
                  class="search-clear-btn"
                  title="Clear search"
                  aria-label="Clear search query"
                  style="display: none;"
                >
                  ✕
                </button>
              </div>
              <button
                type="button"
                id="mobileFilterToggle"
                class="mobile-filter-toggle-btn"
                aria-expanded="false"
              >
                <span>⚙️ Filters</span>
              </button>
            </div>

            <!-- Category Pills Row -->
            <div class="category-pills-row" id="categoryPillsRow">
              <button class="cat-pill active" data-category="all" type="button">
                All (24)
              </button>
              <button class="cat-pill" data-category="island-tours" type="button">
                Island Tours (8)
              </button>
              <button class="cat-pill" data-category="city-culture" type="button">
                City &amp; Culture (4)
              </button>
              <button class="cat-pill" data-category="shows-entertainment" type="button">
                Shows &amp; Theatre (4)
              </button>
              <button class="cat-pill" data-category="adventure-outdoor" type="button">
                Adventure &amp; Outdoor (3)
              </button>
              <button class="cat-pill" data-category="nature-wildlife" type="button">
                Wildlife &amp; Nature (2)
              </button>
              <button class="cat-pill" data-category="waterparks-family" type="button">
                Family &amp; Parks (2)
              </button>
              <button class="cat-pill" data-category="food-wellness" type="button">
                Cooking &amp; Spa (2)
              </button>
            </div>

            <!-- Secondary Filters Bar -->
            <div class="toolbar-secondary-bar" id="secondaryFiltersBar">
              <div class="filter-select-group">
                <label for="durationSelect">Duration:</label>
                <select id="durationSelect" class="filter-select">
                  <option value="all">All Durations</option>
                  <option value="half-day">Half Day (&le; 4 Hours)</option>
                  <option value="full-day">Full Day (5+ Hours)</option>
                  <option value="evening">Evening / Shows</option>
                </select>
              </div>

              <div class="filter-select-group">
                <label for="tourTypeSelect">Format:</label>
                <select id="tourTypeSelect" class="filter-select">
                  <option value="all">All Formats</option>
                  <option value="speedboat">Speedboat Excursions</option>
                  <option value="guided">Guided Tours</option>
                  <option value="show">Theatrical Shows</option>
                  <option value="adventure">Adventures &amp; Outdoor</option>
                  <option value="attraction">Attractions &amp; Passes</option>
                  <option value="private">Private VIP Hire</option>
                </select>
              </div>

              <div class="filter-select-group">
                <label for="styleSelect">Style:</label>
                <select id="styleSelect" class="filter-select">
                  <option value="all">All Styles</option>
                  <option value="beach">Island &amp; Beach</option>
                  <option value="culture">Culture &amp; Temples</option>
                  <option value="adventure">Action &amp; Adventure</option>
                  <option value="family">Family Friendly</option>
                  <option value="luxury">Luxury &amp; Relaxing</option>
                </select>
              </div>

              <div class="filter-select-group">
                <label for="sortSelect">Sort By:</label>
                <select id="sortSelect" class="filter-select">
                  <option value="recommended">Recommended</option>
                  <option value="price-asc">Price: Low to High</option>
                  <option value="price-desc">Price: High to Low</option>
                  <option value="duration-asc">Duration: Shortest</option>
                  <option value="name-asc">Alphabetical (A–Z)</option>
                </select>
              </div>

              <button type="button" id="resetFiltersBtn" class="btn btn-sm ghost" style="align-self: flex-end;">
                ↺ Reset All
              </button>
            </div>

            <!-- Active Filter Status & Match Counter -->
            <div class="filter-status-row" id="filterStatusRow">
              <span id="resultsCount">Showing 24 of 24 experiences</span>
            </div>
          </div>

          <!-- Product Cards Grid -->
          <div class="grid cols-3" id="catalogueGrid">
{cards_html}
          </div>

          <!-- Empty State (Hidden by Default) -->
          <div id="noResultsState" class="card text-center" style="display: none; padding: 48px 24px; margin-top: 20px;">
            <div style="font-size: 48px; margin-bottom: 16px;">🔍</div>
            <h3>No matching Phuket activities found</h3>
            <p class="muted" style="max-width: 500px; margin: 0 auto 20px auto;">
              We couldn't find any activities matching your selected filters or search terms. Try clearing filters or searching for terms like "Phi Phi", "James Bond", "Old Town", or "Water Park".
            </p>
            <button type="button" id="resetEmptyBtn" class="btn btn-primary">
              ↺ Reset All Filters &amp; View All 24 Experiences
            </button>
          </div>
        </div>
      </section>

      <!-- FAQ Section (AEO & Customer Knowledge) -->
      <section class="section alt faq-section" id="faq">
        <div class="container">
          <div class="section-title">
            <h2>Frequently Asked Questions</h2>
            <p class="subtitle">Essential advice for booking and enjoying Phuket tours and activities</p>
          </div>
          <div class="faq-container">
{faqs_html}
          </div>
        </div>
      </section>

      <!-- Call to Action Banner -->
      <section class="section cta">
        <div class="container">
          <div class="section-title">
            <h2 class="text-white">Plan Your Custom Phuket Sightseeing Itinerary</h2>
            <p class="subtitle text-white-90">
              Connect with our local destination team for current offers, group discounts, and private arrangements.
            </p>
          </div>
          <div class="text-center">
            <a
              class="btn btn-lg ghost"
              href="../../../contact.html?destination=phuket&type=sightseeing"
              >📞 Request Custom Quote</a
            >
            <a
              class="btn btn-lg ghost ml-16"
              href="https://wa.me/66946934392?text=Hello,%20I%20would%20like%20to%20enquire%20about%20Phuket%20sightseeing%20tours"
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

    <!-- Footer -->
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
                  >WhatsApp: +66 94 693 4392</a
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
              <a href="../../../contact.html">Contact</a><br />
              <a href="../../../terms-and-conditions.html">Terms &amp; Conditions</a><br />
              <a href="../../../privacy-policy.html">Privacy Policy</a><br />
              <a href="../../../refund-policy.html">Refund Policy</a>
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
                  href="https://www.facebook.com/profile.php?id=61590071764774"
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
                  href="https://www.instagram.com/trippoventioncoltd/"
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
                  href="https://www.youtube.com/@TrippoventionCoLtd"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Follow us on YouTube"
                  title="YouTube"
                >
                  <img
                    src="../../../assets/images/social/youtube.svg"
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
        <div class="text-center section-border-top mt-40 pt-30">
          <p>© 2026 Trippovention. All Rights Reserved.</p>
        </div>
      </div>
    </footer>

    <!-- Scripts -->
    <script src="../../../assets/app.js" defer></script>
    <script src="../../../assets/search.js" defer></script>

    <!-- Client-Side Vanilla JS Interactive Search & Filter Engine -->
    <script>
      document.addEventListener("DOMContentLoaded", function () {{
        const searchInput = document.getElementById("phuketSearchInput");
        const clearBtn = document.getElementById("searchClearBtn");
        const categoryPills = document.querySelectorAll(".cat-pill");
        const collectionCards = document.querySelectorAll(".collection-pill-card");
        const durationSelect = document.getElementById("durationSelect");
        const tourTypeSelect = document.getElementById("tourTypeSelect");
        const styleSelect = document.getElementById("styleSelect");
        const sortSelect = document.getElementById("sortSelect");
        const resetBtn = document.getElementById("resetFiltersBtn");
        const resetEmptyBtn = document.getElementById("resetEmptyBtn");
        const resultsCountEl = document.getElementById("resultsCount");
        const grid = document.getElementById("catalogueGrid");
        const noResultsState = document.getElementById("noResultsState");
        const mobileToggleBtn = document.getElementById("mobileFilterToggle");
        const secondaryBar = document.getElementById("secondaryFiltersBar");

        let allCards = Array.from(grid.querySelectorAll(".product-card"));
        const totalCount = allCards.length;

        let activeCategory = "all";
        let activeCollection = "all";

        function filterCards() {{
          const query = searchInput.value.trim().toLowerCase();
          const selectedDuration = durationSelect.value;
          const selectedTourType = tourTypeSelect.value;
          const selectedStyle = styleSelect.value;
          const selectedSort = sortSelect.value;

          // Toggle clear search button
          if (query.length > 0) {{
            clearBtn.style.display = "block";
          }} else {{
            clearBtn.style.display = "none";
          }}

          let visibleCards = [];

          allCards.forEach((card) => {{
            const cardName = card.getAttribute("data-name") || "";
            const cardCat = card.getAttribute("data-category") || "";
            const cardCollections = (card.getAttribute("data-collections") || "").split(",");
            const cardDuration = card.getAttribute("data-duration") || "";
            const cardTourType = card.getAttribute("data-tour-type") || "";
            const cardStyles = (card.getAttribute("data-styles") || "").split(",");
            const cardText = card.innerText.toLowerCase();

            let matchesSearch = true;
            if (query) {{
              matchesSearch = cardName.includes(query) || cardText.includes(query);
            }}

            let matchesCategory = true;
            if (activeCategory !== "all") {{
              matchesCategory = cardCat === activeCategory;
            }}

            let matchesCollection = true;
            if (activeCollection !== "all") {{
              matchesCollection = cardCollections.includes(activeCollection);
            }}

            let matchesDuration = true;
            if (selectedDuration !== "all") {{
              matchesDuration = cardDuration === selectedDuration;
            }}

            let matchesTourType = true;
            if (selectedTourType !== "all") {{
              matchesTourType = cardTourType === selectedTourType;
            }}

            let matchesStyle = true;
            if (selectedStyle !== "all") {{
              matchesStyle = cardStyles.includes(selectedStyle);
            }}

            if (
              matchesSearch &&
              matchesCategory &&
              matchesCollection &&
              matchesDuration &&
              matchesTourType &&
              matchesStyle
            ) {{
              card.style.display = "flex";
              visibleCards.push(card);
            }} else {{
              card.style.display = "none";
            }}
          }});

          // Sorting
          if (selectedSort !== "recommended") {{
            visibleCards.sort((a, b) => {{
              const priceA = parseFloat(a.getAttribute("data-price")) || 0;
              const priceB = parseFloat(b.getAttribute("data-price")) || 0;
              const durA = parseFloat(a.getAttribute("data-duration-hours")) || 0;
              const durB = parseFloat(b.getAttribute("data-duration-hours")) || 0;
              const nameA = a.querySelector("h3").innerText.trim();
              const nameB = b.querySelector("h3").innerText.trim();

              if (selectedSort === "price-asc") return priceA - priceB;
              if (selectedSort === "price-desc") return priceB - priceA;
              if (selectedSort === "duration-asc") return durA - durB;
              if (selectedSort === "name-asc") return nameA.localeCompare(nameB);
              return 0;
            }});

            visibleCards.forEach((c) => grid.appendChild(c));
          }}

          // Update Counter & Empty State
          resultsCountEl.innerText = `Showing ${{visibleCards.length}} of ${{totalCount}} experiences`;

          if (visibleCards.length === 0) {{
            noResultsState.style.display = "block";
            grid.style.display = "none";
          }} else {{
            noResultsState.style.display = "none";
            grid.style.display = "grid";
          }}
        }}

        // Listeners
        searchInput.addEventListener("input", filterCards);

        clearBtn.addEventListener("click", () => {{
          searchInput.value = "";
          clearBtn.style.display = "none";
          filterCards();
          searchInput.focus();
        }});

        categoryPills.forEach((pill) => {{
          pill.addEventListener("click", () => {{
            categoryPills.forEach((p) => p.classList.remove("active"));
            pill.classList.add("active");
            activeCategory = pill.getAttribute("data-category");
            // reset collection card active styling if category clicked
            collectionCards.forEach((c) => c.classList.remove("active"));
            const matchCol = Array.from(collectionCards).find((c) => c.getAttribute("data-collection") === activeCategory);
            if (matchCol) matchCol.classList.add("active");
            activeCollection = "all";
            filterCards();
          }});
        }});

        collectionCards.forEach((card) => {{
          card.addEventListener("click", () => {{
            collectionCards.forEach((c) => c.classList.remove("active"));
            card.classList.add("active");
            const target = card.getAttribute("data-collection");
            activeCollection = target;

            // synchronize category pill if direct match exists
            categoryPills.forEach((p) => p.classList.remove("active"));
            const matchPill = Array.from(categoryPills).find((p) => p.getAttribute("data-category") === target);
            if (matchPill) {{
              matchPill.classList.add("active");
              activeCategory = target;
              activeCollection = "all";
            }} else {{
              const allPill = Array.from(categoryPills).find((p) => p.getAttribute("data-category") === "all");
              if (allPill) allPill.classList.add("active");
              activeCategory = "all";
            }}

            filterCards();
            document.getElementById("catalogueSection").scrollIntoView({{ behavior: "smooth" }});
          }});
        }});

        durationSelect.addEventListener("change", filterCards);
        tourTypeSelect.addEventListener("change", filterCards);
        styleSelect.addEventListener("change", filterCards);
        sortSelect.addEventListener("change", filterCards);

        function resetAll() {{
          searchInput.value = "";
          durationSelect.value = "all";
          tourTypeSelect.value = "all";
          styleSelect.value = "all";
          sortSelect.value = "recommended";
          activeCategory = "all";
          activeCollection = "all";

          categoryPills.forEach((p) => p.classList.remove("active"));
          const firstPill = Array.from(categoryPills).find((p) => p.getAttribute("data-category") === "all");
          if (firstPill) firstPill.classList.add("active");

          collectionCards.forEach((c) => c.classList.remove("active"));
          const firstCol = Array.from(collectionCards).find((c) => c.getAttribute("data-collection") === "all");
          if (firstCol) firstCol.classList.add("active");

          filterCards();
        }}

        resetBtn.addEventListener("click", resetAll);
        resetEmptyBtn.addEventListener("click", resetAll);

        if (mobileToggleBtn) {{
          mobileToggleBtn.addEventListener("click", () => {{
            const isOpen = secondaryBar.classList.toggle("open");
            mobileToggleBtn.setAttribute("aria-expanded", isOpen);
          }});
        }}
      }});
    </script>
  </body>
</html>
"""
    return html

def main():
    html_content = generate_catalogue_html()
    with open(CATALOGUE_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully generated Phuket Sightseeing Catalogue at: {CATALOGUE_PATH}")
    print(f"Total experiences included: {len(EXPERIENCES)}")
    print(f"Total FAQs included: {len(FAQS_DATA)}")

if __name__ == "__main__":
    main()
