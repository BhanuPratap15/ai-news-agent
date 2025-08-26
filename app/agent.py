from .news_client import fetch_news
from .summarizer import summarize_article

def generate_news_summary(topic: str):
    """
    Fetch articles + summarize into ~50 words.
    """
    articles = fetch_news(topic)
    results = []
    for a in articles:
        text = a.get("content") or a.get("description") or ""
        summary = summarize_article(text)
        results.append({
            "title": a.get("title"),
            "summary": summary,
            "source": a.get("url")
        })
    return results
