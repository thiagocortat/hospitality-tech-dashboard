import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List, Dict


USER_AGENT = "Mozilla/5.0 (compatible; HospitalityBot/1.0)"
HEADERS = {"User-Agent": USER_AGENT}


def fetch_market_updates() -> List[Dict[str, str]]:
    """Fetch sample articles from public sources.

    This function is a placeholder. In a production system it would
    crawl multiple industry websites and social channels. Here we
    simply fetch a predefined list of URLs and parse basic metadata.
    """
    sources = [
        "https://www.hospitalitynet.org/opinion/4106822.html",
        "https://www.hospitalitynet.org/news/4110183.html",
    ]
    results: List[Dict[str, str]] = []
    for url in sources:
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
            resp.raise_for_status()
        except Exception:
            continue
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.find("title").text if soup.find("title") else url
        text = " ".join(p.get_text(strip=True) for p in soup.find_all("p"))
        results.append(
            {
                "title": title,
                "content": text[:1000],
                "source": url,
                "date": datetime.utcnow().isoformat(),
            }
        )
    return results
