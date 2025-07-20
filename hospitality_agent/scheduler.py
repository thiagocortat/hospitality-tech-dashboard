import schedule
import time
from typing import List, Dict
from .crawler import fetch_market_updates
from .classifier import classify_content

LATEST_DATA: List[Dict[str, str]] = []


def job() -> None:
    global LATEST_DATA
    items = fetch_market_updates()
    for item in items:
        item["category"] = classify_content(item)
    LATEST_DATA = items


def start_scheduler() -> None:
    schedule.every().day.at("08:00").do(job)
    job()  # initial run
    while True:
        schedule.run_pending()
        time.sleep(1)
