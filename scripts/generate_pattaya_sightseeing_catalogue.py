#!/usr/bin/env python3
"""
Generate the Pattaya Sightseeing Catalogue Page:
docs/packages/thailand/pattaya/sightseeing.html
Modeled directly on docs/packages/thailand/krabi/sightseeing.html and Bangkok catalogue.
Preserves design system, typography, colors, centered curated collections,
search/filtering engine, 24 experiences, 10 FAQs, and JSON-LD schemas.
"""

import os

CATALOGUE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs", "packages", "thailand", "pattaya", "sightseeing.html"
)

EXPERIENCES = [
    {
        "id": "pat-01",
        "name": "Sanctuary of Truth Museum Guided Tour",
        "link": "sanctuary_of_truth_pattaya.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_sanctuary_of_truth_pattaya.webp",
        "alt": "Sanctuary of Truth hand-carved wooden temple Pattaya",
        "ribbon": "🏛️ Architectural Icon",
        "category": "temples-culture",
        "category_label": "Temples & Culture",
        "collections": "temples-culture,city-landmarks",
        "duration": "half-day",
        "duration_hours": "2.5",
        "duration_label": "⏱️ 2–3 Hours",
        "tour_type": "guided",
        "tour_type_label": "Guided Tour",
        "styles": "culture",
        "price": "700",
        "price_display": "THB 700",
        "price_unit": "Price Per Person",
        "highlights": [
            "World's largest all-wood seaside architectural sanctuary (105m)",
            "Built without metal nails using traditional interlocking joinery",
            "Four cosmological wings representing Thai, Khmer, Chinese & Hindu art",
            "Observe master woodcarvers shaping intricate wooden reliefs"
        ],
        "enquiry_param": "Sanctuary+of+Truth+Museum+Guided+Tour"
    },
    {
        "id": "pat-02",
        "name": "Coral Island (Koh Larn) Speedboat Tour",
        "link": "coral_island_tour.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_coral_island_tour.webp",
        "alt": "Coral Island Koh Larn speedboat tour Pattaya",
        "ribbon": "⭐ Bestseller",
        "category": "coral-island",
        "category_label": "Coral Island & Marine",
        "collections": "coral-island,cruises-boats",
        "duration": "full-day",
        "duration_hours": "6",
        "duration_label": "⏱️ Full Day (6 Hrs)",
        "tour_type": "shared",
        "tour_type_label": "Shared / Speedboat",
        "styles": "beach,adventure",
        "price": "850",
        "price_display": "THB 850",
        "price_unit": "Price Per Person",
        "highlights": [
            "Round-trip shared speedboat transfer from Bali Hai Pier",
            "Relax on white sandy beaches at Tawaen or Tien Beach",
            "Delicious Indian or seafood beachside lunch included",
            "Optional parasailing, seawalker diving & jet ski activities"
        ],
        "enquiry_param": "Coral+Island+Speedboat+Tour+Pattaya"
    },
    {
        "id": "pat-03",
        "name": "Nong Nooch Tropical Garden & Shows",
        "link": "nong_nooch_tropical_garden.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_nong_nooch_tropical_garden.webp",
        "alt": "Nong Nooch Tropical Garden botanical park Pattaya",
        "ribbon": "🌺 World-Renowned",
        "category": "gardens-wildlife",
        "category_label": "Gardens & Wildlife",
        "collections": "gardens-wildlife,waterparks-family",
        "duration": "half-day",
        "duration_hours": "4.5",
        "duration_label": "⏱️ 4–5 Hours",
        "tour_type": "guided",
        "tour_type_label": "Sightseeing Tram & Show",
        "styles": "nature,family",
        "price": "1596",
        "price_display": "THB 1,596",
        "price_unit": "Price Per Person",
        "highlights": [
            "600-acre award-winning world-class botanical landscape",
            "Panoramic hop-on hop-off sightseeing tram tour",
            "Spectacular traditional Thai cultural dance & martial arts show",
            "Life-size prehistoric Dinosaur Valley sculpture walk"
        ],
        "enquiry_param": "Nong+Nooch+Tropical+Garden+Tour"
    },
    {
        "id": "pat-04",
        "name": "Alcazar Cabaret Show Pattaya",
        "link": "alcazar_cabaret_show.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_alcazar_cabaret_show.webp",
        "alt": "Alcazar Cabaret Show Pattaya stage performance",
        "ribbon": "✨ Legendary Cabaret",
        "category": "shows-nightlife",
        "category_label": "Shows & Nightlife",
        "collections": "shows-nightlife",
        "duration": "half-day",
        "duration_hours": "1.5",
        "duration_label": "⏱️ 70 Minutes",
        "tour_type": "onsite",
        "tour_type_label": "Theatre Ticket",
        "styles": "nightlife,culture",
        "price": "900",
        "price_display": "THB 900",
        "price_unit": "Price Per Person",
        "highlights": [
            "World-famous transgender cabaret performance in modern theatre",
            "Extravagant feather costumes, dynamic lighting & sound system",
            "International musical dance acts from Thailand, China, India & West",
            "Courtyard photo session with star performers after the show"
        ],
        "enquiry_param": "Alcazar+Cabaret+Show+Pattaya"
    },
    {
        "id": "pat-05",
        "name": "Ramayana Water Park Pattaya",
        "link": "ramayana_water_park_pattaya.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_ramayana_water_park.webp",
        "alt": "Ramayana Water Park slides and wave pool Pattaya",
        "ribbon": "🌊 #1 Water Park in Thailand",
        "category": "waterparks-family",
        "category_label": "Water Parks & Family",
        "collections": "waterparks-family",
        "duration": "full-day",
        "duration_hours": "7",
        "duration_label": "⏱️ Full Day (6–7 Hrs)",
        "tour_type": "onsite",
        "tour_type_label": "Day Pass",
        "styles": "family,adventure",
        "price": "1190",
        "price_display": "THB 1,190",
        "price_unit": "Price Per Person",
        "highlights": [
            "Thailand's largest water park set in scenic Silverlake valley",
            "21 premium WhiteWater West slides including Aqualoop & Freefall",
            "600-meter lazy river passing through ancient temple ruins",
            "Double-wave pool with gentle and rolling ocean wave zones"
        ],
        "enquiry_param": "Ramayana+Water+Park+Pattaya+Tickets"
    },
    {
        "id": "pat-06",
        "name": "Columbia Pictures Aquaverse",
        "link": "columbia_pictures_aquaverse_tickets.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_columbia_pictures_aquaverse.webp",
        "alt": "Columbia Pictures Aquaverse movie themed water park Pattaya",
        "ribbon": "🎬 World's First",
        "category": "waterparks-family",
        "category_label": "Water Parks & Family",
        "collections": "waterparks-family",
        "duration": "full-day",
        "duration_hours": "6",
        "duration_label": "⏱️ Full Day (5–6 Hrs)",
        "tour_type": "onsite",
        "tour_type_label": "Day Pass",
        "styles": "family,adventure",
        "price": "1290",
        "price_display": "THB 1,290",
        "price_unit": "Price Per Person",
        "highlights": [
            "World's first fully branded Columbia Pictures movie theme park",
            "Ghostbusters Proton Stream enclosed dark sphere water coaster",
            "Hotel Transylvania splash castle with 9 family slides & dump buckets",
            "Mega Wave Pool with giant outdoor LED cinema screen"
        ],
        "enquiry_param": "Columbia+Pictures+Aquaverse+Tickets"
    },
    {
        "id": "pat-07",
        "name": "Underwater World Pattaya Aquarium",
        "link": "underwater_world_pattaya.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_underwater_world_pattaya.webp",
        "alt": "Underwater World Pattaya pedestrian aquarium tunnel",
        "ribbon": "🦈 100m Ocean Tunnel",
        "category": "waterparks-family",
        "category_label": "Water Parks & Family",
        "collections": "waterparks-family,gardens-wildlife",
        "duration": "half-day",
        "duration_hours": "2.5",
        "duration_label": "⏱️ 2–3 Hours",
        "tour_type": "onsite",
        "tour_type_label": "Entry Ticket",
        "styles": "family,nature",
        "price": "650",
        "price_display": "THB 650",
        "price_unit": "Price Per Person",
        "highlights": [
            "100-meter 180-degree curved acrylic underwater tunnel",
            "Over 5,000 marine animals across 500 diverse species",
            "Shark & Stingray zone with scheduled scuba diver feeding shows",
            "Interactive touch pool with starfish, rays & sea cucumbers"
        ],
        "enquiry_param": "Underwater+World+Pattaya+Tickets"
    },
    {
        "id": "pat-08",
        "name": "Pattaya Dolphinarium Show",
        "link": "pattaya_dolphinarium_show.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_dolphinarium.webp",
        "alt": "Pattaya Dolphinarium dolphins jumping during performance",
        "ribbon": "🐬 European-Standard",
        "category": "shows-nightlife",
        "category_label": "Shows & Nightlife",
        "collections": "shows-nightlife,waterparks-family",
        "duration": "half-day",
        "duration_hours": "1.5",
        "duration_label": "⏱️ 50-Min Show",
        "tour_type": "onsite",
        "tour_type_label": "Show Ticket",
        "styles": "family",
        "price": "800",
        "price_display": "THB 800",
        "price_unit": "Price Per Person",
        "highlights": [
            "European-standard marine facility with sheltered stadium seating",
            "Acrobatic bottlenose dolphins performing synchronized aerial leaps",
            "Playful South American fur seal antics and comedic routines",
            "Post-show photo sessions and optional swimming with dolphins"
        ],
        "enquiry_param": "Pattaya+Dolphinarium+Show+Tickets"
    },
    {
        "id": "pat-09",
        "name": "Tiffany's Show Pattaya Cabaret",
        "link": "tiffanys_show_pattaya.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_tiffanys_show_pattaya.webp",
        "alt": "Tiffany's Show Pattaya stage performance dancers",
        "ribbon": "👑 Pioneer Cabaret 1974",
        "category": "shows-nightlife",
        "category_label": "Shows & Nightlife",
        "collections": "shows-nightlife",
        "duration": "half-day",
        "duration_hours": "1.5",
        "duration_label": "⏱️ 75 Minutes",
        "tour_type": "onsite",
        "tour_type_label": "Theatre Ticket",
        "styles": "nightlife,culture",
        "price": "1200",
        "price_display": "THB 1,200",
        "price_unit": "Price Per Person",
        "highlights": [
            "Southeast Asia's pioneer transgender cabaret with 50-year heritage",
            "Palatial 1,000-seat European-style theatre on Pattaya Second Road",
            "Opulent sets, Broadway numbers, Bollywood glitz & Siam court dance",
            "Voted among the Top 10 World Cabaret Spectaculars"
        ],
        "enquiry_param": "Tiffanys+Show+Pattaya+Tickets"
    },
    {
        "id": "pat-10",
        "name": "Colosseum Cabaret Show Pattaya",
        "link": "colosseum_cabaret_show_pattaya.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_colosseum_cabaret_show.webp",
        "alt": "Colosseum Cabaret Show Pattaya amphitheatre dancers",
        "ribbon": "🏛️ Roman Amphitheatre",
        "category": "shows-nightlife",
        "category_label": "Shows & Nightlife",
        "collections": "shows-nightlife",
        "duration": "half-day",
        "duration_hours": "1.5",
        "duration_label": "⏱️ 75 Minutes",
        "tour_type": "onsite",
        "tour_type_label": "Theatre Ticket",
        "styles": "nightlife",
        "price": "850",
        "price_display": "THB 850",
        "price_unit": "Price Per Person",
        "highlights": [
            "Largest cabaret theatre in Pattaya styled like the Roman Colosseum",
            "1,250 tiered amphitheatre seats ensuring 100% clear sightlines",
            "14 kaleidoscopic acts featuring hydraulic stage lifts & LED sets",
            "Convenient location on Thepprasit Road near weekend night market"
        ],
        "enquiry_param": "Colosseum+Cabaret+Show+Pattaya"
    },
    {
        "id": "pat-11",
        "name": "Max Muay Thai Stadium Live Fights",
        "link": "max_muay_thai_stadium_tickets.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_max_muay_thai_stadium.webp",
        "alt": "Max Muay Thai Stadium live boxing bout Pattaya",
        "ribbon": "🥊 Authentic Muay Thai",
        "category": "shows-nightlife",
        "category_label": "Shows & Nightlife",
        "collections": "shows-nightlife,adventure-outdoor",
        "duration": "half-day",
        "duration_hours": "2.5",
        "duration_label": "⏱️ 2–3 Hours",
        "tour_type": "onsite",
        "tour_type_label": "Live Fight Ticket",
        "styles": "adventure,nightlife",
        "price": "1500",
        "price_display": "THB 1,500",
        "price_unit": "Price Per Person",
        "highlights": [
            "Real competitive professional bouts sanctioned by world Muay Thai bodies",
            "3 to 5 hard-hitting fights between Thai champions and world contenders",
            "Traditional Wai Kru pre-fight dance and live Sarama fight music",
            "Ringside VIP and stadium grandstand seating options available"
        ],
        "enquiry_param": "Max+Muay+Thai+Stadium+Fight+Tickets"
    },
    {
        "id": "pat-12",
        "name": "Khao Kheow Open Zoo Excursion",
        "link": "khao_kheow_open_zoo_tour.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_khao_kheow_open_zoo.webp",
        "alt": "Khao Kheow Open Zoo pygmy hippo and wildlife Pattaya",
        "ribbon": "🦛 Home of Moo Deng",
        "category": "gardens-wildlife",
        "category_label": "Gardens & Wildlife",
        "collections": "gardens-wildlife,waterparks-family",
        "duration": "full-day",
        "duration_hours": "5.5",
        "duration_label": "⏱️ 5–6 Hours",
        "tour_type": "shared",
        "tour_type_label": "Shared Safari Tour",
        "styles": "nature,family",
        "price": "1350",
        "price_display": "THB 1,350",
        "price_unit": "Price Per Person",
        "highlights": [
            "2,000-acre open wildlife conservation park in protected rainforest",
            "Visit viral sensation Moo Deng and the pygmy hippo family",
            "Open safari tram connecting African Savanna, Cats & Aviary",
            "Respectful hand-feeding opportunities with giraffes and rhinos"
        ],
        "enquiry_param": "Khao+Kheow+Open+Zoo+Excursion"
    },
    {
        "id": "pat-13",
        "name": "Ethical Elephant Sanctuary Experience",
        "link": "pattaya_elephant_sanctuary_tour.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_elephant_sanctuary.webp",
        "alt": "Ethical Elephant Sanctuary interaction Pattaya",
        "ribbon": "🐘 Strictly No-Riding",
        "category": "gardens-wildlife",
        "category_label": "Gardens & Wildlife",
        "collections": "gardens-wildlife",
        "duration": "half-day",
        "duration_hours": "4.5",
        "duration_label": "⏱️ 4–5 Hours",
        "tour_type": "shared",
        "tour_type_label": "Ethical Program",
        "styles": "nature,family",
        "price": "2200",
        "price_display": "THB 2,200",
        "price_unit": "Price Per Person",
        "highlights": [
            "Compassionate sanctuary dedicated to rescued Asian elephants",
            "Prepare healthy fruit balls, bananas & herbal dietary supplements",
            "Join elephants for cooling mud spa and freshwater bathing pool",
            "Delicious Thai buffet lunch and roundtrip hotel transfers included"
        ],
        "enquiry_param": "Pattaya+Elephant+Sanctuary+Experience"
    },
    {
        "id": "pat-14",
        "name": "Art in Paradise 3D Trick Eye Museum",
        "link": "art_in_paradise_pattaya.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_art_in_paradise_pattaya.webp",
        "alt": "Art in Paradise 3D optical illusion museum Pattaya",
        "ribbon": "🎨 Interactive 3D Art",
        "category": "waterparks-family",
        "category_label": "Water Parks & Family",
        "collections": "waterparks-family,city-landmarks",
        "duration": "half-day",
        "duration_hours": "2",
        "duration_label": "⏱️ 2 Hours",
        "tour_type": "onsite",
        "tour_type_label": "Entry Ticket",
        "styles": "family,couples",
        "price": "450",
        "price_display": "THB 450",
        "price_unit": "Price Per Person",
        "highlights": [
            "Over 140 interactive photorealistic 3D trompe-l'œil murals",
            "6 themed zones: Underwater, Safari, Classic Art, Dinosaur & Fantasy",
            "Download companion AR app for animated video special effects",
            "Fully air-conditioned 5,800-sq.m gallery in North Pattaya"
        ],
        "enquiry_param": "Art+in+Paradise+Pattaya+Tickets"
    },
    {
        "id": "pat-15",
        "name": "ATV Off-Road Adventure Pattaya",
        "link": "atv_off_road_adventure_pattaya.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_atv_off_road_adventure.webp",
        "alt": "ATV off-road quad biking tour Pattaya",
        "ribbon": "🏍️ Adrenaline Trails",
        "category": "adventure-outdoor",
        "category_label": "Adventure & Outdoors",
        "collections": "adventure-outdoor",
        "duration": "half-day",
        "duration_hours": "2.5",
        "duration_label": "⏱️ 2–3 Hours",
        "tour_type": "guided",
        "tour_type_label": "Guided Adventure",
        "styles": "adventure",
        "price": "2500",
        "price_display": "THB 2,500",
        "price_unit": "Price Per Person",
        "highlights": [
            "Conquer rugged backcountry trails on automatic 300cc/450cc quad bikes",
            "Ride through jungle tracks, mud ruts, water splashes & plantations",
            "Scenic hilltop lookout stop with panoramic coastal countryside views",
            "Practice track session, full safety gear & hotel transfers included"
        ],
        "enquiry_param": "ATV+Off-Road+Adventure+Pattaya"
    },
    {
        "id": "pat-16",
        "name": "Khao Chi Chan & Wat Yansangwararam Tour",
        "link": "khao_chi_chan_and_wat_yan_tour.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_khao_chi_chan_buddha_mountain.webp",
        "alt": "Khao Chi Chan Buddha Mountain laser carving Pattaya",
        "ribbon": "🏔️ Laser Buddha Mountain",
        "category": "temples-culture",
        "category_label": "Temples & Culture",
        "collections": "temples-culture,city-landmarks",
        "duration": "half-day",
        "duration_hours": "4.5",
        "duration_label": "⏱️ 4–5 Hours",
        "tour_type": "guided",
        "tour_type_label": "Cultural Tour",
        "styles": "culture",
        "price": "1450",
        "price_display": "THB 1,450",
        "price_unit": "Price Per Person",
        "highlights": [
            "109-meter golden laser-etched Buddha silhouette on Mount Chi Chan",
            "Serene royal monastery of Wat Yansangwararam and holy stupas",
            "Viharn Sien Chinese museum with authentic Terracotta Warrior replicas",
            "Scenic countryside drive past Silverlake vineyard valley"
        ],
        "enquiry_param": "Khao+Chi+Chan+and+Wat+Yansangwararam+Tour"
    },
    {
        "id": "pat-17",
        "name": "Pattaya City Highlights & Landmarks Tour",
        "link": "pattaya_city_landmarks_tour.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_viewpoint_big_buddha.webp",
        "alt": "Pattaya Viewpoint Pratumnak Hill and Big Buddha",
        "ribbon": "🌅 Best Orientation",
        "category": "city-landmarks",
        "category_label": "City Tours & Landmarks",
        "collections": "city-landmarks,temples-culture",
        "duration": "half-day",
        "duration_hours": "3.5",
        "duration_label": "⏱️ 3–4 Hours",
        "tour_type": "guided",
        "tour_type_label": "Guided Sightseeing",
        "styles": "city,culture",
        "price": "850",
        "price_display": "THB 850",
        "price_unit": "Price Per Person",
        "highlights": [
            "Postcard panorama over Pattaya Crescent Bay from Pratumnak Hill",
            "Climb the dragon staircase to 18-meter Golden Big Buddha (Wat Phra Yai)",
            "Scenic drive along Beach Road and Pattaya bay promenade",
            "Thematic dark ride experience at World Gems Museum"
        ],
        "enquiry_param": "Pattaya+City+Highlights+and+Landmarks+Tour"
    },
    {
        "id": "pat-18",
        "name": "Koh Larn Private Speedboat Charter",
        "link": "koh_larn_private_speedboat_tour.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_koh_larn_private_speedboat.webp",
        "alt": "Koh Larn private speedboat charter Pattaya",
        "ribbon": "🛥️ VIP Private Boat",
        "category": "coral-island",
        "category_label": "Coral Island & Marine",
        "collections": "coral-island,cruises-boats",
        "duration": "full-day",
        "duration_hours": "5",
        "duration_label": "⏱️ 4–6 Hours",
        "tour_type": "private",
        "tour_type_label": "Private Boat Charter",
        "styles": "beach,private",
        "price": "7500",
        "price_display": "THB 7,500",
        "price_unit": "Per Boat (Up to 6 Pax)",
        "highlights": [
            "Exclusive twin-engine private speedboat charter for your party",
            "Total flexibility to choose secluded beaches (Tien, Samae, Monkey Beach)",
            "Complimentary snorkeling masks, life vests & ice box on board",
            "Fast 15-minute crossing without waiting for group tour crowds"
        ],
        "enquiry_param": "Koh+Larn+Private+Speedboat+Charter"
    },
    {
        "id": "pat-19",
        "name": "Pattaya Sunset Catamaran Cruise & Snorkel",
        "link": "pattaya_sunset_catamaran_cruise.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_sunset_catamaran_cruise.webp",
        "alt": "Pattaya sunset catamaran cruise Ocean Marina",
        "ribbon": "⛵ Luxury Catamaran",
        "category": "cruises-boats",
        "category_label": "Cruises & Boat Tours",
        "collections": "cruises-boats,coral-island",
        "duration": "half-day",
        "duration_hours": "4.5",
        "duration_label": "⏱️ 4–5 Hours",
        "tour_type": "shared",
        "tour_type_label": "Sailing Cruise",
        "styles": "beach,couples",
        "price": "2400",
        "price_display": "THB 2,400",
        "price_unit": "Price Per Person",
        "highlights": [
            "Sail from Ocean Marina Yacht Club on a 50-ft luxury sailing catamaran",
            "Snorkel around crystal-clear reefs of uninhabited Koh Phai island",
            "Delicious onboard barbecue seafood buffet dinner included",
            "Spacious bow trampoline sun nets & golden hour sunset views"
        ],
        "enquiry_param": "Pattaya+Sunset+Catamaran+Cruise"
    },
    {
        "id": "pat-20",
        "name": "Scuba Diving & Snorkeling Day Trip",
        "link": "scuba_diving_and_snorkeling_pattaya.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_scuba_diving_snorkeling.webp",
        "alt": "Pattaya scuba diving and coral reef snorkeling day trip",
        "ribbon": "🤿 2 Open-Water Dives",
        "category": "adventure-outdoor",
        "category_label": "Adventure & Outdoors",
        "collections": "adventure-outdoor,cruises-boats",
        "duration": "full-day",
        "duration_hours": "6.5",
        "duration_label": "⏱️ Full Day (6–7 Hrs)",
        "tour_type": "guided",
        "tour_type_label": "Full Day Boat Trip",
        "styles": "adventure,beach",
        "price": "3100",
        "price_display": "THB 3,100",
        "price_unit": "Per Certified Diver",
        "highlights": [
            "Full-day boat excursion visiting Pattaya's Near or Far Islands",
            "2 open-water dives with certified PADI Divemasters (max 4 per guide)",
            "Explore famous naval shipwrecks (HTMS Khram) and coral reefs",
            "Hot cooked Thai buffet lunch, fruit, refreshments & full scuba gear"
        ],
        "enquiry_param": "Pattaya+Scuba+Diving+and+Snorkeling+Trip"
    },
    {
        "id": "pat-21",
        "name": "HarborLand Indoor Playground Pattaya",
        "link": "harborland_pattaya_tickets.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_harborland_indoor_playground.webp",
        "alt": "HarborLand Pattaya indoor playground children slides",
        "ribbon": "🏰 Mega Indoor Play",
        "category": "waterparks-family",
        "category_label": "Water Parks & Family",
        "collections": "waterparks-family",
        "duration": "half-day",
        "duration_hours": "3",
        "duration_label": "⏱️ 3–4 Hours",
        "tour_type": "onsite",
        "tour_type_label": "Playground Pass",
        "styles": "family",
        "price": "580",
        "price_display": "THB 580",
        "price_unit": "Per Child",
        "highlights": [
            "Asia's premier indoor playground built to European safety standard EN1176",
            "Multi-tier climbing towers, extreme spiral drop slides & ball cannons",
            "Dedicated Little Land toddler area for young children under 100cm",
            "Fully air-conditioned family haven inside Harbor Pattaya Shopping Mall"
        ],
        "enquiry_param": "HarborLand+Pattaya+Playground+Tickets"
    },
    {
        "id": "pat-22",
        "name": "Pattaya Championship Golf Package",
        "link": "pattaya_golf_package_with_transfers.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_golf_championship.webp",
        "alt": "Pattaya Championship Golf Course fairways Siam Country Club",
        "ribbon": "⛳ 18-Hole Championship",
        "category": "golf-leisure",
        "category_label": "Golf & Leisure",
        "collections": "golf-leisure,adventure-outdoor",
        "duration": "full-day",
        "duration_hours": "5.5",
        "duration_label": "⏱️ 5–6 Hours (18 Holes)",
        "tour_type": "private",
        "tour_type_label": "18 Holes + Private Van",
        "styles": "sports,luxury",
        "price": "4800",
        "price_display": "THB 4,800",
        "price_unit": "Price Per Golfer",
        "highlights": [
            "Guaranteed morning tee time at top-ranked championship courses",
            "Options: Siam Country Club (LPGA host), Chee Chan or Phoenix Gold",
            "Dedicated private VIP minivan hotel transfers with golf bag space",
            "Personal caddy service and motorized golf cart (buggy) included"
        ],
        "enquiry_param": "Pattaya+Championship+Golf+Package"
    },
    {
        "id": "pat-23",
        "name": "Dolphin Show with Tiger Park Combo",
        "link": "dolphin_show_with_tiger_park.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_dolphin_show_with_tiger_park.webp",
        "alt": "Dolphin show and Tiger Park Pattaya combination tour",
        "ribbon": "🐬 Family Favorite",
        "category": "private-combos",
        "category_label": "Private & Combination Tours",
        "collections": "gardens-wildlife,waterparks-family",
        "duration": "half-day",
        "duration_hours": "4",
        "duration_label": "⏱️ 4 Hours",
        "tour_type": "shared",
        "tour_type_label": "Combo Tour",
        "styles": "family,wildlife",
        "price": "1750",
        "price_display": "THB 1,750",
        "price_unit": "Price Per Person",
        "highlights": [
            "Pattaya Dolphinarium acrobatic marine mammal performance",
            "Admission to Tiger Park Pattaya with elevated viewing walkways",
            "Round-trip air-conditioned hotel transfers from central Pattaya",
            "Optional upgrades for direct tiger cub interaction photo sessions"
        ],
        "enquiry_param": "Dolphin+Show+with+Tiger+Park+Pattaya"
    },
    {
        "id": "pat-24",
        "name": "Pattaya City Tour with Colosseum Show",
        "link": "pattaya_city_tour_with_colosseum_show.html",
        "img": "../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_city_tour_with_colosseum_show.webp",
        "alt": "Pattaya city viewpoint and Colosseum cabaret show combination",
        "ribbon": "🌟 City & Show Combo",
        "category": "private-combos",
        "category_label": "Private & Combination Tours",
        "collections": "city-landmarks,shows-nightlife",
        "duration": "full-day",
        "duration_hours": "7",
        "duration_label": "⏱️ Full Day (7 Hrs)",
        "tour_type": "guided",
        "tour_type_label": "Full Day Combo",
        "styles": "culture,city",
        "price": "1850",
        "price_display": "THB 1,850",
        "price_unit": "Price Per Person",
        "highlights": [
            "Daytime city tour covering Pratumnak Hill & Big Buddha Temple",
            "Drive along Pattaya Beach Road and visit World Gems Museum",
            "Seamless transfer to Colosseum Theatre for spectacular evening show",
            "VIP reserved theatre seats and full round-trip transfers included"
        ],
        "enquiry_param": "Pattaya+City+Tour+with+Colosseum+Show"
    }
]

