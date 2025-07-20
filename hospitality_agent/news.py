import re
from datetime import datetime, timedelta
from typing import List, Dict


COMPANIES = [
    "Oracle Hospitality",
    "Omnibees",
    "Beonprice",
    "SiteMinder",
    "Cloudbeds",
]


SAMPLE_NEWS = [
    {
        "title": "Cloudbeds lança novo recurso de IA",
        "content": "A Cloudbeds anunciou hoje um novo recurso de IA para otimizar reservas.",
        "source": "https://example.com/cloudbeds-ai",
        "date": datetime.utcnow().isoformat(),
    },
    {
        "title": "Parceria entre Omnibees e Beonprice",
        "content": "Omnibees firmou parceria com a Beonprice para integração de tarifas.",
        "source": "https://example.com/parceria-omnibees-beonprice",
        "date": datetime.utcnow().isoformat(),
    },
]


def fetch_recent_news() -> List[Dict[str, str]]:
    """Return sample recent news items.

    In a real implementation this would crawl reliable sources using
    Agno Marketing Agent. Network access is restricted here, so we
    return predefined data.
    """
    return SAMPLE_NEWS


def summarize(text: str) -> str:
    """Generate a naive single bullet summary from the text."""
    sentence = re.split(r"(?<=[.!?]) +", text.strip())[0]
    return f"- {sentence}"


def detect_company(text: str) -> str:
    for company in COMPANIES:
        if company.lower() in text.lower():
            return company
    return "Outras"


def filter_last_weeks(items: List[Dict[str, str]], weeks: int = 2) -> List[Dict[str, str]]:
    limit = datetime.utcnow() - timedelta(weeks=weeks)
    result = [item for item in items if datetime.fromisoformat(item["date"]) >= limit]
    return result
