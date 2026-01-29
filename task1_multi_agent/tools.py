import os
import requests 

NEWS_API_KEY = os.getenv('NEWS_API')
ALPHA_API_KEY = os.getenv('ALPHA_VANTAGE')
GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY3')

def fetch_company_news(company: str):
    if not NEWS_API_KEY:
        return ["NEWS_API_KEY not set"]

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": company,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 3,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params, timeout=10)
    articles = response.json().get("articles", [])
    return [a["title"] for a in articles]


def fetch_stock_data(symbol: str):
    if not ALPHA_API_KEY:
        return "ALPHA_VANTAGE_KEY not set"

    url = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": ALPHA_API_KEY
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json().get("Global Quote", {})

    if not data:
        return "Stock data unavailable"

    return {
        "price": data.get("05. price"),
        "change": data.get("09. change"),
        "change_percent": data.get("10. change percent")
    }


def get_company_data(company: str):
    """
    Tool used by Data Collector Agent
    """
    return {
        "company": company,
        "recent_news": fetch_company_news(company),
        "stock_data": fetch_stock_data(company)
    }