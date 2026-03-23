# planner.py
from serpapi import GoogleSearch

# Replace with your actual SerpApi key
SERPAPI_API_KEY ="864d542ebc429ab1d9b68417f82613ec3e0fc4c8164700e095cfc42e5027f597"

def get_destination_info(destination):
    """Fetch top attractions using SerpApi"""
    params = {
        "q": f"Top attractions in {destination}",
        "api_key":SERPAPI_API_KEY,
        "hl": "en",
        "gl": "us"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Get top 5 attractions
    top_attractions = results.get("organic_results", [])[:5]

    places = []
    for item in top_attractions:
        places.append({
            "name": item.get("title", "Unknown place"),
            "link": item.get("link", "")
        })

    return places

def plan_trip(destination, budget):
    """Main planner function"""
    places = get_destination_info(destination)

    if not places:
        return {"error": "No attractions found for this destination!"}

    return {"places": places}
