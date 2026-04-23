# 🧹 Plex Clear Watchlist

Delete all items from your Plex Watchlist via the Plex API.

## Setup

1. Get your Plex token from plex.tv → Settings → Account → Security
2. Export the token:

```bash
export PLEX_TOKEN="your-token-here"
```

## Usage

```bash
# See what would be deleted
python3 plex_clear_watchlist.py --dry-run

# Delete all
python3 plex_clear_watchlist.py

# Delete max 10 items
python3 plex_clear_watchlist.py --limit 10

# Keep the 5 most recent items
python3 plex_clear_watchlist.py --keep 5
```

## Requirements

- Python 3.x
- requests library (pip3 install requests)
