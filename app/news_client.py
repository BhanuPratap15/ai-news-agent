import requests
from .config import NEWS_API_KEY

def fetch_news(topic: str, limit: int = 3):
    """
    Fetch news articles using NewsAPI (free plan: 100 req/day).
    """
    url = f"https://newsapi.org/v2/everything?q={topic}&language=en&apiKey={NEWS_API_KEY}"
    resp = requests.get(url).json()
    return resp.get("articles", [])[:limit]
