#!/usr/bin/env python3
"""
Generate the Bangkok Sightseeing Catalogue Page:
docs/packages/thailand/bangkok/sightseeing.html
Modeled directly on docs/packages/thailand/krabi/sightseeing.html.
Preserves design system, typography, colors, centered curated collections,
search/filtering engine, 24 experiences, 10 FAQs, and JSON-LD schemas.
"""

import os

CATALOGUE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs", "packages", "thailand", "bangkok", "sightseeing.html"
)

EXPERIENCES = [
    {
        "id": "bkk-01",
        "name": "Bangkok City Highlights Tour",
        "link": "full_day_bangkok_city_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_full_day_bangkok_city_tour.webp",
        "alt": "Wat Pho and Bangkok city landmarks tour",
        "ribbon": "⭐ Bestseller",
        "category": "city-tours",
        "category_label": "City Tours & Landmarks",
        "collections": "city-highlights,temples",
        "duration": "full-day",
        "duration_hours": "8",
        "duration_label": "⏱️ 8 Hours",
        "tour_type": "private",
        "tour_type_label": "Private / Guided",
        "styles": "culture,city",
        "price": "1890",
        "price_display": "THB 1,890",
        "price_unit": "Price Per Person",
        "highlights": [
            "Grand Palace & sacred Wat Phra Kaew visit",
            "Wat Pho Reclining Buddha & 91 royal chedis",
            "Chao Phraya River cross-ferry & Wat Arun view",
            "Flower Market & Bangkok Chinatown orientation"
        ],
        "enquiry_param": "Bangkok+City+Highlights+Tour"
    },
    {
        "id": "bkk-02",
        "name": "Grand Palace & Wat Phra Kaew Visit",
        "link": "grand_palace_and_wat_phra_kaew_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_grand_palace.webp",
        "alt": "Grand Palace and Wat Phra Kaew in Bangkok",
        "ribbon": "🛕 Cultural Highlight",
        "category": "temples",
        "category_label": "Temples & Royal Heritage",
        "collections": "temples,city-highlights",
        "duration": "half-day",
        "duration_hours": "4",
        "duration_label": "⏱️ 4 Hours",
        "tour_type": "guided",
        "tour_type_label": "Shared / SIC",
        "styles": "culture",
        "price": "1450",
        "price_display": "THB 1,450",
        "price_unit": "Price Per Person",
        "highlights": [
            "Ceremonial heart of the Siamese Royal Court since 1782",
            "Sacred Emerald Buddha carved from single jadeite stone",
            "Chakri Maha Prasat & Dusit Maha Prasat royal throne halls",
            "Detailed storytelling by licensed English-speaking guide"
        ],
        "enquiry_param": "Grand+Palace+and+Wat+Phra+Kaew+Tour"
    },
    {
        "id": "bkk-03",
        "name": "Wat Pho & Reclining Buddha Tour",
        "link": "wat_pho_and_reclining_buddha_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_wat_pho.webp",
        "alt": "Wat Pho Reclining Buddha temple Bangkok",
        "ribbon": "🧘 Must Visit",
        "category": "temples",
        "category_label": "Temples & Royal Heritage",
        "collections": "temples",
        "duration": "half-day",
        "duration_hours": "3",
        "duration_label": "⏱️ 3 Hours",
        "tour_type": "guided",
        "tour_type_label": "Guided Tour",
        "styles": "culture",
        "price": "950",
        "price_display": "THB 950",
        "price_unit": "Price Per Person",
        "highlights": [
            "Colossal 46-meter-long gold-leaf covered Reclining Buddha",
            "Mother-of-pearl soles illustrating 108 auspicious marks",
            "Historical birthplace of traditional Thai medical massage",
            "Four grand 42-meter royal chedis honoring Chakri kings"
        ],
        "enquiry_param": "Wat+Pho+and+Reclining+Buddha+Tour"
    },
    {
        "id": "bkk-04",
        "name": "Wat Arun – Temple of Dawn Tour",
        "link": "wat_arun_temple_of_dawn_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_wat_arun.webp",
        "alt": "Wat Arun Temple of Dawn beside Chao Phraya River",
        "ribbon": "🌅 Scenic Highlight",
        "category": "temples",
        "category_label": "Temples & Royal Heritage",
        "collections": "temples,river-cruises",
        "duration": "half-day",
        "duration_hours": "2.5",
        "duration_label": "⏱️ 2–3 Hours",
        "tour_type": "guided",
        "tour_type_label": "Guided Tour",
        "styles": "culture",
        "price": "850",
        "price_display": "THB 850",
        "price_unit": "Price Per Person",
        "highlights": [
            "Soaring 70-meter riverside Khmer-style central prang",
            "Glazed colorful Chinese porcelain floral mosaic tiles",
            "Scenic Chao Phraya River passenger ferry crossing",
            "Optional traditional Thai silk costume photoshoot"
        ],
        "enquiry_param": "Wat+Arun+Temple+of+Dawn+Tour"
    },
    {
        "id": "bkk-05",
        "name": "Bangkok Temples & Heritage Tour",
        "link": "bangkok_temples_and_heritage_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_bangkok_temples_heritage.webp",
        "alt": "Bangkok Temples and Cultural Heritage Tour",
        "ribbon": "🏛️ Top Heritage",
        "category": "temples",
        "category_label": "Temples & Royal Heritage",
        "collections": "temples,city-highlights",
        "duration": "half-day",
        "duration_hours": "4.5",
        "duration_label": "⏱️ 4–5 Hours",
        "tour_type": "shared",
        "tour_type_label": "Shared (SIC Transfers)",
        "styles": "culture",
        "price": "1650",
        "price_display": "THB 1,650",
        "price_unit": "Price Per Person",
        "highlights": [
            "Wat Traimit: World's largest 5.5-ton solid gold Buddha",
            "Wat Pho: 46-meter Reclining Buddha & ancient cloisters",
            "Wat Benchamabophit: Exquisite Italian white Carrara marble",
            "Round-trip air-conditioned hotel transfers included"
        ],
        "enquiry_param": "Bangkok+Temples+and+Heritage+Tour"
    },
    {
        "id": "bkk-06",
        "name": "King Power Mahanakhon SkyWalk",
        "link": "mahanakhon_skywalk.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_mahanakhon_skywalk.webp",
        "alt": "Mahanakhon SkyWalk glass tray 314 meters high",
        "ribbon": "🏙️ Skyline Icon",
        "category": "city-tours",
        "category_label": "City Tours & Landmarks",
        "collections": "city-highlights,night",
        "duration": "half-day",
        "duration_hours": "2.5",
        "duration_label": "⏱️ 2–3 Hours",
        "tour_type": "onsite",
        "tour_type_label": "Entry Ticket",
        "styles": "couples,city",
        "price": "880",
        "price_display": "THB 880",
        "price_unit": "Price Per Person",
        "highlights": [
            "Thailand's highest 360-degree observation deck at 314m",
            "World-famous glass tray floor suspended 78 floors high",
            "Ultra-high-speed multimedia multimedia elevator ride",
            "Spectacular golden-hour sunset and twinkling night vistas"
        ],
        "enquiry_param": "King+Power+Mahanakhon+SkyWalk"
    },
    {
        "id": "bkk-07",
        "name": "Chao Phraya River Sightseeing Cruise",
        "link": "chao_phraya_river_sightseeing_cruise.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_chao_phraya_river_cruise.webp",
        "alt": "Chao Phraya river sightseeing tourist boat",
        "ribbon": "🚢 Scenic River",
        "category": "river-cruises",
        "category_label": "River Cruises & Riverside",
        "collections": "river-cruises,city-highlights",
        "duration": "half-day",
        "duration_hours": "3",
        "duration_label": "⏱️ 2–3 Hours / All-Day",
        "tour_type": "cruise",
        "tour_type_label": "Cruise / Hop-On Pass",
        "styles": "family,city",
        "price": "650",
        "price_display": "THB 650",
        "price_unit": "Price Per Person",
        "highlights": [
            "Unlimited hop-on hop-off access across 11 riverside piers",
            "Seamless access to Wat Arun, Grand Palace, and IconSiam",
            "Open-deck panoramic views avoiding Bangkok road traffic",
            "Onboard route map and English commentary guides"
        ],
        "enquiry_param": "Chao+Phraya+River+Sightseeing+Cruise"
    },
    {
        "id": "bkk-08",
        "name": "Princess Chao Phraya Dinner Cruise",
        "link": "princess_chao_phraya_dinner_cruise.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_princess_chao_phraya_dinner_cruise.webp",
        "alt": "Princess Chao Phraya Dinner Cruise at night",
        "ribbon": "⭐ Bestseller",
        "category": "river-cruises",
        "category_label": "River Cruises & Riverside",
        "collections": "river-cruises,night",
        "duration": "sunset",
        "duration_hours": "2",
        "duration_label": "⏱️ 2 Hours (Evening)",
        "tour_type": "cruise",
        "tour_type_label": "Dinner Cruise",
        "styles": "couples,family",
        "price": "1200",
        "price_display": "THB 1,200",
        "price_unit": "Price Per Person",
        "highlights": [
            "2-hour luxury evening voyage on the River of Kings",
            "Lavish international and fresh seafood buffet dinner",
            "Live saxophonist and vocal duo performing timeless hits",
            "Illuminated night views of Wat Arun & Grand Palace"
        ],
        "enquiry_param": "Princess+Chao+Phraya+Dinner+Cruise"
    },
    {
        "id": "bkk-09",
        "name": "White Orchid River Dinner Cruise",
        "link": "white_orchid_river_dinner_cruise.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_white_orchid_river_cruise.webp",
        "alt": "White Orchid dinner cruise Bangkok river",
        "ribbon": "💃 Live Cabaret",
        "category": "river-cruises",
        "category_label": "River Cruises & Riverside",
        "collections": "river-cruises,night,culture-shows",
        "duration": "sunset",
        "duration_hours": "2",
        "duration_label": "⏱️ 2 Hours (Evening)",
        "tour_type": "cruise",
        "tour_type_label": "Dinner Cruise",
        "styles": "couples,family",
        "price": "1250",
        "price_display": "THB 1,250",
        "price_unit": "Price Per Person",
        "highlights": [
            "Expansive 360-degree open-air top deck with skyline view",
            "Sumptuous international buffet featuring grilled prawns",
            "Onboard classical Thai dance & vibrant cabaret show",
            "Welcome drink and festive live disco music entertainment"
        ],
        "enquiry_param": "White+Orchid+River+Dinner+Cruise"
    },
    {
        "id": "bkk-10",
        "name": "Private Longtail Boat Tour of Bangkok Canals",
        "link": "bangkok_canals_private_longtail_boat_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_bangkok_longtail_boat_canals.webp",
        "alt": "Private wooden longtail boat in Bangkok Thonburi khlongs",
        "ribbon": "🛶 Private Charter",
        "category": "river-cruises",
        "category_label": "River Cruises & Riverside",
        "collections": "river-cruises,city-highlights",
        "duration": "half-day",
        "duration_hours": "2",
        "duration_label": "⏱️ 2 Hours",
        "tour_type": "private",
        "tour_type_label": "Private Boat Charter",
        "styles": "couples,culture",
        "price": "1800",
        "price_display": "THB 1,800",
        "price_unit": "Price Per Person",
        "highlights": [
            "Exclusive private wooden longtail boat with captain",
            "Explore historic Thonburi canals ('Venice of the East')",
            "Magnificent waterside view of Wat Paknam 69m Big Buddha",
            "Traditional wooden stilt homes & Artist's House (Baan Silapin)"
        ],
        "enquiry_param": "Bangkok+Canals+Private+Longtail+Boat+Tour"
    },
    {
        "id": "bkk-11",
        "name": "Safari World & Marine Park with Lunch",
        "link": "safari_world_and_marine_park.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_safari_world_and_marine_park.webp",
        "alt": "Safari World and Marine Park Bangkok with dolphin shows",
        "ribbon": "🐬 Family Favourite",
        "category": "family-wildlife",
        "category_label": "Family Attractions & Wildlife",
        "collections": "family-wildlife",
        "duration": "full-day",
        "duration_hours": "7.5",
        "duration_label": "⏱️ 7–8 Hours",
        "tour_type": "shared",
        "tour_type_label": "Shared (SIC Transfers)",
        "styles": "family",
        "price": "1650",
        "price_display": "THB 1,650",
        "price_unit": "Price Per Person",
        "highlights": [
            "Open Zoo safari drive among free-roaming wild animals",
            "Access to all 7 world-class Marine Park animal shows",
            "World's largest giraffe feeding terrace (over 200 giraffes)",
            "International buffet lunch & hotel transfers included"
        ],
        "enquiry_param": "Safari+World+and+Marine+Park+Tour"
    },
    {
        "id": "bkk-12",
        "name": "Safari World Open Zoo Drive Tour",
        "link": "safari_world_open_zoo_drive_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_safari_world_open_zoo.webp",
        "alt": "Safari World Open Zoo coach drive Bangkok",
        "ribbon": "🦁 Wildlife Safari",
        "category": "family-wildlife",
        "category_label": "Family Attractions & Wildlife",
        "collections": "family-wildlife",
        "duration": "half-day",
        "duration_hours": "4.5",
        "duration_label": "⏱️ 4–5 Hours",
        "tour_type": "shared",
        "tour_type_label": "Shared (SIC Transfers)",
        "styles": "family",
        "price": "1150",
        "price_display": "THB 1,150",
        "price_unit": "Price Per Person",
        "highlights": [
            "8-kilometer scenic safari drive through African savannah",
            "See rhinos, zebras, ostriches, antelopes, and camels",
            "Thrilling daily lion & tiger predator feeding show",
            "Comfortable air-conditioned panoramic viewing coach"
        ],
        "enquiry_param": "Safari+World+Open+Zoo+Drive+Tour"
    },
    {
        "id": "bkk-13",
        "name": "Siam Amazing Park (Water & Theme Park)",
        "link": "siam_amazing_park_bangkok.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_siam_amazing_park.webp",
        "alt": "Siam Amazing Park giant wave pool and water slides",
        "ribbon": "🎢 Water & Theme Park",
        "category": "family-wildlife",
        "category_label": "Family Attractions & Wildlife",
        "collections": "family-wildlife",
        "duration": "full-day",
        "duration_hours": "6.5",
        "duration_label": "⏱️ Full Day (6–7 Hrs)",
        "tour_type": "onsite",
        "tour_type_label": "Entry Ticket",
        "styles": "family",
        "price": "950",
        "price_display": "THB 950",
        "price_unit": "Price Per Person",
        "highlights": [
            "Guinness World Record largest wave pool (13,600 sq.m)",
            "7-story rainbow Speed Slide & meandering lazy river",
            "Unlimited rides across X-Zone, Family World & Fantasy World",
            "Suspended looping Vortex roller coaster up to 80 km/h"
        ],
        "enquiry_param": "Siam+Amazing+Park+Bangkok"
    },
    {
        "id": "bkk-14",
        "name": "SEA LIFE Bangkok Ocean World",
        "link": "sea_life_bangkok_ocean_world.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_sea_life_bangkok_ocean_world.webp",
        "alt": "SEA LIFE Bangkok Ocean World underwater tunnel",
        "ribbon": "🐠 Indoor Favourite",
        "category": "family-wildlife",
        "category_label": "Family Attractions & Wildlife",
        "collections": "family-wildlife,city-highlights",
        "duration": "half-day",
        "duration_hours": "2.5",
        "duration_label": "⏱️ 2–3 Hours",
        "tour_type": "onsite",
        "tour_type_label": "Entry Ticket",
        "styles": "family",
        "price": "1190",
        "price_display": "THB 1,190",
        "price_unit": "Price Per Person",
        "highlights": [
            "Southeast Asia's largest aquarium beneath Siam Paragon",
            "Breathtaking 270-degree underwater walkthrough tunnel",
            "Over 30,000 marine animals including sand tiger sharks",
            "Antarctic penguin ice adventure & interactive rock pools"
        ],
        "enquiry_param": "SEA+LIFE+Bangkok+Ocean+World+Tickets"
    },
    {
        "id": "bkk-15",
        "name": "Madame Tussauds Bangkok",
        "link": "madame_tussauds_bangkok.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_madame_tussauds_bangkok.webp",
        "alt": "Madame Tussauds Bangkok celebrity wax museum",
        "ribbon": "🌟 Celebrity Wax Museum",
        "category": "family-wildlife",
        "category_label": "Family Attractions & Wildlife",
        "collections": "family-wildlife,city-highlights",
        "duration": "half-day",
        "duration_hours": "2",
        "duration_label": "⏱️ 1.5–2 Hours",
        "tour_type": "onsite",
        "tour_type_label": "Entry Ticket",
        "styles": "family,couples",
        "price": "890",
        "price_display": "THB 890",
        "price_unit": "Price Per Person",
        "highlights": [
            "Interactive celebrity wax figures with no ropes or barriers",
            "Mingle with Hollywood stars, sports icons & world leaders",
            "Convenient downtown location inside Siam Discovery mall",
            "Fun photo booths, sports zones & wax-making exhibit"
        ],
        "enquiry_param": "Madame+Tussauds+Bangkok+Tickets"
    },
    {
        "id": "bkk-16",
        "name": "Space & Time Cube+ (Mail Hall)",
        "link": "space_and_time_cube_mail_hall.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_space_and_time_cube_mail_hall.webp",
        "alt": "Space and Time Cube digital art exhibition Bangkok",
        "ribbon": "🎨 Immersive Art",
        "category": "shows-entertainment",
        "category_label": "Shows & Entertainment",
        "collections": "culture-shows",
        "duration": "half-day",
        "duration_hours": "1.5",
        "duration_label": "⏱️ 1–2 Hours",
        "tour_type": "onsite",
        "tour_type_label": "Entry Ticket",
        "styles": "couples,family",
        "price": "545",
        "price_display": "THB 545",
        "price_unit": "Price Per Person",
        "highlights": [
            "Cutting-edge 3D projection mapping & infinity mirror rooms",
            "Futuristic light installations & interactive digital art",
            "Instagram-worthy visual photography zones across Mail Hall",
            "Exciting indoor sensory journey suitable for all age groups"
        ],
        "enquiry_param": "Space+and+Time+Cube+Mail+Hall"
    },
    {
        "id": "bkk-17",
        "name": "Mirinn Cabaret & Thai Cultural Show",
        "link": "mirinn_cabaret_theatre_bangkok.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_mirinn_cabaret_theatre.webp",
        "alt": "Mirinn Cabaret and Muay Thai show Bangkok",
        "ribbon": "🥊 Muay Thai & Dance",
        "category": "shows-entertainment",
        "category_label": "Shows & Entertainment",
        "collections": "culture-shows,night",
        "duration": "sunset",
        "duration_hours": "1.5",
        "duration_label": "⏱️ 1.5 Hours (Evening)",
        "tour_type": "onsite",
        "tour_type_label": "Theatre Seat",
        "styles": "culture,couples",
        "price": "950",
        "price_display": "THB 950",
        "price_unit": "Price Per Person",
        "highlights": [
            "Dynamic fusion of glamorous cabaret & live Muay Thai martial arts",
            "Graceful classical Thai royal court dance choreographies",
            "Spectacular costume changes, aerial stunts & modern music",
            "Located at RCA Plaza with optional buffet dinner upgrade"
        ],
        "enquiry_param": "Mirinn+Cabaret+and+Thai+Show+Bangkok"
    },
    {
        "id": "bkk-18",
        "name": "Calypso Cabaret Show Bangkok",
        "link": "calypso_cabaret_show_bangkok.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_calypso_cabaret_show.webp",
        "alt": "Calypso Cabaret show at Asiatique Bangkok",
        "ribbon": "🎭 Legendary Cabaret",
        "category": "shows-entertainment",
        "category_label": "Shows & Entertainment",
        "collections": "culture-shows,night",
        "duration": "sunset",
        "duration_hours": "1.5",
        "duration_label": "⏱️ 1.5 Hours (Show: 70m)",
        "tour_type": "onsite",
        "tour_type_label": "Reserved Seat",
        "styles": "couples",
        "price": "1100",
        "price_display": "THB 1,100",
        "price_unit": "Price Per Person",
        "highlights": [
            "Pioneering Bangkok cabaret theatre operating since 1988",
            "Broadway-style musical revues, glamorous lip-syncs & comedy",
            "Waterfront location in warehouse district of Asiatique",
            "Complimentary beverage included with reserved seat"
        ],
        "enquiry_param": "Calypso+Cabaret+Show+Bangkok"
    },
    {
        "id": "bkk-19",
        "name": "Bangkok Midnight Food & Tuk Tuk Tour",
        "link": "bangkok_midnight_tuk_tuk_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_bangkok_midnight_tuk_tuk.webp",
        "alt": "Bangkok midnight food tour by open-air tuk tuk",
        "ribbon": "🛺 Night Food Tour",
        "category": "night-experiences",
        "category_label": "Night Experiences",
        "collections": "night,markets",
        "duration": "sunset",
        "duration_hours": "4",
        "duration_label": "⏱️ 4 Hours (Evening)",
        "tour_type": "guided",
        "tour_type_label": "Small Group Tour",
        "styles": "food,couples",
        "price": "1750",
        "price_display": "THB 1,750",
        "price_unit": "Price Per Person",
        "highlights": [
            "Zip through illuminated Bangkok boulevards in an iconic Tuk Tuk",
            "Taste Michelin-acclaimed Pad Thai & crispy chicken flat noodles",
            "Visit serene Wat Pho courtyards floodlit under midnight skies",
            "Explore 24-hour Pak Khlong Talad flower market & rooftop bar"
        ],
        "enquiry_param": "Bangkok+Midnight+Food+and+Tuk+Tuk+Tour"
    },
    {
        "id": "bkk-20",
        "name": "Damnoen Saduak Floating Market Tour",
        "link": "damnoen_saduak_floating_market_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_damnoen_saduak_floating_market.webp",
        "alt": "Damnoen Saduak Floating Market paddle boat ride",
        "ribbon": "🛶 Iconic Market",
        "category": "markets-shopping",
        "category_label": "Markets & Shopping",
        "collections": "markets,day-trips",
        "duration": "full-day",
        "duration_hours": "6",
        "duration_label": "⏱️ 6 Hours (Morning)",
        "tour_type": "shared",
        "tour_type_label": "Shared (SIC Transfers)",
        "styles": "culture,family",
        "price": "990",
        "price_display": "THB 990",
        "price_unit": "Price Per Person",
        "highlights": [
            "Thailand's most famous and photogenic canal trading market",
            "Traditional wooden paddle boat ride along active waterways",
            "Friendly vendors cooking fresh boat noodles and tropical fruit",
            "Visit traditional roadside coconut palm sugar cottage farm"
        ],
        "enquiry_param": "Damnoen+Saduak+Floating+Market+Tour"
    },
    {
        "id": "bkk-21",
        "name": "Maeklong Railway & Floating Market Tour",
        "link": "maeklong_railway_market_and_floating_market_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_maeklong_railway_market.webp",
        "alt": "Maeklong Railway Market train passing market stalls",
        "ribbon": "🚂 Double Market Combo",
        "category": "markets-shopping",
        "category_label": "Markets & Shopping",
        "collections": "markets,day-trips",
        "duration": "full-day",
        "duration_hours": "7",
        "duration_label": "⏱️ 7 Hours (Full Day)",
        "tour_type": "shared",
        "tour_type_label": "Shared (SIC Transfers)",
        "styles": "culture,family",
        "price": "1290",
        "price_display": "THB 1,290",
        "price_unit": "Price Per Person",
        "highlights": [
            "Watch market awnings retract as active train passes inches away",
            "Walk along the railway tracks lined with exotic produce stalls",
            "Paddle boat cruise through Damnoen Saduak floating canals",
            "Convenient round-trip hotel transfers from central Bangkok"
        ],
        "enquiry_param": "Maeklong+Railway+Market+and+Floating+Market+Tour"
    },
    {
        "id": "bkk-22",
        "name": "Chinatown & Yaowarat Street Food Tour",
        "link": "chinatown_yaowarat_street_food_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_chinatown_yaowarat_bangkok.webp",
        "alt": "Yaowarat Road Chinatown street food tour Bangkok",
        "ribbon": "🥢 Culinary Journey",
        "category": "markets-shopping",
        "category_label": "Markets & Shopping",
        "collections": "markets,night",
        "duration": "sunset",
        "duration_hours": "3.5",
        "duration_label": "⏱️ 3–4 Hours (Evening)",
        "tour_type": "guided",
        "tour_type_label": "Small Group Tour",
        "styles": "food,culture",
        "price": "1200",
        "price_display": "THB 1,200",
        "price_unit": "Price Per Person",
        "highlights": [
            "Guided evening food walk through neon-lit Yaowarat Road",
            "6 to 8 curated tastings at heritage and Michelin-guide stalls",
            "Savor crispy pork Guay Jub, steamed dim sum & custard buns",
            "Explore hidden temple shrines & lively Chinese herb alleys"
        ],
        "enquiry_param": "Chinatown+Yaowarat+Street+Food+Tour"
    },
    {
        "id": "bkk-23",
        "name": "Ayutthaya Historical Park Full-Day Tour",
        "link": "ayutthaya_historical_park_full_day_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_ayutthaya_historical_park.webp",
        "alt": "Wat Mahathat Buddha head in tree roots Ayutthaya",
        "ribbon": "🏛️ UNESCO World Heritage",
        "category": "day-trips",
        "category_label": "Day Trips from Bangkok",
        "collections": "day-trips,temples",
        "duration": "full-day",
        "duration_hours": "8.5",
        "duration_label": "⏱️ 8–9 Hours (Full Day)",
        "tour_type": "shared",
        "tour_type_label": "Shared (SIC Transfers)",
        "styles": "culture,day-trips",
        "price": "1950",
        "price_display": "THB 1,950",
        "price_unit": "Price Per Person",
        "highlights": [
            "Ancient Siamese capital city (1350–1767) UNESCO World Heritage",
            "Iconic Buddha head entwined in banyan roots at Wat Mahathat",
            "Majestic Khmer-style riverside prangs of Wat Chaiwatthanaram",
            "All temple entrance fees and riverside Thai buffet lunch included"
        ],
        "enquiry_param": "Ayutthaya+Historical+Park+Full+Day+Tour"
    },
    {
        "id": "bkk-24",
        "name": "Ancient City (Muang Boran) & Erawan Museum",
        "link": "ancient_city_and_erawan_museum_tour.html",
        "img": "../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_ancient_city_muang_boran.webp",
        "alt": "Ancient City Muang Boran Sanphet Prasat Palace replica",
        "ribbon": "🐘 Architectural Wonder",
        "category": "day-trips",
        "category_label": "Day Trips from Bangkok",
        "collections": "day-trips,culture-shows",
        "duration": "full-day",
        "duration_hours": "7.5",
        "duration_label": "⏱️ 7–8 Hours (Full Day)",
        "tour_type": "shared",
        "tour_type_label": "Shared (SIC Transfers)",
        "styles": "culture,day-trips",
        "price": "1750",
        "price_display": "THB 1,750",
        "price_unit": "Price Per Person",
        "highlights": [
            "World's largest open-air museum spanning 300 landscaped acres",
            "120+ reconstructed royal palaces, sacred temples & ruins",
            "Colossal 250-ton three-headed bronze elephant at Erawan Museum",
            "Scenic exploration via complimentary bicycle or park tram"
        ],
        "enquiry_param": "Ancient+City+and+Erawan+Museum+Tour"
    }
]

