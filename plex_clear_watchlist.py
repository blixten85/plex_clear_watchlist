import os
import requests

PLEX_TOKEN = os.environ.get("PLEX_TOKEN", "")
if not PLEX_TOKEN:
    raise ValueError("PLEX_TOKEN environment variable not set")

BASE_URL = "https://plex.tv"

HEADERS = {
    "X-Plex-Token": PLEX_TOKEN,
    "Accept": "application/json"
}

def get_watchlist():
    url = f"{BASE_URL}/v2/watchlist"
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return r.json()

def delete_from_watchlist(rating_key):
    url = f"{BASE_URL}/v2/watchlist/{rating_key}"
    r = requests.delete(url, headers=HEADERS)
    if r.status_code == 200:
        print(f"🗑️  Tog bort {rating_key}")
    else:
        print(f"⚠️  Misslyckades ta bort {rating_key}:{r.status_code}")

def main():
    items = get_watchlist()
    total = len(items)
    print(f"📋 Hittade {total} objekt i Plex Watchlist.")

    for item in items:
        delete_from_watchlist(item['ratingKey'])

if __name__ == "__main__":
    main()
