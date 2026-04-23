import os
import requests

PLEX_TOKEN = os.environ.get("PLEX_TOKEN", "")
if not PLEX_TOKEN:
    raise ValueError("PLEX_TOKEN environment variable not set")

HEADERS = {
    "X-Plex-Token": PLEX_TOKEN,
    "Accept": "application/json"
}

# Resten av din kod här...
