#connects the fetcher and processor modules to run the overall sentiment analysis workflow

from fetcher import fetch_news
from processor import analyze_sentiment
from database import init_db, save_to_db # Import our new tools

def run_analysis(topic):
    init_db() 
    articles = fetch_news(topic) # Now contains dictionaries
    
    results = []
    # Initialize our counters
    summary = {"pos": 0, "neg": 0, "neu": 0}

    for item in articles:
        score = analyze_sentiment(item['title'])
        
        # Logic for the Counter
        if score > 0.05: summary["pos"] += 1
        elif score < -0.05: summary["neg"] += 1
        else: summary["neu"] += 1
        
        # Save to Data Base (update your save_to_db to accept the date if desired)
        save_to_db(topic, item['title'], score)
        
        results.append({
            "text": item['title'], 
            "score": score, 
            "date": item['date'][:10] # We slice [:10] to get YYYY-MM-DD
        })
    
    return results, summary

if __name__ == "__main__":
    # This triggers the whole lifecycle:
    # 1. init_db() creates the table
    # 2. fetch_news() gets data from API
    # 3. analyze_sentiment() processes it
    # 4. save_to_db() writes it to SQLite
    results = run_analysis("Technology") 
    print(f"Success! Processed and saved {len(results)} headlines.")