#considered logic for cleaning and analyzing text data, such as removing 
# URLs and special characters, and using TextBlob for sentiment analysis.

import re
from textblob import TextBlob

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE) # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text) # Remove special chars
    return text.strip()

def analyze_sentiment(text):
    cleaned = clean_text(text)
    blob = TextBlob(cleaned)
    # Returns Polarity: -1 (Neg) to 1 (Pos)
    return blob.sentiment.polarity