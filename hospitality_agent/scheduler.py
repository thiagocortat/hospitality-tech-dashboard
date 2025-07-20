import schedule
import time
from typing import List, Dict
from .crawler import fetch_market_updates
from .classifier import classify_content
from .news import fetch_recent_news, summarize, detect_company, filter_last_weeks

LATEST_DATA: List[Dict[str, str]] = []
LATEST_NEWS: List[Dict[str, str]] = []


def job() -> None:
    global LATEST_DATA, LATEST_NEWS
    items = fetch_market_updates()
    for item in items:
        item["category"] = classify_content(item)
    LATEST_DATA = items

    news = fetch_recent_news()
    for item in news:
        item["summary"] = summarize(item["content"])
        item["category"] = classify_content(item)
        item["company"] = detect_company(item["content"])
    combined = news if not LATEST_NEWS else filter_last_weeks(LATEST_NEWS + news)
    # remove duplicates by title
    titles = set()
    unique_news = []
    for it in combined:
        if it["title"] not in titles:
            titles.add(it["title"])
            unique_news.append(it)
    LATEST_NEWS = unique_news

def start_scheduler() -> None:
    schedule.every().day.at("08:00").do(job)
    job()  # initial run
    while True:
        schedule.run_pending()
        time.sleep(1)
