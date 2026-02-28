#connects the fetcher and processor modules to run the overall sentiment analysis workflow

from fetcher import fetch_news
from processor import analyze_sentiment
from database import init_db, save_to_db # Import our new tools

def run_analysis(topic):
    # Ensure the table exists before we try to save anything
    init_db() 
    
    headlines = fetch_news(topic)
    results = []
    
    for text in headlines:
        score = analyze_sentiment(text)
        
        # Save each result to our SQLite file
        save_to_db(topic, text, score)
        
        results.append({"text": text, "score": score})
    
    return results

if __name__ == "__main__":
    # This triggers the whole lifecycle:
    # 1. init_db() creates the table
    # 2. fetch_news() gets data from API
    # 3. analyze_sentiment() processes it
    # 4. save_to_db() writes it to SQLite
    results = run_analysis("Technology") 
    print(f"Success! Processed and saved {len(results)} headlines.")