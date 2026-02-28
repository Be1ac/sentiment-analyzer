import sqlite3
from datetime import datetime

DB_NAME = "sentiment_results.db"

def init_db():
    """Creates the database and the table if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # We create a table with columns for the search topic, the text, and the score.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            headline TEXT NOT NULL,
            sentiment_score REAL NOT NULL,
            timestamp DATETIME NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def save_to_db(topic, headline, score):
    """Inserts a new record into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Use '?' as placeholders to prevent SQL Injection (Security Best Practice)
    query = '''
        INSERT INTO analysis_history (topic, headline, sentiment_score, timestamp)
        VALUES (?, ?, ?, ?)
    '''
    cursor.execute(query, (topic, headline, score, datetime.now()))
    
    conn.commit()
    conn.close()

def get_all_history():
    """Fetches all records to display in a UI or for analysis."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM analysis_history ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows