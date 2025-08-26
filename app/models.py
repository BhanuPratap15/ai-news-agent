from pydantic import BaseModel
from typing import List

class NewsRequest(BaseModel):
    topic: str

class NewsSummary(BaseModel):
    title: str
    summary: str
    source: str

class NewsResponse(BaseModel):
    articles: List[NewsSummary]
