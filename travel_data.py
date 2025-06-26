# travel_data.py
"""
Cambodia Travel Guide Data Module
Contains all travel information, tips, and recommendations
"""

# Specialized Natural Areas
WATERFALLS = {
    "Phnom Kulen Waterfalls": {
        "location": "Siem Reap",
        "description": "Sacred mountain cascades",
        "province": "Siem Reap"
    },
    "Bou Sra Falls": {
        "location": "Mondulkiri",
        "description": "Three-tier jungle waterfall",
        "province": "Mondulkiri"
    },
    "Kbal Chhay Falls": {
        "location": "Sihanoukville",
        "description": "Multi-level swimming holes",
        "province": "Sihanoukville"
    },
    "Tatai Falls": {
        "location": "Koh Kong",
        "description": "River rapids adventure",
        "province": "Koh Kong"
    },
    "Ka Tieng Falls": {
        "location": "Ratanakiri",
        "description": "Hidden jungle cascade",
        "province": "Ratanakiri"
    },
    "Popokvil Falls": {
        "location": "Bokor",
        "description": "Mountain plateau waterfall",
        "province": "Kampot"
    }
}

WILDLIFE_SANCTUARIES = {
    "Elephant Valley Project": {
        "location": "Mondulkiri",
        "description": "Ethical elephant encounters",
        "type": "Elephant Sanctuary"
    },
    "Wildlife Alliance": {
        "location": "Koh Kong",
        "description": "Bear rescue center",
        "type": "Wildlife Rescue"
    },
    "Gibbon Spotting": {
        "location": "Various locations",
        "description": "Endangered primate observation",
        "type": "Primate Conservation"
    },
    "Bird Sanctuaries": {
        "location": "Tonle Sap",
        "description": "Migratory bird watching",
        "type": "Bird Conservation"
    },
    "Turtle Conservation": {
        "location": "Coastal areas",
        "description": "Sea turtle protection programs",
        "type": "Marine Conservation"
    }
}

# Cultural Experiences
TRADITIONAL_CRAFTS = {
    "Silk Weaving": {
        "locations": ["Takeo", "Siem Reap"],
        "description": "Traditional textile production",
        "skill_level": "Beginner friendly"
    },
    "Pottery Making": {
        "locations": ["Kampong Chhnang"],
        "description": "Ancient ceramic techniques",
        "skill_level": "Hands-on experience"
    },
    "Silver Working": {
        "locations": ["Pursat"],
        "description": "Intricate metalwork crafts",
        "skill_level": "Observation/basic"
    },
    "Stone Carving": {
        "locations": ["Pursat"],
        "description": "Marble sculpture workshops",
        "skill_level": "Guided instruction"
    },
    "Basketry": {
        "locations": ["Various provinces"],
        "description": "Traditional weaving techniques",
        "skill_level": "Beginner friendly"
    }
}

CULINARY_SPECIALTIES = {
    "Kampot Pepper": {
        "province": "Kampot",
        "description": "World's finest peppercorns",
        "type": "Spice/Seasoning"
    },
    "Kep Crab": {
        "province": "Kep",
        "description": "Fresh blue swimmer crab with pepper",
        "type": "Seafood"
    },
    "Battambang Orange": {
        "province": "Battambang",
        "description": "Sweet citrus specialty",
        "type": "Fruit"
    },
    "Siem Reap Amok": {
        "province": "Siem Reap",
        "description": "Traditional fish curry",
        "type": "Main Dish"
    },
    "Phnom Penh Street Food": {
        "province": "Phnom Penh",
        "description": "Urban culinary diversity",
        "type": "Street Food"
    }
}

