
---

# Real-Time Sentiment Analysis Engine

## Overview

The **Real-Time Sentiment Analysis Engine** is a full-stack data analytics application designed to bridge the gap between live web data and actionable insights. By integrating the **NewsAPI**, the system fetches live headlines based on user-defined topics and processes them through a Natural Language Processing (NLP) pipeline to determine the public "mood" or sentiment.

This project was built with a focus on **Software Engineering best practices**, including modular architecture, defensive programming, and persistent data storage.

---

## Features

* **Live Data Integration**: Fetches real-time headlines using RESTful API calls.

* **NLP Pipeline**: Implements custom text-cleaning logic using Regular Expressions (Regex) and sentiment scoring via `TextBlob`.

* **Relational Persistence**: Automatically logs every search and result into a **SQLite** database for historical auditing.

* **Web Dashboard**: A clean, responsive UI built with **Flask** and **Bootstrap** for interactive data exploration.

* **Modular Design**: Distinct separation between data fetching, processing, and storage layers (DAO pattern).

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Backend Framework**: Flask
* **Database**: SQLite3
* **NLP Libraries**: TextBlob, RegEx
* **API Integration**: Requests, NewsAPI
* **Environment Management**: Python-Dotenv, Venv
* **Frontend**: HTML5, Jinja2, Bootstrap 5

---

## 🏗️ System Architecture

The project follows a **Modular Monolith** structure to ensure maintainability:

1. **Fetcher (`fetcher.py`)**: Handles HTTP requests and API authentication.
2. **Processor (`processor.py`)**: Normalizes text (lowercase, URL removal, special character stripping) and calculates polarity.
3. **Database Layer (`database.py`)**: Manages the SQLite connection and executes parameterized SQL queries to prevent injection.
4. **Orchestrator (`main.py`)**: Coordinates the flow of data between the fetcher and processor.
5. **Web Interface (`app.py`)**: Serves the Flask application and renders the UI.

---

## 🔧 Setup & Installation

### 1. Prerequisites

* Python 3.x installed.
* A free API Key from [NewsAPI.org](https://newsapi.org/).

### 2. Clone and Environment Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/sentiment-analyzer.git
cd sentiment-analyzer

# Create a virtual environment
python -m venv venv

# Activate the environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configuration

Create a `.env` file in the root directory:

```text
NEWS_API_KEY=your_actual_api_key_here

```

### 5. Running the Application

```bash
# Initialize the database and run the web server
python app.py

Visit `http://127.0.0.1:5000` in your browser.



##  Defensive Programming & Security

* **Environment Variables**: Private keys are never hardcoded; they are managed via `.env` and excluded from version control via `.gitignore`.
* **SQL Injection Prevention**: All database interactions use parameterized queries (`?` placeholders).
* **Error Handling**: The system utilizes `try-except` blocks to handle API timeouts and empty data returns gracefully without crashing.

---

## Future Roadmap

* [ ] Add a **Matplotlib** or **Chart.js** integration to visualize sentiment trends over time.
* [ ] Implement **Asynchronous Fetching** to speed up processing for large datasets.
* [ ] Deploy the application using **Docker** for containerized environment consistency.


