from transformers import pipeline

# Load Hugging Face summarizer (free model)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_article(text: str) -> str:
    """
    Summarize article into ~50 words using free model.
    """
    if not text:
        return "No content available."
    summary = summarizer(text, max_length=60, min_length=40, do_sample=False)
    return summary[0]['summary_text']
