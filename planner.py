from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variable
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY", "864d542ebc429ab1d9b68417f82613ec3e0fc4c8164700e095cfc42e5027f597")

def get_destination_info(destination):
    """Fetch top attractions using SerpApi"""
    params = {
        "q": f"Top attractions in {destination}",
        "api_key": SERPAPI_API_KEY,
        "hl": "en",
        "gl": "us"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Get top 10 attractions
    top_attractions = results.get("organic_results", [])[:10]

    places = []
    for item in top_attractions:
        places.append({
            "name": item.get("title", "Unknown place"),
            "link": item.get("link", "")
        })

    return places
