# Hospital AI Assistant

## Project Description
Hospital AI Assistant is a domain-specific AI chatbot that answers only hospital-related questions using a predefined hospital knowledge base.

## Domain
Hospital

## Features
- Answers hospital-related questions
- Uses hospital-data.txt as the knowledge base
- Rejects questions outside the hospital information
- Built using Streamlit and Google Gemini API

## Technologies Used
- Python
- Streamlit
- Google Gemini API
- VS Code

## Files
- app.py - Main application
- hospital-data.txt - Hospital knowledge base
- README.md - Project documentation
- requirements.txt - Python dependencies

## Setup

1. Create a Gemini API key from Google AI Studio.

2. Open `app.py` and replace:

```python
client = genai.Client(api_key="YOUR_API_KEY")
```

with your own Gemini API key:

```python
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")
```

## How to Run

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
streamlit run app.py
```

3. Open the browser and ask hospital-related questions.
