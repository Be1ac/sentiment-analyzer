import pytest
from processor import clean_text, analyze_sentiment

# ==========================================================
# TEST SUITE 1: DATA PRE-PROCESSING (Sanitization)
# ==========================================================

def test_clean_text_removes_urls():
    """
    SDLC Requirement: Noise reduction.
    Verifies that URLs are stripped to prevent them from skewing sentiment scores.
    """
    input_text = "Check this out http://example.com/news"
    # Note: We expect lowercase as part of our normalization process
    expected = "check this out"
    assert clean_text(input_text) == expected

def test_clean_text_removes_special_chars():
    """
    Ensures that punctuation and symbols are removed, leaving only valid words.
    """
    input_text = "Hello!!! @World #Python"
    expected = "hello world python"
    assert clean_text(input_text) == expected

# ==========================================================
# TEST SUITE 2: SENTIMENT ANALYSIS (NLP Accuracy)
# ==========================================================

def test_analyze_sentiment_positive():
    """
    Verifies that 'Positive' lexicons result in a polarity score > 0.
    """
    text = "The economy is showing excellent growth"
    score = analyze_sentiment(text)
    assert score > 0

def test_analyze_sentiment_negative():
    """
    Verifies that 'Negative' lexicons result in a polarity score < 0.
    """
    text = "The stock market is crashing and terrible"
    score = analyze_sentiment(text)
    assert score < 0

def test_sentiment_threshold_logic():
    """
    Tests the threshold used in our UI (0.05).
    Ensures that neutral-leaning text doesn't accidentally trigger a 'Positive' badge.
    """
    neutral_text = "The table is made of wood."
    score = analyze_sentiment(neutral_text)
    # Most factual statements should fall within the neutral boundary (-0.05 to 0.05)
    assert -0.05 <= score <= 0.05

# ==========================================================
# TEST SUITE 3: DEFENSIVE PROGRAMMING (Edge Cases)
# ==========================================================

def test_clean_text_empty_input():
    """
    Ensures the application handles empty strings without crashing.
    """
    assert clean_text("") == ""

def test_clean_text_only_numbers():
    """
    Checks how the processor handles strings containing no letters.
    """
    input_text = "12345 !!!"
    # Based on Regex [^a-zA-Z\s], this should result in an empty string
    assert clean_text(input_text) == ""

def test_processor_handles_none():
    """
    Verifies the system's resilience against NoneType inputs.
    """
    with pytest.raises(Exception):
        # We expect an error, but we test to see how the system reacts
        analyze_sentiment(None)