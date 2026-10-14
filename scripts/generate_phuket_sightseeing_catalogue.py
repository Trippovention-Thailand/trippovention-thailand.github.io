#!/usr/bin/env python3
"""
Generate the Standardized Phuket Sightseeing Catalogue Page:
docs/packages/thailand/phuket/sightseeing.html
Modeled directly on docs/packages/thailand/krabi/sightseeing.html, Bangkok, and Pattaya catalogues.
Follows standardized architecture:
- .catalogue-hero
- .collections-grid with center-aligned collection-pill-card
- .filter-toolbar with .search-box-row, .category-pills-wrap, .secondary-filters-bar
- Standardized card tiles with clean presentation (no highlights lists)
- 23 verified Phuket experiences (Phuket Luxury Thai Spa removed)
- 10 comprehensive FAQs with <details>/<summary> accordion & Schema.org FAQPage
- Standard 3-column footer with official contact details
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
        "price": "2200",
        "price_display": "THB 2,200",
        "price_unit": "Price Per Person",
        "highlights": [
            "Iconic Maya Bay national park beach framed by 100m karst limestone cliffs",
            "Emerald swimming and cliff jumping in enclosed Pileh Lagoon",
            "Snorkel colorful coral reefs with blacktip reef sharks at Bamboo Island",
            "Buffet lunch on beachfront Phi Phi Don and sightseeing at Viking Cave"
        ],
        "enquiry_param": "Phi+Phi+and+Bamboo+Island+Tour"
    },
    {
        "id": "hkt-03",
        "name": "James Bond Island & Phang Nga Bay Sea Canoe Tour",
        "link": "james_bond_island_speedboat_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_james_bond_island_speedboat_tour.webp",
        "alt": "James Bond Island Koh Tapu and sea canoeing in Phang Nga Bay",
        "ribbon": "🎬 Iconic Movie Site",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "full-day",
        "duration_hours": "8",
        "duration_label": "⏱️ Full Day (8 Hrs)",
        "tour_type": "speedboat",
        "tour_type_label": "Speedboat & Sea Canoe",
        "styles": "nature,adventure",
        "price": "2100",
        "price_display": "THB 2,100",
        "price_unit": "Price Per Person",
        "highlights": [
            "Photograph Koh Tapu limestone nail from 'The Man with the Golden Gun'",
            "Paddled sea canoe exploration through subterranean caves at Koh Panak",
            "Explore hidden mangrove hongs and tidal limestone chambers at Hong Island",
            "Buffet lunch at the historic Muslim stilted sea gypsy village of Koh Panyee"
        ],
        "enquiry_param": "James+Bond+Island+Tour"
    },
    {
        "id": "hkt-04",
        "name": "Phuket FantaSea Cultural Theme Park & Show",
        "link": "phuket_fantasea_show.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_fantasea_show_with_dinner.webp",
        "alt": "Phuket FantaSea Palace of the Elephants cultural show in Kamala",
        "ribbon": "🐘 Grand Cultural Revue",
        "category": "shows-entertainment",
        "category_label": "Shows & Theatre",
        "collections": "shows-entertainment",
        "duration": "evening",
        "duration_hours": "4",
        "duration_label": "⏱️ Evening (4–5 Hrs)",
        "tour_type": "show",
        "tour_type_label": "Theme Park & Live Show",
        "styles": "culture,family",
        "price": "1800",
        "price_display": "THB 1,800",
        "price_unit": "Price Per Person",
        "highlights": [
            "Spectacular 'Fantasy of a Kingdom' theatrical show in 3,000-seat theatre",
            "Thai culture, aerial acrobatics, illusion magic, pyrotechnics and 30+ elephants",
            "Golden Kinnaree 4,000-seat royal banquet hall international buffet dinner",
            "Carnival Village shopping street with traditional crafts, games, and photo ops"
        ],
        "enquiry_param": "Phuket+FantaSea+Show"
    },
    {
        "id": "hkt-05",
        "name": "Carnival Magic Phuket Nighttime Theme Park",
        "link": "carnival_magic_show.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_carnival_magic_show_with_dinner.webp",
        "alt": "Carnival Magic Phuket Kingdom of Lights illuminated theme park",
        "ribbon": "✨ 9 Guinness Records",
        "category": "shows-entertainment",
        "category_label": "Shows & Theatre",
        "collections": "shows-entertainment",
        "duration": "evening",
        "duration_hours": "4.5",
        "duration_label": "⏱️ Evening (4–5 Hrs)",
        "tour_type": "show",
        "tour_type_label": "Light Park & Parade",
        "styles": "family,culture",
        "price": "2100",
        "price_display": "THB 2,100",
        "price_unit": "Price Per Person",
        "highlights": [
            "World's highest concentration of illumination with over 40 million LED lights",
            "River Carnival indoor parade show with colossal floats in 2,200-seat stadium",
            "Kingdom of Lights illuminated walking wonderland spanning 40 manicured acres",
            "Bird of Paradise 3,000-seat royal buffet restaurant with 100+ global delicacies"
        ],
        "enquiry_param": "Carnival+Magic+Phuket"
    },
    {
        "id": "hkt-06",
        "name": "Simon Cabaret Show Phuket",
        "link": "simon_cabaret_show_phuket.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_simon_cabaret_show.webp",
        "alt": "Simon Cabaret Phuket glamorous theatrical performance in Patong",
        "ribbon": "💃 Leading Cabaret",
        "category": "shows-entertainment",
        "category_label": "Shows & Theatre",
        "collections": "shows-entertainment",
        "duration": "evening",
        "duration_hours": "1.5",
        "duration_label": "⏱️ 75 Minutes (Evening)",
        "tour_type": "show",
        "tour_type_label": "Theatrical Revue",
        "styles": "culture,family",
        "price": "900",
        "price_display": "THB 900",
        "price_unit": "Price Per Person",
        "highlights": [
            "Phuket's legendary transvestite theatrical performance operating since 1991",
            "Glitz, glamour, Broadway numbers, international pop, and traditional Asian sets",
            "Elaborate handcrafted feather costumes, crystal gowns, and state-of-the-art acoustics",
            "Centrally located in Patong Beach with convenient multiple nightly showtimes"
        ],
        "enquiry_param": "Simon+Cabaret+Show+Phuket"
    },
    {
        "id": "hkt-07",
        "name": "Hanuman World Zipline & Roller Adventure",
        "link": "hanuman_world_zipline_and_atv_adventure.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_hanuman_world_zipline.webp",
        "alt": "Hanuman World Phuket rainforest canopy zipline and roller coaster",
        "ribbon": "⚡ Eco Adrenaline",
        "category": "adventure-outdoor",
        "category_label": "Adventure & Outdoor",
        "collections": "adventure-outdoor",
        "duration": "half-day",
        "duration_hours": "3.5",
        "duration_label": "⏱️ Half Day (3–4 Hrs)",
        "tour_type": "adventure",
        "tour_type_label": "Jungle Zipline Adventure",
        "styles": "adventure,family",
        "price": "1900",
        "price_display": "THB 1,900",
        "price_unit": "Price Per Person",
        "highlights": [
            "Soar through pristine rainforest canopy across 30 thrilling tree-high platforms",
            "Fly on Thailand's longest 400m high-speed zipline above ancient tree crowns",
            "800m high-gravity Roller Zipline coaster spiraling through dense jungle foliage",
            "Tree-top Skywalk bridge walkway and authentic Southern Thai buffet lunch"
        ],
        "enquiry_param": "Hanuman+World+Zipline+Adventure"
    },
    {
        "id": "hkt-08",
        "name": "Coral Island (Koh Hey) & Racha Island Speedboat Tour",
        "link": "coral_and_racha_island_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_coral_and_racha_island.webp",
        "alt": "Coral Island Banana Beach and Racha Island turquoise snorkeling from Phuket",
        "ribbon": "🤿 Snorkel Paradise",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "full-day",
        "duration_hours": "7.5",
        "duration_label": "⏱️ Full Day (7–8 Hrs)",
        "tour_type": "speedboat",
        "tour_type_label": "Island Speedboat Excursion",
        "styles": "beach,family",
        "price": "1650",
        "price_display": "THB 1,650",
        "price_unit": "Price Per Person",
        "highlights": [
            "Quick 15-minute crossing to Coral Island's powdery white sand Banana Beach",
            "Optional watersports: parasailing, banana boat, and clear-bottom sea kayaking",
            "Cruise to Racha Yai Island for world-class snorkeling in crystal-clear Batok Bay",
            "Encounter tropical parrotfish, damselfish, and vibrant living brain corals"
        ],
        "enquiry_param": "Coral+and+Racha+Island+Tour"
    },
    {
        "id": "hkt-09",
        "name": "Ethical Elephant Care & Sanctuary Program Phuket",
        "link": "elephant_sanctuary.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_elephant_sanctuary.webp",
        "alt": "Ethical elephant feeding and mud spa sanctuary experience Phuket",
        "ribbon": "❤️ 100% Ethical",
        "category": "wildlife-family",
        "category_label": "Wildlife & Nature",
        "collections": "wildlife-family",
        "duration": "half-day",
        "duration_hours": "4",
        "duration_label": "⏱️ Half Day (4 Hrs)",
        "tour_type": "guided",
        "tour_type_label": "Ethical Wildlife Program",
        "styles": "family,nature",
        "price": "2400",
        "price_display": "THB 2,400",
        "price_unit": "Price Per Person",
        "highlights": [
            "Strict no-riding, no-chains sanctuary for rescued working elephants",
            "Prepare fresh nutritional fruit baskets and medicinal herbal dietary balls",
            "Observe gentle giants foraging freely and bathing in natural forest lagoons",
            "Learn elephant social behaviors and conservation science from expert carers"
        ],
        "enquiry_param": "Phuket+Elephant+Sanctuary+Program"
    },
    {
        "id": "hkt-10",
        "name": "Phuket Sunset Dinner Cruise by Catamaran",
        "link": "phuket_sunset_catamaran_cruise.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_sunset_catamaran_cruise.webp",
        "alt": "Luxury sailing catamaran sunset dinner cruise Promthep Cape Phuket",
        "ribbon": "🥂 Sunset Romance",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "evening",
        "duration_hours": "5",
        "duration_label": "⏱️ Afternoon / Sunset (5 Hrs)",
        "tour_type": "speedboat",
        "tour_type_label": "Luxury Sailing Cruise",
        "styles": "luxury,beach",
        "price": "2350",
        "price_display": "THB 2,350",
        "price_unit": "Price Per Person",
        "highlights": [
            "Sail aboard a spacious modern catamaran yacht with sunbeds & shaded saloon",
            "Snorkel off scenic Coral Island and spot wild dolphins near Maiton Island",
            "Anchor beside Promthep Cape and Laem Krating for dramatic Andaman sunset vistas",
            "Fresh Thai barbecue buffet dinner, sashimi, seasonal fruits, and sparkling wine"
        ],
        "enquiry_param": "Phuket+Sunset+Catamaran+Cruise"
    },
    {
        "id": "hkt-11",
        "name": "Similan Islands Day Trip by Speedboat",
        "link": "similan_islands_snorkeling_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_similan_islands_snorkeling.webp",
        "alt": "Similan Islands turquoise sea and Sailing Rock viewpoint",
        "ribbon": "🏝️ National Marine Park",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "full-day",
        "duration_hours": "11",
        "duration_label": "⏱️ Full Day (10–11 Hrs)",
        "tour_type": "speedboat",
        "tour_type_label": "Marine Park Speedboat",
        "styles": "beach,adventure",
        "price": "3100",
        "price_display": "THB 3,100",
        "price_unit": "Price Per Person",
        "highlights": [
            "Open exclusively Oct 15 – May 15: Thailand's #1 protected marine archipelago",
            "Hike up to the iconic balancing Sailing Rock overlook at Koh Similan (Island 8)",
            "Swim among sea turtles, manta rays, and tropical schools at Koh Ba-Ngu (Island 9)",
            "Relax on blinding white coral-powder sand at Donald Duck Bay and Princess Bay"
        ],
        "enquiry_param": "Similan+Islands+Day+Trip"
    },
    {
        "id": "hkt-12",
        "name": "Aquaria Phuket & AR Trickeye Museum Pass",
        "link": "aquaria_phuket_tickets.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_aquaria_phuket.webp",
        "alt": "Aquaria Phuket ocean tunnel and underwater exhibits in Central Phuket",
        "ribbon": "🐠 Largest In Thailand",
        "category": "wildlife-family",
        "category_label": "Family Attractions",
        "collections": "wildlife-family",
        "duration": "half-day",
        "duration_hours": "3",
        "duration_label": "⏱️ 2–3 Hours",
        "tour_type": "attraction",
        "tour_type_label": "Indoor Theme Attraction",
        "styles": "family",
        "price": "890",
        "price_display": "THB 890",
        "price_unit": "Price Per Person",
        "highlights": [
            "Thailand's largest aquarium housing 25,000+ marine animals across 9 themed zones",
            "Walk through panoramic underwater tunnels surrounded by rays and zebra sharks",
            "Daily diver feeding shows, penguin habitat, and otters in Mystic Forest",
            "Includes entry to AR Trick Eye Museum with interactive 3D augmented-reality art"
        ],
        "enquiry_param": "Aquaria+Phuket+Tickets"
    },
    {
        "id": "hkt-13",
        "name": "Phuket Traditional Thai Cooking Class & Market Tour",
        "link": "phuket_thai_cooking_class.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_thai_cooking_class.webp",
        "alt": "Authentic Thai cooking school prep and fresh market tour Phuket",
        "ribbon": "🍲 UNESCO Gastronomy",
        "category": "thai-cooking",
        "category_label": "Food & Cooking",
        "collections": "thai-cooking",
        "duration": "half-day",
        "duration_hours": "4",
        "duration_label": "⏱️ Half Day (4 Hrs)",
        "tour_type": "guided",
        "tour_type_label": "Culinary Workshop",
        "styles": "culture,family",
        "price": "1600",
        "price_display": "THB 1,600",
        "price_unit": "Price Per Person",
        "highlights": [
            "Guided tour of an authentic local morning market to select fresh herbs & spices",
            "Hands-on cooking stations instructed by master chefs in open-air garden kitchen",
            "Cook 4 signature dishes: Tom Yum Goong, Pad Thai, Green Curry & Mango Sticky Rice",
            "Feast on your culinary creations and receive an official recipe certificate"
        ],
        "enquiry_param": "Phuket+Thai+Cooking+Class"
    },
    {
        "id": "hkt-14",
        "name": "Scuba Diving Day Trip (Racha Yai & Noi)",
        "link": "phuket_scuba_diving_day_trip.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_scuba_diving_day_trip.webp",
        "alt": "Scuba diving coral reefs and marine life at Racha Yai from Phuket",
        "ribbon": "🌊 Certified & Beginners",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "full-day",
        "duration_hours": "8",
        "duration_label": "⏱️ Full Day (8 Hrs)",
        "tour_type": "speedboat",
        "tour_type_label": "PADI Dive Boat Trip",
        "styles": "adventure",
        "price": "3400",
        "price_display": "THB 3,400",
        "price_unit": "Price Per Person",
        "highlights": [
            "2 or 3 guided boat dives at Racha Yai & Racha Noi with crystal 25m+ visibility",
            "Discover underwater motorcycle wrecks, artificial reefs, and concrete elephant statues",
            "Encounter moray eels, barracudas, cuttlefish, and gentle sea turtles",
            "Full premium scuba gear, certified divemaster guides & freshly cooked hot buffet lunch"
        ],
        "enquiry_param": "Phuket+Scuba+Diving+Trip"
    },
    {
        "id": "hkt-15",
        "name": "Phi Phi & Khai Islands Speedboat Excursion",
        "link": "phi_phi_island_and_khai_island_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phi_phi_island_and_khai_island_tour_with_lunch_round_trip_transfer.webp",
        "alt": "Speedboat excursion to Phi Phi Don and Khai Nok Island from Phuket",
        "ribbon": "👨‍👩‍👧 Family Favorite",
        "category": "island-tours",
        "category_label": "Island Tours & Marine",
        "collections": "island-tours",
        "duration": "full-day",
        "duration_hours": "8",
        "duration_label": "⏱️ Full Day (8 Hrs)",
        "tour_type": "speedboat",
        "tour_type_label": "Speedboat Excursion",
        "styles": "beach,family",
        "price": "1950",
        "price_display": "THB 1,950",
        "price_unit": "Price Per Person",
        "highlights": [
            "Scenic cruise past Maya Bay, Loh Samah Bay, Viking Cave and Monkey Beach",
            "Open-sea snorkeling stops above vibrant coral gardens in Phi Phi archipelago",
            "Afternoon beach stop at Khai Nok Island with calm shallow waters ideal for kids",
            "Direct beach feeding and swimming right alongside hundreds of sergeant major fish"
        ],
        "enquiry_param": "Phi+Phi+and+Khai+Island+Tour"
    },
    {
        "id": "hkt-16",
        "name": "Phuket Old Town Heritage Cultural Walking Tour",
        "link": "phuket_old_town_heritage_walking_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_phuket_old_town_heritage.webp",
        "alt": "Phuket Old Town Sino-Portuguese architecture shophouses Thalang Road",
        "ribbon": "🏛️ Heritage & Food",
        "category": "city-culture",
        "category_label": "City & Culture",
        "collections": "city-culture",
        "duration": "half-day",
        "duration_hours": "3.5",
        "duration_label": "⏱️ Half Day (3–4 Hrs)",
        "tour_type": "guided",
        "tour_type_label": "Guided Walking Tour",
        "styles": "culture",
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
        "id": "hkt-18",
        "name": "Private Phuket City & Scenic Viewpoints Tour",
        "link": "private_phuket_city_and_viewpoints_tour.html",
        "img": "../../../assets/images/packages/thailand/phuket/sightseeingoptions/hero_private_phuket_city_viewpoints.webp",
        "alt": "Private VIP minivan city tour Promthep Cape and Big Buddha Phuket",
        "ribbon": "⭐ 100% Tailored VIP",
        "category": "city-culture",
        "category_label": "City & Culture",
        "collections": "city-culture",
        "duration": "half-day",
        "duration_hours": "5",
        "duration_label": "⏱️ Flexible (5–6 Hrs)",
        "tour_type": "private",
        "tour_type_label": "Private Minivan Tour",
        "styles": "luxury,culture",
        "price": "3200",
        "price_display": "THB 3,200",
        "price_unit": "Per Vehicle (Up to 9 Pax)",
        "highlights": [
            "Dedicated private VIP minivan with professional English-speaking driver",
            "Fully customisable route: Big Buddha, Wat Chalong, Old Town & Promthep Cape",
            "Travel at your party's personal pace with zero rushed commercial stops",
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
        "collections": "adventure-outdoor",
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
        "category": "wildlife-family",
        "category_label": "Family Attractions",
        "collections": "wildlife-family",
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
        "category_label": "Shows & Theatre",
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
        "category_label": "Adventure & Outdoor",
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
    cards_html_list = []
    item_list_elements = []

    for idx, exp in enumerate(EXPERIENCES, start=1):
        card_html = f"""            <article
              class="card sightseeing-card"
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
              <div class="img-wrap">
                <img
                  src="{exp['img']}"
                  alt="{exp['alt']}"
                  width="400"
                  height="225"
                  loading="lazy"
                />
                <span class="ribbon">{exp['ribbon']}</span>
              </div>
              <div class="body">
                <div class="card-meta-row">
                  <span class="card-tag highlight-tag">{exp['duration_label']}</span>
                  <span class="card-tag">{exp['tour_type_label']}</span>
                  <span class="card-tag">{exp['category_label']}</span>
                </div>
                <h3><a href="{exp['link']}" class="card-title-link">{exp['name']}</a></h3>
                <div class="price-row mt-auto">
                  <span class="price-label">{exp['price_unit']}</span>
                  <span class="price">{exp['price_display']}</span>
                </div>
                <div class="card-footer-actions">
                  <a class="btn btn-outline-details" href="{exp['link']}">View Details</a>
                  <a
                    class="btn btn-enquire"
                    href="../../../contact.html?destination=phuket&tour={exp['enquiry_param']}"
                    >Enquire Now →</a
                  >
                </div>
              </div>
            </article>"""
        cards_html_list.append(card_html)

        item_list_elements.append(f"""          {{
            "@type": "ListItem",
            "position": {idx},
            "name": "{exp['name']}",
            "url": "https://trippovention.co.th/packages/thailand/phuket/{exp['link']}"
          }}""")

    all_cards_html = "\n\n".join(cards_html_list)
    item_list_json = ",\n".join(item_list_elements)

    faq_acc_items = []
    faq_schema_items = []
    for i, (q, a) in enumerate(FAQS_DATA):
        is_open = " open" if i == 0 else ""
        faq_acc_items.append(f"""            <details class="faq-item"{is_open}>
              <summary class="faq-question"><span>{q}</span><span class="faq-chevron" aria-hidden="true">▾</span></summary>
              <div class="faq-answer"><p>{a}</p></div>
            </details>""")
        faq_schema_items.append(f"""          {{
            "@type": "Question",
            "name": "{q}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{a}"
            }}
          }}""")
    all_faqs_html = "\n".join(faq_acc_items)
    faq_schema_str = ",\n".join(faq_schema_items)

    page_html = f"""<!doctype html>
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
    <title>Phuket Sightseeing Tours &amp; Activities | Trippovention</title>
    <meta
      name="description"
      content="Explore Phuket sightseeing tours, Phi Phi island hopping, James Bond Island, Big Buddha, Simon Cabaret, and adventure activities. Enquire with Trippovention for current offers."
    />
    <meta name="author" content="Trippovention" />

    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://trippovention.co.th/packages/thailand/phuket/sightseeing.html" />
    <meta property="og:title" content="Phuket Sightseeing Tours &amp; Activities | Trippovention" />
    <meta
      property="og:description"
      content="Explore Phuket sightseeing tours, Phi Phi island hopping, James Bond Island, Big Buddha, Simon Cabaret, and adventure activities. Enquire with Trippovention for current offers."
    />
    <meta property="og:image" content="https://trippovention.co.th/assets/images/packages/thailand/phuket/hero_phuket.webp" />

    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="https://trippovention.co.th/packages/thailand/phuket/sightseeing.html" />
    <meta property="twitter:title" content="Phuket Sightseeing Tours &amp; Activities | Trippovention" />
    <meta
      property="twitter:description"
      content="Explore Phuket sightseeing tours, Phi Phi island hopping, James Bond Island, Big Buddha, Simon Cabaret, and adventure activities. Enquire with Trippovention for current offers."
    />
    <meta property="twitter:image" content="https://trippovention.co.th/assets/images/packages/thailand/phuket/hero_phuket.webp" />

    <link rel="canonical" href="https://trippovention.co.th/packages/thailand/phuket/sightseeing.html" />
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

    <!-- TouristDestination Schema -->
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "TouristDestination",
        "name": "Phuket Sightseeing Tours & Activities",
        "description": "Comprehensive catalogue of Phuket sightseeing tours, Phi Phi speedboat trips, James Bond Island, Big Buddha viewpoints, ethical elephant sanctuaries, and evening shows.",
        "url": "https://trippovention.co.th/packages/thailand/phuket/sightseeing.html",
        "containedInPlace": {{
          "@type": "Country",
          "name": "Thailand"
        }},
        "touristType": ["Island Hopping", "Beach Lovers", "Cultural Sightseeing", "Family Vacations", "Adventure Travelers"]
      }}
    </script>

    <!-- BreadcrumbList Schema -->
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

    <!-- ItemList Schema -->
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Phuket Sightseeing Tours & Excursions",
        "description": "Curated selection of verified sightseeing activities, island-hopping tours, and entertainment in Phuket.",
        "itemListElement": [
{item_list_json}
        ]
      }}
    </script>

    <!-- FAQPage Schema -->
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
{faq_schema_str}
        ]
      }}
    </script>

    <style>
      /* Scoped Extended Sightseeing Catalogue Styles */
      .catalogue-hero {{
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.92) 100%),
                    url('../../../assets/images/packages/thailand/phuket/hero_phuket.webp') center/cover no-repeat;
        color: #fff;
        padding: 56px 0 44px;
        text-align: center;
      }}
      .catalogue-hero h1 {{
        font-size: clamp(2rem, 4vw, 2.85rem);
        font-weight: 700;
        margin-bottom: 14px;
        letter-spacing: -0.02em;
      }}
      .catalogue-hero p {{
        font-size: 1.1rem;
        line-height: 1.65;
        max-width: 840px;
        margin: 0 auto 24px;
        color: rgba(255, 255, 255, 0.92);
      }}
      .hero-actions {{
        display: flex;
        gap: 12px;
        justify-content: center;
        flex-wrap: wrap;
      }}

      /* Curated Collections - Center-Aligned Grid */
      .collections-section {{
        background: var(--bg-secondary);
        padding: 36px 0 28px;
        border-bottom: 1px solid var(--border-color);
      }}
      .collections-grid {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 14px;
        max-width: 1200px;
        margin: 0 auto;
      }}
      .collection-pill-card {{
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 16px 14px;
        text-align: center;
        cursor: pointer;
        transition: all 0.25s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        color: var(--text-primary);
        box-shadow: var(--shadow-light);
        flex: 1 1 155px;
        max-width: 175px;
        min-width: 140px;
      }}
      .collection-pill-card:hover,
      .collection-pill-card.active {{
        border-color: var(--orange);
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(214, 128, 78, 0.2);
        background: linear-gradient(180deg, rgba(214, 128, 78, 0.08) 0%, var(--bg-primary) 100%);
      }}
      .collection-pill-card .col-icon {{
        font-size: 26px;
        margin-bottom: 6px;
      }}
      .collection-pill-card .col-title {{
        font-size: 0.88rem;
        font-weight: 600;
        line-height: 1.3;
      }}
      .collection-pill-card .col-sub {{
        font-size: 0.74rem;
        color: var(--text-muted);
        margin-top: 4px;
      }}

      /* Search & Filter Toolbar */
      .filter-toolbar {{
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 30px;
        box-shadow: var(--shadow-light);
      }}
      .search-box-row {{
        display: flex;
        gap: 12px;
        margin-bottom: 18px;
        align-items: center;
      }}
      .search-input-wrap {{
        position: relative;
        flex: 1;
      }}
      .search-input-wrap input {{
        width: 100%;
        padding: 12px 42px 12px 16px;
        font-size: 0.98rem;
        border: 1.5px solid var(--border-color);
        border-radius: 10px;
        background: var(--bg-secondary);
        color: var(--text-primary);
        transition: border-color 0.2s, box-shadow 0.2s;
      }}
      .search-input-wrap input:focus {{
        outline: none;
        border-color: var(--orange);
        box-shadow: 0 0 0 3px rgba(214, 128, 78, 0.2);
        background: var(--bg-primary);
      }}
      .search-clear-btn {{
        position: absolute;
        right: 12px;
        top: 50%;
        transform: translateY(-50%);
        background: none;
        border: none;
        font-size: 16px;
        color: var(--text-muted);
        cursor: pointer;
        display: none;
      }}
      .filter-toggle-mobile-btn {{
        display: none;
        padding: 12px 16px;
        font-size: 0.9rem;
        font-weight: 600;
        border: 1.5px solid var(--border-color);
        background: var(--bg-secondary);
        color: var(--text-primary);
        border-radius: 10px;
        cursor: pointer;
        align-items: center;
        gap: 6px;
      }}

      /* Category Pills Navigation */
      .category-pills-wrap {{
        display: flex;
        gap: 8px;
        overflow-x: auto;
        padding-bottom: 12px;
        margin-bottom: 16px;
        scrollbar-width: thin;
      }}
      .cat-pill {{
        white-space: nowrap;
        padding: 8px 16px;
        border-radius: 30px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid var(--border-color);
        background: var(--bg-secondary);
        color: var(--text-secondary);
        cursor: pointer;
        transition: all 0.2s ease;
        display: inline-flex;
        align-items: center;
        gap: 6px;
      }}
      .cat-pill:hover {{
        background: var(--border-light);
        color: var(--text-primary);
      }}
      .cat-pill.active {{
        background: var(--orange);
        color: #fff;
        border-color: var(--orange);
        box-shadow: 0 3px 10px rgba(214, 128, 78, 0.35);
      }}
      .cat-pill .pill-count {{
        background: rgba(0, 0, 0, 0.12);
        padding: 1px 7px;
        border-radius: 12px;
        font-size: 0.72rem;
      }}
      .cat-pill.active .pill-count {{
        background: rgba(255, 255, 255, 0.28);
      }}

      /* Secondary Filters Bar */
      .secondary-filters-bar {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 12px;
        align-items: center;
        padding-top: 14px;
        border-top: 1px solid var(--border-color);
      }}
      .filter-group label {{
        display: block;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        color: var(--text-muted);
        margin-bottom: 4px;
      }}
      .filter-select {{
        width: 100%;
        padding: 9px 12px;
        font-size: 0.88rem;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background: var(--bg-secondary);
        color: var(--text-primary);
        cursor: pointer;
      }}
      .filter-select:focus {{
        outline: none;
        border-color: var(--orange);
      }}
      .reset-filters-btn {{
        padding: 9px 14px;
        font-size: 0.85rem;
        font-weight: 600;
        background: none;
        border: 1px dashed var(--border-color);
        color: var(--text-muted);
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
        height: 38px;
        margin-top: 18px;
      }}
      .reset-filters-btn:hover {{
        border-color: var(--orange);
        color: var(--orange);
      }}

      /* Results Summary Header */
      .results-summary-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
        flex-wrap: wrap;
        gap: 12px;
      }}
      .results-count-text {{
        font-size: 0.95rem;
        color: var(--text-secondary);
        font-weight: 500;
      }}
      .results-count-text strong {{
        color: var(--text-primary);
      }}
      .back-to-dest-link {{
        font-size: 0.88rem;
        font-weight: 600;
        color: var(--orange);
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 6px;
      }}
      .back-to-dest-link:hover {{
        text-decoration: underline;
      }}

      /* Sightseeing Card presentation */
      .sightseeing-card {{
        display: flex;
        flex-direction: column;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
      }}
      .sightseeing-card:hover {{
        transform: translateY(-4px);
        box-shadow: var(--shadow-large);
      }}
      .sightseeing-card .body {{
        display: flex;
        flex-direction: column;
        flex: 1;
      }}
      .card-meta-row {{
        display: flex;
        gap: 6px;
        flex-wrap: wrap;
        margin-bottom: 10px;
      }}
      .card-tag {{
        font-size: 0.72rem;
        font-weight: 600;
        padding: 3px 8px;
        border-radius: 6px;
        background: var(--bg-tertiary);
        color: var(--text-secondary);
      }}
      .card-tag.highlight-tag {{
        background: var(--orange-light);
        color: var(--orange-dark);
      }}
      [data-theme="dark"] .card-tag.highlight-tag {{
        background: rgba(214, 128, 78, 0.25);
        color: #f7b28d;
      }}
      .sightseeing-card h3 {{
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 12px;
        line-height: 1.35;
      }}
      .card-title-link {{
        color: var(--text-primary);
        text-decoration: none;
      }}
      .card-title-link:hover {{
        color: var(--orange);
      }}
      .card-footer-actions {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
        margin-top: 14px;
      }}
      .btn-outline-details {{
        background: transparent !important;
        color: var(--text-primary) !important;
        border: 1.5px solid var(--border-color) !important;
        font-size: 0.8rem !important;
        padding: 8px 10px !important;
        border-radius: 8px !important;
        text-align: center;
        text-transform: none !important;
        box-shadow: none !important;
      }}
      .btn-outline-details:hover {{
        border-color: var(--orange) !important;
        color: var(--orange) !important;
        transform: none !important;
      }}
      .btn-enquire {{
        background: var(--gradient-primary) !important;
        color: #fff !important;
        font-size: 0.8rem !important;
        padding: 8px 10px !important;
        border-radius: 8px !important;
        text-align: center;
        text-transform: none !important;
        box-shadow: none !important;
      }}
      .btn-enquire:hover {{
        transform: none !important;
        box-shadow: 0 4px 12px rgba(214, 128, 78, 0.35) !important;
      }}

      /* Empty State */
      .empty-results-box {{
        grid-column: 1 / -1;
        text-align: center;
        padding: 60px 20px;
        background: var(--bg-secondary);
        border: 2px dashed var(--border-color);
        border-radius: 16px;
      }}
      .empty-results-box .empty-icon {{
        font-size: 44px;
        margin-bottom: 12px;
      }}

      @media (max-width: 1024px) {{
        .collection-pill-card {{
          flex: 1 1 200px;
          max-width: 240px;
        }}
      }}

      @media (max-width: 768px) {{
        .filter-toggle-mobile-btn {{
          display: inline-flex;
        }}
        .secondary-filters-bar {{
          display: none;
        }}
        .secondary-filters-bar.mobile-open {{
          display: grid;
        }}
        .collection-pill-card {{
          flex: 1 1 140px;
          max-width: 48%;
          padding: 14px 10px;
        }}
      }}

      @media (max-width: 480px) {{
        .collections-grid {{
          gap: 10px;
        }}
        .collection-pill-card {{
          flex: 1 1 130px;
          max-width: 48%;
          padding: 12px 8px;
        }}
        .collection-pill-card .col-icon {{
          font-size: 22px;
          margin-bottom: 4px;
        }}
        .collection-pill-card .col-title {{
          font-size: 0.82rem;
        }}
        .collection-pill-card .col-sub {{
          font-size: 0.7rem;
        }}
      }}
    </style>
  </head>

  <body>
    <a href="#main" class="skip-link" aria-label="Skip to main content" id="skip-link">
      Skip to main content
    </a>

    <!-- Main Navigation Bar -->
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

      <!-- Hero Header -->
      <header class="catalogue-hero">
        <div class="container">
          <span class="badge mb-10" style="background: rgba(214, 128, 78, 0.2); color: #f7b28d; border: 1px solid rgba(214, 128, 78, 0.4);">
            Extended Sightseeing Catalogue
          </span>
          <h1>Discover the Best of Phuket</h1>
          <p>
            Explore Phuket's premier island-hopping tours to Phi Phi &amp; James Bond Island, ethical elephant sanctuaries, world-class evening shows, water parks, cultural viewpoints, and outdoor adventures. Discover verified sightseeing options and enquire directly with Trippovention.
          </p>
          <div class="hero-actions">
            <a class="btn btn-lg" href="#catalogue">Browse Experiences ↓</a>
            <a class="btn btn-lg ghost" href="index.html">← Back to Phuket Destination Page</a>
          </div>
        </div>
      </header>

      <!-- Section: Curated Phuket Collections (Center-Aligned) -->
      <section class="collections-section" aria-label="Curated Phuket Collections">
        <div class="container">
          <div class="section-title text-center" style="margin-bottom: 20px;">
            <h2 style="font-size: 1.45rem;">Curated Phuket Collections</h2>
            <p class="subtitle" style="margin-bottom: 0;">Explore handpicked highlights curated for specific travel styles</p>
          </div>
          <div class="collections-grid">
            <button type="button" class="collection-pill-card active" data-collection="all" aria-label="Filter by All Highlights">
              <span class="col-icon">⭐</span>
              <span class="col-title">All Highlights</span>
              <span class="col-sub">23 Experiences</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="island-tours" aria-label="Filter by Island Hopping">
              <span class="col-icon">🏝️</span>
              <span class="col-title">Island Hopping</span>
              <span class="col-sub">Speedboats &amp; Charters</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="city-culture" aria-label="Filter by City & Culture">
              <span class="col-icon">🏛️</span>
              <span class="col-title">City &amp; Heritage</span>
              <span class="col-sub">Viewpoints &amp; Temples</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="shows-entertainment" aria-label="Filter by Night Shows & Theatre">
              <span class="col-icon">🎭</span>
              <span class="col-title">Night Shows</span>
              <span class="col-sub">Grand Productions</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="adventure-outdoor" aria-label="Filter by Adventure & Outdoor">
              <span class="col-icon">⚡</span>
              <span class="col-title">Adventure &amp; Nature</span>
              <span class="col-sub">Zipline, Park &amp; Surf</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="wildlife-family" aria-label="Filter by Wildlife & Family Fun">
              <span class="col-icon">🐘</span>
              <span class="col-title">Family &amp; Wildlife</span>
              <span class="col-sub">Sanctuary &amp; Water Park</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="thai-cooking" aria-label="Filter by Thai Cooking Class">
              <span class="col-icon">🍲</span>
              <span class="col-title">Thai Cooking</span>
              <span class="col-sub">Culinary Workshop</span>
            </button>
          </div>
        </div>
      </section>

      <!-- Sightseeing Catalogue Section -->
      <section class="section" id="catalogue">
        <div class="container">
          <!-- Filter & Search Toolbar -->
          <div class="filter-toolbar" role="search" aria-label="Search and filter Phuket sightseeing">
            <div class="search-box-row">
              <div class="search-input-wrap">
                <input
                  type="text"
                  id="phuketSearchInput"
                  placeholder="Find Your Phuket Experience (e.g. Phi Phi, James Bond, Big Buddha, Simon Cabaret)..."
                  aria-label="Find Your Phuket Experience"
                  autocomplete="off"
                />
                <button type="button" id="searchClearBtn" class="search-clear-btn" aria-label="Clear search">✕</button>
              </div>
              <button type="button" id="filterToggleMobileBtn" class="filter-toggle-mobile-btn" aria-expanded="false" aria-controls="secondaryFiltersBar">
                <span>⚙️ Filters</span>
              </button>
            </div>

            <!-- Category Navigation Pills -->
            <div class="category-pills-wrap" role="tablist" aria-label="Categories">
              <button type="button" class="cat-pill active" data-category="all" role="tab" aria-selected="true">
                All Experiences <span class="pill-count" id="countAll">23</span>
              </button>
              <button type="button" class="cat-pill" data-category="island-tours" role="tab" aria-selected="false">
                🏝️ Island Tours <span class="pill-count">8</span>
              </button>
              <button type="button" class="cat-pill" data-category="city-culture" role="tab" aria-selected="false">
                🏛️ City &amp; Culture <span class="pill-count">4</span>
              </button>
              <button type="button" class="cat-pill" data-category="shows-entertainment" role="tab" aria-selected="false">
                🎭 Shows &amp; Theatre <span class="pill-count">4</span>
              </button>
              <button type="button" class="cat-pill" data-category="adventure-outdoor" role="tab" aria-selected="false">
                ⚡ Adventure &amp; Outdoor <span class="pill-count">3</span>
              </button>
              <button type="button" class="cat-pill" data-category="wildlife-family" role="tab" aria-selected="false">
                🐘 Wildlife &amp; Family <span class="pill-count">3</span>
              </button>
              <button type="button" class="cat-pill" data-category="thai-cooking" role="tab" aria-selected="false">
                🍲 Thai Cooking <span class="pill-count">1</span>
              </button>
            </div>

            <!-- Secondary Filters Panel -->
            <div class="secondary-filters-bar" id="secondaryFiltersBar">
              <div class="filter-group">
                <label for="filterDuration">Duration</label>
                <select id="filterDuration" class="filter-select">
                  <option value="all">All Durations</option>
                  <option value="half-day">Half Day (1–4 hrs)</option>
                  <option value="full-day">Full Day (5+ hrs)</option>
                  <option value="evening">Evening / Shows</option>
                </select>
              </div>

              <div class="filter-group">
                <label for="filterTourType">Tour Format</label>
                <select id="filterTourType" class="filter-select">
                  <option value="all">All Formats</option>
                  <option value="speedboat">Speedboat Excursion</option>
                  <option value="guided">Guided Minivan Tour</option>
                  <option value="show">Theatrical Show</option>
                  <option value="adventure">Adventures &amp; Sports</option>
                  <option value="attraction">Attraction Day Pass</option>
                  <option value="private">Private VIP Hire</option>
                </select>
              </div>

              <div class="filter-group">
                <label for="filterTraveler">Experience Style</label>
                <select id="filterTraveler" class="filter-select">
                  <option value="all">All Styles</option>
                  <option value="beach">Island &amp; Beach</option>
                  <option value="culture">Culture &amp; Temples</option>
                  <option value="adventure">Active Adventure</option>
                  <option value="family">Family Friendly</option>
                  <option value="luxury">Luxury &amp; VIP</option>
                </select>
              </div>

              <div class="filter-group">
                <label for="sortBy">Sort By</label>
                <select id="sortBy" class="filter-select">
                  <option value="recommended">Recommended</option>
                  <option value="price-asc">Price: Low to High</option>
                  <option value="price-desc">Price: High to Low</option>
                  <option value="duration-asc">Duration: Short to Long</option>
                </select>
              </div>

              <button type="button" id="resetFiltersBtn" class="reset-filters-btn" title="Reset all search filters">
                ↺ Reset Filters
              </button>
            </div>
          </div>

          <!-- Results Summary Header -->
          <div class="results-summary-row">
            <div class="results-count-text">
              Showing <strong id="visibleCount">23</strong> of 23 experiences in Phuket
            </div>
            <a href="index.html" class="back-to-dest-link">← Return to Phuket Destination Page</a>
          </div>

          <!-- Product Cards Grid -->
          <div class="grid cols-3" id="cardsGrid">
{all_cards_html}

            <!-- Empty Results Notice -->
            <div id="emptyResultsBox" class="empty-results-box" style="display: none;">
              <div class="empty-icon">🔍</div>
              <h3>No Experiences Matched Your Filters</h3>
              <p class="muted">Try adjusting your keywords, duration, or experience style, or reset all filters.</p>
              <button type="button" class="btn btn-sm mt-15" id="emptyResetBtn">Reset All Filters</button>
            </div>
          </div>
        </div>
      </section>

      <!-- Phuket Sightseeing FAQs Section -->
      <section class="section alt" id="faqs" aria-label="Frequently Asked Questions">
        <div class="container">
          <div class="section-title text-center">
            <h2>Frequently Asked Questions</h2>
            <p class="subtitle">Essential advice for planning your Phuket tours, island trips &amp; activities</p>
          </div>
          <div class="faqs-accordion-wrap max-width-900" style="margin: 0 auto;">
{all_faqs_html}
          </div>
        </div>
      </section>

      <!-- Bottom Advisory Notice -->
      <section class="section" style="padding-top: 30px; padding-bottom: 40px;">
        <div class="container">
          <div class="card" style="padding: 24px; border-left: 4px solid var(--orange); background: var(--bg-secondary);">
            <h4 style="margin-top: 0; margin-bottom: 8px;">Trip Planning &amp; Booking Advisory</h4>
            <p class="muted" style="margin-bottom: 0; font-size: 0.92rem; line-height: 1.6;">
              Trippovention operates on an enquiry-led, personalized booking model. Every excursion is coordinated by experienced destination specialists who confirm hotel pickup schedules, verify marine weather conditions, apply multi-tour discounts, and provide official booking confirmations with dedicated offline support.
            </p>
          </div>
        </div>
      </section>
    </main>

    <!-- Standardized Global Footer -->
    <footer class="footer" role="contentinfo">
      <div class="container">
        <div class="grid cols-3">
          <div>
            <h3>Trippovention</h3>
            <p>
              Your trusted travel partner for unforgettable journeys. We believe that travel
              should be transformative and memorable.
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

    <!-- Interactive Catalogue Filter Engine -->
    <script>
      (function () {{
        const searchInput = document.getElementById("phuketSearchInput");
        const searchClearBtn = document.getElementById("searchClearBtn");
        const mobileToggleBtn = document.getElementById("filterToggleMobileBtn");
        const secondaryBar = document.getElementById("secondaryFiltersBar");
        const catPills = document.querySelectorAll(".cat-pill");
        const collectionCards = document.querySelectorAll(".collection-pill-card");
        const filterDuration = document.getElementById("filterDuration");
        const filterTourType = document.getElementById("filterTourType");
        const filterTraveler = document.getElementById("filterTraveler");
        const sortBy = document.getElementById("sortBy");
        const resetFiltersBtn = document.getElementById("resetFiltersBtn");
        const emptyResetBtn = document.getElementById("emptyResetBtn");
        const visibleCountEl = document.getElementById("visibleCount");
        const cardsGrid = document.getElementById("cardsGrid");
        const emptyResultsBox = document.getElementById("emptyResultsBox");
        const cards = Array.from(document.querySelectorAll(".sightseeing-card"));

        let currentCategory = "all";
        let currentCollection = "all";
        let currentDuration = "all";
        let currentTourType = "all";
        let currentTraveler = "all";
        let currentSearchQuery = "";
        let currentSort = "recommended";

        // Mobile secondary filter toggle
        if (mobileToggleBtn && secondaryBar) {{
          mobileToggleBtn.addEventListener("click", function () {{
            const isOpen = secondaryBar.classList.toggle("mobile-open");
            mobileToggleBtn.setAttribute("aria-expanded", isOpen ? "true" : "false");
          }});
        }}

        // Search Input & Clear
        if (searchInput) {{
          searchInput.addEventListener("input", function () {{
            currentSearchQuery = this.value.trim().toLowerCase();
            if (searchClearBtn) {{
              searchClearBtn.style.display = currentSearchQuery.length > 0 ? "block" : "none";
            }}
            applyFilters();
          }});
        }}
        if (searchClearBtn) {{
          searchClearBtn.addEventListener("click", function () {{
            if (searchInput) searchInput.value = "";
            currentSearchQuery = "";
            this.style.display = "none";
            applyFilters();
            if (searchInput) searchInput.focus();
          }});
        }}

        // Category Pills
        catPills.forEach(pill => {{
          pill.addEventListener("click", function () {{
            catPills.forEach(p => {{
              p.classList.remove("active");
              p.setAttribute("aria-selected", "false");
            }});
            this.classList.add("active");
            this.setAttribute("aria-selected", "true");
            currentCategory = this.dataset.category;

            // Reset collection cards
            collectionCards.forEach(c => c.classList.remove("active"));
            currentCollection = "all";

            applyFilters();
          }});
        }});

        // Curated Collections Grid Cards
        collectionCards.forEach(card => {{
          card.addEventListener("click", function (e) {{
            e.preventDefault();
            const col = this.dataset.collection;
            if (currentCollection === col) {{
              this.classList.remove("active");
              currentCollection = "all";
            }} else {{
              collectionCards.forEach(c => c.classList.remove("active"));
              this.classList.add("active");
              currentCollection = col;
              catPills.forEach(p => {{
                p.classList.remove("active");
                p.setAttribute("aria-selected", "false");
              }});
              const allPill = document.querySelector('.cat-pill[data-category="all"]');
              if (allPill) {{
                allPill.classList.add("active");
                allPill.setAttribute("aria-selected", "true");
              }}
              currentCategory = "all";
            }}
            applyFilters();
            const catalogueEl = document.getElementById("catalogue");
            if (catalogueEl) {{
              catalogueEl.scrollIntoView({{ behavior: "smooth", block: "start" }});
            }}
          }});
        }});

        // Dropdown filter change listeners
        if (filterDuration) {{
          filterDuration.addEventListener("change", function () {{
            currentDuration = this.value;
            applyFilters();
          }});
        }}
        if (filterTourType) {{
          filterTourType.addEventListener("change", function () {{
            currentTourType = this.value;
            applyFilters();
          }});
        }}
        if (filterTraveler) {{
          filterTraveler.addEventListener("change", function () {{
            currentTraveler = this.value;
            applyFilters();
          }});
        }}
        if (sortBy) {{
          sortBy.addEventListener("change", function () {{
            currentSort = this.value;
            applyFilters();
          }});
        }}

        // Reset Filters logic
        function resetAllFilters() {{
          currentCategory = "all";
          currentCollection = "all";
          currentDuration = "all";
          currentTourType = "all";
          currentTraveler = "all";
          currentSearchQuery = "";
          currentSort = "recommended";

          if (searchInput) searchInput.value = "";
          if (searchClearBtn) searchClearBtn.style.display = "none";
          if (filterDuration) filterDuration.value = "all";
          if (filterTourType) filterTourType.value = "all";
          if (filterTraveler) filterTraveler.value = "all";
          if (sortBy) sortBy.value = "recommended";

          catPills.forEach(p => {{
            p.classList.remove("active");
            p.setAttribute("aria-selected", "false");
          }});
          const allPill = document.querySelector('.cat-pill[data-category="all"]');
          if (allPill) {{
            allPill.classList.add("active");
            allPill.setAttribute("aria-selected", "true");
          }}
          collectionCards.forEach(c => c.classList.remove("active"));
          const allCol = document.querySelector('.collection-pill-card[data-collection="all"]');
          if (allCol) allCol.classList.add("active");

          applyFilters();
        }}

        if (resetFiltersBtn) resetFiltersBtn.addEventListener("click", resetAllFilters);
        if (emptyResetBtn) emptyResetBtn.addEventListener("click", resetAllFilters);

        // Core Filter & Sort Engine
        function applyFilters() {{
          let visibleCount = 0;

          cards.forEach(card => {{
            const cat = card.dataset.category || "";
            const collections = (card.dataset.collections || "").split(",");
            const dur = card.dataset.duration || "";
            const tType = card.dataset.tourType || "";
            const styles = (card.dataset.styles || "").split(",");
            const name = (card.dataset.name || "").toLowerCase();
            const textContent = card.textContent.toLowerCase();

            let match = true;

            // Category filter
            if (currentCategory !== "all" && cat !== currentCategory) {{
              match = false;
            }}

            // Curated collection filter
            if (currentCollection !== "all" && !collections.includes(currentCollection)) {{
              match = false;
            }}

            // Duration filter
            if (currentDuration !== "all" && dur !== currentDuration) {{
              match = false;
            }}

            // Tour Type filter
            if (currentTourType !== "all" && tType !== currentTourType) {{
              match = false;
            }}

            // Style filter
            if (currentTraveler !== "all" && !styles.includes(currentTraveler)) {{
              match = false;
            }}

            // Search query filter
            if (currentSearchQuery && !name.includes(currentSearchQuery) && !textContent.includes(currentSearchQuery)) {{
              match = false;
            }}

            if (match) {{
              card.style.display = "flex";
              visibleCount++;
            }} else {{
              card.style.display = "none";
            }}
          }});

          // Sorting visible cards
          const sortedCards = cards.filter(c => c.style.display !== "none");
          if (currentSort === "price-asc") {{
            sortedCards.sort((a, b) => (parseFloat(a.dataset.price) || 9999) - (parseFloat(b.dataset.price) || 9999));
          }} else if (currentSort === "price-desc") {{
            sortedCards.sort((a, b) => (parseFloat(b.dataset.price) || 0) - (parseFloat(a.dataset.price) || 0));
          }} else if (currentSort === "duration-asc") {{
            sortedCards.sort((a, b) => (parseFloat(a.dataset.durationHours) || 0) - (parseFloat(b.dataset.durationHours) || 0));
          }}

          // Re-append sorted cards
          sortedCards.forEach(card => cardsGrid.appendChild(card));

          // Update Counter & Empty State
          if (visibleCountEl) visibleCountEl.textContent = visibleCount;
          if (emptyResultsBox) {{
            emptyResultsBox.style.display = visibleCount === 0 ? "block" : "none";
            cardsGrid.appendChild(emptyResultsBox);
          }}
        }}

        // Initial apply
        applyFilters();
      }})();
    </script>
    <script src="../../../assets/app.js"></script>
    <script src="../../../assets/search.js" defer=""></script>
  </body>
</html>
"""

    with open(CATALOGUE_PATH, "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"Phuket Sightseeing Catalogue successfully created at:\n{CATALOGUE_PATH}")

if __name__ == "__main__":
    generate_catalogue_html()
