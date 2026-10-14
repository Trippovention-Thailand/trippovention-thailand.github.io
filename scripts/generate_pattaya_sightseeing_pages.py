#!/usr/bin/env python3
"""
Generate individual detail pages for the 19 new Pattaya sightseeing tours.
Follows Trippovention design system, typography, SEO metadata, breadcrumbs, 
genuine Pattaya-specific FAQs, and schema.
"""

import os

DEST_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "packages", "thailand", "pattaya")

TOURS_DATA = [
    {
        "filename": "sanctuary_of_truth_pattaya.html",
        "title": "Sanctuary of Truth Museum Pattaya Admission & Guided Tour | Trippovention",
        "h1": "Sanctuary of Truth Museum Guided Tour",
        "subtitle": "All-Wood Oceanfront Architectural Wonder, Four Cosmological Wings & Master Woodcarving",
        "meta_desc": "Visit Pattaya's Sanctuary of Truth Museum (Prasat Sut Ja-Tum) with admission, hard hat, and guided tour. Discover traditional hand-carved wood architecture.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_sanctuary_of_truth_pattaya.webp",
        "duration": "2–3 Hours",
        "price": "THB 700",
        "price_note": "(Per Person)",
        "meetup": "Sanctuary of Truth Main Entrance (Naklua Soi 12, Pattaya) or Hotel Transfer",
        "overview_p1": "Rising dramatically over the rocky shores of Cape Ratchavate in North Pattaya, the Sanctuary of Truth Museum (Prasat Sut Ja-Tum) is an awe-inspiring, 105-meter-tall monumental structure constructed entirely from seasoned Thai hardwood. Built without a single metal nail, the entire temple-castle employs traditional interlocking wood joinery techniques handed down through generations of master artisans.",
        "overview_p2": "Conceived in 1981 by visionary Thai businessman Lek Viriyaphant, the sanctuary serves as an architectural homage to traditional Asian spiritual philosophy, cosmic creation, and filial piety. As an active construction and preservation site, visitors wear safety helmets while exploring intricately carved sanctuaries illustrating Thai, Khmer, Chinese, and Indian cosmological traditions alongside working master craftsmen.",
        "places_col1_title": "Sanctuary Wings & Halls",
        "places_col1_badge": "Architectural Marvel",
        "places_col1_items": [
            ("Central Spire (Phra Kal)", "105-meter towering wooden pinnacle adorned with the equestrian figure of Kalpa, symbolizing the arrival of the fifth Maitreya Buddha."),
            ("Four Cosmological Wings", "Dedicated wings depicting classical themes of creation: Heaven & Earth, Ancestral Duty, Philosophical Wisdom, and Moral Responsibility."),
            ("Hand-Carved Sculptures", "Countless life-size representations of Brahma, Shiva, Vishnu, and celestial Apsaras carved from redwood, ironwood, and teak.")
        ],
        "places_col2_title": "Workshops & Oceanfront Grounds",
        "places_col2_badge": "Living Heritage",
        "places_col2_items": [
            ("Master Woodcarver Workshops", "Observe master woodcarvers shaping intricate relief panels and statues using classical gouges, mallets, and chisels."),
            ("Cliffside Scenic Viewpoint", "Stunning panoramic observation deck overlooking the Gulf of Thailand and the wooden temple complex below."),
            ("Traditional Boat & Cultural Activities", "Optional exploration around the coastal perimeter aboard a traditional wooden rowboat or scenic horse carriage ride.")
        ],
        "inclusions": [
            "Official entrance admission ticket to Sanctuary of Truth Museum",
            "Mandatory safety hard hat for interior exploration",
            "Certified English-speaking museum guide service (regular departures)",
            "Access to open carving workshops and cultural viewpoints",
            "Travel accident insurance coverage"
        ],
        "exclusions": [
            "Round-trip hotel transfers (can be added on request)",
            "Optional activities (wooden rowboat, horse carriage, or elephant greeting)",
            "Personal souvenirs, refreshments, and snacks",
            "Gratuities for museum guide"
        ],
        "timing_text": "Open daily from 08:00 AM to 06:00 PM.<br />Evening illuminated tour sessions available from 06:00 PM to 08:30 PM.",
        "transport_text": "Located at 206/2 Moo 5, Soi Naklua 12, Naklua, Bang Lamung, Chonburi. Hotel transfers available upon request.",
        "what_to_bring": "Modest clothing covering shoulders and knees (sarongs available for hire), comfortable walking shoes, and camera.",
        "contact_tour_param": "Sanctuary+of+Truth+Museum+Guided+Tour",
        "faqs": [
            ("What is the dress code for visiting the Sanctuary of Truth?", "Because the Sanctuary of Truth is a sacred cultural and spiritual monument, visitors must wear clothing that covers both shoulders and knees. Sleeveless tops, miniskirts, short shorts, and sheer fabrics are not permitted. Sarongs can be rented or purchased at the entrance."),
            ("Are guided tours included in the standard admission ticket?", "Yes, official multilingual guided tours (English, Thai, Russian, and Chinese) are included with your admission ticket and depart regularly throughout the day. Exploring with a guide is recommended to understand the deep philosophical symbolism of the carvings."),
            ("Why is the Sanctuary of Truth still under construction?", "The sanctuary is conceived as an ongoing, living masterpiece. Due to coastal sea salt, sun exposure, and tropical humidity, craftsmen continuously restore seasoned timbers while hand-carving new sections in accordance with ancient Khmer and Ayutthaya-era woodworking traditions."),
            ("Is the Sanctuary of Truth wheelchair accessible?", "The sanctuary grounds and viewpoint terrace are wheelchair accessible via paved ramps. However, the inner temple sanctuary requires climbing wooden stairs; wheelchair users can explore the surrounding galleries, viewpoints, and artisan workshops.")
        ]
    },
    {
        "filename": "columbia_pictures_aquaverse_tickets.html",
        "title": "Columbia Pictures Aquaverse Water Park Tickets Pattaya | Trippovention",
        "h1": "Columbia Pictures Aquaverse Water Park",
        "subtitle": "World's First Sony Columbia Pictures Theme & Water Park in Na Jomtien, Pattaya",
        "meta_desc": "Book Columbia Pictures Aquaverse tickets in Pattaya. Enjoy themed water rides, Ghostbusters proton stream, Jumanji jungle drop, Bad Boys go-karts & wave pool.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_columbia_pictures_aquaverse.webp",
        "duration": "Full Day (5–7 Hours)",
        "price": "THB 1,290",
        "price_note": "(Per Person)",
        "meetup": "Na Jomtien, Pattaya (15 mins south of Central Pattaya) or Hotel Transfer",
        "overview_p1": "Immerse yourself in world-class cinematic thrills at Columbia Pictures Aquaverse, the planet's very first fully branded Sony Columbia Pictures theme and water park. Located in Na Jomtien just minutes south of Pattaya, this massive entertainment destination brings iconic blockbuster movies to life across eight immersive themed zones.",
        "overview_p2": "From high-speed water slides themed around Ghostbusters, Jumanji, and Zombieland to the Southeast Asia's largest wave pool with a giant outdoor cinema screen, Aquaverse delivers non-stop excitement for thrill-seekers, kids, and movie lovers alike. Enjoy themed food zones, miniature golf, Bad Boys Miami go-karts, and live character meet-and-greets throughout the day.",
        "places_col1_title": "Top Blockbuster Zones",
        "places_col1_badge": "High-Thrill Rides",
        "places_col1_items": [
            ("Ghostbusters Proton Stream", "World's first water coaster in a dark enclosed sphere featuring twists, turns, and ghost-hunting visual projections."),
            ("Jumanji Jungle Adventure", "Viper-themed wild water slides shooting through jungle canopies into a massive splashdown basin."),
            ("Zombieland Daredevil Drop", "Exhilarating 18-meter vertical trapdoor drop slide reaching breakneck speeds into a high-g deceleration runout.")
        ],
        "places_col2_title": "Family & Entertainment Zones",
        "places_col2_badge": "Family Entertainment",
        "places_col2_items": [
            ("Hotel Transylvania Water Castle", "Southeast Asia's largest kid-friendly splash structure featuring 9 water slides, 100+ water play elements, and giant dump buckets."),
            ("Mega Wave Pool & Aquaverse Cinema", "Catch movie screenings, DJ music sets, and live concerts while floating on rubber tubes in the massive wave pool."),
            ("Bad Boys Raceway", "High-speed outdoor electric go-kart track designed with neon-lit Miami street racing vibes.")
        ],
        "inclusions": [
            "Full-day unlimited access to all water slides, pools, and themed attractions",
            "Use of life vests and park inflatable inner tubes",
            "Live character meet-and-greets (Ghostbusters, Hotel Transylvania)",
            "Access to Mega Wave Pool and outdoor cinema shows",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Hotel pickup and drop-off (optional private transfer available)",
            "Locker and towel rentals (available on-site)",
            "Food, beverages, and merchandise",
            "Bad Boys Go-Karting sessions (optional paid add-on on-site)"
        ],
        "timing_text": "Open daily (except Wednesdays) from 10:00 AM to 06:00 PM.<br />Water slides close at 05:30 PM.",
        "transport_text": "Sukhumvit Road, Na Jomtien, Sattahip, Chonburi. Approximately 20 minutes from Central Pattaya.",
        "what_to_bring": "Appropriate swimwear (no metal buckles or zippers on slides), waterproof sunscreen, sunglasses, and flip-flops.",
        "contact_tour_param": "Columbia+Pictures+Aquaverse+Tickets",
        "faqs": [
            ("What is the difference between adult and child tickets?", "Adult tickets apply to guests aged 13 and above. Child tickets apply to children aged 3 to 12. Infants aged 0 to 2 enter completely free of charge when accompanied by a paying adult."),
            ("Can visitors bring outside food or drinks into the park?", "Outside food and beverages are not permitted inside Aquaverse, with the exception of baby formula and medical dietary necessities. The park features multiple movie-themed dining options offering Thai, Western, and halal choices."),
            ("Are towels and storage lockers available for rent?", "Yes, electronic RFID lockers and clean rental towels are available near the changing rooms for a nominal daily fee."),
            ("Is Columbia Pictures Aquaverse suitable for non-swimmers?", "Yes! Certified life vests are provided free of charge, and professional lifeguards supervise all pools and slide splash basins continuously. Zones like Hotel Transylvania and the Lazy River are ideal for guests of all swimming abilities.")
        ]
    },
    {
        "filename": "ramayana_water_park_pattaya.html",
        "title": "Ramayana Water Park Pattaya Tickets & Day Pass | Trippovention",
        "h1": "Ramayana Water Park Pattaya",
        "subtitle": "Thailand's Largest Water Park, 21 World-Class Slides & Natural Crystal-Clear Springs",
        "meta_desc": "Spend an exhilarating day at Ramayana Water Park Pattaya. 21 thrilling water slides, 2 dedicated kids zones, lazy river, and crystal-clear spring-fed pools.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_ramayana_water_park.webp",
        "duration": "Full Day (6–8 Hours)",
        "price": "THB 1,190",
        "price_note": "(Per Person)",
        "meetup": "Silverlake / Na Jomtien Area, Pattaya (Roundtrip transfers available)",
        "overview_p1": "Ranked consistently as the #1 water park in Thailand and among the top 10 water parks in the world by TripAdvisor, Ramayana Water Park spans over 45 acres of breathtaking natural greenery nestled between Silverlake Vineyard and Khao Chi Chan Buddha Mountain.",
        "overview_p2": "Ramayana features 21 premium WhiteWater West slides, crystal-clear water supplied from the park's own natural freshwater wells with state-of-the-art filtration, two expansive children's aqua playgrounds, a 600-meter lazy river passing ancient ruins, and a dual-wave beach pool. Whether seeking adrenaline-pumping drop slides or relaxing in a private VIP cabana, Ramayana guarantees a premier family day out.",
        "places_col1_title": "Adrenaline Slides",
        "places_col1_badge": "World-Class Thrills",
        "places_col1_items": [
            ("Aqualoop & Freefall", "Step into the launch capsule and feel the floor drop out beneath you into a near-vertical 360-degree looping chute."),
            ("Python & Aquaconda", "Massive interconnected tunnel tubes featuring huge oscillating wall climbs and exhilarating sudden drops on multi-person rafts."),
            ("Boomerango & Spiral", "Propel up a vertical curved wall for a moment of zero-gravity weightlessness before splashing into the lower pool.")
        ],
        "places_col2_title": "Relaxation & Kids Play",
        "places_col2_badge": "Family Leisure",
        "places_col2_items": [
            ("600-Meter Lazy River", "Drift gently through lush tropical gardens, waterfall grottos, and mystical ruins of an ancient lost city."),
            ("Double Wave Pool", "Massive split beach pool generating gentle swells on one side and dramatic rolling waves on the other."),
            ("Aquasplash & River Slide", "Two dedicated interactive water splash zones designed specifically for toddlers and young children with zero-depth entry.")
        ],
        "inclusions": [
            "Full-day unlimited admission to all 21 water slides and pool attractions",
            "Complimentary use of park swim rings, double tubes, and certified life jackets",
            "Access to sand volleyball court, floating market, and sun loungers",
            "Comprehensive visitor insurance"
        ],
        "exclusions": [
            "Hotel transfers (available as optional roundtrip add-on)",
            "Locker, towel, and private poolside cabana rentals",
            "Food, beverages, and retail purchases"
        ],
        "timing_text": "Open daily (except Wednesdays) from 11:00 AM to 06:00 PM.<br />Slide operations close at 05:45 PM.",
        "transport_text": "Located 25 minutes south of Pattaya in the scenic Silverlake valley. Shared or private minivan transfers available.",
        "what_to_bring": "Swimwear without metal rivets, waterproof sunscreen, sunglasses, flip-flops, and a beach towel.",
        "contact_tour_param": "Ramayana+Water+Park+Pattaya+Tickets",
        "faqs": [
            ("Why is Ramayana considered the cleanest water park in Thailand?", "Ramayana sources all its water from on-site deep mineral wells and purifies it through advanced multi-stage filtration systems without relying on harsh chemicals, making the water gentle on sensitive skin and eyes."),
            ("Are there height or weight restrictions on the big slides?", "Yes, most high-thrill slides require a minimum height of 122 cm. Dedicated children's zones accommodate young adventurers under 122 cm with gentler slides and splash fountains."),
            ("Can we rent private cabanas at the park?", "Yes, private shaded poolside cabanas equipped with ceiling fans, electrical outlets, and towel service can be booked for families desiring extra privacy and comfort."),
            ("Are vegetarian, vegan, and halal meals available?", "Yes, Ramayana's food court features certified halal food stations, vegetarian, Western, and authentic Thai cuisine prepared fresh daily.")
        ]
    },
    {
        "filename": "underwater_world_pattaya.html",
        "title": "Underwater World Pattaya Aquarium Tickets & Tunnel Tour | Trippovention",
        "h1": "Underwater World Pattaya",
        "subtitle": "100-Meter Acrylic Tunnel, 5,000+ Marine Animals, Touch Pools & Shark Feeding",
        "meta_desc": "Explore Underwater World Pattaya with tickets from Trippovention. Walk through the 100-meter underwater tunnel with sharks, giant stingrays, and coral reefs.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_underwater_world_pattaya.webp",
        "duration": "2–3 Hours",
        "price": "THB 650",
        "price_note": "(Per Person)",
        "meetup": "Sukhumvit Road, South Pattaya",
        "overview_p1": "Underwater World Pattaya is Thailand's first modern indoor oceanarium, home to an extraordinary collection of over 5,000 aquatic animals representing 500 diverse marine species native to the Gulf of Thailand and the South China Sea.",
        "overview_p2": "The centerpiece of the aquarium is a 100-meter-long, 180-degree curved acrylic pedestrian tunnel divided into three distinct underwater zones: Coral Reef Zone, Shark and Stingray Zone, and Giant of Siam Zone featuring a submerged ancient shipwreck. Watch blacktip reef sharks, nurse sharks, and majestic eagle rays glide effortlessly overhead.",
        "places_col1_title": "Tunnel Zones",
        "places_col1_badge": "Marine Life",
        "places_col1_items": [
            ("Shark & Ray Zone", "Experience heart-pounding views of apex predators, nurse sharks, shovel-nose rays, and blacktip reef sharks swimming overhead."),
            ("Coral Reef Zone", "Vibrant living display of tropical corals, clownfish, angelfish, and delicate sea anemones in brilliant colors."),
            ("Giant of Siam Zone", "Themed around a mystical sunken shipwreck, home to giant freshwater arapaimas, Mekong giant catfish, and sea turtles.")
        ],
        "places_col2_title": "Interactive Encounters",
        "places_col2_badge": "Hands-On Fun",
        "places_col2_items": [
            ("Touch Pool Experience", "Safely touch sea cucumbers, blue-spotted stingrays, starfish, and horseshoe crabs under marine staff guidance."),
            ("Scheduled Feeding Shows", "Watch scuba divers swim inside the main oceanarium tanks to hand-feed hungry sharks and stingrays twice daily."),
            ("Koi Fish Bottle Feeding", "Delight young children with the unique experience of nursing hungry koi fish with specially prepared milk bottles.")
        ],
        "inclusions": [
            "Official entrance admission ticket to Underwater World Pattaya",
            "Access to all aquarium exhibition tunnels and interactive touch zones",
            "Admission to all scheduled public feeding shows",
            "Travel accident insurance"
        ],
        "exclusions": [
            "Roundtrip hotel transfers (can be booked as an add-on)",
            "Scuba diving with sharks experience (advance reservation required)",
            "Koi bottle feeding food tokens (nominal on-site fee)",
            "Souvenirs and refreshments"
        ],
        "timing_text": "Open daily from 09:00 AM to 06:00 PM.<br />Last admission ticket sold at 05:30 PM.",
        "transport_text": "Conveniently located on Sukhumvit Highway in South Pattaya, easily reachable by local Songthaew or private taxi.",
        "what_to_bring": "Comfortable indoor walking shoes, camera (flash photography disabled in tunnels), and light jacket for air-conditioned exhibits.",
        "contact_tour_param": "Underwater+World+Pattaya+Tickets",
        "faqs": [
            ("When are the shark feeding shows held?", "Diver feeding presentations typically take place daily at 11:00 AM, 02:00 PM, and 04:00 PM in the Shark & Stingray Zone and Coral Reef Zone."),
            ("How long does it take to see the whole aquarium?", "Most visitors spend between 1.5 to 2 hours exploring the walk-through tunnels, touch pool, and watching the scheduled feeding demonstrations."),
            ("Is Underwater World fully wheelchair and stroller accessible?", "Yes, the facility is designed on a gentle continuous incline with zero stairs, making it 100% accessible for strollers, wheelchairs, and senior travelers."),
            ("Can certified divers swim with the sharks here?", "Yes, Underwater World offers an exclusive 'Dive with Sharks & Rays' program for certified scuba divers. Advance booking through Trippovention is required.")
        ]
    },
    {
        "filename": "pattaya_dolphinarium_show.html",
        "title": "Pattaya Dolphinarium Dolphin & Seal Show Tickets | Trippovention",
        "h1": "Pattaya Dolphinarium Dolphin & Seal Show",
        "subtitle": "European-Standard Marine Mammal Performance, Acrobatic Dolphins & Fur Seals",
        "meta_desc": "Experience the spectacular dolphin and South American fur seal show at Pattaya Dolphinarium. Enjoy acrobatic stunts, synchronized leaps, and photo sessions.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_dolphinarium.webp",
        "duration": "1.5–2 Hours (50-min show)",
        "price": "THB 800",
        "price_note": "(Per Person)",
        "meetup": "Dolphinarium Complex (Near Motorway 7), Pattaya",
        "overview_p1": "Pattaya Dolphinarium is widely recognized as one of Southeast Asia's modern, European-standard marine mammal facilities. Designed by international marine specialists, the state-of-the-art amphitheatre hosts world-class acrobatic displays that showcase the intelligence, agility, and playful nature of dolphins and fur seals.",
        "overview_p2": "During the 50-minute performance, audience members are treated to synchronized leaps, aerial spins, hoop jumps, balancing acts, and musical interactions between marine mammals and their passionate trainers. Optional VIP seating puts you right at the edge of the water for splash-zone excitement.",
        "places_col1_title": "Performance Highlights",
        "places_col1_badge": "Spectacular Show",
        "places_col1_items": [
            ("Bottlenose Dolphin Acrobatics", "High-flying leaps reaching several meters into the air, tail-walks, basketball hoops, and synchronized underwater choreography."),
            ("South American Fur Seals", "Charming comedic routines, flipper clapping, ball balancing, and interactions with the audience by adorable trained fur seals."),
            ("Trainer Synergy", "Witness the deep bond of trust and positive reinforcement training between international coaches and their marine partners.")
        ],
        "places_col2_title": "Special Programs",
        "places_col2_badge": "Memorable Upgrades",
        "places_col2_items": [
            ("Photo with Dolphins", "Cherish a close-up keepsake photo sitting right beside a smiling dolphin on the stage platform after the show."),
            ("Swimming with Dolphins", "Unique once-in-a-lifetime program allowing guests to swim and play in the pool alongside friendly dolphins (advance booking required)."),
            ("Covered Amphitheatre", "Modern sheltered stadium seating ensuring 100% weather protection from sun or rain with clear sightlines.")
        ],
        "inclusions": [
            "Official reserved admission ticket to the 50-minute Dolphin & Seal Show",
            "Access to chosen seating category (Regular, Deluxe, or VIP)",
            "Covered amphitheatre seating",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Roundtrip hotel transfers (available on request)",
            "Post-show personal photo session with dolphins (optional add-on)",
            "Swimming with dolphins program",
            "Snacks, drinks, and souvenir merchandise"
        ],
        "timing_text": "Three daily shows: 11:00 AM, 02:00 PM, and 05:00 PM.<br />Closed on Wednesdays. Doors open 30 minutes before showtime.",
        "transport_text": "Located near Highway 7 in Nong Prue, Bang Lamung, approximately 15 minutes drive from Central Pattaya.",
        "what_to_bring": "Comfortable casual clothes, light jacket (if seated in splash zone), camera, and booking voucher.",
        "contact_tour_param": "Pattaya+Dolphinarium+Show+Tickets",
        "faqs": [
            ("What is the difference between Regular, Deluxe, and VIP seats?", "Regular seats occupy the upper rows (Rows 6–7). Deluxe seats are located in the middle rows (Rows 3–5) offering balanced panoramic views. VIP seats are in Rows 1–2 right at the pool's edge with prime viewing (complimentary rain ponchos provided)."),
            ("Can children swim with the dolphins?", "Yes, children aged 6 and above can participate in the 'Swimming with Dolphins' program accompanied by an adult, provided they are comfortable in deep water."),
            ("Are photos permitted during the performance?", "Yes, non-commercial photography and video recording from your seat are permitted throughout the performance. Flash photography is prohibited for animal safety."),
            ("Is the venue sheltered from rain and sun?", "Yes, the entire 1,000-seat amphitheatre is fully sheltered with a modern canopy roof, providing comfortable shaded seating in any weather.")
        ]
    },
    {
        "filename": "tiffanys_show_pattaya.html",
        "title": "Tiffany's Show Pattaya World-Class Cabaret Tickets | Trippovention",
        "h1": "Tiffany's Show Pattaya",
        "subtitle": "The Original Transgender Cabaret of Southeast Asia, Opulent Costumes & Broadway Stages",
        "meta_desc": "Reserve Tiffany's Show Pattaya tickets. Southeast Asia's pioneer cabaret spectacular featuring glamorous Broadway-style sets, extravagant costumes, and theatrical music.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_tiffanys_show_pattaya.webp",
        "duration": "1.5 Hours (75-min show)",
        "price": "THB 1,200",
        "price_note": "(Per Person)",
        "meetup": "Tiffany's Theatre, Pattaya Second Road, North Pattaya",
        "overview_p1": "Established in 1974, Tiffany's Show Pattaya is the legendary pioneer of transgender cabaret entertainment in Southeast Asia. Voted among the top 10 world cabaret shows, Tiffany's has dazzled international audiences for over five decades with theatrical artistry, grandeur, and precision choreography.",
        "overview_p2": "Staged inside a palatial 1,000-seat theatre equipped with advanced acoustics, hydraulic stages, and LED backdrops, over 100 glamorous performers present an international songbook spanning Broadway classics, Chinese imperial legends, Bollywood extravaganzas, and traditional Thai court dance.",
        "places_col1_title": "Musical & Theatrical Acts",
        "places_col1_badge": "World-Class Repertoire",
        "places_col1_items": [
            ("Imperial China & Empress Act", "Majestic palace sets with intricate silk costumes, golden dragons, and classical fan dancing."),
            ("Broadway & Hollywood Glitz", "Energetic high-kicking showgirl numbers paying tribute to New York Broadway and classic cinema icons."),
            ("Siam Heritage & Royal Dance", "Graceful classical Thai choreography celebrating ancient Siamese royal folklore and golden chedis.")
        ],
        "places_col2_title": "Theatre & Production",
        "places_col2_badge": "Grand Production",
        "places_col2_items": [
            ("Palatial 1,000-Seat Theatre", "Opulent European-style auditorium with plush tiered seating, state-of-the-art surround sound, and laser lighting."),
            ("Elaborate Feather Costumes", "Spectacular handmade costumes adorned with hundreds of thousands of Swarovski crystals and ostrich feathers."),
            ("Post-Show Photo Courtyard", "Meet the star performers in the open-air fountain plaza after the finale for unforgettable souvenir photos.")
        ],
        "inclusions": [
            "Official admission ticket to 75-minute Tiffany's Show Pattaya",
            "Reserved theatre seating (Mezzanine, VIP, or VIP Gold)",
            "Complimentary soft drink before entering the auditorium",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Hotel pickup and drop-off (can be booked as optional private transfer)",
            "Tips for performers during post-show plaza photos (customary 50–100 THB)",
            "Alcoholic beverages and personal snacks"
        ],
        "timing_text": "Daily performances at 06:00 PM and 07:30 PM.<br />Additional 09:00 PM show on weekends and peak holidays.",
        "transport_text": "Located on Pattaya Second Road, North Pattaya. Within walking distance of Terminal 21 Pattaya.",
        "what_to_bring": "Smart casual attire (dress code prohibits sleeveless vests and beach swimwear) and camera for post-show plaza photos.",
        "contact_tour_param": "Tiffanys+Show+Pattaya+Tickets",
        "faqs": [
            ("What are the differences between seating tiers at Tiffany's?", "Mezzanine seats are on the elevated balcony. VIP seats are located on the ground floor providing excellent direct sightlines. VIP Gold seats occupy the front-central rows closest to the stage with the best view of detailed costumes and makeup."),
            ("Is photography allowed during the show?", "Photography and video recording inside the auditorium are strictly prohibited during the performance to respect copyright and artist safety. However, photo sessions in the outdoor courtyard after the show are welcomed!"),
            ("Is Tiffany's Show suitable for families with children?", "Yes, Tiffany's is a glamorous, family-friendly celebration of music, cultural dance, and theatrical costuming with no vulgar or adult content."),
            ("How early should we arrive before showtime?", "We recommend arriving at the theatre lobby at least 20 to 30 minutes before the scheduled curtain call to redeem your tickets and enjoy your welcome beverage.")
        ]
    },
    {
        "filename": "colosseum_cabaret_show_pattaya.html",
        "title": "Colosseum Cabaret Show Pattaya Tickets & Transfers | Trippovention",
        "h1": "Colosseum Cabaret Show Pattaya",
        "subtitle": "Roman Amphitheatre-Inspired Theatre, 14 Themed Acts & High-Tech Stage Effects",
        "meta_desc": "Book Colosseum Show Pattaya tickets with Trippovention. Enjoy 14 magnificent musical dance acts in Pattaya's largest Roman colosseum-style theatre.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_colosseum_cabaret_show.webp",
        "duration": "1.5 Hours (75-min show)",
        "price": "THB 850",
        "price_note": "(Per Person)",
        "meetup": "The Colosseum Theatre, Thepprasit Road, South Pattaya",
        "overview_p1": "Housed in a breathtaking 17-acre complex inspired by the ancient Roman Colosseum, Colosseum Cabaret Pattaya is the largest and most architecturally striking theatre in Pattaya. With 1,250 amphitheatre seats arranged in a progressive horseshoe curve, every seat guarantees unobstructed sightlines.",
        "overview_p2": "Colosseum presents 14 dynamic, kaleidoscope acts blending contemporary pop, traditional Asian cultural narratives, European opera, and laugh-out-loud comedy. Powered by dynamic hydraulic lift stages, computerized lighting, and opulent custom wardrobe, it is a magnificent evening showpiece.",
        "places_col1_title": "Kaleidoscopic Acts",
        "places_col1_badge": "14 Spectacular Scenes",
        "places_col1_items": [
            ("Love on Top & Disco Finale", "High-energy pop tributes with breathtaking dance routines and shimmering sequined ensembles."),
            ("The Legend of Silk & Lotus", "Enchanting traditional Asian choreography celebrating Chinese court beauty and lotus blossom mythology."),
            ("Roman Gladiator Overture", "Dramatic theatrical opening act paying homage to ancient Rome and the iconic Colosseum architecture.")
        ],
        "places_col2_title": "Theatre Architecture",
        "places_col2_badge": "Grand Amphitheatre",
        "places_col2_items": [
            ("Horseshoe Amphitheatre Design", "Tiered circular seating layout ensuring superior sightlines and acoustic resonance from every angle."),
            ("Hydraulic Stage Machinery", "Multi-level mechanical stages that raise and lower elaborate sets and cast members seamlessly."),
            ("Courtyard Plaza Meet & Greet", "Spacious Roman-columned forecourt where guests can meet performers for photographs after the show.")
        ],
        "inclusions": [
            "Official reserved admission ticket to Colosseum Show Pattaya (75 minutes)",
            "Reserved theatre seat in Deluxe or VIP tier",
            "Welcome soft drink",
            "Travel accident insurance"
        ],
        "exclusions": [
            "Hotel pickup and drop-off (available as optional private transfer)",
            "Gratuities for performers during post-show photo session",
            "Personal food and beverages"
        ],
        "timing_text": "Two daily evening performances: 06:00 PM and 07:30 PM.<br />Doors open 30 minutes prior to showtime.",
        "transport_text": "Thepprasit Road, South Pattaya (near Thepprasit Night Market). Easy access by taxi or Songthaew.",
        "what_to_bring": "Smart casual dress, camera for post-show plaza photos, and small Thai Baht notes for performer tips.",
        "contact_tour_param": "Colosseum+Cabaret+Show+Pattaya",
        "faqs": [
            ("How does Colosseum compare to Alcazar or Tiffany's?", "Colosseum features Pattaya's largest and newest purpose-built amphitheatre, with an iconic Roman exterior and slightly steeper tiered seating, meaning even rear seats enjoy completely unobstructed views over heads in front."),
            ("Can we combine the Colosseum Show with dinner?", "Yes! Located right on Thepprasit Road, many visitors pair the 06:00 PM show with an evening stroll and dinner at the famous Thepprasit Weekend Night Market nearby."),
            ("Is Colosseum wheelchair accessible?", "Yes, the theatre features wheelchair ramps at the entrance and dedicated accessible seating areas on the ground floor."),
            ("Are children permitted to attend?", "Yes, Colosseum is an all-ages theatrical musical show suitable for children, couples, and seniors alike.")
        ]
    },
    {
        "filename": "max_muay_thai_stadium_tickets.html",
        "title": "Max Muay Thai Stadium Pattaya Live Fight Tickets | Trippovention",
        "h1": "Max Muay Thai Stadium Live Fights",
        "subtitle": "Raw Ringside Action, Authentic Muay Thai Fighters & Electric Stadium Atmosphere",
        "meta_desc": "Watch real, hard-hitting live Muay Thai bouts at Max Muay Thai Stadium in Pattaya. Ringside and stadium seats with hotel transfer options.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_max_muay_thai_stadium.webp",
        "duration": "2–3 Hours",
        "price": "THB 1,500",
        "price_note": "(Per Person)",
        "meetup": "Max Muay Thai Stadium, Sukhumvit Road, Central Pattaya",
        "overview_p1": "Experience the thunderous adrenaline and martial heritage of Thailand's national sport at Max Muay Thai Stadium, Pattaya's premier venue for authentic, televised combat sports. Unlike staged exhibitions, Max Muay Thai showcases real, hard-fought professional bouts sanctioned by world Muay Thai authorities.",
        "overview_p2": "Feel the vibration of the canvas from your ringside seat as elite Thai and international contenders trade devastating kicks, lightning elbows, and powerful clinches. Accompanied by the haunting rhythms of live traditional Sarama fight music (piphat), the stadium erupts with raw energy that will leave you on the edge of your seat.",
        "places_col1_title": "Fight Night Features",
        "places_col1_badge": "Real Combat",
        "places_col1_items": [
            ("3 to 5 Professional Bouts", "Full-contact championship matchups between top-ranked Thai warriors and international fighters."),
            ("Wai Kru Ram Muay Ritual", "Ancient spiritual pre-fight dance paying respect to teachers, ancestors, and the art of eight limbs."),
            ("Live Traditional Sarama Music", "Live ringside musicians playing the Javanese oboe, drums, and cymbals to dictate the rising pace of combat.")
        ],
        "places_col2_title": "Stadium Experience",
        "places_col2_badge": "Electric Energy",
        "places_col2_items": [
            ("Ringside & VIP Seating", "Sit just feet away from the action where you can hear every strike and feel the sweat and intensity up close."),
            ("Televised Broadcast Setup", "High-definition stadium screens, professional lighting, and English live fight commentary."),
            ("Photo with Fighters", "Meet champion fighters after their bouts for memorable ringside photos with championship belts.")
        ],
        "inclusions": [
            "Official admission ticket to Max Muay Thai Stadium fight night",
            "Reserved seat (Stadium Seating or Ringside VIP based on selection)",
            "Access to all 3–5 scheduled fight bouts",
            "Visitor accident insurance"
        ],
        "exclusions": [
            "Hotel transfers (can be added as an optional transfer add-on)",
            "Food, beers, and alcoholic beverages inside stadium",
            "Personal souvenirs"
        ],
        "timing_text": "Live fight nights run daily from 07:00 PM to 09:30 PM.<br />Stadium doors open at 06:30 PM.",
        "transport_text": "Sukhumvit Road (near Central Pattaya Road intersection), Central Pattaya. Readily accessible by taxi.",
        "what_to_bring": "Casual attire, ear protection for very young children, and camera (flash disabled during bouts).",
        "contact_tour_param": "Max+Muay+Thai+Stadium+Fight+Tickets",
        "faqs": [
            ("Are these fights real or choreographed?", "Max Muay Thai features 100% genuine, competitive professional fights. Boxers train rigorously and fight full-contact with real knockouts, points scoring, and championship purses."),
            ("What is the difference between Stadium and Ringside tickets?", "Stadium tickets provide elevated grandstand views overlooking the ring with great overall atmosphere. Ringside VIP seats put you in the first few rows directly beside the ring for maximum proximity to the action."),
            ("Is food and beer available at the stadium?", "Yes, the stadium has concession stands serving cold Thai beer, soft drinks, popcorn, and snacks during the bouts."),
            ("Is Max Muay Thai suitable for teenagers or families?", "Yes, many sports-loving families and teenagers attend. However, because fights are real full-contact martial arts with occasional blood or knockouts, parental discretion is advised for very young children.")
        ]
    },
    {
        "filename": "khao_kheow_open_zoo_tour.html",
        "title": "Khao Kheow Open Zoo Excursion Pattaya with Transfers | Trippovention",
        "h1": "Khao Kheow Open Zoo Excursion",
        "subtitle": "2,000-Acre Wildlife Safari, Open Habitats, Green Valley Tram & Pygmy Hippos",
        "meta_desc": "Day trip from Pattaya to Khao Kheow Open Zoo. Travel through sprawling open wildlife habitats, home to pygmy hippos, white lions, rhinos, giraffes, and lemurs.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_khao_kheow_open_zoo.webp",
        "duration": "5–6 Hours",
        "price": "THB 1,350",
        "price_note": "(Per Person)",
        "meetup": "Pattaya Hotel Pickup (Roundtrip Transfer Included)",
        "overview_p1": "Nestled inside a lush protected rainforest reserve in Chonburi, Khao Kheow Open Zoo is Thailand's largest and most celebrated wildlife conservation park. Spanning over 2,000 acres, this open-concept zoo provides natural, barrier-free habitats for more than 8,000 animals across 300 worldwide species.",
        "overview_p2": "The zoo has captured global adoration as the home of world-famous pygmy hippo 'Moo Deng'. Ride the scenic hop-on hop-off open safari tram through themed bioclimatic zones including the African Savanna, Asian Forest, Australian Outback, and Cats Complex, enjoying respectful feeding opportunities with giraffes, rhinos, and hippos.",
        "places_col1_title": "Top Wildlife Encounters",
        "places_col1_badge": "Global Sensation",
        "places_col1_items": [
            ("Pygmy Hippo Enclosure", "Visit the famous home of viral sensation Moo Deng and the adorable pygmy hippo family splashing in their jungle stream pool."),
            ("African Savanna", "Expansive open grassland where giraffes, zebras, white rhinos, and ostriches roam harmoniously together."),
            ("Walk-Through Aviary", "Huge netted rainforest dome home to hundreds of exotic hornbills, flamingos, and vibrant tropical birds.")
        ],
        "places_col2_title": "Safari Exploration",
        "places_col2_badge": "Open Nature",
        "places_col2_items": [
            ("Hop-On Hop-Off Safari Tram", "Panoramic open-air electric tram linking all major wildlife zones throughout the scenic 2,000-acre hillsides."),
            ("Lemur Island Experience", "Take a short raft across the moat to interact with friendly ring-tailed lemurs from Madagascar."),
            ("Feeding Terraces", "Hand-feed fresh string beans and bananas to towering giraffes, rhinos, and gentle Asian elephants.")
        ],
        "inclusions": [
            "Official entrance admission ticket to Khao Kheow Open Zoo",
            "Round-trip air-conditioned hotel transfers from central Pattaya",
            "Hop-on hop-off open safari tram ticket within the zoo",
            "Bottled drinking water",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Animal feed baskets (available for purchase on-site for 30–50 THB)",
            "Golf cart self-drive rental (optional on-site rental with valid driver's license)",
            "Lunch and refreshments",
            "Driver gratuities"
        ],
        "timing_text": "Morning Tour: 08:30 AM – 02:00 PM | Afternoon Tour: 01:00 PM – 06:30 PM.<br />Daily departures.",
        "transport_text": "Round-trip shared or private air-conditioned minivan transfer from central Pattaya hotels (approx. 45 min drive).",
        "what_to_bring": "Comfortable walking shoes, sun hat, sunglasses, insect repellent, camera, and cash for animal feeding baskets.",
        "contact_tour_param": "Khao+Kheow+Open+Zoo+Excursion",
        "faqs": [
            ("Can we see Moo Deng the famous pygmy hippo?", "Yes! Moo Deng and the pygmy hippo family reside in the Zoo's Zone 1. Morning visits between 09:00 AM and 10:30 AM or afternoon feeding times are best to catch her playful antics in the water."),
            ("How large is the zoo and is walking required?", "Khao Kheow is huge (over 2,000 acres). Our package includes the zoo's open-air tram which stops at all major animal pavilions, so you only need to walk short distances around each enclosure."),
            ("Can visitors rent golf carts inside the zoo?", "Yes, 4-seat and 6-seat electric golf carts are available for hire near the entrance for guests wishing to drive themselves (requires a valid physical driver's license)."),
            ("Is this tour suitable for elderly travelers and toddlers?", "Extremely suitable! The park is peaceful, clean, and lush with plenty of shaded seating and easy accessibility via the zoo tram.")
        ]
    },
    {
        "filename": "pattaya_elephant_sanctuary_tour.html",
        "title": "Ethical Elephant Sanctuary Experience Pattaya | Trippovention",
        "h1": "Pattaya Elephant Sanctuary Experience",
        "subtitle": "Ethical Rescued Elephant Interaction, Fruit Preparation, Mud Spa & River Walk",
        "meta_desc": "Experience a truly ethical elephant encounter in Pattaya. Prepare nutrient-rich fruit balls, join elephants for a mud spa and natural bath without riding.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_elephant_sanctuary.webp",
        "duration": "4–5 Hours",
        "price": "THB 2,200",
        "price_note": "(Per Person)",
        "meetup": "Pattaya Hotel Pickup (Air-Conditioned Shared Transfer)",
        "overview_p1": "Immerse yourself in a compassionate, ethical wildlife encounter at Pattaya Elephant Sanctuary. Dedicated to the rescue, rehabilitation, and respectful care of retired elephants from the logging and tourism industries, the sanctuary operates on a strictly hands-off, no-riding philosophy.",
        "overview_p2": "Spend your morning or afternoon learning about Asian elephant biology and behavior from conservation guides. Prepare fresh dietary supplements of bananas, sugarcane, and nutrient herbal balls, feed the gentle giants by hand, and walk alongside them to a natural mud spa and freshwater bathing pool.",
        "places_col1_title": "Sanctuary Activities",
        "places_col1_badge": "Hands-On Care",
        "places_col1_items": [
            ("Elephant Kitchen", "Chop fresh bananas, sugarcane, and blend herbal rice balls tailored for elder rescued elephants with worn teeth."),
            ("Gentle Feeding Session", "Experience the wonder of interacting with elephants up close as they take treats directly from your hands with their sensitive trunks."),
            ("Mud Spa & Skin Care", "Apply cooling natural mineral mud to elephant skin to protect them from insects and the tropical sun.")
        ],
        "places_col2_title": "Natural Living",
        "places_col2_badge": "Ethical Freedom",
        "places_col2_items": [
            ("Freshwater Bathing Pool", "Join the elephants in the natural pond or watch them happily splash, roll, and submerge themselves in the water."),
            ("Jungle Canopy Walk", "Accompany the herd as they wander freely through open bamboo groves and forage naturally."),
            ("Educational Workshop", "Insightful presentation on elephant rescue, conservation challenges, and the evolution of animal welfare in Thailand.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transfers from Pattaya",
            "Fresh ingredients for elephant food and fruit preparation",
            "Traditional mahout clothing / protective shirts for activities",
            "Delicious Thai buffet lunch or afternoon vegetarian refreshments",
            "Professional English-speaking sanctuary educator",
            "Locker and shower facilities with clean towels",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Elephant riding (strictly prohibited at ethical sanctuaries)",
            "Personal spending and souvenir photography purchases",
            "Guide and driver gratuities"
        ],
        "timing_text": "Morning Program: 08:00 AM – 12:30 PM | Afternoon Program: 01:00 PM – 05:30 PM.<br />Daily small-group sessions.",
        "transport_text": "Shared air-conditioned minivan pickup directly from your hotel lobby in Pattaya.",
        "what_to_bring": "Swimwear (to wear under provided clothes), change of dry clothes, sandals or water shoes, sunscreen, insect repellent, and camera.",
        "contact_tour_param": "Pattaya+Elephant+Sanctuary+Experience",
        "faqs": [
            ("Does the sanctuary permit elephant riding?", "No, under no circumstances. We strictly partner with authentic ethical sanctuaries that prioritize elephant health, autonomy, and dignity. Activities focus solely on observing, feeding, and caring for rescued animals."),
            ("Are there shower facilities to clean off mud after the bath?", "Yes! The sanctuary provides clean private showers, soap, shampoo, and fresh towels so you can comfortably rinse off before enjoying your meal and returning to your hotel."),
            ("Is the program safe for children?", "Yes, the rescued elephants at the sanctuary are gentle, habituated to human presence, and supervised by experienced mahouts at all times. Children of all ages love feeding and touching the elephants."),
            ("What should I wear for this experience?", "Wear clothes you don't mind getting dirty. The sanctuary provides lightweight protective cotton shirts to wear over your swimwear during the mud spa session.")
        ]
    },
    {
        "filename": "art_in_paradise_pattaya.html",
        "title": "Art in Paradise Pattaya 3D Optical Illusion Museum | Trippovention",
        "h1": "Art in Paradise 3D Museum",
        "subtitle": "Interactive 3D Optical Illusion Gallery, AR Smartphone App & Themed Zones",
        "meta_desc": "Immerse yourself in 140+ interactive 3D trompe-l'œil paintings at Art in Paradise Pattaya. Pose inside surreal landscapes, safari scenes, and classic art parodies.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_art_in_paradise_pattaya.webp",
        "duration": "2 Hours",
        "price": "THB 450",
        "price_note": "(Per Person)",
        "meetup": "Pattaya Second Road (North Pattaya)",
        "overview_p1": "Art in Paradise Pattaya is Thailand's first and largest interactive 3D art museum, spanning 5,800 square meters across an air-conditioned modern facility in North Pattaya. Created by talented Korean and Thai artists, the gallery features more than 140 photorealistic trompe-l'œil paintings.",
        "overview_p2": "Unlike traditional museums where touching art is forbidden, visitors here become part of the masterpieces! Stand on marked camera photo spots to capture mind-bending optical illusions. Download the museum's companion AR (Augmented Reality) app on your smartphone to watch paintings come to life with animations and sound effects on your video screen.",
        "places_col1_title": "Interactive Themed Zones",
        "places_col1_badge": "Creative Photo Fun",
        "places_col1_items": [
            ("Underwater World Zone", "Pose inside the jaws of a prehistoric megalodon shark or swim alongside giant sea turtles and mermaids."),
            ("Wildlife & Safari Zone", "Escape charging rhinoceroses, touch the trunk of an African elephant, or cross a rickety rope bridge over a canyon."),
            ("Classic Masterpiece Parody", "Insert yourself humorously into famous Western paintings including the Mona Lisa, The Creation of Adam, and Van Gogh's bedroom.")
        ],
        "places_col2_title": "Surreal & Fantasy Worlds",
        "places_col2_badge": "Illusion Art",
        "places_col2_items": [
            ("Fantasy & Magic Realm", "Float inside giant crystal bubbles, fly on flying carpets, or shrink into a miniature dollhouse world."),
            ("Dinosaur & Prehistoric Zone", "Flee from towering T-Rex jaws crashing through concrete museum walls."),
            ("AR Video Interaction", "Use the dedicated AR app to record videos where dragons breathe real fire and waterfalls roar realistically around you.")
        ],
        "inclusions": [
            "Official entrance admission ticket to Art in Paradise Pattaya",
            "Access to all 6 themed 3D illusion zones",
            "Free access to download and use the official AR interactive mobile app",
            "Visitor insurance coverage"
        ],
        "exclusions": [
            "Hotel transfers (readily accessible in central North Pattaya)",
            "Personal camera or smartphone (guests bring their own devices)",
            "Refreshments and cafe purchases"
        ],
        "timing_text": "Open daily from 09:30 AM to 08:00 PM.<br />Ticket counter closes at 07:00 PM.",
        "transport_text": "Located on Pattaya Second Road (Pattaya Sai 2), North Pattaya, near Terminal 21 Pattaya.",
        "what_to_bring": "Smartphone or digital camera with fully charged battery and plenty of storage, and casual comfortable shoes.",
        "contact_tour_param": "Art+in+Paradise+Pattaya+Tickets",
        "faqs": [
            ("How do the 3D photos work?", "Each mural has specific camera photo markers taped on the floor showing the photographer exactly where to stand and what camera angle to hold to produce the realistic 3D perspective effect."),
            ("Is the museum air-conditioned?", "Yes, the entire 5,800-square-meter complex is fully air-conditioned, making it a fantastic rainy-day activity or cool afternoon escape from the tropical heat."),
            ("How long does a visit usually take?", "Most visitors spend between 1.5 to 2.5 hours posing, taking photos, and recording interactive AR videos across the six gallery zones."),
            ("Is Art in Paradise suitable for all ages?", "Yes, toddlers, teenagers, couples, and grandparents all thoroughly enjoy the creative, hilarious photo setups.")
        ]
    },
    {
        "filename": "atv_off_road_adventure_pattaya.html",
        "title": "ATV Off-Road Adventure Tour Pattaya | Trippovention",
        "h1": "ATV Off-Road Adventure Pattaya",
        "subtitle": "Rugged Dirt Trails, Mud Tracks, Pineapple Plantations & Countryside Vistas",
        "meta_desc": "Conquer Pattaya's rugged backcountry on a guided ATV quad-bike tour. Ride through red-dirt tracks, jungle trails, mud ruts, and scenic pineapple farms.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_atv_off_road_adventure.webp",
        "duration": "2–3 Hours",
        "price": "THB 2,500",
        "price_note": "(Per Person / Driver)",
        "meetup": "Pattaya Base Camp (Includes Roundtrip Hotel Pickup)",
        "overview_p1": "Leave the crowded beaches behind and explore the wild, rugged side of Pattaya on an action-packed guided ATV quad-bike safari through Chonburi's picturesque countryside. Navigating deep jungle tracks, sandy trails, rutted hillsides, and sprawling pineapple and coconut plantations, this tour is pure off-road adrenaline.",
        "overview_p2": "Begin with a safety briefing and riding tutorial on a dedicated practice track to master your automatic, user-friendly ATV. Accompanied by professional lead and sweep trail guides, you will traverse diverse terrains tailored to your skill level, complete with splashing water crossings, panoramic hill lookouts, and mud-churning excitement.",
        "places_col1_title": "Trail Highlights",
        "places_col1_badge": "Off-Road Terrain",
        "places_col1_items": [
            ("Jungle Single-Tracks", "Twist and turn through dense tropical jungle foliage, bamboo tunnels, and shaded tree canopies."),
            ("Mud Pits & Water Splashes", "Splash through natural mud ruts, muddy pools, and water crossings for maximum off-road thrill."),
            ("Hilltop Viewpoint", "Ascend to elevated scenic ridgelines offering sweeping panoramic views across Pattaya's coastal hinterland.")
        ],
        "places_col2_title": "Equipment & Safety",
        "places_col2_badge": "Pro Equipment",
        "places_col2_items": [
            ("Automatic 300cc/450cc Quad Bikes", "Modern, fully automatic, easy-to-ride quad bikes suitable for beginners and experienced riders alike."),
            ("Full Safety Gear", "Certified safety helmets, goggles, and face dust masks provided for all participants."),
            ("Dedicated Practice Circuit", "Test track session under guide supervision to build throttle, braking, and steering confidence before hitting the trail.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transfers from Pattaya hotels",
            "Fully automatic ATV quad bike hire (2-hour guided trail ride)",
            "Safety helmet, riding goggles, and dust mask",
            "Professional English-speaking trail marshals and guides",
            "Chilled bottled drinking water and fresh seasonal fruit",
            "Full rider accident insurance coverage"
        ],
        "exclusions": [
            "Damage waiver deposit (nominal credit card pre-auth or cash bond)",
            "GoPro video rental (optional add-on)",
            "Personal refreshments and snacks",
            "Guide gratuities"
        ],
        "timing_text": "Morning Departures: 09:00 AM – 12:30 PM | Afternoon Departures: 02:00 PM – 05:30 PM.<br />Daily tours.",
        "transport_text": "Shared air-conditioned pickup and return directly from your Pattaya hotel lobby.",
        "what_to_bring": "Closed-toe shoes or sneakers (mandatory), clothes you don't mind getting muddy, change of clothes, sunglasses, and sunscreen.",
        "contact_tour_param": "ATV+Off-Road+Adventure+Pattaya",
        "faqs": [
            ("Do I need a motorcycle or driver's license to drive an ATV?", "No formal driver's license is required. The quad bikes are fully automatic (simple thumb throttle and hand brakes). All riders receive instruction and practice time before entering trails."),
            ("Can children ride as passengers?", "Yes, children aged 5 to 14 can ride comfortably as passengers on a tandem ATV behind an adult driver or professional guide at a discounted passenger rate."),
            ("What happens if it rains?", "Rain makes ATV riding even more fun! Rainy conditions create thrilling mud tracks, deeper water splashes, and cooler temperatures. Tours operate rain or shine, except during severe tropical thunderstorms."),
            ("Are shower facilities available after the ride?", "Yes, the off-road base camp provides clean shower cubicles, changing rooms, and lockers so you can wash off mud and change into fresh dry clothes before your hotel transfer.")
        ]
    },
    {
        "filename": "khao_chi_chan_and_wat_yan_tour.html",
        "title": "Khao Chi Chan & Wat Yansangwararam Tour Pattaya | Trippovention",
        "h1": "Khao Chi Chan & Wat Yansangwararam Tour",
        "subtitle": "109-Meter Golden Laser Buddha Mountain, Royal Temple Sanctuary & Viharn Sien",
        "meta_desc": "Tour Pattaya's cultural crown jewels: the 109-meter cliff-carved laser Buddha at Khao Chi Chan, the serene royal monastery of Wat Yansangwararam, and Viharn Sien.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_khao_chi_chan_buddha_mountain.webp",
        "duration": "4–5 Hours",
        "price": "THB 1,450",
        "price_note": "(Per Person)",
        "meetup": "Pattaya Hotel Pickup (Private or Small Group)",
        "overview_p1": "Escape the bustling coastal strip to discover the spiritual majesty and serene countryside of Southern Pattaya. This enriching half-day cultural tour showcases three of Chonburi's most revered cultural landmarks: Khao Chi Chan (Buddha Mountain), the royal monastery of Wat Yansangwararam, and the Viharn Sien Chinese museum temple.",
        "overview_p2": "Gaze up at the world's largest carved Buddha image at Khao Chi Chan, etched into a 109-meter limestone cliff face with precision laser technology and inlaid with 24-karat gold leaf to celebrate King Rama IX's Golden Jubilee. Continue to the tranquil lakeside grounds of Wat Yansangwararam to admire sacred Buddhist stupas, and finish at Viharn Sien to explore rare Terracotta Warrior replicas and antique jade artifacts.",
        "places_col1_title": "Spiritual Landmarks",
        "places_col1_badge": "Sacred Heritage",
        "places_col1_items": [
            ("Khao Chi Chan (Laser Buddha)", "Monumental 109-meter-high, 70-meter-wide golden seated Buddha silhouette etched into a sheer limestone cliff."),
            ("Wat Yansangwararam Woramahawihan", "Prestigious royal temple complex dedicated to the Supreme Patriarch, featuring serene lotus lakes, Chetiya stupas, and sacred relics."),
            ("Ariya Mettrai Viharn", "Sacred mountain chapel housing replicas of the holy footprints of the Buddha overlooking scenic gardens.")
        ],
        "places_col2_title": "Museum & Scenic Grounds",
        "places_col2_badge": "Art & History",
        "places_col2_items": [
            ("Viharn Sien (Anek Kuson Sala)", "Magnificent three-story Chinese palace museum displaying authentic Terracotta Army warriors, antique bronze sculptures, and Imperial art."),
            ("Silverlake Countryside Views", "Scenic drive through the surrounding European-style vineyard valley with panoramic views of rolling hills."),
            ("Landscaped Meditation Gardens", "Peaceful lakeside walking promenades surrounded by frangipani trees, shaded pavilions, and lotus ponds.")
        ],
        "inclusions": [
            "Official admission tickets to Khao Chi Chan, Wat Yansangwararam, and Viharn Sien",
            "Round-trip air-conditioned hotel transportation from Pattaya",
            "Licensed English-speaking cultural tour guide",
            "Chilled bottled drinking water",
            "Comprehensive travel accident insurance"
        ],
        "exclusions": [
            "Personal temple donations and merit-making offerings",
            "Food, lunch, and refreshments",
            "Guide and driver gratuities"
        ],
        "timing_text": "Morning Departures (08:30 AM – 01:00 PM) or Afternoon Departures (01:00 PM – 05:30 PM).<br />Daily departures.",
        "transport_text": "Air-conditioned private vehicle or modern minivan pickup directly from central Pattaya hotels.",
        "what_to_bring": "Modest clothing covering shoulders and knees (mandatory for temple grounds), slip-on comfortable shoes, sun hat, and camera.",
        "contact_tour_param": "Khao+Chi+Chan+and+Wat+Yansangwararam+Tour",
        "faqs": [
            ("What is the history behind Buddha Mountain (Khao Chi Chan)?", "The image was carved into the cliff in 1996 to commemorate the 50th anniversary of King Bhumibol Adulyadej's (Rama IX) accession to the throne. Using laser guidance, the design was cut into the rock face and filled with millions of Baht worth of pure gold leaf."),
            ("What is the dress code for Wat Yansangwararam and Viharn Sien?", "As these are active royal monasteries and sacred temples, modest attire covering shoulders and knees is strictly required for both men and women. No sleeveless shirts, tank tops, or short skirts."),
            ("Are real Terracotta Warriors on display at Viharn Sien?", "Yes! The Chinese government gifted several authentic replicas of the famous Terracotta Warriors, horses, and bronze chariots from Xi'an to Thailand, displayed on the second floor of Viharn Sien."),
            ("How far are these sights from central Pattaya?", "They are located in the Na Jomtien / Sattahip valley, approximately 25 to 30 minutes drive south of Central Pattaya.")
        ]
    },
    {
        "filename": "pattaya_city_landmarks_tour.html",
        "title": "Pattaya City Highlights & Landmarks Tour | Trippovention",
        "h1": "Pattaya City Highlights & Landmarks Tour",
        "subtitle": "Pratumnak Viewpoint, Wat Phra Yai Big Buddha, Pattaya Beach Road & Gems Gallery",
        "meta_desc": "Discover the best of Pattaya in half a day. Take in the crescent bay views from Pratumnak Viewpoint, ascend Wat Phra Yai's Golden Buddha, and cruise Beach Road.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_viewpoint_big_buddha.webp",
        "duration": "3–4 Hours",
        "price": "THB 850",
        "price_note": "(Per Person)",
        "meetup": "Pattaya Hotel Pickup",
        "overview_p1": "Get your bearings and discover the cultural highlights, panoramic vistas, and vibrant coastal character of Pattaya on this essential half-day orientation tour. Designed for first-time visitors and travelers wanting a hassle-free introduction, this journey combines the city's most famous panoramic lookouts with sacred spiritual temples.",
        "overview_p2": "Ascend Pratumnak Hill to Khao Pattaya Viewpoint for world-famous postcard vistas of Pattaya's crescent bay and bustling marina. Visit Wat Phra Yai to climb the grand Naga serpent staircase to the 18-meter golden Big Buddha, drive past vibrant Beach Road, and visit the World Gems Collection to see master gemstone cutters at work.",
        "places_col1_title": "City Lookouts & Temples",
        "places_col1_badge": "Iconic Sights",
        "places_col1_items": [
            ("Pratumnak Hill Viewpoint", "Pattaya's highest vantage point providing the quintessential postcard panorama of the crescent shoreline and Bali Hai Pier."),
            ("Wat Phra Yai (Big Buddha Hill)", "Ascend the golden seven-headed Naga dragon staircase to marvel at the towering 18-meter seated Buddha statue established in 1977."),
            ("Admiral Prince of Chumphon Shrine", "Revered hilltop monument honoring the founder of the Royal Thai Navy overlooking Pattaya Bay.")
        ],
        "places_col2_title": "Coastal Highlights & Culture",
        "places_col2_badge": "Local Orientation",
        "places_col2_items": [
            ("Pattaya Beach Road Drive", "Scenic coastal drive along the palm-fringed beachfront promenade and Walking Street gateway."),
            ("World Gems Museum & Dark Ride", "Fascinating theme-park style dark-ride train through the geological history of precious stones and showroom of master Thai jewellers."),
            ("Local Fruit Market Stop", "Opportunity to sample exotic seasonal fruits like sweet mangoes, mangosteens, and dragon fruit.")
        ],
        "inclusions": [
            "Round-trip air-conditioned hotel transportation from Pattaya hotels",
            "Professional English-speaking licensed sightseeing guide",
            "Admission to Wat Phra Yai and Khao Pattaya Viewpoint",
            "World Gems Museum thematic train ride",
            "Chilled bottled drinking water",
            "Travel accident insurance"
        ],
        "exclusions": [
            "Temple merit-making incense, flowers, or bell-ringing donations",
            "Personal souvenir shopping and food purchases",
            "Guide and driver gratuities"
        ],
        "timing_text": "Morning Tour: 09:00 AM – 12:30 PM | Afternoon Tour: 01:30 PM – 05:00 PM.<br />Daily departures.",
        "transport_text": "Shared air-conditioned minivan or private transport with direct pickup from your hotel lobby.",
        "what_to_bring": "Modest clothing covering shoulders and knees for temple entrance, comfortable slip-on walking shoes, sun hat, and camera.",
        "contact_tour_param": "Pattaya+City+Highlights+and+Landmarks+Tour",
        "faqs": [
            ("Is there a lot of walking or stair climbing on this tour?", "Walking is moderate. Reaching the Big Buddha on Pratumnak Hill involves climbing approximately 60 wide, gentle steps lined by dragon handrails. Guests with mobility challenges can take in views from the flat lower terrace."),
            ("What is the dress code for Wat Phra Yai?", "Modest dress is required out of respect for active Buddhist worshipers. Shoulders and knees must be covered. Avoid sleeveless tops or beachwear."),
            ("Can hotel pickup be arranged outside Central Pattaya?", "Complimentary pickup covers hotels in North, Central, and South Pattaya. Jomtien or Naklua pickups can be accommodated seamlessly with our team."),
            ("Is this tour good for our first day in Pattaya?", "Yes! This is the perfect first-day orientation tour to understand Pattaya's geography, history, and key viewpoints before planning independent activities.")
        ]
    },
    {
        "filename": "koh_larn_private_speedboat_tour.html",
        "title": "Koh Larn Private Speedboat Charter from Pattaya | Trippovention",
        "h1": "Koh Larn Private Speedboat Charter",
        "subtitle": "Exclusive Island Charter, Hidden Beaches, Crystal Waters & Custom Itinerary",
        "meta_desc": "Charter an exclusive private speedboat from Pattaya to Koh Larn (Coral Island). Visit secluded beaches (Tawaen, Tien, Samae) at your own schedule without crowds.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_koh_larn_private_speedboat.webp",
        "duration": "4–6 Hours",
        "price": "THB 7,500",
        "price_note": "(Per Boat / Up to 6 Pax)",
        "meetup": "Bali Hai Pier, Pattaya (Private Boarding)",
        "overview_p1": "Escape the crowded public ferries and rigid tour schedules with an exclusive private speedboat charter from Pattaya to Coral Island (Koh Larn). Cruising across turquoise waters at exhilarating speeds, your private vessel reaches pristine white-sand shores in just 15 to 20 minutes.",
        "overview_p2": "Enjoy complete freedom to customize your island day. Spend your morning swimming and relaxing at tranquil Tien Beach or secluded Nual Beach (Monkey Beach), cruise around hidden coves for reef snorkeling, dine at scenic seaside seafood restaurants, and add high-octane water sports on your own terms.",
        "places_col1_title": "Island Highlights",
        "places_col1_badge": "Tropical Beaches",
        "places_col1_items": [
            ("Tien Beach", "Scenic curved beach famous for crystal-clear aquamarine water, swaying palm trees, and charming wooden boardwalks."),
            ("Samae Beach", "Expansive soft white sand bay offering relaxed sunbeds, beachfront restaurants, and solar-powered eco windmill views."),
            ("Nual Beach (Monkey Beach)", "Tranquil secluded bay at the southern tip of Koh Larn where wild monkeys frequently visit the rocky shoreline.")
        ],
        "places_col2_title": "Private Charter Perks",
        "places_col2_badge": "VIP Freedom",
        "places_col2_items": [
            ("Exclusive Twin-Engine Speedboat", "Private vessel chartered solely for your party with dedicated captain and crew."),
            ("Snorkeling at Coral Coves", "Anchor at quiet reefs around Koh Larn or Koh Sak to snorkel among damselfish and parrotfish."),
            ("Flexible Timetable", "Choose your preferred departure and return times without waiting for group tour buses.")
        ],
        "inclusions": [
            "Exclusive private speedboat charter for your party (up to 6 passengers)",
            "Licensed professional boat captain and marine safety crew",
            "Certified life jackets and snorkeling masks/snorkels",
            "Chilled bottled drinking water and ice box on board",
            "Full boat marine insurance coverage"
        ],
        "exclusions": [
            "Pier transfer from hotel (available as private van add-on)",
            "Beach sunbed and umbrella rental on island (nominal fee 50–100 THB)",
            "Lunch and refreshments at island restaurants",
            "Optional water sports (parasailing, jet ski, banana boat)"
        ],
        "timing_text": "Flexible departure between 08:30 AM and 11:00 AM.<br />Charter duration up to 6 hours. Latest return to Pattaya by 05:00 PM.",
        "transport_text": "Boarding at Bali Hai Pier, South Pattaya. Private hotel transfers available upon request.",
        "what_to_bring": "Swimwear, beach towels, sunglasses, sun hat, waterproof phone pouch, and cash for island lunch/drinks.",
        "contact_tour_param": "Koh+Larn+Private+Speedboat+Charter",
        "faqs": [
            ("How many passengers can fit on the private speedboat?", "Our standard charter package accommodates up to 6 passengers comfortably. For larger groups or extended families, we offer 15-passenger and 30-passenger speedboats on request."),
            ("Can we choose which beaches to visit on Koh Larn?", "Yes! That is the primary advantage of a private charter. You can spend more time at quiet beaches like Tien or Nual Beach, or head to Tawaen Beach for water sports."),
            ("Can we bring our own food and alcoholic beverages on board?", "Yes, you are welcome to bring snacks, beer, wine, or soft drinks on board without corkage fees. We provide an ice-filled cooler box."),
            ("What if someone gets seasick?", "The crossing to Koh Larn takes only 15 to 20 minutes across generally sheltered Gulf waters. Motion sickness pills are available upon boarding if requested.")
        ]
    },
    {
        "filename": "pattaya_sunset_catamaran_cruise.html",
        "title": "Pattaya Sunset Catamaran Cruise & Island Snorkel | Trippovention",
        "h1": "Pattaya Sunset Catamaran Cruise",
        "subtitle": "Luxury Sailing Catamaran, Koh Phai Snorkeling, Sunset BBQ & Golden Hour",
        "meta_desc": "Sail into the Gulf of Thailand aboard a luxury catamaran cruise from Ocean Marina Pattaya. Enjoy snorkeling at Koh Phai, onboard BBQ dinner, and ocean sunset.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_sunset_catamaran_cruise.webp",
        "duration": "4–5 Hours (Afternoon to Sunset)",
        "price": "THB 2,400",
        "price_note": "(Per Person)",
        "meetup": "Ocean Marina Yacht Club, Na Jomtien, Pattaya",
        "overview_p1": "Experience the glamour and romance of the Gulf of Thailand aboard an elegant luxury sailing catamaran departing from Ocean Marina Yacht Club, Southeast Asia's premier marina facility. Leave the noisy city behind as billowed sails catch the afternoon sea breeze.",
        "overview_p2": "Lounge on spacious bow trampolines, swim and snorkel around uninhabited tropical islands with crystal-clear waters, try paddleboarding or onboard fishing, and savor a freshly prepared barbecue seafood dinner as the sun sinks into the horizon, bathing the sea in vivid amber, magenta, and gold.",
        "places_col1_title": "Island & Marine Exploration",
        "places_col1_badge": "Tropical Archipelago",
        "places_col1_items": [
            ("Koh Phai (Bamboo Island)", "Protected uninhabited island under the Royal Thai Navy featuring pristine coral reefs, sea anemones, and white sands."),
            ("Snorkeling & Paddleboarding", "Complimentary snorkel masks, fins, stand-up paddleboards, and inflatable floating mats."),
            ("Hand-Line Fishing", "Try traditional hand-line fishing from the stern under the guidance of friendly crew members.")
        ],
        "places_col2_title": "Onboard Luxury & Sunset",
        "places_col2_badge": "Golden Hour",
        "places_col2_items": [
            ("Bow Trampoline Sundecks", "Relax on open-air netting suspended directly above the ocean spray as the catamaran glides over waves."),
            ("Fresh Seafood BBQ Buffet", "Delicious onboard buffet featuring grilled prawns, chicken satay, fried rice, fresh salads, and seasonal fruits."),
            ("Sunset Golden Hour", "Unforgettable panoramic views of the glowing sun sinking into the Gulf of Thailand with chillout background music.")
        ],
        "inclusions": [
            "4 to 5-hour luxury catamaran sailing cruise",
            "Delicious onboard Thai and Western BBQ buffet dinner",
            "Free-flow soft drinks, iced tea, drinking water, and fresh fruits",
            "Snorkeling gear, life vests, stand-up paddleboards, and fishing gear",
            "National marine park admission / island landing fees",
            "Marine passenger insurance coverage"
        ],
        "exclusions": [
            "Hotel transfers to Ocean Marina (available as private van add-on)",
            "Beers, cocktails, and alcoholic beverages (available for purchase at onboard bar)",
            "Gratuities for boat crew"
        ],
        "timing_text": "Afternoon Departure: 01:30 PM boarding, sailing until 06:30 PM sunset.<br />Operates on scheduled days and private charter.",
        "transport_text": "Ocean Marina Yacht Club, Na Jomtien, Sukhumvit Road (approx. 20 min south of Pattaya).",
        "what_to_bring": "Swimwear, beach towel, sunglasses, sun hat, light jacket for the sea breeze after sunset, and camera.",
        "contact_tour_param": "Pattaya+Sunset+Catamaran+Cruise",
        "faqs": [
            ("Where does the catamaran depart from?", "The cruise boards at Ocean Marina Yacht Club in Na Jomtien, Pattaya. Our team can arrange round-trip hotel transfers directly to the marina pier."),
            ("Is the cruise suitable for non-swimmers?", "Yes! Sailing catamarans are twin-hulled vessels known for extreme stability and very little rocking motion. Non-swimmers can relax comfortably on sunbeds, enjoy the music, and use life jackets on floating mats."),
            ("Can I purchase alcoholic drinks on board?", "Yes, the yacht features a licensed bar stocked with cold beers, wine, sparkling champagne, and handcrafted cocktails at reasonable prices."),
            ("What happens in case of bad weather?", "Catamaran sails are subject to marine safety conditions. If seas are deemed unsafe by the marine department, the trip is rescheduled or refunded in full.")
        ]
    },
    {
        "filename": "scuba_diving_and_snorkeling_pattaya.html",
        "title": "Pattaya Scuba Diving & Snorkeling Day Trip | Trippovention",
        "h1": "Pattaya Scuba Diving & Snorkeling Day Trip",
        "subtitle": "Coral Island Reefs, HTMS Khram Shipwreck Dives & PADI Certified Divemasters",
        "meta_desc": "Dive and snorkel in Pattaya's tropical waters. Full-day boat excursion with 2 dives, PADI certified instructors, coral reefs, sea turtles, and buffet lunch.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_scuba_diving_snorkeling.webp",
        "duration": "Full Day (6–7 Hours)",
        "price": "THB 3,100",
        "price_note": "(Certified Diver) / THB 1,800 (Snorkeler)",
        "meetup": "Bali Hai Pier / Pattaya Hotel Pickup",
        "overview_p1": "Discover the vibrant underwater world of the Gulf of Thailand on a full-day scuba diving and snorkeling excursion to Pattaya's Near and Far Islands. Pattaya is historically Thailand's diving birthplace and is world-renowned for year-round diving conditions and spectacular military shipwreck dive sites.",
        "overview_p2": "Certified divers can explore famous sunken navy wrecks like the HTMS Khram and HTMS Kood alongside coral pinnacles teeming with sea turtles, barracudas, and stingrays. Non-certified travelers and families can enjoy guided introductory Discover Scuba dives or snorkel over shallow coral gardens accompanied by experienced PADI Divemasters.",
        "places_col1_title": "Top Dive Sites",
        "places_col1_badge": "World-Class Diving",
        "places_col1_items": [
            ("HTMS Khram & HTMS Kood Wrecks", "Spectacular scuttled naval vessels sitting in 15–30m depths encrusted in corals and schooling jacks."),
            ("Koh Rin (Far Islands)", "Premier outer island dive site featuring pristine soft coral walls, nurse sharks, and hawksbill sea turtles."),
            ("Koh Sak & Koh Larn Reefs", "Sheltered shallow bays with calm waters, ideal for colorful snorkel exploration and introductory scuba diving.")
        ],
        "places_col2_title": "Full-Day Comfort",
        "places_col2_badge": "Diving Comfort",
        "places_col2_items": [
            ("Spacious 20-Meter Dive Boat", "Custom dive vessel with sun deck, shaded saloon, gearing-up stations, freshwater showers, and marine toilets."),
            ("Hot Onboard Buffet Lunch", "Freshly cooked Thai buffet, hot tea, coffee, seasonal fresh tropical fruits, and chilled drinking water."),
            ("PADI Professional Supervision", "Small dive groups (maximum 4 divers per PADI Divemaster) ensuring personalized safety and attention.")
        ],
        "inclusions": [
            "Full-day boat excursion to Pattaya's Near or Far Islands (2 dive sites)",
            "Complete scuba diving equipment (BCD, regulator, wetsuit, mask, fins, weights, tanks)",
            "Certified PADI Divemaster / Instructor guiding",
            "Hot cooked buffet lunch, fruits, coffee, tea, and drinking water",
            "Snorkeling gear for non-diver companions",
            "Comprehensive dive accident insurance"
        ],
        "exclusions": [
            "Hotel transfers to pier (available as optional private transfer)",
            "Underwater digital photography service (optional on-board hire)",
            "Nitrox tank fills (available for certified Enriched Air divers)",
            "Crew gratuities"
        ],
        "timing_text": "Departure: 08:30 AM from Bali Hai Pier, returning by 03:30 PM.<br />Daily departures subject to marine conditions.",
        "transport_text": "Meeting at Bali Hai Pier, South Pattaya. Hotel transfers available upon request.",
        "what_to_bring": "Certification card and logbook (for certified divers), swimwear, beach towel, reef-safe sunscreen, sunglasses, and dry bag.",
        "contact_tour_param": "Pattaya+Scuba+Diving+and+Snorkeling+Trip",
        "faqs": [
            ("Can beginners without a dive license try scuba diving?", "Yes! We offer the 'PADI Discover Scuba Diving' program where complete beginners receive a safety briefing, shallow water skill practice, and 1-on-1 instructor guidance to dive to a maximum depth of 12 meters."),
            ("What marine life can we expect to encounter in Pattaya?", "Divers regularly spot green sea turtles, hawksbills, blue-spotted stingrays, moray eels, barracudas, batfish, cuttlefish, and diverse macro life including seahorses and nudibranchs."),
            ("How long must I wait after diving before flying?", "According to international PADI medical guidelines, divers must wait at least 18 hours after completing multi-dive profiles before boarding commercial aircraft flights."),
            ("Can non-diving family members join the boat as snorkelers?", "Absolutely! Non-divers and snorkelers can relax on the sun deck, swim in protected island bays, and enjoy the freshly prepared lunch.")
        ]
    },
    {
        "filename": "harborland_pattaya_tickets.html",
        "title": "HarborLand Pattaya Indoor Playground Day Pass | Trippovention",
        "h1": "HarborLand Indoor Playground Pattaya",
        "subtitle": "Asia's Premier Indoor Family Play Complex, Multi-Level Mega Slides & Trampolines",
        "meta_desc": "Treat your family to HarborLand Pattaya indoor playground at Harbor Mall. Featuring European-safety certified multi-tier climbing structures, slides, and ninja courses.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_harborland_indoor_playground.webp",
        "duration": "3–4 Hours",
        "price": "THB 580",
        "price_note": "(Child) / THB 240 (Adult)",
        "meetup": "Harbor Pattaya Mega-Mall, Central Pattaya Road",
        "overview_p1": "Hailed as one of the largest and safest indoor family edutainment complexes in Asia, HarborLand Pattaya spans multiple floors inside Harbor Pattaya Mega-Mall. Designed and manufactured strictly to stringent European Safety Standards (EN1176 and EN1177), it provides an extraordinary playground wonderland for kids from toddlers to teenagers.",
        "overview_p2": "Children can burn boundless energy on colossal multi-tier climbing towers, steep drop slides, giant spiral tube chutes, ball cannons, inflatable obstacle courses, and soft-foam interactive arenas. Fully air-conditioned, spotlessly sanitized, and supervised by certified play marshals, it is Pattaya's ultimate family retreat.",
        "places_col1_title": "Mega Play Features",
        "places_col1_badge": "Active Fun",
        "places_col1_items": [
            ("Multi-Level Mega Playground", "Giant labyrinth of padded rope bridges, crawl tunnels, climbing nets, and interactive ball blaster zones."),
            ("Extreme & Spiral Slides", "Thrilling slides including racing mat chutes, rainbow drop slides, and transparent spiral tubes."),
            ("Ninja & Obstacle Course", "Challenging balance beams, foam pits, and agility hurdles testing reflexes and coordination.")
        ],
        "places_col2_title": "Safety & Toddler Zones",
        "places_col2_badge": "Certified Safety",
        "places_col2_items": [
            ("Little Land Toddler Zone", "Soft, cushioned sensory play area with mini slides, soft building blocks, and ball pits for kids under 100 cm."),
            ("European Safety Standards", "100% compliant with EN1176 safety regulations with certified shock-absorbing padding on all surfaces."),
            ("Parents Relaxation Cafe", "Free high-speed Wi-Fi, comfortable seating, and cafes with direct viewing angles over play areas.")
        ],
        "inclusions": [
            "Official day pass admission ticket to HarborLand Indoor Playground (single session)",
            "Access to all playground slides, climbing towers, and obstacle zones",
            "Access to Little Land toddler area for young children",
            "Accident insurance coverage"
        ],
        "exclusions": [
            "Mandatory anti-slip grip socks (available for purchase on-site for ~60 THB)",
            "Hotel transfers (convenient central Pattaya location)",
            "Food, drinks, and mall arcade tokens",
            "Other mall attractions (Laser Battle, RollerLand, JumpZ)"
        ],
        "timing_text": "Open daily from 10:00 AM to 07:00 PM.<br />Operating in flexible multi-hour play sessions.",
        "transport_text": "Harbor Pattaya Shopping Mall (Floor 7), Central Pattaya Road. Easily reached by local taxi or Songthaew.",
        "what_to_bring": "Comfortable light activewear (long pants recommended for slides) and anti-slip grip socks (or buy on-site).",
        "contact_tour_param": "HarborLand+Pattaya+Playground+Tickets",
        "faqs": [
            ("Are non-slip grip socks mandatory?", "Yes, for safety and hygiene, all children and accompanying adults must wear anti-slip silicone grip socks. You may bring your own or purchase official HarborLand socks at the check-in desk for approximately 60 THB."),
            ("Must adults accompany their children inside the playground?", "Children under 10 years of age must have an accompanying adult inside the play facility. Adults can climb through structures alongside their kids or relax in the adjacent lounge."),
            ("What other attractions are inside Harbor Mall Pattaya?", "Harbor Mall is a full entertainment center. In addition to HarborLand, it houses JumpZ Trampoline Park, RollerLand roller skating rink, Laser Battle laser tag, and Deep Climbing Gym."),
            ("Is HarborLand clean and sanitized?", "HarborLand enforces strict hygiene standards with hourly equipment wipe-downs, UV sanitization, mandatory hand sanitizing, and temperature checks upon entry.")
        ]
    },
    {
        "filename": "pattaya_golf_package_with_transfers.html",
        "title": "Pattaya Championship Golf Package with Private Transfers | Trippovention",
        "h1": "Pattaya Championship Golf Package",
        "subtitle": "18-Hole Championship Round, Siam Country Club / Chee Chan, Caddy & Buggy Included",
        "meta_desc": "Book a premier 18-hole golf package in Pattaya with Trippovention. Play top-ranked championship courses with private roundtrip transfers, motorized cart, and caddy.",
        "og_image": "https://trippovention.co.th/assets/images/packages/thailand/pattaya/sightseeingoptions/hero_pattaya_golf_championship.webp",
        "duration": "5–6 Hours (18 Holes)",
        "price": "THB 4,800",
        "price_note": "(Per Golfer)",
        "meetup": "Pattaya Hotel Pickup (Private VIP Van)",
        "overview_p1": "Pattaya is globally renowned as the 'Golf Capital of the East', boasting over 20 world-class championship golf courses designed by legends including Jack Nicklaus, Pete Dye, and Gary Player. Our comprehensive golf packages provide a seamless, VIP sporting experience for amateur and scratch golfers alike.",
        "overview_p2": "Enjoy guaranteed morning tee times at acclaimed courses such as Siam Country Club (host of the LPGA Thailand), Chee Chan Golf Resort (overlooking Buddha Mountain), or Phoenix Gold Golf & Country Club. Packages include private door-to-door luxury transport, your 18-hole green fee, motorized golf cart, and professional caddy service.",
        "places_col1_title": "Championship Courses",
        "places_col1_badge": "World-Class Layouts",
        "places_col1_items": [
            ("Siam Country Club (Old / Plantation)", "Home of the Honda LPGA Thailand, offering impeccable rolling greens and strategic bunkering."),
            ("Chee Chan Golf Resort", "Spectacular links-style layout set against the dramatic backdrop of the 109m golden laser Buddha cliff."),
            ("Phoenix Gold Golf & Country Club", "27-hole championship layout boasting scenic sea views and manicured fairways.")
        ],
        "places_col2_title": "VIP Service Inclusions",
        "places_col2_badge": "Seamless Day",
        "places_col2_items": [
            ("Private VIP Van Transfers", "Dedicated private air-conditioned vehicle collecting you from your hotel with golf bag storage."),
            ("Dedicated Personal Caddy", "Knowledgeable, friendly local caddy providing accurate yardages, green reads, and club management."),
            ("Motorized Golf Buggy", "Individual or shared motorized golf cart to navigate undulating tropical fairways effortlessly.")
        ],
        "inclusions": [
            "Guaranteed 18-hole green fee at premier championship golf course",
            "18-hole motorized golf cart (buggy)",
            "Dedicated personal caddy service",
            "Private roundtrip air-conditioned hotel transfers in Pattaya",
            "Locker room and clubhouse shower access",
            "Player insurance coverage"
        ],
        "exclusions": [
            "Caddy tip (customary minimum 400–500 THB paid directly to caddy)",
            "Golf club and shoe rentals (available at clubhouse pro-shop)",
            "Food, drinks, and clubhouse dining",
            "Driving range practice balls"
        ],
        "timing_text": "Morning Tee Times (06:30 AM – 09:30 AM) or Afternoon Tee Times (11:30 AM – 01:30 PM).<br />Daily reservations.",
        "transport_text": "Private door-to-door VIP minivan pickup and return directly from your Pattaya hotel.",
        "what_to_bring": "Appropriate golf attire (collared polo shirt, tailored shorts/trousers, soft-spike golf shoes), golf glove, balls, and cash for caddy tip.",
        "contact_tour_param": "Pattaya+Championship+Golf+Package",
        "faqs": [
            ("Can I rent golf clubs and shoes at the golf club?", "Yes, all our partner championship clubs maintain pro shops offering top-tier rental sets (Callaway, Titleist, TaylorMade) for right- and left-handed players, as well as golf shoes in all sizes."),
            ("What is the customary tip for caddies in Thailand?", "Caddies in Thailand provide exceptional service, from reading greens to marking balls and holding umbrellas. The customary cash tip is a minimum of 400 to 500 THB per 18-hole round, paid directly to your caddy at the 18th green."),
            ("What is the dress code on Pattaya golf courses?", "Standard golf etiquette applies: collared golf shirts, tailored trousers or golf shorts, soft-spike golf shoes, and socks. Jeans, t-shirts, tank tops, and sandals are strictly prohibited on the course."),
            ("Can non-golfing spouses or companions ride along?", "Yes, non-golfing companions can accompany players on the course as riders for a modest rider fee (covering insurance and buggy access).")
        ]
    }
]

def generate_tour_page(t):
    # Places col 1
    col1_items_html = "\n".join([f'                  <li><strong>{name}:</strong> {desc}</li>' for name, desc in t["places_col1_items"]])
    col2_items_html = "\n".join([f'                  <li><strong>{name}:</strong> {desc}</li>' for name, desc in t["places_col2_items"]])
    
    # Inclusions & exclusions
    inc_html = "\n".join([f'                  <li>✓ {item}</li>' for item in t["inclusions"]])
    exc_html = "\n".join([f'                  <li>✗ {item}</li>' for item in t["exclusions"]])
    
    # FAQs
    faq_items_html = []
    for idx, (q, a) in enumerate(t["faqs"]):
        open_attr = " open" if idx == 0 else ""
        faq_items_html.append(f'''            <details class="faq-item"{open_attr}>
              <summary class="faq-question"><span>{q}</span><span class="faq-chevron" aria-hidden="true">▾</span></summary>
              <div class="faq-answer"><p>{a}</p></div>
            </details>''')
    faqs_str = "\n".join(faq_items_html)
    
    # FAQ Schema
    faq_entities = []
    for q, a in t["faqs"]:
        faq_entities.append(f'''          {{
            "@type": "Question",
            "name": "{q}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{a}"
            }}
          }}''')
    faq_schema_str = ",\n".join(faq_entities)
    
    url = f"https://trippovention.co.th/packages/thailand/pattaya/{t['filename']}"
    
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
            "name": "Pattaya",
            "item": "https://trippovention.co.th/packages/thailand/pattaya/"
          }},
          {{
            "@type": "ListItem",
            "position": 5,
            "name": "Sightseeing",
            "item": "https://trippovention.co.th/packages/thailand/pattaya/sightseeing.html"
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
              <a href="index.html">Pattaya</a>
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
            <p class="subtitle">Quick answers to common questions about this Pattaya activity</p>
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
              Get the best rates on Pattaya sightseeing, activities, and private arrangements with Trippovention
            </p>
          </div>
          <div class="text-center">
            <a
              class="btn btn-lg ghost"
              href="../../../contact.html?destination=pattaya&tour={t['contact_tour_param']}"
              >📞 Request Custom Quote</a
            >
            <a
              class="btn btn-lg ghost ml-16"
              href="https://wa.me/66946934392?text=Hello,%20I%20am%20interested%20in%20booking%20the%20{t['contact_tour_param']}%20in%20Pattaya"
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
    print(f"\\nSuccessfully generated all {len(TOURS_DATA)} Pattaya sightseeing product pages!")

if __name__ == "__main__":
    main()
