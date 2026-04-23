#!/usr/bin/env python3
import os
import sys
import argparse
import requests
from typing import List, Dict, Optional

# --- Configuration ---
PLEX_TOKEN = os.environ.get("PLEX_TOKEN", "")
if not PLEX_TOKEN:
    print("❌ Error: PLEX_TOKEN environment variable not set", file=sys.stderr)
    print("   Run: export PLEX_TOKEN='your-plex-token'", file=sys.stderr)
    sys.exit(1)

BASE_URL = "https://plex.tv"
WATCHLIST_URL = f"{BASE_URL}/api/v2/user/watchlist"
HEADERS = {
    "X-Plex-Token": PLEX_TOKEN,
    "Accept": "application/json"
}

# --- Functions ---
def get_watchlist() -> List[Dict]:
    """Hämta alla items från Plex Watchlist med paginering."""
    items = []
    page = 1
    page_size = 100
    
    while True:
        params = {"page": page, "pageSize": page_size, "sort": "addedAt:asc"}
        response = requests.get(WATCHLIST_URL, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        
        container = data.get("MediaContainer", {})
        page_items = container.get("Metadata", [])
        total_size = container.get("totalSize", 0)
        
        items.extend(page_items)
        
        if len(items) >= total_size or not page_items:
            break
        page += 1
    
    return items

def delete_from_watchlist(rating_key: str, dry_run: bool = False) -> bool:
    """Ta bort ett item från Watchlist."""
    if dry_run:
        print(f"  [DRY RUN] Would delete: {rating_key}")
        return True
    
    url = f"{WATCHLIST_URL}/{rating_key}"
    response = requests.delete(url, headers=HEADERS)
    
    if response.status_code == 200:
        print(f"  🗑️  Deleted: {rating_key}")
        return True
    else:
        print(f"  ⚠️  Failed to delete {rating_key}: HTTP {response.status_code}", file=sys.stderr)
        return False

def get_item_title(item: Dict) -> str:
    """Hämta titel från ett watchlist-item."""
    return item.get("title", item.get("guid", "Unknown"))

def main():
    parser = argparse.ArgumentParser(description="Clear your Plex Watchlist")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be deleted without actually deleting")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of items to delete (0 = all)")
    parser.add_argument("--keep", type=int, default=0, help="Keep the N most recent items")
    args = parser.parse_args()
    
    print("📋 Fetching Plex Watchlist...")
    
    try:
        items = get_watchlist()
    except requests.RequestException as e:
        print(f"❌ Failed to fetch watchlist: {e}", file=sys.stderr)
        sys.exit(1)
    
    total = len(items)
    
    if total == 0:
        print("✅ Watchlist is already empty!")
        return
    
    # Behåll de senaste om --keep är satt
    if args.keep > 0 and args.keep < total:
        items = items[:-args.keep]
    
    # Begränsa antal om --limit är satt
    if args.limit > 0 and args.limit < len(items):
        items = items[:args.limit]
    
    delete_count = len(items)
    
    if args.dry_run:
        print(f"🔍 DRY RUN: {delete_count} of {total} items would be deleted")
    else:
        print(f"🗑️  Deleting {delete_count} of {total} items...")
    
    success = 0
    failed = 0
    
    for item in items:
        title = get_item_title(item)
        rating_key = item.get("ratingKey", "")
        
        if args.dry_run:
            print(f"  [DRY RUN] Would delete: {title}")
            success += 1
        else:
            if delete_from_watchlist(rating_key):
                success += 1
            else:
                failed += 1
    
    print(f"\n✅ Done! Deleted: {success}, Failed: {failed}")

if __name__ == "__main__":
    main()
