# Real-Time Sentiment Analysis Engine

## Overview 

The **Real-Time Sentiment Analysis Engine** is a full-stack data analytics application designed to bridge the gap between live web data and actionable insights. By integrating the **NewsAPI**, the system fetches live headlines based on user-defined topics and processes them through a Natural Language Processing (NLP) pipeline to determine the public "mood" or sentiment.

---

## Project Overview

This is a full-stack NLP (Natural Language Processing) application that aggregates live news via **NewsAPI**, performs sentiment analysis using **TextBlob**, and persists data in a **SQLite** relational database.

The project was developed following the **Software Development Life Cycle (SDLC)**, emphasizing modular architecture, automated unit testing, and continuous deployment.

---




## Key Features

* **Live News Fetching:** Real-time data retrieval filtered by user-defined topics.

* **NLP Pipeline:** Text cleaning (Regex) and Polarity scoring (-1.0 to 1.0).

* **Data Aggregation:** A dashboard summary showing counts of Positive, Negative, and Neutral results.

* **Relational Persistence:** Historical logging of all searches into an ACID-compliant SQLite database.

* **Responsive UI:** A modern dashboard built with Flask and Bootstrap 5.

---






## Tech Stack

* **Backend:** Python 3.10+, Flask (Web Server)
* **NLP:** TextBlob, Regex (Regular Expressions)
* **Database:** SQLite3
* **Testing:** Pytest (Unit Testing)
* **DevOps:** GitHub Actions (CI), Render (CD), Gunicorn (Production Server)

---

## Testing & Quality Assurance (SDLC)

To ensure reliability, the project includes a comprehensive suite of **Unit Tests**. We verify the "Units" of logic in isolation to prevent regressions.

**Tests cover:**

1. **Text Sanitization:** Ensuring URLs and special characters are stripped before analysis.
2
. **Sentiment Accuracy:** Verifying that positive/negative/neutral strings return correct polarity ranges.

3. **Edge Cases:** Handling empty strings and numerical data gracefully.


**Run tests locally:**
```bash
pip install pytest
pytest

```

---

## Database Schema

The application utilizes an internal SQLite database to track historical analysis:

| Column       |   Type       | Description                  |
---------------|--------------|------------------------------|
| `id`         |   INTEGER    | Primary Key (Auto-increment) |
| `topic`      |   TEXT       | The search keyword           |
| `headline`   |   TEXT       | The news title analyzed      |
| `score`      |   REAL       | Polarity score (-1.0 to 1.0) |
| `timestamp`  |   DATETIME   | Time of analysis             |

---

## Setup & Installation

1. **Clone the Repo:** `git clone https://github.com/YOUR_USERNAME/repo.git`
2. **Environment:** Create a `venv` and run `pip install -r requirements.txt`.
3. **API Key:** Create a `.env` file and add `NEWS_API_KEY=your_key_here`.
4. **Launch:** Run `python app.py` and visit `localhost:5000`.

---

## CI/CD Workflow

* **Continuous Integration:** Every `git push` triggers **GitHub Actions** to run the `pytest` suite.
* **Continuous Deployment:** Upon successful testing, the code is automatically deployed to **Render**.

