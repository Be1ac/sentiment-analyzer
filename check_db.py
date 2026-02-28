import sqlite3

def view_data():
    conn = sqlite3.connect('sentiment_results.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM analysis_history")
        rows = cursor.fetchall()
        
        print(f"{'ID':<4} | {'Topic':<12} | {'Score':<6} | {'Headline'}")
        print("-" * 60)
        
        for row in rows:
            # row[0]=id, row[1]=topic, row[2]=headline, row[3]=score
            print(f"{row[0]:<4} | {row[1]:<12} | {row[3]:<6} | {row[2][:50]}...")
            
    except sqlite3.OperationalError:
        print("Table not found. Did you run the analysis yet?")
    finally:
        conn.close()

if __name__ == "__main__":
    view_data()