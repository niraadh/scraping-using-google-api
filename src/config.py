import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")


# Location config (you can change these anytime)
LATITUDE = 19.0596      # Bandra, Mumbai
LONGITUDE = 72.8295
SEARCH_RADIUS = 3000   # meters
PLACE_TYPE = "Gyms"