from fastapi import FastAPI
from .models import NewsRequest, NewsResponse
from .agent import generate_news_summary

app = FastAPI(title="AI News Agent (Free Version)")

@app.post("/news", response_model=NewsResponse)
def get_news(req: NewsRequest):
    summaries = generate_news_summary(req.topic)
    return {"articles": summaries}
