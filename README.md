# 🧹 Plex Clear Watchlist

![Build](https://github.com/blixten85/plex_clear_watchlist/actions/workflows/build.yml/badge.svg)
![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/blixten85/plex_clear_watchlist?utm_source=oss&utm_medium=github&utm_campaign=blixten85%2Fplex_clear_watchlist&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)

Delete all items from your Plex Watchlist via the Plex API.

## Setup

Get your Plex token from plex.tv → Settings → Account → Security.

## Docker

```bash
# See what would be deleted
docker run --rm -e PLEX_TOKEN=your-token ghcr.io/blixten85/plex-clear-watchlist --dry-run

# Delete all
docker run --rm -e PLEX_TOKEN=your-token ghcr.io/blixten85/plex-clear-watchlist

# Delete max 10 items
docker run --rm -e PLEX_TOKEN=your-token ghcr.io/blixten85/plex-clear-watchlist --limit 10

# Keep the 5 most recent items
docker run --rm -e PLEX_TOKEN=your-token ghcr.io/blixten85/plex-clear-watchlist --keep 5
```

## Python

```bash
export PLEX_TOKEN="your-token-here"
pip3 install requests
python3 plex_clear_watchlist.py --dry-run
```

## Options

| Flag | Description |
|---|---|
| `--dry-run` | Show what would be deleted without deleting |
| `--limit N` | Delete at most N items |
| `--keep N` | Keep the N most recently added items |
