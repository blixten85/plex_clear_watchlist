FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY plex_clear_watchlist.py .
ENTRYPOINT ["python", "plex_clear_watchlist.py"]
