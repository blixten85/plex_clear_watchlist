# 🧹 Plex Clear Watchlist
![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/blixten85/plex_clear_watchlist?utm_source=oss&utm_medium=github&utm_campaign=blixten85%2Fplex_clear_watchlist&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)

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
