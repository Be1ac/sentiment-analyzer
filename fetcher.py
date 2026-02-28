#Handles fetching data from the news API

import requests
import os
from dotenv import load_dotenv

load_dotenv() # Loads the API key from .env

def fetch_news(query="technology"):
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Software Engineering: Check for HTTP errors
        data = response.json()
        # We only want the titles of the articles
        return [{"title": a['title'], "date": a['publishedAt']} for a in data.get('articles', [])]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []
    
    