# Adventure Activities
WATER_SPORTS = {
    "Kayaking": {
        "locations": ["Tatai River", "Mekong tributaries"],
        "difficulty": "Beginner to Advanced",
        "season": "Year-round"
    },
    "Snorkeling/Diving": {
        "locations": ["Sihanoukville islands"],
        "difficulty": "Beginner to Advanced",
        "season": "October to May"
    },
    "River Cruises": {
        "locations": ["Mekong", "Tonle Sap"],
        "difficulty": "Easy",
        "season": "Year-round"
    },
    "Stand-up Paddleboarding": {
        "locations": ["Calm coastal waters"],
        "difficulty": "Beginner to Intermediate",
        "season": "October to April"
    },
    "Fishing Tours": {
        "locations": ["Various waterways"],
        "difficulty": "Easy to Intermediate",
        "season": "Year-round"
    }
}

LAND_ADVENTURES = {
    "Jungle Trekking": {
        "locations": ["Cardamom Mountains", "Ratanakiri"],
        "difficulty": "Intermediate to Advanced",
        "season": "November to March"
    },
    "Mountain Biking": {
        "locations": ["Rural roads", "Temple circuits"],
        "difficulty": "Beginner to Advanced",
        "season": "November to March"
    },
    "Rock Climbing": {
        "locations": ["Kampot limestone cliffs"],
        "difficulty": "Intermediate to Advanced",
        "season": "November to March"
    },
    "Zip-lining": {
        "locations": ["Forest canopy tours"],
        "difficulty": "Easy to Intermediate",
        "season": "Year-round"
    },
    "Motorcycle Touring": {
        "locations": ["Province-to-province routes"],
        "difficulty": "Intermediate",
        "season": "November to March"
    }
}

# Travel Information
BEST_TIME_TO_VISIT = {
    "Temple Exploration": {
        "months": "November-March",
        "reason": "Cool and dry weather"
    },
    "Beach Activities": {
        "months": "December-April", 
        "reason": "Minimal rainfall"
    },
    "Waterfall Visits": {
        "months": "June-October",
        "reason": "Rainy season ensures full water flow"
    },
    "Wildlife Watching": {
        "months": "April-May, September-October",
        "reason": "Transition periods with active wildlife"
    },
    "Cultural Festivals": {
        "months": "April (Khmer New Year), October-November (Water Festival)",
        "reason": "Major cultural celebrations"
    }
}

TRANSPORTATION_OPTIONS = {
    "Domestic Flights": {
        "routes": "Phnom Penh-Siem Reap, limited coastal routes",
        "cost": "$$$$",
        "comfort": "High"
    },
    "Tourist Buses": {
        "routes": "Comfortable connections between major destinations",
        "cost": "$$",
        "comfort": "Medium-High"
    },
    "Private Taxi/Car": {
        "routes": "Flexible destinations",
        "cost": "$$$",
        "comfort": "High"
    },
    "Motorcycle": {
        "routes": "Independent travel (international license required)",
        "cost": "$",
        "comfort": "Low"
    },
    "Boat Services": {
        "routes": "River routes, island connections",
        "cost": "$$",
        "comfort": "Medium"
    },
    "Tuk-tuk": {
        "routes": "Short distances, temple tours",
        "cost": "$",
        "comfort": "Low-Medium"
    },
    "Local Bus": {
        "routes": "Budget option, limited comfort",
        "cost": "$",
        "comfort": "Low"
    }
}

ACCOMMODATION_STYLES = {
    "Luxury Resorts": {
        "locations": "Siem Reap, Sihanoukville islands",
        "price_range": "$150+",
        "amenities": "Full service, spa, fine dining"
    },
    "Boutique Hotels": {
        "locations": "Colonial buildings in major towns",
        "price_range": "$50-150",
        "amenities": "Unique character, personalized service"
    },
    "Guesthouses": {
        "locations": "Throughout Cambodia",
        "price_range": "$10-40",
        "amenities": "Budget-friendly, family-run"
    },
    "Homestays": {
        "locations": "Rural provinces",
        "price_range": "$5-25",
        "amenities": "Cultural immersion, local meals"
    },
    "Eco-lodges": {
        "locations": "National parks",
        "price_range": "$30-100",
        "amenities": "Sustainable tourism, nature access"
    },
    "Floating Hotels": {
        "locations": "Koh Kong, Tatai River",
        "price_range": "$40-120",
        "amenities": "Unique experience, water activities"
    }
}

