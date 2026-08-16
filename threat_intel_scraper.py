import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.cisa.gov/news-events/cybersecurity-advisories"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(URL, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    print("=" * 60)
    print("SIMPLE THREAT INTELLIGENCE WEB SCRAPER")
    print("=" * 60)
    print("Source:", URL)
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 60)

    articles = soup.find_all("a")

    count = 0

    for article in articles:
        title = article.get_text(strip=True)
        link = article.get("href")

        if title and link and len(title) > 20:
            if link.startswith("/"):
                link = "https://www.cisa.gov" + link

            print(f"\nTitle: {title}")
            print(f"Link: {link}")

            count += 1

            if count >= 10:
                break

    print("\n" + "=" * 60)
    print(f"Collected {count} entries.")
    print("=" * 60)

except requests.exceptions.RequestException as error:
    print("Error:", error)