import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Category, Vendor, Package

def seed():
    print("Clearing old data...")
    Package.objects.all().delete()
    Vendor.objects.all().delete()
    Category.objects.all().delete()

    print("Creating the Customer's Exact 9 Curated Categories...")
    cat_data = [
        {
            "name": "Ella Signature Experiences",
            "sinhala": "ඇල්ල සුවිශේෂී අත්දැකීම්",
            "slug": "ella-signature",
            "icon": "🏔️",
            "badge": "Signature Pick",
            "order": 1
        },
        {
            "name": "Tea Trails & Mountain Discoveries",
            "sinhala": "තේ වතු සහ කඳුකර ගවේෂණ",
            "slug": "tea-trails",
            "icon": "🌿",
            "badge": "Hill Country",
            "order": 2
        },
        {
            "name": "Nature & Waterfall Escapes",
            "sinhala": "දියඇලි සහ ස්වභාවික චාරිකා",
            "slug": "nature-waterfalls",
            "icon": "💦",
            "badge": "Adventure",
            "order": 3
        },
        {
            "name": "Wildlife Encounters",
            "sinhala": "වනජීවී සෆාරි අත්දැකීම්",
            "slug": "wildlife-encounters",
            "icon": "🦌",
            "badge": "Must Experience",
            "order": 4
        },
        {
            "name": "Heritage & Cultural Discoveries",
            "sinhala": "ඓතිහාසික සහ සංස්කෘතික ගවේෂණ",
            "slug": "heritage-culture",
            "icon": "🏛️",
            "badge": "UNESCO Heritage",
            "order": 5
        },
        {
            "name": "Scenic Dining Experiences",
            "sinhala": "සුන්දර පරිසරයක භෝජන අත්දැකීම්",
            "slug": "scenic-dining",
            "icon": "🍽️",
            "badge": "Gourmet",
            "order": 6
        },
        {
            "name": "Wellness & Soulful Escapes",
            "sinhala": "සුවතා සහ ආයුර්වේද විවේකයන්",
            "slug": "wellness-escapes",
            "icon": "🧖‍♂️",
            "badge": "Pure Relaxation",
            "order": 7
        },
        {
            "name": "Romance & Special Moments",
            "sinhala": "ආදරණීය සහ විශේෂ මොහොතවල්",
            "slug": "romance-moments",
            "icon": "❤️",
            "badge": "Honeymoon & Couples",
            "order": 8
        },
        {
            "name": "Bespoke Private Journeys",
            "sinhala": "සුවිශේෂී පෞද්ගලික ප්‍රවාහන සේවා",
            "slug": "bespoke-journeys",
            "icon": "🚐",
            "badge": "VIP Private",
            "order": 9
        },
    ]

    cats = {}
    for c in cat_data:
        cat_obj = Category.objects.create(
            name=c["name"],
            sinhala_name=c["sinhala"],
            slug=c["slug"],
            icon_emoji=c["icon"],
            badge=c["badge"],
            order=c["order"]
        )
        cats[c["slug"]] = cat_obj

    print("Creating Private Vendors...")
    v_ella = Vendor.objects.create(
        name="Sunil Jayawardena",
        business_name="Ella Peak Treks & Adventures",
        service_type="Certified Mountaineer & Local Naturalist",
        phone="0774567890",
        whatsapp="94774567890",
        location="Ella / Badulla",
        bank_details="Commercial Bank - Ella Branch, A/C: 8001234567",
        private_notes="Specialist for Ella Rock, Nine Arch and secret waterfall trails. Net price Rs. 13,000 for standard tours."
    )
    v_tea = Vendor.objects.create(
        name="Pradeep Ranasinghe",
        business_name="Ceylon Highland Tea Estate Trails",
        service_type="Tea Planter & Heritage Tour Host",
        phone="0712345678",
        whatsapp="94712345678",
        location="Haputale & Nuwara Eliya",
        bank_details="Sampath Bank - Haputale, A/C: 0045678901",
        private_notes="Exclusive access to private factory estate and colonial tea bungalow high tea setups."
    )
    v_safari = Vendor.objects.create(
        name="Ruwan Priyankara",
        business_name="Yala Wilderness Trackers 4x4",
        service_type="Licensed Safari Jeep Driver & Animal Tracker",
        phone="0773344556",
        whatsapp="94773344556",
        location="Yala / Tissamaharama",
        bank_details="BOC - Tissa, A/C: 4567890123",
        private_notes="Specially modified Toyota Hilux 4x4 safari jeep with high-ground clearance and binoculars."
    )
    v_dining = Vendor.objects.create(
        name="Chef Duminda Karunaratne",
        business_name="Ella Cliffside Sky Dining & Retreats",
        service_type="Private Chef & Dining Experience Host",
        phone="0767788990",
        whatsapp="94767788990",
        location="Ella Gap, Ella",
        bank_details="HNB - Bandarawela, A/C: 0098765432",
        private_notes="Provides romantic candlelit dinners and floating breakfast trays with fresh organic ingredients."
    )
    v_wellness = Vendor.objects.create(
        name="Dr. Ashan Wickramasinghe",
        business_name="AyurVeda Sanctuary & Yoga Pavilions",
        service_type="Ayurvedic Physician & Wellness Coordinator",
        phone="0751234987",
        whatsapp="94751234987",
        location="Ella / Kandy",
        bank_details="Commercial Bank - Kandy, A/C: 8009876543",
        private_notes="Authentic traditional herbal oils, private yoga pavilions with certified instructors."
    )
    v_transport = Vendor.objects.create(
        name="Rohan Fernando",
        business_name="Lanka Royal Chauffeurs & Fleets",
        service_type="VIP Chauffeur & Fleet Operator",
        phone="0719876543",
        whatsapp="94719876543",
        location="Colombo Airport / Island-wide",
        bank_details="Commercial Bank - Negombo, A/C: 1045678901",
        private_notes="Luxury Toyota KDH Super GL Vans and Prius Sedans. English speaking, polite, fully insured."
    )

    print("Creating Curated Packages with High-Quality Royalty-Free Photos...")
    packages = [
        # 1. 🏔️ Ella Signature Experiences
        {
            "code": "EL-01",
            "cat": "ella-signature",
            "vendor": v_ella,
            "title": "Nine Arch Bridge Scenic Train View & Little Adam's Peak Sunset Hike",
            "location": "Ella, Sri Lanka",
            "duration": "Half Day (4-5 Hours)",
            "image": "https://images.unsplash.com/photo-1546708973-b339540b5162?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 18500,
            "orig_price": 23000,
            "cost_price": 13000,
            "badge": "BESTSELLER",
            "rating": 5.0,
            "reviews": 178,
            "overview": "The definitive Ella experience! Watch the iconic blue train curve along the colonial Nine Arch Bridge, followed by an easy sunset hike atop Little Adam's Peak overlooking the panoramic Ella Gap.",
            "highlights": "Guaranteed best photo spot for the passing colonial blue train\n360-degree sunset mountain panorama from Little Adam's Peak\nPrivate certified local guide with insider photography tips\nFresh King Coconut and bottled water included",
            "inclusions": "Private local trek guide, hotel pickup & drop-off in Ella, fresh king coconut & bottled water",
            "exclusions": "Personal expenses and tips",
            "featured": True
        },
        {
            "code": "EL-02",
            "cat": "ella-signature",
            "vendor": v_ella,
            "title": "Ella Rock Challenging Summit Trek via Secret Rail Track & Forest Trails",
            "location": "Ella Peak, Sri Lanka",
            "duration": "Full Morning (4.5 Hours)",
            "image": "https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 16000,
            "orig_price": 20000,
            "cost_price": 11000,
            "badge": "TOP TREK",
            "rating": 4.9,
            "reviews": 124,
            "overview": "Trek through eucalyptus groves, railway tracks, and misty cliffs up to the highest precipice in Ella. Reward yourself with breathtaking valley views that stretch all the way to the southern plains.",
            "highlights": "Reach the summit of Ella Rock for jaw-dropping cliff views\nGuided navigation through confusing forest trails safely\nStop at mountain tea stalls for authentic spiced ginger tea",
            "inclusions": "Expert mountain guide, trail permits, energy snack pack & mineral water",
            "exclusions": "Hiking boots/gear",
            "featured": True
        },

        # 2. 🌿 Tea Trails & Mountain Discoveries
        {
            "code": "TT-01",
            "cat": "tea-trails",
            "vendor": v_tea,
            "title": "Colonial Tea Factory Masterclass, Plucking Experience & High Tea Tasting",
            "location": "Nuwara Eliya / Ella",
            "duration": "3 Hours Experience",
            "image": "https://images.unsplash.com/photo-1588714477688-cf28a50e94f7?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 14500,
            "orig_price": 18500,
            "cost_price": 9500,
            "badge": "AUTHENTIC CEYLON",
            "rating": 4.9,
            "reviews": 92,
            "overview": "Wear a traditional tea-plucking basket, walk through emerald tea terraces with local estate pluckers, and discover the 150-year-old British machinery that produces Ceylon's finest Orange Pekoe tea.",
            "highlights": "Hands-on tea plucking experience in tea gardens\nExclusive factory access to withering, rolling, and drying rooms\nSignature tea tasting session of 5 premium Ceylon tea grades\nFresh scones and local treats at the estate veranda",
            "inclusions": "Factory entrance ticket, private tea sommelier guide, high tea tasting set, souvenir tea sample",
            "exclusions": "Transportation to factory (can be added with BJ-01)",
            "featured": True
        },
        {
            "code": "TT-02",
            "cat": "tea-trails",
            "vendor": v_tea,
            "title": "Lipton's Seat Sunrise Mountain Expedition & Dambatenne Tea Trail",
            "location": "Haputale & Poonagala",
            "duration": "Morning (5:30 AM - 10:00 AM)",
            "image": "https://images.unsplash.com/photo-1566833925852-c8f001c37b83?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 19500,
            "orig_price": 24000,
            "cost_price": 13500,
            "badge": "ICONIC VIEW",
            "rating": 5.0,
            "reviews": 88,
            "overview": "Stand where Sir Thomas Lipton surveyed his vast tea empire! Ascend to 1,970 meters above sea level at dawn to witness sweeping panoramic vistas across 7 Sri Lankan provinces.",
            "highlights": "Spectacular sunrise over rolling emerald tea carpets\nVisit the original bronze statue and viewpoint of Sir Thomas Lipton\nScenic descent through Dambatenne estate villages",
            "inclusions": "Private roundtrip vehicle to summit, estate permits, hot Ceylon tea & light breakfast picnic",
            "exclusions": "Personal expenses",
            "featured": False
        },

        # 3. 💦 Nature & Waterfall Escapes
        {
            "code": "NW-01",
            "cat": "nature-waterfalls",
            "vendor": v_ella,
            "title": "Diyaluma Upper Falls Secret Natural Infinity Pools Hike & Swim",
            "location": "Poonagala / Koslanda",
            "duration": "Full Day (6 Hours)",
            "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 21000,
            "orig_price": 26000,
            "cost_price": 14500,
            "badge": "NATURE WONDER",
            "rating": 5.0,
            "reviews": 145,
            "overview": "Hike to the top of Sri Lanka's second highest waterfall! Bathe in crystal-clear natural rock pools perched right at the cliff's edge, surrounded by lush tropical mountain wilderness.",
            "highlights": "Swim in natural rock infinity pools high above the valley\nCliff jump into safe, refreshing freshwater lagoons\nScenic drive through rubber and lemongrass plantations\nPicnic lunch by cascading crystal streams",
            "inclusions": "Private return transport from Ella, certified water-safety guide, packed picnic lunch, life-jackets",
            "exclusions": "Swimwear and towels",
            "featured": True
        },
        {
            "code": "NW-02",
            "cat": "nature-waterfalls",
            "vendor": v_ella,
            "title": "Secret Ravana Cascade Cave Expedition & Jungle Stream Trek",
            "location": "Ravana Wildlife Sanctuary",
            "duration": "Half Day (3.5 Hours)",
            "image": "https://images.unsplash.com/photo-1510312305653-8ed496efae75?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 14000,
            "orig_price": 18000,
            "cost_price": 9500,
            "badge": "HIDDEN GEM",
            "rating": 4.8,
            "reviews": 76,
            "overview": "Escape the tourist crowds! Follow a secret stream trail deep inside the Ravana jungle to hidden cascades and ancient caves mentioned in the ancient Ramayana legend.",
            "highlights": "Off-the-beaten-path jungle trekking with zero crowds\nNatural mineral mud bath and forest pool swim\nExplore the historic caves shrouded in mist",
            "inclusions": "Private local trekker, forest entry permits, fresh fruit skewers & mineral water",
            "exclusions": "Footwear for water walking",
            "featured": False
        },

        # 4. 🦌 Wildlife Encounters
        {
            "code": "WL-01",
            "cat": "wildlife-encounters",
            "vendor": v_safari,
            "title": "Yala National Park Golden Dawn VIP 4x4 Leopard Tracker Safari",
            "location": "Yala National Park, Block 1",
            "duration": "Morning (5:30 AM - 10:30 AM)",
            "image": "https://images.unsplash.com/photo-1557050543-4d5f4e07ef46?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 27500,
            "orig_price": 34000,
            "cost_price": 19500,
            "badge": "TOP RATED SAFARI",
            "rating": 4.9,
            "reviews": 215,
            "overview": "Track the highest leopard density in the world! Enter the park gates right at sunrise in a customized, shock-absorber 4x4 safari jeep with a veteran animal tracker.",
            "highlights": "High probability of spotting leopards, sloth bears & wild elephants\nCustomized safari vehicle with 360-degree tiered photography seats\nHigh-power binoculars and wildlife guidebooks on board\nComplimentary continental breakfast box inside park rest station",
            "inclusions": "Private 4x4 jeep hire, certified tracker fee, breakfast box, chilled refreshments",
            "exclusions": "Department of Wildlife Conservation entry ticket",
            "featured": True
        },
        {
            "code": "WL-02",
            "cat": "wildlife-encounters",
            "vendor": v_safari,
            "title": "Udawalawe Elephant Sanctuary & Orphanage Transit Home Day Safari",
            "location": "Udawalawe National Park",
            "duration": "Half Day (4 Hours)",
            "image": "https://images.unsplash.com/photo-1534188753412-3e26d0d618d6?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 22500,
            "orig_price": 28000,
            "cost_price": 15500,
            "badge": "FAMILY FAVORITE",
            "rating": 4.9,
            "reviews": 134,
            "overview": "Experience hundreds of wild Asian elephants in their natural savanna grassland habitat! Visit the Elephant Transit Home to watch playful orphaned calves being bottle-fed milk.",
            "highlights": "Guaranteed elephant herd sightings grazing around the reservoir\nObserve the milk-feeding session of baby elephants at the Transit Home\nBirdwatcher's paradise: eagles, hornbills, and peacocks in abundance",
            "inclusions": "Private 4x4 safari jeep, driver/tracker, transit home feeding pass, mineral water",
            "exclusions": "Park entry permit",
            "featured": False
        },

        # 5. 🏛️ Heritage & Cultural Discoveries
        {
            "code": "HC-01",
            "cat": "heritage-culture",
            "vendor": v_ella,
            "title": "Sigiriya 5th-Century Sky Fortress & Dambulla Golden Cave Temples",
            "location": "Cultural Triangle, Sri Lanka",
            "duration": "Full Day Private Excursion",
            "image": "https://images.unsplash.com/photo-1588598198321-9735fd52455b?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 23500,
            "orig_price": 29000,
            "cost_price": 16500,
            "badge": "UNESCO WONDER",
            "rating": 5.0,
            "reviews": 160,
            "overview": "Scale the world-famous Lion Rock of King Kashyapa, marvel at ancient frescoes, and enter the sacred gilded cave temples of Dambulla containing over 150 monumental Buddha statues.",
            "highlights": "Climb UNESCO World Heritage Sigiriya fortress with certified archaeologist\nAdmire the world-renowned Sigiriya celestial maiden frescoes\nExplore 5 sacred monastic cavern shrines at Dambulla",
            "inclusions": "Private air-conditioned car/van, expert heritage guide, cold water & towels",
            "exclusions": "Monument entrance tickets ($36 for foreigners)",
            "featured": True
        },
        {
            "code": "HC-02",
            "cat": "heritage-culture",
            "vendor": v_transport,
            "title": "Historic Galle Dutch Fort Living Ramparts & Stilt Fishermen Journey",
            "location": "Galle, South Coast",
            "duration": "Full Day (8 Hours)",
            "image": "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 19000,
            "orig_price": 24000,
            "cost_price": 13000,
            "badge": "COLONIAL CHARM",
            "rating": 4.9,
            "reviews": 105,
            "overview": "Stroll cobblestone lanes of Asia's best-preserved European fortified city. Walk the 400-year-old ocean ramparts, visit the iconic white lighthouse, and witness traditional stilt fishermen.",
            "highlights": "Walking tour inside Galle Fort's Dutch and British colonial quarters\nVisit iconic Galle Lighthouse and historic bastion ramparts\nObserve traditional stilt fishermen in Koggala with photo opportunity",
            "inclusions": "Private air-conditioned vehicle, chauffeur guide, fort walking tour, highway tolls",
            "exclusions": "Museum tickets and lunch",
            "featured": False
        },

        # 6. 🍽️ Scenic Dining Experiences
        {
            "code": "SD-01",
            "cat": "scenic-dining",
            "vendor": v_dining,
            "title": "Private Cliffside Sunset Dinner Overlooking the Breathtaking Ella Gap",
            "location": "Ella Mountain Ridge",
            "duration": "Evening (6:00 PM - 9:30 PM)",
            "image": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 19500,
            "orig_price": 25000,
            "cost_price": 13000,
            "badge": "GOURMET LUXURY",
            "rating": 5.0,
            "reviews": 86,
            "overview": "An intimate culinary experience perched on a private wooden deck above the clouds! Savor a multi-course fusion dinner crafted by a private chef as the sun sets behind misty peaks.",
            "highlights": "Exclusive private deck setup with ambient lantern lighting\nCurated 4-course menu (Choice of fresh seafood, local steaks or vegan fusion)\nComplimentary bottle of sparkling wine or fresh fruit mocktails",
            "inclusions": "Full 4-course dining menu for 2, private waiter, sparkling welcome drink, candlelit setup",
            "exclusions": "Extra alcoholic beverages",
            "featured": True
        },
        {
            "code": "SD-02",
            "cat": "scenic-dining",
            "vendor": v_dining,
            "title": "Authentic Village Hearth Cooking Masterclass & Clay Pot Rice Feast",
            "location": "Ella Countryside",
            "duration": "3 Hours (Lunch or Dinner)",
            "image": "https://images.unsplash.com/photo-1596797038530-2c107229654b?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 9500,
            "orig_price": 13000,
            "cost_price": 6000,
            "badge": "VILLAGE ROOTS",
            "rating": 4.9,
            "reviews": 112,
            "overview": "Pick organic vegetables from a village garden, scrape coconuts on traditional wooden stools, and cook 6 rich Sri Lankan curries over firewood clay hearths in a thatched village hut.",
            "highlights": "Hands-on preparation of Dhal, Pol Sambol, Jackfruit & Coconut Rotis\nLearn the health secrets of cinnamon, cardamom & curry leaves\nFeast on clay pot dishes served on traditional banana leaves",
            "inclusions": "All fresh ingredients, hands-on cooking lesson, full buffet feast, printed recipe cards",
            "exclusions": "Beverages other than king coconut",
            "featured": False
        },

        # 7. 🧖‍♂️ Wellness & Soulful Escapes
        {
            "code": "WS-01",
            "cat": "wellness-escapes",
            "vendor": v_wellness,
            "title": "Ancient Royal Ayurvedic Herbal Full-Body Rejuvenation & Shirodhara Spa",
            "location": "Ella & Kandy Sanctuaries",
            "duration": "2.5 Hours Treatment",
            "image": "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 17500,
            "orig_price": 22500,
            "cost_price": 11500,
            "badge": "HOLISTIC HEALING",
            "rating": 5.0,
            "reviews": 98,
            "overview": "Dissolve all travel fatigue with authentic Sri Lankan Ayurveda. Experience warm herbal oil body massage (Abhyanga), medicinal herbal steam bath, and the tranquil flow of Shirodhara on the third eye.",
            "highlights": "Consultation with qualified Ayurvedic physician\nFull body massage using medicinal herbal infused oils\nAuthentic Shirodhara warm herbal oil forehead drip therapy\nHerbal steam bath infused with wild medicinal leaves",
            "inclusions": "Full 2.5 hour spa therapy, doctor consultation, herbal tea & fruit refreshments, towel service",
            "exclusions": "Take-home herbal remedies",
            "featured": True
        },
        {
            "code": "WS-02",
            "cat": "wellness-escapes",
            "vendor": v_wellness,
            "title": "Sunrise Mountain Plateau Yoga, Breathwork & Tibetan Sound Bath",
            "location": "Ella Mountain Plateau",
            "duration": "2 Hours (6:30 AM - 8:30 AM)",
            "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 12500,
            "orig_price": 16000,
            "cost_price": 7500,
            "badge": "MINDFUL RETREAT",
            "rating": 4.9,
            "reviews": 64,
            "overview": "Awaken your body and mind as the sun rises over misty valleys. Guided vinyasa yoga suitable for all experience levels, followed by transformative breathwork and healing singing bowl vibrations.",
            "highlights": "Breathtaking open-air mountain yoga platform\nGuided by certified international yoga & sound therapist\nIncludes grounding herbal detox tea and fresh tropical fruits",
            "inclusions": "Premium yoga mats, meditation cushions, sound therapy session, organic detox drinks",
            "exclusions": "Comfortable workout clothes",
            "featured": False
        },

        # 8. ❤️ Romance & Special Moments
        {
            "code": "RM-01",
            "cat": "romance-moments",
            "vendor": v_dining,
            "title": "Honeymoon Candlelit Stargazer Dinner & Secret Campfire Setup",
            "location": "Ella Private Mountain Estate",
            "duration": "Evening (6:30 PM - 10:30 PM)",
            "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 28500,
            "orig_price": 36000,
            "cost_price": 19000,
            "badge": "ULTIMATE ROMANCE",
            "rating": 5.0,
            "reviews": 72,
            "overview": "Create an unforgettable milestone! An isolated mountain sanctuary decorated with hundreds of fairy lights, rose petals, private crackling campfire, and a gourmet candlelight dinner under the constellations.",
            "highlights": "Complete private seclusion with zero interruptions\nCustomized floral path and romantic teepee tent photo setup\nLive acoustic guitar serenades or curated playlist\nSignature celebration cake & chocolate fondue",
            "inclusions": "Private venue rental, full 4-course dinner for 2, celebration cake, fire pit, romantic styling",
            "exclusions": "Hard liquor (BYOB welcome with free corkage)",
            "featured": True
        },
        {
            "code": "RM-02",
            "cat": "romance-moments",
            "vendor": v_ella,
            "title": "Couple Vacation & Engagement 4K Drone & Cinematic Photoshoot",
            "location": "Nine Arch Bridge & Tea Ridges",
            "duration": "2.5 Hours Shoot",
            "image": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 26000,
            "orig_price": 32000,
            "cost_price": 18000,
            "badge": "MEMORIES FOR LIFE",
            "rating": 4.9,
            "reviews": 84,
            "overview": "Star in your own cinematic travel movie! Licensed drone pilot and portrait photographer captures breathtaking wide aerials and intimate closeups across Ella's most dramatic viewpoints.",
            "highlights": "50+ High resolution professionally edited and color-graded photos\n2 Short 4K vertical cinematic reels formatted for Instagram & TikTok\nPrivate high-speed cloud gallery delivery within 24 hours",
            "inclusions": "Pro photographer, 4K DJI drone, color grading, cloud delivery",
            "exclusions": "Outfit changes / makeup",
            "featured": False
        },

        # 9. 🚐 Bespoke Private Journeys
        {
            "code": "BJ-01",
            "cat": "bespoke-journeys",
            "vendor": v_transport,
            "title": "Colombo Airport (CMB) to Ella / Kandy VIP Chauffeur Luxury KDH Van",
            "location": "Airport / Island-wide",
            "duration": "One-Way Private Ride",
            "image": "https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 28000,
            "orig_price": 34000,
            "cost_price": 21000,
            "badge": "VIP LUXURY RIDE",
            "rating": 4.9,
            "reviews": 230,
            "overview": "Arrive in pure comfort without stress. A polished English-fluent chauffeur meets you with a personalized welcome tablet at terminal exit. Ride in a top-spec Toyota KDH Super GL van with leather captain seats.",
            "highlights": "Flight arrival monitoring: zero extra charges for delayed flights\nComplimentary high-speed onboard 4G Wi-Fi & device charging\nComplimentary expressway highway tolls and parking tickets",
            "inclusions": "Air-conditioned luxury van, professional chauffeur, fuel, expressway tolls, passenger insurance",
            "exclusions": "Driver tips (optional)",
            "featured": True
        },
        {
            "code": "BJ-02",
            "cat": "bespoke-journeys",
            "vendor": v_transport,
            "title": "Custom Multi-Day Island Chauffeur & Guided Explorer Tour",
            "location": "Island-wide Sri Lanka",
            "duration": "Flexible Multi-Day Service",
            "image": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1200&q=80",
            "sell_price": 38000,
            "orig_price": 45000,
            "cost_price": 29000,
            "badge": "ULTIMATE FREEDOM",
            "rating": 5.0,
            "reviews": 118,
            "overview": "Your personal private driver and travel companion! Craft your own route across beaches, hill country tea estates, and ancient kingdoms with complete flexibility and local knowledge.",
            "highlights": "Dedicated private hybrid sedan or luxury van at your disposal\nStop wherever and whenever you want for scenic photos and coconuts\nEnglish-speaking SLTDA certified tourist driver",
            "inclusions": "Vehicle hire, driver accommodation & meals, fuel allowance, passenger insurance",
            "exclusions": "Personal monument entry tickets",
            "featured": False
        },
    ]

    for p in packages:
        Package.objects.create(
            code=p["code"],
            category=cats[p["cat"]],
            vendor=p["vendor"],
            title=p["title"],
            location=p["location"],
            duration=p["duration"],
            image_url=p["image"],
            selling_price=p["sell_price"],
            original_price=p["orig_price"],
            vendor_cost=p["cost_price"],
            badge=p["badge"],
            rating=p["rating"],
            reviews_count=p["reviews"],
            overview=p["overview"],
            highlights=p["highlights"],
            inclusions=p["inclusions"],
            exclusions=p["exclusions"],
            is_featured=p["featured"],
            is_available=True
        )

    print(f"Successfully seeded {Category.objects.count()} curated categories and {Package.objects.count()} bespoke packages!")

if __name__ == '__main__':
    seed()