# Activity Search Reference Guide
SEARCHABLE_ACTIVITIES = {
    "Water Sports": {
        "Kayaking": ["tatai", "river", "mekong", "beginner", "advanced", "year-round"],
        "Snorkeling/Diving": ["sihanoukville", "islands", "diving", "snorkel", "underwater", "october", "may"],
        "River Cruises": ["mekong", "tonle sap", "cruise", "boat", "easy", "relaxing"],
        "Stand-up Paddleboarding": ["paddle", "coastal", "beginner", "intermediate", "october", "april"],
        "Fishing Tours": ["fishing", "waterways", "tours", "easy", "intermediate"]
    },
    "Land Adventures": {
        "Jungle Trekking": ["jungle", "trek", "cardamom", "ratanakiri", "hiking", "intermediate", "advanced", "november", "march"],
        "Mountain Biking": ["bike", "cycling", "rural", "temple", "circuit", "beginner", "advanced"],
        "Rock Climbing": ["climbing", "kampot", "limestone", "cliffs", "intermediate", "advanced"],
        "Zip-lining": ["zipline", "canopy", "forest", "trees", "easy", "intermediate", "year-round"],
        "Motorcycle Touring": ["motorcycle", "touring", "province", "routes", "intermediate"]
    },
    "Natural Areas": {
        "Waterfalls": ["waterfall", "falls", "kulen", "bou sra", "kbal chhay", "tatai", "ka tieng", "popokvil"],
        "Wildlife Sanctuaries": ["wildlife", "elephant", "sanctuary", "bear", "gibbon", "bird", "turtle", "conservation"]
    },
    "Cultural Experiences": {
        "Traditional Crafts": ["craft", "silk", "weaving", "pottery", "silver", "stone", "carving", "basketry"],
        "Culinary Specialties": ["food", "pepper", "kampot", "crab", "kep", "orange", "battambang", "amok", "street food"]
    }
}

ACTIVITY_SEARCH_TIPS = [
    "🔍 SEARCH BY DIFFICULTY:",
    "  - 'beginner' or 'easy'",
    "  - 'intermediate'", 
    "  - 'advanced'",
    "",
    "🌍 SEARCH BY LOCATION:",
    "  - Province names: 'siem reap', 'kampot', 'koh kong'",
    "  - Features: 'river', 'mountain', 'coast', 'temple'",
    "  - Specific places: 'tatai', 'mekong', 'cardamom'",
    "",
    "🗓️ SEARCH BY SEASON:",
    "  - 'year-round' for always available",
    "  - Month names: 'november', 'march', 'october'",
    "  - Seasons: 'dry season', 'rainy season'",
    "",
    "🎯 SEARCH BY ACTIVITY TYPE:",
    "  - Water activities: 'water', 'diving', 'kayak', 'cruise'",
    "  - Land activities: 'trek', 'bike', 'climb', 'zipline'",
    "  - Cultural: 'craft', 'food', 'temple', 'tradition'",
    "  - Nature: 'waterfall', 'wildlife', 'jungle', 'sanctuary'"
]

# Utility functions
def get_all_waterfalls():
    """Return all waterfall information"""
    return WATERFALLS

def get_waterfalls_by_province(province):
    """Get waterfalls in a specific province"""
    return {name: info for name, info in WATERFALLS.items() 
            if info.get('province', '').lower() == province.lower()}

def get_activities_by_type(activity_type):
    """Get activities by type (water_sports, land_adventures)"""
    if activity_type.lower() == 'water_sports':
        return WATER_SPORTS
    elif activity_type.lower() == 'land_adventures':
        return LAND_ADVENTURES
    else:
        return {}

def get_all_available_activities():
    """Get all available activities that can be searched"""
    activities = {}
    
    # Add water sports
    for activity, info in WATER_SPORTS.items():
        activities[f"Water Sport: {activity}"] = info
    
    # Add land adventures
    for activity, info in LAND_ADVENTURES.items():
        activities[f"Land Adventure: {activity}"] = info
        
    return activities

