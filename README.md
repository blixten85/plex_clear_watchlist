# 🧹 Plex Clear Watchlist

![Build](https://github.com/blixten85/plex_clear_watchlist/actions/workflows/build.yml/badge.svg)
![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/blixten85/plex_clear_watchlist?utm_source=oss&utm_medium=github&utm_campaign=blixten85%2Fplex_clear_watchlist&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)

Delete all items from your Plex Watchlist via the Plex API.

## Setup

Get your Plex token from plex.tv → Settings → Account → Security.

## Docker Compose

```bash
PLEX_TOKEN=your-token docker compose run --rm plex-clear-watchlist --dry-run
PLEX_TOKEN=your-token docker compose run --rm plex-clear-watchlist
PLEX_TOKEN=your-token docker compose run --rm plex-clear-watchlist --limit 10
PLEX_TOKEN=your-token docker compose run --rm plex-clear-watchlist --keep 5
```

Or put `PLEX_TOKEN=your-token` in a `.env` file and just run:

```bash
docker compose run --rm plex-clear-watchlist --dry-run
```

## Docker

```bash
docker run --rm -e PLEX_TOKEN=your-token ghcr.io/blixten85/plex-clear-watchlist --dry-run
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
