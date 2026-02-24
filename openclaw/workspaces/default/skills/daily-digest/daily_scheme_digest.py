import sys
import requests
import feedparser
from datetime import datetime
sys.stdout.reconfigure(encoding='utf-8')
PIB_RSS_URL = "https://pib.gov.in/RssMain.aspx?ModId=6&Lang=1&Regid=3&lang=en"
BOT_TOKEN = "8644291946:AAEfxVfG7ibUkJb6uVziNoS4Vpo9p9TnsCY"
CHAT_ID = "6219599132"

def fetch_top3():
    try:
        resp = requests.get(PIB_RSS_URL, timeout=15)
        feed = feedparser.parse(resp.content)
        items = []
        for entry in feed.entries[:3]:
            items.append({
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", "")
            })
        return items
    except Exception as e:
        print(f"[ERROR] {e}")
        return None

def build_digest(items):
    lines = ["Daily Scheme Digest - " + datetime.now().strftime("%d %b %Y"), ""]
    for i, it in enumerate(items, 1):
        lines.append(f"{i}. {it['title']}")
        lines.append(f" Date: {it['published']}")
        lines.append(f" URL: {it['link']}")
        lines.append("")
    return "\n".join(lines)

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    resp = requests.post(url, data={"chat_id": CHAT_ID, "text": text}, timeout=10)
    resp.raise_for_status()
    print("[TELEGRAM] Message sent successfully.")

def main():
    items = fetch_top3()
    if not items:
        print("No updates found.")
        sys.exit(0)
    digest = build_digest(items)
    print(digest)
    send_telegram(digest)
    print("[ACTION: daily-scheme-digest sent to Telegram]")

if __name__ == "__main__":
    main()
