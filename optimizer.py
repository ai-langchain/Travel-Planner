# optimizer.py
def create_itinerary(places):
    """
    Simple itinerary generator
    """
    itinerary = []
    day = 1
    for p in places:
        itinerary.append({
            "day": day,
            "place": p["name"],
            "cost": p.get("cost", 0)
        })
        day += 1
    return itinerary