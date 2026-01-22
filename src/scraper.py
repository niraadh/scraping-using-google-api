from src.location_search import discover_restaurants

restaurants = discover_restaurants()

print(f"Found {len(restaurants)} restaurants\n")

for r in restaurants[:5]:  # show first 5
    print({
        "name": r.get("name"),
        "place_id": r.get("place_id"),
        "rating": r.get("rating"),
        "total_reviews": r.get("user_ratings_total"),
        "address": r.get("vicinity")
    })