FAQS_DATA = [
    (
        "What are the best sightseeing attractions to visit in Pattaya?",
        "Pattaya's premier sightseeing attractions include the monumental all-wood Sanctuary of Truth Museum, the award-winning 600-acre Nong Nooch Tropical Garden, Coral Island (Koh Larn) day tours, world-class water parks (Ramayana and Columbia Pictures Aquaverse), dazzling evening cabarets (Alcazar, Tiffany's, and Colosseum), live bouts at Max Muay Thai Stadium, ethical encounters at Pattaya Elephant Sanctuary, and family visits to Khao Kheow Open Zoo to see Moo Deng."
    ),
    (
        "Can I book individual Pattaya sightseeing tours without a holiday package?",
        "Yes, absolutely. Trippovention operates an enquiry-led service supporting standalone bookings for individual Pattaya day tours, attraction admission tickets, island speedboats, evening cabaret shows, and private transport without requiring you to purchase a full multi-day package."
    ),
    (
        "How do I get to Coral Island (Koh Larn) from Pattaya?",
        "Coral Island is situated 7.5 kilometers off Pattaya's coast. You can join our scheduled speedboat day tours (which include hotel pickup, safety life vests, and beach lunch) or charter a private speedboat from Bali Hai Pier for complete schedule flexibility and direct access to secluded beaches."
    ),
    (
        "What is the dress code for Sanctuary of Truth and Big Buddha Hill?",
        "Both the Sanctuary of Truth Museum and Wat Phra Yai (Big Buddha Hill) are sacred cultural and religious monuments. Visitors must wear modest attire covering both shoulders and knees. Sleeveless tops, short skirts, swimwear, and revealing clothing are strictly prohibited. Sarongs are available for hire at the entrance."
    ),
    (
        "Are hotel transfers included in Pattaya sightseeing activities?",
        "Most of our guided day tours (such as Coral Island, Khao Kheow Zoo, Elephant Sanctuary, and City Highlights) include complimentary round-trip transfers from central Pattaya hotels. Standalone attraction tickets (such as Ramayana, Aquaverse, or Underwater World) are admission-only, though private or shared round-trip transfers can be added on request."
    ),
    (
        "Which water park in Pattaya is better: Ramayana or Columbia Pictures Aquaverse?",
        "Both are world-class! Ramayana Water Park is Thailand's largest water park, set in beautiful natural mountains with 21 massive slides and crystal-clear freshwater springs. Columbia Pictures Aquaverse offers unique movie-themed attractions (Ghostbusters, Jumanji, Hotel Transylvania) and an outdoor cinema wave pool. Families with movie fans love Aquaverse, while slide purists often prefer Ramayana."
    ),
    (
        "Is Alcazar or Tiffany's Show better for cabaret entertainment?",
        "Both offer world-class theatrical entertainment with lavish feather costumes, high-tech stages, and talented casts. Tiffany's is the historic pioneer (operating since 1974) with a classic Broadway and imperial Thai aesthetic. Alcazar is famous for high-energy modern pop sets and dynamic international acts. Colosseum provides the newest, largest Roman amphitheatre setting with steep tiered seating."
    ),
    (
        "Are ethical elephant experiences available in Pattaya?",
        "Yes! Trippovention strictly partners with genuine ethical sanctuaries in Pattaya that enforce a 100% no-riding policy. Guests prepare nutrient fruit balls, feed rescued elephants by hand, and join them for a cooling mud bath and freshwater wash."
    ),
    (
        "Can Trippovention customize a private sightseeing itinerary in Pattaya?",
        "Yes, our destination team excels at tailoring private arrangements. Whether you need a private VIP minivan for family sightseeing, a customized golf holiday, or a private catamaran cruise for a celebration, we can design the perfect itinerary."
    ),
    (
        "How do I check availability and request a quotation for Pattaya tours?",
        "Simply click 'Enquire Now' on any experience card, complete our brief contact form, or message our team directly via WhatsApp (+66 94 693 4392). Share your travel dates, group size, and preferred sights, and our travel specialists will confirm availability and current promotional rates."
    )
]

