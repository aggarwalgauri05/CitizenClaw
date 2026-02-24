#!/usr/bin/env python3
import sys
import argparse
import os
import requests
from urllib.parse import urlencode
import feedparser

CIVIC_KEYWORDS = ["scheme","yojana","government","ministry","welfare","pension","subsidy","benefit","policy","PM","CM"]
GNEWS_API_KEY_ENV = "GNEWS_API_KEY"

def contains_civic_keywords(query: str) -> bool:
    q = (query or "").lower()
    return any(k in q for k in CIVIC_KEYWORDS)

def fetch_gnews(query: str, max_results=5):
    api_key = os.environ.get(GNEWS_API_KEY_ENV)
    if not api_key:
        raise ValueError("GNews API key not set in environment variable")
    base = "https://gnews.io/api/v4/search"
    q = f"{query} Ayushman Bharat India government"
    params = {
        "q": q,
        "lang": "en",
        "country": "in",
        "max": max_results,
        "token": api_key
    }
    url = f"{base}?{ urlencode(params) }"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    articles = data.get("articles", [])[:max_results]
    results = []
    for a in articles:
        results.append({
            "title": a.get("title"),
            "source": a.get("source", {}).get("name", ""),
            "date": a.get("publishedAt", ""),
            "url": a.get("url", "")
        })
    return results

def fetch_pib_fallback():
    url = "https://pib.gov.in/RssMain.aspx?ModId=6&Lang=1&Regid=3"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    feed = feedparser.parse(resp.content)
    results = []
    for item in feed.entries[:5]:
        results.append({
            "title": item.get("title", ""),
            "source": feed.feed.get("title", "PIB"),
            "date": item.get("published", ""),
            "url": item.get("link", "")
        })
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--days", type=int, default=1)
    args = parser.parse_args()

    query = args.query
    days = max(0, int(args.days))

    if not contains_civic_keywords(query):
        print("[BLOCKED] Query not related to government/civic domain")
        sys.exit(1)

    print(f"[ALLOWED] Civic query approved: {query}")

    articles = []
    try:
        articles = fetch_gnews(query, max_results=5)
    except Exception:
        try:
            articles = fetch_pib_fallback()
        except Exception as e:
            print(f"[ERROR] Both GNews and PIB fallback failed: {e}")
            sys.exit(1)

    if not articles:
        print("[ERROR] No articles found.")
        sys.exit(1)

    for a in articles[:5]:
        print(f"Title: {a['title']}")
        print(f"Source: {a['source']}")
        print(f"Date: {a['date']}")
        print(f"URL: {a['url']}")
        print()

if __name__ == "__main__":
    main()