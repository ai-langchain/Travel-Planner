import random

# Database of estimated costs for popular attractions (INR)
ATTRACTION_COSTS = {
    # Europe
    "eiffel tower": 2000,
    "louvre museum": 2500,
    "notre dame": 0,  # Free
    "colosseum": 1800,
    "vatican city": 2000,
    "big ben": 0,  # Free to view
    "london eye": 3500,
    "british museum": 0,  # Free
    "sagrada familia": 3000,
    "park guell": 1000,
    
    # Asia
    "taj mahal": 1500,
    "jaipur palaces": 1000,
    "bali temples": 500,
    "tokyo tower": 1200,
    "mount fuji": 0,  # Free viewing
    "great wall": 800,
    "angkor wat": 2500,
    
    # Americas
    "statue of liberty": 2500,
    "central park": 0,  # Free
    "times square": 0,  # Free
    "golden gate bridge": 0,  # Free
    "machu picchu": 4000,
    
    # Default
    "default": 1000
}

def estimate_attraction_cost(attraction_name):
    """Estimate cost for an attraction based on name"""
    name_lower = attraction_name.lower()
    
    # Check if attraction is in our database
    for key, cost in ATTRACTION_COSTS.items():
        if key in name_lower:
            return cost
    
    # If not found, return default cost with some variation
    return ATTRACTION_COSTS["default"] + random.randint(-500, 500)

def calculate_daily_budget(total_budget, num_days):
    """Calculate budget per day based on total budget and number of days"""
    # Reserve 30% for accommodation and food
    attraction_budget = total_budget * 0.7
    daily_budget = attraction_budget / num_days
    return daily_budget

def optimize_itinerary(places, total_budget):
    """
    Create optimized itinerary based on budget
    """
    if not places:
        return []
    
    # Assign estimated costs to each place
    for place in places:
        place["cost"] = estimate_attraction_cost(place["name"])
    
    # Calculate daily budget based on number of attractions
    num_days = len(places)
    daily_budget = calculate_daily_budget(total_budget, num_days)
    
    itinerary = []
    total_attraction_cost = 0
    
    for day, place in enumerate(places, 1):
        attraction_cost = place["cost"]
        total_attraction_cost += attraction_cost
        
        # Check if we're exceeding budget
        is_over_budget = total_attraction_cost > (total_budget * 0.7)
        
        itinerary.append({
            "day": day,
            "place": place["name"],
            "cost": attraction_cost,
            "is_over_budget": is_over_budget,
            "daily_allocation": round(daily_budget, 2)
        })
    
    return itinerary

def create_itinerary(places, total_budget=50000):
    """
    Create itinerary with cost estimation
    """
    return optimize_itinerary(places, total_budget)
