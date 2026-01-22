import time
from src.places_client import get_gmaps_client
from src.config import LATITUDE, LONGITUDE, SEARCH_RADIUS, PLACE_TYPE


def discover_restaurants():
    gmaps = get_gmaps_client()
    location = (LATITUDE, LONGITUDE)

    all_restaurants = []

    response = gmaps.places_nearby(
        location=location,
        radius=SEARCH_RADIUS,
        type=PLACE_TYPE
    )

    all_restaurants.extend(response.get("results", []))

    # Handle pagination (Google requires delay)
    while "next_page_token" in response:
        time.sleep(2)
        response = gmaps.places_nearby(
            page_token=response["next_page_token"]
        )
        all_restaurants.extend(response.get("results", []))

    return all_restaurants
