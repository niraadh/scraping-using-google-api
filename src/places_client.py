import googlemaps
from src.config import GOOGLE_MAPS_API_KEY

def get_gmaps_client():
    if not GOOGLE_MAPS_API_KEY:
        raise ValueError("Google Maps API key not found. Check .env file.")
    return googlemaps.Client(key=GOOGLE_MAPS_API_KEY)