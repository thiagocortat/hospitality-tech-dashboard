from typing import Dict
import re

CATEGORIES = {
    "Fusões e Aquisições": ["acquisition", "merge"],
    "Parcerias estratégicas": ["partnership", "alliance"],
    "Tecnologias emergentes": ["ai", "machine learning", "blockchain"],
    "Atualizações de Produto": ["release", "update", "module"],
    "Casos de uso": ["case study", "benchmark"],
}


def classify_content(item: Dict[str, str]) -> str:
    """Classify an item into one of the known categories."""
    text = f"{item.get('title', '')} {item.get('content', '')}".lower()
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if re.search(r"\b" + re.escape(kw) + r"\b", text):
                return category
    return "Outros"
