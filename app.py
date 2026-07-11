import streamlit as st
from google import genai

# Paste your Gemini API Key here
client = genai.Client(api_key="YOUR_API_KEY_HERE")

st.set_page_config(page_title="Hospital AI Assistant")

st.title("🏥 Hospital AI Assistant")
with open("hospital_data.txt", "r", encoding="utf-8") as file:
    hospital_data = file.read()
question = st.text_input("Ask your hospital-related question")

if question:
    prompt = f"""
You are the AI Assistant of ABC Hospital.

STRICT RULES:
- Answer ONLY using the Hospital Information below.
- NEVER use your own knowledge.
- If the answer is not present in the Hospital Information, reply exactly:
"Sorry, this information is not available in the hospital database."

Hospital Information:
{hospital_data}

Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="models/gemini-3.5-flash",
            contents=prompt
        )

        st.write("### Answer")
        st.write(response.text)

    except Exception as e:
        st.error(f"Error: {e}")