def display_search_guide():
    """Display comprehensive search guide for users"""
    print("📋 SEARCHABLE ACTIVITIES & KEYWORDS")
    print("=" * 60)
    
    for category, activities in SEARCHABLE_ACTIVITIES.items():
        print(f"\n🏷️  {category.upper()}:")
        print("-" * 40)
        
        for activity, keywords in activities.items():
            print(f"• {activity}")
            print(f"  Keywords: {', '.join(keywords)}")
        print()
    
    print("💡 SEARCH TIPS:")
    print("-" * 40)
    for tip in ACTIVITY_SEARCH_TIPS:
        print(tip)

def list_available_activities():
    """Print all available activities in a formatted way"""
    print("🌊 AVAILABLE WATER SPORTS:")
    print("-" * 40)
    for activity, info in WATER_SPORTS.items():
        locations = ", ".join(info['locations']) if isinstance(info['locations'], list) else info['locations']
        print(f"• {activity}")
        print(f"  Locations: {locations}")
        print(f"  Difficulty: {info['difficulty']}")
        print(f"  Season: {info['season']}")
        print()
    
    print("🏔️ AVAILABLE LAND ADVENTURES:")
    print("-" * 40)
    for activity, info in LAND_ADVENTURES.items():
        locations = ", ".join(info['locations']) if isinstance(info['locations'], list) else info['locations']
        print(f"• {activity}")
        print(f"  Locations: {locations}")
        print(f"  Difficulty: {info['difficulty']}")
        print(f"  Season: {info['season']}")
        print()

def search_activities(keyword=""):
    """Search for activities containing keyword, or show all if no keyword provided"""
    
    # If no keyword provided, show all available activities
    if not keyword or keyword.strip() == "":
        print("📋 ALL AVAILABLE ACTIVITIES:")
        print("=" * 50)
        list_available_activities()
        return get_all_available_activities()
    
    results = {}
    keyword = keyword.lower()
    
    # Search in water sports
    for activity, info in WATER_SPORTS.items():
        # Check activity name and all info fields
        search_text = f"{activity} {info['locations']} {info['difficulty']} {info['season']}".lower()
        if keyword in search_text:
            results[f"Water Sport: {activity}"] = info
    
    # Search in land adventures
    for activity, info in LAND_ADVENTURES.items():
        # Check activity name and all info fields
        search_text = f"{activity} {info['locations']} {info['difficulty']} {info['season']}".lower()
        if keyword in search_text:
            results[f"Land Adventure: {activity}"] = info
    
    # Display results
    if results:
        print(f"🔍 SEARCH RESULTS FOR '{keyword.upper()}':")
        print("=" * 50)
        for activity_name, info in results.items():
            locations = ", ".join(info['locations']) if isinstance(info['locations'], list) else info['locations']
            print(f"• {activity_name}")
            print(f"  Locations: {locations}")
            print(f"  Difficulty: {info['difficulty']}")
            print(f"  Season: {info['season']}")
            print()
    else:
        print(f"❌ No activities found matching '{keyword}'")
        print("\n💡 Need help with search keywords? Use display_search_guide()")
        print("   Or call search_activities() without parameters to see all activities!")
            
    return results

def get_travel_tips():
    """Get all travel tips and information"""
    return {
        "best_time_to_visit": BEST_TIME_TO_VISIT,
        "transportation": TRANSPORTATION_OPTIONS,
        "accommodation": ACCOMMODATION_STYLES,
        "searchable_activities": SEARCHABLE_ACTIVITIES,
        "search_tips": ACTIVITY_SEARCH_TIPS
    }

