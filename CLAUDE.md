# Text Summarizer

A Streamlit web app that summarizes text using the Anthropic Claude API.

## Structure

```
text-summarizer/
├── app.py                  # Streamlit UI entry point
├── utils/
│   ├── __init__.py
│   └── claude_client.py    # Anthropic API wrapper
├── requirements.txt
├── .env                    # API key (not committed)
└── .gitignore
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Add your Anthropic API key to `.env`:
   ```
   ANTHROPIC_API_KEY=your_key_here
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Features

- Text input area with live word count
- Summary length slider: Short (50-75 words), Medium (150-200 words), Detailed (300-400 words)
- Output word count displayed after summarization
- Graceful handling of empty input

## Model

Uses `claude-sonnet-4-6`.