def generate_catalogue_html():
    # 1. Build Cards HTML
    cards_html_list = []
    for exp in EXPERIENCES:
        highlights_items = "".join([f"                  <li>{h}</li>\n" for h in exp["highlights"]])
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
                <ul class="highlights-list">
{highlights_items}                </ul>
                <div class="price-row mt-auto">
                  <span class="price-label">{exp['price_unit']}</span>
                  <span class="price">{exp['price_display']}</span>
                </div>
                <div class="card-actions-grid mt-16">
                  <a class="btn btn-outline" href="{exp['link']}">View Details</a>
                  <a
                    class="btn btn-primary"
                    href="../../../contact.html?destination=pattaya&tour={exp['enquiry_param']}"
                    >Enquire Now →</a
                  >
                </div>
              </div>
            </article>"""
        cards_html_list.append(card_html)
    
    all_cards_str = "\n".join(cards_html_list)

    # 2. Build FAQs HTML
    faqs_html_list = []
    for idx, (q, a) in enumerate(FAQS_DATA):
        open_attr = " open" if idx == 0 else ""
        faqs_html_list.append(f"""            <details class="faq-item"{open_attr}>
              <summary class="faq-question"><span>{q}</span><span class="faq-chevron" aria-hidden="true">▾</span></summary>
              <div class="faq-answer"><p>{a}</p></div>
            </details>""")
    all_faqs_str = "\n".join(faqs_html_list)

    # 3. Build FAQ Schema
    faq_schema_items = []
    for q, a in FAQS_DATA:
        faq_schema_items.append(f"""          {{
            "@type": "Question",
            "name": "{q}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{a}"
            }}
          }}""")
    faq_schema_str = ",\n".join(faq_schema_items)

    # Full HTML template
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
    <title>Pattaya Sightseeing Tours &amp; Attractions | Trippovention</title>
    <meta
      name="description"
      content="Explore Pattaya sightseeing tours, Coral Island trips, water parks, tropical gardens and cabaret shows. Enquire with Trippovention for current offers."
    />
    <meta name="author" content="Trippovention" />

    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://trippovention.co.th/packages/thailand/pattaya/sightseeing.html" />
    <meta property="og:title" content="Pattaya Sightseeing Tours &amp; Attractions | Trippovention" />
    <meta
      property="og:description"
      content="Explore Pattaya sightseeing tours, Coral Island trips, water parks, tropical gardens and cabaret shows. Enquire with Trippovention for current offers."
    />
    <meta property="og:image" content="https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_sanctuary_of_truth_pattaya.webp" />

    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="https://trippovention.co.th/packages/thailand/pattaya/sightseeing.html" />
    <meta property="twitter:title" content="Pattaya Sightseeing Tours &amp; Attractions | Trippovention" />
    <meta
      property="twitter:description"
      content="Explore Pattaya sightseeing tours, Coral Island trips, water parks, tropical gardens and cabaret shows. Enquire with Trippovention for current offers."
    />
    <meta property="twitter:image" content="https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_sanctuary_of_truth_pattaya.webp" />

    <link rel="canonical" href="https://trippovention.co.th/packages/thailand/pattaya/sightseeing.html" />
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
        "name": "Pattaya Sightseeing Tours & Attractions",
        "description": "Comprehensive catalogue of Pattaya sightseeing tours, Coral Island trips, water parks, tropical gardens, cabaret shows, and ethical wildlife experiences.",
        "url": "https://trippovention.co.th/packages/thailand/pattaya/sightseeing.html",
        "containedInPlace": {{
          "@type": "Country",
          "name": "Thailand"
        }},
        "touristType": ["Coastal Sightseeing", "Family Holidays", "Island Tours", "Cabaret Entertainment", "Cultural Heritage", "Water Parks"]
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
            "name": "Pattaya",
            "item": "https://trippovention.co.th/packages/thailand/pattaya/"
          }},
          {{
            "@type": "ListItem",
            "position": 5,
            "name": "Sightseeing",
            "item": "https://trippovention.co.th/packages/thailand/pattaya/sightseeing.html"
          }}
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
                    url('../../../assets/images/packages/thailand/pattaya/sightseeingoptions/hero_sanctuary_of_truth_pattaya.webp') center/cover no-repeat;
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
        background: none;
        border: 1px dashed var(--border-color);
        color: var(--text-muted);
        padding: 9px 14px;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
        margin-top: 18px;
      }}
      .reset-filters-btn:hover {{
        border-color: var(--orange);
        color: var(--orange);
      }}

      /* Results Status Bar */
      .results-status-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 22px;
        font-size: 0.95rem;
        color: var(--text-secondary);
      }}
      .results-count-bold {{
        font-weight: 700;
        color: var(--text-primary);
      }}

      /* Cards Grid & Cards Styling */
      .sightseeing-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
        gap: 26px;
      }}
      .sightseeing-card {{
        display: flex;
        flex-direction: column;
        border-radius: 14px;
        overflow: hidden;
        background: var(--bg-primary);
        border: 1px solid var(--border-color);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
      }}
      .sightseeing-card:hover {{
        transform: translateY(-4px);
        box-shadow: var(--shadow-medium);
        border-color: rgba(214, 128, 78, 0.35);
      }}
      .sightseeing-card .img-wrap {{
        position: relative;
        aspect-ratio: 16 / 9;
        overflow: hidden;
        background: var(--border-light);
      }}
      .sightseeing-card .img-wrap img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.35s ease;
      }}
      .sightseeing-card:hover .img-wrap img {{
        transform: scale(1.05);
      }}
      .sightseeing-card .ribbon {{
        position: absolute;
        top: 12px;
        right: 12px;
        background: rgba(15, 23, 42, 0.85);
        color: #fff;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.76rem;
        font-weight: 600;
        backdrop-filter: blur(4px);
      }}
      .sightseeing-card .body {{
        padding: 20px;
        display: flex;
        flex-direction: column;
        flex: 1;
      }}
      .card-meta-row {{
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-bottom: 10px;
      }}
      .card-tag {{
        font-size: 0.72rem;
        padding: 2px 8px;
        border-radius: 4px;
        background: var(--bg-secondary);
        color: var(--text-secondary);
        font-weight: 500;
        border: 1px solid var(--border-color);
      }}
      .card-tag.highlight-tag {{
        background: rgba(214, 128, 78, 0.12);
        color: var(--orange);
        border-color: rgba(214, 128, 78, 0.25);
        font-weight: 600;
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
      .highlights-list {{
        list-style: none;
        padding: 0;
        margin: 0 0 16px 0;
        font-size: 0.84rem;
        color: var(--text-muted);
        line-height: 1.55;
      }}
      .highlights-list li {{
        position: relative;
        padding-left: 16px;
        margin-bottom: 4px;
      }}
      .highlights-list li::before {{
        content: "•";
        color: var(--orange);
        position: absolute;
        left: 2px;
        font-weight: bold;
      }}
      .sightseeing-card .price-row {{
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        padding-top: 12px;
        border-top: 1px solid var(--border-light);
      }}
      .sightseeing-card .price-label {{
        font-size: 0.78rem;
        color: var(--text-muted);
      }}
      .sightseeing-card .price {{
        font-size: 1.18rem;
        font-weight: 700;
        color: var(--orange);
      }}
      .card-actions-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
      }}
      .card-actions-grid .btn {{
        padding: 8px 12px;
        font-size: 0.82rem;
        text-align: center;
        white-space: nowrap;
      }}

      /* Empty State */
      .no-results-box {{
        text-align: center;
        padding: 60px 20px;
        background: var(--bg-secondary);
        border-radius: 16px;
        border: 1px dashed var(--border-color);
        display: none;
      }}
      .no-results-box h3 {{
        font-size: 1.25rem;
        margin-bottom: 8px;
      }}
      .no-results-box p {{
        color: var(--text-muted);
        max-width: 480px;
        margin: 0 auto 18px;
      }}

      @media (max-width: 768px) {{
        .secondary-filters-bar {{
          display: none;
        }}
        .secondary-filters-bar.open {{
          display: grid;
        }}
        .filter-toggle-mobile-btn {{
          display: inline-flex;
        }}
        .sightseeing-grid {{
          grid-template-columns: 1fr;
        }}
        .collections-grid {{
          gap: 10px;
        }}
        .collection-pill-card {{
          flex: 1 1 calc(50% - 10px);
          max-width: calc(50% - 10px);
          padding: 12px 10px;
        }}
      }}
    </style>
  </head>

  <body>
    <a href="#main" class="skip-link" aria-label="Skip to main content" id="skip-link">
      Skip to main content
    </a>

    <!-- Top Navigation -->
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
              <a href="index.html">Pattaya</a>
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
          <span class="badge" style="background: rgba(214, 128, 78, 0.9); color: #fff; margin-bottom: 12px; display: inline-block;">
            Extended Sightseeing Catalogue
          </span>
          <h1>Discover the Best of Pattaya</h1>
          <p>
            Explore Pattaya's premier attractions, world-famous cabaret shows, Coral Island speedboat excursions, colossal water parks, ethical elephant sanctuaries, and panoramic city lookouts.
          </p>
          <div class="hero-actions">
            <a href="#catalogueSection" class="btn btn-primary">Browse All Experiences ({len(EXPERIENCES)})</a>
            <a href="index.html" class="btn btn-outline" style="border-color: rgba(255,255,255,0.7); color: #fff;">
              ← Back to Pattaya Packages
            </a>
          </div>
        </div>
      </header>

      <!-- Curated Collections Bar (Center-Aligned Grid) -->
      <section class="collections-section" aria-label="Curated Pattaya Collections">
        <div class="container">
          <div class="section-title text-center mb-20">
            <h2 style="font-size: 1.45rem;">Curated Pattaya Collections</h2>
            <p class="subtitle" style="font-size: 0.92rem; margin-bottom: 0;">Quickly filter by experience theme and travel style</p>
          </div>
          <div class="collections-grid">
            <div class="collection-pill-card active" data-collection="all" role="button" tabindex="0">
              <div class="col-icon">⭐</div>
              <div class="col-title">All Highlights</div>
              <div class="col-sub">24 Experiences</div>
            </div>
            <div class="collection-pill-card" data-collection="city-landmarks" role="button" tabindex="0">
              <div class="col-icon">🏙️</div>
              <div class="col-title">City Highlights</div>
              <div class="col-sub">Viewpoints & Temples</div>
            </div>
            <div class="collection-pill-card" data-collection="temples-culture" role="button" tabindex="0">
              <div class="col-icon">🛕</div>
              <div class="col-title">Sanctuary & Culture</div>
              <div class="col-sub">All-Wood Temple & Arts</div>
            </div>
            <div class="collection-pill-card" data-collection="coral-island" role="button" tabindex="0">
              <div class="col-icon">🏝️</div>
              <div class="col-title">Coral Island</div>
              <div class="col-sub">Koh Larn Speedboats</div>
            </div>
            <div class="collection-pill-card" data-collection="cruises-boats" role="button" tabindex="0">
              <div class="col-icon">⛵</div>
              <div class="col-title">Cruises & Boats</div>
              <div class="col-sub">Catamarans & Yachts</div>
            </div>
            <div class="collection-pill-card" data-collection="waterparks-family" role="button" tabindex="0">
              <div class="col-icon">🌊</div>
              <div class="col-title">Water Parks & Fun</div>
              <div class="col-sub">Ramayana & Aquaverse</div>
            </div>
            <div class="collection-pill-card" data-collection="gardens-wildlife" role="button" tabindex="0">
              <div class="col-icon">🌿</div>
              <div class="col-title">Wildlife & Gardens</div>
              <div class="col-sub">Nong Nooch & Elephants</div>
            </div>
            <div class="collection-pill-card" data-collection="shows-nightlife" role="button" tabindex="0">
              <div class="col-icon">🎭</div>
              <div class="col-title">Cabaret & Shows</div>
              <div class="col-sub">Alcazar, Tiffany & Muay Thai</div>
            </div>
            <div class="collection-pill-card" data-collection="adventure-outdoor" role="button" tabindex="0">
              <div class="col-icon">🏎️</div>
              <div class="col-title">Adventure & Golf</div>
              <div class="col-sub">ATV, Scuba & 18 Holes</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Main Catalogue Section -->
      <section class="section" id="catalogueSection">
        <div class="container">
          <!-- Filter Toolbar -->
          <div class="filter-toolbar">
            <!-- Search Row -->
            <div class="search-box-row">
              <div class="search-input-wrap">
                <input
                  type="text"
                  id="pattayaSearchInput"
                  placeholder="Search Pattaya tours, attractions, shows, water parks..."
                  aria-label="Search Pattaya experiences"
                />
                <button type="button" class="search-clear-btn" id="searchClearBtn" aria-label="Clear search">✕</button>
              </div>
              <button type="button" class="filter-toggle-mobile-btn" id="filterToggleMobileBtn" aria-expanded="false">
                <span>⚙️ Filters</span>
              </button>
            </div>

            <!-- Category Pills Navigation -->
            <div class="category-pills-wrap" role="tablist" aria-label="Experience Categories">
              <button type="button" class="cat-pill active" data-category="all">
                All <span class="pill-count">24</span>
              </button>
              <button type="button" class="cat-pill" data-category="city-landmarks">
                City Tours &amp; Landmarks <span class="pill-count">2</span>
              </button>
              <button type="button" class="cat-pill" data-category="temples-culture">
                Temples &amp; Culture <span class="pill-count">2</span>
              </button>
              <button type="button" class="cat-pill" data-category="coral-island">
                Coral Island &amp; Marine <span class="pill-count">2</span>
              </button>
              <button type="button" class="cat-pill" data-category="cruises-boats">
                Cruises &amp; Boat Tours <span class="pill-count">1</span>
              </button>
              <button type="button" class="cat-pill" data-category="waterparks-family">
                Water Parks &amp; Family <span class="pill-count">5</span>
              </button>
              <button type="button" class="cat-pill" data-category="gardens-wildlife">
                Gardens &amp; Wildlife <span class="pill-count">3</span>
              </button>
              <button type="button" class="cat-pill" data-category="shows-nightlife">
                Shows &amp; Nightlife <span class="pill-count">5</span>
              </button>
              <button type="button" class="cat-pill" data-category="adventure-outdoor">
                Adventure &amp; Outdoors <span class="pill-count">2</span>
              </button>
              <button type="button" class="cat-pill" data-category="golf-leisure">
                Golf &amp; Leisure <span class="pill-count">1</span>
              </button>
              <button type="button" class="cat-pill" data-category="private-combos">
                Private &amp; Combo Tours <span class="pill-count">2</span>
              </button>
            </div>

            <!-- Secondary Filters Bar -->
            <div class="secondary-filters-bar" id="secondaryFiltersBar">
              <div class="filter-group">
                <label for="filterDuration">Duration</label>
                <select id="filterDuration" class="filter-select">
                  <option value="all">Any Duration</option>
                  <option value="half-day">Half Day (≤ 4 Hours)</option>
                  <option value="full-day">Full Day (> 4 Hours)</option>
                </select>
              </div>

              <div class="filter-group">
                <label for="filterTourType">Tour Format</label>
                <select id="filterTourType" class="filter-select">
                  <option value="all">All Formats</option>
                  <option value="guided">Guided Tour</option>
                  <option value="shared">Shared (SIC)</option>
                  <option value="private">Private Charter</option>
                  <option value="onsite">Admission Ticket</option>
                </select>
              </div>

              <div class="filter-group">
                <label for="filterStyle">Travel Style</label>
                <select id="filterStyle" class="filter-select">
                  <option value="all">All Styles</option>
                  <option value="beach">Island &amp; Beach</option>
                  <option value="culture">Temples &amp; Culture</option>
                  <option value="family">Family &amp; Kids</option>
                  <option value="adventure">Active Adventure</option>
                  <option value="nightlife">Shows &amp; Cabaret</option>
                </select>
              </div>

              <div class="filter-group">
                <label for="filterSort">Sort By</label>
                <select id="filterSort" class="filter-select">
                  <option value="recommended">Recommended</option>
                  <option value="price-low">Price: Low to High</option>
                  <option value="price-high">Price: High to Low</option>
                  <option value="duration-short">Duration: Shortest</option>
                </select>
              </div>

              <div class="filter-group text-center">
                <button type="button" class="reset-filters-btn" id="resetFiltersBtn">
                  ↺ Reset Filters
                </button>
              </div>
            </div>
          </div>

          <!-- Results Status Row -->
          <div class="results-status-bar">
            <div>
              Showing <span class="results-count-bold" id="visibleCount">{len(EXPERIENCES)}</span> of
              <span class="results-count-bold">{len(EXPERIENCES)}</span> verified Pattaya experiences
            </div>
            <div id="activeFilterBadge" style="font-size: 0.85rem; color: var(--orange); font-weight: 600;"></div>
          </div>

          <!-- Cards Grid -->
          <div class="sightseeing-grid" id="sightseeingGrid">
{all_cards_str}
          </div>

          <!-- Empty State -->
          <div class="no-results-box" id="noResultsBox">
            <div style="font-size: 40px; margin-bottom: 12px;">🔍</div>
            <h3>No Matching Pattaya Experiences Found</h3>
            <p>
              We couldn't find any activities matching your active filters. Try adjusting your search query, selecting "All" categories, or resetting filters.
            </p>
            <button type="button" class="btn btn-primary" id="resetEmptyBtn">Reset All Filters</button>
          </div>
        </div>
      </section>

      <!-- FAQ Section (AEO & Answer Engine Optimization) -->
      <section class="section alt faq-section" id="faq">
        <div class="container">
          <div class="section-title text-center">
            <h2>Frequently Asked Questions</h2>
            <p class="subtitle">Everything you need to know about sightseeing in Pattaya</p>
          </div>
          <div class="faq-container">
{all_faqs_str}
          </div>
        </div>
      </section>

      <!-- CTA Contact Section -->
      <section class="section cta">
        <div class="container">
          <div class="section-title text-center">
            <h2 class="text-white">Plan Your Custom Pattaya Sightseeing Itinerary</h2>
            <p class="subtitle text-white-90">
              Connect with our local destination team for current offers, group discounts, and private arrangements.
            </p>
          </div>
          <div class="text-center">
            <a
              class="btn btn-lg ghost"
              href="../../../contact.html?destination=pattaya&type=sightseeing"
              >📞 Request Custom Quote</a
            >
            <a
              class="btn btn-lg ghost ml-16"
              href="https://wa.me/66946934392?text=Hello,%20I%20would%20like%20to%20enquire%20about%20Pattaya%20sightseeing%20tours"
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
              <a href="sightseeing.html">Pattaya Sightseeing Catalogue</a><br />
              <a href="index.html">Pattaya Tour Packages</a><br />
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
        const searchInput = document.getElementById("pattayaSearchInput");
        const clearBtn = document.getElementById("searchClearBtn");
        const categoryPills = document.querySelectorAll(".cat-pill");
        const collectionCards = document.querySelectorAll(".collection-pill-card");
        const durationSelect = document.getElementById("filterDuration");
        const tourTypeSelect = document.getElementById("filterTourType");
        const styleSelect = document.getElementById("filterStyle");
        const sortSelect = document.getElementById("filterSort");
        const resetBtn = document.getElementById("resetFiltersBtn");
        const resetEmptyBtn = document.getElementById("resetEmptyBtn");
        const mobileToggleBtn = document.getElementById("filterToggleMobileBtn");
        const secondaryBar = document.getElementById("secondaryFiltersBar");
        const grid = document.getElementById("sightseeingGrid");
        const cards = Array.from(grid.querySelectorAll(".sightseeing-card"));
        const visibleCountSpan = document.getElementById("visibleCount");
        const noResultsBox = document.getElementById("noResultsBox");

        let activeCategory = "all";
        let activeCollection = "all";

        // Filter Evaluation Function
        function filterCards() {{
          const query = searchInput.value.trim().toLowerCase();
          const selectedDuration = durationSelect.value;
          const selectedTourType = tourTypeSelect.value;
          const selectedStyle = styleSelect.value;
          const selectedSort = sortSelect.value;

          clearBtn.style.display = query ? "block" : "none";

          let visibleList = [];

          cards.forEach((card) => {{
            const name = card.getAttribute("data-name") || "";
            const category = card.getAttribute("data-category") || "";
            const collections = (card.getAttribute("data-collections") || "").split(",");
            const duration = card.getAttribute("data-duration") || "";
            const tourType = card.getAttribute("data-tour-type") || "";
            const styles = (card.getAttribute("data-styles") || "").split(",");
            const cardText = card.textContent.toLowerCase();

            let matches = true;

            // Search query
            if (query && !name.includes(query) && !cardText.includes(query)) {{
              matches = false;
            }}

            // Category Pill Filter
            if (activeCategory !== "all" && category !== activeCategory) {{
              matches = false;
            }}

            // Curated Collection Filter
            if (activeCollection !== "all" && !collections.includes(activeCollection)) {{
              matches = false;
            }}

            // Duration Filter
            if (selectedDuration !== "all" && duration !== selectedDuration) {{
              matches = false;
            }}

            // Tour Type Filter
            if (selectedTourType !== "all" && tourType !== selectedTourType) {{
              matches = false;
            }}

            // Style Filter
            if (selectedStyle !== "all" && !styles.includes(selectedStyle)) {{
              matches = false;
            }}

            if (matches) {{
              card.style.display = "flex";
              visibleList.push(card);
            }} else {{
              card.style.display = "none";
            }}
          }});

          // Sorting
          if (selectedSort === "price-low") {{
            visibleList.sort((a, b) => parseFloat(a.dataset.price) - parseFloat(b.dataset.price));
          }} else if (selectedSort === "price-high") {{
            visibleList.sort((a, b) => parseFloat(b.dataset.price) - parseFloat(a.dataset.price));
          }} else if (selectedSort === "duration-short") {{
            visibleList.sort((a, b) => parseFloat(a.dataset.durationHours) - parseFloat(b.dataset.durationHours));
          }}

          // Re-append sorted visible cards
          visibleList.forEach((c) => grid.appendChild(c));

          // Update Status
          visibleCountSpan.textContent = visibleList.length;
          noResultsBox.style.display = visibleList.length === 0 ? "block" : "none";
        }}

        // Event Listeners
        searchInput.addEventListener("input", filterCards);
        clearBtn.addEventListener("click", () => {{
          searchInput.value = "";
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
    print(f"Successfully generated Pattaya Sightseeing Catalogue at: {CATALOGUE_PATH}")
    print(f"Total experiences included: {len(EXPERIENCES)}")
    print(f"Total FAQs included: {len(FAQS_DATA)}")

if __name__ == "__main__":
    main()
