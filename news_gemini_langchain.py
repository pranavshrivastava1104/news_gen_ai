import os
from dotenv import load_dotenv
from duckduckgo_search import DDGS

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def fetch_news(topic: str, max_results: int = 5):
    """Get latest news items from DuckDuckGo."""
    items = []
    with DDGS() as ddgs:
        for r in ddgs.news(keywords=topic, max_results=max_results, timelimit="d"):
            items.append({
                "title": r.get("title", ""),
                "source": r.get("source", ""),
                "date": r.get("date", ""),
                "url": r.get("url", ""),
                "snippet": r.get("body", ""),
            })
    return items


def main():
    if not GOOGLE_API_KEY:
        print("Missing GOOGLE_API_KEY in .env")
        return

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2
    )

    prompt = ChatPromptTemplate.from_template(
        "Topic: {topic}\n\n"
        "News items:\n{items}\n\n"
        "Summarize in 5 bullet points. Use ONLY the news items. "
        "End with Sources (URLs)."
    )

    while True:
        topic = input("\nEnter topic (or 'exit'): ").strip()
        if topic.lower() == "exit":
            break

        news = fetch_news(topic)
        if not news:
            print("No news found. Try a different topic.")
            continue

        items_text = "\n".join(
            [f"- {n['title']} ({n['source']}, {n['date']})\n  {n['url']}\n  {n['snippet']}"
             for n in news]
        )

        chain = prompt | llm
        result = chain.invoke({"topic": topic, "items": items_text})
        print("\n" + result.content + "\n")


if __name__ == "__main__":
    main()