def format_travel_info(category):
    """Format travel information for display"""
    info_text = ""
    
    if category == "waterfalls":
        info_text = "🏞️ WATERFALLS IN CAMBODIA 🏞️\n\n"
        for name, details in WATERFALLS.items():
            info_text += f"• {name} ({details['location']})\n"
            info_text += f"  {details['description']}\n\n"
    
    elif category == "wildlife":
        info_text = "🐘 WILDLIFE SANCTUARIES 🐘\n\n"
        for name, details in WILDLIFE_SANCTUARIES.items():
            info_text += f"• {name} - {details['location']}\n"
            info_text += f"  {details['description']}\n"
            info_text += f"  Type: {details['type']}\n\n"
    
    elif category == "crafts":
        info_text = "🎨 TRADITIONAL CRAFTS 🎨\n\n"
        for craft, details in TRADITIONAL_CRAFTS.items():
            info_text += f"• {craft}\n"
            info_text += f"  Locations: {', '.join(details['locations'])}\n"
            info_text += f"  {details['description']}\n"
            info_text += f"  Skill Level: {details['skill_level']}\n\n"
    
    elif category == "food":
        info_text = "🍽️ CULINARY SPECIALTIES 🍽️\n\n"
        for food, details in CULINARY_SPECIALTIES.items():
            info_text += f"• {food} ({details['province']})\n"
            info_text += f"  {details['description']}\n"
            info_text += f"  Type: {details['type']}\n\n"
    
    elif category == "activities":
        info_text = "🎯 ALL ACTIVITIES IN CAMBODIA 🎯\n\n"
        
        # Water Sports
        info_text += "🌊 WATER SPORTS:\n"
        for activity, details in WATER_SPORTS.items():
            locations = ", ".join(details['locations']) if isinstance(details['locations'], list) else details['locations']
            info_text += f"• {activity}\n"
            info_text += f"  Locations: {locations}\n"
            info_text += f"  Difficulty: {details['difficulty']}\n"
            info_text += f"  Season: {details['season']}\n\n"
        
        # Land Adventures
        info_text += "🏔️ LAND ADVENTURES:\n"
        for activity, details in LAND_ADVENTURES.items():
            locations = ", ".join(details['locations']) if isinstance(details['locations'], list) else details['locations']
            info_text += f"• {activity}\n"
            info_text += f"  Locations: {locations}\n"
            info_text += f"  Difficulty: {details['difficulty']}\n"
            info_text += f"  Season: {details['season']}\n\n"
        
        # Search Tips
        info_text += "💡 SEARCH TIPS:\n"
        info_text += "Use search_activities('keyword') to find specific activities:\n"
        info_text += "- By difficulty: 'beginner', 'intermediate', 'advanced'\n"
        info_text += "- By location: 'river', 'mountain', 'temple', 'coast'\n"
        info_text += "- By season: 'year-round', 'november', 'march'\n"
        info_text += "- By type: 'water', 'climbing', 'bike', 'trek'\n"
    
    return info_text

# Main function for testing
if __name__ == "__main__":
    print("Cambodia Travel Data Module")
    print("=" * 50)
    print("\n🔧 Available functions:")
    print("- get_all_waterfalls()")
    print("- get_waterfalls_by_province(province)")
    print("- get_activities_by_type('water_sports' or 'land_adventures')")
    print("- search_activities(keyword) - or search_activities() to see all")
    print("- get_all_available_activities()")
    print("- list_available_activities()")
    print("- display_search_guide() - NEW! Shows all searchable keywords")
    print("- get_travel_tips()")
    print("- format_travel_info(category)")
    
    print("\n📂 Available categories for format_travel_info:")
    print("'waterfalls', 'wildlife', 'crafts', 'food', 'activities'/'search'")
    
    print("\n" + "=" * 50)
    print("🎯 EXAMPLE USAGE:")
    print("search_activities()           # Show all activities")
    print("search_activities('beginner') # Find beginner activities")
    print("search_activities('river')    # Find river activities")
    print("search_activities('temple')   # Find temple-related activities")
    print("display_search_guide()        # Show comprehensive search help")
    
    print("\n" + "=" * 50)
    # Demo: Show search guide
    display_search_guide()