FAQS_DATA = [
    (
        "What are the best sightseeing places to visit in Bangkok?",
        "Bangkok's premier sightseeing attractions include the Grand Palace & Wat Phra Kaew, the Reclining Buddha at Wat Pho, the riverside Temple of Dawn (Wat Arun), panoramic views from Mahanakhon SkyWalk (314m), an evening Chao Phraya dinner cruise, family adventures at Safari World & Marine Park, SEA LIFE Bangkok Ocean World, and day trips to Damnoen Saduak Floating Market or Ayutthaya Historical Park."
    ),
    (
        "Can I book individual Bangkok sightseeing activities without a holiday package?",
        "Yes, absolutely. Trippovention supports standalone bookings for individual Bangkok day tours, attraction admission tickets, evening river cruises, and private canal charters without requiring you to purchase a complete multi-day holiday package."
    ),
    (
        "What is the difference between a shared tour and a private Bangkok tour?",
        "Shared (SIC) tours combine travelers in modern air-conditioned minivans with scheduled pickup windows and set itineraries, offering excellent value. Private tours provide an exclusive vehicle and dedicated licensed guide for your party alone, offering flexible timings, customized stops, and direct hotel-to-attraction transit."
    ),
    (
        "Are hotel transfers included in Bangkok sightseeing tours?",
        "Most of our guided day tours (such as the City Highlights Tour, Floating Markets, Safari World package, and Ayutthaya) include complimentary round-trip transfers from central Bangkok hotels in Sukhumvit, Silom, Sathorn, Siam, and Pratunam. Standalone attraction tickets (such as Mahanakhon SkyWalk or SEA LIFE) are entry-only, though private transfers can be added upon request."
    ),
    (
        "Are attraction admission tickets included in the tour price?",
        "Yes, our guided tour packages clearly state and include official entrance admission tickets for all designated itinerary sites (such as the Grand Palace, Wat Pho, Wat Arun, and Ayutthaya ruins) with no hidden fees at the gates."
    ),
    (
        "Can I combine the Grand Palace, Wat Pho, and Wat Arun in one day?",
        "Yes, these three iconic cultural landmarks are situated close together along the Chao Phraya River. We recommend visiting the Grand Palace and Wat Pho in the morning, crossing the river by local ferry for lunch, and exploring Wat Arun in the softer afternoon light."
    ),
    (
        "Are dinner cruises on the Chao Phraya River available?",
        "Yes, we offer leading luxury dinner cruises such as the Princess Chao Phraya Dinner Cruise and White Orchid River Cruise. Both depart nightly, offering 2-hour evening cruises with international seafood buffets, live music, cabaret performances, and illuminated views of riverside temples."
    ),
    (
        "Can I book Safari World and Marine Park with transfers and lunch?",
        "Yes, our most popular family package includes admission to both Safari Park (the 8-km open drive-through zoo) and Marine Park (featuring all 7 daily animal shows), a delicious international lunch buffet, and round-trip hotel transfers from central Bangkok."
    ),
    (
        "Can I arrange a floating market and railway market excursion?",
        "Yes, our combined Maeklong Railway Market and Damnoen Saduak Floating Market tour is one of Bangkok's top day trips. It synchronizes with the scheduled train passing through the market stalls and includes a traditional wooden paddle boat ride through the floating market canals."
    ),
    (
        "How can I request a customised Bangkok sightseeing itinerary?",
        "Simply click 'Enquire Now' on any experience card, use our website contact form, or message our destination specialists via WhatsApp (+66 94 693 4392). Share your travel dates, party size, and preferred sights, and our team will craft a personalized quotation."
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
                <div class="card-footer-actions">
                  <a class="btn btn-outline-details" href="{exp['link']}">View Details</a>
                  <a
                    class="btn btn-enquire"
                    href="../../../contact.html?destination=bangkok&tour={exp['enquiry_param']}"
                    >Enquire Now →</a
                  >
                </div>
              </div>
            </article>"""
        cards_html_list.append(card_html)
    all_cards_html = "\n\n".join(cards_html_list)

    # 2. Build FAQ Accordions & Schema
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

    # 3. Complete Page HTML
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
    <title>Bangkok Sightseeing Tours &amp; Attractions | Trippovention</title>
    <meta
      name="description"
      content="Explore Bangkok sightseeing tours, temples, river cruises, Safari World, city attractions and day trips. Enquire with Trippovention for current offers and travel arrangements."
    />
    <meta name="author" content="Trippovention" />

    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://trippovention.co.th/packages/thailand/bangkok/sightseeing.html" />
    <meta property="og:title" content="Bangkok Sightseeing Tours &amp; Attractions | Trippovention" />
    <meta
      property="og:description"
      content="Explore Bangkok sightseeing tours, temples, river cruises, Safari World, city attractions and day trips. Enquire with Trippovention for current offers and travel arrangements."
    />
    <meta property="og:image" content="https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_full_day_bangkok_city_tour.webp" />

    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:url" content="https://trippovention.co.th/packages/thailand/bangkok/sightseeing.html" />
    <meta property="twitter:title" content="Bangkok Sightseeing Tours &amp; Attractions | Trippovention" />
    <meta
      property="twitter:description"
      content="Explore Bangkok sightseeing tours, temples, river cruises, Safari World, city attractions and day trips. Enquire with Trippovention for current offers and travel arrangements."
    />
    <meta property="twitter:image" content="https://trippovention.co.th/assets/images/packages/thailand/bangkok/sightseeingoptions/hero_full_day_bangkok_city_tour.webp" />

    <link rel="canonical" href="https://trippovention.co.th/packages/thailand/bangkok/sightseeing.html" />
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
        "name": "Bangkok Sightseeing Tours & Attractions",
        "description": "Expanded catalogue of Bangkok sightseeing tours, royal temples, Chao Phraya river cruises, Safari World, floating markets, and cultural excursions.",
        "url": "https://trippovention.co.th/packages/thailand/bangkok/sightseeing.html",
        "containedInPlace": {{
          "@type": "Country",
          "name": "Thailand"
        }},
        "touristType": ["City Sightseeing", "Cultural Heritage", "River Cruises", "Family Vacations", "Night Tours"]
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
            "name": "Bangkok",
            "item": "https://trippovention.co.th/packages/thailand/bangkok/"
          }},
          {{
            "@type": "ListItem",
            "position": 5,
            "name": "Sightseeing",
            "item": "https://trippovention.co.th/packages/thailand/bangkok/sightseeing.html"
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
                    url('../../../assets/images/packages/thailand/bangkok/sightseeingoptions/hero_full_day_bangkok_city_tour.webp') center/cover no-repeat;
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

      /* Card presentation */
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
      .highlights-list {{
        list-style: none;
        padding: 0;
        margin: 10px 0 16px;
        font-size: 0.83rem;
        color: var(--text-secondary);
        line-height: 1.5;
      }}
      .highlights-list li {{
        position: relative;
        padding-left: 18px;
        margin-bottom: 4px;
      }}
      .highlights-list li::before {{
        content: "✓";
        position: absolute;
        left: 0;
        color: var(--emerald);
        font-weight: 700;
      }}
      .card-footer-actions {{
        margin-top: auto;
        padding-top: 14px;
        border-top: 1px solid var(--border-light);
        display: flex;
        gap: 8px;
      }}
      .card-footer-actions .btn {{
        flex: 1;
        text-align: center;
        padding: 10px 12px;
        font-size: 0.88rem;
      }}
      .btn-outline-details {{
        background: transparent;
        border: 1.5px solid var(--border-color);
        color: var(--text-primary);
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.2s;
        cursor: pointer;
      }}
      .btn-outline-details:hover {{
        border-color: var(--orange);
        color: var(--orange);
        background: rgba(214, 128, 78, 0.05);
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
              <a href="index.html">Bangkok</a>
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
          <h1>Discover the Best of Bangkok</h1>
          <p>
            Explore Bangkok through its iconic temples, royal landmarks, scenic river cruises, vibrant markets, modern observation decks, cultural performances, wildlife attractions, and unforgettable local experiences. Discover sightseeing options for families, couples, groups, and independent travellers, and submit an enquiry to plan your preferred activities with Trippovention.
          </p>
          <div class="hero-actions">
            <a class="btn btn-lg" href="#catalogue">Browse Experiences ↓</a>
            <a class="btn btn-lg ghost" href="index.html">← Back to Bangkok Destination Page</a>
          </div>
        </div>
      </header>

      <!-- Section: Curated Bangkok Collections (Center-Aligned) -->
      <section class="collections-section" aria-label="Curated Bangkok Collections">
        <div class="container">
          <div class="section-title text-center" style="margin-bottom: 20px;">
            <h2 style="font-size: 1.45rem;">Curated Bangkok Collections</h2>
            <p class="subtitle" style="margin-bottom: 0;">Explore handpicked highlights curated for specific travel styles</p>
          </div>
          <div class="collections-grid">
            <button type="button" class="collection-pill-card" data-collection="city-highlights" aria-label="Filter by Bangkok City Highlights">
              <span class="col-icon">🏙️</span>
              <span class="col-title">Bangkok City Highlights</span>
              <span class="col-sub">Landmarks &amp; Towers</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="temples" aria-label="Filter by Temples & Royal Heritage">
              <span class="col-icon">🛕</span>
              <span class="col-title">Temples &amp; Heritage</span>
              <span class="col-sub">Palace &amp; Wat Pho</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="river-cruises" aria-label="Filter by River Cruises & Riverside">
              <span class="col-icon">🚢</span>
              <span class="col-title">River Cruises</span>
              <span class="col-sub">Chao Phraya &amp; Canals</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="family-wildlife" aria-label="Filter by Family Fun & Wildlife">
              <span class="col-icon">🦁</span>
              <span class="col-title">Family Fun &amp; Wildlife</span>
              <span class="col-sub">Safari World &amp; Parks</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="culture-shows" aria-label="Filter by Culture, Shows & Entertainment">
              <span class="col-icon">🎭</span>
              <span class="col-title">Culture &amp; Shows</span>
              <span class="col-sub">Cabaret &amp; Thai Shows</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="markets" aria-label="Filter by Markets, Shopping & Local Life">
              <span class="col-icon">🛍️</span>
              <span class="col-title">Markets &amp; Shopping</span>
              <span class="col-sub">Floating &amp; Railway</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="night" aria-label="Filter by Bangkok by Night">
              <span class="col-icon">🌃</span>
              <span class="col-title">Bangkok by Night</span>
              <span class="col-sub">Night Tours &amp; Dinners</span>
            </button>
            <button type="button" class="collection-pill-card" data-collection="day-trips" aria-label="Filter by Day Trips from Bangkok">
              <span class="col-icon">🏛️</span>
              <span class="col-title">Day Trips from Bangkok</span>
              <span class="col-sub">Ayutthaya &amp; Ancient City</span>
            </button>
          </div>
        </div>
      </section>

      <!-- Sightseeing Catalogue Section -->
      <section class="section" id="catalogue">
        <div class="container">
          <!-- Filter & Search Toolbar -->
          <div class="filter-toolbar" role="search" aria-label="Search and filter Bangkok sightseeing">
            <div class="search-box-row">
              <div class="search-input-wrap">
                <input
                  type="text"
                  id="bangkokSearchInput"
                  placeholder="Find Your Bangkok Experience (e.g. Grand Palace, River Cruise, Safari World)..."
                  aria-label="Find Your Bangkok Experience"
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
                All Experiences <span class="pill-count" id="countAll">24</span>
              </button>
              <button type="button" class="cat-pill" data-category="city-tours" role="tab" aria-selected="false">
                🏙️ City Tours &amp; Landmarks <span class="pill-count">2</span>
              </button>
              <button type="button" class="cat-pill" data-category="temples" role="tab" aria-selected="false">
                🛕 Temples &amp; Heritage <span class="pill-count">4</span>
              </button>
              <button type="button" class="cat-pill" data-category="river-cruises" role="tab" aria-selected="false">
                🚢 River Cruises <span class="pill-count">4</span>
              </button>
              <button type="button" class="cat-pill" data-category="family-wildlife" role="tab" aria-selected="false">
                🦁 Family &amp; Wildlife <span class="pill-count">5</span>
              </button>
              <button type="button" class="cat-pill" data-category="shows-entertainment" role="tab" aria-selected="false">
                🎭 Shows &amp; Entertainment <span class="pill-count">3</span>
              </button>
              <button type="button" class="cat-pill" data-category="markets-shopping" role="tab" aria-selected="false">
                🛍️ Markets &amp; Shopping <span class="pill-count">3</span>
              </button>
              <button type="button" class="cat-pill" data-category="night-experiences" role="tab" aria-selected="false">
                🌃 Night Experiences <span class="pill-count">1</span>
              </button>
              <button type="button" class="cat-pill" data-category="day-trips" role="tab" aria-selected="false">
                🏛️ Day Trips <span class="pill-count">2</span>
              </button>
            </div>

            <!-- Secondary Filters Panel -->
            <div class="secondary-filters-bar" id="secondaryFiltersBar">
              <div class="filter-group">
                <label for="filterDuration">Duration</label>
                <select id="filterDuration" class="filter-select">
                  <option value="all">All Durations</option>
                  <option value="half-day">Half Day (1–4 hrs)</option>
                  <option value="full-day">Full Day (5–9 hrs)</option>
                  <option value="sunset">Evening / Night</option>
                </select>
              </div>

              <div class="filter-group">
                <label for="filterTourType">Tour Type</label>
                <select id="filterTourType" class="filter-select">
                  <option value="all">All Tour Types</option>
                  <option value="shared">Shared (SIC Transfers)</option>
                  <option value="private">Private Charter / Tour</option>
                  <option value="onsite">Entry Ticket</option>
                  <option value="cruise">Cruise</option>
                  <option value="guided">Guided Tour</option>
                </select>
              </div>

              <div class="filter-group">
                <label for="filterTraveler">Experience Style</label>
                <select id="filterTraveler" class="filter-select">
                  <option value="all">All Styles</option>
                  <option value="family">Family Friendly</option>
                  <option value="couples">Couples / Romantic</option>
                  <option value="culture">Culture &amp; Heritage</option>
                  <option value="city">Skyline &amp; Modern</option>
                  <option value="food">Food &amp; Nightlife</option>
                  <option value="day-trips">Day Excursions</option>
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
              Showing <strong id="visibleCount">24</strong> of <span id="totalCount">24</span> experiences in Bangkok
            </div>
            <a href="index.html" class="back-to-dest-link">
              ← Return to Bangkok Destination Overview
            </a>
          </div>

          <!-- Cards Grid -->
          <div class="grid cols-3" id="cardsGrid">
{all_cards_html}

            <!-- Empty Results State -->
            <div id="emptyResultsBox" class="empty-results-box" style="display: none;">
              <div class="empty-icon">🔍</div>
              <h3>No Bangkok Experiences Match Your Search</h3>
              <p class="muted">Try adjusting your keywords, resetting filters, or browsing all curated collections.</p>
              <button type="button" id="emptyResetBtn" class="btn btn-outline-details mt-10">↺ Reset All Filters</button>
            </div>
          </div>
        </div>
      </section>

      <!-- Bangkok-Specific FAQ Accordion Section (AEO Guidance) -->
      <section class="section alt faq-section" id="faq">
        <div class="container">
          <div class="section-title text-center">
            <h2>Frequently Asked Questions</h2>
            <p class="subtitle">Essential advice for planning your Bangkok sightseeing, temples, cruises, and day tours</p>
          </div>
          <div class="faq-container">
{all_faqs_html}
          </div>
        </div>
      </section>

      <!-- Destination CTA Banner -->
      <section class="section cta">
        <div class="container">
          <div class="section-title">
            <h2 class="text-white">Plan Your Bangkok Sightseeing Itinerary</h2>
            <p class="subtitle text-white-90">
              Personalized private tours, shared sightseeing, and verified attraction arrangements with Trippovention
            </p>
          </div>
          <div class="text-center">
            <a class="btn btn-lg ghost" href="../../../contact.html?destination=bangkok&type=sightseeing">📞 Request Bangkok Tour Plan</a>
            <a
              class="btn btn-lg ghost ml-16"
              href="https://wa.me/66946934392?text=Hello,%20I%20am%20interested%20in%20planning%20Bangkok%20sightseeing%20tours%20with%20Trippovention"
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
              <a href="sightseeing.html">Bangkok Sightseeing Catalogue</a><br />
              <a href="index.html">Bangkok Tour Packages</a><br />
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

    <!-- Interactive Search, Filtering & Modal JavaScript -->
    <script>
      (function () {{
        const searchInput = document.getElementById("bangkokSearchInput");
        const searchClearBtn = document.getElementById("searchClearBtn");
        const filterToggleMobileBtn = document.getElementById("filterToggleMobileBtn");
        const secondaryFiltersBar = document.getElementById("secondaryFiltersBar");
        const catPills = document.querySelectorAll(".cat-pill");
        const collectionCards = document.querySelectorAll(".collection-pill-card");
        const filterDuration = document.getElementById("filterDuration");
        const filterTourType = document.getElementById("filterTourType");
        const filterTraveler = document.getElementById("filterTraveler");
        const sortBy = document.getElementById("sortBy");
        const resetFiltersBtn = document.getElementById("resetFiltersBtn");
        const emptyResetBtn = document.getElementById("emptyResetBtn");
        const cardsGrid = document.getElementById("cardsGrid");
        const cards = Array.from(document.querySelectorAll(".sightseeing-card"));
        const visibleCountEl = document.getElementById("visibleCount");
        const totalCountEl = document.getElementById("totalCount");
        const emptyResultsBox = document.getElementById("emptyResultsBox");

        if (totalCountEl) totalCountEl.textContent = cards.length;

        // Current filter state
        let currentCategory = "all";
        let currentCollection = "all";
        let currentDuration = "all";
        let currentTourType = "all";
        let currentTraveler = "all";
        let currentSearchQuery = "";
        let currentSort = "recommended";

        // Mobile filter panel toggle
        if (filterToggleMobileBtn && secondaryFiltersBar) {{
          filterToggleMobileBtn.addEventListener("click", function () {{
            const isOpen = secondaryFiltersBar.classList.toggle("mobile-open");
            filterToggleMobileBtn.setAttribute("aria-expanded", isOpen ? "true" : "false");
          }});
        }}

        // Search Input listeners
        if (searchInput) {{
          searchInput.addEventListener("input", function () {{
            currentSearchQuery = this.value.trim().toLowerCase();
            if (searchClearBtn) {{
              searchClearBtn.style.display = currentSearchQuery ? "block" : "none";
            }}
            applyFilters();
          }});
        }}
        if (searchClearBtn) {{
          searchClearBtn.addEventListener("click", function () {{
            if (searchInput) {{
              searchInput.value = "";
              currentSearchQuery = "";
              this.style.display = "none";
              searchInput.focus();
              applyFilters();
            }}
          }});
        }}

        // Category pills click
        catPills.forEach(pill => {{
          pill.addEventListener("click", function () {{
            catPills.forEach(p => {{
              p.classList.remove("active");
              p.setAttribute("aria-selected", "false");
            }});
            this.classList.add("active");
            this.setAttribute("aria-selected", "true");
            currentCategory = this.dataset.category || "all";
            collectionCards.forEach(c => c.classList.remove("active"));
            currentCollection = "all";
            applyFilters();
          }});
        }});

        // Curated Collections click
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
    print(f"Bangkok Sightseeing Catalogue successfully created at:\n{CATALOGUE_PATH}")

if __name__ == "__main__":
    generate_catalogue_html()
